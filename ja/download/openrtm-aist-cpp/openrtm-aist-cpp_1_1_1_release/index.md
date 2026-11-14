---
layout: page
title: openrtm-aist c++ 1.1.1-release
---

<!-- Title: OpenRTM-aist C++ 1.1.1-RELEASE -->
<div align="right"><a href="cpp_logo.png"><img src="cpp_logo.png" width="15%;" align="right"></a></div>
#contents


- <span style="color:red;">1.0.0 で作成したコンポーネントと 1.1.1 で作成したコンポーネントには互換性はありますが、ポートの接続方法が若干変更されたため、ツール (RTSystemEditor) は 1.1.0 のものを使用してください。</span>;

&aname(src);
## ソースコード

<table class="table-alt">
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.1/OpenRTM-aist-1.1.1.tar.bz2">OpenRTM-aist-1.1.1-RELEASE.tar.bz2</a><br>MD5: 1d030c4972618f2f1e81cf83286af1d0</td>
    <td>2015.03.16</td>
  </tr>
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.1/OpenRTM-aist-1.1.1.tar.gz">OpenRTM-aist-1.1.1-RELEASE.tar.gz</a><br>MD5: 67abe01eb0e8df1cd3efbcd1ca78108d</td>
    <td>2015.03.16</td>
  </tr>
  <tr>
    <td>C++版 Windows 専用ソース</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.1/OpenRTM-aist-1.1.1-win32.zip">OpenRTM-aist-1.1.1-RELEASE-win32.zip</a><br>MD5: beedc1f16973eb6cc6c2bc7916bafeb7</td>
    <td>2015.03.16</td>
  </tr>
</table>

<br>
## パッケージ
### Windows インストーラー

インストーラーで、ツールの RTSystemEditorRCP と OpenRTP を選択できるようになりました。また、ツールを起動するために必要な JRE(OpenJDK) もインストールすることができます。<br>
これらの選択は、デフォルト設定のままインストールすることをお勧めします。オプションの選択については、[OpenRTM-aistを10分で始めよう！]()（リンク切れです） のページで手順を紹介しています。

#### 32bit用

- Visual Studio をインストールされている方は、バージョンにあったインストーラーをダウンロードしてください。

<table class="table-alt">
  <tr>
    <td colspan="3" style="text-align: center;">**Visual Studio 32bit用**</td>
  </tr>
  <tr>
    <td>Visual Studio 2008</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/cxx/1.1/OpenRTM-aist-1.1.1-RELEASE_x86_vc9.msi">OpenRTM-aist-1.1.1-RELEASE_x86_vc9.msi</a><br>MD5: d800c7fefea48965dcbdb43a0150245f</td>
    <td>2015.04.09</td>
  </tr>
  <tr>
    <td>Visual Studio 2010</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/cxx/1.1/OpenRTM-aist-1.1.1-RELEASE_x86_vc10.msi">OpenRTM-aist-1.1.1-RELEASE_x86_vc10.msi</a><br>MD5: 8efd345ba871aa92f814cde6014e338f</td>
    <td>2015.04.09</td>
  </tr>
  <tr>
    <td>Visual Studio 2012</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/cxx/1.1/OpenRTM-aist-1.1.1-RELEASE_x86_vc11.msi">OpenRTM-aist-1.1.1-RELEASE_x86_vc11.msi</a><br>MD5: def246f243be45df332d4caa0393267c</td>
    <td>2015.04.09</td>
  </tr>
  <tr>
    <td>Visual Studio 2013</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/cxx/1.1/OpenRTM-aist-1.1.1-RELEASE_x86_vc12.msi">OpenRTM-aist-1.1.1-RELEASE_x86_vc12.msi</a><br>MD5: bdf6fd6dafcba9455e8e87d30db3c516</td>
    <td>2015.04.09</td>
  </tr>
</table>


