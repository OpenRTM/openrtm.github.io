#!/usr/bin/env python3

import os
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_excluded(url_path, exclude_dirs):
    return any(url_path.startswith(exclude) for exclude in exclude_dirs)

def download_image_for_page(base_url, img_src, exclude_dirs):
    full_url = urljoin(base_url, img_src)
    parsed_img_url = urlparse(full_url)
    img_filename = os.path.basename(parsed_img_url.path)

    if is_excluded(parsed_img_url.path, exclude_dirs):
        print(f"Skipping excluded image: {parsed_img_url.path}")
        return

    save_path = os.path.join(os.getcwd(), img_filename)

    if os.path.exists(save_path):
        print(f"Already exists: {save_path}, skipping.")
        return

    try:
        response = requests.get(full_url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Saved: {save_path}")
        else:
            print(f"Failed to fetch image: {full_url} (status {response.status_code})")
    except Exception as e:
        print(f"Error downloading {full_url}: {e}")

def process_page(url, exclude_dirs):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        body = soup.body

        downloaded_urls = set()

        if body:
            images = body.find_all("img", src=True)
            for img in images:
                img_src = img["src"]
                full_url = urljoin(url, img_src)

                if full_url in downloaded_urls:
                    continue
                downloaded_urls.add(full_url)

                download_image_for_page(url, img_src, exclude_dirs)

    except Exception as e:
        print(f"Failed to process page {url}: {e}")

def crawl_images(start_urls, exclude_dirs):
    for start_url in start_urls:
        print(f"\n=== Processing: {start_url} ===\n")
        process_page(start_url, exclude_dirs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="指定ページ内画像のみをダウンロードするスクリプト")
    parser.add_argument("--start_url", required=True, nargs="+", help="対象ページURL（複数指定可）")
    parser.add_argument("--exclude", nargs="*", default=[], help="除外する画像ディレクトリパス（複数可）")

    args = parser.parse_args()

    start_urls = args.start_url
    crawl_images(start_urls, args.exclude)
