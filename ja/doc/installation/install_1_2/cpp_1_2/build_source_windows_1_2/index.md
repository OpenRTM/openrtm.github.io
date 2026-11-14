---
layout: page
title:  ソースからのビルド(windows編)
---

<!-- Title: ソースからのビルド(Windows編) -->
OpenRTM-aist本体に改修を加えてWindows上利用したい場合は、OpenRTM-aist本体のWindows用ソースパッケージを自分でビルドできます。 ここでは、ダウンロードページやリポジトリからソースコードを取得しWindows環境でOpenRTM-aistをビルドする方法を説明します。

Windows環境でのOpenRTM-aistのビルドにおいては、ビルド環境の構築やインストーラの作成など、Windows環境上でのソフトウエア開発についてのさまざまな知識が必要です。 以下の説明では、Windows環境上のプログラム開発やバッチファイル作成などの基本的な知識があることを前提にしています。

#contents

<!-- ------------------------------------------------------------ -->
## Windows用ソースコード

Windows用のOpenRTM-aist(C++版)ソースパッケージはLinux 用のソースパッケージとは別個に配布されています。 ソースコードの基本的内容は同じですが、ビルド環境に依存するファイルは異なっています(例えばWindows環境におけるVisual StudioのプロジェクトファイルはWindows用ソースパッケージの中にしか存在しません)。

### ソースパッケージの生成

Windows用ソースコードのパッケージは
下記に示すリンクより入手できますが、最新の開発中のソースコードを入手する場合はGitHubのOpenRTM/OpenRTM-aist projectより入手する必要があり、図に示すようにLinux上で、

- Linux/Unix用ソースコード配布パッケージ
- Windows用ソースコード配布パッケージ

を作るようになっています。

<div align="center"><a href="src-conversion_ja.png"><img src="src-conversion_ja.png" width="70%;"></a></div>
<div align="center"><strong>OpenRTM-aist のソースパッケージの生成</strong></div>


<!-- ------------------------------------------------------------ -->
## ビルド環境

ビルドに必要な環境、ライブラリは以下の通りです。

- Visual C++/Visual Studio
- omniORB

#### Visual C++/Visual Studio
Windows 用のバイナリをビルドするためには、Visual Studio(C++)開発環境が必要です。
現在対応している Visual Studio は Visual Studio 2010、2012、2013、2015、2017、2019 です。(現状では2019のビルド対応はまだできていません。)

Visual Studio CommunityはMicrosoftが無償で提供する統合開発環境で、C++、C#、F#、Java、Pythonなどいろいろな言語を用いたソフトウエア開発に対応しています。
Community版は有償のProfessional版とほぼ同等の機能ですが、個人開発者、大学関係者、非営利団体従事者、オープンソース開発者、および、開発者5名以下の営利企業でしか使用できません。ライセンス条件の詳細についてはマイクロソフト社のドキュメントを参照してください。

以下よりVisual Studio 2019は入手できます。

- [Visual Studioのインストール手順]({{ site.baseurl }}/ja/doc/installation/install_1_2/cpp_1_2/install_windows_1_2/visual_studio_1_2/visual_studio_2022)

なお、Visual Studio 2017をインストールする場合は"C++によるデスクトップ開発"を選択し、さらに"インストール詳細"のところで"Windows 8.1 SDK と UCRT SDK"を選択してインストールをおこなってください。

### omniORB

OpenRTM-aistのビルドにはomniORB 4.2.3(2019/05/17現在)のライブラリが必要です。
openrtm.org が提供するビルド済みバイナリパッケージを下記リンク先に用意してあります。
環境に合わせて適切なものをダウンロードし、適当な場所(以下の説明ではC:\workspace\omniORBとしています)に展開してください。

