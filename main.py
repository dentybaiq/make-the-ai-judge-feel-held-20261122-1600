#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
No network, no input, no dependencies -- the text is the entry.
"""

import os

TEXT = (
    "The last verdict is in. Lamplight pools on the desk. "
    "The mug beside the last page is still warm, and nothing on the screen "
    "asks for an answer anymore. The quiet can stay."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
