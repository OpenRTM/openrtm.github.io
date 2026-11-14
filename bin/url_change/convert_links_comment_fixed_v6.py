#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import csv
import re
import sys
from pathlib import Path


# Markdown inline links/images: [text](url) or ![alt](url)
MD_LINK_RE = re.compile(r'(?P<prefix>!?\[[^\]]*\]\()(?P<url>[^)]+)(?P<suffix>\))')
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


def split_fragment(url: str):
    """
    Split URL into the part used for CSV lookup and its #fragment.

    Example:
      /ja/node/640#2005SDKattention
        -> ("/ja/node/640", "#2005SDKattention")
    """
    if "#" not in url:
        return url, ""
    base, fragment = url.split("#", 1)
    return base, "#" + fragment


def normalize_lookup_url(url: str):
    """
    Normalize a URL only for CSV lookup.

    - Remove "{{ site.baseurl }}" from the beginning.
    - Remove #fragment and return it separately.

    Examples:
      {{ site.baseurl }}/ja/node/1554
        -> ("/ja/node/1554", "")

      {{ site.baseurl }}/ja/node/640#2005SDKattention
        -> ("/ja/node/640", "#2005SDKattention")
    """
    url = url.strip()

    baseurl_prefix = "{{ site.baseurl }}"
    if url.startswith(baseurl_prefix):
        url = url[len(baseurl_prefix):]

    return split_fragment(url)


def find_rule(url: str, rules: dict):
    """
    Find a CSV rule for a URL.

    Matching order:
    1. Exact URL as written in index.md.
    2. URL normalized for CSV lookup:
       - remove "{{ site.baseurl }}"
       - remove #fragment

    Returns:
        (row, fragment)

    fragment is returned so that action=change can preserve the original anchor.
    """
    # Prefer an exact CSV match if one exists.
    row = rules.get(url)
    if row is not None:
        return row, ""

    lookup_url, fragment = normalize_lookup_url(url)
    row = rules.get(lookup_url)
    if row is not None:
        return row, fragment

    return None, ""


def get_comment(row: dict, lang: str) -> str:
    if lang == "ja":
        return (row.get("comment_ja") or row.get("comment_jp") or "").strip()
    return (row.get("comment_en") or "").strip()


def replacement_for_url(url: str, row: dict, lang: str, fragment: str = ""):
    """Return (new_url, comment_to_append) for one URL match."""
    action = (row.get("action") or "").strip()

    if action == "keep":
        return url, ""

    if action == "change":
        new_url = make_change_url(lang, row.get("new_url") or "")
        # If matching succeeded after removing #fragment, preserve that fragment
        # on the converted destination URL.
        if fragment:
            new_url += fragment
        return new_url, ""

    if action == "no_link_page":
        return "", get_comment(row, lang)

    if action == "projectpage":
        # Keep the original URL and append the language-specific comment.
        return url, get_comment(row, lang)

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
        row, fragment = find_rule(url, rules)
        if row is None:
            return m.group(0)

        action = (row.get("action") or "").strip()
        new_url, comment = replacement_for_url(url, row, lang, fragment)
        if action in counts:
            counts[action] += 1

        result = f'{m.group("prefix")}{new_url}{m.group("suffix")}'
        if action in ("no_link_page", "projectpage"):
            result = append_comment_once(result, comment)
        return result

    text = MD_LINK_RE.sub(md_repl, text)

    def html_repl(m):
        url = m.group("url")
        row, fragment = find_rule(url, rules)
        if row is None:
            return m.group(0)

        action = (row.get("action") or "").strip()
        new_url, comment = replacement_for_url(url, row, lang, fragment)
        if action in counts:
            counts[action] += 1

        result = (
            f'{m.group("open")}{m.group("quote")}{new_url}{m.group("quote")}'
            f'{m.group("attrs")}{m.group("body")}{m.group("close")}'
        )
        if action in ("no_link_page", "projectpage"):
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
