---
layout: page
title: ソースからのビルド(linux編)
---

<!-- Title: ソースからのビルド(Linux編) -->
#contents

Linux上でソースパッケージからインストールしたい場合、OpenRTM-aist-Pythonを自分でビルドする必要があります。以下にUbuntu 18.04でのビルド作業の手順を説明します。

## 対応 OS およびディストリビューション 
OpenRTM-aist-Pythonは下記のOSおよびLinuxディストリビューションで動作することが確認されています。
- Ubuntu
- Debian(対応するOpenRTM-aistのバージョンに制限あり)
- Fedora(対応するOpenRTM-aistのバージョンに制限あり)

上記以外の環境でも一般的なLinux/UNIX環境であれば、ビルドできる可能性があります。

## 依存ライブラリ
OpenRTM-aist-Python-1.2.1のインストールには下記の開発環境およびライブラリが必要です。
- python: ビルドツールを利用するために必要
- omniORBpy: OpenRTM-aistのビルド(IDLコンパイル)に必要

それぞれのソフトウエアのドキュメントに従いインストールを行ってください。これらのパッケージが、標準のディレクトリ(/usr、/usr/lib/ など)下にインストールされていると、以降のOpenRTM-aist-Pythonのビルド作業を比較的簡単に行うことができます。

Ubuntu, DebianではomniORB関連のものは以下のコマンドでインストールできます。
```
 sudo apt-get install python-omniorb-omg omniidl-python omniorb-nameserver
```

## ソースのダウンロード
OpenRTM-aist-Pythonのソースをダウンロードします。
- https://github.com/OpenRTM/OpenRTM-aist-Python/releases/tag/v1.2.1

## ソースコードの展開 
まずソースコードパッケージOpenRTM-aist-Python-1.2.1.tar.gzを適当なディレクトリに展開します。
```
 $ tar xvzf OpenRTM-aist-Python-X.X.X.tar.gz
 $ cd OpenRTM-aist-Python-X.X.X
```

## ビルド 
OpenRTM-aist-Pythonはパッケージのビルドにdistutilsモジュールを使用しています。
ビルドの仕方は、他のdistutilsを使用したパッケージと同様に行います。
```
 $ python setup.py build [options]
```

[options]で使用可能なオプションは
```
 $ python setup.py --help
```

で参照してください。

## インストール
ビルド が正常に終了したら、Pythonモジュール、ユーティリティコマンド群をインストールします。
```
 $ sudo python setup.py install
```

以上で、ソースコードからのビルドおよびインストールは終了です。

