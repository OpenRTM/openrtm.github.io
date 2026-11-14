#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

PROJECT_BASE = "https://www.openrtm.org/openrtm/ja/"

# Markdown inline links/images: [text](url) or ![alt](url)
MD_LINK_RE = re.compile(r'(?P<prefix>!?\[[^\]]*\]\()(?P<url>[^)\s]+)(?P<suffix>\))')
# HTML anchor tags: <a ... href="url" ...>...</a>
HTML_A_RE = re.compile(
    r'(?P<open><a\b[^>]*?\bhref\s*=\s*)(?P<quote>["\'])(?P<url>.*?)(?P=quote)(?P<attrs>[^>]*>)(?P<body>.*?)(?P<close></a>)',
    re.IGNORECASE | re.DOTALL,
)


def load_rules(csv_path: Path):
    """Load conversion rules from the UTF-8 CSV file."""
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV header was not found.")

        required = {"original_url", "action", "new_url", "comment_en"}
        missing = required - set(reader.fieldnames)
        if missing:
            raise ValueError(f"Missing CSV columns: {', '.join(sorted(missing))}")

        # The current CSV uses comment_jp. Also accept comment_ja for future files.
        if "comment_jp" not in reader.fieldnames and "comment_ja" not in reader.fieldnames:
            raise ValueError("CSV must contain either comment_jp or comment_ja.")

        rules = {}
        for line_no, row in enumerate(reader, start=2):
            original = (row.get("original_url") or "").strip()
            action = (row.get("action") or "").strip()
            if not original or not action:
                continue
            if original in rules:
                print(
                    f"Warning: duplicate original_url at CSV line {line_no}: {original}",
                    file=sys.stderr,
                )
            rules[original] = row
        return rules


def make_change_url(lang: str, new_url: str) -> str:
    """Build {{ site.baseurl }}/<lang>/<new_url>."""
    new_url = (new_url or "").strip().strip("/")
    if new_url:
        return f"{{{{ site.baseurl }}}}/{lang}/{new_url}"
    return f"{{{{ site.baseurl }}}}/{lang}/"


def make_project_url(original_url: str) -> str:
    """
    Convert an old project-page URL to the canonical Japanese openrtm.org URL.

    Examples:
      /project/foo
        -> https://www.openrtm.org/openrtm/ja/project/foo
      http://openrtm.org/openrtm/ja/project/foo
        -> https://www.openrtm.org/openrtm/ja/project/foo
    """
    original_url = original_url.strip()

    if original_url.startswith(("http://", "https://")):
        path = urlsplit(original_url).path
        marker = "/openrtm/ja/"
        if marker in path:
            path = path.split(marker, 1)[1]
        else:
            path = path.lstrip("/")
    else:
        path = original_url.lstrip("/")

    return PROJECT_BASE + path


def get_comment(row: dict, lang: str) -> str:
    if lang == "ja":
        return (row.get("comment_ja") or row.get("comment_jp") or "").strip()
    return (row.get("comment_en") or "").strip()


def replacement_for_url(url: str, row: dict, lang: str):
    """Return (new_url, comment_to_append) for one exact URL match."""
    action = (row.get("action") or "").strip()

    if action == "keep":
        return url, ""
    if action == "change":
        return make_change_url(lang, row.get("new_url") or ""), ""
    if action == "no_link_page":
        return "", get_comment(row, lang)
    if action == "projectpage":
        return make_project_url(url), ""

    print(f"Warning: unknown action '{action}' for {url}", file=sys.stderr)
    return url, ""


def append_comment_once(text: str, comment: str) -> str:
    if not comment:
        return text
    # Avoid duplicating the same comment if the script is run again.
    if text.rstrip().endswith(comment):
        return text
    return text + comment


def transform_text(text: str, rules: dict, lang: str):
    counts = {"change": 0, "keep": 0, "no_link_page": 0, "projectpage": 0}

    def md_repl(m):
        url = m.group("url")
        row = rules.get(url)
        if row is None:
            return m.group(0)

        action = (row.get("action") or "").strip()
        new_url, comment = replacement_for_url(url, row, lang)
        if action in counts:
            counts[action] += 1

        result = f'{m.group("prefix")}{new_url}{m.group("suffix")}'
        if action == "no_link_page":
            result = append_comment_once(result, comment)
        return result

    text = MD_LINK_RE.sub(md_repl, text)

    def html_repl(m):
        url = m.group("url")
        row = rules.get(url)
        if row is None:
            return m.group(0)

        action = (row.get("action") or "").strip()
        new_url, comment = replacement_for_url(url, row, lang)
        if action in counts:
            counts[action] += 1

        result = (
            f'{m.group("open")}{m.group("quote")}{new_url}{m.group("quote")}'
            f'{m.group("attrs")}{m.group("body")}{m.group("close")}'
        )
        if action == "no_link_page":
            result = append_comment_once(result, comment)
        return result

    text = HTML_A_RE.sub(html_repl, text)
    return text, counts


def main():
    parser = argparse.ArgumentParser(
        description="Convert links in index.md according to a CSV mapping file."
    )
    parser.add_argument("lang", choices=["ja", "en"], help="target language: ja or en")
    parser.add_argument(
        "csv_file",
        nargs="?",
        default="jekyll_url_link_map_data_0820.csv",
        help="mapping CSV file (default: jekyll_url_link_map_data_0820.csv)",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="process index.md files recursively under the current directory",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show what would change without writing files",
    )
    args = parser.parse_args()

    csv_path = Path(args.csv_file)
    if not csv_path.is_file():
        parser.error(f"CSV file not found: {csv_path}")

    rules = load_rules(csv_path)
    targets = sorted(Path(".").rglob("index.md")) if args.recursive else [Path("index.md")]
    targets = [p for p in targets if p.is_file()]

    if not targets:
        print("index.md was not found.", file=sys.stderr)
        return 1

    total_changed_files = 0
    total_counts = {"change": 0, "keep": 0, "no_link_page": 0, "projectpage": 0}

    for path in targets:
        original_text = path.read_text(encoding="utf-8")
        new_text, counts = transform_text(original_text, rules, args.lang)

        for key, value in counts.items():
            total_counts[key] += value

        if new_text != original_text:
            total_changed_files += 1
            if not args.dry_run:
                path.write_text(new_text, encoding="utf-8")
            print(f"{'Would update' if args.dry_run else 'Updated'}: {path}")

    print(
        "Matches: "
        + ", ".join(f"{k}={v}" for k, v in total_counts.items())
    )
    print(f"Changed files: {total_changed_files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
