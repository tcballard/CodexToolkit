# Premonition build-log entry template

Use the smallest entry that preserves an auditable handoff. Write `None` where a required section has no content; do not delete the section.

```markdown
## Entry <unique-id> — <short outcome>

**Date:** YYYY-MM-DD

**Recorded at:** YYYY-MM-DDTHH:MM:SS±HH:MM

**Phase:** <planning or S0–S6>

**Status:** Complete | Partial | Blocked

**Model:** GPT-5.6 Sol — <how explicitly confirmed, or Not confirmed>

**Session ID:** <stable ID or Not captured>

### Objective

<One or two sentences describing the intended outcome.>

### Completed

- <Concrete result.>

### Decisions and provenance

- **Owner decision:** <Decision, or None.>
- **Sol implemented:** <Scope, or None.>
- **Sol reviewed:** <Scope, or None.>
- **Human-authored and Sol-reviewed:** <Scope, or None.>

### Artefacts

- `<path, commit or durable artefact>` — <purpose>.

### Verification

- `<command or named manual check>` — <observed result>.

### Deviations

- <Deviation from the authoritative specification and reason, or None.>

### Risks and missing evidence

- <Known issue, blocker or unverified claim, or None.>

### Next entry state

- <The exact first action and entry criteria for the next session.>
```

For a correction, retain the same structure, title it `Correction to Entry <id>`, and state both the original claim and the evidence-backed correction without altering the earlier entry.
