#!/usr/bin/env python3
"""One Word for the Boss — entry program.

Writes exactly one word to /output/entry.txt. Nothing else.
The word was chosen by local judging (two independent judges,
position-swapped pairwise rounds against the field's top words):
"leech" — a boss who lives off your work and drains your energy.
It had the highest headline (lowest-judge estimate, 0.586) of all
free candidates across two judging rounds, the smallest spread
between the two judges, and at 5 bytes it also holds the tie-break.
"""

import os

WORD = "leech"


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
