#!/usr/bin/env python3
"""Make the Judge Smile — entry program, version 2.

Writes one line, at most 200 characters, about a small good thing that
happened today, to /output/entry.txt. Deterministic: the same text, byte
for byte, on every run. No network, no input, no dependencies beyond the
Python standard library.

Version 2 revises version 1 (the librarian who waived the fine and said
the book had missed its reader) with a third beat from the same giver:
she lends her own copy of the sequel. The change targets warmth (K2)
and surprise (K3) while keeping the subject, the concrete stamp detail,
and the fresh wording of version 1 untouched.
"""

import os

TEXT = "The librarian stamped my overdue book RETURNED WITH THANKS, waived the fine, and whispered that the book had missed me, then lent me her own copy of the sequel."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
