#!/usr/bin/env python3
"""Generate a lean project orchestration Skill or a non-destructive refresh candidate."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

from inspect_scaffold_inputs import inspect


SCHEMA = "1.0"
MANAGED = [
    "SKILL.md", "agents/openai.yaml", "references/project-map.md",
    "references/milestone-map.md", "references/repository-contract.md",
    "references/source-manifest.json", "scripts/inspect_project_state.py",
    "scripts/validate_project_skill.py",
]


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render(template: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    if "{{" in template:
        raise ValueError("unresolved template placeholder")
    return template


def write(path: Path, content: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    if executable:
        path.chmod(path.stat().st_mode | 0o111)


def generated_skill_md(config: dict) -> str:
    slug = config["skill_slug"]
    project = config["project_name"]
    return f'''---
name: {slug}
description: Orchestrate fresh and resumed implementation sessions for {project} from its authoritative repository sources, milestone contracts, invariants, and current evidence. Use when starting, resuming, reviewing, testing, or handing off work on {project}. Do not use as a replacement for the project specification, implementation specialists, verified tests, decision records, or repository delivery rules.
---

# Build {project}

Reconstruct project truth before selecting work. Read [project-map.md](references/project-map.md), [repository-contract.md](references/repository-contract.md), and [milestone-map.md](references/milestone-map.md). Do not copy or reinterpret the authoritative specification.

## Start every session

1. Read repository instructions and inspect branch/worktree state.
2. Run `python3 scripts/inspect_project_state.py --repo /path/to/repository`.
3. Resolve every reported stale source or status conflict before implementation.
4. Re-open the authoritative sources named in the project map.
5. Treat the reported next milestone as a candidate. Re-verify its entry criteria and acceptance evidence.
6. Choose one bounded slice whose finish evidence can be produced in this session.

Requirements, observed implementation, documented status, inferences, unknowns, and future work are separate facts. A filename never proves milestone completion. Never encode the current branch, commit, installed plugin version, or relative deadline as permanent project truth.

## Route implementation

Use the specialist routes and fallbacks in the repository contract. Specialist Skills own technical implementation details; this Skill owns authority, sequencing, project invariants, and evidence. If a required specialist is unavailable and its fallback is insufficient, stop with the exact blocker.

## Implement and verify

Preserve invariants and non-goals. Implement only the chosen slice. Run the milestone's named checks plus repository-required validation. Record commands and exact outcomes; do not convert an expected CI result, log entry, or plausible file into passing evidence.

When documented progress conflicts with repository evidence, report both and use the less optimistic state until re-verified or decided by the owner.

## Finish

Return the bounded outcome, files changed, verification commands/results, unresolved failures, decisions or deviations, milestone evidence state, and the exact next candidate slice. Update an authorized project log/status source separately; never rewrite this orchestration Skill merely to record transient completion.

For repository delivery, follow the repository contract and authorized publishing workflow. Never commit directly to the default branch and never create a ceremonial issue.
'''


STATE_INSPECTOR = r'''#!/usr/bin/env python3
"""Reconstruct project evidence without inferring completion from filenames."""
import argparse, hashlib, json
from pathlib import Path

def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    skill = Path(__file__).resolve().parents[1]
    manifest_path = args.manifest or skill / "references/source-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    repo = args.repo.resolve()
    sources, conflicts = [], []
    for source in manifest["sources"]:
        path = repo / source["path"]
        observed = {"path": source["path"], "required": source["required"], "exists": path.is_file()}
        if path.is_file():
            observed["sha256"] = digest(path)
            observed["matches_generation"] = observed["sha256"] == source.get("sha256")
            if source["required"] and not observed["matches_generation"]:
                conflicts.append(f"authoritative source changed: {source['path']}")
        elif source["required"]:
            conflicts.append(f"required authoritative source missing: {source['path']}")
        sources.append(observed)
    status = {"milestones": {}}
    status_path = manifest.get("status_file")
    if status_path:
        candidate = repo / status_path
        if candidate.is_file():
            try:
                status = json.loads(candidate.read_text(encoding="utf-8"))
            except Exception as error:
                conflicts.append(f"status file unreadable: {status_path}: {error}")
        else:
            conflicts.append(f"optional status file absent: {status_path}")
    documented_complete = set()
    states = []
    known = {item["id"] for item in manifest["milestones"]}
    for identifier, item in status.get("milestones", {}).items():
        if identifier not in known:
            conflicts.append(f"status contains unknown milestone: {identifier}")
        if item.get("state") == "complete":
            evidence = item.get("evidence", [])
            if not isinstance(evidence, list) or not evidence:
                conflicts.append(f"{identifier} is documented complete without evidence")
            else:
                documented_complete.add(identifier)
    next_candidate = None
    for milestone in manifest["milestones"]:
        identifier = milestone["id"]
        if identifier in documented_complete:
            state = "documented_complete_pending_reverification"
        elif all(value in documented_complete for value in milestone.get("prerequisites", [])):
            state = "eligible_pending_entry_verification"
            if next_candidate is None:
                next_candidate = identifier
        else:
            state = "blocked_by_documented_prerequisites"
        states.append({"id": identifier, "state": state, "prerequisites": milestone.get("prerequisites", [])})
    required_specialists = [s for s in manifest.get("specialists", []) if s.get("level") == "required"]
    starter = (
        f"Read repository instructions and authoritative sources; resolve {len(conflicts)} conflict(s); "
        f"re-verify entry criteria for {next_candidate or 'no eligible milestone'}; route required specialist work; "
        "finish with exact commands, outcomes, unresolved risks, and next candidate slice."
    )
    result = {"fact_model": "documented status is not observed completion", "sources": sources,
              "conflicts": conflicts, "milestones": states, "next_candidate": next_candidate,
              "required_specialists": required_specialists, "fresh_session_starter": starter}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if conflicts else 0

if __name__ == "__main__": raise SystemExit(main())
'''


GENERATED_VALIDATOR = r'''#!/usr/bin/env python3
"""Validate this generated project Skill without CodexToolkit dependencies."""
import argparse, hashlib, json, re
from pathlib import Path

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--repo", type=Path, required=True); parser.add_argument("--skill", type=Path)
    args = parser.parse_args(); skill = (args.skill or Path(__file__).resolve().parents[1]).resolve(); failures = []
    required = ["SKILL.md", "agents/openai.yaml", "references/project-map.md", "references/milestone-map.md", "references/repository-contract.md", "references/source-manifest.json", "scripts/inspect_project_state.py", "scripts/validate_project_skill.py"]
    for relative in required:
        if not (skill / relative).is_file(): failures.append(f"missing generated file: {relative}")
    try: manifest = json.loads((skill / "references/source-manifest.json").read_text(encoding="utf-8"))
    except Exception as error: manifest = {}; failures.append(f"invalid manifest: {error}")
    ids = [m.get("id") for m in manifest.get("milestones", [])]
    if not ids or len(ids) != len(set(ids)): failures.append("milestone IDs must be present and unique")
    for source in manifest.get("sources", []):
        path = args.repo.resolve() / source["path"]
        if source.get("required") and not path.is_file(): failures.append(f"required source missing: {source['path']}")
        elif path.is_file() and source.get("sha256") != digest(path): failures.append(f"source hash stale: {source['path']}")
    text = (skill / "SKILL.md").read_text(encoding="utf-8") if (skill / "SKILL.md").is_file() else ""
    if not re.search(r"^---\nname: build-[a-z0-9-]+\n", text): failures.append("invalid build-* Skill frontmatter")
    print(json.dumps({"valid": not failures, "failures": failures}, indent=2)); return 0 if not failures else 1
if __name__ == "__main__": raise SystemExit(main())
'''


def milestone_sections(milestones: list[dict]) -> str:
    sections = []
    for item in milestones:
        specialists = item.get("specialists", [])
        sections.append(
            f"## {item['id']} — {item['title']}\n\n"
            f"Goal: {item['goal']}\n\nPrerequisites:\n{bullet(item.get('prerequisites', []) or ['None'])}\n\n"
            f"Entry evidence:\n{bullet(item['entry'])}\n\nAcceptance evidence:\n{bullet(item['evidence'])}\n\n"
            f"Exit evidence:\n{bullet(item['exit'])}\n\nSpecialist routes:\n{bullet(specialists or ['Use repository-appropriate implementation expertise'])}"
        )
    return "\n\n".join(sections)


def generate(repo: Path, config: dict, output: Path, templates: Path, prior: Path | None) -> dict:
    preserved_edits: list[str] = []
    preserved_unmanaged: list[str] = []
    old_manifest = None
    if prior:
        old_manifest = json.loads((prior / "references/source-manifest.json").read_text(encoding="utf-8"))
        if old_manifest.get("schema_version") != SCHEMA:
            raise ValueError(f"unsupported prior schema: {old_manifest.get('schema_version')}")

    output.mkdir(parents=True)
    sources = []
    for source in config["authoritative_sources"]:
        target = repo / source["path"]
        sources.append({"path": source["path"], "role": source["role"], "required": bool(source.get("required", True)),
                        "sha256": sha256(target) if target.is_file() else None})

    source_table = "\n".join(f"| `{s['path']}` | {s['role']} | {'required' if s['required'] else 'optional'} |" for s in sources)
    source_table = "| Path | Role | Requirement |\n|---|---|---|\n" + source_table
    specialists = config.get("specialists", [])
    specialist_lines = [f"- **{s['name']}** ({s['level']}): {s['job']}. Fallback: {s['fallback']}" for s in specialists] or ["- Use repository-appropriate specialists; stop if required expertise is unavailable."]
    values = {
        "PROJECT_NAME": config["project_name"], "PURPOSE": config["purpose"], "ENVIRONMENT": config["implementation_environment"],
        "SOURCE_TABLE": source_table, "AUTHORITY_LIST": bullet(config["authority_order"]),
        "MILESTONE_SECTIONS": milestone_sections(config["milestones"]), "INVARIANTS": bullet(config["invariants"]),
        "NON_GOALS": bullet(config["non_goals"]), "DELIVERY_RULES": bullet(config["delivery_rules"]),
        "SPECIALISTS": "\n".join(specialist_lines),
    }
    contents = {
        "SKILL.md": generated_skill_md(config),
        "agents/openai.yaml": "interface:\n  display_name: " + json.dumps(f"Build {config['project_name']}") +
            "\n  short_description: " + json.dumps(f"Orchestrate evidence-backed {config['project_name']} build sessions") +
            "\n  default_prompt: " + json.dumps(f"Use ${config['skill_slug']} to reconstruct project state and select the next bounded implementation slice.") +
            "\npolicy:\n  allow_implicit_invocation: true\n",
        "references/project-map.md": render((templates / "project-map.md").read_text(), values),
        "references/milestone-map.md": render((templates / "milestone-map.md").read_text(), values),
        "references/repository-contract.md": render((templates / "repository-contract.md").read_text(), values),
        "scripts/inspect_project_state.py": STATE_INSPECTOR,
        "scripts/validate_project_skill.py": GENERATED_VALIDATOR,
    }

    old_hashes = (old_manifest or {}).get("generated_hashes", {})
    for relative, content in contents.items():
        prior_path = prior / relative if prior else None
        if prior_path and prior_path.is_file() and old_hashes.get(relative) and sha256(prior_path) != old_hashes[relative]:
            destination = output / relative; destination.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(prior_path, destination)
            preserved_edits.append(relative)
        else:
            write(output / relative, content, relative.startswith("scripts/"))

    if prior:
        old_managed = set((old_manifest or {}).get("managed_files", []))
        for path in prior.rglob("*"):
            if path.is_file():
                relative = path.relative_to(prior).as_posix()
                if relative not in old_managed:
                    destination = output / relative; destination.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(path, destination)
                    preserved_unmanaged.append(relative)

    generated_hashes = {relative: sha256(output / relative) for relative in MANAGED if relative != "references/source-manifest.json" and (output / relative).is_file()}
    manifest_values = {
        "SCHEMA_VERSION": SCHEMA, "PROJECT_NAME_JSON": json.dumps(config["project_name"]), "SKILL_SLUG_JSON": json.dumps(config["skill_slug"]),
        "SOURCES_JSON": json.dumps(sources, indent=2), "MILESTONES_JSON": json.dumps(config["milestones"], indent=2),
        "SPECIALISTS_JSON": json.dumps(config.get("specialists", []), indent=2),
        "STATUS_FILE_JSON": json.dumps(config.get("status_file")), "MANAGED_FILES_JSON": json.dumps(MANAGED, indent=2),
        "GENERATED_HASHES_JSON": json.dumps(generated_hashes, indent=2),
    }
    manifest = render((templates / "source-manifest.json").read_text(), manifest_values)
    write(output / "references/source-manifest.json", manifest)
    return {"output": str(output), "preserved_edited_generated_files": preserved_edits, "preserved_unmanaged_files": preserved_unmanaged,
            "source_hashes": {s["path"]: s["sha256"] for s in sources}}


def recursive_diff(old: Path, new: Path) -> str:
    paths = sorted({p.relative_to(old).as_posix() for p in old.rglob("*") if p.is_file()} | {p.relative_to(new).as_posix() for p in new.rglob("*") if p.is_file()})
    chunks = []
    for relative in paths:
        left, right = old / relative, new / relative
        try:
            before = left.read_text(encoding="utf-8").splitlines(True) if left.is_file() else []
            after = right.read_text(encoding="utf-8").splitlines(True) if right.is_file() else []
            chunks.extend(difflib.unified_diff(before, after, fromfile=f"active/{relative}", tofile=f"candidate/{relative}"))
        except UnicodeDecodeError:
            if not left.is_file() or not right.is_file() or sha256(left) != sha256(right): chunks.append(f"Binary files differ: {relative}\n")
    return "".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True); parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True); parser.add_argument("--refresh-from", type=Path); parser.add_argument("--diff-output", type=Path)
    args = parser.parse_args(); repo = args.repo.resolve(); config_path = args.config.resolve(); output = args.output.resolve()
    try:
        gate = inspect(repo, config_path)
        if gate["verdict"] == "Needs specification":
            print(json.dumps({"generated": False, "gate": gate}, indent=2)); return 1
        config = json.loads(config_path.read_text(encoding="utf-8")); prior = args.refresh_from.resolve() if args.refresh_from else None
        if output.exists(): raise ValueError(f"output already exists; refusing to overwrite: {output}")
        if prior and not prior.is_dir(): raise ValueError(f"refresh source is not a directory: {prior}")
        if prior and output == prior: raise ValueError("refresh output must be separate from the active Skill")
        templates = Path(__file__).resolve().parents[1] / "assets/templates"
        result = generate(repo, config, output, templates, prior)
        result.update({"generated": True, "gate_verdict": gate["verdict"]})
        if prior:
            diff = recursive_diff(prior, output); result["diff_lines"] = len(diff.splitlines())
            if args.diff_output:
                args.diff_output.parent.mkdir(parents=True, exist_ok=True); args.diff_output.write_text(diff, encoding="utf-8"); result["diff_output"] = str(args.diff_output.resolve())
            else: result["diff"] = diff
        print(json.dumps(result, indent=2, sort_keys=True)); return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr); return 2


if __name__ == "__main__": raise SystemExit(main())
