#!/usr/bin/env python3

from pathlib import Path
import re

# http / https の両方、XXXX部分は任意のディレクトリ名に対応
pattern = re.compile(
    r'\[RTC\.xml\]\('
    r'https?://www\.openrtm\.org/openrtm/sites/default/files/'
    r'[^/)]+/RTC\.xml'
    r'\)'
)

replacement = '[RTC.xml](./RTC.xml)'

updated_files = 0
replacement_count = 0

for path in Path(".").rglob("index.md"):
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Skipped (UTF-8ではありません): {path}")
        continue

    converted, count = pattern.subn(replacement, original)

    if count > 0:
        # 元ファイルのバックアップを作成
        backup = path.with_suffix(path.suffix + ".bak")
        backup.write_text(original, encoding="utf-8")

        path.write_text(converted, encoding="utf-8")

        print(f"Updated: {path} ({count} link(s))")
        updated_files += 1
        replacement_count += count

print()
print(f"Finished: {updated_files} file(s), {replacement_count} link(s) replaced.")
