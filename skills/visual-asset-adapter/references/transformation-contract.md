# Transformation contract

Classify every requested change before editing.

| Class | Examples | Skill behavior |
|---|---|---|
| Mechanical | proportional resize, format conversion, padding, lossless optimization, metadata cleanup | supported when the target is explicit |
| Compositional | reposition, crop expendable space, extend an approved background, safe-area adaptation, authorized text placement | supported after a written composition plan |
| Semantic | reconstruct, inpaint, redraw, alter subjects, generated extension | route to explicit image editing; never perform silently |

## Immutable core

Record the source-of-truth file and SHA-256. Treat logo geometry, wordmark typography, product name, approved copy, brand colors, proportions, and signature motifs as immutable unless the user names a permitted change.

The adapter may change the canvas around the core. It must not redraw, approximate, recolor, distort, or replace the core. Embedded raster text is not editable typography.

## Composition plan

Before compositional work, state:

- source and output paths;
- protected core and source priority;
- target canvas, format, background, bytes, and safe area;
- fit mode, scale, anchor, crop, and padding;
- every added element and its approval source;
- preview crops to inspect;
- known fidelity risks.

`contain` preserves all source pixels and adds surrounding space. `cover` fills the canvas by removing source edges and is permitted only when those edges are confirmed expendable. Non-proportional stretching is never permitted.

## Compression

Optimize only after composition. Lossless PNG optimization is preferred for logos, transparency, and sharp graphics. JPEG/WebP quality reduction may be used only when the target format permits it and must be reported. If a byte ceiling cannot be met without visible or identity-damaging degradation, fail and offer explicit trade-offs.
