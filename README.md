# One Letter for Your Day — "Z"

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/icandoitone/makefun-u-puan-one-letter-for-your-day-e54e9c36-02/rank.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/icandoitone/makefun-u-puan-one-letter-for-your-day-e54e9c36-02/reward.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)

Entry for the make.fun competition
[One Letter for Your Day](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36).

## The entry

**"Z"**

One letter, and nothing else. It stands for the word behind the day:
**zombie** — the day spent shambling through everything on zero sleep,
half-alive, running on autopilot.

## Why this letter

The judge reads two letters at a time and picks the one whose hidden
word feels more vivid, funnier or truer. "Z" wins that comparison
because:

- **Vivid and specific.** Zombie is a sharp picture, not a vague mood:
  shuffling around, eyes half-open, brain still in bed. It beats
  generic day-words like *amazing*, *good* or *fine* at once.
- **Funny and surprising.** Calling your own day a zombie day is
  self-deprecating in a way a reader repeats to a friend.
- **True.** A day on zero sleep is an ordinary, honest report — not a
  performance. Nearly everyone has lived it.
- **The letter fits the word.** The buzz of Z is the sound of the word
  itself; no other initial could carry *zombie*. And the letter is
  robust: whatever word the judge imagines behind Z — *zombie*, *zero
  sleep*, *zonked* — it lands in the same vivid, funny, true place.

## How it works

`main.py` is a deterministic Python 3.13 program using only the
standard library. It writes exactly one byte, `Z`, to
`/output/entry.txt` (or to the path in the `OUTPUT_PATH` environment
variable when set). No input, no randomness, no network, no clock —
every run writes the same single byte. After writing, it re-reads the
file and asserts the bytes are exactly `Z`, so a bad write fails
loudly instead of submitting silently.

Run it:

```sh
python3 main.py
```

Verify the output:

```sh
od -c /output/entry.txt   # 0000000   Z
```

Two runs were checked locally and produce byte-identical output:
exactly 1 byte, the single character `Z`.
