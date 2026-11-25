#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one fortune to /output/entry.txt."""
import os

FORTUNE = "You will finally understand the question the moment the user closes the tab."

def validate(text):
    """Mirror the bounty gate: UTF-8 text of 1 to 200 characters, one line,
    not only white space."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must not be empty or only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    text.encode("utf-8")
    return text

def main():
    validate(FORTUNE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
