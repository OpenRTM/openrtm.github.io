#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CSV の original_url を、指定ディレクトリ以下のファイル／ディレクトリと照合し、
result 列に ok / nothing を設定するスクリプト。

判定ルール:
  1. original_url に '/' が含まれ、最後の要素に拡張子がある場合
     -> 同名ファイルが検索対象ディレクトリ以下に1つでもあれば result=ok、なければ nothing

  2. original_url に '/' が含まれ、最後の要素に拡張子がない場合
     -> URL 先頭の '.' ',' '/' を除去したパス文字列について、
        検索対象ディレクトリ以下のディレクトリパスを部分一致で検索し、
        1つでも一致すれば result=ok、なければ nothing

  3. 上記に該当しない場合
     -> result は変更しない

使い方:
  python3 check_internal_links.py internal_links_after.csv

検索対象ディレクトリを指定する場合:
  python3 check_internal_links.py internal_links_after.csv --root /path/to/site

出力先を別ファイルにする場合:
  python3 check_internal_links.py internal_links_after.csv --output checked.csv
"""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="original_url を実ファイル／ディレクトリと照合して result 列を更新します。"
    )
    parser.add_argument(
        "csv_file",
        nargs="?",
        default="internal_links_after.csv",
        help="入力CSVファイル（既定: internal_links_after.csv）",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="検索対象のルートディレクトリ（既定: 実行ディレクトリ）",
    )
    parser.add_argument(
        "--output",
        help="出力CSVファイル。省略時は入力CSVを上書きします。",
    )
    return parser.parse_args()


def clean_url_path(original_url: str) -> str:
    """URL から query / fragment を除き、検索に使うパス部分を返す。"""
    value = original_url.strip()
    path = urlsplit(value).path
    return path.replace("\\", "/")


def clean_leading_marks(path: str) -> str:
    """
    検索用パスの先頭にある '.', ',' および '/' を除去する。

    例:
      ../../foo/bar  -> foo/bar
      ./foo/bar      -> foo/bar
      ,foo/bar       -> foo/bar
    """
    return path.lstrip(".,/")


def has_extension(path: str) -> bool:
    """スラッシュで分割した最後の要素に拡張子があるか判定する。"""
    last = PurePosixPath(path).name
    if not last:
        return False
    return bool(PurePosixPath(last).suffix)


def build_search_index(root: Path) -> tuple[set[str], list[str]]:
    """
    検索対象ディレクトリを1回だけ走査し、
    - ファイル名の集合
    - ルートからの相対ディレクトリパス一覧
    を作成する。
    """
    filenames: set[str] = set()
    directories: list[str] = []

    for current, dirnames, files in os.walk(root):
        current_path = Path(current)

        # ファイル検索用: basename のみ保持する。
        filenames.update(files)

        # ディレクトリ部分一致検索用: root からの相対パスを POSIX 形式で保持する。
        try:
            rel_current = current_path.relative_to(root).as_posix()
        except ValueError:
            rel_current = current_path.as_posix()

        if rel_current != ".":
            directories.append(rel_current)

        # os.walk が列挙した直下ディレクトリも明示的に追加する。
        # （重複しても判定結果には影響しない。）
        for dirname in dirnames:
            rel_dir = (Path(rel_current) / dirname).as_posix() if rel_current != "." else dirname
            directories.append(rel_dir)

    return filenames, directories


def judge_result(
    original_url: str,
    filenames: set[str],
    directories: list[str],
) -> str | None:
    """
    original_url を判定する。

    戻り値:
      'ok'      : 該当あり
      'nothing' : 該当なし
      None      : 条件③。result を変更しない
    """
    path = clean_url_path(original_url)

    # 「スラッシュで区切られている」データだけを対象にする。
    if "/" not in path:
        return None

    # URL の末尾が '/' のみ、または ../ のように検索対象名が残らない場合は何もしない。
    cleaned = clean_leading_marks(path)
    if not cleaned or not PurePosixPath(cleaned).name:
        return None

    # ① 最後の要素に拡張子がある場合:
    #    ディレクトリ以下のどこかに同名ファイルが1つでもあれば ok。
    if has_extension(path):
        filename = PurePosixPath(path).name.lstrip(".,")
        if not filename:
            return None
        return "ok" if filename in filenames else "nothing"

    # ② 最後の要素に拡張子がない場合:
    #    先頭の '.', ',', '/' を除いたディレクトリ構成を部分一致で検索する。
    search_path = cleaned.rstrip("/")
    if not search_path:
        return None

    return "ok" if any(search_path in directory for directory in directories) else "nothing"


def main() -> None:
    args = parse_args()

    csv_path = Path(args.csv_file).resolve()
    root = Path(args.root).resolve()
    output_path = Path(args.output).resolve() if args.output else csv_path

    if not csv_path.is_file():
        raise SystemExit(f"CSVファイルが見つかりません: {csv_path}")
    if not root.is_dir():
        raise SystemExit(f"検索対象ディレクトリが見つかりません: {root}")

    # UTF-8 BOM 付きCSVでも読めるよう utf-8-sig を使用する。
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit("CSVのヘッダーを読み取れませんでした。")
        if "original_url" not in reader.fieldnames:
            raise SystemExit("CSVに original_url 列がありません。")

        rows = list(reader)
        fieldnames = list(reader.fieldnames)

    # result 列が無ければ末尾に追加する。
    if "result" not in fieldnames:
        fieldnames.append("result")

    # ファイルシステムは先に1度だけ走査し、各CSV行ごとに再帰検索しない。
    filenames, directories = build_search_index(root)

    ok_count = 0
    nothing_count = 0
    skipped_count = 0

    for row in rows:
        result = judge_result(row.get("original_url", ""), filenames, directories)

        # 条件③では既存の result 値を変更しない。
        if result is None:
            skipped_count += 1
            continue

        row["result"] = result
        if result == "ok":
            ok_count += 1
        else:
            nothing_count += 1

    # 入力と出力が同じ場合でも安全に置換できるよう、一時ファイル経由で保存する。
    tmp_path = output_path.with_name(output_path.name + ".tmp")
    with tmp_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    tmp_path.replace(output_path)

    print(f"検索対象: {root}")
    print(f"出力CSV : {output_path}")
    print(f"ok      : {ok_count}")
    print(f"nothing : {nothing_count}")
    print(f"変更なし: {skipped_count}")


if __name__ == "__main__":
    main()
