# Launch evidence contract

## Authority order

Prefer evidence in this order unless the project defines a stricter authority:

1. Verified behavior of the release build or artifact.
2. Passing tests, measurements, signed artifacts, and reproducible commands.
3. Authoritative specification and acceptance criteria.
4. Release configuration, version source, tag, and packaging metadata.
5. Maintained build logs, decision records, and release notes.
6. Current repository documentation.
7. Owner statements not yet independently verified.
8. Existing marketing copy.

When sources conflict, block the affected claim. Public copy never outranks product evidence.

## Claim statuses

| Status | Meaning | Public use |
| --- | --- | --- |
| Verified | Directly supported by inspected evidence | May be used as written |
| Qualified | Supported only within a stated boundary | May be used with the qualification visible |
| Blocked | Missing, conflicting, stale, or insufficient evidence | Must not appear publicly |
| Removed | Intentionally excluded from this launch | Must not reappear downstream |

Each material claim needs:

- stable ID;
- exact proposed wording;
- importance;
- evidence path, command, measurement, or observed behavior;
- status;
- required qualification;
- approved channels;
- owner when unresolved.

## Consistency contract

Treat these as shared release fields, not channel-specific creative choices:

- product and release name;
- version and build;
- availability state and rollout boundary;
- release date or window;
- supported platforms and minimum versions;
- pricing, eligibility, geography, and account requirements;
- measured numbers and comparison baselines;
- privacy, security, retention, and AI/model statements;
- limitations and known issues;
- canonical destination URL;
- primary call to action.

If a field legitimately differs by channel or audience, record the rule in the brief and channel matrix.

## Privacy and provenance

- Use non-sensitive fixtures in screenshots and demos.
- Remove internal hosts, tokens, account identifiers, notifications, and private analytics.
- Do not expose embargoed URLs in public artifacts or metadata.
- Record whether assets are captured, generated, edited, or supplied.
- Keep model contribution factual when disclosure or submission rules require it.
- Never present a generated interface image as proof of product behavior.
