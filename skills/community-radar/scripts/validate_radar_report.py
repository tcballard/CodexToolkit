#!/usr/bin/env python3
"""Validate the mechanical evidence contract of a Community Radar report."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


HEADINGS = (
    "# Community Radar",
    "## Product context",
    "## Evidence ledger",
    "## Audience profile",
    "## Community map",
    "## Current conversations",
    "## Opportunity ranking",
    "## Engagement strategy",
    "## Risks and unknowns",
    "## Action plan",
    "## Sources",
    "## Checked on",
    "## Not checked",
)
PLACEHOLDERS = ("TODO", "TBD", "REPLACE_ME", "YYYY-MM-DD", "[REQUIRED]", "Lorem ipsum")
EVIDENCE_STATES = ("Confirmed", "Inferred", "Unverified", "Preference")
POSTURES = (
    "reply today", "answer without promoting", "observe first", "write a technical article",
    "improve docs first", "invite feedback", "publish a release", "wait for capability", "do not engage",
)


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    start += len(heading)
    match = re.search(r"^##?\s+", text[start:], re.MULTILINE)
    end = start + match.start() if match else len(text)
    return text[start:end].strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    failures: list[str] = []
    if not args.report.is_file():
        print(json.dumps({"passed": False, "failures": [f"Report not found: {args.report}"]}, indent=2))
        return 2
    text = args.report.read_text(encoding="utf-8")
    missing = [heading for heading in HEADINGS if heading not in text]
    if missing:
        failures.append(f"Missing required headings: {', '.join(missing)}")
    placeholders = [token for token in PLACEHOLDERS if token.casefold() in text.casefold()]
    if placeholders:
        failures.append(f"Unresolved placeholders: {', '.join(placeholders)}")
    ledger = section(text, "## Evidence ledger")
    absent_states = [state for state in EVIDENCE_STATES if state not in ledger]
    if absent_states:
        failures.append(f"Evidence ledger must address: {', '.join(absent_states)}")
    conversations = section(text, "## Current conversations")
    if not re.search(r"https://[^\s)>|]+", conversations):
        failures.append("Current conversations must contain at least one direct HTTPS source.")
    if len(re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", conversations)) < 2:
        failures.append("Current conversations must include publication/activity and observed ISO dates.")
    ranking = section(text, "## Opportunity ranking")
    if not re.search(r"\b(?:100|[1-9]?\d)\s*(?:/\s*100)?\b", ranking):
        failures.append("Opportunity ranking must include a numeric score from 0 to 100.")
    strategy = section(text, "## Engagement strategy").casefold()
    if not any(posture in strategy for posture in POSTURES):
        failures.append("Engagement strategy must use at least one defined posture.")
    sources = section(text, "## Sources")
    if not re.search(r"https://[^\s)>|]+", sources):
        failures.append("Sources must include at least one direct HTTPS URL.")
    checked = section(text, "## Checked on")
    dates = re.findall(r"\b(20\d{2}-\d{2}-\d{2})\b", checked)
    if not dates:
        failures.append("Checked on must include an ISO date.")
    else:
        try:
            date.fromisoformat(dates[0])
        except ValueError:
            failures.append("Checked-on date is invalid.")
    if not section(text, "## Not checked"):
        failures.append("Not checked must explicitly state coverage gaps.")
    result = {"report": str(args.report.resolve()), "failures": failures, "passed": not failures}
    print(json.dumps(result, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
