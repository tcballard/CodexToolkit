#!/usr/bin/env python3
"""Validate Premonition's paired BUILDLOG.md and DEVLOG.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ENTRY_RE = re.compile(r"^## Entry (?P<id>.+?)\s+—\s+.+$", re.MULTILINE)
DEV_ENTRY_RE = re.compile(r"^## (?P<id>[A-Za-z0-9.-]+)\s+—\s+.+$", re.MULTILINE)
REQUIRED_METADATA = ("Date", "Phase", "Status", "Model", "Session ID")
REQUIRED_SECTIONS = (
    "Objective",
    "Completed",
    "Decisions and provenance",
    "Artefacts",
    "Verification",
    "Deviations",
    "Risks and missing evidence",
    "Next entry state",
)
FORBIDDEN_HEADINGS = re.compile(
    r"^###\s+(?:Raw\s+)?(?:Prompt|Clipboard(?: contents?)?|Diff|Model output|stdout|stderr)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("buildlog", type=Path, help="Path to BUILDLOG.md")
    parser.add_argument(
        "--previous",
        type=Path,
        help="Previous copy; current file must contain it as an exact prefix",
    )
    parser.add_argument("--devlog", type=Path, help="Path to paired DEVLOG.md")
    parser.add_argument(
        "--previous-devlog",
        type=Path,
        help="Previous DEVLOG copy; current file must contain it as an exact prefix",
    )
    return parser.parse_args()


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_utf8(path: Path, label: str) -> tuple[bytes, str]:
    try:
        raw = path.read_bytes()
        return raw, raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"ERROR: cannot read UTF-8 {label}: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


def check_append(current: bytes, previous_path: Path, label: str, errors: list[str]) -> None:
    try:
        previous = previous_path.read_bytes()
    except OSError as exc:
        print(f"ERROR: cannot read previous {label}: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    if not current.startswith(previous):
        fail(errors, f"current {label} is not an exact append of the previous copy")
    elif len(current) == len(previous):
        fail(errors, f"current {label} contains no appended bytes")


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    current_bytes, text = read_utf8(args.buildlog, "build log")

    if args.previous:
        check_append(current_bytes, args.previous, "build log", errors)

    if not text.startswith("# Premonition Build Log\n"):
        fail(errors, "missing exact '# Premonition Build Log' title")

    entries = list(ENTRY_RE.finditer(text))
    if not entries:
        fail(errors, "no '## Entry <id> — <title>' headings found")
    else:
        ids = [match.group("id").strip() for match in entries]
        duplicates = sorted({entry_id for entry_id in ids if ids.count(entry_id) > 1})
        if duplicates:
            fail(errors, f"duplicate entry IDs: {', '.join(duplicates)}")

        latest = text[entries[-1].start() :]
        for field in REQUIRED_METADATA:
            if not re.search(rf"^\*\*{re.escape(field)}:\*\*\s+\S", latest, re.MULTILINE):
                fail(errors, f"latest entry missing metadata field: {field}")

        date_match = re.search(r"^\*\*Date:\*\*\s+(\S+)", latest, re.MULTILINE)
        if date_match and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_match.group(1)):
            fail(errors, "latest entry Date must use YYYY-MM-DD")

        status_match = re.search(r"^\*\*Status:\*\*\s+(.+)$", latest, re.MULTILINE)
        if status_match and status_match.group(1).strip() not in {"Complete", "Partial", "Blocked"}:
            fail(errors, "latest entry Status must be Complete, Partial or Blocked")

        for section in REQUIRED_SECTIONS:
            if not re.search(rf"^### {re.escape(section)}\s*$", latest, re.MULTILINE):
                fail(errors, f"latest entry missing section: {section}")

        if FORBIDDEN_HEADINGS.search(latest):
            fail(errors, "latest entry contains a forbidden raw-content section")
        if re.search(r"^diff --git |^@@ -\d", latest, re.MULTILINE):
            fail(errors, "latest entry appears to contain a raw diff")
        for pattern in SECRET_PATTERNS:
            if pattern.search(latest):
                fail(errors, "latest entry appears to contain a credential or private key")
                break
        if re.search(r"\b(?:TODO|TBD|FIXME)\b", latest):
            fail(errors, "latest entry contains an unresolved placeholder")

    if args.previous_devlog and not args.devlog:
        fail(errors, "--previous-devlog requires --devlog")

    dev_entries: list[re.Match[str]] = []
    if args.devlog:
        dev_bytes, dev_text = read_utf8(args.devlog, "dev log")
        if args.previous_devlog:
            check_append(dev_bytes, args.previous_devlog, "dev log", errors)
        if not dev_text.startswith("# Premonition Dev Log\n"):
            fail(errors, "missing exact '# Premonition Dev Log' title")
        dev_entries = list(DEV_ENTRY_RE.finditer(dev_text))
        if not dev_entries:
            fail(errors, "no '## <id> — <title>' dev-log headings found")
        else:
            dev_ids = [match.group("id").strip() for match in dev_entries]
            duplicates = sorted({entry_id for entry_id in dev_ids if dev_ids.count(entry_id) > 1})
            if duplicates:
                fail(errors, f"duplicate dev-log entry IDs: {', '.join(duplicates)}")

            build_ids = {match.group("id").strip() for match in entries}
            for index, match in enumerate(dev_entries):
                dev_id = match.group("id").strip()
                end = dev_entries[index + 1].start() if index + 1 < len(dev_entries) else len(dev_text)
                dev_entry = dev_text[match.start() : end]
                if dev_id not in build_ids:
                    fail(errors, f"dev-log entry {dev_id} has no matching BUILDLOG entry")
                source_pattern = rf"^\*\*Source:\*\* `BUILDLOG\.md`, Entry {re.escape(dev_id)}\s*$"
                if not re.search(source_pattern, dev_entry, re.MULTILINE):
                    fail(errors, f"dev-log entry {dev_id} has no exact matching BUILDLOG source line")

            latest_build_id = entries[-1].group("id").strip() if entries else None
            if latest_build_id and latest_build_id not in dev_ids:
                latest_build = text[entries[-1].start() :]
                if "DEVLOG: no material narrative change" not in latest_build:
                    fail(errors, f"dev log has no entry paired with latest BUILDLOG entry {latest_build_id}")

            latest_dev = dev_text[dev_entries[-1].start() :]
            if not re.search(r"^\*\*Date:\*\*\s+\d{4}-\d{2}-\d{2}\s*$", latest_dev, re.MULTILINE):
                fail(errors, "latest dev-log entry missing YYYY-MM-DD Date")
            if re.search(r"^diff --git |^@@ -\d", latest_dev, re.MULTILINE):
                fail(errors, "latest dev-log entry appears to contain a raw diff")
            for pattern in SECRET_PATTERNS:
                if pattern.search(latest_dev):
                    fail(errors, "latest dev-log entry appears to contain a credential or private key")
                    break
            if re.search(r"\b(?:TODO|TBD|FIXME)\b", latest_dev):
                fail(errors, "latest dev-log entry contains an unresolved placeholder")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    result = f"OK: BUILDLOG {len(entries)} entries; latest={entries[-1].group('id').strip()}"
    if args.devlog:
        result += f"; DEVLOG {len(dev_entries)} entries; latest={dev_entries[-1].group('id').strip()}"
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
