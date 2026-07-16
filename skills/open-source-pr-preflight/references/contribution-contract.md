# Open-source contribution contract

## Authority order

Apply requirements in this order unless the repository states otherwise:

1. Platform and organisation policies that govern the target repository.
2. Root and path-scoped repository instructions.
3. Contribution, security, governance, and code-of-conduct documentation.
4. Pull-request templates, CI configuration, package scripts, and generated-file rules.
5. Established maintainer conventions visible in current accepted work.

An old accepted PR does not overrule current written policy.

## Contract record

Capture:

- upstream repository and contribution destination;
- base and head refs with resolved commit IDs, plus how base freshness was confirmed;
- applicable instruction files and their scope;
- contribution purpose and linked issue requirement;
- allowed patch scope and deliberately excluded work;
- title, commit, branch, and PR-template conventions;
- required checks and supported environments;
- documentation, changelog, snapshot, and generated-file expectations;
- DCO, CLA, licence, provenance, and disclosure requirements;
- maintainer actions the contributor cannot complete automatically.

## Diff authority

The proposed contribution is not just the most convenient diff view. Include:

- commits reachable from head but not base;
- staged changes;
- unstaged changes;
- untracked files intended for submission;
- submodule pointer, file mode, binary, lockfile, and generated-file changes.

If the intended submission set is ambiguous, the preflight is blocked until scope is explicit.

## Evidence language

Use exact states:

- **Passed:** command completed successfully in the stated environment.
- **Failed:** command ran and returned a failure or produced invalid output.
- **Blocked:** command could not run because a named prerequisite was unavailable.
- **Skipped:** command was deliberately not run, with reason and consequence.
- **Not applicable:** repository rules or patch scope make the check irrelevant.

Do not collapse blocked or skipped into passed.

## Maintainer respect

- Keep one coherent purpose per PR.
- Minimise review surface without hiding necessary tests or documentation.
- Explain non-obvious choices and intentional limitations.
- Avoid speculative refactors and drive-by cleanup.
- Do not summon maintainers, request expedited review, or create process artefacts without permission.
- Leave unsupported checklist items visibly incomplete.
