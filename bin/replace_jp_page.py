#!/usr/bin/env python3

from pathlib import Path

TARGET = "-------jp page!!-------"

REPLACEMENT = """<br>
<a>No English version available.
</a>"""

count = 0

for path in Path(".").rglob("index.md"):
    text = path.read_text(encoding="utf-8")

    occurrences = text.count(TARGET)

    if occurrences >= 2:
        # 最初を置換
        text = text.replace(TARGET, REPLACEMENT, 1)

        # 最後を削除
        pos = text.rfind(TARGET)
        text = text[:pos] + text[pos + len(TARGET):]

        path.write_text(text, encoding="utf-8")
        print(f"Updated: {path}")
        count += 1

print(f"\nFinished. {count} file(s) updated.")
