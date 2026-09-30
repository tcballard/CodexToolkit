# X ranking mechanics

## Evidence status

Checked 30 September 2026 against official default-branch head `77d431aabf409ca1c1eed9bec7e2183f7c914e23` (03:53:42 UTC). Home-mixer defaults header synchronized 29 September, 17:02:52 UTC. Compared with the saved 24 September baseline `44d37ebf87f2185b949cd37b710d410c2a77d21f` across all four subsequent published commits.

Scope: complete changed-path inventory, with targeted static inspection of For You retrieval, scoring defaults and consumers, cold-start eligibility and selection, model configuration, reply-spam routing, and the transparency report. Diversity paths were checked for changes; visibility and enforcement refactors were classified without a full rule-equivalence audit. This is not a full audit of every upstream change. Publication is not proof of deployment date, experiment allocation or exact production predictions. Some dependencies, prompts, weights and anti-abuse internals are unavailable. Other surfaces can behave differently.

Distinguish **published mechanism** (source-backed behavior and defaults), **editorial judgment** (a writing choice), and **hypothesis to test** (an unverified performance explanation). Do not present an inference as an algorithm rule.

## Published mechanisms

Retrieval precedes scoring. Followed-account and discovery sources create candidates, including Phoenix and SimClusters. The inspected Phoenix retrieval configuration uses favorites as positive targets; SimClusters also uses favorite-based representations. A low final like coefficient does not make likes irrelevant to discovery. Semantic and author representations are not a keyword recipe.

Phoenix predicts viewer-specific actions from content and history. Ranking combines probabilities and continuous outputs, then applies additional adjustments and selection. Visibility, age, previously seen/served history, social context and conversation deduplication can affect eligibility. A good hypothetical score does not guarantee an impression.

Scoring now uses shared arithmetic in `xai-value-model/scoring.rs`. Home-mixer computes local weighted scores and cold-start decisions, then requests value-model computation in `vm-ranker`, which resolves configuration and applies adjustments before DPP selection. The request explicitly enables computation even though the service parameter alone defaults false. Missing configuration or RPC failure can fall back to local scores; do not assume every route applies identical adjustments. Removed home-mixer parameters have moved to the service, not necessarily disappeared.

Selected public weighted-score defaults (post-click and not-interested changed since 24 September; other rows below unchanged):

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
| Post click | 0.3 |
| Link open | 0.2 |
| Continuous dwell time | 0.004 |
| Not interested | -47.52 |
| Block author | -31.2 |
| Mute author | -58.8 |
| Report | -234.0 |
| Not dwelled | -0.02 |


These multiply predictions, not engagement counts. Different probabilities, units and normalization prevent equivalences such as “one report cancels 468 likes.” Binary dwell, continuous dwell and click-dwell outputs are distinct; do not assume every dwell field measures seconds.

Other relevant defaults: profile click `0.0`, photo expand `0.05`, video open `0.07`, qualified video view `0.0`, continuous click dwell `0.4` (previously `0.0`). The scorer applies the `click_dwell_time` output directly with this weight; the field name does not establish seconds or a linear reward for extra text. The inspected training configuration defines a binary click-dwell head with threshold `10.0` and a configurable loss weight whose fallback is zero; exact deployed training settings are unknown. Profile visits can still be useful conversion steps; they are not equivalent to the direct follow coefficient. Bookmarks and show-more appear in the action taxonomy but have no dedicated term in the inspected final weighted formula. No universal media multiplier or link-placement penalty follows.

### Relationships, diversity and eligibility

- Mutual-follow reply boost adds `15.0` to base `5.0` for eligible mutual-follow candidates, excluding replies and reposts in the inspected condition. It is not a 15× boost to every reply. Mutual-follow dwell boost defaults `0.0`.
- Out-of-network factor defaults `0.75`; enabled in-network reply/repost rescoring also uses `0.75`. Eligibility and rescoring are separate stages.
- Author diversity uses `0.25 + 0.75 × 0.5^k` for successive same-author candidates in a score-ordered pool: `1`, `0.625`, `0.4375`, `0.34375`, approaching `0.25`. This is not a daily quota, posting timer or literal score halving each time.
- The DPP diversity stage selects an embedding-diverse subset, preserving selected scores and assigning zero to unselected candidates in the inspected implementation. It does not merely rearrange adjacent posts; zero score does not by itself prove removal in every downstream route.
- The inspected For You filter excludes candidates marked as out-of-network replies/reposts. This does not make replies invisible across X. Self-contained original posts can serve discovery, while replies serve real conversation. Deduplication means thread parts are not independent guaranteed reach opportunities.
- The general For You age filter retains a 48-hour maximum. Author cold-start defaults now require a post no older than two hours, an author with at most 50,000 followers, and fewer than 200 Home impressions, plus original-post, viewer/author-arm and pool-position conditions. Thompson sampling is enabled: favorites and Home views inform sampled selection, followed by scoring among the sampled top candidates. This is a gated exploration path, not a guaranteed boost or 200-impression entitlement. Retrieval/export separately supports HOME_HOT/HOME_COLD pools and a two-hour cold-pool freshness default. The combined two-tower configuration now enables split Home checkpoints, while the generic model fallback remains false. These are distinct stages, not a universal post lifespan or optimal posting interval.

### Changes since the previous saved check

