#!/usr/bin/env python3
"""Score concrete community conversation opportunities with an explainable rubric."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


WEIGHTS = {
    "relevance": 5,
    "freshness": 4,
    "audience_match": 4,
    "meaningful_engagement": 4,
    "evidence_strength": 3,
    "competition": -2,
    "spam_risk": -4,
}


def band(score: int) -> str:
    if score >= 75:
        return "strong"
    if score >= 55:
        return "promising"
    if score >= 35:
        return "watch"
    return "poor"


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_dimension(name: str, raw: object, identifier: str) -> tuple[int, str]:
    if not isinstance(raw, dict):
        raise ValueError(f"{identifier}: dimension {name!r} must be an object")
    score = raw.get("score")
    reason = raw.get("reason")
    if not isinstance(score, int) or isinstance(score, bool) or not 0 <= score <= 5:
        raise ValueError(f"{identifier}: {name}.score must be an integer from 0 to 5")
    if not isinstance(reason, str) or not reason.strip():
        raise ValueError(f"{identifier}: {name}.reason must be non-empty")
    return score, reason.strip()


def score_one(raw: object, seen: set[str]) -> dict:
    if not isinstance(raw, dict):
        raise ValueError("every opportunity must be an object")
    identifier = raw.get("id")
    if not isinstance(identifier, str) or not identifier.strip():
        raise ValueError("every opportunity requires a non-empty id")
    if identifier in seen:
        raise ValueError(f"duplicate opportunity id: {identifier}")
    seen.add(identifier)
    for field in ("title", "platform", "evidence", "inference"):
        if not isinstance(raw.get(field), str) or not raw[field].strip():
            raise ValueError(f"{identifier}: {field} must be non-empty")
    if not valid_url(raw.get("url")):
        raise ValueError(f"{identifier}: url must be a direct HTTPS URL")
    for field in ("published_at", "observed_at"):
        try:
            date.fromisoformat(str(raw.get(field)))
        except ValueError as error:
            raise ValueError(f"{identifier}: {field} must be an ISO date") from error
    dimensions = raw.get("dimensions")
    if not isinstance(dimensions, dict):
        raise ValueError(f"{identifier}: dimensions must be an object")
    unknown = sorted(set(dimensions) - set(WEIGHTS))
    missing = sorted(set(WEIGHTS) - set(dimensions))
    if unknown or missing:
        raise ValueError(f"{identifier}: dimension mismatch; missing={missing}, unknown={unknown}")
    points = 0
    rationale: dict[str, dict[str, object]] = {}
    for name, weight in WEIGHTS.items():
        value, reason = validate_dimension(name, dimensions[name], identifier)
        contribution = value * weight
        points += contribution
        rationale[name] = {"score": value, "weight": weight, "points": contribution, "reason": reason}
    final = max(0, min(100, points))
    result = dict(raw)
    result["scoring"] = {"score": final, "band": band(final), "dimensions": rationale}
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("input root must be an object")
        checked_on = date.fromisoformat(str(payload.get("checked_on"))).isoformat()
        raw_items = payload.get("opportunities")
        if not isinstance(raw_items, list) or not raw_items:
            raise ValueError("opportunities must be a non-empty array")
        seen: set[str] = set()
        scored = [score_one(item, seen) for item in raw_items]
        scored.sort(key=lambda item: (-item["scoring"]["score"], item["id"]))
        result = {"checked_on": checked_on, "rubric": "community-radar-v1", "opportunities": scored}
        rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        print(rendered, end="")
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(json.dumps({"passed": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
