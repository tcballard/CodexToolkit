#!/usr/bin/env python3
"""Render labeled raw icon previews on contrasting review backgrounds."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


SIZES = (16, 32, 64, 128, 256)
BACKGROUNDS = ("light", "dark", "checker")


def require_pillow():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        raise SystemExit("Pillow is required. Install it in an approved environment, then retry.")
    return Image, ImageDraw, ImageFont


def checker(Image, size: tuple[int, int], unit: int = 12):
    image = Image.new("RGB", size, "#f1f1f1")
    pixels = image.load()
    for y in range(size[1]):
        for x in range(size[0]):
            if (x // unit + y // unit) % 2:
                pixels[x, y] = (190, 190, 190)
    return image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        Image, ImageDraw, ImageFont = require_pillow()
        if not args.source.is_file():
            raise ValueError(f"source does not exist or is not a file: {args.source}")
        if args.source.resolve() == args.output.resolve():
            raise ValueError("refusing to overwrite the source")
        with Image.open(args.source) as opened:
            opened.load()
            source = opened.convert("RGBA")
        cell = 300
        label_height = 28
        grid = Image.new("RGB", (cell * len(BACKGROUNDS), (cell + label_height) * len(SIZES)), "#888888")
        draw = ImageDraw.Draw(grid)
        font = ImageFont.load_default()
        for row, size in enumerate(SIZES):
            preview = source.resize((size, size), Image.Resampling.LANCZOS)
            for column, background_name in enumerate(BACKGROUNDS):
                x0 = column * cell
                y0 = row * (cell + label_height)
                if background_name == "light":
                    field = Image.new("RGB", (cell, cell), "#f5f5f5")
                elif background_name == "dark":
                    field = Image.new("RGB", (cell, cell), "#171717")
                else:
                    field = checker(Image, (cell, cell))
                px = (cell - size) // 2
                py = (cell - size) // 2
                field.paste(preview, (px, py), preview)
                grid.paste(field, (x0, y0))
                draw.rectangle((x0, y0 + cell, x0 + cell, y0 + cell + label_height), fill="#dedede")
                draw.text((x0 + 8, y0 + cell + 8), f"{size}px · {background_name} · raw artwork", fill="#111111", font=font)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        grid.save(args.output, format="PNG", optimize=True)
        evidence = {
            "source": str(args.source), "output": str(args.output),
            "output_width": grid.width, "output_height": grid.height,
            "review_sizes": list(SIZES), "backgrounds": list(BACKGROUNDS),
            "mask_simulation": False,
            "note": "Review grid only; sizes are not asset-catalogue requirements and raw previews do not simulate a platform mask.",
        }
        print(json.dumps(evidence, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
