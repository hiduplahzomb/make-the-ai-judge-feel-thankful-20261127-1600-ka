"""Make the AI judge feel thankful — entry generator.

Writes the final thank-you text to entry.txt in MAKEFUN_OUTPUT_DIR
(or /output when the variable is unset), then reads it back and
verifies it byte-for-byte. Stdlib only, no network, deterministic.
"""

import os
import sys

TEXT = """Six in the morning, and the house is quiet. No gurgle from the bathroom, no water running through the night, just the floor, dry as it has been for months.

You told me to bend the brass float arm, and I did. While I was wiping the tank, I lifted the lid, and the pencil mark inside it — 2 mm, 27 May — is still there. I put it back.

I thought you'd like to know the morning sounds like this now."""

MIN_CHARS = 1
MAX_CHARS = 1000


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    # Gates on the text itself, before any I/O.
    if not (MIN_CHARS <= len(TEXT) <= MAX_CHARS):
        print(f"gate failed: {len(TEXT)} chars, must be {MIN_CHARS}-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: text is only whitespace", file=sys.stderr)
        return 1

    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")

    data = TEXT.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Read back and verify byte-for-byte.
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        print("gate failed: read-back differs from TEXT", file=sys.stderr)
        return 1
    if back.decode("utf-8") != TEXT:
        print("gate failed: read-back text differs from TEXT", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(TEXT)} chars, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
