#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
check.csv に記載されたファイル名を、実行したディレクトリ以下から再帰検索し、
存在すれば result 列に「ある」、存在しなければ「無し」を書き込みます。

find ./ -name 'xxxxx' と同じように、ディレクトリ階層を再帰的に検索します。

使い方:
    python3 check_files.py
    python3 check_files.py check.csv
    python3 check_files.py check.csv --column filename

CSV の検索対象列は、次の順で自動判定します。
    filename, file_name, file, name, path

該当する列名がない場合、result 以外の列が1列だけなら、その列を検索対象にします。
複数列あって自動判定できない場合は --column で列名を指定してください。
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from pathlib import Path


CANDIDATE_COLUMNS = ("filename", "file_name", "file", "name", "path")


def detect_encoding(csv_path: Path) -> str:
    """UTF-8 BOM付きにも対応してCSVを読み込むためのエンコーディングを返す。"""
    with csv_path.open("rb") as f:
        head = f.read(3)
    return "utf-8-sig" if head == b"\xef\xbb\xbf" else "utf-8"


def choose_target_column(fieldnames: list[str], requested: str | None) -> str:
    """検索対象にするCSV列を決定する。"""
    if requested:
        if requested not in fieldnames:
            raise ValueError(
                f"指定した列 '{requested}' がCSVにありません。"
                f" 利用可能な列: {', '.join(fieldnames)}"
            )
        return requested

    # よく使われる列名を優先して自動判定する。
    lower_map = {name.lower(): name for name in fieldnames}
    for candidate in CANDIDATE_COLUMNS:
        if candidate in lower_map:
            return lower_map[candidate]

    # result以外の列が1つだけなら、その列を検索対象とする。
    non_result = [name for name in fieldnames if name.lower() != "result"]
    if len(non_result) == 1:
        return non_result[0]

    raise ValueError(
        "検索対象の列を自動判定できません。"
        " --column 列名 を指定してください。"
        f" 利用可能な列: {', '.join(fieldnames)}"
    )


def collect_file_names(root: Path, ignored_paths: set[Path]) -> set[str]:
    """
    root以下に存在する全ファイル名を収集する。
    find ./ -name 'xxxxx' と同様、ファイル名そのもの（basename）で判定する。
    """
    names: set[str] = set()

    for current_root, _dirs, files in os.walk(root):
        current = Path(current_root)
        for filename in files:
            full_path = (current / filename).resolve()
            if full_path in ignored_paths:
                continue
            names.add(filename)

    return names


def main() -> int:
    parser = argparse.ArgumentParser(
        description="check.csvのファイル名をカレントディレクトリ以下から再帰検索します。"
    )
    parser.add_argument(
        "csv_file",
        nargs="?",
        default="check.csv",
        help="入力CSVファイル。省略時は check.csv",
    )
    parser.add_argument(
        "--column",
        help="ファイル名が入っている列名。省略時は自動判定",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="検索を開始するディレクトリ。省略時はカレントディレクトリ",
    )
    parser.add_argument(
        "--output",
        help="出力CSV。省略時は入力CSVを上書き",
    )
    args = parser.parse_args()

    csv_path = Path(args.csv_file).resolve()
    root = Path(args.root).resolve()
    output_path = Path(args.output).resolve() if args.output else csv_path

    if not csv_path.is_file():
        print(f"エラー: CSVファイルが見つかりません: {csv_path}", file=sys.stderr)
        return 1
    if not root.is_dir():
        print(f"エラー: 検索ディレクトリが見つかりません: {root}", file=sys.stderr)
        return 1

    encoding = detect_encoding(csv_path)

    # CSVを読み込む。newline='' はcsvモジュール利用時の推奨指定。
    with csv_path.open("r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("エラー: CSVにヘッダーがありません。", file=sys.stderr)
            return 1
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    try:
        target_column = choose_target_column(fieldnames, args.column)
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        return 1

    # result列がなければ末尾に追加する。
    result_column = next((n for n in fieldnames if n.lower() == "result"), None)
    if result_column is None:
        result_column = "result"
        fieldnames.append(result_column)

    # 入出力CSV自身は検索対象から除外する。
    ignored = {csv_path.resolve(), output_path.resolve()}

    print(f"検索対象ディレクトリ: {root}")
    print(f"CSV: {csv_path}")
    print(f"検索対象列: {target_column}")
    print("ファイル一覧を再帰検索しています...")

    # 行ごとにfindを実行すると遅いため、一度だけ再帰走査してファイル名一覧を作る。
    existing_names = collect_file_names(root, ignored)

    found_count = 0
    missing_count = 0
    blank_count = 0

    for row in rows:
        value = (row.get(target_column) or "").strip()

        # 空欄は検索せず result も空欄にする。
        if not value:
            row[result_column] = ""
            blank_count += 1
            continue

        # find ./ -name xxxxx と同じく「ファイル名」で検索する。
        # CSVにパスが書かれていた場合も、最後のファイル名部分を使用する。
        target_name = Path(value.replace("\\", "/")).name

        if target_name in existing_names:
            row[result_column] = "ある"
            found_count += 1
        else:
            row[result_column] = "無し"
            missing_count += 1

    # UTF-8で書き出す。日本語の「ある」「無し」もそのまま保存される。
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"出力: {output_path}")
    print(f"ある: {found_count}件")
    print(f"無し: {missing_count}件")
    if blank_count:
        print(f"空欄: {blank_count}件")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
