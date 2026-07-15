# Frontend doctrine

## Direction and composition

Derive the direction from the product narrative. Editorial authority, neo-brutalist industry, luxury restraint, retro-futurist CRT, organic tactility, punk collage, Bauhaus precision, and controlled psychedelia are territories, not presets.

- Avoid the centered hero, three rounded feature cards, icon row, and generic CTA sequence.
- Use a consistent grid with at least one intentional break.
- Use asymmetry when it clarifies hierarchy; do not confuse novelty with disorder.
- Preserve narrative rhythm when the layout transforms across viewport sizes.
- Use one dominant visual idea rather than several unrelated flourishes.

## Signature element

Valid patterns include a state-bearing frame, spatial navigation, branded data language, a typographic navigation system, a meaningful orchestrated reveal, or a texture system that communicates hierarchy and focus. Custom cursor behavior is valid only when it improves discoverability and never impairs ordinary input.

## Token foundation

Define equivalent semantic tokens before layout. Adapt this inventory to the framework rather than copying it mechanically:

```css
:root {
  --color-bg:; --color-surface:; --color-text:; --color-muted:;
  --color-accent:; --color-focus:; --color-success:;
  --color-warning:; --color-danger:;

  --font-display:; --font-body:; --font-mono:;
  --text-xs:; --leading-xs:; --text-sm:; --leading-sm:;
  --text-base:; --leading-base:; --text-lg:; --leading-lg:;
  --text-xl:; --leading-xl:; --text-2xl:; --leading-2xl:;

  --space-1:; --space-2:; --space-3:; --space-4:;
  --space-6:; --space-8:;
  --radius-sm:; --radius-md:; --radius-lg:;
  --shadow-sm:; --shadow-md:; --shadow-lg:;
  --duration-fast:; --duration-base:; --duration-slow:;
  --ease-out:; --ease-spring:;
}
```

Use role names rather than appearance names. Components consume tokens; do not scatter one-off values through component files.

## Typography, palette, and icons

- Avoid Inter, Roboto, Arial, and generic system stacks as the primary visual voice unless preserving an established system requires them.
- Pair a characterful display face with a refined, readable body face. Tune optical size, weight, letter spacing, line height, and measure intentionally. Provide robust fallbacks that preserve tone.
- Use typographic contrast as a primary design tool.
- Establish one dominant hue and one to three accents with defined semantic roles.
- Reject the purple-gradient-on-white SaaS default and recognizable AI-product styling.
- Add dark mode only when it strengthens the thesis or the product requires it.
- Do not use emoticons as icons. Use one coherent icon system or a purpose-made graphical language.

## Motion and material

- Use motion to communicate structure, continuity, feedback, or affordance.
- Prefer one orchestrated entrance over scattered micro-animation. Use scroll reveal only when sequence matters.
- Prefer transform and opacity. Honor `prefers-reduced-motion` with a complete static behavior.
- Lazy-initialize canvas, WebGL, particles, and other costly effects; provide a lower-capability mode.
- Avoid sterile flatness unless austerity is the thesis. Grain, SVG patterns, noise gradients, paper shadows, scanlines, or procedural texture may support hierarchy.
- Maintain one consistent depth language. Use glass only as a committed and readable system.

## Production behavior

- Use semantic HTML; add ARIA only when native semantics are insufficient.
- Support complete keyboard navigation with integrated `:focus-visible` styling.
- Keep mobile touch targets at least 44 by 44 CSS pixels.
- Author validation and recovery messaging for forms.
- Design network failure, offline, delayed, partial-data, and user-error recovery. Never rely on silent failure or default browser error presentation.
