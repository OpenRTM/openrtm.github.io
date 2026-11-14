#!/usr/bin/env python3
import os

INSERT_TEXT = "-------jp page!!-------\n"

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # フロントマター判定（先頭が --- の場合のみ）
    new_lines = []
    i = 0

    if lines and lines[0].strip() == "---":
        new_lines.append(lines[0])
        i = 1

        # フロントマター終了までコピー
        while i < len(lines):
            new_lines.append(lines[i])
            if lines[i].strip() == "---":
                i += 1
                break
            i += 1

        # フロントマター直後に挿入
        new_lines.append(INSERT_TEXT)
    else:
        # フロントマターが無い場合は先頭に入れる
        new_lines.append(INSERT_TEXT)

    # 残りの本文
    new_lines.extend(lines[i:])

    # 最後に挿入（重複防止したいなら条件追加可）
    if not new_lines[-1].endswith("\n"):
        new_lines[-1] += "\n"
    new_lines.append(INSERT_TEXT)

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def main():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "index.md":
                path = os.path.join(root, file)
                print(f"Processing: {path}")
                process_file(path)

if __name__ == "__main__":
    main()
