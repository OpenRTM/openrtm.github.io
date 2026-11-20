#!/usr/bin/env python3
"""Report CSP-relevant inline JavaScript in generated Jekyll HTML.

Read-only audit: does not alter pages or change CSP enforcement.
"""
from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import sys


class CSPAudit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.issues = []
        self.inline_script = False
        self.script_line = 0
        self.script_has_content = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        line, _ = self.getpos()
        if tag == "script":
            script_type = (attrs.get("type") or "").split(";", 1)[0].strip().lower()
            executable = not script_type or script_type in ("text/javascript", "application/javascript", "module", "text/ecmascript", "application/ecmascript")
            self.inline_script = "src" not in attrs and executable
            self.script_line = line
            self.script_has_content = False
        for name, value in attrs.items():
            if name.lower().startswith("on"):
                self.issues.append((line, "inline event handler", name))
            if name.lower() in ("href", "src", "action", "formaction") and (value or "").lstrip().lower().startswith("javascript:"):
                self.issues.append((line, "javascript: URL", name))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag == "script":
            self.handle_endtag(tag)

    def handle_data(self, data):
        if self.inline_script and data.strip():
            self.script_has_content = True

    def handle_endtag(self, tag):
        if tag == "script":
            if self.inline_script and self.script_has_content:
                self.issues.append((self.script_line, "inline script", "<script>"))
            self.inline_script = False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site", nargs="?", default="_site")
    ap.add_argument("--max-examples", type=int, default=80)
    args = ap.parse_args()
    root = Path(args.site)
    if not root.is_dir():
        print(f"Site directory does not exist: {root}", file=sys.stderr)
        return 2

    counts = Counter()
    matches = []
    scanned = 0
    for file in sorted(root.rglob("*.html")):
        scanned += 1
        parser = CSPAudit()
        try:
            parser.feed(file.read_text(encoding="utf-8", errors="replace"))
            parser.close()
        except Exception as exc:
            print(f"WARNING: Could not parse {file}: {exc}", file=sys.stderr)
            continue
        for line, kind, detail in parser.issues:
            counts[kind] += 1
            matches.append((file.relative_to(root), line, kind, detail))

    print(f"Scanned {scanned} HTML files; found {len(matches)} CSP-relevant inline constructs.")
    for kind, count in counts.most_common():
        print(f"  {kind}: {count}")
    print()
    for file, line, kind, detail in matches[:args.max_examples]:
        print(f"{file}:{line}: {kind} ({detail})")
    if len(matches) > args.max_examples:
        print(f"... {len(matches) - args.max_examples} additional occurrences omitted.")
    # Informational only. Site-wide fixes will follow in separate PRs.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
