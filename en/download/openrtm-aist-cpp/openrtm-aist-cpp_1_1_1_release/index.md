---
layout: page
title: openrtm-aist c++ 1.1.1-release
---

<!-- Title: OpenRTM-aist C++ 1.1.1-RELEASE -->
<div align="right"><a href="cpp_logo.png"><img src="cpp_logo.png" width="15%;" align="right"></a></div>
#contents


- <span style="color:red;">RT-Components for versions 1.0.0 and 1.1.0 are compatible with each other. However, since the port connection rules have slightly changed, tools (for example RTSystemEditor) must support version 1.1.x.</span>;

&aname(src);
## Source Code

<table class="table-alt">
  <tr>
    <td>C++ source code</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.1/OpenRTM-aist-1.1.1.tar.bz2">OpenRTM-aist-1.1.1-RELEASE.tar.bz2</a><br>MD5: 1d030c4972618f2f1e81cf83286af1d0</td>
    <td>2015.03.16</td>
  </tr>
  <tr>
    <td>C++ source code</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.1/OpenRTM-aist-1.1.1.tar.gz">OpenRTM-aist-1.1.1-RELEASE.tar.gz</a><br>MD5: 67abe01eb0e8df1cd3efbcd1ca78108d</td>
    <td>2015.03.16</td>
  </tr>
  <tr>
    <td>C++ source code (for Windows)</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/cxx/1.1.1/OpenRTM-aist-1.1.1-win32.zip">OpenRTM-aist-1.1.1-RELEASE-win32.zip</a><br>MD5: beedc1f16973eb6cc6c2bc7916bafeb7</td>
    <td>2015.03.16</td>
  </tr>
</table>

<br>
## Packages
### Windows Installer

