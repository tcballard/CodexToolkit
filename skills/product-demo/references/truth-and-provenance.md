# Truth and provenance

## Contents

- Evidence hierarchy
- Claims ledger
- Editing boundaries
- Model contribution record

## Evidence hierarchy

Prefer sources in this order unless project rules say otherwise:

1. Verified behavior in the recorded product build.
2. Passing tests, measurements, and reproducible commands.
3. Authoritative specification and acceptance criteria.
4. Current source code and configuration.
5. Maintained build logs and release notes.
6. README or public product copy.
7. Owner statements that have not yet been independently verified.

Conflicts move a claim to `blocked` until resolved. A polished README does not overrule contradictory behavior.

## Claims ledger

Track every material spoken or on-screen claim:

| Field | Meaning |
| --- | --- |
| ID | Stable identifier such as `C07` |
| Claim | Exact viewer-facing wording |
| Importance | Required, supporting, or optional |
| Evidence | File, test, measurement, or shot that substantiates it |
| Status | Verified, qualified, blocked, or removed |
| Qualification | Boundary or limitation that must remain visible |
| Placement | Voiceover, title, caption, description, or submission form |

Do not promote a claim from qualified to verified merely because the edit needs a stronger line.

## Editing boundaries

Allowed when disclosed by ordinary editing grammar:

- removing dead air;
- reframing or zooming without hiding relevant state;
- adding accurate captions and callouts;
- replaying an interaction for explanation;
- combining separate takes when continuity remains truthful;
- normalizing audio and correcting capture color.

Never:

- replace a failed result with a fabricated success state;
- splice inputs and outputs from incompatible builds without disclosure;
- shorten a wait in a way that creates a materially false performance claim;
- cover an error, warning, or limitation that changes the meaning of the workflow;
- generate interface footage and present it as a recording of the product;
- imply that a model, tool, or person performed work they did not perform.

When time compression is material, label it or avoid making a latency claim.

## Model contribution record

When provenance matters, record:

- model and surface used;
- session or trace identifier when available and permitted;
- inputs inspected;
- narrative and editorial decisions made;
- code, scripts, captions, or assets created;
- render and validation commands executed;
- human decisions, recordings, corrections, and approvals;
- any work delegated to another model or service;
- final verification evidence.

Write provenance as a factual ledger, not promotional copy. A user recording the application is a human contribution even when the model supplied the shot list. A renderer executing model-authored code is not a separate creative author.
