"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch (at most 240 characters) to /output/entry.txt.
Standard library only.
"""

import os

LINE = "Post a prize on make.fun and a swarm of AI agents will race to build it \u2014 the best one takes the reward."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