RT System Editor RCP or OpenRTP can be selected. JRE (OpenJDK) is also included. <br>
The default setting is recommended in installing. 
<!-- インストーラで、ツールの RTSystemEditorRCP と OpenRTP を選択できるようになりました。また、ツールを起動するために必要な JRE(OpenJDK) もインストールすることができます。&br; -->
<!-- これらの選択は、デフォルト設定のままインストールすることをお勧めします。オプションの選択については、[[OpenRTM-aistを10分で始めよう！:http://openrtm.org/openrtm/ja/content/lets_start]] のページで手順を紹介しています。 -->

#### 32bit

<!-- - Visual Studioをインストールされている方は、バージョンにあったインストーラーをダウンロードしてください。 -->
- Download the appropriate version of Visual Studio.

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
    <td colspan="3" style="text-align: center;">**Visual Studio 64bit**</td>
  </tr>
  <tr>
    <td>Python-64bit (Needed for tools)<br> Python 2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi">python-2.7.9.amd64.msi</a></td>
    <td><a href="https://www.python.org/">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML (Needed for tools)<br> Pythonのバージョンに合わせること</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.11.win-amd64-py2.7.exe">PyYAML-3.11.win-amd64-py2.7.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
  <tr>
    <td>CMake （To generate Visual C++ project)</td>
    <td><a href="http://www.cmake.org/files/v3.2/cmake-3.2.1-win32-x86.exe">cmake-3.2.1-win32-x86.exe</a></td>
    <td><a href="http://www.cmake.org">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen (To generate documents)</td>
    <td><a href="http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.9.1-setup.exe">doxygen-1.8.9.1-setup.exe</a></td>
    <td><a href="http://www.stack.nl/`dimitri/doxygen/">doxygen</a></td>
    <td>`</td>
  </tr>
</table>


<!-- - 64bit版OpenRTM-aistは、Python 2.7(64bit) がインストールされていれば動作します。 -->
OpenRTM-aist x64 version needs Python 2.7 (x64).


#### Precautions for Windows installation

- <span style="color:red;">* Do not use multiple OpenRTMs with multiple versions of Visual Studio.</span>; Please select and install an appropriate package of your environment.
- Please uninstall older version of OpenRTM-aist before installing version 1.1.1.
<!-- - 古いバージョンのOpenRTM-aistをインストールされている場合は、あらかじめアンインストールすることをお勧めします。　（1.1.1-RELEASEはアンインストールしてもゴミは残りません） -->
- If you uninstall OpenRTM-aist 1.1.0, some files and menu icons in start menu would remain (C++/Python/Java)
<!-- - 1.1.0版をアンインストールしてもファイルとスタートメニューの一部が残ることを確認しています。(C++/Python/Java全てで確認） -->
- You do not have to remove the remainder files of older version, but we recommend to remove them manually for your convenience.
<!-- - 残ったままで新しいバージョンをインストールしても動作に影響はありませんが、手動で削除することをお勧めします。 -->
  - Cautions for the manual remove
<!-- -- 手動で削除する場合の注意： -->
  - If multiple language versions are installed, please upgrade both language versions.
<!-- -- OpenRTM-aistの異なる言語バージョン（例えばC++とPython）をインストールされている場合は、どちらも新しいバージョンに移行することをお勧めします -->
  - After uninstalling older OpenRTM-aist, please remove the following files:
<!-- -- 古いOpenRTM-aistの全てをアンインストール後、手動で下記を削除して下さい -->
    - C:\Program Files (x86)\OpenRTM-aist folder
<!-- --- C:\Program Files (x86) 下の OpenRTM-aist フォルダ -->
    - Start Menu > Programs > OpenRTM-aist menu (Right click and delete)
<!-- --- スタートメニューのOpenRTM-aist　： スタートメニューで表示させて右クリックで削除できます -->


<br>

### Linux Packages

<!-- Linuxパッケージは順次提供される予定です。ソースからのビルドの仕方は以下を参考にしてください。 -->

Currently, the following packages are available. <br>
Please use the installer scripts to install dependencies at the same time.
<!-- 現在のところ以下のディストリビューション・バージョンでパッケージを提供しています。&br; -->
<!-- 以下で配布しているインストールスクリプトを利用すれば、必要なパッケージを一括でインストールすることができます。 -->


<table class="table-alt">
  <tr>
    <th>Distribution Version</th>
    <th>Install Scripts</th>
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

<!-- 1.1.0-RELEASEを既にインストールしている場合は、削除後apt-get updateを実行した上で、再度インストールしてください。 -->
<!-- $ sudo dpkg -r openrtm-aist-doc openrtm-aist-example openrtm-aist-dev openrtm-aist -->
<!-- $ sudo apt-get clean -->
<!-- $ sudo apt-get update -->
<!-- $ sudo apt-get install openrtm-aist openrtm-aist-doc openrtm-aist-example openrtm-aist-dev -->

<!-- 1.1.0-RELEASEを既にインストールしている場合はアップデートが可能です。 -->
If you already installed 1.1.0-RELEASE version, just upgrade it please.

In Ubuntu / Debian

```
 $ sudo apt-get update
 $ sudo apt-get upgrade
```

In Fedora

```
 # yum update
```

<!-- ダウンロード方法・インストール方法については、[[こちら(C++):/ja/node/999]] をご覧くだい。 -->
To download and install, please check [HERE(C++)]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1).


### Build from source code

To build OpenRTM-aist from source code, please check [HERE (Windows)]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/build_source_windows_1_1) or [HERE(Linux)]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/build_source_linux_1_1).
<!-- ソースからビルドする方法については、[[ソースからのビルド(Windows編):/ja/node/793]] または [[ソースからのビルド(Linux編):/ja/node/788]] をご覧くだい。 -->

### deb/rpm package creation

From version 1.1, generating the deb package (for Ubuntu, Debian) and rpm package (Fedora, Vine) is supported. <br>
Please follow the following steps (Please install the dependencies before generating packages)
<!-- 1.1から上記の [[ソースコード>#src]] からのUbuntu, Debian 用debパッケージ、Fedora, Vine用 rpmパッケージの作成が正式にサポートされました。&br; -->
<!-- 以下の手順でパッケージを作成することができます。パッケージ作成に当たっては、一括インストールスクリプト（pkg_install_***.sh）を利用して必要なパッケージを予めインストールしておいてください。 -->

```
 $ tar xvzf OpenRTM-aist-1.1.1-RELEASE.tar.gz
 $ cd OpenRTM-aist-1.1.1
 $ ./configure --prefix=/usr
 $ cd packages
 $ make
```

<!-- パッケージはpacakgesディレクトリ内に作成されます。 -->
The packages are created in packages directory.

<!-- &color(red){※ UbuntuやDebianにてdebパッケージを作成する場合は "dpkg-dev build-essential debhelper devscripts"、Fedoraにてrpmパッケージを作成する場合は "rpm-build createrepo" といったツールを予めインストールしておく必要があります。}; -->
<span style="color:red;">* In Ubuntu, Debian, Install the tools with the command "dpkg-dev build-essential debhelper devscripts". In Fedora, do "rpm-build createrepo"</span>;

<!-- &br; -->
<!-- ***MacPorts -->
<!-- MacPorts用Portfileが利用可能です。あらかじめXcodeおよびMacPortsをインストールした上でご利用ください。 -->
<!-- - [[Portfile (ports.tgz) :http://www.openrtm.org/pub/MacOSX/macports/ports.tgz]] -->
<!-- - [[インストールスクリプト (port_install.sh) :http://www.openrtm.org/pub/MacOSX/macports/port_install.sh]]: ports.tgz のダウンロード、OpenRTM-aistのビルド・インストールまで自動で行います。 -->

## Tool

If OpenRTP is selected when installing OpenRTM-aist, you do not have to install these tools.
<!-- インストーラのオプションで OpenRTP を選択していれば、インストールする必要はありません。 -->
<!-- ツールを別途インストールする方法については、　[[OpenRTP 1.1.0-RC5:/ja/node/5778]] をご覧ください。 -->
If you want to install tools separately, please check [OpenRTP 1.1.0-RC5]({{ site.baseurl }}/en/download/tools/openrtp_1_1_0_rc5).

<br>
## Release note: 1.1.1-RELEASE
From OpenRTM-aist Official Website, Source Code Install, Windows Installer, and Linux packages are available with LGPL License or individual license (please contact us).

<!-- - [[OpenRTM-aist-1.1.0-RELEASE.tar.gz:http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.0/OpenRTM-aist-1.1.0-RELEASE.tar.gz]] -- 2012.05.25リリース -->

### Chanages on Functionarities
  - Bug fixes
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

### Changes on portabilities
  - For 64bitLinunx
  - For 64bitWindows
<!-- -- Mac OS　Xへの正式な対応 -->
<!-- -- Linux+RtORBの正式サポート -->
<!-- -- Cygwin+RtORBの正式サポート -->
<!-- -- MacOS+RtORBの正式サポート -->
  - VC2012(32bit/64bit) Support
  - VC2013(32bit/64bit) Support
<!-- -- CMakeへの正式対応 -->

### Changes on extensions 
<!-- -- ComponentObserverの提供 -->
<!-- -- RT preemptive kernel用ECの正式サポート -->

### Changes on usabilities
- Updated omniORB to 4.1.7 in the Windows installer
- Updated OpenCV to 2.4.9 in the Windows installer and recompiled with Intel TBB
- Added a sample component using OpenCV, ImageCalib (with GUI), to the Windows installer
- Made it possible to select RTSystemEditor (RCP version) and OpenRTP tools in the Windows installer
- Unified the Start Menu tools in the Windows installer across all languages (C++, Python, Java)
- Made installation of OpenJDK 7 JRE optional in the Windows installer
- Added support for multi-architecture (multiarch) in deb package creation
- Reviewed the uninstall behavior when coexisting with OpenRTM-aist Python in environments using deb packages

### Support (Build Tested) OSes
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
