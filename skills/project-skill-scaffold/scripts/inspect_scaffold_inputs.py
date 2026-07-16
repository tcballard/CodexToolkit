#!/usr/bin/env python3
"""Inspect a project-Skill input contract against the stability gate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


SLUG = re.compile(r"^build-[a-z0-9]+(?:-[a-z0-9]+)*$")


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def nonempty_list(config: dict, key: str) -> bool:
    value = config.get(key)
    return isinstance(value, list) and bool(value) and all(str(item).strip() for item in value)


def inspect(repo: Path, config_path: Path) -> dict:
    failures: list[dict] = []
    warnings: list[str] = []
    if not repo.is_dir():
        return {"verdict": "Needs specification", "failures": [{"gate": "inspectable_state", "reason": f"repository is not a directory: {repo}"}]}
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return {"verdict": "Needs specification", "failures": [{"gate": "input_contract", "reason": f"cannot read valid JSON config: {error}"}]}

    identity = all(str(config.get(key, "")).strip() for key in ("project_name", "purpose", "implementation_environment"))
    if not identity or not SLUG.fullmatch(str(config.get("skill_slug", ""))):
        failures.append({"gate": "identity", "reason": "project_name, purpose, implementation_environment, and normalized build-* skill_slug are required"})

    sources = config.get("authoritative_sources")
    source_evidence: list[dict] = []
    if not isinstance(sources, list) or not sources:
        failures.append({"gate": "authority", "reason": "at least one authoritative source is required"})
    else:
        for source in sources:
            if not isinstance(source, dict) or not str(source.get("path", "")).strip() or not str(source.get("role", "")).strip():
                failures.append({"gate": "authority", "reason": "every source needs path and role"})
                continue
            relative = Path(source["path"])
            if relative.is_absolute() or ".." in relative.parts:
                failures.append({"gate": "authority", "reason": f"source path must be repository-relative: {relative}"})
                continue
            target = repo / relative
            exists = target.is_file()
            required = bool(source.get("required", True))
            evidence = {"path": str(relative), "role": source["role"], "required": required, "exists": exists}
            if exists:
                evidence["sha256"] = sha256(target)
            elif required:
                failures.append({"gate": "inspectable_state", "reason": f"required source is missing: {relative}"})
            source_evidence.append(evidence)

    milestones = config.get("milestones")
    milestone_ids: list[str] = []
    if not isinstance(milestones, list) or not milestones:
        failures.append({"gate": "milestones", "reason": "at least one bounded milestone is required"})
    else:
        for index, milestone in enumerate(milestones):
            if not isinstance(milestone, dict):
                failures.append({"gate": "milestones", "reason": f"milestone {index} is not an object"})
                continue
            identifier = str(milestone.get("id", "")).strip()
            milestone_ids.append(identifier)
            missing = [key for key in ("id", "title", "goal") if not str(milestone.get(key, "")).strip()]
            missing += [key for key in ("entry", "evidence", "exit") if not isinstance(milestone.get(key), list) or not milestone.get(key)]
            if missing:
                failures.append({"gate": "milestones", "reason": f"milestone {identifier or index} lacks: {', '.join(missing)}"})
        if len(set(milestone_ids)) != len(milestone_ids) or "" in milestone_ids:
            failures.append({"gate": "milestones", "reason": "milestone IDs must be non-empty and unique"})
        known = set(milestone_ids)
        for milestone in milestones:
            if isinstance(milestone, dict):
                unknown = set(milestone.get("prerequisites", [])) - known
                if unknown:
                    failures.append({"gate": "milestones", "reason": f"{milestone.get('id')} has unknown prerequisites: {sorted(unknown)}"})

    if not nonempty_list(config, "invariants") or not nonempty_list(config, "non_goals"):
        failures.append({"gate": "constraints", "reason": "non-empty invariants and non_goals are required"})
    if not nonempty_list(config, "authority_order"):
        failures.append({"gate": "status_authority", "reason": "authority_order is required"})
    if not nonempty_list(config, "delivery_rules"):
        failures.append({"gate": "delivery", "reason": "delivery_rules are required"})

    specialists = config.get("specialists", [])
    if not isinstance(specialists, list):
        failures.append({"gate": "specialists", "reason": "specialists must be a list"})
    else:
        for specialist in specialists:
            if not isinstance(specialist, dict) or not all(str(specialist.get(key, "")).strip() for key in ("name", "level", "job", "fallback")):
                failures.append({"gate": "specialists", "reason": "each specialist needs name, level, job, and fallback"})
            elif specialist["level"] not in ("required", "recommended", "optional"):
                failures.append({"gate": "specialists", "reason": f"invalid specialist level: {specialist['level']}"})

    unknowns = config.get("unknowns", [])
    if not isinstance(unknowns, list):
        failures.append({"gate": "unknowns", "reason": "unknowns must be a list"})
        unknowns = []
    for unknown in unknowns:
        if isinstance(unknown, dict) and unknown.get("blocks_next_milestone"):
            failures.append({"gate": "unknowns", "reason": f"blocking unresolved decision: {unknown.get('question', unknown)}"})

    branch = None
    dirty = None
    if (repo / ".git").exists():
        branch_result = subprocess.run(["git", "branch", "--show-current"], cwd=repo, text=True, capture_output=True, check=False)
        status_result = subprocess.run(["git", "status", "--porcelain"], cwd=repo, text=True, capture_output=True, check=False)
        branch = branch_result.stdout.strip() or None
        dirty = bool(status_result.stdout)
    else:
        warnings.append("repository has no inspectable .git directory; history and branch rules were not checked")

    verdict = "Needs specification" if failures else ("Scaffoldable with explicit unknowns" if unknowns else "Scaffoldable")
    return {
        "verdict": verdict, "repository": str(repo.resolve()), "config": str(config_path.resolve()),
        "project_name": config.get("project_name"), "skill_slug": config.get("skill_slug"),
        "sources": source_evidence, "milestone_ids": milestone_ids,
        "unknowns": unknowns, "git_branch_observed": branch, "git_worktree_dirty": dirty,
        "failures": failures, "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = inspect(args.repo.resolve(), args.config.resolve())
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0 if result["verdict"] != "Needs specification" else 1


if __name__ == "__main__":
    raise SystemExit(main())
