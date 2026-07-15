---
name: product-demo
description: Plan, stage, edit, and verify evidence-grounded product demonstration videos from real application footage, using code-defined editing and optional Remotion skills. Use when Codex needs to create or revise an app demo, competition or Devpost submission video, launch walkthrough, README video, product tour, narrated screen recording, or short social cut; or when it must produce a narrative, claims ledger, shot list, recording checklist, edit, captions, render, or video QA. Do not use for fictional cinematic generation, general-purpose film editing, or image-only social artwork.
---

# Product Demo

Direct the whole product-demo workflow while keeping the demonstrated product truthful, legible, and central. Treat code-defined editing as the source of truth and external software as rendering machinery.

## Non-negotiables

- Ground every product claim in supplied evidence or visibly demonstrated behavior.
- Use genuine application footage for claimed interactions. Never manufacture a successful state that the application did not produce.
- Preserve the viewer's ability to understand what happened; do not hide material waits, failures, or limitations with misleading cuts.
- Keep secrets, personal data, notifications, account identifiers, and unrelated applications out of frames and metadata.
- Keep editorial decisions attributable to the selected model when model provenance matters. Do not silently delegate creative judgment to another AI service.
- Never publish, upload, commit, push, or overwrite source footage unless the user explicitly asks.

Read [truth-and-provenance.md](references/truth-and-provenance.md) whenever claims, competition rules, AI provenance, or public publication matter.

## Choose the working mode

Infer the narrowest mode that completes the request:

- **Plan:** Create the brief, narrative, claims ledger, timing, and shot list.
- **Capture:** Prepare deterministic product state and a recording checklist.
- **Edit:** Inspect supplied media and implement a reproducible edit.
- **Review:** Audit an existing cut and produce a prioritized QA report.
- **End to end:** Run all stages, pausing only when real footage, narration, credentials, or a consequential user choice is genuinely required.

Do not force an editing project when the user only wants a script or review.

## Establish the contract

Before creative work, determine:

1. Product, audience, and desired viewer action.
2. Distribution surface and hard duration or format limits.
3. Authoritative product evidence: specification, source, build logs, README, tests, submission rules, and existing brand assets.
4. Available footage, narration, music, screenshots, and logos.
5. Required proof, prohibited claims, privacy boundaries, and disclosure requirements.
6. Whether the edit must maximize or document a particular model's contribution.

Ask only for missing information that materially changes the result. When evidence is available locally, inspect it instead of asking the user to restate it.

## Create the pre-production pack

Use the templates in `assets/templates/` when useful. Follow [narrative-and-capture.md](references/narrative-and-capture.md).

Default to a `demo-video/` working directory unless the repository already defines another location. Produce only the files needed for the selected mode:

- `DEMO_BRIEF.md`
- `CLAIMS_LEDGER.md`
- `SHOT_LIST.md`
- `RECORDING_CHECKLIST.md`
- `EDIT_DECISIONS.json`
- `QA_REPORT.md`

The narrative must show the product's meaningful outcome early. Prefer one complete, understandable workflow before explanatory replays or architecture detail.

If the requested edit requires footage that does not exist, finish the recording pack and pause. State exactly which clips are needed and how each will be judged usable.

## Prepare and capture the application

- Create deterministic fixtures and reset scripts only when authorized and within the product repository.
- Rehearse the shortest honest route through the workflow.
- Record actions in separate takes with handles before and after each interaction.
- Capture failure, safety, or control states when they substantiate important claims.
- Keep pointer movement deliberate and important text readable at the target resolution.
- Record clean source footage; add zooms, callouts, captions, and framing during editing.

For macOS products, preserve native density and behavior. Do not turn the application into a generic web-style mockup in post-production.

## Inspect supplied media

Check for `ffprobe` and `ffmpeg` before running bundled helpers. If missing, explain the dependency and ask before installing anything.

```bash
python3 scripts/media_inspect.py footage.mp4 --output media.json
python3 scripts/create_contact_sheet.py footage.mp4 contact-sheet.jpg
```

Inspect contact sheets or extracted frames as image inputs. Do not assume a filename or duration proves that a clip contains the expected interaction.

## Implement the edit

Read [remotion-companion.md](references/remotion-companion.md) before creating or modifying a Remotion project.

1. Prefer the official Remotion plugin and its maintained skills when they are installed.
2. Do not copy or vendor Remotion's skills into this skill.
3. If Remotion support is absent, continue planning and review work. Before implementation, recommend the official plugin or use the documented Remotion CLI only with the user's approval for new dependencies.
4. Keep the edit as code: timing, crops, captions, callouts, audio levels, and transitions must be reproducible.
5. Preserve untouched source footage outside the render directory.
6. Use restraint. The demonstrated product—not decorative motion—is the spectacle.

When available and relevant, use companion skills rather than duplicating them:

- Use `merge-and-tell` for public-facing voice and concise launch copy.
- Use an authored native-design skill to preserve the application's visual character.
- Use the project's build-log or provenance skill to record verified model contributions.

## Render and review

Render a review copy before the final export. Follow [review-standard.md](references/review-standard.md).

```bash
python3 scripts/validate_export.py review.mp4 \
  --max-duration 180 \
  --width 1920 \
  --height 1080 \
  --expected-fps 30 \
  --require-audio
```

Review representative frames at minimum from:

- the opening hook;
- every major product-state transition;
- every title or caption treatment;
- the closing frame;
- any cut where privacy or misleading continuity is plausible.

Iterate until hard gates pass. Do not describe an export as final when a required gate remains unresolved.

## Handoff

Report:

- final path, duration, dimensions, frame rate, and codec;
- source footage used and omitted;
- factual or visual limitations that remain;
- validation performed and its outcome;
- files the user should review;
- model contribution suitable for the project's provenance record.

Separate verified facts from editorial judgments. If publication is not explicitly requested, stop with the finished local artifact.
