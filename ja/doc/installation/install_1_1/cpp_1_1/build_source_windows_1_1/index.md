---
layout: page
title: ソースからのビルド (windows編)
---

<!-- Title: ソースからのビルド (Windows編) -->
OpenRTM-aist 本体に手を加えたうえで Windows 上で利用したい場合は、Windows 用ソースパッケージを自分でビルドするができます。
ここでは、ダウンロードページやリポジトリからソースを取得し Windows 上で OpenRTM-aist をビルドする方法を解説します。

Windows 上での OpenRTM-aist のビルドは、環境の整備やインストーラの作成など、Windows 上での様々な知識が必要となります。
本ドキュメントは、Windows 上でのプログラム開発やバッチファイル等の基本的な知識がある方を対象としています。

#contents

<!-- ------------------------------------------------------------ -->
## Windows 用ソースコード

Windows 用の OpenRTM-aist (C++版) ソースパッケージは Linux 用のソースとは別に配布されています。
ソースコードの内容は全く同じですが、以下の部分が異なっています。

- 文字コード (Windows: Shift-JIS、Linux: EUC)
- Visual Studio のソリューションを含む
- Visual C++ のプロジェクトファイルを含む
- msi インストーラ作成環境を含む

### ソースコードの構成

図に示すように、オリジナルは subversion リポジトリのソースコードで、そのソースコードから、Linux上で、

- Linux/Unix 用ソースコード配布パッケージ
- Windows 用ソースコード配布パッケージ

の2種類を作成する構成になっています。

<div align="center"><a href="openrtm_src_dist_ja.png"><img src="openrtm_src_dist_ja.png" width="70%;"></a></div>
<div align="center"><strong>OpenRTM-aist のソースの構成</strong></div>

リポジトリから取得した最新のソースコードを Windows で利用する場合は、一旦 Linux で Windows 用のソースコードを生成する必要があります。

<!-- ------------------------------------------------------------ -->
## ビルド環境

ビルドに必要な環境、ライブラリは以下の通りです。

- Visual C++
  - Visual C++ Express Edition でも利用可能です
- omniORB

### Visual C++/Visual Studio

Windows 用のバイナリをビルドするためには、Visual C++ 開発環境が必要です。
現在対応している Visual C++ は Visual C++ 2008、2010、2012、2013 です。
<!-- Visual C++ 2010 はプロジェクト変換ウィザードでビルドできる可能性がありますが、依存ライブラリである omniORB も自分でビルドする必要があるため、少々手間がかかります。 -->

Visual C++ Express Edition は Microsoft が無償で提供する C++ の開発環境で、MFC や ATL などは利用できませんが、Windows アプリケーション (Win32アプリケーション) を開発することができます。
OpenRTM-aist を利用したコンポーネント開発でも、MFC や ATLなどを利用しないコンポーネントは Visual C++ Express Edition のみで開発することができます。
下記リンクから ISO イメージをダウンロードしてインストールした上で、Microsoft Live ID を取得してライセンス(無料)を取得してください。

