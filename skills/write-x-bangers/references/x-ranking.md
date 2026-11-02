# X ranking mechanics

## Evidence status

Checked 2 November 2026 against official default-branch head `9106e9f33ee9cc6a92929fc798ae6c566e2841cb` (31 October, 02:25:48 UTC). Home-mixer defaults header synchronized 30 October, 22:59:56 UTC. Compared with the saved 26 October baseline `6258a1549ef808be88fba83d3b2d58364b587ee0` across five subsequent published commits. Earlier findings are retained below as previous updates. Official explanatory claims are attributed separately.

Scope: complete 311-path change inventory from two untruncated Git trees (the compare endpoint returned only 300 files), with targeted static inspection of both scoring-default sets, shared scoring, user-debias and page-reranking gates, retrieval configuration, new-user safety filtering, carousel scoring and affected pipelines. Cold-start, out-of-network reply, fair-share and zero-favorite-source filters were checked for changes. Broader Phoenix performance/training, visibility and enforcement work was classified without a full behavioral-equivalence audit. This is not a full audit of every upstream change. The official explanation says defaults are synchronized to primary production values, but publication does not prove deployment timing, experiment allocation or exact per-request configuration. Some dependencies, prompts, weights and anti-abuse internals are unavailable. Other surfaces can behave differently.

Distinguish **published mechanism** (source-backed behavior and defaults), **editorial judgment** (a writing choice), and **hypothesis to test** (an unverified performance explanation). Do not present an inference as an algorithm rule.

### Official explanation: reading-related updates

