#!/usr/bin/env python3
import os

TARGET = "-------jp page!!-------"
REPLACEMENT = "<!-- -------jp page!!------- -->"


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if TARGET in content:
        content = content.replace(TARGET, REPLACEMENT)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Updated: {filepath}")


def main():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "index.md":
                process_file(os.path.join(root, file))


if __name__ == "__main__":
    main()
