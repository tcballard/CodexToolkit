# Opportunity scoring

Score only a concrete, directly linked conversation. Community-level fit remains a separate evidence-backed judgment.

## Input dimensions

Each dimension is an integer from `0` to `5` and requires a short explanation.

| Dimension | Meaning | Weight |
|---|---|---:|
| relevance | Directness of the problem/product connection | +5 |
| freshness | Whether participation is timely for this conversation type | +4 |
| audience_match | Evidence that likely users are present | +4 |
| meaningful_engagement | Ability to contribute useful substance | +4 |
| evidence_strength | Quality and completeness of the source evidence | +3 |
| competition | Crowding, duplicate answers, or recent launches | -2 |
| spam_risk | Rule conflict or likelihood of perceived promotion | -4 |

The raw score is:

```text
5R + 4F + 4A + 4E + 3V - 2C - 4S
```

Clamp the result to `0–100`.

## Bands

- `75–100` — strong: act if rules and product readiness permit;
- `55–74` — promising: engage selectively or prepare a useful asset;
- `35–54` — watch: observe, learn, or improve prerequisites;
- `0–34` — poor: do not spend attention now.

The band never overrides a hard rule conflict, inaccessible evidence, or product inability. A score is a prioritization aid, not proof of likely growth.

## Confidence

Set confidence separately:

- `high`: direct current source, visible dates, clear norms, and corroborated audience fit;
- `medium`: direct source with one material unknown;
- `low`: incomplete dates, indirect audience evidence, inaccessible rules, or thin product fit.

## JSON contract

```json
{
  "checked_on": "2026-07-18",
  "opportunities": [
    {
      "id": "thread-1",
      "title": "A real conversation title",
      "platform": "Example forum",
      "url": "https://example.com/thread/1",
      "published_at": "2026-07-17",
      "observed_at": "2026-07-18",
      "evidence": "Direct question asking for an alternative.",
      "inference": "The product may help if capability X is complete.",
      "dimensions": {
        "relevance": {"score": 5, "reason": "Exact problem match."},
        "freshness": {"score": 5, "reason": "Active yesterday."},
        "audience_match": {"score": 4, "reason": "Forum serves the target role."},
        "meaningful_engagement": {"score": 4, "reason": "A technical answer is possible."},
        "evidence_strength": {"score": 5, "reason": "Direct dated source and rules."},
        "competition": {"score": 1, "reason": "One partial answer."},
        "spam_risk": {"score": 2, "reason": "Affiliated links allowed with disclosure."}
      }
    }
  ]
}
```
