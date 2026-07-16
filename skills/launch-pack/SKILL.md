---
name: launch-pack
description: Plan, assemble, audit, and hand off an evidence-backed launch package for a software release across repository, website, social, community, store, submission, and demo surfaces. Use when Codex needs to coordinate launch claims, audiences, channel deliverables, screenshots, product demos, release copy, asset readiness, provenance, or a final launch checklist from verified product evidence. Do not use for publishing without explicit authority, fictional campaigns, generic brand strategy, or copy-only work better handled directly by merge-and-tell.
---

# Launch Pack

Turn a verified product release into one coherent public package. Own the evidence contract, channel plan, cross-asset consistency, readiness gates, and handoff. Route specialist production to the relevant toolkit skill instead of duplicating it.

Read [evidence-contract.md](references/evidence-contract.md) before accepting claims. Read [delivery-matrix.md](references/delivery-matrix.md) when selecting channels. Read [quality-gates.md](references/quality-gates.md) before final handoff.

## Non-negotiables

- Ground every public claim in inspected evidence. Qualify uncertainty; never strengthen wording to fill a launch slot.
- Keep version, availability, date, audience, pricing, platform support, limitations, and call to action consistent across outputs.
- Distinguish ready, draft, blocked, omitted, and not applicable. A file existing does not make it launch-ready.
- Keep private data, credentials, unreleased links, internal metrics, and unsupported commitments out of the pack.
- Never publish, upload, create a release, submit a form, or send communication without explicit user authority for that action.

## Choose the mode

- **Plan:** Establish the release contract, evidence, audiences, channels, deliverables, owners, and blockers.
- **Assemble:** Produce or coordinate the selected assets from verified inputs.
- **Audit:** Review an existing launch package for factual, visual, technical, and cross-channel consistency.
- **End to end:** Plan, assemble, validate, and hand off the complete package, pausing only for missing evidence, assets, credentials, or consequential owner decisions.

Use the narrowest mode that completes the request.

## Establish the release contract

Inspect the repository and supplied evidence before asking the user to restate it. Determine:

1. Product, release name, exact version/build, release state, and authoritative source.
2. Primary audience, user outcome, launch objective, and desired next action.
3. Release date or window, availability, platforms, pricing, eligibility, and material limitations.
4. Required channels, format constraints, submission rules, accessibility needs, and publication authority.
5. Existing screenshots, footage, logos, copy, links, measurements, tests, build logs, and provenance records.

Ask only for missing information that would otherwise force fabrication or materially change the package.

## Create the working pack

Default to a repository-root `launch-pack/` directory unless the project defines another location. Copy and complete only the templates required for the selected mode:

- `LAUNCH_BRIEF.md`
- `CLAIMS_LEDGER.md`
- `ASSET_INVENTORY.md`
- `CHANNEL_MATRIX.md`
- `RELEASE_CHECKLIST.md`
- `HANDOFF.md`

Use the templates in `assets/templates/`. Put finished channel deliverables under `launch-pack/outputs/` with descriptive names. Do not overwrite authoritative source material.

## Build one evidence spine

- Apply the evidence hierarchy and claim statuses in [evidence-contract.md](references/evidence-contract.md).
- Give every material claim a stable ID and map every deliverable to the claims it uses.
- Record qualifications where viewers can actually see them; a private ledger note is not disclosure.
- Resolve conflicting versions, dates, availability statements, metrics, and links before specialist production begins.

## Route specialist work

- Use `product-demo` for launch videos, walkthroughs, shot lists, captions, media inspection, and export QA. Pass it the verified brief and claims ledger.
- Use `merge-and-tell` for launch posts, release updates, community copy, and channel-specific rewrites. Supply only verified facts, required qualifications, and the selected call to action.
- Use `github-social-preview` for exact-brand repository link-preview artwork. Supply the confirmed product facts, exact tagline, repository assets, and channel constraints.
- Use `authored-frontend-design` for a launch page or web surface that needs implementation.
- Use `authored-macos-design` when launch work requires changes to a native Mac presentation surface.
- For Premonition, use `build-premonition` and `maintain-premonition-build-log` as evidence sources and provenance workflows; do not let launch materials overrule the specification or logs.

Record every routed deliverable, owner, source, status, constraint, and output path in `CHANNEL_MATRIX.md`.

## Assemble and audit

Review the package as one system, not as independent polished files. Check factual agreement, narrative order, visual identity, audience fit, accessibility, technical constraints, privacy, link destinations, and recovery from missing or delayed assets.

For a final pack, run:

```bash
python3 scripts/check_launch_pack.py launch-pack --final
```

The checker validates structure and unresolved markers; it does not prove claims. Inspect every cited source and rendered asset before marking the package ready.

## Handoff

Report the release identity, included and omitted channels, verified and qualified claims, ready and blocked assets, validation performed, publication authority, remaining decisions, and exact next action. Stop at handoff unless the user explicitly authorizes publication or submission.
