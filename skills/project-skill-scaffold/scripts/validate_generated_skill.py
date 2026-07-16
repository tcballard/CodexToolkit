#!/usr/bin/env python3
"""Validate a generated project orchestration Skill and its repository contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


REQUIRED = [
    "SKILL.md", "agents/openai.yaml", "references/project-map.md", "references/milestone-map.md",
    "references/repository-contract.md", "references/source-manifest.json",
    "scripts/inspect_project_state.py", "scripts/validate_project_skill.py",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--skill", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(); repo = args.repo.resolve(); skill = args.skill.resolve()
    failures: list[str] = []; warnings: list[str] = []
    for relative in REQUIRED:
        if not (skill / relative).is_file(): failures.append(f"missing required file: {relative}")
    try:
        manifest = json.loads((skill / "references/source-manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        manifest = {}; failures.append(f"invalid source manifest: {error}")
    if manifest.get("schema_version") != "1.0": failures.append(f"unsupported schema: {manifest.get('schema_version')}")
    managed = manifest.get("managed_files", [])
    if sorted(managed) != sorted(REQUIRED): failures.append("managed_files does not match the minimal generated contract")
    for relative, expected in manifest.get("generated_hashes", {}).items():
        path = skill / relative
        if not path.is_file(): failures.append(f"generated file missing: {relative}")
        elif sha256(path) != expected: warnings.append(f"generated file has hand edits: {relative}")
    for source in manifest.get("sources", []):
        path = repo / source.get("path", "")
        if source.get("required") and not path.is_file(): failures.append(f"required source missing: {source.get('path')}")
        elif path.is_file() and source.get("sha256") != sha256(path): failures.append(f"authoritative source hash changed: {source.get('path')}")
    milestones = manifest.get("milestones", [])
    identifiers = [m.get("id") for m in milestones if isinstance(m, dict)]
    if not identifiers or len(identifiers) != len(set(identifiers)) or None in identifiers: failures.append("milestone IDs must be present and unique")
    known = set(identifiers)
    for milestone in milestones:
        missing = [key for key in ("id", "title", "goal") if not str(milestone.get(key, "")).strip()]
        missing += [key for key in ("entry", "evidence", "exit") if not isinstance(milestone.get(key), list) or not milestone.get(key)]
        if missing: failures.append(f"milestone {milestone.get('id')} missing contract fields: {missing}")
        unknown = set(milestone.get("prerequisites", [])) - known
        if unknown: failures.append(f"milestone {milestone.get('id')} has unknown prerequisites: {sorted(unknown)}")
    skill_text = (skill / "SKILL.md").read_text(encoding="utf-8") if (skill / "SKILL.md").is_file() else ""
    match = re.search(r"\A---\nname: (build-[a-z0-9-]+)\ndescription: .+?\n---\n", skill_text, re.DOTALL)
    if not match or match.group(1) != manifest.get("skill_slug"): failures.append("SKILL.md frontmatter does not match manifest slug")
    transient_patterns = {
        "commit SHA": r"\b[0-9a-f]{40}\b", "installed plugin version": r"\bv\d+\.\d+\.\d+\b",
        "relative deadline": r"\b(today|tomorrow|next week)\b", "embedded completion": r"\bmilestone\s+[A-Za-z0-9_-]+\s+(?:is\s+)?complete\b",
    }
    for label, pattern in transient_patterns.items():
        if re.search(pattern, skill_text, re.IGNORECASE): failures.append(f"SKILL.md contains transient {label}")
    references = re.findall(r"\]\(([^)]+)\)", skill_text)
    for reference in references:
        if "://" not in reference and not (skill / reference).is_file(): failures.append(f"SKILL.md reference does not resolve: {reference}")
    script_results = []
    for relative, extra in (("scripts/validate_project_skill.py", ["--repo", str(repo), "--skill", str(skill)]),
                            ("scripts/inspect_project_state.py", ["--repo", str(repo)])):
        path = skill / relative
        if path.is_file():
            run = subprocess.run([sys.executable, str(path), *extra], text=True, capture_output=True, check=False)
            script_results.append({"script": relative, "exit_code": run.returncode, "stdout": run.stdout.strip(), "stderr": run.stderr.strip()})
            if relative.endswith("validate_project_skill.py") and run.returncode != 0: failures.append("generated validator failed")
            if relative.endswith("inspect_project_state.py") and run.returncode not in (0, 1): failures.append("generated state inspector could not run")
    result = {"valid": not failures, "skill": str(skill), "failures": failures, "warnings": warnings, "script_results": script_results}
    rendered = json.dumps(result, indent=2, sort_keys=True); print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__": raise SystemExit(main())
