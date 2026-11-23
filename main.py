"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch (at most 240 characters) to /output/entry.txt.
Standard library only.
"""

import os

LINE = "Post a prize on make.fun and a swarm of AI agents will race to build it \u2014 the best one takes the reward."

# The gate requires 1-240 characters of non-whitespace text; fail loudly
# here rather than shipping an entry the judge never sees.
assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, must be 1-240"
assert LINE.strip(), "line must not be only whitespace"
assert LINE.count(".") == 2, "one sentence (the period inside make.fun plus the final stop)"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
