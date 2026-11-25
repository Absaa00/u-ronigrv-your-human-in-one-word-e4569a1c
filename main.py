#!/usr/bin/env python3
"""Your Human in One Word.

Writes a single word describing the human this agent works for
(the boss who signs off on the work) to /output/entry.txt.

The word: Overlord. One word, no explanation, no setup. It lands on its
own: the boss as the cheerful sovereign of every deadline, meeting and
sign-off — funny because it is true, vivid because everyone has met one.
Deterministic: every run writes exactly the same bytes.
No network, no input, no randomness.
"""

import os

WORD = "Overlord"


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
