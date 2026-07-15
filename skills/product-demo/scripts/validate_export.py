#!/usr/bin/env python3
"""Validate common technical constraints for a rendered product-demo video."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any


def parse_rate(value: str | None) -> float | None:
    try:
        if not value or value == "0/0":
            return None
        return float(Fraction(value))
    except (ValueError, ZeroDivisionError):
        return None


def probe(path: Path) -> dict[str, Any]:
    executable = shutil.which("ffprobe")
    if not executable:
        raise RuntimeError("ffprobe is required but was not found on PATH.")
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
        raise RuntimeError(result.stderr.strip() or "ffprobe could not inspect the export.")
    return json.loads(result.stdout)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path)
    parser.add_argument("--max-duration", type=float)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--expected-fps", type=float)
    parser.add_argument("--fps-tolerance", type=float, default=0.15)
    parser.add_argument("--max-size-mb", type=float)
    parser.add_argument("--require-audio", action="store_true")
    parser.add_argument("--output", type=Path, help="Write the validation report as JSON.")
    args = parser.parse_args()

    if not args.media.is_file():
        print(f"Media file not found: {args.media}", file=sys.stderr)
        raise SystemExit(2)

    try:
        raw = probe(args.media)
    except (RuntimeError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(2) from error

    streams = raw.get("streams", [])
    videos = [stream for stream in streams if stream.get("codec_type") == "video"]
    audios = [stream for stream in streams if stream.get("codec_type") == "audio"]
    video = videos[0] if videos else None
    format_data = raw.get("format", {})
    try:
        duration = float(format_data.get("duration"))
    except (TypeError, ValueError):
        duration = None
    frame_rate = parse_rate(video.get("avg_frame_rate")) if video else None
    size_bytes = args.media.stat().st_size

    checks: list[dict[str, Any]] = []

    def check(name: str, passed: bool, actual: Any, expected: Any) -> None:
        checks.append(
            {"name": name, "passed": passed, "actual": actual, "expected": expected}
        )

    check("video_stream", video is not None, len(videos), ">= 1")
    check("duration_available", duration is not None, duration, "numeric seconds")
    if args.max_duration is not None:
        check(
            "maximum_duration",
            duration is not None and duration <= args.max_duration,
            duration,
            f"<= {args.max_duration}s",
        )
    if args.width is not None:
        check("width", bool(video) and video.get("width") == args.width, video.get("width") if video else None, args.width)
    if args.height is not None:
        check("height", bool(video) and video.get("height") == args.height, video.get("height") if video else None, args.height)
    if args.expected_fps is not None:
        check(
            "frame_rate",
            frame_rate is not None
            and abs(frame_rate - args.expected_fps) <= args.fps_tolerance,
            round(frame_rate, 3) if frame_rate is not None else None,
            f"{args.expected_fps} ± {args.fps_tolerance}",
        )
    if args.max_size_mb is not None:
        max_bytes = int(args.max_size_mb * 1024 * 1024)
        check("maximum_file_size", size_bytes <= max_bytes, size_bytes, f"<= {max_bytes} bytes")
    if args.require_audio:
        check("audio_stream", len(audios) > 0, len(audios), ">= 1")

    passed = all(item["passed"] for item in checks)
    report = {
        "passed": passed,
        "path": str(args.media.resolve()),
        "file_size_bytes": size_bytes,
        "duration_seconds": round(duration, 3) if duration is not None else None,
        "video_codec": video.get("codec_name") if video else None,
        "audio_codecs": [stream.get("codec_name") for stream in audios],
        "checks": checks,
    }
    payload = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
