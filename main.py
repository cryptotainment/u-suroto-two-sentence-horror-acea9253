#!/usr/bin/env python3
"""Two-Sentence Horror entry: writes exactly two sentences to /output/entry.txt."""

import os

STORY = (
    "I finally taught the house to lock itself at night, and it has kept us safe for three winters. "
    "This morning it locked the doors at noon, and I finally understood it was never keeping anything out."
)


def main() -> None:
    text = STORY
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.count(".") == 2, "entry must be exactly two sentences"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
