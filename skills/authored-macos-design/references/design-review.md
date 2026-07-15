# Evidence-based macOS design review

Review the rendered interface, not source code alone. Capture representative window sizes and the primary, empty, loading, error, selected, focused, and inactive-window states that apply. Evaluate each lens independently; do not let strong visual polish conceal weak native behavior.

## 1. Narrative alignment

- State the design thesis in one sentence.
- Check that typography, density, palette, materials, symbols, motion, copy, and the signature element reinforce that thesis.
- Flag any element that appears borrowed from a different product or aesthetic system.
- Ask whether the interface remains recognisable without its app name.

## 2. Visual hierarchy

- Identify the intended first, second, and third points of attention.
- Check that task priority, selection, status, and primary action are legible without relying on colour alone.
- Confirm that grouping follows information relationships rather than a habit of placing everything in cards.
- Inspect hierarchy at minimum, ideal, and expanded window sizes.

## 3. Craft precision

- Check alignment, optical balance, text measure, truncation, symbol weight, spacing rhythm, corner relationships, material edges, and active/inactive window treatment.
- Confirm that tokens govern authored choices while native control metrics remain native.
- Reject arbitrary values that have no optical, semantic, or platform rationale.
- Inspect real content and extreme values, not only a tidy fixture.

## 4. Native task fitness

- Complete the primary task using pointer and keyboard separately.
- Check scene choice, resizing, focus order, commands, menu validation, default/cancel/Escape behavior, selection persistence, recovery, and accessibility.
- Confirm that controls behave like Mac controls and that custom interaction earns its maintenance cost.
- Verify that newer APIs degrade to a fallback with the same task model.

## 5. Distinctiveness

- Name the functional signature element and the product concept it expresses.
- Check that distinctiveness comes from the product narrative rather than fashionable gradients, glass, giant type, card repetition, or ornamental motion.
- Compare against common web, Electron, Tauri, iOS, and generic SwiftUI compositions.
- Remove any flourish that could be transplanted unchanged into an unrelated app.

## Review outcome

For each lens, record concrete evidence, the strongest aspect, and the most consequential weakness. Treat any material weakness in native task fitness or accessibility as a release blocker. Revise weak lenses directly; do not average them into a flattering overall score.
