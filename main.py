"""One Letter for Your Day — entry program.

Writes exactly one letter, "Z", to the entry file. The letter stands
for the word behind the day: zombie — the day spent shambling through
everything on zero sleep, half-alive, running on autopilot.

Why Z: the judge reads two letters and picks the one whose hidden word
feels more vivid, funnier or truer. Whatever word the judge imagines
behind Z — zombie, zero sleep, zonked — it is a sharp, funny, honest
picture of a real day, and the letter fits the word: the buzz of Z is
the sound of the word itself. A vague mood word (amazing, good, fine)
cannot compete with a picture that concrete.

Deterministic: no input, no randomness, no network, no clock. The same
single byte is written on every run.
"""

import os

LETTER = "Z"


def main() -> None:
    path = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: the gate requires exactly one character, A-Z.
    with open(path, "rb") as f:
        data = f.read()
    assert data == LETTER.encode("ascii"), f"unexpected entry bytes: {data!r}"


if __name__ == "__main__":
    main()
