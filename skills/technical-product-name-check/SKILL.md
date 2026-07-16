---
name: technical-product-name-check
description: Run a dated, evidence-backed practical naming and collision preflight for developer tools, libraries, CLIs, applications, plugins, packages, and open-source projects. Use when Codex needs to check one or more candidate names across current web search, GitHub, relevant package registries, commands, app/distribution channels, search ambiguity, spelling, or expansion fit; compare a shortlist; re-run a prior report; or recommend proceed, reserve first, modify, or reject. Do not use for formal trademark clearance, legal advice, unrestricted naming ideation, domain purchasing, namespace reservation, repository creation, or package publication.
---

# Technical Product Name Check

Decide whether a technical product name is practical to adopt using current, source-linked evidence. Treat every result as time-bound. A name that is not found is neither reserved nor legally clear.

Read [channel-matrix.md](references/channel-matrix.md) to choose coverage. Read [risk-rubric.md](references/risk-rubric.md) before rating. Apply [quality-gates.md](references/quality-gates.md) before delivery.

## Establish the product contract

Resolve:

- candidate name or shortlist;
- one-line product description, category, and audience;
- intended distribution channels;
- desired repository slug, package name, CLI command, app/display name, domain, or handle where relevant;
- geographic/language constraints and naming preferences;
- future expansion that the name must not block.

Inspect the repository before asking for facts already present. Read instructions, README, manifests, executable names, bundle identifiers, release configuration, terminology, and relevant history. If product context or required namespaces remain unclear, propose coverage and pause before assigning risk.

## Normalize variants

Run:

```bash
python3 scripts/normalize_name.py "Candidate Name"
```

Use its deterministic variants as a starting set, not a complete linguistic judgment. Add likely pronunciation variants and misspellings only when evidence or user behavior supports them. Keep user-approved spelling authoritative.

## Select current checks

Always check:

1. quoted and unquoted general web results;
2. GitHub repositories, organisations/users, and relevant code or package references;
3. strong existing company/product collisions;
4. same-category and near-name collisions;
5. search ambiguity and dominant unrelated meanings.

Add only the registries and channels the product actually plans to use. Follow [channel-matrix.md](references/channel-matrix.md). Check repository slug, package namespace, executable command, display name, and domain separately when they differ.

Use live web or connected-app evidence on every run. Prefer official registry endpoints and primary product/repository pages. Open material results; do not judge from snippets alone. Respect rate limits and serialize repeated registry searches. Record `Blocked` or `Ambiguous` rather than retrying aggressively or inventing certainty.

## Classify evidence

For each result record:

- source and direct URL;
- exact query or normalized variant;
- checked-at date;
- result state: `Found`, `Not found`, `Blocked`, `Not checked`, or `Ambiguous`;
- collision class: exact, near, same-category, inactive, unrelated, command, or search ambiguity;
- relevance and evidence for activity/category;
- whether it affects a required namespace.

Use these fact states when needed: `Confirmed`, `Inferred`, `Unverified`, `Preference`, and `Proposed`. Never treat an inactive project as permission or hide an exact collision because its category differs.

## Evaluate the name

Assess pronounceability, spelling, memorability, descriptive fit, distinctiveness, searchability, package/command ergonomics, unwanted cultural or technical meanings, and expansion flexibility. Separate observed collision evidence from qualitative judgment.

Apply one rating from [risk-rubric.md](references/risk-rubric.md): `LOW`, `LOW–MODERATE`, `MODERATE`, `HIGH`, or `BLOCKING`. Recommend one of:

- proceed;
- proceed with caveats;
- reserve required namespaces first;
- modify the name;
- reject and continue naming.

Suggest variants only when they solve a named problem. Never claim trademark clearance or provide legal advice.

## Produce and validate the report

Use [naming-report.md](assets/templates/naming-report.md) for a durable report. Default to an inline report unless the user requests a file or repository workflow requires one. A durable path should be `docs/naming/<candidate>-name-check.md` unless repository instructions define another location.

Run:

```bash
python3 scripts/validate_naming_report.py docs/naming/<candidate>-name-check.md
```

For a re-run, preserve the prior report and explicitly compare changed results, coverage, and risk. A prior report is historical evidence, never a live availability source.

## Safety and delivery boundary

Do not buy a domain, reserve a handle or namespace, create a repository, publish a package, file a trademark, or contact another owner without explicit authorization. Do not expose private user information in public searches.

When repository changes are requested, inspect instructions, branch, and worktree; use a focused branch; validate and review the diff; then hand off to the repository's authorized delivery workflow. Never commit directly to the default branch and never create a ceremonial issue.

## Deliver

Return candidates, checked-at time, coverage, material exact/near collisions, namespace results, usability findings, risk rating, recommendation, changed results since any prior report, and everything not checked. State that the result is practical naming research, not legal or trademark clearance.
