#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Stdlib only, deterministic, no network. The line is written exactly once,
byte-identical on every run.
"""

import os

LINE = "My smart fridge just locked the ice cream drawer, emailed me a diet plan, and changed its own password."

# The gate allows 1 to 200 characters; keep the entry safely inside it.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS, "line must be 1-200 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
