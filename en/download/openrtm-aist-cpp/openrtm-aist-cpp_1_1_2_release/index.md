---
layout: page
title: openrtm-aist c++ 1.1.2-release
---

<!-- Title: OpenRTM-aist C++ 1.1.2-RELEASE -->

<div align="right"><a href="cpp_logo.png"><img src="cpp_logo.png" width="10%;" align="right"></a></div>
#contents(4)

<!-- -&color(red){まだリリースしておりません。準備中です。もうしばらくお待ち下さい。}; -->

<br>
## Packages
### Windows installer

#### For 32bit

<table class="table-alt">
  <tr>
    <td>Windows installer <br> (OpenRTM-aist for C++, Python, Java,<br> and OpenRTP, rtshell(4.1.0) are included)<br>(Visual Studio 2008, 2010, 2012, 2013, 2015 are supported)</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/1.1/OpenRTM-aist-1.1.2-RELEASE_x86.msi">OpenRTM-aist-1.1.2-RELEASE_x86.msi</a> <br>MD5:d7bc03556e6b643a7e6102ab08fe9ff6</td>
    <td>2016/05/27</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi">python-2.7.10.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.11.win32-py2.7.exe">PyYAML-3.11.win32-py2.7.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://cmake.org/files/v3.5/cmake-3.5.2-win32-x86.msi">cmake-3.5.2-win32-x86.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="https://www.doxygen.nl/files/doxygen-1.9.2-setup.exe">doxygen-1.9.2-setup.exe</a></td>
    <td><a href="https://www.doxygen.nl/">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">* Currently Python 2.7.10 is recommended. 2.7.11 might need to set PYTHONPATH environment variables.</span>;
