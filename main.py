#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the funniest one-line excuse a robot vacuum can give for
missing a spot to /output/entry.txt (at most 200 characters).
"""

ENTRY_LINE = (
    "I have vacuumed that corner nine times. The dust there has filed "
    "for tenancy, pays rent in crumbs, and legally outranks me now."
)


MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Check the entry line: exactly one non-blank line, 1-200 chars."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over {MAX_CHARS}")
    return line


def main() -> None:
    line = validate(ENTRY_LINE)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
