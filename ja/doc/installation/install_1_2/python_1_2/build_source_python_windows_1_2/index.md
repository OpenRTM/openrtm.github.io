---
layout: page
title: ソースからのビルド(windows編)
---

<!-- Title: ソースからのビルド(Windows編) -->
#contents

Windows上でソースパッケージからインストールしたい場合、OpenRTM-aist-Pythonを自分でビルドする必要があります。

## ビルド環境
- Python
- omniORBpy
- Doxgen

が必要です。以下に入手方法を説明しますのでインストールしてください。

### Python
Python 2.7(もしくは3.6、3.7)が必要です。以下のサイトから最新のものを取得しインストールしてください。

- [Python Official Website](https://www.python.org/)

以降の説明では、Pythonのインストールに際して以下の設定が必要です。（その他はインストーラのデフォルト設定です。)

- インストール先をC:\Python**'X.Y**'に設定。
  - **'X.Y**'は2.7か3.6か3.7、例:C:¥Python2.7など。
- Python3.7ではインストール時に[Customize Installation]を選択。
- コマンドサーチパス(環境変数PATHに設定されるパス)に上記ディレクトリが含まれていること。
  - 3.7ではインストール中に[Add Python to environmental variable]にチェックを入れればインストーラが設定します
  - その他の場合は手動で設定する必要があります。

### omniORBpy

OpenRTM-aist-PythonのビルドにはomniORBpyのライブリが必要です。omniORBpyは以下のリンクから、必要なファイルを入手できます。

- [OpenRTM.orgサイト](https://openrtm.org/pub/omniORB/win32/)

また、公式サイトからはソースが入手できます。
- [omniORB official](http://omniorb.sourceforge.net/)
  - [sourceforge download page](http://sourceforge.net/projects/omniorb/files/omniORBpy/)

openrtm.orgのサイトのファイルは、特別な理由がない限りは最新版(現時点では4.2.3)を使用することを推奨します。また、複数のファイルがあり、そのファイル名の意味は以下になります。説明にあわせて使用するファイルを選択してください。

ファイル名の書式は、以下のフォーマットになっています。

omniORB-**'x.y.z**'-{win32|x64}-{vc100|vc110|vc120|vc140}-{py27|py36|py37}.zip

ここで、
** **'x.y.z**'**: |omniORBのバージョン、例えば4.2.3

: win32|32ビット版のPythonを使う場合
: x64|64ビット版のPythonを使う場合

: vc100| C++環境を使う場合で、Visual Studio 2010の場合
: vc110| C++環境を使う場合で、Visual Studio 2012の場合
** vc120|**:  C++環境を使う場合で、Visual Studio 2013の場合
: vc140| C++環境を使う場合で、Visual Studio 2015/2017/2019の場合

: py27| Python 2.7を使う場合
: py36| Python 3.6を使う場合
: py37| Python 3.7を使う場合

omniORB 4.2.3を64bitのPython 3.7の環境で使用する場合、omniORB-4.2.3-x64-vc140-py37.zipをダウンロードします。

#### omniORBのファイルのインストールの仕方

ダウンロードしたZIPファイルを展開すると、以下の様なディレクトリツリーが展開されます。それぞれのディレクトリ下のファイルを以下の指示通りに Python のディレクトリにコピーしてください。

なお、omniORBpyのバージョンを**'x.y**'、Pythonのバージョンを**'X.Y**'として記述しています。

 + omniORBpy-x.y
  + bin
    + x86_win32 -> exe、dllともにC:\PythonX.Y直下へ
  + doc -> 削除してもよい
  + examples -> 削除してもよい
  + idl -> 削除してもよいがC:\PythonX.Y\Lib\site-packages\omniORB\idl以下においておいてもよい
  + lib
    + python -> 以下のディレクトリとファイルを丸ごとC:\PythonX.Y\Lib\site-packages直下へ
    + x86_win32 -> .pydをC:\PythonX.Y\Lib\site-packages直下へ

### Doxygen

- [Doxygen](http://www.doxygen.nl/download.html)

のWebページからWindows版のバイナリ実行形式ファイルをダウンロードして実行してインストールしてください。

## ソースパッケージの取得

まず下記リンクよりソースコードファイルOpenRTM-aist-Python-1.2.x.zipをダウンロードし、適当なディレクトリに展開します。

- [OpenRTM-aist-Python-1.2.1](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/tag/v1.2.1/)

## ビルド

コマンドプロンプトを起動し、先程ソースコードを展開したフォルダーに移動後、以下のコマンドにてビルドを行います。

```
  python setup.py build
```

## インストール
すべてが正しくビルドできたら、以下のコマンドにてインストールを完了させます。

```
  python setup.py install
```

以上で、OpenRTM-aist-pythonのインストールは終了です。



