#!/usr/bin/env python3
"""Run deterministic mechanical checks for a proposed Git contribution."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


SECRET_NAMES = re.compile(
    r"(^|/)(\.env($|\.)|id_(rsa|dsa|ecdsa|ed25519)$|credentials\.json$|secrets?\.[^/]+$)|\.(key|p12|pfx)$",
    re.IGNORECASE,
)
SECRET_EXCEPTIONS = {".env.example", ".env.sample", ".env.template"}


def run(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result


def nul_paths(result: subprocess.CompletedProcess[str]) -> set[str]:
    return {item for item in result.stdout.split("\0") if item}


def resolve_base(repo: Path, requested: str | None) -> tuple[str, str]:
    candidates = [requested] if requested else []
    if not requested:
        symbolic = run(repo, "symbolic-ref", "--quiet", "refs/remotes/origin/HEAD", check=False)
        if symbolic.returncode == 0:
            candidates.append(symbolic.stdout.strip().removeprefix("refs/remotes/"))
        candidates.extend(["origin/main", "origin/master", "main", "master"])
    for candidate in candidates:
        if not candidate:
            continue
        resolved = run(repo, "rev-parse", "--verify", f"{candidate}^{{commit}}", check=False)
        if resolved.returncode == 0:
            return candidate, resolved.stdout.strip()
    raise RuntimeError("Could not resolve the intended base; pass --base explicitly.")


def whitespace_findings(repo: Path, base: str) -> list[str]:
    findings: list[str] = []
    commands = (
        ("diff", "--check", f"{base}...HEAD"),
        ("diff", "--check"),
        ("diff", "--cached", "--check"),
    )
    for args in commands:
        result = run(repo, *args, check=False)
        if result.stdout.strip():
            findings.extend(result.stdout.strip().splitlines())
    return sorted(set(findings))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit mechanical PR readiness")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--base", help="intended base ref, for example origin/main")
    parser.add_argument("--max-file-bytes", type=int, default=1_000_000)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    if args.max_file_bytes < 1:
        print("--max-file-bytes must be at least 1", file=sys.stderr)
        return 2
    try:
        root = Path(run(repo, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
        base, base_sha = resolve_base(root, args.base)
        branch = run(root, "branch", "--show-current").stdout.strip()
        head_sha = run(root, "rev-parse", "HEAD").stdout.strip()
        committed = nul_paths(run(root, "diff", "--name-only", "-z", f"{base}...HEAD"))
        staged = nul_paths(run(root, "diff", "--cached", "--name-only", "-z"))
        unstaged = nul_paths(run(root, "diff", "--name-only", "-z"))
        untracked = nul_paths(run(root, "ls-files", "--others", "--exclude-standard", "-z"))
        conflicted = sorted(nul_paths(run(root, "diff", "--name-only", "--diff-filter=U", "-z")))
    except (OSError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    changed = sorted(committed | staged | unstaged | untracked)
    suspicious_names: list[str] = []
    oversized: list[dict[str, int | str]] = []
    conflict_markers: list[str] = []
    symlinks: list[str] = []
    for relative in changed:
        path = root / relative
        if path.name.lower() not in SECRET_EXCEPTIONS and SECRET_NAMES.search(relative):
            suspicious_names.append(relative)
        if path.is_symlink():
            symlinks.append(relative)
            continue
        if not path.is_file():
            continue
        size = path.stat().st_size
        if size > args.max_file_bytes:
            oversized.append({"path": relative, "bytes": size})
        if size <= 2_000_000:
            data = path.read_bytes()
            if b"\0" not in data:
                text = data.decode("utf-8", errors="replace")
                if re.search(r"^<<<<<<< .+$", text, re.MULTILINE) and re.search(
                    r"^>>>>>>> .+$", text, re.MULTILINE
                ):
                    conflict_markers.append(relative)

    local_base = base.removeprefix("origin/")
    blockers: list[str] = []
    warnings: list[str] = []
    if not branch:
        blockers.append("HEAD is detached.")
    if branch in {"main", "master", base, local_base}:
        blockers.append("The proposed head is the target default/base branch.")
    if not changed:
        blockers.append("No proposed changes were found against the selected base.")
    if conflicted or conflict_markers:
        blockers.append("Unresolved merge conflict state or markers were found.")
    whitespace = whitespace_findings(root, base)
    if whitespace:
        blockers.append("Git reported whitespace errors.")
    if suspicious_names:
        blockers.append("Changed paths include filenames commonly used for secrets.")
    if oversized:
        warnings.append("One or more changed files exceed the configured size threshold.")
    if symlinks:
        warnings.append("One or more changed paths are symbolic links and require manual review.")
    if staged or unstaged or untracked:
        warnings.append("The worktree contains uncommitted proposed changes.")

    commits_ahead = int(run(root, "rev-list", "--count", f"{base}..HEAD").stdout.strip())
    result = {
        "repository": str(root),
        "base": {"ref": base, "sha": base_sha},
        "head": {"branch": branch or None, "sha": head_sha, "commits_ahead": commits_ahead},
        "changed_paths": changed,
        "committed_paths": sorted(committed),
        "staged_paths": sorted(staged),
        "unstaged_paths": sorted(unstaged),
        "untracked_paths": sorted(untracked),
        "conflicted_paths": conflicted,
        "conflict_marker_paths": sorted(conflict_markers),
        "whitespace_findings": whitespace,
        "suspicious_secret_filenames": sorted(suspicious_names),
        "oversized_files": oversized,
        "symbolic_links": sorted(symlinks),
        "warnings": warnings,
        "blockers": blockers,
        "mechanical_preflight_passed": not blockers,
        "note": "This does not validate repository policy, provenance, correctness, tests, or remote PR state.",
    }
    print(json.dumps(result, indent=2))
    return 0 if not blockers else 1


if __name__ == "__main__":
    raise SystemExit(main())
