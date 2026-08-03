#!/usr/bin/env python3
"""Validate an AsDecided Agent Citation Scorecard JSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_CHECKS = (
    "direct_answer",
    "extractable_definitions",
    "entity_clarity",
    "original_contribution",
    "claim_evidence_proximity",
    "stable_primary_sources",
    "structured_data_fidelity",
    "retrieval_access",
    "paragraph_extraction_safety",
    "freshness_context",
)
VALID_STATUSES = {"pass", "warn", "fail", "na"}


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_scorecard(data: Any) -> tuple[list[str], list[str], str]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        return ["Root value must be a JSON object."], warnings, "blocked"

    page = data.get("page")
    if not isinstance(page, dict):
        errors.append("page must be an object.")
    else:
        for field in ("title", "checked_on"):
            if not non_empty_string(page.get(field)):
                errors.append(f"page.{field} must be a non-empty string.")

    checks = data.get("checks")
    if not isinstance(checks, dict):
        return errors + ["checks must be an object."], warnings, "blocked"

    unknown = sorted(set(checks) - set(REQUIRED_CHECKS))
    if unknown:
        warnings.append("Unknown checks were ignored: " + ", ".join(unknown))

    for name in REQUIRED_CHECKS:
        item = checks.get(name)
        prefix = f"checks.{name}"
        if not isinstance(item, dict):
            errors.append(f"{prefix} is required and must be an object.")
            continue

        status = item.get("status")
        if status not in VALID_STATUSES:
            errors.append(
                f"{prefix}.status must be one of: "
                + ", ".join(sorted(VALID_STATUSES))
                + "."
            )

        if not non_empty_string(item.get("evidence")):
            errors.append(f"{prefix}.evidence must be a non-empty string.")

        if status == "warn":
            if not non_empty_string(item.get("risk")):
                errors.append(f"{prefix}.risk is required when status is warn.")
            if not non_empty_string(item.get("follow_up")):
                errors.append(f"{prefix}.follow_up is required when status is warn.")
            warnings.append(f"{name}: {item.get('risk', 'warning recorded')}")

        if status == "na" and not non_empty_string(item.get("reason")):
            errors.append(f"{prefix}.reason is required when status is na.")

        if status == "fail":
            errors.append(f"{prefix} failed: {item.get('evidence', 'no evidence supplied')}")

    readiness = "ready" if not errors else "blocked"
    return errors, warnings, readiness


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate an AsDecided Agent Citation Scorecard JSON file."
    )
    parser.add_argument("scorecard", type=Path, help="Path to the scorecard JSON file")
    args = parser.parse_args()

    try:
        data = json.loads(args.scorecard.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.scorecard}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"ERROR: could not read {args.scorecard}: {exc}", file=sys.stderr)
        return 2

    errors, warnings, readiness = validate_scorecard(data)

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    print(f"READINESS: {readiness}")
    return 0 if readiness == "ready" else 1


if __name__ == "__main__":
    raise SystemExit(main())
