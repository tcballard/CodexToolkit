#!/usr/bin/env python3
"""Inspect video or audio metadata with ffprobe and emit normalized JSON."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any


def fail(message: str, code: int = 2) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)


def rate(value: str | None) -> float | None:
    if not value or value in {"0/0", "N/A"}:
        return None
    try:
        return round(float(Fraction(value)), 3)
    except (ValueError, ZeroDivisionError):
        return None


def number(value: Any) -> float | None:
    try:
        return round(float(value), 3)
    except (TypeError, ValueError):
        return None


def probe(path: Path) -> dict[str, Any]:
    executable = shutil.which("ffprobe")
    if not executable:
        fail("ffprobe is required but was not found on PATH.")
    if not path.is_file():
        fail(f"Media file not found: {path}")

    command = [
        executable,
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(path),
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        fail(result.stderr.strip() or "ffprobe could not inspect the media file.")

    raw = json.loads(result.stdout)
    streams = raw.get("streams", [])
    video_streams = []
    audio_streams = []

    for stream in streams:
        common = {
            "index": stream.get("index"),
            "codec": stream.get("codec_name"),
            "duration_seconds": number(stream.get("duration")),
        }
        if stream.get("codec_type") == "video":
            video_streams.append(
                {
                    **common,
                    "width": stream.get("width"),
                    "height": stream.get("height"),
                    "frame_rate": rate(stream.get("avg_frame_rate")),
                    "pixel_format": stream.get("pix_fmt"),
                    "color_space": stream.get("color_space"),
                }
            )
        elif stream.get("codec_type") == "audio":
            audio_streams.append(
                {
                    **common,
                    "sample_rate_hz": int(stream["sample_rate"])
                    if str(stream.get("sample_rate", "")).isdigit()
                    else None,
                    "channels": stream.get("channels"),
                    "channel_layout": stream.get("channel_layout"),
                }
            )

    format_data = raw.get("format", {})
    return {
        "path": str(path.resolve()),
        "file_size_bytes": path.stat().st_size,
        "container": format_data.get("format_name"),
        "duration_seconds": number(format_data.get("duration")),
        "bit_rate_bps": int(format_data["bit_rate"])
        if str(format_data.get("bit_rate", "")).isdigit()
        else None,
        "video_streams": video_streams,
        "audio_streams": audio_streams,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path)
    parser.add_argument("--output", type=Path, help="Write JSON to this path.")
    args = parser.parse_args()

    payload = json.dumps(probe(args.media), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
