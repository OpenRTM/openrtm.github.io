---
layout: post
title:  "MacOS用パッケージ群を公開しました"
# excerpt: "MacOS用パッケージ群公開"
date:   2020-10-30
categories: release
lang: ja

#※使っていない変数
#slug: 2021-12-11-rtmcontest2021
#permalink: {{ page.slug }}

#image: contest2021_news_.png

image: assets/post_image/2020/680px-Homebrew_logo.svg_.png
image_dir: assets/post_image/2020/
image_alt: homebrew_package_alt
image_caption: homebrew_package_cap

permalink: 2020-10-30-homebrew_package

toc: true
---


MacOS 用OpenRTM-aistパッケージ群を公開しました。

[homebrew](https://brew.sh/index_ja) はMac用パッケージマネージャの一種で、様々なソフトウェアをインストール・管理することができます。
OpenRTM-aistもhomebrewを使ってバイナリパッケージをMacOSにインストールできるようになりました。提供しているパッケージは以下のとおりです。

- OpenRTM-aist-1.2.2
  - C++ version
  - Python version
  - Java version
  - OpenRTP

OpenRTM-aistをインストールするには、まず、以下のページに従い [homebrew](https://brew.sh/index_ja) をインストールします。

- [homebrew](https://brew.sh/index_ja)

さらに、以下のページに示す手順に従うことで OpenRTM-aist (C++, Python, Java) および OpenRTP ␈をインストールすることができます。

- [homebrew-openrtm](https://github.com/OpenRTM/homebrew-openrtm)

例えば、C++版であれば以下のように簡単にインストールすることができます。

```
 $ brew update
 $ brew tap openrtm/omniorb
 $ brew tap openrtm/openrtm
 $ brew install openrtm/openrtm-aist
 $ brew link openrtm-aist
 $ /usr/local/share/openrtm-1.2/components/c++/examples/ConsoleInComp
```


