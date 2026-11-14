---
layout: page
title: openrtm-aist c++ 1.2.0-release
---

<!-- Title: OpenRTM-aist C++ 1.2.0-RELEASE -->
<div align="right"><a href="cpp_logo.png"><img src="cpp_logo.png" width="15%;" align="right"></a></div>
#contents(4)

<!-- ** &color(blue){まだリリースしておりません。準備中です。もうしばらくお待ち下さい。}; -->

<br>
インストール手順については以下のページを参照してください。

- [OpenRTM-aist (C++版) 1.2系のインストール]({{ site.baseurl }}/ja/doc/installation/install_1_2/cpp_1_2)

## パッケージ
### Windows インストーラー

#### 32bit用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist、C++、Python、<br>Java版、および OpenRTP、<br>rtshell(4.2.2) 含む)<br>(Visual Studio 2008、2010、<br>2012、2013、2015、2017 共通)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86.msi">OpenRTM-aist-1.2.0-RELEASE_x86.msi</a> <br>MD5:abef26d7b3fa89f1ed8c7b96ea1a452b</td>
    <td>2019/03/15</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi">python-2.7.16.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe">python-3.6.8.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe">python-3.7.3.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.14.2/cmake-3.14.2-win32-x86.msi">cmake-3.14.2-win32-x86.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="http://doxygen.nl/files/doxygen-1.8.15-setup.exe">doxygen-1.8.15-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python は、"2.7"  "3.6"  "3.7" のいずれかのバージョンをインストールして下さい。</span>;
- <span style="color:red;">※ 古い rtshell は事前に削除しておいてください。ただし、OpenRTM-aist 1.1.2版をmsiでインストールしている場合は対応不要です。</span>;

#### 64bit用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist、C++、Python、<br>Java版、および OpenRTP、<br> rtshell (4.2.2) 含む)<br>(Visual Studio 2010、2012、<br> 2013、2015、2017 共通)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86_64.msi">OpenRTM-aist-1.2.0-RELEASE_x86_64.msi</a> <br>MD5:7a2670eb70a3e53abc819fa722be690a</td>
    <td>2019/03/15</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi">python-2.7.16.amd64.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe">python-3.6.8-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe">python-3.7.3-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.14.2/cmake-3.14.2-win64-x64.msi">cmake-3.14.2-win64-x64.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="http://doxygen.nl/files/doxygen-1.8.15-setup.exe">doxygen-1.8.15-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python は、"2.7"  "3.6"  "3.7" のいずれかのバージョンをインストールして下さい。</span>;
- <span style="color:red;">※ 古い rtshell は事前に削除しておいてください。ただし、OpenRTM-aist 1.1.2版をmsiでインストールしている場合は対応不要です。</span>;

インストールについては、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/lets_start121) のページで手順を紹介しています。<br>

#### （重要なお知らせ）OpenRTM-aistインストール後の設定

- Pythonのインストール先によっては、rtshellのexeコマンド実行時にエラーとなることが判明しました
- 下記手順で更新して頂ければ改善します

```
  pip uninstall rtshell rtctree rtsprofile
  pip install rtshell-aist
```

#### Visual Studio のバージョン指定

インストールされている Visual Studio のバージョンに合わせて、システム環境変数 **RTM_VC_VERSION** を設定しています。
インストール後に変更する場合は、GUI ツールを使って設定することができます。使い方は [VCVerChanger]({{ site.baseurl }}/ja/content/vc_version_changer) のページで解説しています。
<br>

<table class="table-alt">
  <tr>
    <th>Visual Studio のバージョン</th>
    <th>システム環境変数 RTM_VC_VERSION の指定値</th>
    <th></th>
  </tr>
  <tr>
    <td>2008</td>
    <td>vc9</td>
    <td>32bit用インストーラーのみ</td>
  </tr>
  <tr>
    <td>2010</td>
    <td>vc10</td>
    <td></td>
  </tr>
  <tr>
    <td>2012</td>
    <td>vc11</td>
    <td></td>
  </tr>
  <tr>
    <td>2013</td>
    <td>vc12</td>
    <td></td>
  </tr>
  <tr>
    <td>2015</td>
    <td>vc14</td>
    <td></td>
  </tr>
  <tr>
    <td>2017</td>
    <td>vc141</td>
    <td>初期設定</td>
  </tr>
</table>

