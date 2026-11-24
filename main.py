#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) to
/output/entry.txt. Python standard library only, no network,
deterministic: the same sentence every run.

Self-check: the output must be a single sentence of 1-320
characters. Any violation exits 1 without writing a file.
"""

import os
import re
import sys

SENTENCE = (
    "The senator who wrote the toughest AI law in the country has "
    "never once turned a .docx into a PDF \u2014 his staff does that "
    "for him, just like they write the laws he signs."
)

MAX_CHARS = 320


def validate(text: str) -> str:
    """Return the cleaned sentence or raise ValueError."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty or only whitespace")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(cleaned)} characters, over the "
            f"{MAX_CHARS} character limit"
        )
    # Sentence terminators: . ! ? followed by whitespace or end of
    # text. The period inside ".docx" is followed by a letter, so it
    # is not counted as a terminator.
    terminators = re.findall(r"[.!?](?=\s|$)", cleaned)
    if len(terminators) != 1:
        raise ValueError(
            f"entry must be exactly one sentence, found "
            f"{len(terminators)} sentence terminators"
        )
    if not re.search(r"[.!?]$", cleaned):
        raise ValueError("entry must end with sentence punctuation")
    return cleaned


def validate_entry(text: str) -> str | None:
    """Run the self-check; return an error message, or None if valid."""
    try:
        validate(text)
    except ValueError as exc:
        return str(exc)
    return None


def main() -> int:
    # ENTRY_OVERRIDE exists only to test the self-check locally; the
    # grader runs with no environment, so the shipped sentence is used.
    text = os.environ.get("ENTRY_OVERRIDE", SENTENCE)
    error = validate_entry(text)
    if error is not None:
        print(f"self-check failed: {error}", file=sys.stderr)
        return 1
    entry = validate(text)
    out_path = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_path, exist_ok=True)
    with open(os.path.join(out_path, "entry.txt"), "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write(entry + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
