---
name: visual-asset-adapter
description: Faithfully inspect, resize, pad, crop, compress, reformat, or review an existing approved visual asset for a specified destination while preserving its identity. Use for transparent README banners, profile banners, documentation headers, release cards, platform crops, and verified format variants. Do not use when no real source exists, for brand exploration or redesign, for GitHub-specific social-preview storytelling, or for macOS icon suitability.
---

# Visual Asset Adapter

Adapt the approved design; do not reinterpret it. Work in one of two modes: **Adapt** creates a verified derivative, while **Review** compares an existing derivative with its source and destination contract.

Read [transformation-contract.md](references/transformation-contract.md) before changing pixels, use [target-profiles.md](references/target-profiles.md) to establish destination constraints, and apply [quality-gates.md](references/quality-gates.md) before delivery.

## Establish the source contract

When repository-bound, first read repository instructions and inspect the branch and worktree. Locate and open the real source asset. If several assets conflict, establish which one is authoritative rather than blending them.

Require:

- a readable source asset;
- target platform or exact canvas dimensions;
- output format and transparency behavior;
- permitted transformation class: mechanical, compositional, or semantic;
- approved copy, file-size ceiling, safe area, background, and destination when applicable.

Inspect the source with:

```bash
python3 scripts/inspect_image.py path/to/source.png
```

Record dimensions, aspect ratio, signature/format, mode, bytes, SHA-256, alpha-channel presence, transparent-pixel presence, alpha/visual bounds, frames, and color-profile presence. Open and visually inspect it. Identify immutable logo geometry, wordmark typography, product name, colors, motifs, and embedded copy.

Stop if the source is missing, unreadable, corrupt, opaque to available tooling, or too small for a credible output. A description is not an approved visual source.

## Define the target contract

Resolve exact canvas, format, bytes, transparency, safe area, crop behavior, background, destination, and allowed changes. For any transform that changes placement or surrounding space, write a short composition plan first.

Choose the least invasive operation:

1. proportional resize;
2. transparent or approved-color padding;
3. crop only expendable surrounding area;
4. reposition or extend an approved background without altering the core;
5. place exact approved copy deterministically with a real font only when explicitly authorized;
6. compress after composition.

Mechanical and approved compositional work belong here. Reconstruction, inpainting, generated extension, subject alteration, and other semantic edits require explicit authorization and an image-editing workflow. Never use generation for the final logo, wordmark, or exact typography.

## Adapt

Use the bundled utility for proportional `contain` or `cover` placement:

```bash
python3 scripts/adapt_image.py source.png output.png \
  --width 1280 --height 640 --fit contain --background transparent
```

The utility never stretches, refuses to overwrite its source, records exact transform evidence, and capability-checks Pillow. Use `--anchor` and `--safe-area` only after documenting why the placement is permitted. Treat `cover` as destructive cropping: use it only when the expendable region is known.

Do not overwrite the original by default. Re-hash the source after export.

## Review

Inspect both source and adaptation. Compare core proportions, visual bounds, alpha semantics, sharpness at intended size, approved copy, palette, protected content, crop previews, and bytes. Automated geometry is evidence, not proof of identity or visual quality. Call out distortion, approximation, blur, crop loss, alpha failures, or unsupported claims explicitly.

## Verify

Run:

```bash
python3 scripts/verify_image.py output.png \
  --width 1280 --height 640 --max-bytes 1000000 \
  --source source.png --require-alpha --require-transparent
```

Verify that source and output open, exact dimensions/format/bytes meet the contract, required alpha and actual transparency both exist, protected bounds remain inside the safe area, and the source hash is unchanged. Inspect full size and at least one representative destination preview; inspect every named crop when the platform has multiple crops. Revise failures.

## Repository and publication boundary

Save to the requested path or a non-destructive sibling. Modify README, code references, commits, pushes, or platform settings only when explicitly requested. For repository delivery, use a focused branch, validate paths and diff, and hand off to the authorized delivery workflow. Never commit directly to the default branch.

## Deliver

Provide source and output paths and hashes; dimensions, format, mode, alpha state, and actual bytes; immutable elements and allowed transforms; exact transform/compression parameters; safe-area and crop findings; full-size and reduced-preview observations; automated and manual checks; and unresolved limitations. Never claim fidelity, transparency, crop safety, or quality from an automated check alone.
