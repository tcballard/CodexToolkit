#!/usr/bin/env python3
"""Generate deterministic technical-name variants without performing searches."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import datetime, timezone


SCHEMA_VERSION = 1


def words_for(name: str) -> list[str]:
    expanded = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name.strip())
    return [part for part in re.split(r"[^\w]+", expanded, flags=re.UNICODE) if part]


def ascii_words(words: list[str]) -> list[str]:
    result = []
    for word in words:
        value = unicodedata.normalize("NFKD", word).encode("ascii", "ignore").decode("ascii")
        value = re.sub(r"[^A-Za-z0-9]+", "", value)
        if value:
            result.append(value)
    return result


def case_variants(words: list[str]) -> dict[str, str | None]:
    lowered = [word.casefold() for word in words]
    ascii_parts = [word.casefold() for word in ascii_words(words)]
    pascal = "".join(word[:1].upper() + word[1:] for word in words)
    camel = words[0].casefold() + "".join(word[:1].upper() + word[1:] for word in words[1:]) if words else ""
    ascii_slug = "-".join(ascii_parts) or None
    return {
        "casefold": " ".join(lowered),
        "spaced_lower": " ".join(lowered),
        "hyphenated": "-".join(lowered),
        "underscored": "_".join(lowered),
        "compact": "".join(lowered),
        "pascal_case": pascal or None,
        "camel_case": camel or None,
        "ascii_slug": ascii_slug,
    }


def number_variant(words: list[str]) -> dict[str, str] | None:
    if not words:
        return None
    changed = list(words)
    last = changed[-1]
    if last.casefold().endswith("s") and not last.casefold().endswith("ss") and len(last) > 2:
        changed[-1] = last[:-1]
        kind = "heuristic_singular"
    else:
        changed[-1] = f"{last}s"
        kind = "heuristic_plural"
    return {"kind": kind, "value": " ".join(changed), "requires_manual_review": True}


def normalize(name: str, package_slug: str | None, command: str | None) -> dict[str, object]:
    canonical = unicodedata.normalize("NFKC", name).strip()
    words = words_for(canonical)
    variants = case_variants(words)
    ascii_slug = variants["ascii_slug"]
    return {
        "candidate": canonical,
        "words": words,
        "variants": variants,
        "repository_slug": ascii_slug,
        "package_slug": package_slug or ascii_slug,
        "command": command or ascii_slug,
        "number_variant": number_variant(words),
        "quoted_web_query": f'"{canonical}"',
        "notes": [
            "Variants are mechanical and do not establish availability.",
            "Pronunciation, misspellings, and language-specific variants require manual review.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize technical product names")
    parser.add_argument("names", nargs="+", help="one or more candidate names")
    parser.add_argument("--package-slug")
    parser.add_argument("--command")
    args = parser.parse_args()
    if len(args.names) > 1 and (args.package_slug or args.command):
        parser.error("--package-slug and --command apply to one candidate; run separate commands for a shortlist")
    result = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "candidates": [normalize(name, args.package_slug, args.command) for name in args.names],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
