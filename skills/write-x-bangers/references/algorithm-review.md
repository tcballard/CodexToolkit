# Algorithm source review: 6 November 2026

## Scope and method

Official head: `2e2295b0df598eee5aa05f9c9b458f4490c7fcbe`, published 2026-11-06 03:48:04 UTC. Installed evidence baseline: `74d49a4ffb398949a5f9312f828d7112d7d31f00`, 20 October. Maintained bundle baseline: `6258a1549ef808be88fba83d3b2d58364b587ee0`, source dated 24 October and reviewed 26 October. The bundle had newer evidence but identical other skill contents; both were reconciled without discarding the newer findings.

The complete installed-baseline diff contains 484 paths across 13 commits, 62,240 added and 34,438 deleted lines. The newer bundle comparison contains 397 paths. Inventory all paths; inspect behavior-changing code for each guidance category; trace changed settings to consumers and distinguish training, diagnostics, experiments and runtime defaults. Recheck unchanged core claims where they constrain the advice. The full comparison links and pinned source files are in `x-ranking.md`.

This is a static, comprehensive guidance refresh, not a proof of behavioral equivalence for every changed line. No production requests, model checkpoints, live experiments or reach results were available. GPU kernel correctness, all enforcement edge cases and deployment infrastructure were not exhaustively audited. Do not relabel the path inventory as a complete implementation audit.

## Coverage ledger

| Area | Changed paths | Review treatment |
|---|---:|---|
| Home Mixer | 89 | Inspect defaults, scorer/request/service wiring, source allocation, retrieval context, filters, page selection, carousel, history and diagnostics; classify ads/cache/client work separately. |
| VM Ranker | 11 | Inspect new debiasing gates, score recomputation/cache behavior, top-head reporting, carousel-model integration and service parameters. |
| Shared value model | 5 | Inspect all shared scoring/weight/proto changes; preserve prediction-versus-count distinction. |
| Phoenix | 125 | Inspect ranking/retrieval configuration, output meanings, feature preparation, losses and page-RL wiring; classify CUDA/attention/packing/checkpoint/optimizer work as model/runtime infrastructure without numerical-equivalence claims. |
| Visibility filtering | 161 | Inspect changed surface/rule definitions and relevant eligibility effects; classify broad hydration/engine/test refactors without claiming complete semantic equivalence. |
| Enforcement service | 39 | Inspect user/post rule changes and label pathways; classify action-control, backfill, confidence and rollback machinery separately from organic ranking. |
| Grox | 15 | Inspect classifier routing, mention/media-tag handling and video processing changes; no new copy formula follows from classifier plumbing. |
| Safety label source | 10 | Label retrieval/cache infrastructure; no inferred writing bonus. |
| Visibility client | 5 | Interface, discovery and notification wiring; distinguish surfaces. |
| Under the Hood | 17 | Inspect trace-page gate and score reporting alongside aggregate labels; do not promise universal diagnostic access. |
| Scarecrow | 3 | Review-intake/report infrastructure; no copy tactic inferred. |
| Candidate pipeline | 2 | Trace/partition helper changes; verify inspected age, relationship and seen/reply predicates retain their meanings. |
| Botmaker rules | 1 | Datacenter-derived feature change; not a writing rule. |
| README | 1 | Recheck publication scope, configuration caveats and pipeline description against implementation. |

## Material changes and their limits

| Change since installed baseline | Evidence interpretation |
|---|---|
| Home weights: favorite 0.66 → 0.708; share 2.0 → 2.118; click 0.3 → 0.274; video-open 0.02 → 0; continuous dwell 0.006 → 0.0075; click dwell 0.4 → 0.385; not interested -52.272 → -53.07 | VM Ranker's corresponding defaults are unchanged. Compare both; do not claim a unique production formula or reach uplift. |
| `react_with_video` renamed to `post_video`; `grok_analyze` added | Both default to zero in both scoring consumers; no engagement solicitation tactic. |
| Excursion history becomes the Home aggregation default; excursion score transport enabled | Training/feature evidence is stronger than the earlier shadow-only description; direct video-continuation/profile-visit weights remain zero. |
| Default-on fair-share pre-score capacity allocation | Proportional by retrieval served type, not author fairness or equal topic exposure. Already documented in the newer bundle. |
| Retrieval weight override plumbing and recent-search hydration | Empty override/default-off hydration (with shadow exception); no keyword recipe. Already partly documented in the newer bundle. |
| Page decode and exploration integrated into Home pipeline | Both default-off; distinguish page-order experiments from ordinary weighted post scoring. |
| User-debias transport enabled; correction service added | Correction remains default-off and artifact-dependent. Diagnostic/cache exceptions matter. |
| Carousel scoring, safety and history extensions | Carousel and several new features remain default-off; high-risk/missing-verdict filtering is within that module. |
| Topic-history language counts and serendipity observations expanded | Measurements, not a demonstrated language or novelty reward. |
| Existing `llm_slop_user` and majority-poster spam-label TTLs shorten to seven days | Existing enforcement pathway; not a new blanket ban on AI-assisted writing. The classifier criteria are not fully published. |
| Spam/liveness/impersonation rule updates; notification/reaction/media rules | Eligibility and enforcement work, not ranking coefficients. Some thresholds are explicitly placeholders. |
| Standalone Brazil election filter removed | Do not generalise to all legal-label restrictions, which still have separate code. |
| Request trace and top weighted-head diagnostic support | Feature-gated, request-specific information; not a complete causal account-reach explanation. |

## Rechecked boundaries

- Cold-start scorer is unchanged from the installed baseline. The original-post, two-hour, 50,000-follower and 200-Home-impression gates remain conditional exploration, not promised exposure.
- Out-of-network reply filtering was refactored to a partition helper without changing the inspected predicates. Reply exceptions stay default-off.
- Service author diversity, DPP, mutual-follow reply boost and ordinary OON defaults remain; topic OON 0.5 is an existing distinction now made explicit.
- The combined favorite/dwell retrieval targets remain. Optional click-head support is not evidence that it is enabled in that configuration.
- Click-dwell's generic zero training fallback must not obscure the named Home configuration's inherited nonzero loss. Field names alone do not establish raw seconds or reading completion.
- Popular retrieval and exclusive-zero-favorite-source gating retain their documented scope.
- No inspected source establishes five-sentence rewards, a mandatory single niche, a six-month promotion entitlement, income guarantees or a universal media/link-placement rule.

## Validation

Validate frontmatter and local references, verify every pinned GitHub path at the reviewed SHA, mechanically compare documented numeric coefficients with both source parameter files, and forward-test the optional format and algorithm explanations. Validate the installed directory itself before saving. Compare all maintained skill files byte for byte after updating the bundle; report whether the bundle update is merged or still proposed.
