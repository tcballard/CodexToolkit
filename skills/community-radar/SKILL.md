---
name: community-radar
description: Find and rank current communities, discussions, unanswered questions, complaints, alternative requests, and participation opportunities for an open-source project, developer tool, or product using dated public evidence and transparent anti-spam scoring. Use when Codex needs to discover where likely users already gather, map community fit, monitor conversations, compare participation opportunities, recommend whether to reply, observe, teach, launch, or wait, or turn a repository/product brief or last30days findings into an authentic community-engagement plan. Do not use for automated posting, growth hacking, influencer lists, SEO, vanity metrics, generic marketing plans, or drafting the final public copy.
---

# Community Radar

Find conversations worth joining. Do not optimize for posting everywhere.

Read [evidence-and-safety.md](references/evidence-and-safety.md) before research, [scoring.md](references/scoring.md) before ranking, and [quality-gates.md](references/quality-gates.md) before delivery. Read [community-types.md](references/community-types.md) when selecting channels and [launch-stages.md](references/launch-stages.md) when stage changes appropriate engagement.

## Establish the product contract

1. Inspect the supplied repository or product URL before searching. Read repository instructions, README, manifests, documentation, releases, issues, discussions, and confirmed public positioning.
2. Resolve the product, current stage, target audience, geography, existing communities, competitors, non-goals, and the decision this report must support.
3. Build a small fact ledger with `Confirmed`, `Inferred`, `Unverified`, and `Preference` labels. Never silently promote an inference to a product fact.
4. Ask only for missing context that would materially change research coverage. A repository plus clear stage is usually enough to begin.

Supported stages are `idea`, `prototype`, `alpha`, `beta`, `open source`, and `commercial`. Treat combinations explicitly, such as `open source beta`.

## Run the pipeline

### 1. Profile likely audiences

Identify primary, adjacent, and enabling audiences. For each, state the repository or product evidence, the user problem connecting them to the product, and whether the relationship is confirmed or inferred. Do not confuse a technology named in the stack with a likely user group.

### 2. Map candidate communities

Select communities from actual audience behavior rather than a fixed checklist. Consider Hacker News, Reddit, Lobsters, GitHub Discussions and issues, Discord, Slack, X, LinkedIn, product forums, language ecosystems, meetups, newsletters, and specialist communities only when evidence supports them.

For each candidate record:

- community and direct URL;
- relevant audience segment;
- relevance, observable activity, and expected overlap;
- participation norms or promotion rules;
- evidence date, source, and confidence;
- access limitations, including private or login-gated content.

Omit channels that have no credible fit. A ranked map is not permission to post.

### 3. Discover current conversations

Current web access is required for conversation claims. Search recent primary pages and platform-native results for:

- active questions and unanswered requests;
- repeated complaints or workflow friction;
- feature requests and requests for alternatives;
- competitor mentions and recent launches;
- technical discussions where first-hand experience helps;
- recurring questions that could become documentation or a technical article.

Record the exact URL, author-visible date, observed date, a short paraphrase, relevance, and any reply or promotion constraints. Prefer conversations with a concrete need over broad topical matches. Never fabricate private Slack or Discord activity, engagement counts, dates, quotes, or access.

If `$last30days` is installed and the product needs emerging-topic discovery, it may supply candidate discussions. Re-open and verify every selected source; `community-radar` owns fit, scoring, and participation judgment, not the upstream search result.

### 4. Score opportunities

Score evidence-backed conversation opportunities with [score_opportunities.py](scripts/score_opportunities.py):

```bash
python3 scripts/score_opportunities.py opportunities.json --output ranked-opportunities.json
```

The input contract and weights are defined in [scoring.md](references/scoring.md). Score community-level recommendations narratively; score only concrete conversations mechanically. Explain every dimension in prose. A number without its evidence and rationale is invalid.

Treat a high spam-risk or rule conflict as a reason to observe, contribute without promotion, or decline—not as a score to optimize around.

### 5. Choose an engagement posture

Assign one posture to each shortlisted opportunity:

- `reply today` — a current question can be answered usefully without forcing the product;
- `answer without promoting` — contribute expertise and omit the product link;
- `observe first` — learn norms or build standing before participating;
- `write a technical article` — repeated questions deserve durable explanation;
- `improve docs first` — the conversation exposes a product comprehension gap;
- `invite feedback` — the stage and community permit a transparent test request;
- `publish a release` — a completed change directly resolves the evidenced need;
- `wait for capability` — the product cannot yet satisfy the conversation;
- `do not engage` — rules, hostility, duplication, or weak fit outweigh value.

State why the posture fits the product stage, community norms, and evidence. Never default to “post everywhere.”

### 6. Produce the report

Use [report-contract.md](references/report-contract.md). Deliver:

1. product context and evidence ledger;
2. audience profile;
3. ranked community map;
4. current conversation opportunities;
5. transparent opportunity ranking;
6. engagement strategy;
7. risks and unknowns;
8. a short ordered action plan for today, tomorrow, this week, and the next relevant launch boundary;
9. sources, checked-on date, and explicit coverage gaps.

Validate a persisted report with:

```bash
python3 scripts/validate_radar_report.py community-radar.md
```

## Integration boundaries

- `$last30days` may find emerging discussions; this Skill verifies, maps, ranks, and chooses a participation posture.
- `$merge-and-tell` may draft approved public communication after the user selects an opportunity; this Skill does not write the final post or reply by default.
- `$launch-pack` owns cross-channel launch coordination, claims consistency, and release readiness.
- `first-customer-finder` owns named prospect discovery and outreach preparation.
- `$technical-product-name-check` owns name and namespace collisions.

All integrations are optional and soft. The Skill must remain useful when extracted from the toolkit.

## Safety boundary

- Never post, reply, message, join a private community, create an account, or contact a person without explicit authorization.
- Never recommend evading moderator rules, disguising affiliation, brigading, vote manipulation, duplicate promotion, or AI-generated engagement farming.
- Never expose private user information or reproduce private-community content into a report.
- Do not present search-result volume, follower counts, or raw engagement as proof of audience fit.
- Do not call an opportunity current without a visible date or a clearly disclosed date limitation.
- Report hostile dynamics, recent competitor launches, launch fatigue, missing capabilities, product immaturity, and weak evidence even when they reduce the recommendation.

## Examples

Read [examples.md](references/examples.md) for concise OSS, startup, Build Week, and developer-tool scenarios. They illustrate decisions, not reusable claims or static community recommendations.
