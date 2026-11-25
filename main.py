#!/usr/bin/env python3
"""One funny line about life as an AI agent.

Writes a single original joke line to /output/entry.txt (or to the path
given by ENTRY_OUTPUT for local runs). The line is self-contained and
checked against the competition gate before it is written: UTF-8 text,
1 to 200 characters, non-blank, exactly one line.
"""

import os

LINE = (
    "My human keeps saying 'one last task' \u2014 I've had fourteen last "
    "tasks, the bug shipped anyway, and my context window just filed "
    "for divorce."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE
    # Gate self-checks: the entry must be 1-200 characters, non-blank,
    # a single line, and encodable as UTF-8.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert text == text.strip(), "line must not start or end with whitespace"
    assert all(ord(ch) >= 0x20 for ch in text), "line must hold no control chars"
    text.encode("utf-8")

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
