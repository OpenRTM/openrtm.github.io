---
layout: page
title: "choreonoid用openrtm連携プラグイン python版 インストール手順"
---

#contents

## 動作環境
動作環境は以下の通りです。

- Windows 8.1
- Windows 10
- Ubuntu 14.04
- Ubuntu 16.04

Windowsの場合はビルド済みバイナリを配布してあります。


## インストール手順(Windows)

### Python

Python 2.7(**64bit**)をインストールしてください。

- [Python 2.7.14](https://www.python.org/downloads/release/python-2714/)

### Choreonoid

ビルド済みChoreonoid+OpenRTM連携プラグインは以下からダウンロードできます。

- [Choreonoid+OpenRTM-Python-Plugin.zip](https://drive.google.com/a/nobu777.net/uc?authuser=0&id=1EA9LEduA1mVAoPbyL4IFQ5k8L61TxQux&export=download)


このファイルを[Lhaplus](https://forest.watch.impress.co.jp/library/software/lhaplus/)等で適当な場所に展開すればインストール完了です。

### ソースコードからビルドする場合
何らかの事情によりソースコードからビルドせざる得ない場合は、以下のページの手順でビルドしてください。

- [インストール手順(Windows、ソースからビルド)](https://github.com/Nobu19800/OpenRTMPythonPlugin/wiki/%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%89%8B%E9%A0%86(Windows))

## インストール手順(Ubuntu)

### ダウンロード

Choreonoidのインストール手順については[Choreonoid ホームページ](http://choreonoid.org/ja/manuals/latest/install/build-ubuntu.html)に詳しく記載されているようなのですが、一応こちらでも説明します。

Choreonoidのソースコードですが、以下の理由により独自の変更を加えてあります。


- OpenRTM連携プラグインのRTシステムエディタ上でRTCをダブルクリックした際に専用Pythonエディタを開く機能を追加するための変更
- 2017年7月時点でWindowsで動作しなかったため一部変更
- Pythonでライトを操作するための関数追加


このため、オリジナルのChoreonoidではなくフォークしたものをクローンしてください。

```
 git clone https://github.com/Nobu19800/choreonoid.git
```

gitをインストールしていない場合は以下のコマンドを入力してください。

```
 sudo apt-get install git
```


### インストール
#### 依存ライブラリ
Choreonoidには必要ライブラリをインストールするスクリプトが付属しているようなので、このスクリプトを起動してください。

```
 cd choreonoid
 sh misc/script/install-requisites-ubuntu-14.04.sh
```

#### OpenRTM-aist

```
 wget http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-aist/build/pkg_install_ubuntu.sh
```
sudo sh pkg_install_ubuntu.sh

#### OpenRTM-aist-Python

以下のコマンドを入力してください。

```
 wget http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_2/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh
 sudo sh pkg_install_python_ubuntu.sh
```


#### Choreonoid

```
 cd sample
 git clone https://github.com/Nobu19800/OpenRTMPythonPlugin.git
 cd ..
 mkdir build
 cd build
 cmake .. -DENABLE_PYTHON=ON -DBUILD_PYTHON_PLUGIN=ON -DBUILD_OPENRTM_PYTHON_PLUGIN=ON
 make
 sudo make install
```

cmakeコマンドのオプションを変更してビルドしてください。

```
 cmake .. -DENABLE_PYTHON=ON -DBUILD_PYTHON_PLUGIN=ON -DBUILD_OPENRTM_PYTHON_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_OPENRTM_PLUGIN=ON
```


### 動作確認に必要なソフトウェアのインストール

動作確認のためにゲームパッドのRTCを使用しますが、このRTCの動作にはPySDL2がインストールされている必要があります。

動作確認用のRTCに必要というだけなので、次ページの動作確認を行わない場合はインストールの必要はありません。

以下のコマンドを入力してください。

```
 wget https://bitbucket.org/marcusva/py-sdl2/downloads/PySDL2-0.9.5.tar.gz
 tar xf PySDL2-0.9.5.tar.gz
 cd PySDL2-0.9.5
 sudo python setup.py install
```

さらにSDL2のインストールが必要なので、以下のコマンドでインストールしてください。

```
 sudo apt-get install libsdl2-2.0-0 libsdl2-image-2.0-0
```

これで準備完了です。

### 追記
choreonoidのsampleフォルダにOpenRTMPythonPluginのソースコードを入れる必要があります。

```
 cd sample
 git clone https://github.com/Nobu19800/OpenRTMPythonPlugin.git
```


