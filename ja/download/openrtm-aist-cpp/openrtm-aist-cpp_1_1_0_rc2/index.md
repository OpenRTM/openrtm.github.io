---
layout: page
title: openrtm-aist c++ 1.1.0-rc2
---

<!-- Title: 1.1.0-RC2 -->
<div align="right"><a href="cpp_logo.png"><img src="cpp_logo.png" width="15%;" align="right"></a></div>
#contents

- <span style="color:red;">1.1.0-RC1はROBOMEC2011で使用するために参加者を対象にリリースされたものです。1.1.0-RELEASEがリリースされるまでは1.1.0-RC2をご利用ください。</span>;
- <span style="color:red;">1.0.0で作成したコンポーネントと1.1.0で作成したコンポーネントには互換性はありますが、ポートの接続方法が若干変更されたため、ツールは1.1.0のものを使用してください。</span>;


## ソースコード

<table class="table-alt">
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="">OpenRTM-aist-1.1.0-RC2.tar.bz2</a>（リンク切れです）<br>MD5:fba1dbc10b99381d6c46afd33be4f9ca</td>
    <td>2011.06.06</td>
  </tr>
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="">OpenRTM-aist-1.1.0-RC2.tar.gz</a>（リンク切れです）<br>MD5:86bab7c5153e9d0a3ab12311471e36d3</td>
    <td>2011.06.06</td>
  </tr>
  <tr>
    <td>C++版Windows専用ソース</td>
    <td><a href="">OpenRTM-aist-1.1.0-RC2-win32.zip</a>（リンク切れです）<br>MD5:5dfb2359c90f86e4674483b19839eaac</td>
    <td>2011.06.06</td>
  </tr>
</table>

<br>
## パッケージ
### Windowsインストーラ
<table class="table-alt">
  <tr>
    <th colspan="3">Visual Studio 2008 用</th>
  </tr>
  <tr>
    <td>Windowsインストーラ</td>
    <td><a href="">OpenRTM-aist-1.1.0-RC2_vc9.msi</a>（リンク切れです）<br>MD5:f4f605d8ff3375929a7ab296d792d8bc</td>
    <td>2011.06.06</td>
  </tr>
  <tr>
    <td>Python Windows用インストーラ</td>
    <td><a href="http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi">python-2.6.4.msi</a></td>
    <td><a href="http://www.python.org/">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML (rtc-templateに必要)</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.09.win32-py2.6.exe">PyYAML-3.09.win32-py2.6.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
</table>

<br>

