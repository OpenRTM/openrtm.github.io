---
layout: page
title: ソースからのビルド (windows編)
---
<br>
<a>No English version available.
</a>

<!-- Title: ソースからのビルド (Windows編) -->
#contents

Windows 上でソースパッケージからインストールしたい場合、OpenRTM-aist-Python を自分でビルドする必要があります。

<!-- ------------------------------------------------------------ -->
## Windows 用ソースコード

Windows 用の OpenRTM-aist (Python版) ソースパッケージは Linux 用のソースとは別に配布されています。
ソースコードの内容は全く同じですが、以下の部分が異なっています。

- 文字コード (Windows: Shift-JIS、Linux: EUC)

### ソースコードの構成

オリジナルは subversion リポジトリのソースコードで、そのソースコードから、Linux 上では、

- Linux/Unix 用ソースコード配布パッケージ
- Windows 用ソースコード配布パッケージ

の2種類を、

Windows 上では、

- Windows 用ソースコード配布パッケージ

の1種類だけを作成する構成になっています。


<!-- ------------------------------------------------------------ -->
## ビルド環境

ビルドに必要な環境、ライブラリは以下の通りです。

- Python
- omniORBpy

### Python
Python 2.7 が必要です。以下のサイトから最新のものを取得しインストールしてください。

- [Python Official Website](https://www.python.org/) 

インストーラを起動すると、ウィザードで幾つか選択する部分がありますが、
デフォルトのままでインストールしてかまいません。


### omniORBpy

OpenRTM-aist-Python のビルドには omniORBpy のライブリが必要です。omniORBpy は以下のリンクから、ソースコードおよびバイナリを取得できます。
<!-- が、openrtm.org が提供するビルド済みバイナリインストーラが便利です。 -->

- [omniORB official](http://omniorb.sourceforge.net/)
  - [sourceforge download page](http://sourceforge.net/projects/omniorb/files/omniORBpy/)
<!-- -[[openrtm.org提供msiパッケージ:http://www.openrtm.org/pub/Windows/omniORB/]] -->
<!-- --omniORBpyのインストーラはPythonのバージョンによって分かれています。環境に合わせて適切なものをインストールしてください。 -->

ZIPファイルを展開すると、以下の様なディレクトリツリーが展開されるはずです。
それぞれのディレクトリー下のファイルを以下の指示通りに Python のディレクトリーに配置してください。
なお、omniORBpy のバージョンを x.y, Python のバージョンを X.Y として記述しています。

 + omniPRBpy-x.y
  + bin
    + x86_win32 -> exe, dllともに C:\PythonXY 直下へ
  + doc -> 削除してもよい
  + examples -> 削除してもよい
  + idl -> 削除してもよいが C:\PythonXY\Lib\site-packages\omniORB\idl 以下においておいてもよい
  + lib
    + python -> 以下のディレクトリとファイルを丸ごと C:\PythonXY\Lib\site-packages 直下へ
    + x86_win32 -> .pyd を C:\PythonXY\Lib\site-packages 直下へ

<!-- ------------------------------------------------------------ -->
## ソースパッケージの取得

まずソースコード OpenRTM-aist-Python-X.X.X.zip をダウンロードし、適当なディレクトリーに展開します。

- [OpenRTM-aist-Python-1.1.2](http://www.openrtm.org/pub/OpenRTM-aist/python/1.1.2/)
- [OpenRTM-aist-Python-1.1.0]()(No corresponding page available.)


## ビルド

コマンドプロンプトを起動し、先程ソースコードを展開したフォルダーに移動後、以下のコマンドにてビルドを行います。

```
 > OpenRTM-aist-Python-X.X.X
 > python setup.py build
```

## インストール
すべてが正しくビルドできたら、以下のコマンドにてインストールを完了させます。

```
 > python setup.py install
```

以上で、OpenRTM-aist のインストールは終了です。


