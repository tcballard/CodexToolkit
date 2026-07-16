# Refresh contract

Refresh is proposed-diff-first.

1. Inspect the active Skill and its `source-manifest.json`.
2. Refuse unsupported schema or missing ownership evidence.
3. Generate to a separate empty candidate path.
4. Regenerate only files whose current hashes still match their recorded generation hashes.
5. Preserve changed generated files byte-for-byte and report them for reconciliation.
6. Copy unmanaged files byte-for-byte.
7. Never copy transient completion into permanent `SKILL.md` instructions.
8. Emit a recursive unified diff and validate the candidate.
9. Replace the active Skill only after explicit owner review in a separate action.

A changed authoritative source hash, missing path, changed milestone ID/criteria, unavailable required specialist, status conflict, or old schema marks the Skill stale. Stale means review required, not wrong.

The v0.0.1 generator does not merge concurrent edits inside a generated file. Preservation is safer: edited files remain untouched in the candidate and are named as conflicts.
