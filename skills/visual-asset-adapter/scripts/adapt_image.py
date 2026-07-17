#!/usr/bin/env python3
"""Create a proportional, non-destructive image adaptation with evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


ANCHORS = {
    "center": (0.5, 0.5), "top": (0.5, 0.0), "bottom": (0.5, 1.0),
    "left": (0.0, 0.5), "right": (1.0, 0.5), "top-left": (0.0, 0.0),
    "top-right": (1.0, 0.0), "bottom-left": (0.0, 1.0), "bottom-right": (1.0, 1.0),
}


def require_pillow():
    try:
        from PIL import Image, ImageColor, ImageOps
    except ImportError:
        raise SystemExit("Pillow is required. Install it in an approved environment, then retry.")
    return Image, ImageColor, ImageOps


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def parse_background(value: str, ImageColor):
    if value.lower() == "transparent":
        return (0, 0, 0, 0)
    try:
        color = ImageColor.getcolor(value, "RGBA")
    except ValueError as error:
        raise ValueError(f"invalid background color: {value}") from error
    return color


def save_image(image, output: Path, fmt: str | None, quality: int) -> None:
    selected = (fmt or output.suffix.lstrip(".")).upper()
    selected = {"JPG": "JPEG", "TIF": "TIFF"}.get(selected, selected)
    if not selected:
        raise ValueError("output format is unknown; use a file extension or --format")
    output.parent.mkdir(parents=True, exist_ok=True)
    if selected == "JPEG":
        if image.mode == "RGBA":
            flattened = image.convert("RGB")
        else:
            flattened = image
        flattened.save(output, format=selected, quality=quality, optimize=True)
    elif selected == "WEBP":
        image.save(output, format=selected, quality=quality, method=6)
    elif selected == "PNG":
        image.save(output, format=selected, optimize=True)
    else:
        image.save(output, format=selected)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    parser.add_argument("--fit", choices=("contain", "cover"), default="contain")
    parser.add_argument("--anchor", choices=tuple(ANCHORS), default="center")
    parser.add_argument("--background", default="transparent")
    parser.add_argument("--format")
    parser.add_argument("--quality", type=int, default=92)
    parser.add_argument("--max-bytes", type=int)
    parser.add_argument("--evidence", type=Path)
    args = parser.parse_args()

    try:
        Image, ImageColor, ImageOps = require_pillow()
        if not args.source.is_file():
            raise ValueError(f"source does not exist or is not a file: {args.source}")
        if args.width < 1 or args.height < 1:
            raise ValueError("width and height must be positive")
        if not 1 <= args.quality <= 100:
            raise ValueError("quality must be between 1 and 100")
        if args.source.resolve() == args.output.resolve():
            raise ValueError("refusing to overwrite the source asset")
        before_hash = digest(args.source)
        with Image.open(args.source) as opened:
            opened.load()
            source = opened.convert("RGBA")
        background = parse_background(args.background, ImageColor)
        scale = min(args.width / source.width, args.height / source.height)
        if args.fit == "cover":
            scale = max(args.width / source.width, args.height / source.height)
        scaled = (max(1, round(source.width * scale)), max(1, round(source.height * scale)))
        resized = source.resize(scaled, Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (args.width, args.height), background)
        ax, ay = ANCHORS[args.anchor]
        x = round((args.width - scaled[0]) * ax)
        y = round((args.height - scaled[1]) * ay)
        canvas.alpha_composite(resized, (x, y))
        save_image(canvas, args.output, args.format, args.quality)
        after_hash = digest(args.source)
        if before_hash != after_hash:
            raise ValueError("source changed during adaptation")
        actual_bytes = args.output.stat().st_size
        if args.max_bytes is not None and actual_bytes > args.max_bytes:
            args.output.unlink(missing_ok=True)
            raise ValueError(
                f"output would be {actual_bytes} bytes, exceeding {args.max_bytes}; "
                "choose an explicit format/quality trade-off"
            )
        evidence = {
            "source": str(args.source), "source_sha256": before_hash,
            "output": str(args.output), "output_sha256": digest(args.output),
            "output_bytes": actual_bytes, "canvas": [args.width, args.height],
            "source_size": [source.width, source.height], "scaled_size": list(scaled),
            "fit": args.fit, "anchor": args.anchor, "placement": [x, y],
            "scale": scale, "background": args.background,
            "proportional": True, "source_unchanged": True,
        }
        rendered = json.dumps(evidence, indent=2, sort_keys=True)
        print(rendered)
        if args.evidence:
            args.evidence.parent.mkdir(parents=True, exist_ok=True)
            args.evidence.write_text(rendered + "\n", encoding="utf-8")
        return 0
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
