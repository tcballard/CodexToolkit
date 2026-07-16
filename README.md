# TC Ballard Toolkit

A growing workshop of focused skills for building, presenting, and shipping software with Codex.

The toolkit gives useful workflows somewhere to mature without turning every experiment into a separate distributable. Skills can remain here, work together, and graduate into standalone plugins later if their audience or release cadence diverges.

## Included skills

### Product Demo

Plans, stages, edits, and verifies evidence-grounded product demonstration videos from real application footage.

It can:

- turn product evidence and submission rules into a timed narrative;
- produce a claims ledger, shot list, and recording checklist;
- direct a reproducible code-defined edit;
- inspect footage and generate review contact sheets;
- validate export duration, dimensions, frame rate, audio, and file size;
- verify factual claims, privacy, captions, and model provenance.

Product Demo treats the official Remotion plugin as an optional maintained companion. It owns the product story, capture discipline, editorial intent, and acceptance gates without copying Remotion's implementation skills.

Invoke it directly with `$product-demo`, or invoke the toolkit and ask for a product demo.

### Launch Pack

Plans, assembles, audits, and hands off an evidence-backed launch package across repository, website, social, community, store, submission, and demo surfaces.

It owns the shared release contract, claims ledger, asset inventory, channel matrix, readiness gates, and cross-channel consistency. Specialist production remains with Product Demo, Merge & Tell, and the Authored Design skills. A deterministic checker catches missing files, placeholders, blocked claims, inconsistent versions, and unready final states without pretending to prove the underlying claims.

Invoke it directly with `$launch-pack` when preparing or reviewing a coordinated software launch.

### GitHub Social Preview

Creates polished 1280 × 640 repository social-preview PNGs below 1 MB using confirmed product facts and the exact repository logo. Image generation is limited to supporting backgrounds or illustrations; final logo placement and typography are composed deterministically.

It validates dimensions and byte size, creates a temporary 50% thumbnail, requires visual inspection at both sizes, and stops without committing, pushing, editing the README, or changing GitHub settings.

Invoke it directly with `$github-social-preview` when creating or auditing `assets/github-social-preview.png`.

### README Front Door

Improves only the opening portion of a repository README so a visitor can understand the product, audience, outcome, distinction, and fastest credible way to try or see it within seconds.

It selects from an approved hero or screenshot, title, specific tagline, concise explanation, verified install or first-use command, proof point, demo link, and restrained badges. It preserves the deeper README, rejects unsupported marketing claims, and deterministically checks unresolved placeholders and local asset paths.

Invoke it directly with `$readme-front-door` when the repository's above-the-fold explanation needs writing, refinement, or audit.

### Open-Source PR Preflight

Audits a proposed contribution against an open-source repository's actual rules before maintainers see it. It establishes the target base and complete diff, checks scope and provenance, runs required repository checks, identifies DCO or CLA obligations, and prepares a truthful PR package and readiness verdict.

Its deterministic checker catches mechanical blockers such as default-branch work, missing diffs, merge markers, whitespace errors, suspicious secret filenames, and oversized files. Publishing remains a separate explicitly authorized action.

Invoke it directly with `$open-source-pr-preflight` before submitting a contribution to an open-source or third-party repository.

### Authored Frontend Design

Creates distinctive, production-grade web interfaces with a committed art direction, a functional signature element, token-driven styling, complete interaction and failure states, accessibility, and responsive behavior.

It explicitly rejects generic template convergence: predictable SaaS layouts, default framework styling, placeholder copy, disconnected visual systems, and polish without usability completeness.

Invoke it directly with `$authored-frontend-design`, or ask the toolkit to design or substantially restyle a web interface.

### Authored macOS Design

Designs native macOS interfaces with an authored shell while preserving platform behavior: windows, commands, focus, selection, keyboard access, accessibility, desktop density, and narrow AppKit boundaries.

It adds target-aware Liquid Glass guidance, evidence-based design review, expressive anti-convergence rules, and native patterns for utility surfaces, inspectors, split views, tables, documents, and menu-bar applications.

Invoke it directly with `$authored-macos-design`, or ask the toolkit to design or substantially restyle a native Mac interface.

### Merge & Tell

Drafts and rewrites concise, candid public product communication with a builder-operator voice. It supports launch posts, release and shipping updates, incident communication, feedback prompts, community replies, and critiques of existing copy without inventing facts or impersonating individuals.

The standalone [Merge & Tell repository](https://github.com/tcballard/MergeAndTell) remains the canonical development source. This toolkit contains a synchronized copy for personal distribution. Install either the standalone plugin or this toolkit when using `$merge-and-tell`; installing both would expose the same skill name twice.

Invoke it directly with `$merge-and-tell` when the destination is public product communication.

### Build Premonition

Runs specification-led GPT-5.6 Sol sessions for the Premonition macOS menu-bar app. It establishes the authoritative specification and repository state, enforces phase entry and exit criteria, routes native implementation through the appropriate macOS workflows, protects the product's safety invariants, and records exact verification and provenance.

Invoke it directly with `$build-premonition` when starting, resuming, implementing, reviewing, testing, packaging, or preparing a submission for Premonition.

### Maintain Premonition Logs

Maintains Premonition's paired append-only `BUILDLOG.md` and `DEVLOG.md`: an evidence-backed session handoff and Sol provenance record alongside a candid builder diary. It includes deterministic validation for structure, pairing, and append-only integrity.

Invoke it directly with `$maintain-premonition-build-log` at session boundaries, phase transitions, compaction checkpoints, owner decisions, verification results, deviations, failures, or blockers.

## Status

`v0.0.7` adds Open-Source PR Preflight for respectful, evidence-backed contribution readiness before publication.

## Principles

- Focus each skill on one defensible job.
- Prefer truthful evidence over impressive but unsupported claims.
- Keep reusable instructions concise and load detailed guidance only when needed.
- Use deterministic scripts for fragile validation steps.
- Depend on maintained specialist plugins instead of vendoring their knowledge.
- Let skills graduate from the toolkit when independence creates real value.

## Licence

Apache License 2.0. See [LICENSE](LICENSE).
