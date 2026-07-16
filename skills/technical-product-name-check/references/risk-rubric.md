# Practical naming risk rubric

Use the highest rating supported by a material finding. Explain exceptions; do not average risks into a score.

## LOW

- No material collision in required channels.
- Search results are distinguishable.
- Repository, package, and command plan is practical.
- Spelling and pronunciation create little friction.

## LOW–MODERATE

- Minor unrelated or inactive uses exist.
- Preferred namespaces are practical or an accepted scoped alternative exists.
- Search ambiguity is manageable with product/category context.

## MODERATE

- A preferred slug or command is occupied but a credible alternative exists.
- Near-name or cross-category uses could cause confusion.
- Spelling, pronunciation, or search ambiguity needs deliberate mitigation.
- The name may constrain a plausible expansion.

## HIGH

- A strong established same-category product or dominant search result exists.
- Package, command, app, or repository confusion is likely.
- The workaround materially weakens discoverability or user trust.
- A serious cultural/technical meaning needs owner review.

## BLOCKING

- Exact collision in a required namespace has no accepted alternative.
- Similarity to an established same-category product is likely deceptive or operationally unusable.
- Required current checks are blocked and the user needs a confident adoption decision now.

## Recommendation mapping

| Rating | Default recommendation |
| --- | --- |
| LOW | Proceed |
| LOW–MODERATE | Proceed with caveats or reserve first |
| MODERATE | Reserve first or modify |
| HIGH | Modify or reject |
| BLOCKING | Reject for the current namespace plan or pause for missing evidence |

This rubric describes practical product risk. It does not assess trademark validity, infringement, registrability, or legal clearance.
