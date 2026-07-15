# macOS quality gates

Reject and revise the output if any gate fails.

## Native integrity

- The scene and surface model matches the product's working model.
- Pointer, keyboard, menus, commands, focus, windowing, resizing, restoration, and accessibility are treated as first-class design.
- Standard controls remain native unless custom behavior is functionally necessary and complete.
- SwiftUI owns the interface and state unless a named platform gap justifies a narrow AppKit bridge.
- The result is not a web, Tauri, Electron, or iOS composition wearing macOS colors.

## Authored coherence

- One clear narrative governs hierarchy, density, palette, typography, materials, symbols, motion, and copy.
- The signature element improves the task and does not compete with native behavior.
- Semantic tokens coordinate brand decisions without overriding native metrics.
- Every surface has a distinct role; rounded cards are not used as universal grouping.
- Verified brand assets are used faithfully; no emoji, invented mark, fake illustration, or unexplained production placeholder substitutes for missing artwork.

## Complete states

- Default, hover, pressed, key focus, inactive window, disabled, loading, empty, unavailable, error, permission, offline, partial, destructive, and recovery states exist where applicable.
- Light/dark appearance, increased contrast, differentiated-without-color, Reduce Motion, and Reduce Transparency remain coherent.
- Empty and error states offer a clear next action in the established voice. No silent or default-framework failures remain.

## Material integrity

- Material choices match the deployment target.
- Older targets do not receive fake Liquid Glass.
- Modern glass begins with standard structure and controls; custom glass is grouped, semantic, readable, and limited to appropriate chrome or interaction surfaces.
- Opaque fills, decorative tints, blur stacks, and custom shadows do not fight system hierarchy.

## Final evidence

- The relevant scheme or package builds.
- The running app or previews were inspected at representative sizes and appearances when tooling permits.
- The rendered result passes every lens in `design-review.md`; weak lenses were revised rather than averaged away behind an overall score.
- Keyboard-only operation and accessibility semantics were checked.
- The output contains production copy and complete requested behavior, not a static concept facade.
