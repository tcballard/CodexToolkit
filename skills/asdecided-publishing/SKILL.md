---
name: asdecided-publishing
description: Research, draft, revise, and preflight AsDecided articles and durable web pages so they are useful to software teams, technically credible, indexable by search engines, extractable by answer engines, and citable by coding agents. Use when creating or improving AsDecided.com articles, guides, comparisons, definitions, product pages, documentation-adjacent essays, or publishing briefs; when turning product or repository evidence into citation-worthy content; or when auditing a draft for SEO, GEO, AEO, structured data, source quality, entity clarity, and agent retrieval. Do not use for generic SEO audits, keyword-volume farming, backlink spam, unsupported thought leadership, automated publishing, or content unrelated to AsDecided.
---

# AsDecided Publishing

Publish the clearest useful answer on the question. Earn citations by being specific, inspectable, and worth citing—not by repeating keywords.

This Skill is intentionally opinionated for AsDecided. It treats architectural decisions as durable technical artifacts and assumes the audience includes software engineers, technical leads, architects, engineering managers, platform teams, and AI coding-agent users.

## Operating principles

1. Help the reader complete a real decision or task.
2. State the answer early; do not hide it behind scene-setting.
3. Prefer original evidence, concrete examples, and falsifiable claims over generic commentary.
4. Separate what AsDecided currently does from what it recommends, intends, or may support later.
5. Write for humans first, while making important passages easy for search and answer systems to retrieve accurately.
6. Never claim that `llms.txt`, schema, metadata, or a particular writing pattern guarantees indexing, ranking, inclusion, or citation.
7. Never manufacture authority through invented benchmarks, customers, quotes, integrations, or consensus.

## Establish the publishing contract

Before drafting, inspect the supplied repository, site, issue, release, product brief, prior article, or decision record. Build a compact ledger:

- `Confirmed`: directly supported by current product, repository, first-party documentation, or primary evidence.
- `Observed`: directly measured or reproduced during this task, including the method and date.
- `Attributed`: supported by a named external source.
- `Inferred`: a reasoned interpretation that must be labelled as such.
- `Proposed`: future behaviour, design, recommendation, or roadmap item.
- `Unknown`: material information that could not be verified.

Do not draft product claims until the relevant ledger entries exist. Resolve naming consistently: **AsDecided** is the product and brand; `decided` is the CLI only where verified by current product evidence.

## Choose the page job

Assign one primary job before writing:

- `definition`: establish a precise term and why it matters;
- `how-to`: help a reader complete a specific workflow;
- `decision guide`: compare approaches and state when each fits;
- `technical argument`: defend a position with evidence and limits;
- `reference`: provide durable facts, interfaces, schemas, commands, or conventions;
- `product explanation`: explain verified AsDecided behaviour and boundaries;
- `comparison`: compare named approaches without straw-manning competitors;
- `research note`: publish original observations, measurements, or synthesis.

One page may support secondary jobs, but the opening, title, structure, and call to action must serve the primary job.

## Research before prose

Current web research is required for time-sensitive claims, standards, search-engine guidance, product behaviour outside the repository, competitor capabilities, and direct quotations. Prefer primary sources in this order:

1. official documentation, specifications, standards, repositories, release notes, or first-party statements;
2. original research, papers, datasets, and reproducible measurements;
3. high-quality independent technical analysis;
4. community evidence only when the claim is explicitly about community experience or practice.

Record source URL, publisher, title, relevant claim, publication or update date when visible, checked-on date, and whether the source is primary. Place citations next to the claim they support. Do not collect sources merely to decorate the article.

For an AsDecided product claim, prefer current repository behaviour and documentation over older marketing copy. If sources conflict, say so and narrow the claim.

## Build the answer architecture

A strong AsDecided page normally contains:

1. a specific title matching the reader's real question;
2. a two-to-four sentence direct answer near the top;
3. an explicit definition of the central entity or term;
4. the practical problem and affected workflow;
5. the mechanism or recommended approach;
6. at least one concrete example, decision, repository scenario, command, schema, or failure mode;
7. trade-offs, limits, and cases where the approach is wrong;
8. a concise conclusion or next action;
9. directly adjacent sources and a checked-on date where freshness matters.

Use descriptive headings that remain meaningful when extracted alone. Prefer question headings when users genuinely ask that question; do not turn every heading into a contrived FAQ.

## Write citation-worthy passages

Important passages should survive extraction without misleading the reader. For each central claim:

- name the subject explicitly rather than relying on pronouns;
- state one main proposition per paragraph;
- define uncommon terms on first use;
- include scope, conditions, and exceptions in the same passage;
- use concrete nouns, dates, versions, commands, and repository paths when material;
- place the supporting citation immediately after the supported sentence or paragraph;
- distinguish product fact, recommendation, inference, and opinion;
- avoid unsupported superlatives, vague market claims, and circular definitions.

Include a compact quotable definition only when it is genuinely useful. Do not write synthetic soundbites solely for agents.

## Original-value requirement

Do not publish a page that merely paraphrases existing search results. Every substantive article must contribute at least one of:

- an original framework or decision model;
- a reproducible test or measurement;
- an implementation pattern;
- a concrete worked example;
- a novel synthesis across primary sources;
- a product-specific observation grounded in current behaviour;
- a useful negative result, trade-off, or failure mode;
- a reusable checklist tied to evidence.

State which contribution the page makes in the publishing brief.

## Technical discoverability preflight

Inspect or specify, as appropriate:

