#!/usr/bin/env python3
"""Validate the deterministic structure of a technical naming report."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


REQUIRED_HEADINGS = (
    "# Technical Product Name Check",
    "## Product context",
    "## Checked on",
    "## Normalized variants",
    "## Coverage plan",
    "## Evidence",
    "## Exact collisions",
    "## Near and category collisions",
    "## Registry results",
    "## Search and usability",
    "## Namespace plan",
    "## Risk rating",
    "## Recommendation",
    "## Changes since prior report",
    "## Not checked",
    "## Legal boundary",
)
PLACEHOLDERS = ("REPLACE_ME", "YYYY-MM-DD", "NOT SET", "[REQUIRED]", "TODO", "TBD")
RATINGS = ("LOW", "LOW–MODERATE", "MODERATE", "HIGH", "BLOCKING")
RESULT_STATES = ("Found", "Not found", "Blocked", "Not checked", "Ambiguous")


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    start += len(heading)
    match = re.search(r"^##?\s+", text[start:], re.MULTILINE)
    end = start + match.start() if match else len(text)
    return text[start:end].strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a technical naming report")
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    failures: list[str] = []
    if not args.report.is_file():
        print(json.dumps({"passed": False, "failures": [f"Report not found: {args.report}"]}, indent=2))
        return 2
    text = args.report.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in text]
    if missing:
        failures.append(f"Missing required headings: {', '.join(missing)}")
    found_placeholders = [token for token in PLACEHOLDERS if token in text]
    if found_placeholders:
        failures.append(f"Unresolved placeholders: {', '.join(found_placeholders)}")
    dates = re.findall(r"\b(20\d{2}-\d{2}-\d{2})\b", section(text, "## Checked on"))
    if not dates:
        failures.append("Checked on must contain an ISO date.")
    else:
        try:
            date.fromisoformat(dates[0])
        except ValueError:
            failures.append("Checked-on date is invalid.")
    risk = section(text, "## Risk rating")
    if not any(re.search(rf"\b{re.escape(rating)}\b", risk) for rating in RATINGS):
        failures.append("Risk rating must use the defined rubric.")
    if not re.search(r"https://[^\s)>|]+", section(text, "## Evidence")):
        failures.append("Evidence must contain at least one direct HTTPS source.")
    if not any(state in section(text, "## Evidence") for state in RESULT_STATES):
        failures.append("Evidence must use a defined result state.")
    not_checked = section(text, "## Not checked")
    if not not_checked:
        failures.append("Not checked must be explicit, even when coverage is complete.")
    legal = section(text, "## Legal boundary").casefold()
    if "not legal advice" not in legal or "trademark clearance" not in legal:
        failures.append("Legal boundary must disclaim legal advice and trademark clearance.")
    result = {"report": str(args.report.resolve()), "failures": failures, "passed": not failures}
    print(json.dumps(result, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
