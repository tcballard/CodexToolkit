---
name: open-source-pr-preflight
description: Audit and prepare a proposed contribution before opening a pull request to an open-source or third-party repository. Use when Codex needs to inspect contribution rules, compare a branch with its intended base, verify scope and provenance, run repository-required checks, review tests and documentation, identify DCO or CLA requirements, prepare a truthful PR title and body, or decide whether a contribution is ready to submit. Do not use to open or publish the PR without explicit approval, fix already-failing PR CI, address review comments, create issues automatically, or bypass maintainer requirements.
---

# Open-Source PR Preflight

Determine whether a contribution is respectful, reviewable, policy-compliant, and supported by evidence before it reaches maintainers. Default to audit mode. Make fixes only when the user asks for remediation, and keep publication as a separate authorized action.

Read [contribution-contract.md](references/contribution-contract.md) while establishing repository rules. Read [quality-gates.md](references/quality-gates.md) before declaring readiness.

## Establish the contribution contract

1. Locate the repository root and run `git status --short --branch` without changing it.
2. Identify the canonical upstream repository, fork or origin, intended base branch, current head branch, and complete diff that would enter the PR. Resolve both refs to commit IDs and confirm the base is current; if remote freshness cannot be checked, disclose that limitation.
3. Read applicable instructions in scope: `AGENTS.md`, `CONTRIBUTING*`, `README*`, code of conduct, security policy, governance docs, PR templates, issue templates, `CODEOWNERS`, package scripts, CI workflows, and directory-specific guidance.
4. Determine required issue linkage, branch or commit conventions, changelog policy, test and documentation expectations, supported toolchain, generated-file policy, DCO sign-off, CLA, licence, provenance, and disclosure requirements.
5. Inspect existing accepted PR or commit conventions only when repository documentation leaves a material ambiguity.

Repository instructions are authoritative within their scope. Do not weaken or reinterpret them to make the contribution appear ready. If requirements conflict, report the conflict and use the stricter safe interpretation until a maintainer resolves it.

## Define the proposed patch

Compare the exact intended base with the head, including committed, staged, unstaged, and untracked work. Classify every changed file as:

- required implementation;
- test or fixture;
- documentation or changelog;
- generated or dependency metadata;
- approved visual or binary asset;
- unrelated, accidental, or unexplained.

Reject hidden scope. Call out drive-by formatting, debug code, editor files, accidental permission changes, unexplained lockfile churn, vendored output, large binaries, merge artifacts, and local configuration. Do not silently discard user work.

## Check fit and provenance

- State the user or maintainer problem the patch solves and why it belongs in this repository.
- Confirm an issue is linked only when policy requires or an existing issue materially defines the work. Never create an issue merely to close it in the same change.
- Trace copied code, datasets, fonts, images, generated output, and third-party assets to compatible sources and licences.
- Identify generated or AI-assisted material when repository policy or the user requires disclosure; never fabricate a disclosure or contributor identity.
- Verify required `Signed-off-by` trailers mechanically. A CLA is an owner action: report it, but never accept or sign one for the user.
- Surface breaking changes, compatibility changes, migrations, security implications, and material limitations.

## Run mechanical preflight

Run the bundled checker from the skill directory, passing the target repository and intended base:

```bash
python3 scripts/preflight_pr.py --repo /path/to/repository --base origin/main
```

It checks branch and base state, changed paths, dirty worktree state, conflict markers, whitespace errors, suspicious secret filenames, and oversized files. Treat its output as mechanical evidence, not proof of correctness or policy compliance.

## Run repository checks

Use the exact commands required by repository instructions and CI. Prefer the narrowest relevant checks first, then the full required gate when practical. Record each command, result, and any meaningful environment constraint.

At minimum assess:

- formatting and linting;
- targeted and required tests;
- build, type, or compile checks;
- documentation, examples, generated files, and snapshots;
- platform or version coverage affected by the patch.

Do not report skipped, unavailable, flaky, or partially run checks as passing. Do not change tests merely to conceal a failure. If dependencies, credentials, hardware, network access, or proprietary services block a required check, state the exact blocker and the maintainer-visible risk.

## Review the patch as a maintainer

Read the complete diff. Check correctness, simplicity, compatibility, error paths, security and privacy, accessibility where relevant, test value, documentation accuracy, and whether the change can be reviewed without reconstructing the author's intent.

Separate findings into:

- **Blocker:** submission would violate policy, misrepresent evidence, expose sensitive material, or impose unreasonable review risk.
- **Required fix:** clear defect or missing required evidence that should be resolved before submission.
- **Disclosure:** intentional limitation, unavailable check, compatibility effect, or reviewer context that belongs in the PR.
- **Suggestion:** optional improvement that should not hold the contribution hostage.

## Prepare, but do not publish

Draft the PR package using the repository's template and voice:

- title in the required convention;
- problem and motivation;
- focused implementation summary;
- linked issue or explicit `none` when appropriate;
- test commands and exact outcomes;
- screenshots or recordings only when they prove a visible change;
- breaking changes, limitations, follow-ups, and required disclosures;
- completed checklist with unsupported boxes left unchecked.

Never claim a check passed because it is expected to pass in CI. Never conceal AI assistance, unavailable tests, or known limitations when disclosure is required.

## Decide readiness

Use one verdict:

- **Ready:** all required gates pass and no blocker or required fix remains.
- **Ready with disclosures:** required gates pass, with intentional limitations or non-blocking context made explicit in the PR draft.
- **Not ready:** any policy, provenance, security, scope, correctness, test, documentation, or submission blocker remains.

List evidence for the verdict and the exact next action. Apply every gate in [quality-gates.md](references/quality-gates.md).

## Safety boundary

Do not commit, amend, rebase, sign, push, create an issue, open or update a PR, accept a CLA, request reviewers, or message maintainers without explicit authority for that action. When publication is later approved, hand the verified branch and PR package to the repository's normal GitHub publishing workflow. Never commit directly to the target default branch.