- <span style="color:red;">※ インストール後、Visual Studio のバージョンを変更しない場合でも、一度 [VCVerChanger]({{ site.baseurl }}/ja/content/vc_version_changer) で システム環境変数の設定を確認して下さい。不要なパスが残っていた場合はこれを削除します。</span>;
<br>
<!-- **** 手動での「 RTM_VC_VERSION 」設定手順 -->
<!--  -->
<!-- システム環境変数の設定画面は、以下の手順で開くことができます。 -->
<!--  -->
<!-- |Windows7|スタートボタン ＞ コンピュータを右クリック ＞ プロパティ ＞ システムの詳細設定|&ref(system_env1.png,60%,center);| -->
<!-- |Windows8.1|デスクトップ画面を表示 ＞ Windows ボタンを右クリック ＞ システム ＞ システムの詳細設定|同上| -->
<!-- |Windows10|検索窓で「システム環境変数」と入力 ＞ システム環境変数の編集をクリック|&ref(system_env2.png,60%,center);| -->
<!--  -->
<!-- システムのプロパティ画面で、「環境変数」をクリックします。 -->
<!--  -->
<!-- #ref(system_env3.png,70%,center) -->
<!--  -->
<!-- 「RTM_VC_VERSION」を編集します。 -->
<!--  -->
<!-- CENTER:&ref(system_env4.png,70%);  &ref(system_env5.png,70%); -->

<!-- **** ツールを使った「 RTM_VC_VERSION 」設定手順 -->
<!--  -->
<!-- GUI ツールを使って設定することができます。使い方は [[VCVerChanger:/ja/node/6136]] のページで解説しています。 -->
<!-- &br; -->

&aname(vc2013_install);
#### Visual Studio のダウンロード・インストール

Microsoftのダウンロードページから Visual Studio Community 2017 をダウンロードできます。
- [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/)

インストールについては、[Visual Studio 2017 インストール方法]()（リンク切れです） のページで手順を紹介しています。<br>

Microsoftのダウンロードページでは、Visual Studio の最新バージョンしかダウンロードできません。<br>
サポート対象の別バージョンの Visual Studio をダウンロード・インストールしたい方は、無償プログラムの <br>
「Visual Studio Dev Essential」への登録が必要です。下記サイトの手順に従って登録してください。
- [https://blogs.msdn.microsoft.com/ayatokura/2016/12/20/vsdevessential/](https://blogs.msdn.microsoft.com/ayatokura/2016/12/20/vsdevessential/)

vc2013 のインストール方法を紹介します。

- Visual Studio Dev Essential 画面を開き、左端にある「Visual sutdio Community」の Download をクリックします
- 検索窓に「Visual Studio Express 2013 for Windows Desktop with Update 5」と入力して検索してください
- インストーラーのデフォルト言語は English となっていますが、Japanese を選択可能です
- EXE の web インストーラーをダウンロードしてインストールしてください




##### インストールの確認

講習会前などには、Visual  C++のプロジェクトが作成できるかを確認をお勧めします。

まずはVisual Studioを起動し、「ファイル」→「新規作成」→「プロジェクト」をクリックしてください。<br>
テンプレートに**Visual C++**を選択して、**空のプロジェクト**を選択してください。

<br>

<div align="center"><a href="vc2017.png"><img src="vc2017.png" width="70%;"></a></div>
<br>


プロジェクト名を入力後にOKをクリックするとVisual C++のプロジェクトが生成されます。


**Visual C++**を選択できない場合は、[Visual Studio 2017 インストール方法]()（リンク切れです） の手順に従って「C++によるデスクトップ開発」をインストールしてください。


またVisual Studio 2017以外を使用の場合にも、念のためにVisual C++のプロジェクトが作成できるかの確認することをお勧めします。


#### C++版の旧バージョンランタイム利用方法

旧バージョンのランタイムは、OpenRTM-aist ディレクトリー下に、1.0.0（32bit用のみ）、1.1.0、1.1.1 としてインストールされます。
**RTM_BASE**というシステム環境変数を使いパスを通してお使いください。

例）1.1.1版 vc12 のランタイムのパスは、「RTM_BASE1.1.1\vc12\bin」で指定できます。

#### Windows10 等の高解像度(HiDPI)モードで OpenRTP/RTSystemEditor が縮小表示される場合の対処方法

Windows10などの高解像度モードを利用すると、Eclipse のアイコンなどが縮小表示される場合があります。
以下のFAQで解決方法を説明しています。
<br>
[Windows10 などで、高解像度モードのときにアイコン等が小さくなる]({{ site.baseurl }}/ja/doc/faq/faq_rtp_tools#toc1)


#### インストール環境の設定を確認する方法

windows_installer_test.bat スクリプトで確認することができます。使い方は下記ページで解説しています。
<br>
[windows_installer_test.batの利用方法]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/windows_install_test_bat)


<!-- - 1.1.2版を「標準」インストールすると、C++版だけでなく、Python版、Java版、rtshell もインストールされますので、 -->
<!-- これらの古いバージョンをインストールされている場合は、あらかじめ全てアンインストールしてください。 -->

<br>
### Linux パッケージ

<!-- Linux パッケージは順次提供される予定です。ソースからのビルドの仕方は以下を参考にしてください。 -->

現在のところ、以下のディストリビューション・バージョンでパッケージを提供しています。<br>
以下で配布しているインストールスクリプトを利用すれば、必要なパッケージを一括でインストールすることができます。


<table class="table-alt">
  <tr>
    <th>ディストリビューション・バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Ubuntu 14.04 (trusty) i386/amd64 <br>  Ubuntu 16.04 (xenial) i386/amd64 <br> Ubuntu 18.04 (bionic) amd64 <br> Ubuntu 18.10 (cosmic) amd64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian  8.0  (jessie) i386/amd64 <br> Debian  9.0  (stretch) i386/amd64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_debian.sh">pkg_install_debian.sh </a></td>
  </tr>
  <tr>
    <td>Fedora 27 i686/x86_64 <br> Fedora 28 i686/x86_64 <br> Fedora 29 i686/x86_64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_fedora.sh">pkg_install_fedora.sh </a></td>
  </tr>
</table>

<!-- ※Fedora用一括インストール・スクリプトはOpenRTM-aist 1.2.0版以降対応予定です。 -->



オプションを指定することで、目的に合わせたパッケージをインストールすることができるようになりました。インストール方法やオプション、パッケージの種類につきましては、[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script) をご確認ください。


1.1.2-RELEASE を既にインストールしている場合はアップデートが可能です。

Ubuntu / Debian の場合

```
 $ sudo apt-get update
 $ sudo apt-get upgrade
```

Fedora　の場合

```
 # dnf update
```

ダウンロード方法・インストール方法については、[OpenRTM-aist (C++版) 1.x系のインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1) をご覧くだい。

&aname(src);
## ソースコード

<table class="table-alt">
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0.tar.bz2">OpenRTM-aist-1.2.0.tar.bz2</a> <br>MD5:c16297cfb3ee6b10f895131dfa154222</td>
    <td>2019.03.15</td>
  </tr>
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0.tar.gz">OpenRTM-aist-1.2.0.tar.gz</a> <br>MD5:198b1f67729955bc061f1df0b1e2a7d5</td>
    <td>2019.03.15</td>
  </tr>
  <tr>
    <td>C++版Windows専用ソース</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-win32.zip">OpenRTM-aist-1.2.0-win32.zip</a> <br>MD5:4b4cee65cf40f3a79415277cd347a751</td>
    <td>2019.03.15</td>
  </tr>
</table>

### ソースからのビルド

ソースからビルドする方法については、[ソースからのビルド(Windows編)]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/build_source_windows_1_1) または [ソースからのビルド(Linux編)]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/build_source_linux_1_1) をご覧くだい。

