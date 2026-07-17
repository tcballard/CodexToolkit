#!/usr/bin/env python3
"""Inspect image facts needed for faithful adaptation."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def require_pillow():
    try:
        from PIL import Image, ImageChops, UnidentifiedImageError
    except ImportError:
        raise SystemExit("Pillow is required. Install it in an approved environment, then retry.")
    return Image, ImageChops, UnidentifiedImageError


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inspect(path: Path) -> dict:
    Image, ImageChops, UnidentifiedImageError = require_pillow()
    if not path.is_file():
        raise ValueError(f"source does not exist or is not a file: {path}")
    try:
        with Image.open(path) as image:
            image.load()
            bands = image.getbands()
            has_alpha = "A" in bands or "transparency" in image.info
            rgba = image.convert("RGBA")
            alpha = rgba.getchannel("A")
            alpha_extrema = alpha.getextrema()
            transparent_pixels = sum(count for value, count in enumerate(alpha.histogram()) if value < 255)
            alpha_bounds = alpha.getbbox()
            background = Image.new("RGBA", rgba.size, rgba.getpixel((0, 0)))
            visual_bounds = ImageChops.difference(rgba, background).getbbox()
            return {
                "path": str(path),
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
                "format": image.format,
                "width": image.width,
                "height": image.height,
                "aspect_ratio": image.width / image.height,
                "mode": image.mode,
                "frames": getattr(image, "n_frames", 1),
                "has_alpha_channel": has_alpha,
                "has_transparent_pixels": transparent_pixels > 0,
                "transparent_pixel_count": transparent_pixels,
                "alpha_extrema": list(alpha_extrema),
                "alpha_bounds": list(alpha_bounds) if alpha_bounds else None,
                "visual_bounds_from_corner": list(visual_bounds) if visual_bounds else None,
                "icc_profile_present": bool(image.info.get("icc_profile")),
            }
    except (UnidentifiedImageError, OSError) as error:
        raise ValueError(f"unreadable or corrupt image: {path}: {error}") from error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--output", type=Path, help="Optional JSON evidence path")
    args = parser.parse_args()
    try:
        result = inspect(args.image)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
