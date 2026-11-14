#!/usr/bin/env python3

import os
import sys
import csv


def get_structure(root):
    """
    root以下のファイル・ディレクトリ構成を取得する。
    戻り値:
        {
            "dir1": "dir",
            "dir1/file.txt": "file",
            ...
        }
    """
    structure = {}

    for current_dir, dirs, files in os.walk(root):

        for name in dirs:
            full_path = os.path.join(current_dir, name)
            relative_path = os.path.relpath(full_path, root)
            structure[relative_path] = "dir"

        for name in files:
            full_path = os.path.join(current_dir, name)
            relative_path = os.path.relpath(full_path, root)
            structure[relative_path] = "file"

    return structure


def compare_directories(dir_a, dir_b, output_csv):
    structure_a = get_structure(dir_a)
    structure_b = get_structure(dir_b)

    all_paths = sorted(set(structure_a) | set(structure_b))

    with open(output_csv, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        writer.writerow([
            "path",
            "A",
            "B",
            "status"
        ])

        for path in all_paths:
            type_a = structure_a.get(path, "")
            type_b = structure_b.get(path, "")

            if path not in structure_a:
                status = "Bのみ"

            elif path not in structure_b:
                status = "Aのみ"

            elif type_a != type_b:
                status = "種別が異なる"

            else:
                # A/Bで同じ構成のものはCSVに出力しない
                continue

            writer.writerow([
                path,
                type_a,
                type_b,
                status
            ])

    print(f"比較結果を出力しました: {output_csv}")


def main():
    if len(sys.argv) != 4:
        print(
            f"Usage: {sys.argv[0]} DIR_A DIR_B OUTPUT.csv"
        )
        sys.exit(1)

    dir_a = sys.argv[1]
    dir_b = sys.argv[2]
    output_csv = sys.argv[3]

    if not os.path.isdir(dir_a):
        print(f"ディレクトリが存在しません: {dir_a}")
        sys.exit(1)

    if not os.path.isdir(dir_b):
        print(f"ディレクトリが存在しません: {dir_b}")
        sys.exit(1)

    compare_directories(dir_a, dir_b, output_csv)


if __name__ == "__main__":
    main()
