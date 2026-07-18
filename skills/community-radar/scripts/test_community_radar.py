#!/usr/bin/env python3
"""Forward-test Community Radar's deterministic scoring and report gates."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class CommunityRadarTests(unittest.TestCase):
    def run_script(self, script: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / script), *args],
            capture_output=True, text=True, check=False,
        )

    def test_scoring_orders_and_explains(self) -> None:
        dimensions = {
            "relevance": {"score": 5, "reason": "Exact problem."},
            "freshness": {"score": 5, "reason": "Active today."},
            "audience_match": {"score": 4, "reason": "Target users."},
            "meaningful_engagement": {"score": 4, "reason": "Useful answer."},
            "evidence_strength": {"score": 5, "reason": "Direct source."},
            "competition": {"score": 1, "reason": "One answer."},
            "spam_risk": {"score": 1, "reason": "Disclosure allowed."},
        }
        payload = {"checked_on": "2026-07-18", "opportunities": [{
            "id": "one", "title": "Question", "platform": "Forum",
            "url": "https://example.com/thread", "published_at": "2026-07-17",
            "observed_at": "2026-07-18", "evidence": "Direct question.",
            "inference": "Product may help.", "dimensions": dimensions,
        }]}
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "input.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_script("score_opportunities.py", str(path))
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(output["opportunities"][0]["scoring"]["score"], 86)
        self.assertEqual(output["opportunities"][0]["scoring"]["band"], "strong")
        self.assertIn("reason", output["opportunities"][0]["scoring"]["dimensions"]["spam_risk"])

    def test_scoring_rejects_missing_reason(self) -> None:
        payload = {"checked_on": "2026-07-18", "opportunities": [{
            "id": "bad", "title": "Question", "platform": "Forum",
            "url": "https://example.com/thread", "published_at": "2026-07-17",
            "observed_at": "2026-07-18", "evidence": "Direct.", "inference": "Possible.",
            "dimensions": {name: {"score": 3, "reason": ""} for name in (
                "relevance", "freshness", "audience_match", "meaningful_engagement",
                "evidence_strength", "competition", "spam_risk")},
        }]}
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "input.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_script("score_opportunities.py", str(path))
        self.assertNotEqual(result.returncode, 0)

    def test_report_contract_passes_complete_report(self) -> None:
        report = """# Community Radar
## Product context
Open-source developer tool.
## Evidence ledger
Confirmed: repository. Inferred: audience. Unverified: private groups. Preference: UK.
## Audience profile
Developers because the repository exposes a CLI.
## Community map
Forum — direct fit.
## Current conversations
https://example.com/thread — published 2026-07-17; observed 2026-07-18.
## Opportunity ranking
86/100 strong; direct question and current evidence.
## Engagement strategy
reply today with a technical answer.
## Risks and unknowns
Promotion rules require confirmation.
## Action plan
Today: confirm rules and answer.
## Sources
https://example.com/thread
## Checked on
2026-07-18
## Not checked
Private Discord and Slack communities.
"""
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "report.md"
            path.write_text(report, encoding="utf-8")
            result = self.run_script("validate_radar_report.py", str(path))
        self.assertEqual(result.returncode, 0, result.stdout)


if __name__ == "__main__":
    unittest.main()
