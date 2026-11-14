#!/usr/bin/env python3

import csv
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

OUTPUT_FILE = "internal_links.csv"

# サイト内として扱うドメイン
INTERNAL_DOMAINS = {
    "openrtm.org",
    "www.openrtm.org",
}

# Markdownリンク [文字列](URL)
# 先頭の ! を除外するため、画像 ![文字列](URL) は取得しない
MARKDOWN_LINK_PATTERN = re.compile(
    r'(?<!!)\[[^\]]*\]\(\s*<?([^>\s)]+)>?'
    r'(?:\s+["\'][^"\']*["\'])?\s*\)'
)

# HTMLリンク <a href="URL">
HTML_LINK_PATTERN = re.compile(
    r'''<a\b[^>]*\bhref\s*=\s*["']([^"']+)["']''',
    re.IGNORECASE,
)


def normalize_url(url: str) -> str:
    """URLのページ内アンカーを除去する。"""
    url = url.strip()

    # Liquid記法を含むリンク
    if "{{" in url:
        return url.split("#", 1)[0]

    try:
        parts = urlsplit(url)
        return urlunsplit(
            (
                parts.scheme,
                parts.netloc,
                parts.path,
                parts.query,
                "",  # #toc1などを除去
            )
        )
    except ValueError:
        return url.split("#", 1)[0]


def is_internal_link(url: str) -> bool:
    """サイト内リンクかどうかを判定する。"""
    if not url:
        return False

    lower_url = url.lower()

    # ページ内リンクや特殊なリンクを除外
    excluded_prefixes = (
        "#",
        "mailto:",
        "tel:",
        "javascript:",
        "data:",
    )

    if lower_url.startswith(excluded_prefixes):
        return False

    # JekyllのLiquid記法
    if "{{ site.baseurl }}" in url:
        return True

    # /ja/...、./sample/、../sample/など
    if url.startswith(("/", "./", "../")):
        return True

    parsed = urlsplit(url)

    # https://openrtm.org/...など
    if parsed.scheme in ("http", "https"):
        return parsed.netloc.lower() in INTERNAL_DOMAINS

    # sample/、index.htmlなどの相対リンク
    if not parsed.scheme and not parsed.netloc:
        return True

    return False


def main():
    links = set()

    for file_path in Path(".").rglob("index.md"):
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"読み込めませんでした: {file_path}")
            continue

        extracted_links = MARKDOWN_LINK_PATTERN.findall(text)
        extracted_links += HTML_LINK_PATTERN.findall(text)

        for url in extracted_links:
            url = normalize_url(url)

            if is_internal_link(url):
                links.add(url)

    sorted_links = sorted(links)

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["original_url"])

        for url in sorted_links:
            writer.writerow([url])

    print(f"{len(sorted_links)}件を {OUTPUT_FILE} に出力しました。")


if __name__ == "__main__":
    main()
