#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the phone's final text message to /output/entry.txt.
Deterministic, stdlib-only, no input, no network.
"""

import os

ENTRY_TEXT = (
    "1% left. Delete my search history, keep the photos, and tell "
    "the charger I only loved it for the cable. "
    "Thanks for holding me. Goodbye, thumb."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
