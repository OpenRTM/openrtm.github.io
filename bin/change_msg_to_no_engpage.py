#!/usr/bin/env python3
import os
import re

INSERT_TEXT = """<br>
<a>No English version available.
</a>
"""


TARGET_STRING1 = "-------jp page!!-------"
TARGET_STRING = "-------jp page!!!-------"


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 対象文字列を削除
    content = content.replace(TARGET_STRING, "")

    # フロントマター直後に挿入
    # --- ... --- の直後
    pattern = r"^(---\s*\n.*?\n---\s*\n)"
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(
            pattern,
            r"\1" + INSERT_TEXT + "\n",
            content,
            count=1,
            flags=re.DOTALL
        )

    # 変更があった場合のみ保存
    if content != original:
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
