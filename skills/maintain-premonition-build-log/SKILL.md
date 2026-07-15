---
name: maintain-premonition-build-log
description: "Maintain Premonition's paired append-only BUILDLOG.md and DEVLOG.md: an evidence-backed handoff and Sol provenance record plus a candid, traceable builder diary. Use when initialising, reconstructing, appending, validating, correcting, or summarising either Premonition log; at a Sol session boundary, phase transition, context-compaction checkpoint, owner decision, verification result, deviation, failure, or blocker; or when identifying the exact next Premonition session state. Do not use for unrelated projects or as a substitute for PREMONITION_SPEC.md, ADRs, Git history, or the Sol provenance ledger."
---

# Maintain Premonition Logs

Keep `BUILDLOG.md` concise, append-only, evidence-backed and sufficient for a fresh Sol session to resume. Keep `DEVLOG.md` human, candid and readable without allowing its prose to become project evidence.

## Establish the record

1. Locate the Premonition repository and inspect `git status --short` without changing it.
2. Read `BUILDLOG.md` and `DEVLOG.md` in full when present. If `BUILDLOG.md` does not exist, inspect the available specification, Git history and owner-provided evidence before creating either log.
3. Locate `PREMONITION_SPEC.md`; before repository canonicalisation, accept `Premonition-Implementation-Spec-v2.md` as the source artefact.
4. Read the specification's authority rules, build-session plan, verification register, Sol-ledger schema and settled decision log when available.
5. Treat the latest build-log entry as current. A preamble status block is historical if a later entry supersedes it. Never use `DEVLOG.md` as factual authority.
6. Use this authority order:
   1. observable files, commands and results from the current session;
   2. explicit owner decisions in visible context;
   3. settled decisions already recorded in the log;
   4. repository history and timestamps;
   5. inference, labelled as inference.

Never reconstruct facts from memory when evidence can be inspected. Never invent dates, model identity, Session IDs, commits, commands, test results, owner approvals or completion states.

## Choose the operation

- **Initialise:** Create a short build-log preamble plus the earliest evidence-supported entry, then create the paired dev-log entry. Mark missing evidence explicitly. Do not manufacture a retrospective success narrative.
- **Append:** Add one factual entry for a coherent session or consequential owner decision, then add a matching diary entry. Preserve all existing bytes in both files.
- **Checkpoint:** Append before anticipated context compaction, interruption or handoff even when the phase is incomplete.
- **Correct:** Append a dated correction naming the affected entry and corrected claim. Never edit the original entry silently.
- **Validate:** Run the bundled checker across both logs and inspect the final diff. Validation proves structure, pairing and append-only integrity, not factual truth.

Use the entry structure in [references/entry-template.md](references/entry-template.md). Preserve an existing ID convention. For the planning sequence use the next unused `P<number>`; during implementation use a unique phase-qualified ID such as `S0.1`.

## Record evidence, not narrative

Include:

- objective and status: `Complete`, `Partial` or `Blocked`;
- exact model evidence and Session ID, or `Not captured`;
- concrete outcomes and material owner decisions;
- files, commits or durable artefacts produced;
- commands actually run and their observed results;
- deviations from the specification and why;
- unresolved risks, missing evidence and known failures;
- one exact next-session entry state.

Separate these evidence classes explicitly when ambiguity exists:

- **Observed:** directly inspected or run in the current workspace;
- **Owner-confirmed:** stated by the owner in visible context;
- **Previously recorded:** inherited from an earlier log entry;
- **Unverified:** plausible or planned, but not yet proved.

Distinguish `Sol implemented`, `Sol reviewed`, `Human-authored and Sol-reviewed`, and `Owner decision`. A claim that Sol handled a phase requires visible model confirmation plus a corresponding session or ledger record. A commit trailer alone is insufficient.

## Write the paired dev diary

After the factual entry passes review, append a matching `DEVLOG.md` entry using the same ID and [references/devlog-template.md](references/devlog-template.md).

Use `merge-and-tell` in Draft mode when available. Supply only the completed BUILDLOG entry as factual source material and request a candid builder-operator diary entry, not launch copy. The diary may interpret why a decision mattered, acknowledge uncertainty, and describe the shape of the work. It must not introduce a new metric, date, result, commitment, owner decision or claim of Sol involvement.

For every material session or consequential decision, maintain both logs. For a mechanical compaction checkpoint with no story change, append only BUILDLOG and state `DEVLOG: no material narrative change` in its Artefacts section.

Keep diary entries short: three to seven paragraphs, normally under 250 words. Lead with the most interesting truthful change. Include what remains unfinished. End with the concrete next move. Add an exact source line pointing to the corresponding BUILDLOG entry.

## Protect privacy and scope

Never include:

- clipboard or repository content captured at runtime;
- raw prompts, diffs, model output, stdout or stderr;
- credentials, tokens, private keys or signed transfer URLs;
- content-bearing application logs or crash dumps;
- unverifiable claims that a patch is correct, private data was redacted, or provider retention is controlled.

Apply these exclusions to both logs. The diary may be lively; it may not be evidentially loose.

Record safe command names, exit status, test counts, timings and reason enums where useful. Summarise failures without copying sensitive payloads.

Keep this skill outside the Premonition product and runtime. The product specification's v0.1 exclusion of a shipped skill/plugin remains binding; this is project workflow infrastructure, not a product feature or runtime dependency.

## Finish the update

1. Append the BUILDLOG entry without changing prior content.
2. For material work, append the paired DEVLOG entry only after the BUILDLOG facts are settled.
3. If previous copies are available, run:

   ```bash
   python3 scripts/check_buildlog.py BUILDLOG.md \
     --previous <previous-buildlog-copy> \
     --devlog DEVLOG.md \
     --previous-devlog <previous-devlog-copy>
   ```

   Otherwise run:

   ```bash
   python3 scripts/check_buildlog.py BUILDLOG.md --devlog DEVLOG.md
   ```

4. Inspect `git diff -- BUILDLOG.md DEVLOG.md` when the files are in a repository.
5. Confirm that every verification claim maps to a command or explicitly named manual observation and that DEVLOG adds no new facts.
6. Update `docs/build-week/sol-ledger.md` separately for every material phase. Do not treat BUILDLOG, DEVLOG or a commit trailer as a substitute for the ledger.
7. Return the paired entry ID, verification performed, missing evidence and exact next-session entry state.
