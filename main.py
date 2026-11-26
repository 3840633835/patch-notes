#!/usr/bin/env python3
"""Sheep to regrets — the entry program for make.fun's
"Real-Life Patch Notes: The Comedy Changelog".

Writes the one-line entry (a software patch note for a bug in human
biology, 98 characters, under the 160-character gate) to
``<output>/entry.txt`` and prints it. Standard library only, no
network, no randomness, no clock: the same bytes come out on every run.

The grader runs this as ``python3 -P -s /bot/main.py`` and reads
``/output/entry.txt``; ``MAKEFUN_OUTPUT_DIR`` (used by the local test)
overrides the output directory, default ``/output``.
"""

import os
import sys

# The entry, byte-identical to entry.txt in this repository.
# The brain's sleep routine counts sheep until 4 a.m., then — with no
# setting changed — switches to counting regrets. A bug report for the
# mind's own insomnia, written as if it had shipped in v2.5.8.
ENTRY = "v2.5.8: fixed a bug where the brain counted sheep until 4 a.m., then switched to counting regrets."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = "entry.txt"


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 160):
        raise SystemExit("entry must be 1 to 160 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file
    # readable by everyone (0644), never the 0600 a temp file gets.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
