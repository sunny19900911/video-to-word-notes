#!/usr/bin/env python3
"""Extract speech-friendly WAV audio from a video without altering the source."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Input video/audio path")
    parser.add_argument("output", type=Path, help="Output WAV path")
    parser.add_argument("--ffmpeg", help="Explicit ffmpeg executable path")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.input.expanduser().resolve()
    target = args.output.expanduser().resolve()

    if not source.is_file():
        raise SystemExit(f"Input file does not exist: {source}")
    if target.exists() and not args.force:
        raise SystemExit(f"Output exists; pass --force to replace it: {target}")

    ffmpeg = args.ffmpeg or shutil.which("ffmpeg")
    if not ffmpeg:
        try:
            import imageio_ffmpeg

            ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        except (ImportError, RuntimeError, OSError):
            ffmpeg = None
    if not ffmpeg:
        raise SystemExit(
            "ffmpeg was not found. Install it, install imageio-ffmpeg, or pass --ffmpeg PATH."
        )

    target.parent.mkdir(parents=True, exist_ok=True)
    command = [
        ffmpeg,
        "-hide_banner",
        "-loglevel",
        "error",
        "-y" if args.force else "-n",
        "-i",
        str(source),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        "-c:a",
        "pcm_s16le",
        str(target),
    ]
    completed = subprocess.run(command, check=False)
    if completed.returncode != 0 or not target.is_file() or target.stat().st_size == 0:
        if target.exists() and target.stat().st_size == 0:
            target.unlink()
        raise SystemExit(f"ffmpeg failed with exit code {completed.returncode}")

    print(target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
