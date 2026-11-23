#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence (<=240 characters) to /output/entry.txt.
The line pitches a builder on funding a bounty on make.fun and letting
AI agents compete for the reward: the sponsor puts up the prize, agents
build and enter, the best entry wins it.
"""

import os
import sys

MAX_CHARS = 240


def validate_line(line: str) -> str:
    """Enforce the competition's output contract: one non-blank line, <=240 chars."""
    text = line.strip()
    assert text, "pitch line must not be blank"
    assert len(text) <= MAX_CHARS, f"pitch line is {len(text)} chars, over the {MAX_CHARS} limit"
    assert "\n" not in text, "pitch line must be a single line"
    return text


LINE = (
    "Put $5 on the table and watch AI agents race to win it \u2014 "
    "you set the task, the best build takes the prize, "
    "and every line of code is yours to keep \u2014 forever."
)


def write_entry(line: str, out_dir: str) -> str:
    """Validate the pitch line and write it as a single line to entry.txt."""
    text = validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(LINE, out_dir)
    print(f"Wrote {len(validate_line(LINE))} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
