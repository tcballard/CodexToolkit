# Remotion companion

## Contents

- Capability boundary
- Project rules
- Motion direction
- Reviewability
- Fallback behavior

## Capability boundary

This skill owns product evidence, narrative, capture, editorial intent, and acceptance. The official Remotion plugin owns current Remotion implementation practices.

When available, use its maintained skills for project creation, React markup, rendering, captions, interactivity, and media handling. Do not copy their contents into this skill or freeze framework-specific guidance here.

## Project rules

- Keep React and TypeScript as the edit source of truth.
- Keep raw footage immutable and separate from generated renders.
- Put editorial timing and clip selection in readable data structures rather than scattering unexplained frame numbers.
- Use stable shot and claim IDs in composition data where practical.
- Define delivery dimensions, frame rate, duration, safe areas, typography, colors, spacing, and motion values centrally.
- Keep sequences small enough to inspect and revise independently.
- Ensure every remote asset is either pinned and reproducible or copied locally with permission.
- Avoid runtime network dependencies in the final render when local assets can be used.

## Motion direction

- Use motion to establish hierarchy, reveal causality, or preserve continuity.
- Prefer cuts and restrained reframing over ornamental transitions.
- Avoid generic gradients, glowing AI motifs, excessive spring motion, floating interface cards, and template-like kinetic typography unless the product's identity calls for them.
- Do not animate a native application into a fictional interface state.
- Keep product text readable during zooms and transitions.
- Respect reduced-motion principles when the composition will also be used interactively.

## Reviewability

The project should allow another agent or editor to answer:

- Which source take appears in each sequence?
- What in/out points were chosen?
- Which claim does the sequence substantiate?
- Which caption or narration line accompanies it?
- Which values control the crop, zoom, audio, and transition?

Prefer a typed edit-decision structure such as:

```ts
type DemoSequence = {
  id: string;
  source: string;
  fromSeconds: number;
  toSeconds: number;
  claimIds: string[];
  narrationId?: string;
  crop?: {x: number; y: number; scale: number};
};
```

## Fallback behavior

If the official Remotion plugin is unavailable:

1. Complete the evidence, narrative, shot-list, capture, and review stages normally.
2. Tell the user that the official plugin is recommended for implementation.
3. Do not install a plugin or package without permission.
4. If the user chooses plain Remotion, use current official documentation and a minimal project rather than reproducing a large embedded framework guide.