- one indexable canonical URL;
- server-rendered or otherwise reliably accessible primary content;
- unique title and meta description aligned with the page job;
- canonical, Open Graph, and social-card metadata;
- one clear H1 and logical heading hierarchy;
- descriptive internal links from relevant AsDecided pages;
- links to primary evidence using stable URLs;
- sitemap inclusion and sensible `robots.txt` behaviour;
- no accidental `noindex`, authentication wall, script-only content, or canonical mismatch;
- article author, publisher, published date, modified date, and checked-on date where relevant;
- structured data that matches visible content.

Recommend Schema.org types conservatively. Typical candidates include `Article`, `TechArticle`, `SoftwareApplication`, `Organization`, `Person`, and `BreadcrumbList`. Use `FAQPage` only when the page visibly contains genuine questions and answers and current platform guidance makes it appropriate. Never add schema for content the reader cannot see.

Treat `llms.txt` as an optional navigation aid, not an indexing or citation mechanism. It must not substitute for crawlable pages, strong internal linking, sitemaps, or clear documentation.

## Agent-access preflight

Check whether an unauthenticated agent can retrieve the same substantive content a human sees. Flag:

- essential facts available only after client-side interaction;
- content hidden in images, video, canvas, or inaccessible embeds;
- ambiguous product or organisation identity;
- inconsistent naming across title, copy, schema, repository, and metadata;
- important claims separated from their evidence;
- tables without surrounding prose or clear headers;
- code samples without language, context, expected result, or version assumptions;
- stale pages that lack visible update context;
- unsupported claims likely to be repeated inaccurately when extracted.

Do not recommend cloaking, agent-specific factual variants, or serving materially different claims to bots and users.

## Internal-link model

Link for understanding, not PageRank theatre. Each article should identify:

- the parent concept or product page;
- prerequisite definitions;
- directly related decisions or implementation guides;
- one logical next question;
- relevant AsDecided documentation or repository evidence.

Use descriptive anchor text. Avoid repeated exact-match anchors, orphan pages, sitewide keyword links, and unrelated cross-linking.

## Draft and review workflow

### 1. Produce a publishing brief

Include:

- primary page job;
- target reader and triggering question;
- direct answer;
- confirmed entity names;
- evidence ledger;
- original contribution;
- required examples;
- source plan;
- likely internal links;
- appropriate structured data;
- claims that must not be made;
- freshness and review requirements.

### 2. Draft

Write in AsDecided's preferred voice: direct, technically literate, calm, specific, and candid about trade-offs. Avoid generic SaaS language, SEO filler, inflated urgency, unexplained jargon, and repetitive conclusions.

### 3. Run the citation review

For every externally verifiable claim, mark one outcome:

- `Cited`: supported by an adjacent source;
- `First-party`: supported by inspected AsDecided evidence;
- `Observed`: reproduced and documented during this task;
- `Qualified`: narrowed so it no longer overclaims;
- `Removed`: unsupported or unnecessary.

Any remaining unmarked material claim blocks publication.

### 4. Run the extraction review

Read only the title, opening answer, headings, first sentence of each section, definitions, tables, captions, and conclusion. Confirm that this reduced view still identifies:

- what the page is about;
- the direct answer;
- who the advice applies to;
- the main mechanism;
- the important limitation;
- what is specifically true about AsDecided.

Repair ambiguity without making the prose robotic.

### 5. Deliver the publication package

Return or persist:

1. publishing brief;
2. finished draft;
3. evidence and citation ledger;
4. metadata recommendation;
5. structured-data recommendation or implementation;
6. internal-link plan;
7. technical and agent-access findings;
8. blocked claims and unresolved unknowns;
9. checked-on date and review trigger.

## Quality gates

A page is not ready when any of the following is true:

- the opening does not answer the title;
- the article lacks an original contribution;
- AsDecided behaviour is described without current first-party evidence;
- a material factual claim lacks evidence or qualification;
- citations are remote from the claims they support;
- a quoted or paraphrased source is misrepresented;
- the central term or entity is ambiguous;
- examples are generic placeholders rather than plausible technical scenarios;
- recommendations omit meaningful trade-offs or failure cases;
- metadata promises something the page does not deliver;
- structured data contradicts or exceeds visible content;
- primary content is inaccessible without interaction or authentication;
- the draft relies on keyword repetition, mass-produced variants, or synthetic FAQs;
- the page could plausibly mislead an agent when a paragraph is extracted alone.

## Integration boundaries

- A specialist SEO suite may crawl the whole site, measure performance, inspect Search Console, validate schema at scale, or perform broader technical audits. This Skill owns AsDecided's publishing standard and page-level citation readiness.
- `$community-radar` may identify recurring questions and conversations worth turning into durable articles.
- `$merge-and-tell` may adapt an approved article into public launch or social communication.
- `$launch-pack` owns coordinated release packaging across channels.
- `$authored-frontend-design` owns substantial visual and interaction design for article or documentation surfaces.

All integrations are optional. The Skill must remain useful when extracted from the toolkit.

## Safety and integrity boundary

- Never fabricate sources, quotes, dates, test results, customers, rankings, traffic, citations, or agent mentions.
- Never imply endorsement by OpenAI, Google, Anthropic, Microsoft, Perplexity, or another platform without explicit evidence.
- Never automate publication, outreach, link placement, or account changes without explicit authorization.
- Never recommend doorway pages, cloaking, scraped-content multiplication, fake authorship, review schema abuse, hidden text, or manipulative link schemes.
- Report weak evidence, crawl blocks, stale content, ambiguous claims, and likely non-citation candidly even when they reduce the publishing recommendation.
