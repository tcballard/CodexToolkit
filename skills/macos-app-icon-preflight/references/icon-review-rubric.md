# Icon review rubric

## Finding labels

- **Platform rule:** current official Apple source, date, and target context are recorded.
- **Evidence-backed defect:** a measured fact is visually confirmed in the supplied asset.
- **Subjective craft concern:** a review judgment such as weak optical balance; never present it as policy.
- **Unverified:** tooling, source, or evidence is insufficient.

## Review dimensions

### Source integrity

Check real source priority, dimensions, square geometry, file format, corruption, scaling history, alpha, visual bounds, and source hash. A plausible filename is not provenance.

### Outer treatment

Inspect transparent corners, edge-center occupancy, enclosure geometry, frames, bevels, glows, and shadows. A heuristic may flag a likely rounded mask, but visual confirmation is mandatory. Separate semi-transparent antialiasing from a material halo or external shadow.

### Internal depth

Preserve shadows and lighting that describe the central subject. Removing an inappropriate outer effect does not authorize flattening all dimensionality.

### Padding and bounds

Measure each edge as pixels and a canvas percentage. Flag contact with the canvas and visibly imbalanced or excessive margins. Thresholds are review cues, not Apple rules.

### Small-size behavior

Inspect 16, 32, 64, 128, and 256-pixel previews on light, dark, and checkerboard contexts. Look for recognition, silhouette, thin-detail loss, muddy contrast, aliasing, and an icon that appears optically too small. These are display tests, not required source slots.

## Readiness layers

Report independently:

1. **Design readiness** — visual concerns resolved for the target context.
2. **Source/export readiness** — correct authoritative files and mechanical evidence exist.
3. **Integration readiness** — handoff contains current format/tool requirements; Xcode work may remain.
4. **Runtime status** — only passed after actual project build/run inspection.
5. **Release status** — outside visual preflight unless separately verified.
