# X ranking mechanics

## Evidence status

Checked 24 September 2026 against official default-branch head `44d37ebf87f2185b949cd37b710d410c2a77d21f` (01:53:14 UTC). Home-mixer defaults header synchronized 23 September, 16:28:43 UTC. Compared with the installed 17 September baseline `42266f3e2be54d8a3c4d2228aac2e8f8d1c1f034`, incorporating the maintained bundle’s draft 21 September review of `8b25829717a4f104dd04403ee7d0253c5fedb1b7`.

Scope: targeted static inspection of changes to the published For You retrieval, scoring defaults and wiring, diversity, cold-start eligibility, and reply-spam paths; not a full audit of every upstream change. Publication is not proof of deployment date, experiment allocation or exact production predictions. Some dependencies, prompts, weights and anti-abuse internals are unavailable. Other surfaces can behave differently.

Distinguish **published mechanism** (source-backed behavior and defaults), **editorial judgment** (a writing choice), and **hypothesis to test** (an unverified performance explanation). Do not present an inference as an algorithm rule.

## Published mechanisms

Retrieval precedes scoring. Followed-account and discovery sources create candidates, including Phoenix and SimClusters. The inspected Phoenix retrieval configuration uses favorites as positive targets; SimClusters also uses favorite-based representations. A low final like coefficient does not make likes irrelevant to discovery. Semantic and author representations are not a keyword recipe.

Phoenix predicts viewer-specific actions from content and history. Ranking combines probabilities and continuous outputs, then applies additional adjustments and selection. Visibility, age, previously seen/served history, social context and conversation deduplication can affect eligibility. A good hypothetical score does not guarantee an impression.

Scoring now uses shared arithmetic in `xai-value-model/scoring.rs`. Home-mixer computes local weighted scores and cold-start decisions, then requests value-model computation in `vm-ranker`, which resolves configuration and applies adjustments before DPP selection. The request explicitly enables computation even though the service parameter alone defaults false. Missing configuration or RPC failure can fall back to local scores; do not assume every route applies identical adjustments. Removed home-mixer parameters have moved to the service, not necessarily disappeared.

Selected public weighted-score defaults (all 17 unchanged from the installed baseline):

| Predicted action | Default weight |
|---|---:|
| Like/favorite | 0.5 |
| Reply | 5.0 |
| Repost | 1.0 |
| Share | 2.0 |
| Share by DM | 5.0 |
| Share by copied link | 20.0 |
| Dwell | 0.05 |
| Quote | 5.0 |
| Follow author | 4.0 |
| Post click | 0.4 |
| Link open | 0.2 |
| Continuous dwell time | 0.004 |
| Not interested | -43.2 |
| Block author | -31.2 |
| Mute author | -58.8 |
| Report | -234.0 |
| Not dwelled | -0.02 |


These multiply predictions, not engagement counts. Different probabilities, units and normalization prevent equivalences such as “one report cancels 468 likes.” Binary dwell, continuous dwell and click-dwell outputs are distinct; do not assume every dwell field measures seconds.

Other relevant defaults: profile click `0.0`, photo expand `0.05`, video open `0.07`, qualified video view `0.0`, continuous click dwell `0.0`. Profile visits can still be useful conversion steps; they are not equivalent to the direct follow coefficient. Bookmarks and show-more appear in the action taxonomy but have no dedicated term in the inspected final weighted formula. No universal media multiplier or link-placement penalty follows.

### Relationships, diversity and eligibility

- Mutual-follow reply boost adds `15.0` to base `5.0` for eligible mutual-follow candidates, excluding replies and reposts in the inspected condition. It is not a 15× boost to every reply. Mutual-follow dwell boost defaults `0.0`.
- Out-of-network factor defaults `0.75`; enabled in-network reply/repost rescoring also uses `0.75`. Eligibility and rescoring are separate stages.
- Author diversity uses `0.25 + 0.75 × 0.5^k` for successive same-author candidates in a score-ordered pool: `1`, `0.625`, `0.4375`, `0.34375`, approaching `0.25`. This is not a daily quota, posting timer or literal score halving each time.
- The DPP diversity stage selects an embedding-diverse subset, preserving selected scores and assigning zero to unselected candidates in the inspected implementation. It does not merely rearrange adjacent posts; zero score does not by itself prove removal in every downstream route.
- The inspected For You filter excludes candidates marked as out-of-network replies/reposts. This does not make replies invisible across X. Self-contained original posts can serve discovery, while replies serve real conversation. Deduplication means thread parts are not independent guaranteed reach opportunities.
- The inspected general age filter and author cold-start eligibility use 48-hour maxima, with additional follower, impression, source/experiment and placement conditions. New retrieval/export machinery separately supports HOME_HOT/HOME_COLD pools and a two-hour cold-pool freshness default; split-checkpoint configuration defaults false. These are different stages, not a universal two-hour or 48-hour post lifespan. No guaranteed boost or impression entitlement follows.

### Changes since the previous saved check

