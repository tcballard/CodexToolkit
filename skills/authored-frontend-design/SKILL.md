---
name: authored-frontend-design
description: Design, build, restyle, or substantially refactor distinctive production-grade websites and web apps with a coherent human-authored art direction, functional signature element, semantic design tokens, responsive behavior, accessibility, complete interaction states, and intentional failure handling. Use when Codex is implementing a frontend and generic template, default framework, marketplace, or recognizably AI-generated aesthetics are unacceptable. Do not use for logic-only changes, exact visual cloning, or minor maintenance that must preserve an established design system unchanged.
---

# Authored Frontend Design

Create an interface with a point of view. Treat visual identity, behavior, copy, accessibility, responsiveness, performance, and failure recovery as one authored system.

Read [references/frontend-doctrine.md](references/frontend-doctrine.md) before choosing the direction. Read [references/quality-gates.md](references/quality-gates.md) before delivery.

## Workflow

1. Ground the product.
   - Inspect the repository, current interface, content, data shape, brand assets, and supplied references.
   - Identify the user's problem, audience, primary tasks, framework, performance constraints, accessibility needs, brand anchors, and taboos.
   - Ask only for missing information that blocks a correct build. Infer reversible details and state consequential assumptions.

2. Commit to one radical direction.
   - Choose a precise visual thesis with a clear emotional register. Radical restraint and controlled maximalism are equally valid.
   - Do not present a menu of safe directions unless the user asks for exploration.
   - Write a compact internal art-direction brief: tone, type logic, palette roles, grid, motion grammar, material, and signature element.
   - Vary choices across unrelated builds. Never reuse an aesthetic formula by habit.

3. Invent one functional signature element.
   - Make it improve navigation, hierarchy, comprehension, feedback, or discoverability.
   - Integrate it with the product's purpose and state model. Decoration alone does not qualify.
   - Give it a clean reduced-motion and lower-capability behavior.

4. Define the system before components.
   - Establish semantic tokens for color, typography, spacing, shape, depth, and motion.
   - Establish the grid, responsive transformations, state vocabulary, icon language, and copy voice.
   - Extend an existing system when continuity is required; do not erase working conventions merely to appear original.

5. Build the complete experience.
   - Use contextual production copy. Remove filler, generic marketing language, and unexplained empty states.
   - Implement every applicable state: default, hover, pressed, focus-visible, disabled, loading, error, empty, offline, partial, and delayed.
   - Preserve narrative and hierarchy at a minimum of three meaningful breakpoints.
   - Make implementation complexity proportional to the art direction.

6. Verify, render, and revise.
   - Build and run relevant checks. Inspect the rendered interface at representative sizes and states when tooling permits.
   - Verify semantics, keyboard operation, focus visibility, WCAG AA intent, non-color communication, motion preferences, touch targets, performance, and recovery paths.
   - Apply every rejection gate. Revise rather than disclaiming a failed gate.

## Delivery

Lead with the completed outcome. Provide complete runnable code or edited files for the requested scope, a concise art-direction brief when it aids comprehension, verification evidence, and extension notes only where future work could break coherence.
