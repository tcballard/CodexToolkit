# macOS surface patterns

## Choose the surface by job

| Surface | Use for | Avoid |
| --- | --- | --- |
| Menu-bar menu | Short status and immediate commands | Rich layouts, long text, hidden core state |
| Popover | Compact glanceable state and one focused interaction | Multi-step workflows or deep editing |
| Main window | Persistent work, navigation, editing, comparison | Treating the app as a transient oversized popover |
| Utility panel | Supporting controls or information tied to work | Replacing ordinary document or settings windows |
| Inspector | Attributes and actions for current selection | Global navigation or unrelated settings |
| Settings scene | Durable app preferences | Embedding preferences as a main-window destination |
| Sheet | Document- or task-scoped modal work | Generic containers and routine navigation |
| Alert | Consequential interruption or confirmation | Verbose explanations and ordinary validation |

## Menu-bar apps

- Decide deliberately between menu-bar-only accessory behavior and a regular app with menu-bar presence.
- If requirements specify `NSStatusItem`, `NSPopover`, `NSPanel`, `LSUIElement`, or activation behavior, preserve that architecture.
- Keep the popover's primary state legible at a glance. Use compact spacing, clear grouping, and one obvious next action.
- Keep status-item and menu labels short. Move full prompts, diffs, logs, documents, or configuration into a dedicated window.
- Handle outside click, Escape, activation, focus transfer, reopening, and held state explicitly.

## Windows and navigation

- Model standard windows, auxiliary singleton windows, settings, panels, and document windows as distinct scenes when their lifecycles differ.
- Use a multi-instance window group for primary work that supports reopening or multiple windows; use a singleton window for one auxiliary destination; use a utility-window or narrow AppKit panel for floating tools; use document scenes when file lifecycle is the product model. Preserve a specified alternative architecture.
- Use `NavigationSplitView` for stable hierarchy and selection-driven detail. Prefer a flat native source-list sidebar: one leading symbol, one strong title, and at most one secondary line.
- Use horizontal or vertical split views for peer workspaces such as editor/preview or compare panes, not for hierarchical navigation.
- Use a native table for sortable or selectable multi-column data. Keep important identity visible when columns collapse or space becomes constrained.
- Keep metadata-heavy presentation in detail or inspector panes rather than stuffing it into sidebar rows.
- Preserve resizing, minimum sizes, column priorities, truncation strategy, restoration, and per-window state.
- Put persistent top-level switching in appropriate tabs; put contextual attributes in an inspector; put actions in content, toolbars, menus, or commands according to scope.
- Gate newer scene and window APIs by availability and provide a fallback with the same information hierarchy and action model rather than a visually unrelated legacy screen.

## Toolbars, controls, and commands

- Use native toolbar grouping, search placement, badges, labels, and control sizes before creating custom chrome.
- Keep mini, small, and regular control density appropriate to utility, inspector, or main-window contexts.
- Expose important actions through keyboard shortcuts and menu commands as well as visible UI.
- Preserve standard default, cancel, destructive, undo, redo, copy, paste, selection, and validation behavior where applicable.
- Use custom controls only for product-specific interaction, then implement focus, keyboard, pointer, accessibility, active/inactive, disabled, pressed, and error states completely.

## Focus and selection

- Use `Button`, `Toggle`, `Picker`, `Table`, and other semantic controls before gesture-driven replicas.
- Give every custom interactive surface a logical focus position, visible key-focus treatment, keyboard activation, accessibility representation, and disabled behavior.
- Use focused values to route menu and command actions to the active selection or document instead of reaching into global state.
- Prefer declarative default focus and focus scopes over timing-dependent focus writes.
- Do not add a tap handler that redundantly writes focus to an already focusable control; this can destabilize focus and command routing.
- Preserve selection through resizing, filtering, navigation changes, window activation, and restoration when the product model expects it.

## Settings

- Use a dedicated Settings scene and standard entry points.
- Group preferences by user goal, not implementation module.
- Use native form controls, concise labels, immediate persistence where safe, and explicit confirmation for destructive or security-sensitive changes.
- Explain unavailable options and permission requirements in context rather than failing silently.