- The optional dwell-regret and gated modes were removed on 18 September. The subsequent refactor removes `ranking_scorer.rs` and moves shared scoring to `xai-value-model`, with service-side defaults in `vm-ranker/params.rs`. The former optional click-probability × click-dwell adjustment is absent from the inspected current formula; direct continuous click-dwell weight remains zero.
- Hot/cold retrieval pools, separate cold-start result limits and retrieval-source tracking were added. The inspected MOE defaults request zero ordinary candidates and 200 cold-start candidates, subject to source enablement and other gates. Candidate counts are retrieval limits, not promised impressions. Cold-pool metadata filtering is not a reason to avoid likes.
- SimClusters age is now configurable, retaining the 48-hour default. Duplicate filtering retains retrieval provenance; this is not a new penalty for similar wording.
- Author diversity, out-of-network adjustments and DPP selection remain in the configured service path. Trace request flags and fallback behavior before interpreting isolated defaults.
- Reply-spam routing thresholds and parsing changed, including use of the full scorer for posts with quoted content. Withheld prompts and unknown live allocation prevent claims about a blanket AI-text penalty, quote-post penalty or safe follower threshold.
- The previous click-dwell training/history work does not establish a direct dwell-padding tactic. Serving/export, ads, visibility and transparency changes do not automatically imply organic-copy advice. Under the Hood legal-takedown reporting is a transparency change.

Historical correction: the old September 9 note overstated consistency with August. Dwell changed `0 → 0.05` and qualified video view `0.05 → 0` in the August 25 snapshot; video-open also changed `0.05 → 0.07` by September 9. These are historical corrections, not newly discovered September deployments. Mutual-follow reply boosting predates this refresh.

## Editorial judgments and hypotheses

Prefer a recognisable subject, an earned payoff and truthful proof. These improve comprehension and may support matching; no inspected code validates a particular hook, six-part rubric or optimal length. Allow meaningful disagreement: predicted negative actions do not mean all controversy is bad. Choose media for its contribution and links for the reader's task. Write useful replies without treating them as a visibility exploit. Vary substance rather than prescribing a magic posting interval. Test performance explanations against actual results using the learning reference.

## Refresh procedure

1. Resolve the official default-branch head; record date and full SHA. If unavailable, retain the saved date and state the limitation rather than calling it current.
2. Diff from this saved revision. Check retrieval/targets, feature preparation, model training/output meanings, scorer wiring/modes, filters, selection/diversity, defaults and cold-start changes. A coefficients-only comparison is insufficient.
3. Separate active defaults, configurable/experimental code, training configuration and unknown production deployment. Trace a changed parameter to its consumer. Distinguish a newly noticed omission from a new change.
4. Update one current evidence header, affected guidance and source links together. Retain concise historical corrections; remove contradictory “latest” statements. Do not turn every code change into writing advice.
5. Reconcile the installed skill and maintained bundle, preserving newer instructions in either copy. Verify the same reviewed contents before calling them synchronized. Do not overwrite a newer installed version with stale repository files. Disclose coverage honestly; do not claim an entire upstream audit from selected files.

## Pinned primary sources

- [Defaults](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/home-mixer/params/param.rs)
- [Scoring](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/xai-value-model/scoring.rs)
- [Cold start](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/home-mixer/scorers/author_cold_start.rs)
- [Out-of-network filter](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/home-mixer/filters/oon_retweet_reply_filter.rs)
- [Favorite holdout](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/home-mixer/filters/fav_holdout_filter.rs)
- [Diversity selection](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/vm-ranker/scoring/dpp_model.rs)
- [Retrieval configuration](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/phoenix/xrex/configs/xrecsys_two_tower.py)
- [SimClusters source](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/home-mixer/sources/simclusters_source.rs)
- [Training configuration](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/phoenix/xrex/configs/xrecsys.py)
- [Model outputs](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/phoenix/xrex/models/recsys_model.py)
- [History features](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/phoenix/xrex/models/recsys_feature_prep.py)
- [Reply spam routing](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/grox/flows/reply_spam/task_filter.py)
- [Publication limitations](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/README.md)
- [Saved-to-current diff](https://github.com/xai-org/x-algorithm/compare/42266f3e2be54d8a3c4d2228aac2e8f8d1c1f034...44d37ebf87f2185b949cd37b710d410c2a77d21f)
- [Service defaults](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/vm-ranker/params.rs)
- [Scoring request](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/home-mixer/scorers/vm_ranker_request.rs)
- [Service wiring](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/vm-ranker/scoring/mod.rs)
- [Local scoring and fallback](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/home-mixer/scorers/vm_ranker.rs)
- [Cold retrieval metadata and freshness](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/phoenix/xrex/data/cold_pool_filter.py)
- [Cold-pool configuration](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/phoenix/xrex/models/recsys_two_tower_model.py)
- [MOE retrieval](https://github.com/xai-org/x-algorithm/blob/44d37ebf87f2185b949cd37b710d410c2a77d21f/home-mixer/sources/phoenix_moe_source.rs)
