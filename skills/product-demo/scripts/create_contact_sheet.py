#!/usr/bin/env python3
"""Create a uniformly sampled video contact sheet with ffmpeg."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys


def fail(message: str, code: int = 2) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)


def duration_seconds(path: Path, ffprobe: str) -> float:
    command = [
        ffprobe,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        str(path),
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        fail(result.stderr.strip() or "ffprobe could not determine duration.")
    try:
        return float(json.loads(result.stdout)["format"]["duration"])
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        fail("No usable duration was found in the media file.")
        return 0.0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--rows", type=int, default=3)
    parser.add_argument("--width", type=int, default=360, help="Width of each tile.")
    parser.add_argument("--start", type=float, default=0.0)
    parser.add_argument("--end", type=float, help="End time in seconds.")
    args = parser.parse_args()

    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        fail("ffmpeg and ffprobe are required but were not both found on PATH.")
    if not args.media.is_file():
        fail(f"Media file not found: {args.media}")
    if args.columns < 1 or args.rows < 1 or args.width < 80:
        fail("Columns and rows must be positive; tile width must be at least 80.")

    full_duration = duration_seconds(args.media, ffprobe)
    end = args.end if args.end is not None else full_duration
    if args.start < 0 or end <= args.start or end > full_duration + 0.25:
        fail(f"Invalid sample range {args.start:.3f}–{end:.3f}s for {full_duration:.3f}s media.")

    count = args.columns * args.rows
    span = end - args.start
    interval = max(span / (count + 1), 0.04)
    video_filter = (
        f"fps=1/{interval:.6f},"
        f"scale={args.width}:-2:flags=lanczos,"
        f"tile={args.columns}x{args.rows}:padding=8:margin=8:color=0x111111"
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        ffmpeg,
        "-y",
        "-ss",
        f"{args.start:.6f}",
        "-t",
        f"{span:.6f}",
        "-i",
        str(args.media),
        "-vf",
        video_filter,
        "-frames:v",
        "1",
        "-q:v",
        "2",
        str(args.output),
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        fail(result.stderr.strip() or "ffmpeg could not create the contact sheet.", 1)
    print(args.output.resolve())


if __name__ == "__main__":
    main()
