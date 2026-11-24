#!/usr/bin/env python3
"""news-23 b51 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import hashlib
import os
import struct
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is empty", file=sys.stderr)
        return 2
    repo = os.path.dirname(os.path.abspath(__file__))
    if os.path.abspath(out_dir) == repo or os.path.abspath(out_dir).startswith(repo + os.sep):
        print("MAKEFUN_OUTPUT_DIR must be outside the repo", file=sys.stderr)
        return 2
    with open(SRC, "rb") as fh:
        data = fh.read()
    if len(data) > 1024 * 1024:
        print("entry.png over 1 MiB", file=sys.stderr)
        return 2
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("bad PNG signature", file=sys.stderr)
        return 2
    width, height, depth, ctype = struct.unpack(">IIBB", data[16:26])
    if (width, height) != (1024, 1024):
        print(f"bad size {width}x{height}", file=sys.stderr)
        return 2
    if depth != 8 or ctype not in (2, 6):
        print(f"bad IHDR depth={depth} colour={ctype}", file=sys.stderr)
        return 2
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        print("bad IEND trailer", file=sys.stderr)
        return 2
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as fh:
        fh.write(data)
    with open(dst, "rb") as fh:
        back = fh.read()
    if back != data:
        print("output differs from source", file=sys.stderr)
        return 2
    print(f"wrote {dst} ({len(data)} bytes, {width}x{height}, sha256 {hashlib.sha256(data).hexdigest()})")
    print(f"source: {SRC} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
