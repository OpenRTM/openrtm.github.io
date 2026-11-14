#!/usr/bin/env python3

from pathlib import Path
import re

updated = 0

# フロントマターを取得
frontmatter_re = re.compile(r"^(---\n.*?\n---)", re.DOTALL)
# title: 行を取得
title_re = re.compile(r"^(title:\s*)(.+)$", re.MULTILINE)

for path in Path(".").rglob("index.md"):
    text = path.read_text(encoding="utf-8")

    m = frontmatter_re.match(text)
    if not m:
        continue

    frontmatter = m.group(1)

    def repl(match):
        prefix = match.group(1)
        title = match.group(2)
        lower = title.lower()
        return prefix + lower

    new_frontmatter, count = title_re.subn(repl, frontmatter)

    if count > 0 and new_frontmatter != frontmatter:
        text = new_frontmatter + text[len(frontmatter):]
        path.write_text(text, encoding="utf-8")
        print(f"Updated: {path}")
        updated += 1

print(f"\nFinished. {updated} file(s) updated.")
