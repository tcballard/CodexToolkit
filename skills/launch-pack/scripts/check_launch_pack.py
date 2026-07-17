#!/usr/bin/env python3
"""Validate the structure and unresolved state of a Launch Pack workspace."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CORE_FILES = (
    "LAUNCH_BRIEF.md",
    "CLAIMS_LEDGER.md",
    "ASSET_INVENTORY.md",
    "CHANNEL_MATRIX.md",
    "RELEASE_CHECKLIST.md",
    "HANDOFF.md",
)
UNRESOLVED_MARKERS = re.compile(
    r"\b(?:TODO|TBD|FIXME|NOT SET|PENDING EVIDENCE)\b", re.IGNORECASE
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
)
UNREADY_CELLS = {
    "blocked",
    "draft",
    "fail",
    "missing",
    "pending",
    "unverified",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", type=Path, help="Launch Pack working directory")
    parser.add_argument(
        "--final",
        action="store_true",
        help="Require a complete pack with no unresolved markers or unready table states",
    )
    return parser.parse_args()


def read_utf8(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        errors.append(f"{path.name}: cannot read UTF-8 content: {exc}")
        return ""


def table_cells(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def table_rows(text: str) -> list[list[str]]:
    return [
        cells
        for line in text.splitlines()
        if (cells := table_cells(line)) and not is_separator_row(cells)
    ]


def check_claims(text: str, final: bool, errors: list[str]) -> None:
    rows = table_rows(text)
    if not rows:
        errors.append("CLAIMS_LEDGER.md: no Markdown table found")
        return
    header = [cell.casefold() for cell in rows[0]]
    required = {"id", "claim", "evidence", "status"}
    if not required.issubset(header):
        errors.append("CLAIMS_LEDGER.md: table must include ID, Claim, Evidence, and Status")
        return
    status_index = header.index("status")
    data = rows[1:]
    if not data:
        errors.append("CLAIMS_LEDGER.md: at least one claim row is required")
        return
    allowed = {"verified", "qualified", "blocked", "removed"}
    for index, row in enumerate(data, start=1):
        if len(row) <= status_index:
            errors.append(f"CLAIMS_LEDGER.md: claim row {index} has no Status cell")
            continue
        status = row[status_index].casefold()
        if status not in allowed:
            errors.append(f"CLAIMS_LEDGER.md: claim row {index} has invalid status '{row[status_index]}'")
        elif final and status == "blocked":
            errors.append(f"CLAIMS_LEDGER.md: claim row {index} remains Blocked")


def collect_versions(documents: dict[str, str]) -> set[str]:
    versions: set[str] = set()
    pattern = re.compile(r"(?im)^-\s*Version:\s*(.+?)\s*$")
    for text in documents.values():
        for match in pattern.finditer(text):
            value = match.group(1).strip()
            if value and not UNRESOLVED_MARKERS.search(value):
                versions.add(value)
    return versions


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    if not args.pack.is_dir():
        print(f"ERROR: launch pack directory not found: {args.pack}", file=sys.stderr)
        return 2

    documents: dict[str, str] = {}
    for name in CORE_FILES:
        path = args.pack / name
        if not path.is_file():
            errors.append(f"missing required file: {name}")
            continue
        documents[name] = read_utf8(path, errors)

    for name, text in documents.items():
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{name}: possible credential or private key detected")
                break
        if args.final and UNRESOLVED_MARKERS.search(text):
            errors.append(f"{name}: contains unresolved placeholder text")
        if args.final:
            for cells in table_rows(text)[1:]:
                for cell in cells:
                    if cell.casefold() in UNREADY_CELLS:
                        errors.append(f"{name}: contains unready table state '{cell}'")
                        break

    claims = documents.get("CLAIMS_LEDGER.md")
    if claims is not None:
        check_claims(claims, args.final, errors)

    versions = collect_versions(documents)
    if len(versions) > 1:
        errors.append(f"inconsistent Version fields: {', '.join(sorted(versions))}")
    elif args.final and not versions:
        errors.append("no resolved Version field found")

    if errors:
        for error in dict.fromkeys(errors):
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    state = "final" if args.final else "structural"
    version = next(iter(versions), "not resolved")
    print(
        f"OK: {state} Launch Pack validation passed; "
        f"files={len(documents)}/{len(CORE_FILES)}; version={version}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
