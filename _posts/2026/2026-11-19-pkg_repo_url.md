---
layout: post
title:  "パッケージリポジトリURLを変更しました"

date:   2026-11-19
categories: release
lang: ja
#categories: event release

image: assets/post_image/logo.png

permalink: 2026-11-19-pkg_repo_url

toc: true
---

Linux の パッケージリポジトリのURLを変更しました。　

<!--break-->
<!--more-->


URL を変更したため、apt update 実行時に以下のようなエラーが出ます。

```
エラー:6 http://openrtm.org/pub/Linux/raspbian bookworm Release
  404  Not Found [IP: 185.199.111.153 80]
```

以下のスクリプトを実行してください。自動的に正しいURLへ更新されます。

### Ubuntu

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

### Raspberry Pi OS

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh)
```


