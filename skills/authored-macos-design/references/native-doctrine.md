# Native macOS doctrine

## Authored shell

Keep standard macOS behavior familiar and make the shell distinctive. The shell comprises composition, hierarchy, density, surface relationships, materials, iconography, data presentation, copy voice, and motion continuity. Standard controls remain standard unless a product-specific capability cannot be expressed otherwise.

- Prefer native grouping, alignment, separators, tables, lists, split views, inspectors, and negative space over universal rounded cards.
- Use one intentional compositional break only where it strengthens task hierarchy.
- Keep chrome minimal, purposeful, and appropriate to the surface.
- Treat compact menu-bar utilities as information-dense tools, not miniature landing pages.
- Reject literal ports of Tauri, Electron, web, or iOS layouts. Preserve features and workflow, then recompose them through macOS scene and interaction patterns.

## Source of truth and asset integrity

Resolve conflicts in this order: product behavior and requirements, the visual direction selected by the user, verified brand assets and tokens, platform conventions, then the current implementation. Existing code is evidence of available functionality, not automatic authority over the new composition.

- Use real logos, icons, illustrations, and imagery. Never approximate a brand mark with text, emoji, an improvised SF Symbol, or an AI-drawn vector.
- If a required asset is unavailable, ask for it. A clearly labelled neutral placeholder is acceptable only in an explicit prototype and must not survive production delivery.
- Treat supplied screenshots as visual evidence: identify their hierarchy, density, materials, geometry, and state language, then recompose the required functionality inside that system.
- When exploring directions, change structure, hierarchy, density, and signature behavior—not merely palette or corner radius.

## Expressiveness without convergence

Avoid repeated patterns that reveal the tool rather than the product:

- universal rounded cards as the only grouping device;
- centered welcome or marketing heroes in working application surfaces;
- decorative purple-blue gradients, default blue tint, or neon-on-charcoal chosen by habit rather than brand meaning;
- emoji or mismatched symbol weights as functional iconography;
- stock abstract illustrations, fake logos, and invented filler assets;
- asymmetry, oversized type, blur, or glass applied without task-level purpose.

These are anti-default rules, not substitute defaults. Do not force warm neutrals, serif headings, asymmetry, or a custom accent onto every product. A direction is successful because its choices form a coherent narrative, not because it uses a preferred recipe.

## Typography, color, and symbols

- Prefer SF Pro through semantic SwiftUI text styles for controls, lists, tables, settings, utilities, and data-dense work.
- Use weight, width, monospaced digits, alignment, measure, and restrained scale to create hierarchy.
- Permit a custom display face only on a brand-bearing editorial or presentation surface with appropriate licensing and bundling.
- Use semantic and asset-catalog colors that adapt across appearance and accessibility settings. Never hard-code a light-mode assumption.
- Give one dominant accent a clear role and reserve additional colors for selection, status, or meaning. Avoid decorative rainbow tinting.
- Prefer SF Symbols for exact standard actions and objects. Configure weight, scale, rendering, and accessibility labels intentionally. Use custom symbols for genuinely product-specific concepts.

## Token foundation

Use a compact semantic layer through asset catalogs, environment values, static namespaces, or a theme model:

```swift
enum DesignTokens {
    enum ColorRole { /* canvas, surface, text, muted, accent, focus, status */ }
    enum Space { /* compact project scale with explicit roles */ }
    enum Shape { /* control, group, prominent surface */ }
    enum Depth { /* separator, overlay, floating surface */ }
    enum Motion { /* feedback, transition, reveal, reduced */ }
    enum Symbol { /* point size, weight, rendering by role */ }
}
```

Do not tokenize values owned by native control metrics. A token system should prevent drift, not force every system value through custom abstraction.

Use semantic grouping, progressive disclosure, and content-driven sizing before arbitrary frames. Keep spacing on a deliberate compact scale, but allow optical corrections where typography, symbols, or native metrics require them; mathematical regularity is not a substitute for visual rhythm.

## Target-aware materials

Inspect the deployment target before selecting material APIs.

### Older or cross-version targets

- Do not fake Liquid Glass with hand-built blur, glow, refraction, or translucent capsules.
- Use supported system materials, vibrancy, standard toolbars, sidebars, sheets, popovers, and restrained custom surfaces.
- When newer APIs are optional, provide availability-guarded structure and an intentional fallback with the same hierarchy.
- If the project explicitly targets macOS 14+ and rejects a newer visual system, preserve that decision.

### Supported modern targets

- Update standard app structure and controls before adding custom glass.
- Let system toolbars, sidebars, sheets, search, and controls provide their native material. Remove obsolete opaque fills or scrims that fight the system.
- Use custom glass only for product-specific interactive surfaces that standard controls do not cover.
- Group nearby custom glass elements in the platform's shared glass container so refraction remains coherent.
- Use tint semantically for primary actions, selection, or status—not to decorate every surface.
- Keep content and data as content. Glass is chrome, control, navigation, or a purposeful overlay; it is not the default background for every card.
- Respect Reduce Transparency and increased contrast with a complete, readable alternative.

## Motion grammar

- Launch into a stable working state. Do not import the web convention of animating every region into place.
- Use short, interruptible motion for selection, disclosure, navigation, reordering, task completion, and continuity between related states.
- Avoid perpetual ornamental motion in productivity interfaces.
- Do not make animation the sole carrier of state. Supply reduced-motion behavior without losing spatial meaning.

## AppKit boundary

Prefer SwiftUI scenes, toolbars, commands, inspectors, standard controls, and state. Use AppKit narrowly for capabilities such as `NSStatusItem`, `NSPopover`, non-activating panels, responder-chain behavior, mature text systems, precise window control, or platform gaps.

Name the gap, choose the smallest bridge, keep SwiftUI as the source of truth, and validate lifecycle behavior. Never replace a specified AppKit status-item architecture with generic `MenuBarExtra` advice merely because it is shorter.

## App icon rule

When app-icon work is in scope, supply full-bleed square artwork intended for the macOS mask. Do not bake in an outer rounded-square frame, external drop shadow, or duplicate mask edge. Keep safe padding around the subject and use internal lighting or depth only.
