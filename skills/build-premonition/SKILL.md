---
name: build-premonition
description: Run specification-led GPT-5.6 Sol sessions for the Premonition macOS menu-bar app. Use when starting, resuming, implementing, reviewing, testing, designing, documenting, packaging, or preparing a submission for Premonition; when a user references PREMONITION_SPEC.md, the Premonition build log, its Sol provenance, or an S0–S6 build phase; or when Codex must establish the project workspace from the authoritative Premonition specification.
---

# Build Premonition

Treat the repository specification as product authority and this skill as the session operator. Never bundle or recreate the full specification inside the skill.

## Establish authority

1. Locate the repository root and inspect Git status without changing it.
2. Locate the specification in this order:
   - repository-root `PREMONITION_SPEC.md`;
   - repository-root `Premonition-Implementation-Spec-v2.md` only before S0 canonicalisation;
   - a user-attached or Library-backed copy only when no repository copy exists.
3. If multiple plausible authoritative copies exist, stop and ask which one becomes `PREMONITION_SPEC.md`. Do not merge them from memory.
4. Read `AGENTS.md`, the complete specification, `BUILDLOG.md`, and §13 of the specification before editing.
5. Apply this authority order:
   1. `PREMONITION_SPEC.md`;
   2. settled decisions already recorded in `BUILDLOG.md`;
   3. verified behaviour of the current machine and installed tools;
   4. this skill;
   5. other plugin guidance.
6. When verified machine behaviour conflicts with the specification, record the conflict and propose the smallest compliant adjustment. Do not silently reinterpret a safety invariant.

## Confirm Sol provenance

Confirm that the current session explicitly uses GPT-5.6 Sol from visible session context or the user's explicit statement. Do not infer the model from capability or prose style.

Before material work in a session:

- run or request `/feedback` when the surface supports it;
- record the stable Session ID when available;
- append the phase, model, owner decision, result and verification to `docs/build-week/sol-ledger.md`;
- keep the core S1–S2 work in the durable session identified for the submission.

If Sol cannot be confirmed, perform read-only orientation only and ask the user to select or confirm Sol before implementation.

## Initialise missing project evidence

If `BUILDLOG.md` is absent, create it before implementation. Reconstruct only facts supported by the specification, visible conversation artefacts, file timestamps or Git history. Never fabricate session IDs, model attribution, dates, commits or test results.

The initial log must contain:

- current phase and exact repository state;
- canonical spec path and version;
- known pre-existing planning with dates;
- known Sol-led refinements with evidence;
- decisions already settled;
- verification already completed;
- deviations from earlier plans;
- missing evidence explicitly marked missing;
- the exact next-session entry state.

Keep `BUILDLOG.md` append-only. Correct mistakes with later entries. Append at every session boundary and before anticipated context compaction.

If `docs/build-week/sol-ledger.md` is absent, create it from the schema in the specification. Do not treat a commit trailer alone as proof of Sol involvement.

## Select the build phase

Read the S0–S6 entry and exit criteria. Select only the earliest incomplete phase whose entry criteria are met.

- Do not implement later phases opportunistically.
- Do not mark a phase complete without its specified verification.
- Do not start S1 until S0 evidence, scaffold and tool contracts exist.
- Do not start publication work merely because the build is ready.
- Use the named cut order when time is constrained; flag any cut before making it.

At the beginning, state the selected phase, evidence read and blocking unknowns. At the end, append the build-log entry and report the exact next entry state.

## Route macOS work

Use the Build macOS Apps plugin as a supporting implementation playbook:

| Work | Skill |
|---|---|
| SwiftPM product discovery, build and tests | `build-macos-apps:swiftpm-macos` |
| Stable `.app` build/run entrypoint and Codex Run action | `build-macos-apps:build-run-debug` |
| Settings and SwiftUI view/state structure | `build-macos-apps:swiftui-patterns` |
| `NSStatusItem`, `NSPopover`, pasteboard and non-activating `NSPanel` | `build-macos-apps:appkit-interop` |
| Narrowing SwiftPM/XCTest failures | `build-macos-apps:test-triage` |
| Signing, hardened runtime and Gatekeeper | `build-macos-apps:signing-entitlements` |
| Release bundle and notarisation | `build-macos-apps:packaging-notarization` |

Preserve these Premonition-specific boundaries:

- Keep the SwiftPM plus native `.app` bundle architecture.
- Use `NSStatusItem` rather than replacing the specified status behaviour with a generic `MenuBarExtra`.
- Use the smallest AppKit bridge and keep SwiftUI as the view source of truth.
- Keep the macOS 14+ deployment target; do not introduce macOS 15+/26-only APIs without guarded fallback and an owner-approved decision entry.
- Do not introduce Liquid Glass.
- Treat unified logging as local debugging only. Never add remote telemetry or content-bearing logs.
- Keep `script/build_and_run.sh` as the developer entrypoint and let it call the lower-level app-bundle build script; do not create competing run workflows.

## Protect invariants

Before accepting any implementation change, check it against C1–C5 and §13. In particular:

- no model call before gate, allowlist and cap admission;
- no clipboard or patch content in normal persistence or logs;
- pinned Sol runtime and verified ephemeral execution;
- read-only speculation;
- one candidate, never queued or silently replaced;
- one diff parser for validate, render and Apply;
- `.git`, traversal, binary and symlink escape rejection;
- explicit clean-tree Apply through `git apply` only;
- no auto-apply, staging, commit or post-apply command;
- rationale only after final validation;
- no public action without explicit owner authority.

## Verify proportionately

Run the narrowest relevant test first, then the phase exit suite. Distinguish build, assertion, crash, timing, environment, entitlement and fixture failures. Record commands and results, not just “tests passed”.

For UI work, verify a real `.app` bundle rather than launching a raw SwiftPM GUI executable. Do not claim visual or focus behaviour that was not inspected.

For release work, separate local build success, signing validity, Gatekeeper assessment and notarisation. Missing owner credentials are a recorded blocker, not a reason to invent configuration.

## Finish the session

Append to `BUILDLOG.md`:

- timestamp and phase;
- model and Session ID evidence;
- completed work;
- owner decisions;
- files and commits produced;
- deviations with reasons;
- verification commands and results;
- unresolved risks;
- exact next-session entry state.

Update the Sol ledger for material work. Review the final diff. Preserve unrelated user changes. Never publish, submit, create a public release or upload a Homebrew formula without explicit owner instruction.

Return a concise outcome containing:

1. phase outcome;
2. material files changed;
3. verification performed;
4. blockers or deviations;
5. exact next entry state.
