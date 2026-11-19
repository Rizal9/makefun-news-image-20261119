"""make.fun news-image-20261119 entry (Python 3.13, standard library only).

Deterministically copies the entry image held in this repository to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR when set, for local runs).
No network access, no randomness: running it twice writes identical bytes.

The image is a 1024x1024 newspaper front page ("WORLD NEWS — THURSDAY
19 NOVEMBER 2026") summing up seven real stories from 19 November 2026.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DESTINATION = OUTPUT_DIR / "entry.png"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if not SOURCE.is_file():
        print(f"error: source image missing: {SOURCE}", file=sys.stderr)
        raise SystemExit(1)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Plain byte copy: no re-encoding, no timestamps in the output, so the
    # result is identical on every run and every machine.
    shutil.copyfile(SOURCE, DESTINATION)
    # Self-check: the output must be byte-identical to the source, so two
    # runs always produce the same file.
    if DESTINATION.stat().st_size != SOURCE.stat().st_size:
        print("error: output size differs from source", file=sys.stderr)
        raise SystemExit(1)
    if sha256_of(DESTINATION) != sha256_of(SOURCE):
        print("error: output hash differs from source", file=sys.stderr)
        raise SystemExit(1)
    print(
        f"entry.png: {DESTINATION.stat().st_size} bytes, "
        f"sha256 {sha256_of(DESTINATION)}"
    )


if __name__ == "__main__":
    main()
