---
name: macos-app-icon-preflight
description: Inspect, prepare, review, or hand off actual artwork for modern macOS app-icon suitability using current official Apple guidance and measured image evidence. Use to diagnose baked masks, outer shells, shadows, padding, edge collisions, contrast, small-size legibility, source/export readiness, or an existing Mac project's icon handoff. Do not use for open-ended icon ideation, brand redesign, non-macOS adaptation, Xcode integration alone, signing, notarization, packaging, or App Store clearance.
---

# macOS App Icon Preflight

Determine whether supplied artwork is ready to become a macOS application icon without conflating visual readiness with Xcode integration or release readiness.

Read [apple-requirements.md](references/apple-requirements.md) and refresh its sources for every version-sensitive run. Use [icon-review-rubric.md](references/icon-review-rubric.md) to classify findings and [quality-gates.md](references/quality-gates.md) before delivery.

## Establish the operation

Choose one mode:

- **Inspect:** report source suitability and blockers.
- **Prepare:** make only an authorized deterministic source transformation.
- **Review export:** compare a prepared export with its source contract.
- **Implementation handoff:** give Build macOS Apps or Xcode the verified design evidence and remaining integration work.

Require a real readable source, target macOS version range/distribution context, chosen mode, and whether stylistic or semantic changes are permitted. Inspect repository instructions, deployment target, asset catalogues, `.icon` files, project settings, build/distribution configuration, and brand-source hierarchy when available.

No actual image target means no inspection-specific verdict, generation, or editing. Explain what source is needed and pause.

## Refresh platform facts

Before any version-sensitive claim, open the current official Apple sources listed in [apple-requirements.md](references/apple-requirements.md) or use current Build macOS Apps guidance. Record URLs, checked date, target versions, tool availability, and contradictions. Bundled notes are a source index, not permanent platform truth.

Label every conclusion as one of:

- `Platform rule` — directly supported by a dated current official source;
- `Evidence-backed defect` — measured and visually confirmed in this asset;
- `Subjective craft concern` — professional judgment, not an Apple mandate;
- `Unverified` — insufficient current evidence.

## Inspect the source

Run:

```bash
python3 scripts/inspect_icon.py path/to/icon-source.png
python3 scripts/render_preview_grid.py path/to/icon-source.png /tmp/icon-preview-grid.png
```

The probe reports dimensions, aspect ratio, format, SHA-256, color/alpha state, visual bounds, edge clearance, corner and edge alpha behavior, semi-transparent halo evidence, detail density, and a *likely* baked-mask heuristic. It does not decide platform compliance.

Open the full-size source and preview grid. Distinguish:

- useful internal subject lighting, shading, and dimensionality;
- dynamic/platform material treatment;
- baked outer container, rounded mask, external frame, glow, or drop shadow.

Assess edge clearance, excessive transparent margins, optical balance, contrast, scaling sharpness, and recognition at the grid's representative display sizes. The preview sizes are review conditions, not asset-catalogue slot requirements.

## Prepare only deterministic changes

When authorized, use the least invasive reliable transform: proportional crop/scale/pad, remove a detachable vector/layer mask or outer effect, export approved layers, or clean a background only when exact source pixels make it non-semantic. Soft-use `$visual-asset-adapter` for proportional raster mechanics when installed.

Preserve the central subject, its geometry, brand identity, and useful internal lighting. Never bake the platform mask. If a shell, frame, or shadow is inseparable from a raster subject, stop and provide a specialist editing handoff; a crop is not a faithful removal.

Never overwrite the source by default. Record before/after hashes and exact transforms.

## Verify and hand off

Re-run inspection and the preview grid on prepared output. Compare dimensions, alpha, bounds, edge clearance, sharpness, contrast, small-size recognition, and visual balance. Confirm the central subject and intentional depth remain unchanged.

For an implementation handoff, state:

- project, deployment target, distribution context, and checked date;
- current Apple source links and chosen delivery format;
- approved source and derivative paths/hashes;
- design and export readiness;
- remaining `.icon`/asset-catalogue integration and runtime checks;
- signing, packaging, notarization, and App Store status as not assessed unless separately proven.

Build macOS Apps owns Xcode integration, build/run inspection, signing, packaging, and notarization. Product Design or image editing owns creative exploration and authorized semantic repair. Authored macOS Design owns application interface design.

## Deliver

Return mode, source facts, dated platform evidence, labeled findings, full-size and preview-grid observations, authorized changes, verification results, readiness by layer, unresolved risks, and the next responsible workflow. Never claim App Store or release readiness from visual preflight.
