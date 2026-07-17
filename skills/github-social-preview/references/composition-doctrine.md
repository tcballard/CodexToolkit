# GitHub social-preview composition doctrine

## Source-of-truth order

1. Repository instructions and explicit user requirements.
2. Exact logo, wordmark, icon, and brand assets in the repository.
3. Confirmed product facts, product name, tagline, and supporting line.
4. Established palette, typography, and visual motifs.
5. Product-specific art direction.
6. Newly generated supporting imagery.

Generated content never outranks an existing brand asset.

## Canvas and safe area

- Canvas: exactly 1280 × 640 pixels.
- Default safe margin: at least 64 pixels on every edge.
- Keep the primary logo, product name, and tagline within a more conservative 80-pixel inset when the composition permits.
- Use one clear focal region and one supporting region; avoid evenly distributing many small objects.
- Judge balance at 1280 × 640 and 640 × 320.

## Deterministic construction

Prefer a composition that can be reproduced from source layers:

- SVG with an exact linked or embedded repository asset plus real text;
- HTML/CSS rendered at a fixed viewport;
- a graphics script using installed fonts and the original asset;
- an established design-tool file when available.

Use the original logo file directly. Preserve its aspect ratio and colours. Do not trace, redraw, prompt-recreate, stretch, skew, or apply destructive effects that obscure its identity.

Render all final text deterministically. Confirm the actual font file or installed family used. Do not rely on image generation for letters, punctuation, terminal prompts, code, or wordmarks.

## Image-generation boundary

Image generation is suitable for:

- an original abstract background;
- a large supporting illustration;
- texture, atmosphere, or material;
- a brand-compatible conceptual visual.

Exclude from the generated layer:

- logo and wordmark;
- product name, tagline, supporting line, and labels;
- code, terminal content, UI, badges, and measurements;
- third-party marks;
- any detail intended to prove product behavior.

Crop or mask generated imagery as a supporting layer, then place exact assets and text afterward.

## Typography

- Make the product name and tagline readable at 50% scale.
- Prefer one display treatment plus one restrained supporting treatment.
- Use short line lengths and intentional line breaks.
- Avoid tiny feature lists and paragraph copy.
- When the supporting line adds no new value, omit it.
- Preserve exact supplied punctuation and capitalization.

## Palette and material

- Derive the limited palette from repository assets.
- Assign clear roles: background, primary text, secondary text, brand accent, and optional material/texture.
- Maintain strong contrast without defaulting to glow.
- Use gradients only when they belong to the existing identity or materially support depth.
- Keep textures subtle enough that type and logo remain crisp after compression.

## Compression

The final PNG must be below 1,000,000 bytes.

1. Export a clean 1280 × 640 PNG.
2. Remove unnecessary metadata.
3. Try lossless optimization with an available tool such as `oxipng`, `pngcrush`, or ImageMagick.
4. If still too large, use high-quality palette quantization such as `pngquant --quality 85-100 --speed 1`.
5. Re-run validation and visually inspect full size and the 50% thumbnail.

Never satisfy the byte limit by changing the required dimensions or accepting obvious banding, broken transparency, smeared type, or damaged logo edges.
