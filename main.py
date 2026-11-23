#!/usr/bin/env python3
"""One Word, First Thought — entry program.

Writes exactly one word, and nothing else, to /output/entry.txt.

The chosen word: "defenestration" — the act of throwing someone (or
something) out of a window. Surprising (nobody guesses it), vivid (the
mental image is instant and absurd), and with a spark of wit (a grand,
Latinate word for a gloriously undignified act). It beats safe filler on
every point of the judge's brief.

Standard library only. Deterministic: the same bytes every run.
"""

import os
import sys

WORD = "defenestration"


def _out_dir():
    """Where the entry goes: the harness dir, /output, or local out/."""
    d = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if d:
        return d
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return "out"


def main():
    out_dir = _out_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = WORD.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Verify what was written: exactly one word, no newline, valid UTF-8.
    with open(path, "rb") as f:
        back = f.read()
    text = back.decode("utf-8")
    assert back == data, "bytes differ from the chosen word"
    assert len(text.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(text) <= 24, "entry must be 1-24 characters"
    assert not text.isspace(), "entry must not be only whitespace"
    # No trailing newline, no extra bytes: the brief wants exactly one
    # word and nothing else, and the gate allows 1-24 characters.
    assert b"\n" not in back and b"\r" not in back, "no newline allowed"
    assert text == text.strip(), "no leading or trailing whitespace"
    print(f"wrote {len(back)} bytes ({len(text)} chars) to {path}: {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
