# @tcballard Codex Toolkit

**A working set of sharp, evidence-led Skills for building and shipping with Codex.**

[![Plugin version](https://img.shields.io/badge/plugin-v0.0.14-24292f?style=flat-square)](.codex-plugin/plugin.json)
[![Skills](https://img.shields.io/badge/skills-19-cb5c35?style=flat-square)](skills)
[![License](https://img.shields.io/badge/license-Apache--2.0-2f6f67?style=flat-square)](LICENSE)

@tcballard Codex Toolkit packages 19 focused workflows for product design, repository polish, community research, launch preparation, visual production, project orchestration, and macOS delivery. Each Skill owns a narrow job, verifies what it can, and hands specialist implementation to the right capability instead of hiding broad prompts behind polished names.

### Install

```bash
codex plugin marketplace add tcballard/CodexToolkit
codex plugin add tcballard-toolkit@tcballard-toolkit
```

Start a new Codex session after installation, then invoke a Skill directly—for example, `$readme-front-door`, `$launch-pack`, or `$authored-macos-design`. In the ChatGPT desktop app, the same marketplace is available from **Plugins** after it has been added and the app restarted.

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

### Community Radar

Finds and ranks current communities, discussions, unanswered questions, complaints, alternative requests, and participation opportunities using dated public evidence and transparent anti-spam scoring.

It owns audience inference, community fit, conversation verification, opportunity ranking, participation posture, and the ordered next-step plan. `last30days` can supply emerging discussions; Merge & Tell can draft communication after an opportunity is chosen; Launch Pack remains responsible for coordinated launches.

Invoke it directly with `$community-radar` when deciding where a project can earn attention by joining the right conversation.

### AsDecided Publishing Suite

Three linked skills turn first-party product and audience evidence into durable AsDecided content without creating a content farm:

- `$asdecided-content-radar` ranks evidence-backed opportunities and refresh work;
- `$asdecided-publishing` develops technically credible, citation-worthy canonical pages;
- `$asdecided-distribute` turns an approved source into a small set of faithful channel-native derivatives.

Use the individual skill that owns the current stage; none of them publishes automatically.

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

### Technical Product Name Check

Runs a dated, source-linked practical collision and namespace preflight for developer tools, libraries, CLIs, applications, plugins, packages, and open-source projects.

It normalizes candidate variants, chooses current registries from the actual distribution plan, separates exact and near collisions, checks package and command names independently, and returns an explainable risk rating without claiming legal or trademark clearance.

Invoke it directly with `$technical-product-name-check` before adopting or comparing technical product names.

### Visual Asset Adapter

Faithfully reformats approved logos, wordmarks, artwork, and finished compositions for new canvases and destinations without turning adaptation into redesign.

It records source and output hashes, preserves proportions, distinguishes an alpha channel from actual transparent pixels, verifies exact dimensions and bytes, and requires full-size plus destination-preview inspection. Mechanical and explicitly approved compositional changes are supported; semantic image editing remains a separate authorized workflow.

Invoke it directly with `$visual-asset-adapter` to adapt or review an existing source asset.

### macOS App Icon Preflight

Inspects real source artwork for modern macOS app-icon suitability and, where safely authorized, prepares deterministic source variants without silently redesigning the icon.

It measures alpha bounds and edge clearance, flags likely pre-baked masks and external halos as heuristics for visual confirmation, renders a labeled small-size preview grid, refreshes version-sensitive claims from current Apple sources, and keeps design, Xcode integration, and release readiness separate.

Invoke it directly with `$macos-app-icon-preflight` before handing icon artwork to Xcode or Build macOS Apps.

### Project Skill Scaffold

Generates and safely refreshes lean `build-<project>` orchestration Skills from stable specifications and inspectable repositories.

Its hard stability gate rejects vague ideas; its generator produces authority, milestone, repository, source-provenance, state-inspection, and validation contracts without copying large specifications or embedding transient completion. Refreshes always write a separate candidate and diff, preserve unmanaged files, and protect detected hand edits.

Invoke it directly with `$project-skill-scaffold` when a long-running project needs a reusable, extraction-safe session orchestrator rather than another one-off handoff.

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

### Write X Bangers

Writes, rewrites, critiques, and plans X posts and threads using X's published recommendation-system mechanics as editorial constraints rather than a promise of reach.

It targets a recognisable audience, leads with a self-contained idea, keeps factual proof close to the claim, creates an honest reply or share surface, verifies X's weighted 280-character limit, and avoids hype, engagement bait, hashtag piles, and invented evidence. Its dated source snapshot correctly treats ranking weights as coefficients on personalised action predictions—not raw engagement-count equivalences.

Use `$write-x-bangers` when the destination is X and distribution mechanics matter. Use `$merge-and-tell` for broader public product communication.

### Build Premonition

Runs specification-led GPT-5.6 Sol sessions for the Premonition macOS menu-bar app. It establishes the authoritative specification and repository state, enforces phase entry and exit criteria, routes native implementation through the appropriate macOS workflows, protects the product's safety invariants, and records exact verification and provenance.

Invoke it directly with `$build-premonition` when starting, resuming, implementing, reviewing, testing, packaging, or preparing a submission for Premonition.

### Maintain Premonition Logs

Maintains Premonition's paired append-only `BUILDLOG.md` and `DEVLOG.md`: an evidence-backed session handoff and Sol provenance record alongside a candid builder diary. It includes deterministic validation for structure, pairing, and append-only integrity.

Invoke it directly with `$maintain-premonition-build-log` at session boundaries, phase transitions, compaction checkpoints, owner decisions, verification results, deviations, failures, or blockers.

## Status

`v0.0.14` adds Write X Bangers for evidence-led, recommendation-aware X posts and brings the catalog metadata in sync with the 19 packaged skills.

## Principles

- Focus each skill on one defensible job.
- Prefer truthful evidence over impressive but unsupported claims.
- Keep reusable instructions concise and load detailed guidance only when needed.
- Use deterministic scripts for fragile validation steps.
- Depend on maintained specialist plugins instead of vendoring their knowledge.
- Let skills graduate from the toolkit when independence creates real value.

## Licence

Apache License 2.0. See [LICENSE](LICENSE).