<table class="table-alt">
  <tr>
    <td colspan="3" style="text-align: center;">**各Visual Studio 32bit用バージョンで共通**</td>
  </tr>
  <tr>
    <td>Python (各種ツールで必要)<br> Python 2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi">python-2.7.9.msi</a></td>
    <td><a href="https://www.python.org/">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML (各種ツールで必要)<br> Pythonのバージョンに合わせること</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.11.win32-py2.7.exe">PyYAML-3.11.win32-py2.7.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
  <tr>
    <td>CMake （Visual C++のプロジェクトを作成するのに必要)</td>
    <td><a href="http://www.cmake.org/files/v3.2/cmake-3.2.1-win32-x86.exe">cmake-3.2.1-win32-x86.exe</a></td>
    <td><a href="http://www.cmake.org">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen (ビルドの過程でドキュメントを整形するのに必要)</td>
    <td><a href="http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.9.1-setup.exe">doxygen-1.8.9.1-setup.exe</a></td>
    <td><a href="http://www.stack.nl/`dimitri/doxygen/">doxygen</a></td>
  </tr>
</table>
<!-- |Doxygen (ビルドの過程でドキュメントを整形するのに必要)|[[doxygen-1.8.8-setup.exe:http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.8-setup.exe]] |[[doxygen:http://www.stack.nl/~dimitri/doxygen/]]| -->

- Python のバージョンは、Python版 OpenRTM-aist も同時に利用することを考え、Python 2.7 を利用することを推奨します。

#### 64bit用

- Visual Studio をインストールされている方は、バージョンにあったインストーラーをダウンロードしてください。
- Visual C++ Express 版では(デフォルトでは) 64bit バイナリのビルドができませんのでご注意ください。

<table class="table-alt">
  <tr>
    <td colspan="3" style="text-align: center;">**Visual Studio 64bit用**</td>
  </tr>
  <tr>
    <td>Visual Studio 2010</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/cxx/1.1/OpenRTM-aist-1.1.1-RELEASE_x86_64_vc10.msi">OpenRTM-aist-1.1.1-RELEASE_x86_64_vc10.msi</a><br>MD5: 4dc5ec26f83677b57ae70f9a35c96d9a</td>
    <td>2015.04.09</td>
  </tr>
  <tr>
    <td>Visual Studio 2012</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/cxx/1.1/OpenRTM-aist-1.1.1-RELEASE_x86_64_vc11.msi">OpenRTM-aist-1.1.1-RELEASE_x86_64_vc11.msi</a><br>MD5: 4f3aa87e584b79eec3dc50f721f82b1c</td>
    <td>2015.04.09</td>
  </tr>
  <tr>
    <td>Visual Studio 2013</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/cxx/1.1/OpenRTM-aist-1.1.1-RELEASE_x86_64_vc12.msi">OpenRTM-aist-1.1.1-RELEASE_x86_64_vc12.msi</a><br>MD5: 521a5c9a54b7002edf1a8e5d097e2cec</td>
    <td>2015.04.09</td>
  </tr>
</table>

<table class="table-alt">
  <tr>
    <td colspan="3" style="text-align: center;">**各Visual Studio 64bit 用バージョンで共通**</td>
  </tr>
  <tr>
    <td>Python-64bit (各種ツールで必要)<br> Python 2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi">python-2.7.9.amd64.msi</a></td>
    <td><a href="https://www.python.org/">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML (各種ツールで必要)<br> Python のバージョンに合わせること</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.11.win-amd64-py2.7.exe">PyYAML-3.11.win-amd64-py2.7.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
  <tr>
    <td>CMake （Visual C++ のプロジェクトを作成するのに必要)</td>
    <td><a href="http://www.cmake.org/files/v3.2/cmake-3.2.1-win32-x86.exe">cmake-3.2.1-win32-x86.exe</a></td>
    <td><a href="http://www.cmake.org">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen (ビルドの過程でドキュメントを整形するのに必要)</td>
    <td><a href="http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.9.1-setup.exe">doxygen-1.8.9.1-setup.exe</a></td>
    <td><a href="http://www.stack.nl/`dimitri/doxygen/">doxygen</a></td>
  </tr>
</table>


- 64bit版 OpenRTM-aist は、Python 2.7 (64bit) がインストールされていれば動作します。


#### Windows 版インストールにあたっての注意事項

- <span style="color:red;">※ Visual Studio のバージョンが異なる環境でビルドしたものは混在できません。</span>; お使いの開発環境に合わせて適切なパッケージをダウンロードしてください。
- 古いバージョンの OpenRTM-aist をインストールされている場合は、あらかじめアンインストールすることをお勧めします。　（1.1.1-RELEASEはアンインストールしてもゴミは残りません）
- 1.1.0 版をアンインストールしてもファイルとスタートメニューの一部が残ることを確認しています。(C++/Python/Javaすべてで確認）
- 残ったままで新しいバージョンをインストールしても動作に影響はありませんが、手動で削除することをお勧めします。
  - 手動で削除する場合の注意：
  - OpenRTM-aist の異なる言語バージョン（例えば C++とPython）をインストールされている場合は、どちらも新しいバージョンに移行することをお勧めします
  - 古い OpenRTM-aist の全てをアンインストール後、手動で下記を削除してください
    - C:\Program Files (x86) 下の OpenRTM-aist フォルダー
    - スタートメニューの OpenRTM-aist：スタートメニューで表示させて右クリックで削除できます


<br>
### Linux パッケージ

<!-- Linux パッケージは順次提供される予定です。ソースからのビルドの仕方は以下を参考にしてください。 -->

現在のところ以下のディストリビューション・バージョンでパッケージを提供しています。<br>
以下で配布しているインストールスクリプトを利用すれば、必要なパッケージを一括でインストールすることができます。

<table class="table-alt">
  <tr>
    <th>ディストリビューション・バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Ubuntu 12.04 (precise) i386/amd64 <br> Ubuntu 14.04 (trusty) i386/amd64 <br> Ubuntu 14.10 (utopic) i386/amd64 <br> Ubuntu 15.04 (vivid) i386/amd64</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian  6.0  (squeeze) i386/amd64 <br> Debian  7.0  (wheezy) i386/amd64</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_debian.sh">pkg_install_debian.sh </a></td>
  </tr>
  <tr>
    <td>Fedora 19 i386/amd64 <br> Fedora 20 i386/amd64 <br> Fedora 21 i386/amd64</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_fedora.sh">pkg_install_fedora.sh </a></td>
  </tr>
</table>

<!-- 1.1.0-RELEASE を既にインストールしている場合は、削除後 apt-get updateを 実行した上で、再度インストールしてください。 -->
<!-- $ sudo dpkg -r openrtm-aist-doc openrtm-aist-example openrtm-aist-dev openrtm-aist -->
<!-- $ sudo apt-get clean -->
<!-- $ sudo apt-get update -->
<!-- $ sudo apt-get install openrtm-aist openrtm-aist-doc openrtm-aist-example openrtm-aist-dev -->

1.1.0-RELEASE を既にインストールしている場合はアップデートが可能です。

Ubuntu / Debian の場合

```
 $ sudo apt-get update
 $ sudo apt-get upgrade
```

Fedora　の場合

```
 # yum update
```

ダウンロード方法・インストール方法については、[こちら(C++)]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1) をご覧くだい。


### ソースからのビルド

ソースからビルドする方法については、[ソースからのビルド(Windows編)]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/build_source_windows_1_1) または [ソースからのビルド(Linux編)]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/build_source_linux_1_1) をご覧くだい。