<!-- |LEFT:200|LEFT|LEFT:100|c -->
<!-- |>|>|CENTER:''Visual Studio 2005 用''| -->
<!-- |Windowsインストーラ|[[OpenRTM-aist-1.1.0-RC1_vc8.msi>http://www.openrtm.org/pub/Windows/OpenRTM-aist/cxx/OpenRTM-aist-1.1.0-RC1_vc8_100212.msi]]&br;MD5:|2011.05.24| -->
<!-- |Python Windows用インストーラ|[[python-2.6.4.msi:http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi]]|[[python.org:http://www.python.org/]]| -->
<!-- |PyYAML (rtc-templateに必要)|[[PyYAML-3.09.win32-py2.6.exe:http://pyyaml.org/download/pyyaml/PyYAML-3.09.win32-py2.6.exe]]|[[pyyaml.org:http://pyyaml.org/]]| -->
<!--  -->
- <span style="color:red;">Windowsインストーラには、''OpenRTM-aist (DLL,ヘッダ,サンプル,コマンド), omniORB-4.1.4, RTSystemEditor (RCP版), さらにOpenCV 2.1 とこれを利用したサンプルコンポーネントが含まれていますので、omniORBやツールを別途インストールする必要はありません。</span>;
- <span style="color:red;">※Visual Studio 2005でビルドしたOpenRTM-aistとVisual Studio 2008でビルドしたものは混在できません。お使いの開発環境に合わせて適切なパッケージをダウンロードしてください。</span>;

<br>
### Linuxパッケージ (準備中)

LinuxパッケージはRELEASE版で提供される予定です。ソースからのビルドの仕方は以下を参考にしてください。

- [ソースからのビルド]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/build_source_linux_1_1)

なお、1.1から上記配布ソースからのUbuntu, Debian 用debパッケージ、Fedora, Vine用 rpmパッケージの作成が正式にサポートされました。
以下の手順でパッケージを作成することができます。パッケージ作成に当たっては、以下のインストールスクリプトを利用して必要なパッケージを予めインストールしておいてください。

```
 $ tar xvzf OpenRTM-aist-1.1.0-RC2.tar.gz
 $ cd OpenRTM-aist-1.1.0
 $ ./configure --prefix=/usr
 $ cd packages
 $ make
```

パッケージはpacakgesディレクトリ内に作成されます。

<!-- Vine Linux, Fedora, Ubuntu, Debianの各ディストリビューション用のパッケージを www.openrtm.org 上のリポジトリサーバにて配布しています。 -->
<!-- 詳細は、以下のドキュメントを参照してください。 -->

<!-- -[[Vine Linux:/ja/node/1000]] -->
<!-- -[[Fedora:/ja/node/1002/]] -->
<!-- -[[Debian/Ubuntu:/ja/node/1001]] -->

また、以下で配布しているインストールスクリプトを利用すれば、必要なパッケージを一括でインストールすることができます。

<table class="table-alt">
  <tr>
    <th>ディストリビューション</th>
    <th>対応バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Vine Linux</td>
    <td>4.0, 4.2, 5.0</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_vine.sh">pkg_install_vine.sh </a></td>
  </tr>
  <tr>
    <td>Fedora</td>
    <td>10, 11, 12 (共にi386/x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_fedora.sh">pkg_install_fedora.sh </a></td>
  </tr>
  <tr>
    <td>Ubuntu</td>
    <td>8.04, 8.10, 9.04, 9.10, 10.04 (共にi386/x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian</td>
    <td>3.1 (i386), 4.0, 5.0 (共にi386, x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_debian.sh">pkg_install_debian.sh </a></td>
  </tr>
</table>

<!-- &br; -->
<!-- ***MacPorts -->
<!-- MacPorts用Portfileが利用可能です。あらかじめXcodeおよびMacPortsをインストールした上でご利用ください。 -->
<!-- - [[Portfile (ports.tgz) :http://www.openrtm.org/pub/MacOSX/macports/ports.tgz]] -->
<!-- - [[インストールスクリプト (port_install.sh) :http://www.openrtm.org/pub/MacOSX/macports/port_install.sh]]: ports.tgz のダウンロード、OpenRTM-aistのビルド・インストールまで自動で行います。 -->

<br>
## ツール
<table class="table-alt">
  <tr>
    <td>Windows用全部入り<br>(RTSystemEditor1.1.0+RTCBUilder1.1.0)</td>
    <td><a href="">eclipse342_rtmtools110-rc1_win32_ja.zip</a>（リンク切れです）<br>MD5:f5619616be753fef7bae9ef863e5b33f</td>
    <td>2011.05.24</td>
  </tr>
  <tr>
    <td>Linux用全部入り<br>(RTSystemEditor1.1.0+RTCBUilder1.1.0)</td>
    <td><a href="">eclipse342_rtmtools110-rc1_linux_ja.tar.gz</a>（リンク切れです）<br>MD5:062355b5963cd0f0a42fb3b8ad43ddc2</td>
    <td>2011.05.24</td>
  </tr>
</table>

<br>
## リリースノート: 1.1.0-RC2
OpenRTM-aist-1.1.0 のrelease candidate version を2011年6月6日にリリースしました。
OpenRTM-aist Official Website からソースコード、Windowsインストーラ、Linux用パッケージ等が LGPL ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

- [OpenRTM-aist-1.1.0-RC2.tar.gz](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.0/OpenRTM-aist-1.1.0-RC2.tar.gz) -- 2011.06.06リリース
  - APIの追加
    - コールバックAPI
    - 実行コンテキストに関するコールバック
  - SDOサービスフレームワーク
  - 雑多なバグフィックス
  - 実験的
    - オブザーバSDOサービスの導入
    - CMake用ファイル"OpenRTMConfig.cmake"の導入(Linux/Windows)
  - Windows版 インストーラ
    - OpenCV2.1とサンプルコンポーネントを同梱
  - 対応(ビルド検証済)OS
    - Debian4.0-i686
    - Debian4.0-x86_64
    - Debian5.0-i686
    - Debian5.0-x86_64
    - Fedora release 11 (Leonidas)-i686
    - Fedora release 11 (Leonidas)-x86_64
    - Fedora release 12 (Constantine)-i686
    - Fedora release 12 (Constantine)-x86_64
    - Fedora release 13 (Goddard)-i686
    - Fedora release 13 (Goddard)-x86_64
    - Fedora release 14 (Laughlin)-i686
    - Fedora release 14 (Laughlin)-x86_64
    - FreeBSD7.x-amd64
    - FreeBSD7.x-i386
    - FreeBSD8.x-amd64
    - FreeBSD8.x-i386
    - Ubuntu 8.04-i686
    - Ubuntu 8.04-x86_64
    - Ubuntu 9.10-i686
    - Ubuntu 9.10-x86_64
    - Ubuntu 10.04-i686
    - Ubuntu 10.04-x86_64
    - Ubuntu 10.10-i686
    - Ubuntu 10.10-x86_64
    - Ubuntu 11.04-i686
    - Ubuntu 11.04-x86_64
    - Vine Linux 4.2 (Lynch Bages)-i686
    - Vine Linux 5.0 (Lafite)-i686
    - Windows-XP-VC2005-i386
    - Windows-Vista-VC2008-i386

<br>
## 過去のバージョン
- [1.0.0-RELEASE](openRTM-aist-1.0.0-RELEASE)
- [1.0.0-RC1](OpenRTM-aist-1.0.0-RC1)
- [0.4.2-RELESE](OpenRTM-aist-0.4.2-RELEASE]])
- [0.4.2-RC2](OpenRTM-aist-0.4.2-RC2]])
- [0.4.1-RELEASE](OpenRTM-aist-0.4.1-RELEASE]])
- [0.4.0-RELEASE](OpenRTM-aist-0.4.0-RELEASE]])
- [0.4.0-RC2](OpenRTM-aist-0.4.0-RC2]])
