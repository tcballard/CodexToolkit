# Launch Pack quality gates

## Hard blockers

Do not mark the pack ready when any are true:

- release version, build, date, availability, pricing, support, or destination link conflicts across files;
- a public deliverable uses a blocked, removed, or unqualified claim;
- a measurement lacks its baseline, method, or boundary;
- a screenshot or demo contains private data, misleading state, or unreadable proof;
- a required platform, store, competition, or accessibility constraint is unverified;
- a required asset is missing, corrupt, stale, or still a placeholder;
- publication authority is absent or ambiguous;
- an output implies publishing, submission, endorsement, or team authority that was not granted;
- generated imagery is presented as product evidence;
- a link, download, form, or call to action has not been checked.

## Coherence review

Verify:

- one release identity and one evidence spine govern every output;
- each channel has a specific audience, job, and desired action;
- the same product limitation is expressed consistently at the appropriate depth;
- visual assets share an intentional identity without becoming template-like;
- demo, screenshots, written claims, and repository state describe the same build;
- public copy sounds like the same product team even when channel cadence changes;
- omitted channels and assets are deliberate rather than forgotten.

## Final evidence

Before handoff:

1. Run the deterministic pack checker with `--final`.
2. Inspect every evidence source cited by a used claim.
3. Open every finished file and link.
4. Render and inspect visual assets at delivery size.
5. Verify technical constraints for video, images, stores, and submissions.
6. Confirm privacy, accessibility, provenance, and required disclosures.
7. Record the exact ready, qualified, blocked, omitted, and not-applicable items.
8. State who may publish and what action remains manual.

The checker establishes structural readiness only. The final verdict still requires human or agent inspection of evidence and rendered outputs.
