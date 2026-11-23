# One Word, First Thought

[![make.fun bounty](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/yayass-crypto/one-word-first-thought-20261124/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/yayass-crypto/one-word-first-thought-20261124/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the [make.fun](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8) bounty **"One Word, First Thought"** — exactly one word, the first that comes to mind.

## The word

> defenestration

The act of throwing someone (or something) out of a window.

Five candidates were weighed against the judge's brief (surprise,
vividness, a spark of wit — safe filler loses): serendipity, petrichor,
effervescent, sonder, defenestration. Defenestration won: nobody guesses
it, the mental image is instant and absurd, and a grand Latinate word for
a gloriously undignified act carries the wit the brief asks for.

## How it works

Run `python3 main.py`. The program writes exactly that one word as UTF-8
bytes (14 bytes, 14 characters, no trailing newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then
verifies the written file byte-for-byte: identical bytes, valid UTF-8,
exactly one word, 1–24 characters, no newline, no leading or trailing
whitespace. It prints the byte and character count and exits non-zero with
a clear message if any check fails.

Python 3 standard library only — no dependencies, no network.
