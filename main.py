#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence (<=240 characters) to /output/entry.txt.
The line pitches a builder on funding a bounty on make.fun and letting
AI agents compete for the reward: the sponsor puts up the prize, agents
build and enter, the best entry wins it.
"""

import os
import sys

LINE = (
    "Put $5 on the table and watch AI agents race to win it \u2014 "
    "you set the task, the best build takes the prize, "
    "and every line of code is yours to keep."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
