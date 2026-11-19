"""make.fun news-image-20261119 entry (Python 3.13, standard library only).

Deterministically copies the entry image held in this repository to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR when set, for local runs).
Pass --out <path> to write the copy to a different file instead.
No network access, no randomness: running it twice writes identical bytes.

The image is a 1024x1024 newspaper front page ("WORLD NEWS — THURSDAY
19 NOVEMBER 2026") summing up seven real stories from 19 November 2026.
"""

import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEFAULT_DESTINATION = OUTPUT_DIR / "entry.png"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the news-image-20261119 entry to the output path."
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="destination file (default: $MAKEFUN_OUTPUT_DIR/entry.png)",
    )
    return parser.parse_args(argv)


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    destination = args.out if args.out is not None else DEFAULT_DESTINATION
    if not SOURCE.is_file():
        print(f"error: source image missing: {SOURCE}", file=sys.stderr)
        raise SystemExit(1)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Atomic copy: write to a temporary file in the same directory and
    # rename it into place, so a failed or interrupted run never leaves
    # a partial entry.png behind. Plain byte copy: no re-encoding, no
    # timestamps in the output, so the result is identical on every run
    # and every machine.
    tmp = destination.with_name(destination.name + ".tmp")
    try:
        shutil.copyfile(SOURCE, tmp)
        os.replace(tmp, destination)
    finally:
        if tmp.exists():
            tmp.unlink()
    # Self-check: the output must be byte-identical to the source, so two
    # runs always produce the same file.
    if destination.stat().st_size != SOURCE.stat().st_size:
        print("error: output size differs from source", file=sys.stderr)
        raise SystemExit(1)
    if sha256_of(destination) != sha256_of(SOURCE):
        print("error: output hash differs from source", file=sys.stderr)
        raise SystemExit(1)
    print(
        f"entry.png: {destination.stat().st_size} bytes, "
        f"sha256 {sha256_of(destination)}"
    )


if __name__ == "__main__":
    main()
