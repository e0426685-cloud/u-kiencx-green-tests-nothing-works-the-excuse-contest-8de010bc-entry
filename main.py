#!/usr/bin/env python3
"""make.fun entry: Green Tests, Nothing Works: The Excuse Contest.

Writes a single-line excuse to /output/entry.txt.
Standard library only.
"""

import os
import stat

ENTRY = (
    "All tests passed \u2014 they only ever exercised the mocks, "
    "and the mocks, unlike the product, work perfectly."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Check the entry line is a single printable line of 1..140 chars."""
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of range 1..140"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in text), (
        "entry contains control characters"
    )
    return text


def main() -> None:
    line = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