- <span style="color:red;">* Old rtshell must be removed before installing rtshell from this installer.</span>;
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [[doxygen: http: //www.doxygen.nl/index.html]] and download and install the latest "doxygen-X.X.X-setup.exe".


#### For 64bit

<table class="table-alt">
  <tr>
    <td colspan="4" style="text-align: center;">CENTER:**Visual Studio 64bit用**</td>
  </tr>
  <tr>
    <td>Windows installer <br> (OpenRTM-aist for C++, Python, Java,<br> and OpenRTP, rtshell(4.1.0) are included)<br>(VVisual Studio 2008, 2010, 2012, 2013, 2015 are supported)</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/1.1/OpenRTM-aist-1.1.2-RELEASE_x86_64.msi">OpenRTM-aist-1.1.2-RELEASE_x86_64.msi</a> <br>MD5:dd182bd4daa31c2c26066a56cf5fed59</td>
    <td>2016/05/27</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.amd64.msi">python-2.7.10.amd64.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.11.win-amd64-py2.7.exe">PyYAML-3.11.win-amd64-py2.7.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://cmake.org/files/v3.5/cmake-3.5.2-win32-x86.msi">cmake-3.5.2-win32-x86.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="https://www.doxygen.nl/files/doxygen-1.9.2-setup.exe">doxygen-1.9.2-setup.exe</a></td>
    <td><a href="https://www.doxygen.nl/">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">* Currently Python 2.7.10 is recommended. 2.7.11 might need to set PYTHONPATH environment variables.</span>;
- <span style="color:red;">* Old rtshell must be removed before installing rtshell from this installer.</span>;
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [doxygen](http://www.doxygen.nl/index.html) and download and install the latest "doxygen-X.X.X-setup.exe".


<!-- インストールについては、[[OpenRTM-aistを10分で始めよう！:http://openrtm.org/openrtm/ja/node/6026]] のページで手順を紹介しています。&br; -->

#### How to set Visual Studio version

Modify system environment variable **RTM_VC_VERSION** according to Visual Studio version used in your system.

<table class="table-alt">
  <tr>
    <td>Visual Studio version</td>
    <td>RTM_VC_VERSION value</td>
    <td></td>
  </tr>
  <tr>
    <td>2008</td>
    <td>vc9</td>
    <td>Only 32bit version supported</td>
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
    <td>default setting</td>
  </tr>
  <tr>
    <td>2015</td>
    <td>vc14</td>
    <td></td>
  </tr>
</table>

#### How to use old version runtime of C++

Old version runtime libraries are installed version-name folder (such as 1.0.0(only 32bit), 1.1.0, 1.1.1 folders) under OpenRTM-aist Program folder, .
Set target search path to PATH environment variable by using **RTM_BASE** environment variable.

ex) vc12 run-time libraries for version 1.1.1 are located under **RTM_BASE1.1.1\vc12\bin**.


<br>
### Linux package

Currently pre-build packages are provided for the following distribution and versions.
Installing OpenRTM-aist is just run the following installation script.

<table class="table-alt">
  <tr>
    <th>Distribution / version</th>
    <th>Installation script</th>
  </tr>
  <tr>
    <td>Ubuntu 12.04 (precise) i386/amd64 <br> Ubuntu 14.04 (trusty) i386/amd64 <br> Ubuntu 15.10 (wily) i386/amd64 <br> Ubuntu 16.04 (xenial) i386/amd64</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian  7.0  (wheezy) i386/amd64 <br> Debian  8.0  (jessie) i386/amd64</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_debian.sh">pkg_install_debian.sh </a></td>
  </tr>
</table>
<!-- | Fedora 21 i386/amd64 &br; Fedora 22 i386/amd64 &br; Fedora 23 i386/amd64| [[pkg_install_fedora.sh >http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_fedora.sh]] | -->

1.1.1-RELEASE can be updated, if you already installed it.

For Ubuntu / Debian

```
 $ sudo apt-get update
 $ sudo apt-get upgrade
```

For Fedora

```
 # dnf update
```

<!-- See [[this:/ja/node/999]] for is the more details for downloading and installation  をご覧くだい。 -->

&aname(src);
## Source code

<table class="table-alt">
  <tr>
    <td>C++ source code</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.2/OpenRTM-aist-1.1.2.tar.bz2">OpenRTM-aist-1.1.2.tar.bz2</a> <br>MD5:c270ad187f26e473bf274e8d589fcd8f</td>
    <td>2016.05.27</td>
  </tr>
  <tr>
    <td>C++ source code</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.2/OpenRTM-aist-1.1.2.tar.gz">OpenRTM-aist-1.1.2.tar.gz</a> <br>MD5:e09d05bb93bef22657d133cff20255a4</td>
    <td>2016.05.27</td>
  </tr>
  <tr>
    <td>C++ source for Windows</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.2/OpenRTM-aist-1.1.2-win32.zip">OpenRTM-aist-1.1.2-win32.zip</a> <br>MD5:ade9f4e555d76ca6c29bdd67dd64d42b</td>
    <td>2016.05.27</td>
  </tr>
</table>

### Build from sourcecode

ソースからビルドする方法については、[ソースからのビルド(Windows編)]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/build_source_windows_1_1) または [ソースからのビルド(Linux編)]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/build_source_linux_1_1) をご覧くだい。

### deb/rpmパッケージ作成

1.1から上記の [[ソースコード>#src]] からのUbuntu, Debian 用debパッケージ、Fedora, Vine用 rpmパッケージの作成が正式にサポートされました。<br>
以下の手順でパッケージを作成することができます。パッケージ作成に当たっては、一括インストールスクリプト（pkg_install_***.sh）を利用して必要なパッケージを予めインストールしておいてください。

```
 $ tar xvzf OpenRTM-aist-1.1.2-RELEASE.tar.gz
 $ cd OpenRTM-aist-1.1.2
 $ ./configure --prefix=/usr
 $ cd packages
 $ make
```

パッケージはpacakgesディレクトリ内に作成されます。

<span style="color:red;">※ UbuntuやDebianにてdebパッケージを作成する場合は "dpkg-dev build-essential debhelper devscripts"、Fedoraにてrpmパッケージを作成する場合は "rpm-build createrepo" といったツールを予めインストールしておく必要があります。</span>;

<!-- &br; -->
<!-- ***MacPorts -->
<!-- MacPorts用Portfileが利用可能です。あらかじめXcodeおよびMacPortsをインストールした上でご利用ください。 -->
<!-- - [[Portfile (ports.tgz) :http://www.openrtm.org/pub/MacOSX/macports/ports.tgz]] -->
<!-- - [[インストールスクリプト (port_install.sh) :http://www.openrtm.org/pub/MacOSX/macports/port_install.sh]]: ports.tgz のダウンロード、OpenRTM-aistのビルド・インストールまで自動で行います。 -->

<!-- ** ツール -->

<!-- インストーラのオプションで OpenRTP を選択していれば、インストールする必要はありません。 -->
<!-- ツールを別途インストールする方法については、　[[OpenRTP 1.1.0-RC5:/ja/node/5778]] をご覧ください。 -->

<br>
## リリースノート: 1.1.2-RELEASE
OpenRTM-aist Official Website からソースコード、Windowsインストーラ、Linux用パッケージ等が LGPL ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

<!-- - [[OpenRTM-aist-1.1.0-RELEASE.tar.gz:http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.0/OpenRTM-aist-1.1.0-RELEASE.tar.gz]] -- 2012.05.25リリース -->

### 機能に関する変更
  - 雑多なバグフィックス
<!-- -- RTCの各種動作をフックするリスナ機構の追加 -->
<!-- --- ComponentActionListener: コンポーネントの各種動作をフック可能に -->
<!-- --- PortConnectionListeners: ポートの接続切断をフックする事が可能に -->
<!-- --- ManagerActionListener: マネージャの各種動作のフック -->
<!-- --- ConfigurationListener:コンフィギュレーションの動作のフック -->
<!-- --- ConnectorListener：データポートの送受信の各種動作のフック -->
<!-- -- rtcdでC++だけでなくPython、JavaのRTCプロファイルを取得可能に -->
<!-- -- ECにアクセスするための各種関数群の提供 -->
<!-- -- SDOサービス（プロバイダ・コンシューマ）管理機能の導入 -->
<!-- -- ログのタイムスタンプで ms, usが出力可能 -->
<!-- -- 各種オプションの追加:　manager.auto_shutdown_duration等 -->

### ポータビリティに関する変更
  - 64bitLinunxへの雑多な対応
  - 64bitWindowsへの対応
<!-- -- Mac OS　Xへの正式な対応 -->
<!-- -- Linux+RtORBの正式サポート -->
<!-- -- Cygwin+RtORBの正式サポート -->
<!-- -- MacOS+RtORBの正式サポート -->
  - VC2015(32bit/64bit)の正式サポート
<!-- -- CMakeへの正式対応 -->

### 拡張機能に関する変更
<!-- -- ComponentObserverの提供 -->
<!-- -- RT preemptive kernel用ECの正式サポート -->

### ユーザビリティに関する変更
- Windowsインストーラをアーキテクチャ別の２種類にまとめる
 - １つのインストーラで複数のVisual Studioバージョンに対応
 - C++版、Python版、Java版、rtshellも同時にインストール可能
- WindowsインストーラでomniORBを4.2.1に更新
- WindowsインストーラでOpenCVを2.4.11に更新し、IntelTBBで再コンパイル
<!-- -- WindowsインストーラでツールのRTSystemEditorRCP版とOpenRTPを選択可能にする -->
<!-- -- Windowsインストーラのスタートメニューでのツールを、各言語（C++,Python,Java)で共通にする -->
<!-- -- WindowsインストーラでOpenJDK7 JREのインストールを選択可能にする -->
<!-- -- debパッケージ作成でマルチアーチ機能へ対応 -->
<!-- -- debパッケージ利用環境でOpenRTM-aist Pythonと共存時のアンインストール動作の見直し -->

### 対応 (ビルド検証済) OS
- Debian 7.0 i386, x86_64
- Debian 8.0 i386, x86_64
<!-- ---Fedora release 21 i386, x86_64 -->
<!-- ---Fedora release 22 i386, x86_64 -->
- Ubuntu 12.04 i386, x86_64
- Ubuntu 14.04 i386, x86_64
- Ubuntu 15.10 i386, x86_64
- Ubuntu 16.04 i386, x86_64
- Windows-7 (32/64bit)
- Windows-8.1 (32/64bit)
