---
layout: page
title: ソースからのビルド (linux編)
---

<!-- Title: ソースからのビルド (Linux編) -->
#contents

パッケージが用意されていない UNIX 環境や、クロス開発環境、OpenRTM-aist-Python 本体のソースを変更して利用したい場合には、ソースからビルドすることができます。

## 配布ソースのビルド

OpenRTM-aist (Python版) は Python の distutils モジュール を利用したビルド環境を提供しているため、様々な環境で容易にビルドできます。

### 対応 OS およびディストリビューション 
OpenRTM-aist-Python は下記の OS および Linux ディストリビューションで動作することが確認されています。

- FreeBSD
- Vine Linux
- Fedora
- Debian
- Ubuntu

これ以外の環境でも、一般的な Linux/UNIX 環境であれば、ビルドできる可能性があります。

### 依存ライブラリ

OpenRTM-aist-Python-1.0.0 のインストールには下記の開発環境およびライブラリが必要です。

- python: ビルドツールを利用するために必要
- omniORBpy: OpenRTM-aist のビルド (IDL コンパイル) に必要

それぞれのライブラリ等のドキュメントに従いインストールを行ってください。
これらのパッケージが、標準のディレクトリー(/usr、/usr/lib/ 等)下にインストールされていると、以降の OpenRTM-aist-Python のビルド作業を比較的簡単に行うことができます。

### ソースのダウンロード

OpenRTM-aist-Python のソースをダウンロードします。

- http://openrtm.org/pub/OpenRTM-aist/python/


### ソースコードの展開 

まずソースコード OpenRTM-aist-Python-X.X.X.tar.gz を適当なディレクトリに展開します。

```
 $ tar xvzf OpenRTM-aist-Python-X.X.X.tar.gz
 $ cd OpenRTM-aist-Python-X.X.X
```

### ビルド 

OpenRTM-aist-Python はパッケージのビルドに distutils モジュール を使用しています。
ビルドの仕方は、他の distutils を使用したパッケージと同様に行います。

```
 $ python setup.py build [options]
```

[options]で使用可能なオプションは

```
 $ python setup.py --help
```

で参照して下さい。

### インストール

ビルド が正常に終了したら、Python モジュール、ユーティリティコマンド群をインストールします。

```
 $  su
 # python setup.py install
```

以上で、ソースコードからのビルドおよびインストールは終了です。


## リポジトリのソースのビルド

OpenRTM-aist は開発に利用している subversion リポジトリを一般に公開しています。
リポジトリからチェックアウトしたソースコードからビルドを行うこともできます。

### ソースのチェックアウト

ソースをリポジトリからチェックアウトします。

```
 $ svn co http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python
 A    OpenRTM-aist-Python/OpenRTM_aist
 A    OpenRTM-aist-Python/OpenRTM_aist/CorbaPort.py
 A    OpenRTM-aist-Python/OpenRTM_aist/__init__.py
 A    OpenRTM-aist-Python/OpenRTM_aist/Guard.py
 A    OpenRTM-aist-Python/OpenRTM_aist/RTM_IDL
 A    OpenRTM-aist-Python/OpenRTM_aist/RTM_IDL/RTC.idl
 A    OpenRTM-aist-Python/OpenRTM_aist/RTM_IDL/Manager.idl
 中略
 A    OpenRTM-aist-Python/installer/WixUI_es-es.wxl
 A    OpenRTM-aist-Python/installer/WixUI_fr-fr.wxl
 A    OpenRTM-aist-Python/installer/WixUI_de-de.wxl
 A    OpenRTM-aist-Python/installer/WixUI_cs-cz.wxl
 A    OpenRTM-aist-Python/installer/WixUI_da-dk.wxl
 リビジョン 349 をチェックアウトしました。
```

### ビルド

チェックアウトすると、OpenRTM-aist-Python というディレクトリーができているはずですので、そのディレクトリーに入ります。

```
 $ ls 
 OpenRTM-aist-Python
 $ cd OpenRTM-aist-Python
 $ ls
 MANIFEST.in           OpenRTM-aist.pth  README      setup.py
 MANIFEST_examples.in  OpenRTM_aist/     installer/
```


setup.py を使用してビルドします。

```
 $ python setup.py build
```


### パッケージの作成

**python setup.py sdist** を行うことで openrtm.org で配布しているようなソースのパッケージを作成することもできます。
ただし、パッケージの作成を行うには、doxygen や latex、qkc等、さらに追加のコマンドが必要となります。

```
 $ python setup.py sdist
```

```
 $ ls -l dist/
```
 -rw-rw-r-- 1 openrtm openrtm 2721202  2月 24 16:43 OpenRTM-aist-Python-1.1.0.tar.gz
 -rw-rw-r-- 1 openrtm openrtm 4686452  2月 24 16:43 OpenRTM-aist-Python-1.1.0.zip


生成されたソースパッケージはそれぞれ以下の通りです。

- OpenRTM-aist-Python-1.1.0.tar.gz: 汎用ソース (gzip 圧縮)
- OpenRTM-aist-Python-1.1.0.zip: Windows 用ソース
<!-- -OpenRTM-aist-Python-example-1.0.0.tar.gz: サンプル用ソース (gzip 圧縮) -->


