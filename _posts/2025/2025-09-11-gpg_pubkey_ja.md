---
layout: post
title:  "GPG公開鍵を更新しました"
# excerpt: "update gpg_pubkey"
date:   2025-09-11
categories: release
lang: ja
#categories: event release

#※使っていない変数
#slug: 2025-12-11-rtmcontest2025
#permalink: {{ page.slug }}

#image: contest2025_news_.png

image: assets/post_image/logo.png
#image: assets/post_image/2025/
#image_dir: assets/post_image/2025/(permalink_dir)/
image_alt: 20250911_gpg_pubkey
image_caption: 20250911_gpg_pubkey

permalink: 2025-09-11-20250911_gpg_pubkey_ja

toc: true
---

Linux の deb パッケージ署名に使用している GPG 公開鍵を更新しました。　

<!--break-->
<!--more-->


apt update 実行時に以下のような警告が表示される場合は、公開鍵を更新してください。

```
W: 署名照合中にエラーが発生しました。リポジトリは更新されず、過去のインデックスファイルが使われます。
        GPG エラー: http://openrtm.org/pub/Linux/ubuntu noble InRelease: 公開鍵を利用できないため、以下の署名は検証できませんでした: NO_PUBKEY BD151425C7DBB13F
 W: http://openrtm.org/pub/Linux/ubuntu/dists/noble/InRelease の取得に失敗しました 公開鍵を利用できないため、以下の署名は検証できませんでした: NO_PUBKEY BD151425C7DBB13F
```

公開鍵を更新しない場合、OpenRTM-aist の新しいバージョンが apt upgrade で自動更新できなくなります。

以下のスクリプトを一度実行することで、自動的に公開鍵が更新されます。

### Ubuntu

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

### Raspberry Pi OS

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh)
```


