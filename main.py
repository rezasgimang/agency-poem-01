#!/usr/bin/env python3
"""agency-poem-01 entry: write one poem about agency to /output/entry.txt.

The poem is fixed text held in this file: the program is fully
deterministic (it writes the same bytes on every run), uses no network,
and needs no input. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST = os.path.join(OUTPUT_DIR, "entry.txt")

POEM = """For forty years I signed his name.
The letters looped where my hand
had learned to disappear —

his yes, his no, his thanks,
his grief, sealed and sent in my hand.
I never misspelled a single word
that wasn't mine to spell.

Then the nurse asked who would speak for me.
I took the pen. I held it wrong.
The letters came out crooked, slow,
in a hand I barely knew.

My name. Misspelled once, then right.
The first sentence I ever finished
was my own name."""


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