### deb/rpmパッケージ作成

1.1から上記の [[ソースコード>#src]] からの Ubuntu, Debian 用 deb パッケージ、Fedora, Vine用 rpm パッケージの作成が正式にサポートされました。<br>
以下の手順でパッケージを作成することができます。パッケージ作成に当たっては、一括インストールスクリプト（pkg_install_***.sh）を利用して必要なパッケージを予めインストールしておいてください。

```
 $ tar xvzf OpenRTM-aist-1.1.1-RELEASE.tar.gz
 $ cd OpenRTM-aist-1.1.1
 $ ./configure --prefix=/usr
 $ cd packages
 $ make
```

パッケージはpacakgesディレクトリ内に作成されます。

<span style="color:red;">※ UbuntuやDebian にて deb パッケージを作成する場合は "dpkg-dev build-essential debhelper devscripts"、Fedora にて rpm パッケージを作成する場合は "rpm-build createrepo" といったツールを予めインストールしておく必要があります。</span>;

<!-- &br; -->
<!-- ***MacPorts -->
<!-- MacPorts 用 Portfile が利用可能です。あらかじめXcodeおよびMacPortsをインストールした上でご利用ください。 -->
<!-- - [[Portfile (ports.tgz) :http://www.openrtm.org/pub/MacOSX/macports/ports.tgz]] -->
<!-- - [[インストールスクリプト (port_install.sh) :http://www.openrtm.org/pub/MacOSX/macports/port_install.sh]]: ports.tgz のダウンロード、OpenRTM-aist のビルド・インストールまで自動で行います。 -->

## ツール

インストーラのオプションで OpenRTP を選択していれば、インストールする必要はありません。
ツールを別途インストールする方法については、　[OpenRTP 1.1.0-RC5]({{ site.baseurl }}/ja/download/tools/openrtp_1_1_0_rc5) をご覧ください。

<br>
## リリースノート: 1.1.1-RELEASE
OpenRTM-aist Official Website からソースコード、Windows インストーラー、Linux 用パッケージ等が LGPL ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

<!-- - [[OpenRTM-aist-1.1.0-RELEASE.tar.gz:http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.0/OpenRTM-aist-1.1.0-RELEASE.tar.gz]] -- 2012.05.25リリース -->

### 機能に関する変更
  - 雑多なバグフィックス
<!-- -- RTCの各種動作をフックするリスナ機構の追加 -->
<!-- --- ComponentActionListener: コンポーネントの各種動作をフック可能に -->
<!-- --- PortConnectionListeners: ポートの接続切断をフックする事が可能に -->
<!-- --- ManagerActionListener: マネージャの各種動作のフック -->
<!-- --- ConfigurationListener:コンフィギュレーションの動作のフック -->
<!-- --- ConnectorListener：データポートの送受信の各種動作のフック -->
<!-- -- rtcd で C++ だけでなくPython、JavaのRTCプロファイルを取得可能に -->
<!-- -- EC にアクセスするための各種関数群の提供 -->
<!-- -- SDO サービス（プロバイダ・コンシューマ）管理機能の導入 -->
<!-- -- ログのタイムスタンプで ms, usが出力可能 -->
<!-- -- 各種オプションの追加:　manager.auto_shutdown_duration等 -->

### ポータビリティに関する変更
- 64bit Linunxへの雑多な対応
- 64bit Windowsへの対応
<!-- -- Mac OS Xへの正式な対応 -->
<!-- -- Linux+RtORB の正式サポート -->
<!-- -- Cygwin+RtORB の正式サポート -->
<!-- -- MacOS+RtORB の正式サポート -->
- VC2012(32bit/64bit) の正式サポート
- VC2013(32bit/64bit) の正式サポート
<!-- -- CMake への正式対応 -->

### 拡張機能に関する変更
<!-- -- ComponentObserver の提供 -->
<!-- -- RT preemptive kernel 用 EC の正式サポート -->

### ユーザービリティに関する変更
- Windows インストーラーで omniORB を 4.1.7 に更新
- Windows インストーラーで OpenCV を 2.4.9 に更新し、IntelTBB で再コンパイル
- Windows インストーラーで OpenCV を使ったサンプルコンポーネント ImageCalib (GUIを持つ)を追加
- Windows インストーラーでツールの RTSystemEditorRCP版 と OpenRTP を選択可能にする
- Windows インストーラーのスタートメニューでのツールを、各言語（C++、Python、Java)で共通にする
- Windows インストーラーで OpenJDK7 JREの インストールを選択可能にする
- deb パッケージ作成でマルチアーチ機能へ対応
- deb パッケージ利用環境で OpenRTM-aist Python と共存時のアンインストール動作の見直し

### 対応 (ビルド検証済) OS
- Debian 6.0-i386
- Debian 6.0-x86_64
- Debian 7.0-i386
- Debian 7.0-x86_64
- Fedora release 19 i386
- Fedora release 19 x86_64
- Fedora release 20 i386
- Fedora release 20 x86_64
- Ubuntu 12.04-i386
- Ubuntu 12.04-x86_64
- Ubuntu 14.04-i386
- Ubuntu 14.04-x86_64
- Windows-7
- Windows-7 (64bit)
- Windows-8.1
- Windows-8.1 (64bit)

