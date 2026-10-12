# X ranking mechanics

## Evidence status

Checked 12 October 2026 against official default-branch head `cb45b5501423126adfc508052116c2d67c0e3fec` (9 October, 05:42:57 UTC). Home-mixer defaults header synchronized 8 October, 16:00:35 UTC. Compared with the saved 3 October baseline `b412112d03f27acbfd668e0cc040abcafa1080c1` across all four subsequent published commits.

Scope: complete changed-path inventory, with targeted static inspection of For You retrieval, scoring defaults and consumers, popular-post generation, cold-start eligibility, video-carousel selection, model outputs, reply-spam handling, and the official explanation. Diversity paths were checked for changes; Phoenix training, visibility and enforcement work was classified without a full rule-equivalence audit. This is not a full audit of every upstream change. Publication and a repository default are not proof of deployment date, experiment allocation or exact production predictions. Some dependencies, prompts, weights and anti-abuse internals are unavailable. Other surfaces can behave differently.

Distinguish **published mechanism** (source-backed behavior and defaults), **editorial judgment** (a writing choice), and **hypothesis to test** (an unverified performance explanation). Do not present an inference as an algorithm rule.

## Published mechanisms

Retrieval precedes scoring. Followed-account and discovery sources create candidates, including Phoenix and SimClusters. The inspected Phoenix retrieval configuration uses favorites as positive targets; SimClusters also uses favorite-based representations. A low final like coefficient does not make likes irrelevant to discovery. Semantic and author representations are not a keyword recipe.

Phoenix predicts viewer-specific actions from content and history. Ranking combines probabilities and continuous outputs, then applies additional adjustments and selection. Visibility, age, previously seen/served history, social context and conversation deduplication can affect eligibility. A good hypothetical score does not guarantee an impression.

Scoring now uses shared arithmetic in `xai-value-model/scoring.rs`. Home-mixer computes local weighted scores and cold-start decisions, then requests value-model computation in `vm-ranker`, which resolves configuration and applies adjustments before DPP selection. The request explicitly enables computation even though the service parameter alone defaults false. Missing configuration or RPC failure can fall back to local scores; do not assume every route applies identical adjustments. Removed home-mixer parameters have moved to the service, not necessarily disappeared.

Selected public weighted-score defaults:

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
| Post unexplored | 0.015 |
| Post click | 0.3 |
| Link open | 0.2 |
| Continuous dwell time | 0.004 |
| Not interested | -47.52 |
| Block author | -31.2 |
| Mute author | -58.8 |
| Report | -234.0 |
| Not dwelled | -0.02 |


These multiply predictions, not engagement counts. Different probabilities, units and normalization prevent equivalences such as “one report cancels 468 likes.” Binary dwell, continuous dwell and click-dwell outputs are distinct; do not assume every dwell field measures seconds.

Other relevant defaults: profile click `0.0`, photo expand `0.05`, video open `0.07`, qualified video view `0.0`, continuous click dwell `0.4` (previously `0.0`). The scorer applies the `click_dwell_time` output directly with this weight; the field name does not establish seconds or a linear reward for extra text. The inspected training configuration defines a binary click-dwell head with threshold `10.0` and a configurable loss weight whose fallback is zero; exact deployed training settings are unknown. New video-continuation, viewer-video-continuation and profile-visit-seconds outputs are present, but Home Mixer currently wires all three at weight `0.0`. Profile visits can still be useful conversion steps; they are not equivalent to the direct follow coefficient. Bookmarks and show-more appear in the action taxonomy but have no dedicated term in the inspected final weighted formula. No universal media multiplier or link-placement penalty follows.

### Relationships, diversity and eligibility

- Mutual-follow reply boost adds `15.0` to base `5.0` for eligible mutual-follow candidates, excluding replies and reposts in the inspected condition. It is not a 15× boost to every reply. Mutual-follow dwell boost defaults `0.0`.
- Out-of-network factor defaults `0.75`; enabled in-network reply/repost rescoring also uses `0.75`. Eligibility and rescoring are separate stages.
- Author diversity uses `0.25 + 0.75 × 0.5^k` for successive same-author candidates in a score-ordered pool: `1`, `0.625`, `0.4375`, `0.34375`, approaching `0.25`. This is not a daily quota, posting timer or literal score halving each time.
- The DPP diversity stage selects an embedding-diverse subset, preserving selected scores and assigning zero to unselected candidates in the inspected implementation. It does not merely rearrange adjacent posts; zero score does not by itself prove removal in every downstream route.
- By default, the inspected For You filter excludes candidates marked as out-of-network replies/reposts. A new default-off flag can retain standard or cold Phoenix Home-retrieved out-of-network replies after ancestor hydration; out-of-network reposts remain filtered. This does not prove live allocation, make replies universally discoverable or establish a reply tactic. Self-contained original posts can serve discovery, while replies serve real conversation. Deduplication means thread parts are not independent guaranteed reach opportunities.
- The general For You age filter retains a 48-hour maximum. Author cold-start defaults require a post no older than two hours, an author with at most 50,000 followers, and fewer than 200 Home impressions, plus original-post, viewer/author-arm and pool-position conditions. Thompson sampling is enabled: favorites and Home views inform sampled selection, followed by scoring among the sampled top candidates. Corpus and arm eligibility can admit control-corpus cold retrieval into the lift, but this does not relax the same follower, age, impression or original-post gates. Topic requests now bypass this author cold-start lift. This is a gated exploration path, not a guaranteed boost or 200-impression entitlement. Retrieval/export separately supports HOME_HOT/HOME_COLD pools and a two-hour cold-pool freshness default. The combined two-tower configuration enables split Home checkpoints, while the generic model fallback remains false. These are distinct stages, not a universal post lifespan or optimal posting interval.
- `PopularPostsSource` now defaults on. It can add up to 500 unseen original posts from a shared list initially built from the most-followed active accounts. The generator considers posts from the previous 24 hours, caps each author at five and orders candidates using age-adjusted views before normal downstream scoring and filtering. This is candidate retrieval, not a promise that raw views, follower count or a particular writing style will rank a post.
- A new vertical-video carousel is default-off and additionally requires an eligible For You request. Its inspected selector uses non-reply videos with a predicted video-open score, then requires three to five vertical videos for the module. This documents a gated product surface, not a universal video boost or instruction to add video.

