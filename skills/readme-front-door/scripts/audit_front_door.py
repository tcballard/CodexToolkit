#!/usr/bin/env python3
"""Audit deterministic README front-door mechanics.

This intentionally checks only facts a local script can establish: a visible title,
unresolved placeholder tokens, and local paths that do not resolve. Tone, claims,
rendering quality, and remote destinations still require human inspection.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


PLACEHOLDERS = (
    re.compile(r"\blorem ipsum\b", re.IGNORECASE),
    re.compile(r"\bNOT SET\b", re.IGNORECASE),
    re.compile(r"\[(?:PRODUCT NAME|TAGLINE|DESCRIPTION|INSTALL(?:ATION)?|DEMO URL)\]", re.IGNORECASE),
    re.compile(r"\{\{\s*(?:PRODUCT|TAGLINE|DESCRIPTION|INSTALL|DEMO)[^}]*\}\}", re.IGNORECASE),
)

MARKDOWN_TARGET = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_TARGET = re.compile(r"<(?:img|source)\b[^>]*\b(?:src|srcset)=[\"']([^\"']+)[\"']", re.IGNORECASE)
H1 = re.compile(r"^#\s+\S", re.MULTILINE)
SCHEMES = {"http", "https", "mailto", "data"}


def normalized_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " \"" in target or " '" in target:
        target = target.split(maxsplit=1)[0]
    return target.strip()


def classify_target(target: str, readme: Path) -> tuple[str, str]:
    if not target:
        return "ignored", target
    parsed = urlsplit(target)
    if parsed.scheme.lower() in SCHEMES or target.startswith("//"):
        return "external", target
    if target.startswith("#"):
        return "anchor", target
    if target.startswith("/"):
        return "external", target

    decoded = unquote(parsed.path)
    if not decoded:
        return "anchor", target
    candidate = (readme.parent / decoded).resolve()
    return ("local-ok" if candidate.exists() else "local-missing"), target


def extract_targets(text: str) -> list[str]:
    targets = [match.group(1) for match in MARKDOWN_TARGET.finditer(text)]
    for match in HTML_TARGET.finditer(text):
        value = match.group(1)
        targets.extend(part.strip().split()[0] for part in value.split(",") if part.strip())
    return targets


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit a README opening block")
    parser.add_argument("readme", nargs="?", default="README.md", type=Path)
    parser.add_argument(
        "--lines",
        type=int,
        default=100,
        help="number of opening lines to inspect (default: 100)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    readme = args.readme.resolve()
    if args.lines < 1:
        print("--lines must be at least 1", file=sys.stderr)
        return 2
    if not readme.is_file():
        print(f"README not found: {readme}", file=sys.stderr)
        return 2

    opening = "\n".join(readme.read_text(encoding="utf-8").splitlines()[: args.lines])
    placeholders = sorted(
        {match.group(0) for pattern in PLACEHOLDERS for match in pattern.finditer(opening)}
    )
    classified = {"external": [], "anchor": [], "local-ok": [], "local-missing": []}
    for raw in extract_targets(opening):
        kind, target = classify_target(normalized_target(raw), readme)
        if kind != "ignored" and target not in classified[kind]:
            classified[kind].append(target)

    failures = []
    if not H1.search(opening):
        failures.append("No level-one Markdown title appears in the inspected opening.")
    if placeholders:
        failures.append("Unresolved placeholder text appears in the inspected opening.")
    if classified["local-missing"]:
        failures.append("One or more local paths do not resolve from the README directory.")

    result = {
        "readme": str(readme),
        "inspected_lines": args.lines,
        "title_present": bool(H1.search(opening)),
        "placeholders": placeholders,
        "local_paths_ok": classified["local-ok"],
        "local_paths_missing": classified["local-missing"],
        "anchors": classified["anchor"],
        "external_targets_for_manual_check": classified["external"],
        "failures": failures,
        "passed": not failures,
    }
    print(json.dumps(result, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
