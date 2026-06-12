import re
from pathlib import Path
from typing import Tuple, List


def read_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p.read_text(encoding="utf-8")


def file_stats(text: str) -> Tuple[int, int, int]:
    lines = text.splitlines()
    num_lines = len(lines)
    words = re.findall(r"\w+", text)
    num_words = len(words)
    num_chars = len(text)
    return num_lines, num_words, num_chars


def find_occurrences(text: str, substring: str) -> List[int]:
    positions = []
    start = 0
    while True:
        idx = text.find(substring, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + len(substring)
    return positions


def replace_text(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


def normalize_text(text: str) -> str:
    # Lowercase and remove basic punctuation
    text = text.lower()
    text = re.sub(r"[^
\w\s]", "", text)
    return text


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple text processing utilities")
    parser.add_argument("path", help="Path to the text file")
    parser.add_argument("--stats", action="store_true", help="Print file statistics")
    parser.add_argument("--find", help="Find substring occurrences")
    parser.add_argument("--replace", nargs=2, metavar=("OLD", "NEW"), help="Replace OLD with NEW and print result")
    parser.add_argument("--out", help="Write output to file (used with --replace)")

    args = parser.parse_args()

    content = read_file(args.path)

    if args.stats:
        lines, words, chars = file_stats(content)
        print(f"Lines: {lines}")
        print(f"Words: {words}")
        print(f"Characters: {chars}")

    if args.find:
        positions = find_occurrences(content, args.find)
        print(f"Found {len(positions)} occurrences at positions: {positions}")

    if args.replace:
        old, new = args.replace
        out_text = replace_text(content, old, new)
        if args.out:
            Path(args.out).write_text(out_text, encoding="utf-8")
            print(f"Wrote replaced text to {args.out}")
        else:
            print(out_text)
