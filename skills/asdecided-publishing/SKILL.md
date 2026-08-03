---
name: asdecided-publishing
description: Research, draft, revise, and preflight AsDecided articles and durable web pages so they are useful to software teams, technically credible, indexable by search engines, extractable by answer engines, and citable by coding agents. Use when creating or improving AsDecided.com articles, guides, comparisons, definitions, product pages, documentation-adjacent essays, or publishing briefs; when turning product or repository evidence into citation-worthy content; or when auditing a draft for SEO, GEO, AEO, structured data, source quality, entity clarity, and agent retrieval. Do not use for generic SEO audits, keyword-volume farming, backlink spam, unsupported thought leadership, automated publishing, or content unrelated to AsDecided.
---

# AsDecided Publishing

Publish the clearest useful answer to the question. Earn citations by being specific, inspectable, and worth citing—not by repeating keywords.

Read [agent-citation-scorecard.md](references/agent-citation-scorecard.md) before reviewing a draft or declaring a page ready.

## Operating principles

1. Help the reader complete a real decision or task.
2. State the answer early; do not hide it behind scene-setting.
3. Prefer original evidence, concrete examples, and falsifiable claims over generic commentary.
4. Separate what AsDecided currently does from what it recommends, intends, or may support later.
5. Write for humans first while making important passages safe to retrieve and quote accurately.
6. Never claim that `llms.txt`, schema, metadata, or a writing pattern guarantees indexing, ranking, inclusion, or citation.
7. Never manufacture authority through invented benchmarks, customers, quotes, integrations, or consensus.

## Establish the publishing contract

Inspect the supplied repository, site, issue, release, brief, article, or decision record. Build a compact ledger:

- `Confirmed`: supported by current first-party product or repository evidence.
- `Observed`: measured or reproduced during this task, with method and date.
- `Attributed`: supported by a named external source.
- `Inferred`: a reasoned interpretation that remains labelled.
- `Proposed`: future behaviour, recommendation, or roadmap item.
- `Unknown`: material information that could not be verified.

Do not draft product claims until the relevant ledger entries exist. Use **AsDecided** for the product and brand; use `decided` for the CLI only where current evidence verifies it.

Assign one primary page job: `definition`, `how-to`, `decision guide`, `technical argument`, `reference`, `product explanation`, `comparison`, or `research note`. The title, opening, structure, and next action must serve that job.

## Research before prose

Current web research is required for time-sensitive claims, standards, external product behaviour, competitor capabilities, search-platform guidance, and direct quotations. Prefer:

1. official documentation, specifications, repositories, release notes, and first-party statements;
2. original research, papers, datasets, and reproducible measurements;
3. high-quality independent technical analysis;
4. community evidence only for claims about community experience or practice.

Record the source URL, publisher, title, supported claim, visible publication or update date, checked-on date, and whether it is primary. Put citations beside the claims they support. For AsDecided behaviour, prefer current repository behaviour and documentation over older marketing copy.

## Build the answer architecture

A substantive page should normally include:

1. a specific title matching the reader's real question;
2. a two-to-four sentence direct answer near the top;
3. a precise definition of the central entity or term;
4. the practical problem and affected workflow;
5. the mechanism or recommended approach;
6. at least one concrete example, decision, repository scenario, command, schema, measurement, or failure mode;
7. trade-offs, limits, and cases where the approach is wrong;
8. a concise conclusion or next action;
9. adjacent sources and visible freshness context where relevant.

Use headings that remain meaningful when extracted alone. Do not manufacture an FAQ structure merely for schema or search appearance.

## Write citation-worthy passages

For each central claim:

- name the subject explicitly;
- state one main proposition per paragraph;
- define uncommon terms on first use;
- include scope, conditions, and important exceptions nearby;
- use concrete dates, versions, commands, and paths when material;
- place the supporting citation immediately after the supported claim;
- distinguish product fact, recommendation, inference, and opinion;
- avoid unsupported superlatives, vague market claims, and circular definitions.

Include a compact quotable definition only when it helps the reader. Do not write synthetic soundbites solely for agents.

## Require original value

Do not publish a page that merely paraphrases existing results. Every substantive page must contribute at least one original framework, reproducible measurement, implementation pattern, worked example, novel synthesis, product-specific observation, negative result, failure mode, or evidence-backed checklist. Name that contribution in the publishing brief.

## Run the discoverability preflight

Inspect or specify:

