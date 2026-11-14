# Algorithm source review: 14 November 2026

## Scope and method

Official head: `590f3926e5bc33c50d9ece13953623e1e75ee595`, published 13 November 2026 at 21:42:04 UTC. Both installed and maintained copies matched the 6 November baseline `2e2295b0df598eee5aa05f9c9b458f4490c7fcbe` before editing. The complete comparison has five commits and 287 changed paths, with 24,121 additions and 13,520 deletions.

Inventory every changed path, then inspect guidance-relevant behavior, parameter consumers and defaults. This review covers all guidance categories but does not assert line-by-line review of every infrastructure change, complete behavioral equivalence of refactors, production deployment or causal effects on reach. No account analytics, live checkpoints, experiments or reach trials were available. The author's reported decline motivates the diagnostic workflow; it does not establish a cause.

## Coverage ledger

| Area | Changed paths | Treatment and limits |
|---|---:|---|
| Home Mixer | 83 | Inspect parameter diff, local/service request wiring, topic/recent-view transport, selection/filter changes, carousel, trace delivery and diversity diagnostics. Classify hydration performance rewrites, ads and frames separately; no blanket semantic-equivalence claim. |
| VM Ranker | 7 | Inspect defaults, DPP history window, greedy score reassignment and service resolution. Recheck unchanged scoring defaults and adjustment paths. |
| Phoenix | 26 | Inspect model/config changes and recent-positive history defaults; classify data loaders, CUDA, embedding transfer, ads-side inputs and export/training plumbing as infrastructure. No numerical-equivalence or deployed-checkpoint claim. |
| Phoenix rankall / strato | 3 | Inspect new AI-video self/declaration/detection indexes and window exclusions; candidate indexing is not a blanket AI-text/media penalty. |
| Candidate pipeline | 7 | Hydration/partition/selection and trace infrastructure; inspect filter consumers, without full runtime validation. |
| Visibility filtering | 115 | Inspect rule audiences, safety-level lists and diagnostic scope. Broad hydration, engine, treatment and test moves are not proven equivalent end to end. |
| Visibility client | 8 | Interface, hydration and notification plumbing; keep surfaces distinct. |
| Safety label source | 9 | Retrieval/cache infrastructure; no inferred writing reward or account diagnosis. |
| Abuse enforcement | 14 | Label-write deduplication/action control; existing rule YAML is unchanged. Do not infer a new blanket AI-writing policy. |
| Grox | 14 | Inspect multi-media safety chunking and configuration changes; no image-count or AI-assisted-writing penalty inferred. |
| SimClusters | 1 | Retrieval-job infrastructure; no keyword recipe inferred. |

## Material changes

| Change | Interpretation |
|---|---|
| Home copied-link share weight `20 → 0`; service remains `20` | Correct the two-column table. Local and service formulas differ; this does not mean external links are penalised or sharing is worthless. |
| DPP greedy-order and sliding-history support | Defaults `false` / window `0`; Home history transport also false. Describe optional score reassignment without inventing a live repetition penalty. |
| Recent-view / candidate-topic transport | Default-off. Topic annotations in request data do not establish a ranking reward or mandatory niche. |
| New-viewer ratio switch `false → true`; threshold `0 → 0.004` | Parent filter remains false; viewer age/resurrection and out-of-network candidate scope matter. Not a target engagement rate. |
| Carousel seen/medium-risk filtering turns on within module | Parent carousel remains false. CTR model is named but its switch stays false. New take-from-feed switch and not-interested weight remain inactive. |
| Optional recent-positive model history scaling/dropout | Scale `1`, dropout `0`; no default adjustment. No early-engagement timing recipe follows. |
| Trace-frame delivery and cross-page/session diversity metrics | Feature-gated diagnostics and measurements; no causal account-reach explanation. |
| `DoNotAmplify` / `MaliciousUrl` audiences become non-followers; notification spam rule changes | Eligibility rules must be read with their surfaces and labels. No blanket link penalty inferred. |
| Multi-media safety processing and label deduplication | Safety/action infrastructure; no universal carousel suppression inferred. |

## Rechecked boundaries

Shared value-model scoring and weights files, local value-model mapping, service value-model resolution, author cold-start scorer and retrieval two-tower configuration have no changes against this baseline. Home's copied-link default still maps into local scoring; VM Ranker still resolves its own default and retains `compute_value_model=true` request wiring. Cached/fallback distinctions continue to matter.

The out-of-network reply filter's changes are tests, not new eligibility predicates. Fair-share and duplicate handling change implementation; inspected predicates/grouping remain consistent with earlier guidance. Cold-start gates, author-diversity defaults and the other documented numerical scoring defaults remain as recorded. Topic/history and DPP extensions must not be confused with measurements in the diversity side effect.

No inspected source establishes a 50%-visible impression rule, optimal post length, mandatory topic exclusivity, universal link placement rule, or guaranteed recovery from a reach decline. Feed visibility is an editorial/layout preference. Use comparable post analytics to investigate performance.

## Validation

Validate frontmatter and local reference links in the installed directory. Check every pinned source-file path against the reviewed checkout and compare every table coefficient with both Rust parameter files. Forward-test ordinary drafting and reduced-reach interpretation using the edited skill. Run the existing weighted-length helper tests. Compare the maintained skill directory byte for byte after copying, excluding generated dependency directories, and disclose whether the maintained update is merged or proposed.
