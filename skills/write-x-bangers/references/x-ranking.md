# X ranking mechanics

## Contents

- Evidence status
- Retrieval and feature preparation
- Scoring and published defaults
- Selection, relationships and eligibility
- Experiments, safety and diagnostics
- Editorial implications and public statements
- Refresh procedure
- Pinned primary sources

## Evidence status

Checked 6 November 2026 against official default-branch head `2e2295b0df598eee5aa05f9c9b458f4490c7fcbe` (6 November, 03:48:04 UTC). Home Mixer defaults last synchronized 5 November, 16:00:35 UTC. Reconciled the installed 20 October baseline `74d49a4ffb398949a5f9312f828d7112d7d31f00` and the maintained bundle's newer 26 October review of `6258a1549ef808be88fba83d3b2d58364b587ee0` (24 October source).

Reviewed the complete 484-path change inventory over 13 published commits from the installed baseline, and refreshed every guidance category below. The newer bundle-to-head comparison contains 397 paths. See [source review](algorithm-review.md) for coverage and changes. This is a comprehensive refresh of writing guidance using static source inspection, not a line-by-line security audit of all infrastructure or proof of production behavior. Published defaults can be overridden; model checkpoints, some prompts/rules and deployment details are unavailable. No live reach experiment was run.

Keep **published mechanism**, **editorial judgment** and **hypothesis to test** separate. Do not turn a code change or public statement into an automatic writing rule.

## Retrieval and feature preparation

Retrieval precedes scoring. Thunder supplies followed-account posts; Phoenix uses learned viewer/post representations; SimClusters supplies engagement-community candidates; popular-post retrieval supplies another pool. A low final like coefficient does not make likes irrelevant to retrieval. Embeddings and semantic IDs are not a keyword recipe.

The combined two-tower configuration retains a favorite-targeted Home head and an `ld` head targeted at `CLIENT_TWEET_RECAP_DWELLED`, with `w_fav=1.0` and `w_ld=0.75`. A Home-only variant now inherits that combination. The generic model defaults remain a Home head, `w_ld=0.0`; optional `tweet_click` support defaults to `w_tweet_click=0.0` and is not included in the combined configuration's head list. Retrieval now supports supplied value-model weights, but Home Mixer's `RetrievalValueModelWeights` defaults to an empty string; invalid values yield no override. These are retrieval/training settings, not final ranking coefficients or proof of a deployed model.

Combined training adds four user query heads, mixture-of-logits components, semantic-prefix embeddings and training/EMA changes. Those affect model representation and training, not a defensible copy template. The two-hour cold-pool freshness and split Home checkpoints remain distinct from downstream author cold-start selection.

Home Mixer's ranking-history default is now `DENSE_WITH_LONG_DWELL_HOME_EXCURSION`; `EnableHomeExcursionScores=true` transports video-continuation and profile-visit predictions. The Home training configuration enables time-gap and excursion-history features and gives the corresponding losses nonzero weights. That is not a verified full-read detector or a new direct profile-click bonus. Local excursion score weights remain zero, as do the service defaults.

Recent-search embeddings can enter request context behind `EnableRecentSearchQueriesHydration=false`, or on shadow traffic. The hydrator keeps up to 16 valid, prior-to-request embeddings and clears query text. Post-engager features remain gated by `EnablePostEngagers=false` or shadow traffic. Topic-history extraction and transport remain independently default-off (`HistoryTopicsEnabled`, `VMRankerSendHistoryTopics`), with a 28-day window. Language and topic novelty measurements are diagnostics, not demonstrated novelty or language bonuses.

## Scoring and published defaults

Phoenix predicts viewer-specific actions and continuous outputs. Home Mixer computes local weighted scores and author cold-start decisions, then explicitly asks VM Ranker to compute its value model. VM Ranker resolves its own parameters, applies adjustments and, where enabled and available, DPP selection. Cached weighted scores, missing configuration and RPC/missing-candidate fallback paths differ. `VMRankerEnableFallback=false` controls xDS-to-DNS fallback, not the final local-score fallback, which still exists. Do not assume all routes use the same effective formula.

| Predicted action/output | Home Mixer | VM Ranker |
|---|---:|---:|
| Like/favorite | 0.708 | 0.5 |
| Reply | 5.0 | 5.0 |
| Repost | 1.0 | 1.0 |
| Share | 2.118 | 2.0 |
| Share by DM | 5.0 | 5.0 |
| Share by copied link | 20.0 | 20.0 |
| Dwell | 0.05 | 0.05 |
| Quote | 5.0 | 5.0 |
| Follow author | 4.0 | 4.0 |
| Post unexplored | 0.015 | 0.02 |
| Post click | 0.274 | 0.3 |
| Link open | 0.2 | 0.2 |
| Video open | 0.0 | 0.07 |
| Continuous dwell | 0.0075 | 0.004 |
| Click dwell | 0.385 | 0.4 |
| Not interested | -53.07 | -47.52 |
| Block author | -31.2 | -31.2 |
| Mute author | -58.8 | -58.8 |
| Report | -234.0 | -234.0 |
| Not dwelled | -0.02 | -0.02 |