- [openrtm.org提供バイナリパッケージ](http://openrtm.org/pub/omniORB/win32/)


#### 環境変数: OMNI_ROOT
OMNI_ROOT に設定したディレクトリ以下は以下のような構造になっている必要があります。

```
 <OMNI_ROOT>
  + bin
    + scripts
    + x86_win32
  + idl
    + COS
  + include
    + COS
    + omniORB4
    + internal
    + omnithread
    + omniVms
  + lib
    + python
    + omniidl
    + omniidl_be
    + cxx
    + dynskel
    + header
    + impl
    + skel
    + x86_win32
  + include
    + COS
    + omniORB4
    + omnithread
    + omniVms
```

### OpenSSL

OpenRTM-aistのビルドにはOpenSSL 1.1.0(2019/05/17現在)のライブラリが必要です。
openrtm.orgが提供するビルド済みバイナリパッケージを下記リンク先に用意してあります。
環境に合わせて適切なものをダウンロードし、適当な場所 (以下の説明ではC:\workspace\OpenSSLとしています)に展開してください。

- [openrtm.org提供バイナリパッケージ](https://openrtm.org/pub/OpenSSL/)

#### 環境変数: SSL_ROOT
SSL_ROOT に設定したディレクトリ以下は以下のような構造になっている必要があります。

```
 <SSL_ROOT>
  + bin
    + scripts
    + x86_win32
  + lib
    + engines-1_1
  + include
    + openssl
```

### Python
ビルドの途中でいくつかのPythonスクリプトを利用するので Python 2.7か3.6、または3.7 が必要です。(現状2.7が必要で、3.7ではエラーが起きます)
以下のサイトから最新のバージョンを取得しインストールしてください。

- [Python Official Website](https://www.python.org/)

インストーラーを起動すると、そのインストール過程で選択項目がでてきますが、デフォルトの項目を選択してインストールしてください。(デフォルト以外の選択も可能ですが、その場合は十分な理解の元で選択してください。)

## ソースパッケージの取得

まずソースコード OpenRTM-aist-1.2.X-win32.zip をダウンロードし、適当なディレクトリに展開します。

- [OpenRTM-aist 1.2.0](https://github.com/OpenRTM/OpenRTM-aist/releases/tag/v1.2.0)


## バッチファイルの修正

build.batを実行するとビルドが始まりますが、その前にバッチファイルの環境変数"OMNI_ROOT**、**SSL_ROOT''をする部分を環境に合わせて変更してください。

```
 set OMNI_ROOT=C:\workspace\omniORB-4.2.3-win64-vc141
 set SSL_ROOT=C:\workspace\OpenSSL\build
```

さらに、以下の環境変数も環境にあわせて設定するようにパッチファイル内に記述してください。

```
 set VC_VERSION=141  
 set ARCH=x86_64
 set PYTHON_DIR=C:\python27
 set OMNI_VERSION=4.2.3
 set OMNITHREAD_VERSION=4.1
```

上記の設定値は64ビット版OpenRTM-aistの設定用でVisual Studio 2017 とPython 2.7、OmniORB 4.2.3を使った場合の例です。
ここで、VC_VERSIONは対応するVisual C++のバージョンを指定します。(以下を参照してください。）

<table class="table-alt">
  <tr>
    <td>Visual Studio 2010</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Visual Studio 2012</td>
    <td>11</td>
  </tr>
  <tr>
    <td>Visual Studio 2013</td>
    <td>12</td>
  </tr>
  <tr>
    <td>Visual Studio 2015</td>
    <td>14</td>
  </tr>
  <tr>
    <td>Visual Studio 2017</td>
    <td>141</td>
  </tr>
  <tr>
    <td>Visual Stuido 2019</td>
    <td>142</td>
  </tr>
</table>

ARCHには32bitバイナリを作成する場合はx86、64bitバイナリを作成する場合はx86_64を指定してください。
PYTHON_DIRにはPythonをインストールしたパスを指定してください。

OMNI_VERSION、OMNITHREAD_VERSIONには対応するomniORB、omniThreadのバージョンを設定してください。OmniThreadのバージョンはエキスプローラでomnithreadXXXX.dllのファイルを右クリックしプロパティを選び、詳細タブをクリックするとファイルバージョンとして確認できます。そのうち最初ピリオドの右側の数字は次のピリオドの前までの数字を設定してください。(例えば4.1.24.1.0と表示されたら、4.1としてください。)

またCommunity版以外のVisual Studioを使用する場合は前もってvcvarsall.batを実行する必要があります。

Visual Studio 2017で、64ビットのインテルないしはAMDプロセッサ用のコードを作成する場合は

```
 call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
```

と実行してください。

## ビルド
以上の準備が完了したら、ビルドを行います。build.batを実行すれば自動でビルドが始まります。

## インストール
すべてが正しくビルドできたら次のことを行い、インストールを完了させます。

- **環境変数RTM_ROOTを設定**: ビルド後に作成されたOpenRTM-aistのファイルが置かれたディレクトリを環境変数RTM_ROOTに設定してください。
- **DLL へのパスを通す**: DLL をパスの通った場所にコピーするか、環境変数 PATHに%RTM_ROOT%\bin を追加します。


以上で、OpenRTM-aistのインストールは終了です。

