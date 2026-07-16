#!/usr/bin/env python3
"""Validate a GitHub social-preview PNG and create a temporary 50% thumbnail."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import tempfile


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1280
EXPECTED_HEIGHT = 640
THUMBNAIL_WIDTH = 640
THUMBNAIL_HEIGHT = 320
DEFAULT_MAX_BYTES = 1_000_000


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    parser.add_argument(
        "--thumbnail",
        type=Path,
        help="Thumbnail output path; defaults to a temporary PNG.",
    )
    return parser.parse_args()


def png_dimensions(path: Path) -> tuple[int, int]:
    try:
        with path.open("rb") as handle:
            header = handle.read(24)
    except OSError as exc:
        raise ValueError(f"cannot read image: {exc}") from exc

    if len(header) < 24 or header[:8] != PNG_SIGNATURE:
        raise ValueError("file is not a valid PNG")
    if header[12:16] != b"IHDR":
        raise ValueError("PNG has no leading IHDR chunk")
    return struct.unpack(">II", header[16:24])


def thumbnail_path(requested: Path | None) -> Path:
    if requested is not None:
        requested.parent.mkdir(parents=True, exist_ok=True)
        return requested
    with tempfile.NamedTemporaryFile(
        prefix="github-social-preview-",
        suffix="-50.png",
        delete=False,
    ) as handle:
        return Path(handle.name)


def create_with_pillow(source: Path, output: Path) -> bool:
    try:
        from PIL import Image
    except ImportError:
        return False

    with Image.open(source) as image:
        resampling = getattr(Image, "Resampling", Image)
        image.resize(
            (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT),
            resampling.LANCZOS,
        ).save(output, format="PNG", optimize=True)
    return True


def run_checked(command: list[str]) -> None:
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "thumbnail command failed"
        raise ValueError(detail)


def create_thumbnail(source: Path, output: Path) -> str:
    if create_with_pillow(source, output):
        return "Pillow"

    magick = shutil.which("magick")
    if magick:
        run_checked(
            [
                magick,
                str(source),
                "-resize",
                f"{THUMBNAIL_WIDTH}x{THUMBNAIL_HEIGHT}!",
                str(output),
            ]
        )
        return "ImageMagick"

    convert = shutil.which("convert")
    if convert:
        run_checked(
            [
                convert,
                str(source),
                "-resize",
                f"{THUMBNAIL_WIDTH}x{THUMBNAIL_HEIGHT}!",
                str(output),
            ]
        )
        return "ImageMagick convert"

    sips = shutil.which("sips")
    if sips:
        run_checked(
            [
                sips,
                "-z",
                str(THUMBNAIL_HEIGHT),
                str(THUMBNAIL_WIDTH),
                str(source),
                "--out",
                str(output),
            ]
        )
        return "sips"

    raise ValueError(
        "cannot create thumbnail: install Pillow or provide ImageMagick or macOS sips"
    )


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    if not args.image.is_file():
        print(f"ERROR: image not found: {args.image}", file=sys.stderr)
        return 2
    if args.max_bytes < 1:
        print("ERROR: --max-bytes must be positive", file=sys.stderr)
        return 2

    try:
        width, height = png_dimensions(args.image)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    size = args.image.stat().st_size
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        errors.append(
            f"dimensions are {width}x{height}; expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )
    if size >= args.max_bytes:
        errors.append(f"file size is {size} bytes; must be below {args.max_bytes}")

    thumbnail = thumbnail_path(args.thumbnail)
    try:
        backend = create_thumbnail(args.image, thumbnail)
        thumb_width, thumb_height = png_dimensions(thumbnail)
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
        backend = "unavailable"
        thumb_width, thumb_height = 0, 0

    if (thumb_width, thumb_height) != (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT):
        errors.append(
            f"thumbnail dimensions are {thumb_width}x{thumb_height}; expected "
            f"{THUMBNAIL_WIDTH}x{THUMBNAIL_HEIGHT}"
        )

    payload = {
        "passed": not errors,
        "image": str(args.image.resolve()),
        "format": "PNG",
        "width": width,
        "height": height,
        "file_size_bytes": size,
        "maximum_bytes_exclusive": args.max_bytes,
        "thumbnail": str(thumbnail.resolve()),
        "thumbnail_width": thumb_width,
        "thumbnail_height": thumb_height,
        "thumbnail_backend": backend,
        "errors": errors,
    }
    print(json.dumps(payload, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