The [official repository explanation](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/README.md#notable-updates) now dates improved ranking prediction of time spent to 8 October and retrieval training for posts people finish reading to 13 October. These entries were added after the saved snapshot; they explain earlier work, not a newly discovered late-October deployment. This supplies direct primary-source support for the reading-related claims previously recorded from the 20 October public announcement. It does not identify deployed checkpoints, coefficients, experiment allocation or a measured definition of reading completion. Do not equate the published binary dwell target with a verified full-read detector.

Editorial implication: earn attention through a clear premise, concrete substance and a satisfying payoff. Test reading retention when suitable measurements exist; impressions and likes alone do not measure completion. Let the material determine length. This explanation supplies no universal length advantage, linear reward for more words, reason to abandon video, or guaranteed reach uplift.

## Published mechanisms

Retrieval precedes scoring. Followed-account and discovery sources create candidates, including Phoenix and SimClusters. The combined Phoenix two-tower configuration retains a favorite-targeted Home head and adds an `ld` head targeted at `CLIENT_TWEET_RECAP_DWELLED`. Its configured retrieval mixture uses `w_fav=1.0` and `w_ld=0.75`; the generic model defaults to no `ld` head and `w_ld=0.0`, and inference can override the mixture. These are retrieval-model settings, not final ranking coefficients or evidence that a particular checkpoint is deployed. SimClusters also uses favorite-based representations. A low final like coefficient does not make likes irrelevant to discovery. Semantic and author representations are not a keyword recipe.

Phoenix predicts viewer-specific actions from content and history. Ranking combines probabilities and continuous outputs, then applies additional adjustments and selection. Visibility, age, previously seen/served history, social context and conversation deduplication can affect eligibility. A good hypothetical score does not guarantee an impression.

Scoring uses shared arithmetic in `xai-value-model/scoring.rs`. Home-mixer computes local weighted scores and cold-start decisions, then requests value-model computation in `vm-ranker`, which resolves configuration and applies adjustments before DPP selection. The request explicitly enables computation even though the service parameter alone defaults false. Missing configuration or RPC failure can fall back to local scores; do not assume every route applies identical adjustments. Removed home-mixer parameters have moved to the service, not necessarily disappeared.

Selected published defaults, separated by consumer. Home Mixer uses its values for local scoring and cold-start decisions; configured service recomputation resolves `vm-ranker` parameters independently. A feature-switch configuration can override either set. Do not present either column as the unique effective production formula.

| Predicted action | Home Mixer | VM Ranker |
|---|---:|---:|
| Like/favorite | 0.66 | 0.5 |
| Reply | 5.0 | 5.0 |
| Repost | 1.0 | 1.0 |
| Share | 2.0 | 2.0 |
| Share by DM | 5.0 | 5.0 |
| Share by copied link | 20.0 | 20.0 |
| Dwell | 0.05 | 0.05 |
| Quote | 5.0 | 5.0 |
| Follow author | 4.0 | 4.0 |
| Post unexplored | 0.015 | 0.02 |
| Post click | 0.3 | 0.3 |
| Link open | 0.2 | 0.2 |
| Video open | 0.02 | 0.07 |
| Continuous dwell time | 0.006 | 0.004 |
| Not interested | -52.272 | -47.52 |
| Block author | -31.2 | -31.2 |
| Mute author | -58.8 | -58.8 |
| Report | -234.0 | -234.0 |
| Not dwelled | -0.02 | -0.02 |


These multiply predictions, not engagement counts. Different probabilities, units and normalization prevent equivalences such as “one report cancels 468 likes.” Binary dwell, continuous dwell and click-dwell outputs are distinct; do not assume every dwell field measures seconds.

Other relevant defaults shared by both parameter files: profile click `0.0`, photo expand `0.05`, qualified video view `0.0`, continuous click dwell `0.4`, and the `post_video` term `0.0` (renamed from `react_with_video` in this update). The scorer applies the `click_dwell_time` output directly with this weight; the field name does not establish seconds or a linear reward for extra text. The inspected training configuration defines a binary click-dwell head with threshold `10.0` and a configurable loss weight whose fallback is zero; exact deployed training settings are unknown. Video-continuation, viewer-video-continuation and profile-visit-seconds outputs are present, but Home Mixer wires all three at weight `0.0`, matching the service defaults. Profile visits can still be useful conversion steps; they are not equivalent to the direct follow coefficient. Bookmarks and show-more appear in the action taxonomy but have no dedicated term in the inspected shared weighted formula. Separate page-RL training/decoding code includes other objectives; new Home Mixer page reranking and exploration are both default-off, as detailed below. Do not relabel experimental settings as ordinary For You defaults. No universal media multiplier or link-placement penalty follows.

### Relationships, diversity and eligibility

- Mutual-follow reply boost adds `15.0` to base `5.0` for eligible mutual-follow candidates, excluding replies and reposts in the inspected condition. It is not a 15× boost to every reply. Mutual-follow dwell boost defaults `0.0`.
- Out-of-network factor defaults `0.75`; enabled in-network reply/repost rescoring also uses `0.75`. Eligibility and rescoring are separate stages.
- Author diversity uses `0.25 + 0.75 × 0.5^k` for successive same-author candidates in a score-ordered pool: `1`, `0.625`, `0.4375`, `0.34375`, approaching `0.25`. This is not a daily quota, posting timer or literal score halving each time.
- The DPP diversity stage selects an embedding-diverse subset, preserving selected scores and assigning zero to unselected candidates in the inspected implementation. It does not merely rearrange adjacent posts; zero score does not by itself prove removal in every downstream route. With resolved service parameters, topic requests now skip DPP by default (`TopicDppEnabled=false`); without resolved parameters the enable check still allows DPP. This is request routing, not a hashtag tactic.
- Home Mixer now enables a pre-score fair-share filter by default for fresh requests with a scoring sequence and an available Phoenix ranker. When the pool exceeds the default `PhoenixScoresResultSize=2800`, it retains the same proportion from each served-type group before Phoenix scoring. It preserves candidate-source mix; it does not promise equal exposure to authors or topics, and it creates no posting-format tactic.
- By default, the inspected For You filter excludes candidates marked as out-of-network replies/reposts. A default-off flag can retain standard or cold Phoenix Home-retrieved out-of-network replies after ancestor hydration; a second default-off flag can restrict that exception to replies directly to the conversation root. Out-of-network reposts remain filtered. This does not prove live allocation, make replies universally discoverable or establish a reply tactic. Self-contained original posts can serve discovery, while replies serve real conversation. Deduplication means thread parts are not independent guaranteed reach opportunities.
- The general For You age filter retains a 48-hour maximum. Author cold-start defaults require a post no older than two hours, an author with at most 50,000 followers, and fewer than 200 Home impressions, plus original-post, viewer/author-arm and pool-position conditions. Thompson sampling is enabled: favorites and Home views inform sampled selection, followed by scoring among the sampled top candidates. Corpus and arm eligibility can admit control-corpus cold retrieval into the lift, but this does not relax the same follower, age, impression or original-post gates. Topic requests bypass this author cold-start lift. This is a gated exploration path, not a guaranteed boost or 200-impression entitlement. Retrieval/export separately supports HOME_HOT/HOME_COLD pools and a two-hour cold-pool freshness default. The combined two-tower configuration enables split Home checkpoints, while the generic model fallback remains false. These are distinct stages, not a universal post lifespan or optimal posting interval.
- `PopularPostsSource` remains default-on. It can add up to 500 unseen original posts from a shared list initially built from the most-followed active accounts. The generator considers posts from the previous 24 hours, caps each author at five and orders candidates using age-adjusted views before normal downstream scoring and filtering. This is candidate retrieval, not a promise that raw views, follower count or a particular writing style will rank a post.
- The vertical-video carousel remains default-off and additionally requires an eligible For You request. It selects three to five non-reply vertical videos using separate video-open and immersive-VQV coefficients (defaults `1.0` and `0.0`). Additional open-probability × immersive-dwell and existing-weighted-score terms both default to `0.0`. Selection deduplicates by original author, semantic-ID prefix and available video embeddings. Media IDs and available MD5 hashes also prevent repeated videos within the carousel and videos already present in the selected main-feed page; too few distinct candidates suppress the module. These carousel-specific settings are not ordinary post weights, a universal video boost or a posting-frequency rule.
- A new default-off zero-favorite-source experiment filters candidates retrieved exclusively through `ForYouPhoenixRetrievalZeroFav` according to viewer and author treatment assignment. Its filter tests source metadata, not a candidate's current like count. Do not infer that all zero-like posts are suppressed, that one like unlocks distribution or that this supersedes author cold-start eligibility.

### Changes since the previous saved check: 24–31 October

- All 19 numeric action defaults in the table remain unchanged in both consumers. The shared arithmetic renames `react_with_video` to `post_video`, alongside the action enum and transport fields; its weight remains zero. The name alone does not establish a reward for attaching video.
- VM Ranker adds optional per-viewer probability recentering before recomputing value scores. `UserDebiasEnabled=false` and `UserDebiasAlpha=0.0` are the published defaults. Home Mixer now sends debias inputs by default, but transport does not enable the service adjustment. Missing or stale model artifacts and missing inputs skip it; already-cached weighted scores bypass recentering. This is an experimental adjustment to predictions, not a new engagement-count exchange rate or writing tactic.
- Home Mixer wires page-decode reranking and page-RL exploration after VM Ranker. Both enable flags default false. When enabled, decoded picks can take the highest score slots; exploration can reorder the top-scored pool, skipping when decoded picks are already present. Default-on page logging is separate from these gates. Do not interpret logged training support as proof that page-level optimization is serving every timeline.
- The official README now directly explains the earlier time-spent and reading-completion work. The combined two-tower configuration changes training and model settings, but retains the favorite/dwell retrieval mixture. These changes support studying useful reading attention, without prescribing more words, an ideal length or an expected reach uplift.
- The default-off new-viewer soft-NSFW filter expands its age window from one to seven days and adds a scoring-history-length gate: below 100, or unavailable, with zero disabling that length restriction. The Brazil election filter is removed from the pipeline, consistent with the official 26 October note. These change eligibility in specific contexts, not general copywriting advice.
- The default-off video carousel gains the two zero-weight terms noted above and further safety/embedding work. Ads blending, Phoenix performance/training and visibility changes were also inspected at the change-inventory level; no full behavioral-equivalence or enforcement audit was performed. None supplies a defensible general organic-copy bonus.

### Previous update: 20–24 October

- Existing Home Mixer and VM Ranker scoring coefficients are unchanged. The shared scoring formula, cold-start scorer, out-of-network reply filter, zero-favorite-source experiment and combined favorite/dwell retrieval configuration also have no relevant changes.
- The new default-on fair-share filter applies the source-proportional `2800`-candidate budget described above in both the Phoenix candidate and Phoenix-scores pipelines. It is disabled for cached posts, requests without a scoring sequence and Phoenix-ranker kill-switch traffic. This is pre-score capacity allocation, not a topic, length or media bonus.
- Phoenix retrieval can now accept configurable value-model weights, but the published Home Mixer default is an empty string; invalid settings are rejected. Recent search-query hydration is wired into Phoenix request context behind `EnableRecentSearchQueriesHydration=false`. These are configurable or default-off inputs, not proof that adding keywords or chasing search trends improves reach.
- A new safety filter for newly created viewers can remove out-of-network posts labelled soft NSFW. It is gated off by default and does not apply to topic requests in the inspected code. This is eligibility and safety work, not general copy guidance.
- A shadow Phoenix cluster now has a published `0.3` sampling rate, and carousel, funnel and scoring diagnostics gained logging. Phoenix added training, value-head and candidate-packing work; visibility and enforcement were substantially restructured. These changes do not identify an organic-copy bonus, ideal length, engagement-count equivalence or blanket AI-text penalty.

### Previous update: 17–20 October

- Existing Home Mixer scoring coefficients are unchanged, including favorite `0.66`, video-open `0.02`, continuous dwell `0.006` and not-interested `-52.272`. VM Ranker defaults and shared scoring are unchanged; the two-consumer distinctions above still apply. The combined favorite/dwell retrieval configuration, cold-start and checked reply/zero-favorite-source filters are also unchanged.
- Topic-history extraction can count semantic-ID topic prefixes from positive engagements within a configurable `HistoryTopicsWindowDays=28` window. `HistoryTopicsEnabled=false` gates extraction; `VMRankerSendHistoryTopics=false` separately gates transport in the experiment payload. This supplies experimental inputs, not a documented new topic coefficient, keyword recipe or posting niche requirement.
- A new serendipity side effect measures served-topic diversity and unfamiliar-topic shares, including first-level topic novelty among the top ten positions, against a 28-day engagement-history summary. It requires that summary; unbucketed recording is sampled at `0.05`, while experiment-bucket recording has separate routing. These are measurements, not a novelty boost, exploration quota or evidence that changing subjects earns reach.
- Video-carousel deduplication now checks media IDs and available MD5 hashes against both selected carousel videos and the main-feed page. It remains conditional on the default-off carousel; this is not a general duplicate-text or video penalty.
- Shadow prediction infrastructure can override history aggregation per model cluster. The published mapping includes `Experiment16Fou:DENSE_WITH_LONG_DWELL_HOME_EXCURSION`, with sampled shadow predictions stored and later logged for comparison. This is experiment support, not proof that this history variant serves the main timeline or implements a verified full-read detector. Neither its name nor its presence mandates longer posts.
- Phoenix retrieval sources now call the retrieval client directly rather than the removed home-mixer retrieval-dispatch fallback wrapper; prediction dispatch is also refactored. This is service wiring, distinct from VM Ranker's local-score fallback. Phoenix runtime/performance and visibility/enforcement changes do not establish a defensible new writing tactic; no full enforcement-equivalence audit was performed.

### Previous update: 9–17 October

- Home Mixer changed favorite `0.5 → 0.66`, video-open `0.07 → 0.02`, continuous dwell `0.004 → 0.006`, and not-interested `-47.52 → -52.272`. VM Ranker retains the older defaults for all four. Its `PostUnexploredWeight=0.02` also differs from Home Mixer's `0.015`; that mismatch already existed at the saved baseline and is a newly documented omission, not a new upstream change. Neither set proves an ideal length, a reach percentage or an engagement-count exchange rate.
- Phoenix's combined retrieval configuration adds the dwell-targeted head described above. This broadens the published target mix beyond favorite-only Home retrieval, without proving a deployed checkpoint or an advantage for longer copy.
- React-with-video is wired through model-score transport and shared arithmetic, but defaults to zero in both consumers. Post-engager identity/action features are newly hydrated and sent to Phoenix behind `EnablePostEngagers=false` (or for shadow traffic), excluding the viewer and future-dated events. This is not evidence that engagement groups reliably increase reach.
- Root-only reply gating, zero-favorite-source treatment filtering, topic DPP gating and carousel-specific deduplication/scoring are distinct mechanisms with the limits documented above. Video-exclusion requests now also exclude quotes containing video and replies with displayed video ancestors; this respects request context, not a blanket video penalty.
- Popular-post retrieval remains default-on; numeric cold-start gates, the age limit and the checked reply-spam routing/labelling files are unchanged. Anti-abuse thresholds are still not safe account sizes or writing tactics.
- New reply-model and immersive page-RL work, training/runtime changes, visibility/enforcement restructuring and the Brazil election account-list update do not establish organic-copy bonuses or blanket AI-text penalties. No full enforcement-equivalence audit was performed.

Historical correction: the old September 9 note overstated consistency with August. Dwell changed `0 → 0.05` and qualified video view `0.05 → 0` in the August 25 snapshot; video-open also changed `0.05 → 0.07` by September 9. These are historical corrections, not newly discovered September deployments. Mutual-follow reply boosting predates this refresh.

## Editorial judgments and hypotheses

Prefer a recognisable subject, an earned payoff and truthful proof. These improve comprehension and may support matching; no inspected code validates a particular hook, six-part rubric or optimal length. Allow meaningful disagreement: predicted negative actions do not mean all controversy is bad. A substantive payoff after opening a post remains worth testing; dwell-related retrieval and scoring are reasons to study genuine attention, not to pad, bait clicks or require long posts. The changed Home Mixer coefficients do not justify abandoning video, soliciting likes or predicting a reach uplift. Keep those hypotheses separate from source-backed mechanics. Choose media for its contribution and links for the reader's task. Write useful replies without treating them as a visibility exploit. Vary substance rather than prescribing a magic posting interval. Test performance explanations against actual results using the learning reference.

## Refresh procedure

1. Resolve the official default-branch head; record date and full SHA. If unavailable, retain the saved date and state the limitation rather than calling it current.
2. Diff from this saved revision. Check retrieval/targets, feature preparation, model training/output meanings, scorer wiring/modes, filters, selection/diversity, defaults and cold-start changes. A coefficients-only comparison is insufficient.
3. Separate active defaults, configurable/experimental code, training configuration and unknown production deployment. Trace a changed parameter to its consumer; compare local and service defaults, configuration overrides and fallback paths rather than assuming their values match. Distinguish a newly noticed omission from a new change.
4. Update one current evidence header, affected guidance and source links together. Retain concise historical corrections; remove contradictory “latest” statements. Do not turn every code change into writing advice.
5. Reconcile the installed skill and maintained bundle, preserving newer instructions in either copy. Verify the same reviewed contents before calling them synchronized. Do not overwrite a newer installed version with stale repository files. Disclose coverage honestly; do not claim an entire upstream audit from selected files.

## Pinned primary sources

- [Defaults](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/params/param.rs)
- [Scoring](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/xai-value-model/scoring.rs)
- [Cold start](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/scorers/author_cold_start.rs)
- [Out-of-network filter](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/filters/oon_retweet_reply_filter.rs)
- [Phoenix reply ancestor hydration](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/candidate_hydrators/phoenix_reply_ancestors_hydrator.rs)
- [Favorite holdout](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/filters/fav_holdout_filter.rs)
- [Diversity selection](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/vm-ranker/scoring/dpp_model.rs)
- [Retrieval configuration](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/phoenix/xrex/configs/xrecsys_two_tower.py)
- [SimClusters source](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/sources/simclusters_source.rs)
- [Popular-posts source](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/sources/popular_posts_source.rs)
- [Popular-post selection](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/util/popular_posts.rs)
- [Video-carousel gating](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/util/video_carousel.rs)
- [Semantic-ID source](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/sources/sid_source.rs)
- [Training configuration](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/phoenix/xrex/configs/xrecsys.py)
- [Model outputs](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/phoenix/xrex/models/recsys_model.py)
- [History features](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/phoenix/xrex/models/recsys_feature_prep.py)
- [Reply spam routing](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/grox/flows/reply_spam/task_filter.py)
- [Reply spam labelling](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/grox/flows/reply_spam/task_write.py)
- [Publication limitations](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/README.md)
- [Saved-to-current diff](https://github.com/xai-org/x-algorithm/compare/6258a1549ef808be88fba83d3b2d58364b587ee0...9106e9f33ee9cc6a92929fc798ae6c566e2841cb)
- [Service defaults](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/vm-ranker/params.rs)
- [Service weight resolution](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/vm-ranker/scoring/value_model.rs)
- [Local weight resolution](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/scorers/value_model.rs)
- [Scoring request](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/scorers/vm_ranker_request.rs)
- [Service wiring](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/vm-ranker/scoring/mod.rs)
- [Local scoring and fallback](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/scorers/vm_ranker.rs)
- [Cold retrieval metadata and freshness](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/phoenix/xrex/data/cold_pool_filter.py)
- [Cold-pool configuration](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/phoenix/xrex/models/recsys_two_tower_model.py)
- [MOE retrieval](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/sources/phoenix_moe_source.rs)
- [Transparency report schema](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/under-the-hood/jetfuel/routes/_lib/report.ts)
- [Zero-favorite-source experiment](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/filters/zero_fav_codivert_filter.rs)
- [Post-engager hydration](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/candidate_hydrators/post_engagers_hydrator.rs)
- [Post-engager feature filtering](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/util/post_engagers.rs)
- [Immersive carousel scoring](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/scorers/immersive_video_scorer.rs)
- [Video-exclusion filter](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/filters/video_filter.rs)
- [Ancestor-video exclusion](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/filters/ancestor_video_filter.rs)
- [Immersive page-RL settings](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/phoenix/xrex/models/page_rl.py)
- [Topic-history extraction](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/util/viewer_history.rs)
- [Topic-history hydration and window](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/query_hydrators/scoring_sequence_query_hydrator.rs)
- [Topic-history request transport](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/scorers/vm_ranker_debias_payload.rs)
- [Serendipity measurements](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/side_effects/serendipity_stats_side_effect.rs)
- [Video-media identity hydration](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/candidate_hydrators/video_media_hydrator.rs)
- [Carousel/main-feed selection](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/filters/video_carousel_filter.rs)
- [Shadow aggregation selection](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/util/shadow.rs)
- [Shadow prediction storage and logging](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/side_effects/phoenix_experiments_side_effect.rs)
- [Direct Phoenix retrieval and weight transport](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/sources/phoenix_source.rs)
- [Prediction dispatch](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/util/egress.rs)
- [Fair-share pre-score selection](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/filters/fair_share_ranking_filter.rs)
- [Phoenix candidate pipeline](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/candidate_pipeline/phoenix_candidate_pipeline.rs)
- [Phoenix scores pipeline](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/candidate_pipeline/phoenix_scores_pipeline.rs)
- [Recent-search hydration](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/query_hydrators/recent_search_queries_query_hydrator.rs)
- [Retrieval request and configurable weights](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/util/phoenix_request.rs)
- [New-user soft-NSFW filter](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/filters/new_user_soft_nsfw_filter.rs)
- [User-debias gating and recentering](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/vm-ranker/scoring/debias.rs)
- [Page-decode reranking](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/scorers/page_decode_rerank_scorer.rs)
- [Page-RL exploration](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/home-mixer/scorers/page_rl_exploration_scorer.rs)
- [Action names](https://github.com/xai-org/x-algorithm/blob/9106e9f33ee9cc6a92929fc798ae6c566e2841cb/phoenix/python/common/xai-proto/proto/recsys.proto)