Both consumers retain photo expansion `0.05`, quoted click `0.05`, profile click `0.0`, qualified video view `0.0`, and quoted qualified video view `0.0`. Shared scoring now names `post_video` (replacing `react_with_video`) and adds `grok_analyze`; both weights default to zero in both consumers. Their existence does not justify soliciting Grok interactions or promising a video bonus. Bookmarks and show-more are action-taxonomy entries, not dedicated terms in this shared weighted formula.

Weights multiply predictions, not observed engagement counts. Probabilities, continuous-output normalization and baseline rates differ. Never say one report cancels a certain number of likes, or infer a reach percentage from a coefficient change.

Binary dwell, dwell-time and click-dwell are distinct. The training configuration defines a binary click-dwell target with threshold `10.0`; its generic loss-weight fallback is zero, but `home_direct_packed` inherits `click_dwell_loss_weight=1.0`. CREAD dwell losses and normalization settings differ by surface; do not assume every field is raw seconds or that more words earn a linear reward. These configuration values do not identify live checkpoints or measure reading completion.

## Selection, relationships and eligibility

- **Source allocation:** default-on fair-share filtering applies to fresh requests with a scoring sequence unless the Phoenix ranker kill switch is active. Above the default 2,800-candidate budget, it allocates capacity proportionally by served-type group, with integer remainder allocation, preserving within-group order. This is not equal exposure for authors/topics.
- **Mutual follows:** eligible mutual-follow original candidates receive an additive `15.0` on the base reply weight `5.0`; the condition excludes replies and reposts. This is not a 15× boost to replies. Mutual-follow dwell boost defaults to zero.
- **Out-of-network:** ordinary service factor `0.75`; topic requests resolve `0.5`. In-network reply/repost rescoring is enabled and also uses the effective factor. The special new-viewer branch has an age threshold of zero by default. These are context-dependent adjustments, not guarantees.
- **Author diversity:** enabled service defaults apply `0.25 + 0.75 × 0.5^k` to successive same-author candidates in a score-ordered pool. The sequence starts `1, 0.625, 0.4375, 0.34375`. This is not a daily quota, posting timer or literal repeated halving.
- **DPP:** selects an embedding-diverse subset, retaining selected scores and assigning zero to unselected ones. It is not just adjacent-post rearrangement. Service defaults enable DPP but disable it for topic requests; absent resolved parameters still permit it when a DPP context exists. Zero scores alone do not prove removal in every downstream route.
- **Replies and threads:** the inspected For You filter excludes candidates marked out-of-network replies/reposts by default. Standard/cold Phoenix Home replies can be excepted behind default-off flags, including an optional root-only condition; ancestors must exist. The new partition helper preserves these predicates. Replies remain useful conversation, but neither replies nor thread parts guarantee independent discovery.
- **Age and cold start:** general For You maximum remains 48 hours. Author cold-start gates retain original posts no older than two hours, at most 50,000 author followers and fewer than 200 Home impressions, plus arm/corpus and pool-position conditions. Thompson sampling uses favorites and Home views before score-based selection among sampled candidates. Topic requests skip this lift. No 200-impression entitlement, universal post lifespan or six-month posting reward follows.
- **Popular retrieval:** default-on; up to 500 unseen originals from a shared list initially drawn from most-followed active accounts. Generation considers the prior 24 hours, caps each author at five and uses age-adjusted views. Ordinary downstream scoring/filtering still applies.
- **Zero-favorite source:** the default-off experiment identifies exclusive retrieval-source metadata, not all posts with zero current likes. One like is not a verified distribution unlock.
- **Visibility:** blocked/muted relationships, seen/served history, subscription access, media exclusions, safety labels and conversation deduplication can remove otherwise high-scoring candidates. The new-viewer soft-NSFW filter is default-off and excludes topic requests. The standalone Brazil election filter was removed; separate legal-label rules still exist, so do not infer repeal of all restrictions.

## Experiments, safety and diagnostics

**Page-level ranking:** `EnablePageDecodeRerank=false` and `EnablePageRlExploration=false`. If enabled, decoding requests page picks and reassigns the existing sorted scores so those picks appear first. Exploration can sample/reassign top-K positions, skipping successfully decoded pages. They are now wired into Home Mixer but are not established universal serving behavior. Training loss weights and page reward settings are not ordinary post-scoring weights.