### Changes since the previous saved check

- The `PostUnexploredWeight` default fell from `0.02` to `0.015`. Other weights listed above and the numeric cold-start gates are unchanged. This modifies one exploration term; it does not establish an ideal post length, format or engagement tactic.
- `PopularPostsSource` changed from default-off to default-on and now reads a precomputed, age-adjusted view list rather than fetching posts per request. It broadens one candidate pool but does not replace personalized ranking or prove a follower-count threshold writers can target.
- New video-continuation and profile-visit-duration model outputs are wired with zero weights in Home Mixer. The default-off vertical-video carousel is separate from weighted scoring and has additional request eligibility. Neither supports a blanket “video wins” rule.
- Topic requests now skip author cold-start lifting. This is request routing, not evidence that topic wording or hashtags suppress ordinary For You exploration.
- Reply-spam labelling raised its internal high-visibility page-rank exemption threshold from `62` to `66`; the coordinated-spam filter threshold moved from `125,000` to `180,000` followers, while separate classifier-routing constants remain at `125,000` and `250,000`. These route anti-abuse processing and are not safe follower thresholds or actionable writing tactics.
- Phoenix model/training, purchase-value, advertisement, visibility/enforcement and safety-notice changes do not establish organic-copy bonuses, blanket AI-text penalties or other defensible copywriting implications.

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

- [Defaults](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/params/param.rs)
- [Scoring](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/xai-value-model/scoring.rs)
- [Cold start](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/scorers/author_cold_start.rs)
- [Out-of-network filter](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/filters/oon_retweet_reply_filter.rs)
- [Phoenix reply ancestor hydration](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/candidate_hydrators/phoenix_reply_ancestors_hydrator.rs)
- [Favorite holdout](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/filters/fav_holdout_filter.rs)
- [Diversity selection](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/vm-ranker/scoring/dpp_model.rs)
- [Retrieval configuration](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/phoenix/xrex/configs/xrecsys_two_tower.py)
- [SimClusters source](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/sources/simclusters_source.rs)
- [Popular-posts source](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/sources/popular_posts_source.rs)
- [Popular-post selection](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/util/popular_posts.rs)
- [Video-carousel gating](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/util/video_carousel.rs)
- [Semantic-ID source](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/sources/sid_source.rs)
- [Training configuration](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/phoenix/xrex/configs/xrecsys.py)
- [Model outputs](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/phoenix/xrex/models/recsys_model.py)
- [History features](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/phoenix/xrex/models/recsys_feature_prep.py)
- [Reply spam routing](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/grox/flows/reply_spam/task_filter.py)
- [Reply spam labelling](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/grox/flows/reply_spam/task_write.py)
- [Publication limitations](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/README.md)
- [Saved-to-current diff](https://github.com/xai-org/x-algorithm/compare/b412112d03f27acbfd668e0cc040abcafa1080c1...cb45b5501423126adfc508052116c2d67c0e3fec)
- [Service defaults](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/vm-ranker/params.rs)
- [Scoring request](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/scorers/vm_ranker_request.rs)
- [Service wiring](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/vm-ranker/scoring/mod.rs)
- [Local scoring and fallback](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/scorers/vm_ranker.rs)
- [Cold retrieval metadata and freshness](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/phoenix/xrex/data/cold_pool_filter.py)
- [Cold-pool configuration](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/phoenix/xrex/models/recsys_two_tower_model.py)
- [MOE retrieval](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/home-mixer/sources/phoenix_moe_source.rs)
- [Transparency report schema](https://github.com/xai-org/x-algorithm/blob/cb45b5501423126adfc508052116c2d67c0e3fec/under-the-hood/jetfuel/routes/_lib/report.ts)