### deb/rpm パッケージ作成

1.1から上記の [[ソースコード>#src]] からのUbuntu、Debian 用 deb パッケージ、Fedora、Vine 用 rpmパッケージの作成が正式にサポートされました。<br>
以下の手順でパッケージを作成することができます。パッケージ作成に当たっては、一括インストールスクリプト（pkg_install_***.sh）を利用して必要なパッケージを予めインストールしておいてください。

```
 $ tar xvzf OpenRTM-aist-1.2.0-RELEASE.tar.gz
 $ cd OpenRTM-aist-1.2.0
 $ ./configure --prefix=/usr
 $ cd packages
 $ make
```

パッケージは pacakges ディレクトリー内に作成されます。

<span style="color:red;">※ Ubuntu や Debian にて deb パッケージを作成する場合は "dpkg-dev build-essential debhelper devscripts"、Fedora にて rpm パッケージを作成する場合は "rpm-build createrepo" といったツールを予めインストールしておく必要があります。</span>;
これらは、[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)  を -c オプションで実行すればインストールされます。

<!-- &br; -->
<!-- ***MacPorts -->
<!-- MacPorts 用 Portfile が利用可能です。あらかじめ Xcode および MacPorts をインストールした上でご利用ください。 -->
<!-- - [[Portfile (ports.tgz) :http://www.openrtm.org/pub/MacOSX/macports/ports.tgz]] -->
<!-- - [[インストールスクリプト (port_install.sh) :http://www.openrtm.org/pub/MacOSX/macports/port_install.sh]]: ports.tgz のダウンロード、OpenRTM-aist のビルド・インストールまで自動で行います。 -->

<!-- ** ツール -->

<!-- インストーラーのオプションで OpenRTP を選択していれば、インストールする必要はありません。 -->
<!-- ツールを別途インストールする方法については、　[[OpenRTP 1.1.0-RC5:/ja/node/5778]] をご覧ください。 -->

<br>
## リリースノート: 1.2.0-RELEASE
OpenRTM-aist Official Website からソースコード、Windows インストーラー、Linux 用パッケージ等が LGPL ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

<!-- - [[OpenRTM-aist-1.1.0-RELEASE.tar.gz:http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.0/OpenRTM-aist-1.1.0-RELEASE.tar.gz]] -- 2012.05.25リリース -->

### 機能に関する変更
- 雑多なバグフィックス
- マネージャ起動時にポートを接続する機能
- マネージャ起動時にコンポーネントをアクティベーションする機能
- CORBA_RTCUtil：コンポーネント操作関数群の導入
- トピックベースのポート接続機能
- 共有メモリ通信データポート(shared_memory型インターフェース)
- 同一プロセス内通信のデータ転送を変数で渡すダイレクト接続データポート(direct型インターフェース)
- OpenSSLによるセキュアな通信機能
- 名前付けポリシー機能の拡張(同一ネームサーバー、同一ノードで独自のインスタンス名を設定する)
- rtcloc形式のコンポーネント指定方法(マスターマネージャに登録されたスレーブマネージャからコンポーネントを名前で検索)
- rtcname形式のコンポーネント指定方法(ネームサーバーに登録されたコンポーネントを名前で検索)
- デフォルトでデータポートの二重接続を許可しない機能
- omniidl shortcutの利用
- LogstreamBase：ロガー機能の拡張
- Fluent Bitによるログ収集機能(Linuxのみ)
- コンポーネントオブザーバのデータ入出力検知機能
- モジュール探索パスのサブディレクトリのモジュールを探索する機能
- ログファイルのエスケープシーケンスをデフォルトで無効にする機能


<!-- -- RTC の各種動作をフックするリスナ機構の追加 -->
<!-- --- ComponentActionListener: コンポーネントの各種動作をフック可能に -->
<!-- --- PortConnectionListeners: ポートの接続切断をフックする事が可能に -->
<!-- --- ManagerActionListener: マネージャの各種動作のフック -->
<!-- --- ConfigurationListener:コンフィギュレーションの動作のフック -->
<!-- --- ConnectorListener：データポートの送受信の各種動作のフック -->
<!-- -- rtcd で C++ だけでなく Python、Java の RTC プロファイルを取得可能に -->
<!-- -- EC にアクセスするための各種関数群の提供 -->
<!-- -- SDO サービス（プロバイダ・コンシューマ）管理機能の導入 -->
<!-- -- ログのタイムスタンプで ms,、usが出力可能 -->
<!-- -- 各種オプションの追加:　manager.auto_shutdown_duration 等 -->

### ポータビリティに関する変更
- 64bit Linunx への雑多な対応
- 64bit Windows への対応
<!-- -- Mac OS X への正式な対応 -->
<!-- -- Linux+RtORB の正式サポート -->
<!-- -- Cygwin+RtORB の正式サポート -->
<!-- -- MacOS+RtORB の正式サポート -->
- VC2017(32bit/64bit) の正式サポート
<!-- -- CMake への正式対応 -->

### 拡張機能に関する変更
- ComponentObserver がRTCのdll, libに含まれるようになったため、ext\sdo下に配置していた処理を外した
<!-- -- RT preemptive kernel 用 EC の正式サポート -->

### ユーザービリティに関する変更
- インストール時、VisualStudioのバージョンを指定できる機能を組み込む
- Windows7, 8.1, 10の環境でスタートメニュー表示が同じように見えるよう整備
- ExtTriggerサンプルを起動するbatスクリプトを追加
- OpenRTM-aistの32bit版、64bit版の両方をインストールされた環境に対応するためスタートメニューを別々に定義
- ネームサービス終了スクリプトを定義する
- Windows インストーラーで omniORBを4.2.3に更新
- Windows インストーラーで rtshellを4.2.0に更新
- Windows インストーラーで OpenCVを3.4に更新し、IntelTBB で再コンパイル、GStreamer対応
- RTSE上でマネジャー経由でOpenCVサンプルRTCを起動できるようにrtc.confを整備する


### 対応 (ビルド検証済) OS
- Debian 8.0 i386, amd64
- Debian 9.0 i386, amd64
- Ubuntu 14.04 i386, amd64
- Ubuntu 16.04 i386, amd64
- Ubuntu 18.04 amd64
- Ubuntu 18.10 amd64
- Fedora release 27 i686, x86_64
- Fedora release 28 i686, x86_64
- Fedora release 29 i686, x86_64
- Windows-7 (32/64bit)
- Windows-8.1 (32/64bit)
- Windows-10 (32/64bit)
