---
name: project-skill-scaffold
description: Generate, validate, or safely refresh a lean project-specific build orchestration Skill from a stable specification and inspectable repository. Use when Codex needs to preserve project authority, milestones, invariants, specialist routing, repository rules, state reconstruction, or a fresh-session starter across long-running coding sessions. Do not use for vague ideas, specification writing, project implementation, generic repository scaffolding, one-off handoffs, build-journal maintenance, or autonomous project management.
---

# Project Skill Scaffold

Create a project-specific orchestration Skill that reconstructs authority and selects the next bounded implementation slice. Do not implement the project or copy its specification into the generated Skill.

Read [stability-gate.md](references/stability-gate.md), [generated-skill-contract.md](references/generated-skill-contract.md), and [refresh-contract.md](references/refresh-contract.md). Apply [quality-gates.md](references/quality-gates.md) before delivery.

## Inspect before scaffolding

Read repository instructions, working tree, history, specification candidates, milestones, logs, manifests, CI, tests, and any existing project Skill. Establish authority among specification, decisions, verified behavior/tests, logs, and user decisions. Distinguish stable requirements, observed implementation, inferences, unknowns, and future plans.

Prepare a JSON input contract containing project identity, purpose, authoritative source paths, milestone contracts, invariants, non-goals, authority order, delivery rules, specialist routes, and optional external status file. See [generated-skill-contract.md](references/generated-skill-contract.md) for the schema.

Run the hard gate:

```bash
python3 scripts/inspect_scaffold_inputs.py --repo /path/to/repo --config /path/to/project-skill.json
```

Proceed only on `Scaffoldable` or `Scaffoldable with explicit unknowns`. On `Needs specification`, return the exact failed gates; do not generate confident orchestration from a brainstorm.

## Generate a new project Skill

Generate outside an existing Skill path:

```bash
python3 scripts/scaffold_project_skill.py \
  --repo /path/to/repo \
  --config /path/to/project-skill.json \
  --output /path/to/repo/skills/build-project
```

The generator creates only the lean contract: `SKILL.md`, `agents/openai.yaml`, project/milestone/repository maps, a source manifest, and self-contained state/validation scripts. It references source documents rather than copying them. It never marks a milestone complete from a plausible filename.

Validate:

```bash
python3 scripts/validate_generated_skill.py \
  --repo /path/to/repo --skill /path/to/repo/skills/build-project
```

Then run the generated `scripts/inspect_project_state.py --repo /path/to/repo`. Its next slice is a candidate based on documented evidence and prerequisites, not a completion claim. Re-verify required acceptance evidence in the new session.

## Refresh safely

Never rewrite an active Skill in place. Generate a sibling candidate and diff:

```bash
python3 scripts/scaffold_project_skill.py \
  --repo /path/to/repo \
  --config /path/to/project-skill.json \
  --refresh-from /path/to/repo/skills/build-project \
  --output /tmp/build-project-candidate \
  --diff-output /tmp/build-project-refresh.diff
```

The generator copies unmanaged files byte-for-byte. If a previously generated file no longer matches its recorded generation hash, it preserves that edited file in the candidate and reports it for human reconciliation. It does not silently overwrite hand work.

Treat changed source hashes, missing authority, changed milestone contracts, unsupported schema, status/evidence conflict, or unavailable required specialists as stale signals—not proof the active Skill is wrong.

## Architecture boundaries

The generated Skill owns project orchestration: authority reconstruction, milestone eligibility, specialist routing, verification, and finish/handoff. It may consume a spec-to-build plan, project handoff, or build journal, but replaces none of them. Technical implementation stays with specialist Skills such as Build macOS Apps; document a fallback or blocker for every toolkit-specific route.

Do not embed a current branch, commit, installed plugin version, relative deadline, or transient `milestone complete` statement as permanent instruction. Never claim completion from filenames or stale prose.

## Repository delivery

Review the complete candidate diff. When repository delivery is explicitly requested, read instructions, use a focused branch, run validation, review the diff, and open a draft PR through the authorized workflow. Never commit to the default branch and never create a ceremonial issue.

## Deliver

Return gate verdict and evidence, generated/candidate path, source hashes, validation results, state-inspection result, preserved edits/unmanaged files, refresh diff path, conflicts, fresh-session starter, specialist routes, and limitations. State explicitly that the Skill was scaffolded—not that the project was implemented.
