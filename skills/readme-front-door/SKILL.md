---
name: readme-front-door
description: Improve, rewrite, or audit only the opening portion of a repository README so a visitor can understand the product within seconds. Use when Codex is asked to add or refine a README banner, title, tagline, concise product explanation, primary install or use command, proof point, demo link, or justified status and compatibility badges; fix the README above-the-fold experience; or validate relative asset paths in that opening block. Do not use for full README generation, documentation architecture, release notes, API documentation, or unsupported marketing copy.
---

# README Front Door

Make the repository's opening block answer, within seconds: what is this, who is it for, why is it different, and how do I try it? Change only that front door. Preserve the rest of the README unless the user explicitly expands scope.

Read [front-door-doctrine.md](references/front-door-doctrine.md) before drafting. Read [quality-gates.md](references/quality-gates.md) before delivery.

## Establish the evidence

1. Locate the repository root and read its instructions, including `AGENTS.md` or equivalents.
2. Inspect the complete README before editing its opening.
3. Inspect package manifests, product documentation, release metadata, licence, compatibility declarations, tests, demo destinations, and existing brand assets relevant to the front door.
4. Run `git status --short` and preserve unrelated changes.
5. Record the exact product name, audience, confirmed outcome, differentiator, primary command, strongest proof, demo destination, compatibility, status, and usable asset paths.

Do not ask the user to repeat facts already established by the repository. Ask only when a missing fact would force invention or materially change the front door.

## Define the boundary

The front door begins at the first README line and ends before the first substantive documentation section, such as features, concepts, configuration, usage detail, development, contributing, or licence.

It may contain only what earns a place there:

- approved hero, banner, screenshot, or social asset;
- product title;
- exact or evidence-backed tagline;
- one short explanatory paragraph;
- one primary install or first-use command;
- one key proof point;
- one demo link;
- a restrained set of authoritative status or compatibility badges.

Not every repository needs every item. Omit unsupported, redundant, stale, or distracting elements. Do not rearrange or rewrite content below the boundary merely to make the opening edit easier.

## Build the message hierarchy

Choose the order that best serves the repository rather than applying a fixed template. Ensure the opening communicates:

1. **Identity:** the exact product name and a specific, non-cringe tagline.
2. **Comprehension:** one paragraph stating what the product does, who it helps, and the meaningful distinction.
3. **Action:** the shortest verified install or first-use command, ready to copy.
4. **Credibility:** one concrete, repository-supported proof point or visible demonstration.

Prefer plain, confident language. Remove vague superlatives, breathless claims, empty mission language, and repeated phrasing. Never invent adoption, performance, compatibility, security, maturity, or availability claims.

## Use assets and badges carefully

- Reuse exact repository assets; do not redraw, recolour, distort, or approximate brand marks.
- Use paths relative to the README location, with exact filename case. Prefer repository-owned assets that render on GitHub and forks.
- Add alt text that identifies or explains meaningful images. Use empty alt text only for truly decorative imagery.
- Keep screenshots large enough to read and place them near the claim they prove.
- Use `github-social-preview` when the requested artifact is specifically a new GitHub social-preview image. Do not silently substitute social artwork for a README hero if its composition does not suit the document.
- Add a badge only when its source is authoritative, its destination is useful, and its status is current. Avoid badge walls and vanity counters.

## Edit narrowly

Patch only the front-door block. Preserve useful anchors, reference definitions, HTML needed for alignment, and the established Markdown style. Keep installation commands consistent with the repository's actual package manager, executable, target, and supported environment.

When installation is conditional or unusually long, show the primary path and link to existing detail below. Do not duplicate a full setup guide at the top.

## Validate

Run the repository's relevant documentation or link checks when available. Then run:

```bash
python3 scripts/audit_front_door.py README.md
```

The script checks the opening block for a title, unresolved placeholders, and broken local Markdown or HTML asset paths. It reports external links for manual verification; it does not prove claims, judge tone, or guarantee remote link availability.

Review the rendered README or a faithful preview when tooling permits. Apply every gate in [quality-gates.md](references/quality-gates.md), inspect the diff to confirm the boundary held, and revise any failure.

## Deliver

Report the changed README path, the front-door elements added or refined, evidence used for material claims and commands, validation performed, and any deliberately omitted element. State whether any commit or push was made.
