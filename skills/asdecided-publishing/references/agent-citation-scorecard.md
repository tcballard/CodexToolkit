# Agent Citation Scorecard

Use this scorecard for every substantive AsDecided article, guide, comparison, definition, research note, or durable product page. It is a publication gate, not a claim that an answer engine will cite the page.

## Status values

- `pass`: the criterion is satisfied with concrete evidence.
- `warn`: the page is usable, but a material weakness or uncertainty remains.
- `fail`: the criterion is not satisfied and publication is blocked.
- `na`: the criterion genuinely does not apply; include a reason.

Every item must include evidence. A bare status is invalid.

## Required checks

### `direct_answer`

The opening answers the page title or triggering question within the first 200 words.

Evidence should quote or identify the opening answer and explain how it resolves the question.

### `extractable_definitions`

The central term, product, mechanism, or distinction is defined in a passage that remains accurate when extracted alone.

Evidence should identify the definition and confirm that its subject, scope, and important limitation are explicit.

### `entity_clarity`

Product, organisation, CLI, standards, competitors, and other named entities are unambiguous and named consistently across copy, metadata, schema, repository evidence, and links.

Evidence should list the important entities and note any aliases or naming boundaries.

### `original_contribution`

The page contributes more than a paraphrase of existing results. It includes at least one original framework, worked example, measurement, implementation pattern, synthesis, product observation, negative result, or evidence-backed checklist.

Evidence should name the contribution and point to where it appears.

### `claim_evidence_proximity`

Material factual claims are supported by adjacent citations, first-party evidence, documented observation, or explicit qualification.

Evidence should summarize the citation review and identify any remaining weak claims.

### `stable_primary_sources`

Important external claims rely primarily on stable first-party documentation, specifications, repositories, papers, datasets, or original research rather than copied summaries.

Evidence should identify the primary sources and disclose unavoidable secondary sources.

### `structured_data_fidelity`

Recommended or implemented structured data matches visible page content and does not invent authorship, reviews, FAQs, dates, product capabilities, or other facts.

Evidence should state the selected Schema.org types and the visible content supporting them. Use `na` only when no structured data is appropriate.

### `retrieval_access`

An unauthenticated agent can retrieve the substantive content without requiring interaction, login, image interpretation, video playback, inaccessible embeds, or script-only state.

Evidence should describe the retrieval path and any rendering dependency.

### `paragraph_extraction_safety`

Central paragraphs can be extracted without changing the meaning through missing antecedents, hidden conditions, remote caveats, or unsupported certainty.

Evidence should record the extraction review and any passages revised.

### `freshness_context`

Time-sensitive claims, product behaviour, standards, comparisons, and measurements include enough version, date, checked-on, or review-trigger context to avoid appearing timeless when they are not.

Evidence should identify the freshness markers or justify `na` for stable material.

## Readiness rule

A scorecard is `ready` only when:

- all ten required checks are present;
- no required check is `fail`;
- every `warn` includes a concrete risk and follow-up;
- every `na` includes a reason;
- the article has passed the Skill's separate quality gates.

Warnings do not automatically block publication, but the final package must surface them prominently. The author or owner makes the final publication decision.

## JSON contract

Persist the scorecard as JSON when validation is useful:

```json
{
  "page": {
    "title": "How should AI coding agents use architecture decisions?",
    "url": "https://asdecided.com/articles/example",
    "checked_on": "2026-08-03"
  },
  "checks": {
    "direct_answer": {
      "status": "pass",
      "evidence": "The opening states the recommended control loop in the first paragraph."
    },
    "extractable_definitions": {
      "status": "pass",
      "evidence": "The second paragraph defines an architectural decision system with its scope."
    },
    "entity_clarity": {
      "status": "pass",
      "evidence": "AsDecided is consistently the product; decided is identified only as the CLI."
    },
    "original_contribution": {
      "status": "pass",
      "evidence": "The article contributes a repository-to-agent enforcement loop and worked example."
    },
    "claim_evidence_proximity": {
      "status": "warn",
      "evidence": "One ecosystem claim uses a secondary source.",
      "risk": "The claim may become stale or inherit the source's interpretation.",
      "follow_up": "Replace it with first-party documentation before the next review."
    },
    "stable_primary_sources": {
      "status": "pass",
      "evidence": "Standards and product behaviour link to specifications and current repositories."
    },
    "structured_data_fidelity": {
      "status": "pass",
      "evidence": "TechArticle, Person, Organization, and BreadcrumbList match visible fields."
    },
    "retrieval_access": {
      "status": "pass",
      "evidence": "The complete article is available in server-rendered HTML without authentication."
    },
    "paragraph_extraction_safety": {
      "status": "pass",
      "evidence": "The reduced-view review retained subject, scope, mechanism, and limitation."
    },
    "freshness_context": {
      "status": "pass",
      "evidence": "Product behaviour is tied to a checked-on date and repository revision."
    }
  }
}
```

Validate it with:

```bash
python3 scripts/validate_agent_citation_scorecard.py agent-citation-scorecard.json
```
