#!/usr/bin/env python3
"""Measure macOS icon preflight signals without claiming platform compliance."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path


def require_pillow():
    try:
        from PIL import Image, ImageFilter, ImageStat
    except ImportError:
        raise SystemExit("Pillow is required. Install it in an approved environment, then retry.")
    return Image, ImageFilter, ImageStat


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def region_mean(channel, box) -> float:
    values = channel.crop(box).histogram()
    count = sum(values)
    return sum(index * amount for index, amount in enumerate(values)) / count if count else 0.0


def count_outside_box(channel, box, low: int, high: int) -> int:
    width, height = channel.size
    l, t, r, b = box
    count = 0
    pixels = channel.load()
    for y in range(height):
        for x in range(width):
            if l <= x < r and t <= y < b:
                continue
            if low <= pixels[x, y] <= high:
                count += 1
    return count


def inspect(path: Path) -> dict:
    Image, ImageFilter, ImageStat = require_pillow()
    if not path.is_file():
        raise ValueError(f"source does not exist or is not a file: {path}")
    try:
        with Image.open(path) as opened:
            opened.load()
            image_format = opened.format
            source_mode = opened.mode
            source_has_alpha = "A" in opened.getbands() or "transparency" in opened.info
            rgba = opened.convert("RGBA")
    except OSError as error:
        raise ValueError(f"unreadable or corrupt image: {path}: {error}") from error

    width, height = rgba.size
    alpha = rgba.getchannel("A")
    hist = alpha.histogram()
    transparent_count = sum(amount for value, amount in enumerate(hist) if value < 255)
    semi_count = sum(amount for value, amount in enumerate(hist) if 0 < value < 255)
    alpha_bounds = alpha.getbbox()
    solid = alpha.point(lambda value: 255 if value >= 250 else 0)
    solid_bounds = solid.getbbox()
    if alpha_bounds:
        l, t, r, b = alpha_bounds
        clearance = {"left": l, "top": t, "right": width - r, "bottom": height - b}
    else:
        clearance = {"left": width, "top": height, "right": width, "bottom": height}
    clearance_percent = {
        "left": clearance["left"] / width,
        "right": clearance["right"] / width,
        "top": clearance["top"] / height,
        "bottom": clearance["bottom"] / height,
    }

    sample = max(1, round(min(width, height) * 0.08))
    corner_boxes = {
        "top_left": (0, 0, sample, sample),
        "top_right": (width - sample, 0, width, sample),
        "bottom_left": (0, height - sample, sample, height),
        "bottom_right": (width - sample, height - sample, width, height),
    }
    edge_boxes = {
        "top": (width // 2 - sample // 2, 0, width // 2 + math.ceil(sample / 2), sample),
        "bottom": (width // 2 - sample // 2, height - sample, width // 2 + math.ceil(sample / 2), height),
        "left": (0, height // 2 - sample // 2, sample, height // 2 + math.ceil(sample / 2)),
        "right": (width - sample, height // 2 - sample // 2, width, height // 2 + math.ceil(sample / 2)),
    }
    corner_alpha = {name: round(region_mean(alpha, box), 2) for name, box in corner_boxes.items()}
    edge_alpha = {name: round(region_mean(alpha, box), 2) for name, box in edge_boxes.items()}
    mean_corner = sum(corner_alpha.values()) / 4
    mean_edge = sum(edge_alpha.values()) / 4
    bounds_fill = 0.0
    if alpha_bounds:
        bounds_fill = ((alpha_bounds[2] - alpha_bounds[0]) * (alpha_bounds[3] - alpha_bounds[1])) / (width * height)
    likely_baked_mask = bool(
        width == height and bounds_fill > 0.9 and mean_corner < 64 and mean_edge > 220
    )

    halo_pixels = count_outside_box(alpha, solid_bounds, 1, 249) if solid_bounds else 0
    grayscale = rgba.convert("RGB").convert("L")
    reduced = grayscale.resize((min(128, width), min(128, height)), Image.Resampling.LANCZOS)
    edges = reduced.filter(ImageFilter.FIND_EDGES)
    edge_hist = edges.histogram()
    edge_pixels = sum(amount for value, amount in enumerate(edge_hist) if value >= 32)
    detail_density = edge_pixels / (reduced.width * reduced.height)
    stats = ImageStat.Stat(reduced)

    cues: list[str] = []
    if width != height:
        cues.append("source is not square")
    if likely_baked_mask:
        cues.append("likely pre-baked rounded enclosure; visually confirm")
    if min(clearance_percent.values()) < 0.01:
        cues.append("visible alpha bounds approach at least one canvas edge")
    if min(clearance_percent.values()) > 0.15:
        cues.append("transparent margins may make the subject optically small")
    if halo_pixels / (width * height) > 0.002:
        cues.append("semi-transparent pixels outside the near-opaque core may indicate a halo or shadow")
    if detail_density > 0.35:
        cues.append("high edge density may lose clarity at small display sizes")

    return {
        "path": str(path), "sha256": digest(path), "bytes": path.stat().st_size,
        "format": image_format, "mode": source_mode, "width": width, "height": height,
        "square": width == height, "has_alpha_channel": source_has_alpha,
        "has_transparent_pixels": transparent_count > 0,
        "transparent_pixel_count": transparent_count, "semi_transparent_pixel_count": semi_count,
        "alpha_bounds": list(alpha_bounds) if alpha_bounds else None,
        "near_opaque_bounds": list(solid_bounds) if solid_bounds else None,
        "edge_clearance_pixels": clearance, "edge_clearance_fraction": clearance_percent,
        "corner_alpha_mean": corner_alpha, "edge_center_alpha_mean": edge_alpha,
        "bounds_fill_fraction": bounds_fill,
        "likely_prebaked_rounded_mask": likely_baked_mask,
        "semi_transparent_pixels_outside_near_opaque_core": halo_pixels,
        "detail_edge_density": detail_density,
        "small_preview_luminance_mean": stats.mean[0],
        "small_preview_luminance_stddev": stats.stddev[0],
        "review_cues": cues,
        "heuristic_warning": "Cues require full-size and preview-grid visual confirmation; they are not Apple compliance findings.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--output", type=Path)
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
