---
name: github-social-preview
description: Create, audit, and prepare polished 1280×640 GitHub repository social-preview PNG artwork under 1 MB using confirmed product facts, the repository's exact brand assets, deterministic logo and text composition, full-size and thumbnail visual inspection, and strict repository safety. Use when Codex is asked for a GitHub social card, repository link-preview image, Open Graph-style repo artwork, or assets/github-social-preview.png. Do not use for general social posts, profile banners, app icons, logo redesign, fictional branding, or publishing without explicit approval.
---

# GitHub Social Preview

Create one deliberate developer-tool brand image that survives small link previews. Treat the repository as the brand authority, image generation as an optional supporting technique, and deterministic composition as the source of truth for the final artwork.

Read [composition-doctrine.md](references/composition-doctrine.md) before designing. Read [quality-gates.md](references/quality-gates.md) before delivery.

## Establish the contract

Resolve:

- repository URL or local root;
- exact product name;
- one or two sentences of confirmed product facts;
- exact tagline;
- optional supporting line or `NONE`;
- product-specific design direction.

Inspect the repository instead of asking the user to repeat information already present. Ask only for a missing value that would force invention or materially alter the composition.

## Inspect before designing

1. Locate the repository root and inspect `git status --short` without changing it.
2. Read repository instructions such as `AGENTS.md`, then inspect the README and relevant product documentation.
3. Inventory existing logo, icon, wordmark, palette, typography, imagery, and recurring visual motifs.
4. Identify the exact asset paths and decide which asset is authoritative for the composition.
5. Record which product facts and text strings are confirmed by the prompt or repository.

Treat existing brand assets as source material, not inspiration. Do not redraw, approximate, recolour, distort, replace, or ask an image model to reproduce the logo. If no usable brand asset exists, stop and ask whether the user wants a separate identity task or a typographic-only card.

## Commit to one visual idea

Write a compact internal direction covering:

- narrative and focal point;
- palette roles derived from the repository;
- composition and alignment;
- exact logo placement;
- typographic hierarchy;
- background, illustration, texture, or supporting motif;
- small-preview survival strategy.

Use large forms, generous negative space, strong alignment, deliberate spacing, and safe margins. The result should feel authored for this repository rather than generated from a generic developer-tool template.

## Produce the artwork

1. Work at exactly 1280 × 640 pixels.
2. Use image generation only when it materially improves an original background, illustration, texture, or supporting visual concept.
3. When using image generation, exclude the final logo, product name, tagline, supporting copy, fake code, and fake UI from the generated layer.
4. Build the final composition deterministically with a code-native or graphics workflow that can place the exact repository asset and render real text.
5. Use a real installed font. Preserve exact spelling, punctuation, capitalization, colours, logo proportions, and aspect ratio.
6. Keep important content at least 64 pixels from the canvas edge unless the approved brand system specifies a larger safe area.
7. Export the final file as `assets/github-social-preview.png`.
8. If the PNG exceeds 1,000,000 bytes, optimize it losslessly first. If perceptual compression is still required, use the least destructive setting that passes and re-inspect both sizes.

Follow the construction and compression guidance in [composition-doctrine.md](references/composition-doctrine.md).

## Avoid

- generic AI sparkles, brains, robots, neural networks, or default purple SaaS imagery;
- invented product claims, fake code, fake UI, or illegible terminal text;
- third-party logos, trademarks, named individuals, or pre-baked GitHub interface frames;
- excessive gradients, glow, glassmorphism, clutter, or tiny supporting text;
- a cute mascot unless it is already part of the repository identity;
- AI-generated approximations of the logo, wordmark, or final typography.

## Verify and revise

Run:

```bash
python3 scripts/validate_social_preview.py assets/github-social-preview.png
```

The checker verifies PNG format, exact dimensions, byte size, and a temporary 640 × 320 thumbnail. Inspect the full-resolution file and reported thumbnail visually. Confirm:

- product name and tagline remain readable;
- the exact repository logo asset is present and undistorted;
- every text string is spelled and punctuated correctly;
- alignment, spacing, contrast, hierarchy, and safe margins hold;
- the thumbnail retains the intended focal point;
- no unconfirmed content or malformed generated detail appears.

Revise any failure. Do not accept the first generated or composed result automatically.

## Repository safety

Creating `assets/github-social-preview.png` is the only repository change authorized by an artwork request. Do not modify the README, commit, push, alter GitHub settings, publish, or upload the image elsewhere without a later explicit request.

If publication is later approved, follow repository contribution instructions, create a focused branch, add only the approved artwork and explicitly requested documentation, and open a pull request. Never commit directly to `main`. Never create a GitHub issue merely to close it within the same change.

## Deliver

Provide a clickable link to `assets/github-social-preview.png`, exact dimensions, exact byte size, confirmation that full-size and 50% thumbnail checks passed, and confirmation that no commit or push was made.
