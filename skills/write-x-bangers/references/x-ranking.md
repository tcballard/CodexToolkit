# X ranking mechanics

Verified 2026-08-15 against `xai-org/x-algorithm` at commit `c65aa179db7bdd61e2c2821eac87f208a105c053`.

Use this as a grounding reference, not a recipe for guaranteed reach. X runs experiments, some production values are configurable, and some prompts and anti-abuse rules are not published.

## What the system does

- Candidate retrieval mixes in-network posts from followed accounts with out-of-network posts selected through Phoenix embeddings and SimClusters.
- Phoenix uses the viewer's recent action history and predicts that viewer's probability of taking many actions on each candidate.
- Ranking combines predicted action probabilities and continuous values; the public weights do not multiply raw engagement counts.
- Visibility filtering is separate from ranking and may drop a post regardless of its score.
- A diversity ranker may trade a little score for less similarity between adjacent recommendations.

The practical consequence is personalisation: there is no universally optimal post. Write a valuable post for a recognisable audience whose prior interests make the promised action plausible.

## Published default signals

Selected defaults from `home-mixer/params/param.rs`:

| Predicted action | Default weight |
|---|---:|
| Like/favorite | 0.5 |
| Reply | 5.0 |
| Repost | 1.0 |
| Share | 2.0 |
| Share by DM | 5.0 |
| Share by copied link | 20.0 |
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

Interpret these only as coefficients on model predictions. A report is not “worth 468 likes”; X explicitly warns that this reading is wrong because base probabilities differ and predictions are viewer-specific.

## Distribution adjustments

- Out-of-network candidates use a default factor of `0.75`. In-network replies and reposts can receive the same rescore.
- Additional posts from the same author decay by `0.5` to a floor of `0.25`, supporting topic and author diversity.
- Pre-scoring removes posts older than 48 hours, duplicates, already-seen or already-served posts, muted topics/keywords, inaccessible posts, and some out-of-network replies/reposts.
- Out-of-network replies and reposts are filtered, while self-contained top-level posts are eligible for broader retrieval.
- New-author/cold-start logic can give limited exposure to qualifying posts, but it is not a writing tactic and should not be presented as one.

## Sound editorial inferences

These are inferences from the system, not promises made by X:

- Specific topic language helps embeddings and clusters find the appropriate audience.
- A self-contained first line improves comprehension for viewers who do not know the author.
- Useful, surprising, or identity-relevant content can create authentic reasons to reply, quote, DM, copy, or follow.
- Proof and precise framing reduce the risk that curiosity becomes disappointment or negative feedback.
- Repetitive bursts are a weak strategy because author and content diversity are explicit system goals.

## Primary sources

- Repository and architecture: https://github.com/xai-org/x-algorithm
- Production-mirrored defaults: https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs
- Score calculation: https://github.com/xai-org/x-algorithm/blob/main/home-mixer/scorers/ranking_scorer.rs
- Verified commit: https://github.com/xai-org/x-algorithm/commit/c65aa179db7bdd61e2c2821eac87f208a105c053