- [Visual Studio のダウンロード](https://www.visualstudio.com/ja/downloads/)
<!-- -[[Visual Studio 2008 Express Edition:http://www.microsoft.com/japan/msdn/vstudio/2008/product/express/offline.aspx]]: 2008 の DVDISO イメージをここからダウンロードできます。 -->


### omniORB

OpenRTM-aist のビルドには omniORB 4.1.7（2015/03/31現在）のライブリが必要です。
<!-- omniORB は以下のリンクから、ソースコードおよびバイナリをダウンロードできます。 -->
openrtm.org が提供するビルド済みバイナリパッケージを下記リンク先に用意してあります。
環境に合わせて適切なものをダウンロードし、適当な場所 (以下では C:\distribution\omniORB を仮定) に展開してください。

- [openrtm.org提供バイナリパッケージ](http://openrtm.org/pub/omniORB/win32/omniORB-4.1.7/)
<!-- が、openrtm.org が提供するビルド済みバイナリインストーラーが便利です。 -->

<!-- -[[omniORB official:http://omniorb.sourceforge.net/]] -->
<!-- --[[sourceforge download page:http://sourceforge.net/projects/omniorb/files/omniORB/omniORB-4.1.7/]] -->

<!-- --vc8 (Visual C++ 2005) 用とvc9 (Visual C++ 2008)用に分かれています。環境に合わせて適切なものをインストールしてください。 -->

<!-- omniORBを上記インストーラ以外の方法でインストールした場合には、後の -->
<!-- OpenRTM-aistのビルドおよび、自作コンポーネントのビルドの際に必要な環境 -->
<!-- 変数が設定されませんのでご注意ください。 -->

<!-- **** msi omniORBインストーラ -->

<!-- インストーラは以下の作業を行います。 -->

<!-- -デフォルトのインストールディレクトリはC:\Program Files\omniORB\<version_number> -->
<!-- -インストールディレクトリにソース、ヘッダ、スクリプト、LIB等をコピー -->
<!-- -環境変数 ''PATH'' に ''bin/x86_win32'' を追加 -->
<!-- -環境変数 ''OMNI_ROOT'' にインストールディレクトリをセット -->

<!-- なお、環境変数のアプリケーションへの通知はされませんので、環境変数の更 -->
<!-- 新を有効にするには再起動してください。または、「マイコンピュータ」→ -->
<!-- 「プロパティ」→「詳細設定」→「環境変数」から環境変数のどれかを選択し -->
<!-- 「編集」をクリックして編集ダイアログを表示させ、そのまま何も変更せずに -->
<!-- OKを押すことで、シェルへ環境変数の変数が通知され、そのシェルから新たに -->
<!-- 実行したアプリケーションでは変更された環境変数が有効になりますが、よく -->
<!-- わからなければ再起動したほうが無難です。) -->

#### 環境変数: OMNI_ROOT

<!-- 上記の msi インストーラー以外の方法でインストールした場合は環境変数 ''OMNI_ROOT'' を設定する必要があります。 -->
OMNI_ROOT に設定したディレクトリー以下は以下のような構造になっている必要があります。

```
<OMNI_ROOT>
  + bin
  |  + scripts
  |  + x86_win32
  + idl
  |  + COS
  + include
  |  + COS
  |  + omniORB4
  |  |  + internal
  |  + omnithread
  |  + omniVms
  + lib
  |  + python
  |  |  + omniidl
  |  |  + omniidl_be
  |  |     + cxx
  |  |        + dynskel
  |  |        + header
  |  |        + impl
  |  |        + skel
  |  + x86_win32
```

### WiX

<span style="color:red;">1.1.1-RELEASE 版ではソースに含まれているインストーラー作成コードのメンテナンスは行っておりません。</span>;

WiX (Windows Installer XML) は Windows の msi インストーラをコマンドラインベースのツール群で作成することを目指しているオープンソースのプロジェクトです。

- [WiX official](http://wixtoolset.org/)
- [WiX download page](http://wixtoolset.org/releases/)

OpenRTM-aist は Windows 用のインストーラーを WiX を利用して作成しています。
インストーラーまで作成する場合には、WiX を予めインストールしておいてください。

### Python

ビルドの途中でいくつかの Python スクリプトを利用するので Python 2.7 が必要になります。
以下のサイトから最新のものを取得しインストールしてください。

- [Python Official Website](https://www.python.org/)

インストーラーを起動すると、ウィザードで幾つか選択する部分がありますが、
デフォルトのままでインストールしてかまいません。


<!-- *** OpenCV -->
<!--  -->
<!-- Windows版OpenRTM-aistではOpenCVを利用したサンプルコンポーネントが含まれ -->
<!-- ていますのでOpenCVが必要となります。現在のところOpenCV 1.0のみ対応です。 -->
<!--  -->
<!-- -[[OpenCV win32 installer(sourceforge)>http://downloads.sourceforge.net/opencvlibrary/OpenCV_1.0.exe?modtime=1161287502&big_mirror=1]] -->
<!--  -->
<!-- ここからOpenCVのインストーラ OpenCV_1.0.exeをダウンロードします。 -->
<!-- OpenCV_1.0.exeを実行するとインストーラが起動するので指示に従ってインス -->
<!-- トールします。 -->
<!--  -->
<!-- *** boost -->
<!--  -->
<!-- 拡張モジュールのビルドにboostが必要です。 boostのインストール方法は２通りあります。 -->
<!--  -->
<!-- -インストーラによるバイナリパッケージ利用 -->
<!-- -ソースをビルドする -->
<!--  -->
<!-- インストーラの提供は、最新バージョンには追いついていないようです。ここでは、1.51版のインストーラを利用する方法と、 -->
<!-- 1.53版をソースからビルドする方法を紹介します。 -->
<!--  -->
<!-- **** インストーラによるバイナリパッケージ利用 -->
<!--  -->
<!-- 開発環境が VS2010(32bit) なので、下記のサイトからインストーラの最新版である「BoostPro 1.51.0 Installer (32-bit)」をダウンロードします。 -->
<!--  -->
<!-- -[[boost Windowsパッケージ:http://www.boostpro.com/download/]] -->
<!--  -->
<!-- インストーラを起動して下記のオプションを選択します。 -->
<!--  -->
<!-- #ref(boost_installer.png,70%,center,nolink) -->
<!-- CENTER:''boostインストーラ画面'' -->
<!--  -->
<!-- インストールが完了したら、バッチファイルの修正のパスを確認します。今回の場合は autobuild_vc10.bat を以下のように修正します。 -->
<!--  -->
<!-- @set BOOST_ROOT=C:\Program Files (x86)\boost\boost_1_51 -->
<!--  -->
<!-- 環境変数も定義します。 -->
<!--  -->
<!-- BOOST_ROOT		C:\Program Files (x86)\boost\boost_1_51 -->
<!--  -->
<!-- **** ソースをビルドする -->
<!--  -->
<!-- 公式サイトから、最新版である「boost_1_53_0.zip」をダウンロードし、解凍します。 -->
<!--  -->
<!-- -[[boost:http://www.boost.org/]] -->
<!-- -http://www.boost.org/ -->
<!--  -->
<!-- ここでは、C:\distribution\boost_1_53_0　に解凍したものとします。 -->
<!-- 最初に、コマンドプロンプトを起動してbootstrap.batコマンドを実行します。 -->
<!--  -->
<!-- C:\distribution\boost_1_53_0> bootstrap.bat -->
<!--  -->
<!-- 完了すると、「b2.exe」と「bjam.exe」が生成されています。bootstrap.batコマンドの出力メッセージに従い、b2コマンドでboostライブラリをビルドします。 -->
<!--  -->
<!-- b2コマンドのオプションについては関連ドキュメントをご覧下さい。ここでは以下の指定で、２回に分けてビルドします。 -->
<!--  -->
<!-- C:\distribution\boost_1_53_0> b2.exe link=static runtime-link=static,shared -->
<!-- C:\distribution\boost\boost_1_53_0> b2.exe link=shared runtime-link=shared -->
<!--  -->
<!-- ビルドが完了すると、ライブラリファイルは「C:\distribution\boost_1_53_0\stage\lib」に出力されます。このlibフォルダを丸ごと移動させて、 -->
<!-- 「C:\distribution\boost_1_53_0\lib」へ置いて下さい。 -->
<!-- バッチファイルのパスを以下のように修正します。 -->
<!--  -->
<!-- @set BOOST_ROOT=C:\distribution\boost_1_53_0 -->
<!--  -->
<!-- 環境変数も定義します。 -->
<!--  -->
<!-- BOOST_ROOT		C:\distribution\boost_1_53_0 -->
<!--  -->
<!-- 以上でインストールは完了です。 -->

## ソースパッケージの取得

まずソースコード OpenRTM-aist-1.1.1-win32.zip をダウンロードし、適当なディレクトリーに展開します。

- [OpenRTM-aist-1.1.1-win32.zip](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.1/OpenRTM-aist-1.1.1-win32.zip)


### バッチファイルの修正

build.bat の先頭に以下のような部分があります。これらが、それぞれ適切な値に設定されているかを確認してください。　<br>
ARCH、VC_VERSION の設定については、このバッチファイルに記述されている説明をご覧ください。

```
 set RTM_ROOT=%~dp0
 set COIL_ROOT=%RTM_ROOT%\coil
 set OMNI_ROOT=C:\distribution\omniORB-4.1.7-win64-vc12
 if not DEFINED ARCH       set ARCH=x86_64
 if not DEFINED VC_VERSION set VC_VERSION=12
 if not DEFINED PYTHON_DIR set PYTHON_DIR=C:\Python27_x64
```

<!-- また、そのままでは、RTSystemEditor の RCP パッケージがないためインストーラを -->
<!-- ビルドする途中でエラーとなります。以下の2種類の方法のうち一つを選択して -->
<!-- ください。 -->
<!--  -->
<!-- -installer/autowix.cmd を修正 -->
<!-- -openrtm.org配布のmsiインストーラでインストールされるRTSystemEditorをC:\distributionにコピー -->
<!--  -->
<!-- ****installer/autowix.cmd を修正 -->
<!--  -->
<!-- installer/autowix.cmd の初めの方にある RTSystemEditor に関する部分を以 -->
<!-- 下のように修正します。 -->
<!--  -->
<!-- @rem ------------------------------------------------------------ -->
<!-- @rem Generate RTSystemEditor wxs file -->
<!-- @rem -->
<!-- @rem RTSystemEditorRCP.exe should be under %RTSE_ROOT% -->
<!-- @rem -->
<!-- @rem ------------------------------------------------------------ -->
<!-- @rem if "x%RTSE_ROOT%" == "x" ( -->
<!-- @rem    echo Envrionment variable "RTSE_ROOT" is not set. Abort. -->
<!-- @rem    goto END -->
<!-- @rem ) -->
<!-- @rem if not exist "%RTSE_ROOT%\RTSystemEditorRCP.exe" ( -->
<!-- @rem    echo RTSystemEditorRCP.exe does not found. Abort -->
<!-- @rem    goto END -->
<!-- @rem ) -->
<!-- set INCLUDE_RTSE=NO -->
<!-- set INCLUDE_OPENRTP=NO -->
<!--  -->
<!-- ****RTSystemEditorをコピー -->
<!--  -->
<!-- openrtm.org で配布している Windows 用インストーラでOpenRTM-aistをインストールすると、デフォルトでは C:\Program Files\OpenRTP 以下に RTSystemEditor の RCP 版がインストールされます。また//は、msiからファイルを抽出ツールなどを使いRTSystemEditorを取り出します。これを、C:\distribution 以下にコピーします。 -->
<!--  -->
<!-- C:\distribution -->
<!-- + OpenRTP -->
<!-- + RTSystemEditor -->
<!-- + configuration -->
<!-- + NewProjectName -->
<!-- + plugins -->
<!-- + ... -->
<!--  -->
<!-- このような構造になっている必要があります。 -->

## ビルド

以上の準備が完了したら、ビルドを行います。build.bat をダブルクリックし、起動すれば自動でビルドが始まります。

<!-- また、ソリューションファイル(sln)からのビルドも可能です。 -->
<!-- OpenRTM-aist_vc8.sln (開発環境がVC2005の場合) あるいは -->
<!-- OpenRTM-aist_vc9.sln (開発環境がVC2008の場合) をダブルクリックし、ビル -->
<!-- ドを行ってください。 -->

## インストール
すべてが正しくビルドできたら次のことを行い、インストールを完了させます。

- **環境変数 RTM_ROOT を設定**: OpenRTM-aist のディレクトリーを環境変数 RTM_ROOT に設定してください。
- **DLL へのパスを通す**: DLL をパスの通った場所にコピーする、あるいは、環境変数 PATHに%RTM_ROOT%\bin を追加します。
- **環境変数 PATH の設定**: 環境変数 PATHに%RTM_ROOT%\binだけでなく%RTM_ROOT%\utils\rtc-templateも登録することをお勧めします。

以上で、OpenRTM-aist のインストールは終了です。