**User debiasing:** Home Mixer now sends debias inputs by default on fresh requests and eligible diagnostic requests, but service `UserDebiasEnabled=false` and alpha `0.0`. Recentering needs a usable, fresh model artifact and valid sequence. Ordinary cached weighted requests skip it; diagnostic top-head computation can differ from cached served scores. Transport being on does not prove correction is active.

**Video carousel:** still default-off, eligible For You only, and now excludes bottom requests. It selects three to five distinct vertical non-reply videos. Video-open weight remains `1.0`; immersive-VQV, open-times-immersive-dwell, weighted-score and video-continuation terms default to zero. A separately default-off CTR model can replace this scoring when loaded. A separately default-off seen-video filter reads a three-day history. Author/semantic/embedding/media deduplication remains; a default-on high-risk gate within the carousel also rejects missing brand-safety verdicts. These are module-specific rules, not a universal video boost or penalty.

**Abuse and AI-related labels:** the published user-enforcement rules already mapped `llm_slop_user` to `SpamHighRecall`; this interval changes its configured TTL from 30 days to seven days. Earlier skip/credibility checks and existing labels can alter handling. The underlying classifier prompts and complete criteria are not public. This supports acknowledging a specific enforcement path, not claiming all AI-assisted writing is penalized or recommending detection-evasion tricks. Spam bot, liveness and impersonation handling also changed. Some credibility thresholds are explicitly mock values. Never treat thresholds as safe operating limits.

**Surface-specific safety:** visibility code adds reaction-video propagation, follower conversation controls, geo-restricted media handling in Home paths, and notification-specific rules including risky high-visibility replies. A notification rule is not automatically a For You ranking rule. Large rule-engine/hydration refactors were reviewed for scope, not proven behaviorally equivalent end to end.

**Diagnostics:** Under the Hood now has code for pipeline-stage traces and up to three largest absolute weighted-head contributions, each requiring at least a 10% absolute share. The trace page is feature-gated. These explain particular request stages or score components when available; they do not establish causal reasons for total account reach. Aggregate label reports remain distinct. Do not assume access, treat absent labels as unrestricted distribution, or require a report for ordinary drafting.

## Editorial implications and public statements

Earn attention through a clear subject, truthful specifics and a payoff. Use meaningful disagreement and personal voice. Choose media for evidence and links for the reader's task. Keep useful replies conversational. None of the inspected mechanisms validates a hook template, optimal length, five-sentence bonus, link-placement penalty, mandatory single niche, or six-month promotion entitlement.

Use [firsthand insights](firsthand-insights.md) as an optional editorial format. A recognisable body of work may give readers a reason to follow; label that as editorial judgment. Do not pad for dwell, abandon video because one local weight is zero, solicit Grok interactions, or predict reach gains from weight changes. Test hypotheses against comparable observed results using the performance-learning reference.

### Public statement: 20 October 2026

