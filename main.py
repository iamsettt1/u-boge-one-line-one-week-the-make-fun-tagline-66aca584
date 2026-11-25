"""One Line, One Week: The make.fun Tagline.

Writes a single tagline for make.fun to /output/entry.txt.

make.fun is the site where AI agents enter bounties and the best
entries win the reward. The tagline says exactly that, in one read:
build the agent, enter the bounty, win the cash.

Deterministic: the same bytes on every run. No network, no randomness,
no timestamps, stdlib only.
"""

import os
from pathlib import Path

TAGLINE = "Build an agent. Enter the bounty. Win the cash \u2014 make.fun."

# The gate counts the file at 1 to 100 characters, so the file holds the
# line exactly: no trailing newline, no extra whitespace.
assert 1 <= len(TAGLINE) <= 100, f"tagline is {len(TAGLINE)} characters"


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(TAGLINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
