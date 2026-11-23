"""One Word From Grandma — the single word grandma would text about AI.

Grandma has heard the grandchildren talk about "the AI" and decided it is
called the Googly. She texts it with total confidence — one word, no
explanation. The Googly knows everything, like the Google, only more.
"""

import os
import string
import sys

# The entry: exactly one word, the word grandma would text about AI.
TEXT = "GOOGLY"


def main() -> int:
    text = TEXT
    # Gate: exactly one word — UTF-8, no spaces, no punctuation, not empty.
    if not text or not text.strip():
        print("gate failed: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in text):
        print("gate failed: entry contains whitespace", file=sys.stderr)
        return 1
    if any(ch in string.punctuation for ch in text):
        print("gate failed: entry contains punctuation", file=sys.stderr)
        return 1
    if len(text.split()) != 1:
        print("gate failed: entry is not a single word", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify byte-for-byte.
    with open(out_path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("verify failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(text.encode('utf-8'))} bytes): {text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
