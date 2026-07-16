#!/usr/bin/env python3
"""Verify mechanical output requirements and emit machine-readable evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def require_pillow():
    try:
        from PIL import Image
    except ImportError:
        raise SystemExit("Pillow is required. Install it in an approved environment, then retry.")
    return Image


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        box = tuple(int(part) for part in value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError("box must be left,top,right,bottom") from error
    if len(box) != 4 or box[0] >= box[2] or box[1] >= box[3]:
        raise argparse.ArgumentTypeError("box must be left,top,right,bottom with positive area")
    return box


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--format")
    parser.add_argument("--max-bytes", type=int)
    parser.add_argument("--require-alpha", action="store_true")
    parser.add_argument("--require-transparent", action="store_true")
    parser.add_argument("--safe-area", type=parse_box)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--source-sha256")
    args = parser.parse_args()

    failures: list[str] = []
    try:
        Image = require_pillow()
        if not args.image.is_file():
            raise ValueError(f"output does not exist or is not a file: {args.image}")
        with Image.open(args.image) as opened:
            opened.load()
            bands = opened.getbands()
            has_alpha = "A" in bands or "transparency" in opened.info
            alpha = opened.convert("RGBA").getchannel("A")
            transparent_count = sum(count for value, count in enumerate(alpha.histogram()) if value < 255)
            alpha_bounds = alpha.getbbox()
            actual_format = opened.format
            width, height = opened.size
        byte_size = args.image.stat().st_size
        if args.width is not None and width != args.width:
            failures.append(f"width is {width}, expected {args.width}")
        if args.height is not None and height != args.height:
            failures.append(f"height is {height}, expected {args.height}")
        if args.format and (actual_format or "").upper() != args.format.upper().replace("JPG", "JPEG"):
            failures.append(f"format is {actual_format}, expected {args.format}")
        if args.max_bytes is not None and byte_size > args.max_bytes:
            failures.append(f"size is {byte_size} bytes, limit is {args.max_bytes}")
        if args.require_alpha and not has_alpha:
            failures.append("alpha channel is required but absent")
        if args.require_transparent and transparent_count == 0:
            failures.append("transparent pixels are required but absent")
        if args.safe_area and alpha_bounds:
            l, t, r, b = args.safe_area
            al, at, ar, ab = alpha_bounds
            if al < l or at < t or ar > r or ab > b:
                failures.append(f"non-transparent bounds {alpha_bounds} escape safe area {args.safe_area}")
        source_hash = None
        if args.source:
            if not args.source.is_file():
                failures.append(f"source does not exist: {args.source}")
            else:
                source_hash = digest(args.source)
                if args.source_sha256 and source_hash != args.source_sha256.lower():
                    failures.append("source SHA-256 changed")
        evidence = {
            "path": str(args.image), "sha256": digest(args.image), "bytes": byte_size,
            "format": actual_format, "width": width, "height": height,
            "has_alpha_channel": has_alpha,
            "has_transparent_pixels": transparent_count > 0,
            "transparent_pixel_count": transparent_count,
            "non_transparent_bounds": list(alpha_bounds) if alpha_bounds else None,
            "safe_area": list(args.safe_area) if args.safe_area else None,
            "source": str(args.source) if args.source else None,
            "source_sha256": source_hash, "automated_pass": not failures,
            "failures": failures,
            "manual_review_required": ["identity fidelity", "sharpness", "crop meaning", "visual balance", "approved text"],
        }
        print(json.dumps(evidence, indent=2, sort_keys=True))
        return 0 if not failures else 1
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