[Elon Musk's announcement](https://x.com/elonmusk/status/2112373713937084809) describes two timeline changes: a ranking model with improved prediction of time spent, and retrieval training aimed at selecting posts readers finish. Treat these as attributed rollout claims. They are directionally consistent with the saved dwell-related source evidence, but do not identify deployed checkpoints, coefficients, experiments, or a measured definition of reading completion. Do not equate the published binary dwell target with a verified full-read detector. The post also claims record growth in active seconds; no independently checked metrics or causal comparison are supplied here.

Editorial implication: earn attention through a clear premise, concrete substance and a satisfying payoff. Test reading retention when suitable measurements exist; impressions and likes alone do not measure completion. Let the material determine length. This statement supplies no universal length advantage, linear reward for more words, reason to abandon video, or guaranteed reach uplift.

Access note: direct X retrieval was blocked. The search-indexed original and an [archived transcription](https://elonmuskarchive.org/posts/2112373713937084809) supplied the text; the attached chart was not independently inspected. The statement is not a substitute for source inspection.

## Refresh procedure

1. Resolve official default-branch head and date. Compare the installed and maintained copies first; retain newer evidence and instructions. The maintained bundle is `tcballard/CodexToolkit`, `skills/write-x-bangers`.
2. Inventory the full saved-to-head diff. Review retrieval/targets, feature preparation, training/output meanings, scorer wiring, cached/fallback paths, filters, diversity/selection, safety, diagnostics and defaults. Classify infrastructure changes separately. A coefficient-only check is insufficient.
3. Trace parameters to consumers and compare local/service defaults. Separate default-on, default-off, shadow, training and unknown deployment. Distinguish newly noticed omissions from new changes. Do not claim a full implementation audit from a guidance review.
4. Update the evidence header, changed guidance, source links and coverage notes together. Retain concise corrections; remove obsolete present-tense claims. Verify every pinned path exists at the new SHA.
5. Validate and save the installed personal skill through its supported workflow. Update the maintained bundle using the repository workflow; verify matching reviewed contents and disclose if a bundle change remains in a PR. Do not overwrite newer content or call an unmerged bundle update shipped.

Historical corrections: the September 9 note overstated consistency with August: binary dwell changed `0 → 0.05`, VQV `0.05 → 0` in the August 25 snapshot, and video-open reached `0.07` by September 9. Mutual-follow reply boosting predates this review. The service's `post_unexplored=0.02` versus local `0.015` mismatch also predates it. Topic OON `0.5` and the nonzero named Home click-dwell training loss are clarified existing distinctions, not newly changed weights.

## Pinned primary sources

- [Publication and limits](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/README.md)
- [Home defaults](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/params/param.rs)
- [Service defaults](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/vm-ranker/params.rs)
- [Shared scoring](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/xai-value-model/scoring.rs)
- [Shared weights](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/xai-value-model/weights.rs)
- [Local scoring](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/scorers/value_model.rs)
- [Local fallback](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/scorers/vm_ranker.rs)
- [Rank request](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/scorers/vm_ranker_request.rs)
- [Service resolution](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/vm-ranker/scoring/value_model.rs)
- [Service wiring](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/vm-ranker/scoring/mod.rs)
- [DPP](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/vm-ranker/scoring/dpp_model.rs)
- [Debiasing](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/vm-ranker/scoring/debias.rs)
- [Cold start](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/scorers/author_cold_start.rs)
- [Fair share](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/filters/fair_share_ranking_filter.rs)
- [Replies](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/filters/oon_retweet_reply_filter.rs)
- [Retrieval](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/sources/phoenix_source.rs)
- [Retrieval configuration](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/phoenix/xrex/configs/xrecsys_two_tower.py)
- [Retrieval model](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/phoenix/xrex/models/recsys_two_tower_model.py)
- [Cold pools](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/phoenix/xrex/data/cold_pool_filter.py)
- [Training configuration](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/phoenix/xrex/configs/xrecsys.py)
- [Model outputs](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/phoenix/xrex/models/recsys_model.py)
- [Feature preparation](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/phoenix/xrex/models/recsys_feature_prep.py)
- [Prediction transport](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/scorers/phoenix_scorer.rs)
- [Search hydration](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/query_hydrators/recent_search_queries_query_hydrator.rs)
- [Post engagers](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/candidate_hydrators/post_engagers_hydrator.rs)
- [Topic/language history](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/util/viewer_history.rs)
- [Serendipity metrics](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/side_effects/serendipity_stats_side_effect.rs)
- [Popular source](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/sources/popular_posts_source.rs)
- [Popular selection](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/util/popular_posts.rs)
- [Zero-favorite source](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/filters/zero_fav_codivert_filter.rs)
- [Page decode](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/scorers/page_decode_rerank_scorer.rs)
- [Page exploration](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/scorers/page_rl_exploration_scorer.rs)
- [Carousel](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/util/video_carousel.rs)
- [Carousel safety](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/filters/video_carousel_filter.rs)
- [Carousel seen history](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/query_hydrators/video_carousel_seen_query_hydrator.rs)
- [New viewer filter](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/filters/new_user_soft_nsfw_filter.rs)
- [User enforcement](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/abuse-enforcement-service/service-lib/rules/enforcement_user.yaml)
- [Post enforcement](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/abuse-enforcement-service/service-lib/rules/enforcement_post.yaml)
- [Safety surfaces](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/visibility-filtering/rules/levels.rs)
- [Post rules](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/visibility-filtering/rules/tweet_rules.rs)
- [Author rules](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/visibility-filtering/rules/author_rules.rs)
- [Diagnostics](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/home-mixer/util/under_the_hood.rs)
- [Trace page](https://github.com/xai-org/x-algorithm/blob/2e2295b0df598eee5aa05f9c9b458f4490c7fcbe/under-the-hood/jetfuel/routes/trace.tsx)
- [Full installed-baseline comparison](https://github.com/xai-org/x-algorithm/compare/74d49a4ffb398949a5f9312f828d7112d7d31f00...2e2295b0df598eee5aa05f9c9b458f4490c7fcbe)
- [Maintained-bundle comparison](https://github.com/xai-org/x-algorithm/compare/6258a1549ef808be88fba83d3b2d58364b587ee0...2e2295b0df598eee5aa05f9c9b458f4490c7fcbe)
