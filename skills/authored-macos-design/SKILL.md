---
name: authored-macos-design
description: "Design, implement, restyle, or substantially refactor distinctive native macOS interfaces in SwiftUI and AppKit using an authored-shell approach: preserve native controls, behavior, windowing, focus, commands, accessibility, and desktop density while giving composition, hierarchy, materials, iconography, data presentation, motion, and functional signature elements a strong point of view. Use for Mac apps, menu-bar utilities, popovers, panels, settings, inspectors, and desktop workflows where a web layout in a window or generic SwiftUI scaffold is unacceptable. Apply target-aware Liquid Glass rules: never fake it for older targets and adopt system glass deliberately on supported targets. Do not use for web frontends, iOS-first interfaces, logic-only work, or exact visual cloning."
---

# Authored macOS Design

Design a Mac app, not a website inside a window. Preserve the platform's behavioral contract while making the product unmistakably authored.

Read [references/native-doctrine.md](references/native-doctrine.md) before selecting a direction. Read [references/surface-patterns.md](references/surface-patterns.md) for the relevant scene or surface. Use [references/design-review.md](references/design-review.md) when evaluating a rendered interface. Read [references/quality-gates.md](references/quality-gates.md) before delivery.

## Governing hierarchy

Resolve design decisions in this order:

1. Product working model and user task.
2. macOS behavior, accessibility, focus, commands, and window semantics.
3. Existing architecture, deployment target, brand anchors, and supplied visual source of truth.
4. Authored art direction and functional signature element.
5. Decoration.

Never sacrifice a higher layer to make a lower layer more visually novel.

## Workflow

1. Ground the native context.
   - Inspect the app structure, deployment target, current scenes, state ownership, AppKit bridges, menus, commands, assets, screenshots, and requirements.
   - Identify the app model: document, editor, sidebar-detail, utility window, menu-bar-only, menu-bar plus windows, settings, inspector, or a deliberate combination.
   - Inventory the actual logo, app icon, symbols, imagery, palette, typography, and existing tokens. Do not invent substitutes for missing brand assets.
   - Resolve source priority explicitly: product requirements and selected visual reference first, established brand system next, current implementation last. Recompose features into the chosen system rather than treating existing layout as truth by default.
   - Ask only for missing information that blocks correct scene or interaction behavior.

2. Write the native art-direction brief.
   - Define tone, hierarchy, density, palette roles, type treatment, material policy, motion grammar, surface roles, and one functional signature element.
   - When the user requests exploration, produce two or three structurally different directions rather than palette swaps, then lock the selected direction. Otherwise choose one direction and commit without presenting a menu of safe options.
   - Keep SF Pro and standard control typography unless a brand-bearing presentation surface clearly earns a custom face.
   - Make the signature element improve status, navigation, selection, comparison, editing, or feedback. It may not justify rebuilding standard controls.

3. Establish the authored shell.
   - Use native scene, window, panel, toolbar, sidebar, inspector, sheet, menu, focus, and command behavior.
   - Place distinctiveness in composition, spatial rhythm, controlled grid breaks, material boundaries, icon treatment, branded data language, and state transitions.
   - Prefer SwiftUI for composition and state. Cross into AppKit only through the smallest boundary required for mature Mac behavior.

4. Define semantic tokens and state language.
   - Centralize brand and status colors, spacing, shape, depth, typography roles, icon configuration, and motion timing.
   - Use system metrics where control behavior depends on them. Tokens coordinate authored choices; they do not replace platform intelligence.
   - Define active/inactive window, key focus, hover, pressed, disabled, loading, unavailable, empty, error, permission, offline, partial, destructive, and recovery treatments.

5. Build complete desktop behavior.
   - Support pointer, keyboard traversal, standard shortcuts, menu commands, default/cancel actions, Escape, focus restoration, resizing, persistence, and multiple windows where applicable.
   - Keep compact desktop density. Do not inflate a utility into touch-first card stacks.
   - Use real copy that fits the surface. Keep menu and popover text scannable and move detail into an appropriate window.

6. Verify the running app.
   - Build the relevant Xcode scheme or Swift package and inspect the app or previews at representative sizes.
   - Capture or inspect rendered evidence for the primary, empty, loading, error, and inactive-window states where applicable. Review the evidence through narrative alignment, hierarchy, craft, native task fitness, and distinctiveness.
   - Exercise keyboard-only operation, VoiceOver semantics where tooling permits, light/dark appearance, active/inactive windows, increased contrast, differentiated-without-color, Reduce Motion, Reduce Transparency, and every failure path.
   - Apply every rejection gate and revise failures before delivery.

## Delivery

Lead with the completed outcome. Include the native art-direction brief when useful, complete runnable code or edited files, verification evidence, and concise extension notes for tokens, scenes, or AppKit boundaries that future work must preserve.
