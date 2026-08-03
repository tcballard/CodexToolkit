---
name: asdecided-content-radar
description: Build and refresh an evidence-backed AsDecided content opportunity queue from repository changes, releases, decisions, documentation gaps, recurring user questions, community conversations, search-performance data, stale pages, broken sources, and citation gaps. Use for periodic editorial planning, deciding what AsDecided should publish or update next, or converting observed product and audience evidence into ranked publishing briefs. Do not use for generic trend lists, keyword-volume farming, automated publishing, mass content generation, outreach, backlink schemes, or drafting final articles.
---

# AsDecided Content Radar

Find the next useful thing to explain, prove, update, or retire. Do not create content merely to maintain cadence.

This Skill produces an evidence-backed editorial queue for `$asdecided-publishing`. It may run periodically, but each run is a fresh inspection rather than an instruction to publish automatically.

## Establish the radar scope

Confirm the inspected period, repositories, product surfaces, site inventory, available analytics or Search Console data, known audiences, active product stage, and current strategic questions. If a source is unavailable, record the coverage gap rather than inventing findings.

Build a source ledger with checked-on dates for:

- merged PRs, releases, commits, issues, discussions, and decision records;
- current AsDecided pages, docs, metadata, sitemaps, and internal links;
- user questions, support or feedback themes, and approved private notes when supplied;
- public community conversations verified through `$community-radar` or current research;
- Search Console or analytics evidence when connected and authorized;
- source freshness, broken links, product drift, and outdated examples;
- known answer-engine prompts or citation observations when actually measured.

## Discover candidate work

Create candidates only when evidence supports one of these jobs:

- `new explanation`: a recurring question lacks a durable answer;
- `new proof`: a product claim needs a worked example, measurement, or implementation record;
- `decision guide`: teams face a real choice that AsDecided can clarify;
- `documentation bridge`: repository behaviour and public explanation have diverged;
- `refresh`: a useful page has stale versions, links, claims, examples, or schema;
- `consolidate`: overlapping pages weaken clarity or authority;
- `retire`: a page is obsolete, misleading, unsupported, or no longer strategically useful;
- `internal link`: an existing page needs a clearer relationship to another durable resource;
- `distribution follow-up`: an approved canonical page lacks a justified derivative for an evidenced audience;
- `measurement`: a question cannot be answered credibly until a test or dataset exists.

Do not convert every release or PR into an article. Most changes should remain release notes, documentation, or no public content at all.

## Evidence signals

Useful signals include:

- the same concrete question appearing across multiple independent sources;
- a merged change that alters an important workflow or architectural principle;
- an existing page gaining impressions but failing to answer the apparent query;
- a page cited or linked for the wrong reason because its definition is ambiguous;
- repeated agent or contributor violations that expose a decision-governance gap;
- a current comparison or standard change that makes an existing article inaccurate;
- a product capability with enough first-party evidence for a worked example;
- a high-value negative result, trade-off, or failure mode not yet documented.

Weak signals include raw keyword volume, generic industry trends, competitor publishing frequency, vanity engagement, and an arbitrary content calendar.

## Score candidates

Score each candidate from 0 to 3 on:

- `reader_need`: strength and specificity of the observed problem;
- `asdecided_authority`: whether AsDecided has first-party evidence or a defensible contribution;
- `original_value`: likelihood of adding a framework, example, measurement, or useful synthesis;
- `product_relevance`: connection to current product strategy and audience;
- `evidence_readiness`: quality of available sources and examples;
- `freshness_urgency`: cost of leaving stale or misleading content unchanged;
- `distribution_fit`: whether a real destination or conversation exists;
- `effort`: expected research, implementation, and review burden, where 3 means high effort.

Calculate:

```text
priority = reader_need + asdecided_authority + original_value + product_relevance + evidence_readiness + freshness_urgency + distribution_fit - effort
```

A score never overrides weak evidence, lack of authority, or a poor ethical fit. Explain every dimension in prose.

## Classify the recommendation

Assign one outcome:

- `publish now` — evidence and original contribution are ready;
- `brief next` — worthwhile, but the publishing brief still needs work;
- `measure first` — run a test or gather product evidence before writing;
- `refresh now` — the current page risks misleading readers or agents;
- `link or document instead` — solve the need through docs, examples, or internal links;
- `distribute approved source` — use `$asdecided-distribute` rather than write another article;
- `observe` — the signal is promising but not yet repeated or clear;
- `retire or consolidate` — remove or merge weak content;
- `do not pursue` — low value, weak authority, duplication, or content-farm risk.

## Detect refresh triggers

For existing pages, inspect:

- current product behaviour versus the page's claims;
- dates, versions, standards, competitors, and commands;
- source availability and changed source meaning;
- canonical, metadata, schema, sitemap, and internal-link consistency;
- Agent Citation Scorecard weaknesses or missing scorecards;
- paragraphs that no longer extract safely;
- traffic or visibility changes only when actual data is available;
- references to proposed functionality that has shipped, changed, or been abandoned.

Never rewrite a page solely because a fixed interval elapsed. Time is a review trigger, not evidence that content is stale.

## Produce the radar report

Return or persist:

1. scope, period, and source coverage;
2. product and audience changes observed;
3. ranked candidate queue with scores and evidence;
4. recommended outcome for each candidate;
5. refresh, consolidate, and retire queue;
6. measurement or evidence-gathering tasks;
7. internal-link and documentation opportunities;
8. approved-source distribution opportunities;
9. candidates rejected and why;
10. the next three actions, each with owner approval requirements;
11. checked-on date and next sensible review trigger.

For each `publish now` or `brief next` item, include a compact handoff containing the page job, triggering question, direct-answer hypothesis, original contribution, first-party evidence, external sources needed, and claims that must not be made.

## Automation boundary

This Skill is safe to schedule as a read-only recurring report when the required sources are connected. A scheduled run may inspect and rank; it must not create site commits, publish pages, post derivatives, contact people, or change accounts.

Suppress empty reports. When no candidate crosses the evidence threshold and no page requires refresh, report that no action is warranted rather than inventing a content obligation.

## Quality gates

The radar is invalid when candidates lack direct evidence; scores lack explanations; private material is exposed; keyword volume substitutes for reader need; every product change becomes content; existing pages are ignored; rejected ideas disappear without rationale; stale claims are reported without checking current behaviour; or the output implies that ranking, citation, or traffic is guaranteed.

## Integration boundaries

- `$asdecided-publishing` turns approved candidates into canonical pages and owns evidence, drafting, and citation readiness.
- `$asdecided-distribute` creates derivatives from approved canonical sources.
- `$community-radar` verifies public communities and conversations.
- `$launch-pack` owns release-wide channel coordination.
- Specialist SEO tools may supply crawl, performance, indexing, schema, Search Console, and site-inventory evidence; this Skill owns editorial prioritization.

All integrations are optional. The Skill must remain useful when extracted from the toolkit.

## Safety and integrity boundary

Never fabricate questions, traffic, rankings, mentions, citations, customer demand, community activity, or product evidence. Never recommend mass generation, scraped-content variants, doorway pages, reciprocal link schemes, automated community participation, or publishing to satisfy a quota. Report uncertainty and source limitations explicitly.
