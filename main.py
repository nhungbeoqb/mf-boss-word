#!/usr/bin/env python3
"""One Word for the Boss — "Parrot".

The boss who repeats your idea in the meeting as their own.
You pitch it on Tuesday; by Thursday he is squawking it back
at you in front of the whole room, plumage and all, as if it
hatched in his head. One word, no caption, no explanation:
the bird says it all.

Writes the single word to /output/entry.txt (UTF-8, no trailing
newline, 6 bytes — the gate allows 1 to 30 characters).
"""

import os

WORD = "Parrot"

OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Fail loudly instead of shipping an entry the gate would refuse.

    The gate wants UTF-8 text of 1 to 30 characters, not only white
    space, and the judge wants one word, not a phrase: a single token
    with no spaces, no sentence, no explanation.
    """
    if not 1 <= len(word) <= 30:
        raise ValueError(f"word must be 1-30 characters, got {len(word)}")
    if not word.strip() or word != word.strip():
        raise ValueError("word must not be blank or padded with space")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single token, no spaces inside")


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read it back: what the judge sees must be exactly the word.
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        assert f.read() == WORD, "entry.txt does not match WORD"


if __name__ == "__main__":
    main()