- Home-mixer and vm-ranker agree on post-click `0.4 → 0.3`, continuous click-dwell `0.0 → 0.4`, and not-interested `-43.2 → -47.52`. Both local and service consumers map these defaults into the shared formula. Binary dwell stays `0.05`; ordinary continuous dwell stays `0.004`. Distinguish these outputs rather than saying all dwell received a boost.
- Cold-start follower cap changed `1,000 → 50,000`, age `48 hours → 2 hours`, Home-impression threshold `1,000 → 200`, and eligible pool-position ratio `0.85 → 0.97`; Thompson sampling changed false → true. Ordinary Phoenix cold-start retrieval limit changed `0 → 200`. Limits, eligibility, sampled selection and eventual impressions remain different quantities.
- Cold and MOE retrieval candidates now retain their base scores across viewer arms instead of being zeroed by the former author policy. Cold-start lift eligibility still depends on the arm/corpus. The holdout arm can now explore arm-gated retrieval; the control arm excludes it from lifts. Removed policy-zeroing fields were traced through local scoring, the request and shared scorer.
- Seen-post exclusion was added to ordinary Phoenix retrieval but defaults false. Existing downstream history filtering remains separate. This is not evidence of a new universal repost penalty.
- Reply-spam routing thresholds changed to 125,000 in two paths. These are classifier-routing boundaries, not safe follower thresholds or actionable copywriting rules; prompts and live allocation remain unknown.
- Combined Home checkpoint splitting is now enabled in its configuration. An immersive-only retrieval configuration uses multiple engagement targets, including bookmarks and qualified video views. Do not transfer that surface's targets to the For You final weighted formula or claim a new universal bookmark bonus.
- Search lexical-match features were added behind an enable flag whose fallback is false. They do not establish a For You keyword-stuffing tactic. Ads/purchase-value, media-safety and visibility/enforcement changes do not establish organic-copy bonuses or blanket AI-text penalties.
- Under the Hood now has a published page implementation and a new documented URL, `https://x.com/i/jf/under_the_hood`. It reports aggregate account/post labels over a stated period and remains a pilot with eligibility checks. Use an available user-provided report as diagnostic evidence, not proof of what caused one post's reach.

Historical correction: the old September 9 note overstated consistency with August. Dwell changed `0 → 0.05` and qualified video view `0.05 → 0` in the August 25 snapshot; video-open also changed `0.05 → 0.07` by September 9. These are historical corrections, not newly discovered September deployments. Mutual-follow reply boosting predates this refresh.

## Editorial judgments and hypotheses

Prefer a recognisable subject, an earned payoff and truthful proof. These improve comprehension and may support matching; no inspected code validates a particular hook, six-part rubric or optimal length. Allow meaningful disagreement: predicted negative actions do not mean all controversy is bad. A substantive payoff after opening a post is worth testing; the nonzero click-dwell term supports inspecting that hypothesis, not padding, deceptive hooks or mandatory long posts. Keep this separate from source-backed mechanics. Choose media for its contribution and links for the reader's task. Write useful replies without treating them as a visibility exploit. Vary substance rather than prescribing a magic posting interval. Test performance explanations against actual results using the learning reference.

## Refresh procedure

1. Resolve the official default-branch head; record date and full SHA. If unavailable, retain the saved date and state the limitation rather than calling it current.
2. Diff from this saved revision. Check retrieval/targets, feature preparation, model training/output meanings, scorer wiring/modes, filters, selection/diversity, defaults and cold-start changes. A coefficients-only comparison is insufficient.
3. Separate active defaults, configurable/experimental code, training configuration and unknown production deployment. Trace a changed parameter to its consumer. Distinguish a newly noticed omission from a new change.
4. Update one current evidence header, affected guidance and source links together. Retain concise historical corrections; remove contradictory “latest” statements. Do not turn every code change into writing advice.
5. Reconcile the installed skill and maintained bundle, preserving newer instructions in either copy. Verify the same reviewed contents before calling them synchronized. Do not overwrite a newer installed version with stale repository files. Disclose coverage honestly; do not claim an entire upstream audit from selected files.

## Pinned primary sources

- [Defaults](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/home-mixer/params/param.rs)
- [Scoring](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/xai-value-model/scoring.rs)
- [Cold start](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/home-mixer/scorers/author_cold_start.rs)
- [Out-of-network filter](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/home-mixer/filters/oon_retweet_reply_filter.rs)
- [Favorite holdout](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/home-mixer/filters/fav_holdout_filter.rs)
- [Diversity selection](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/vm-ranker/scoring/dpp_model.rs)
- [Retrieval configuration](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/phoenix/xrex/configs/xrecsys_two_tower.py)
- [SimClusters source](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/home-mixer/sources/simclusters_source.rs)
- [Training configuration](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/phoenix/xrex/configs/xrecsys.py)
- [Model outputs](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/phoenix/xrex/models/recsys_model.py)
- [History features](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/phoenix/xrex/models/recsys_feature_prep.py)
- [Reply spam routing](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/grox/flows/reply_spam/task_filter.py)
- [Publication limitations](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/README.md)
- [Saved-to-current diff](https://github.com/xai-org/x-algorithm/compare/44d37ebf87f2185b949cd37b710d410c2a77d21f...77d431aabf409ca1c1eed9bec7e2183f7c914e23)
- [Service defaults](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/vm-ranker/params.rs)
- [Scoring request](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/home-mixer/scorers/vm_ranker_request.rs)
- [Service wiring](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/vm-ranker/scoring/mod.rs)
- [Local scoring and fallback](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/home-mixer/scorers/vm_ranker.rs)
- [Cold retrieval metadata and freshness](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/phoenix/xrex/data/cold_pool_filter.py)
- [Cold-pool configuration](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/phoenix/xrex/models/recsys_two_tower_model.py)
- [MOE retrieval](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/home-mixer/sources/phoenix_moe_source.rs)
- [Transparency report schema](https://github.com/xai-org/x-algorithm/blob/77d431aabf409ca1c1eed9bec7e2183f7c914e23/under-the-hood/jetfuel/routes/_lib/report.ts)
