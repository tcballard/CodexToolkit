# Open-source PR preflight quality gates

## Repository contract

- Canonical upstream, target base, and proposed head are unambiguous.
- Every applicable contribution instruction has been read and recorded.
- Required issue, template, commit, DCO, CLA, licence, and disclosure rules are understood.
- No repository rule has been inferred away for convenience.

## Scope and hygiene

- Every changed path belongs to the stated purpose or is explicitly justified.
- No secret, local configuration, debug output, conflict marker, or editor artefact is present.
- Generated files, snapshots, lockfiles, permissions, submodules, binaries, and large files are intentional.
- The patch contains no unrelated formatting or opportunistic refactor.

## Correctness and evidence

- The complete diff has been reviewed for correctness, compatibility, error handling, security, privacy, and accessibility where relevant.
- Required formatting, lint, build, test, documentation, and generation checks have exact recorded outcomes.
- Tests exercise the meaningful behavior or regression rather than implementation trivia alone.
- Skipped, blocked, partial, and flaky checks are identified honestly.

## Provenance

- Third-party code and assets have traceable, compatible provenance.
- Required author, DCO, CLA, and contribution disclosures are satisfied or explicitly blocked on the user.
- No identity, authorship, licence, or review evidence is fabricated.

## PR package

- Title and body follow repository conventions and templates.
- Motivation, approach, scope, tests, visible evidence, limitations, and breaking changes are clear.
- Links and checklist answers are accurate.
- The draft gives maintainers enough context without marketing language or unnecessary narrative.

## Authority

- The readiness verdict matches the evidence.
- The exact remaining action and owner are named.
- No commit, history rewrite, signature, push, issue, PR, CLA, review request, or maintainer message occurred without explicit authority.
- The target default branch was not modified directly.

Any failed gate makes the contribution `Not ready` unless the gate is genuinely not applicable and the reason is recorded.