- one indexable canonical URL;
- reliably accessible primary content;
- unique title and meta description aligned with the page job;
- canonical, Open Graph, and social-card metadata;
- one H1 and a logical heading hierarchy;
- useful internal links from relevant AsDecided pages;
- stable links to primary evidence;
- sitemap inclusion and sensible `robots.txt` behaviour;
- no accidental `noindex`, authentication wall, script-only content, or canonical mismatch;
- visible author, publisher, published date, modified date, and checked-on date where relevant;
- structured data that matches visible content.

Recommend Schema.org types conservatively. Typical candidates are `Article`, `TechArticle`, `SoftwareApplication`, `Organization`, `Person`, and `BreadcrumbList`. Use `FAQPage` only for genuine visible questions and answers. Treat `llms.txt` as an optional navigation aid, never as an indexing or citation mechanism.

## Run the agent-access preflight

Confirm an unauthenticated agent can retrieve the same substantive content a human sees. Flag facts available only after interaction, content trapped in images or video, ambiguous entities, inconsistent naming, remote evidence, inaccessible tables, context-free code, stale claims, and paragraphs likely to become misleading when extracted.

Never recommend cloaking, agent-specific factual variants, or materially different claims for bots and users.

## Draft and review workflow

### 1. Produce the publishing brief

Include the page job, target reader, triggering question, direct answer, entity names, evidence ledger, original contribution, required examples, source plan, internal links, structured-data choice, forbidden claims, freshness requirements, and review trigger.

### 2. Draft

Write in AsDecided's voice: direct, technically literate, calm, specific, and candid about trade-offs. Avoid generic SaaS language, SEO filler, inflated urgency, unexplained jargon, and repetitive conclusions.

### 3. Run the citation review

Mark every material externally verifiable claim as `Cited`, `First-party`, `Observed`, `Qualified`, or `Removed`. Any unmarked material claim blocks publication.

### 4. Run the extraction review

Read only the title, opening answer, headings, first sentence of each section, definitions, tables, captions, and conclusion. The reduced view must still identify the topic, answer, audience, mechanism, important limitation, and what is specifically true about AsDecided.

### 5. Produce and validate the Agent Citation Scorecard

Create the JSON scorecard defined in [agent-citation-scorecard.md](references/agent-citation-scorecard.md). Every check needs evidence. Warnings need a risk and follow-up; `na` needs a reason; failures block readiness.

Validate the persisted scorecard:

```bash
python3 scripts/validate_agent_citation_scorecard.py agent-citation-scorecard.json
```

The scorecard measures citation readiness and extraction safety. It does not predict or guarantee that an agent or answer engine will cite the page.

### 6. Deliver the publication package

Return or persist:

1. publishing brief;
2. finished draft;
3. evidence and citation ledger;
4. Agent Citation Scorecard and validator result;
5. metadata recommendation;
6. structured-data recommendation or implementation;
7. internal-link plan;
8. technical and agent-access findings;
9. blocked claims and unresolved unknowns;
10. checked-on date and review trigger.

## Quality gates

A page is not ready when the opening does not answer the title; it lacks original value; AsDecided behaviour lacks current first-party evidence; a material claim lacks support or qualification; citations are remote; a source is misrepresented; entities are ambiguous; examples are placeholders; trade-offs are missing; metadata overpromises; schema exceeds visible content; primary content is inaccessible; the draft relies on keyword repetition or synthetic FAQs; a paragraph becomes misleading when extracted; or the Agent Citation Scorecard is incomplete or blocked.

## Integration boundaries

- A specialist SEO suite may crawl the site, measure performance, inspect Search Console, validate schema at scale, or run broad technical audits. This Skill owns AsDecided's publishing standard and page-level citation readiness.
- `$community-radar` may identify recurring questions worth turning into durable articles.
- `$merge-and-tell` may adapt an approved article into public communication.
- `$launch-pack` owns coordinated release packaging.
- `$authored-frontend-design` owns substantial visual and interaction design.

All integrations are optional. The Skill must remain useful when extracted from the toolkit.

## Safety and integrity boundary

Never fabricate sources, quotes, dates, results, customers, rankings, traffic, citations, or agent mentions. Never imply platform endorsement without evidence. Never automate publication, outreach, link placement, or account changes without explicit authorization. Never recommend doorway pages, cloaking, scraped-content multiplication, fake authorship, schema abuse, hidden text, or manipulative link schemes. Report weak evidence, crawl blocks, stale content, ambiguous claims, and likely non-citation candidly.
