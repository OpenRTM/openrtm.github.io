---
layout: page
title: openrtm-aist c++ 1.1.0-rc2
---
<!-- Title: 1.1.0-RC2 -->
<div align="right"><a href="cpp_logo.png"><img src="cpp_logo.png" width="15%;" align="right"></a></div>
#contents
#clear

- <span style="color:red;">1.1.0-RC1 has already been released for only ROBOMEC2011 tutorial attendees. Please use 1.1.0-RC1 until 1.1.0-RELEASE is released.</span>;
- <span style="color:red;">RTCs built on 1.0.0 and RTCs built on 1.1.0 have compatibility each other, but tool version should be 1.1.0 when you connect 1.0.0's port and 1.1.0's port, because connection method has been changed.</span>;


## Source code

<table class="table-alt">
  <tr>
    <td>C++ source code</td>
    <td><a href="">OpenRTM-aist-1.1.0-RC2.tar.bz2</a>(No corresponding page available.)<br>MD5:fba1dbc10b99381d6c46afd33be4f9ca</td>
    <td>2011.06.06</td>
  </tr>
  <tr>
    <td>C++ source code</td>
    <td><a href="">OpenRTM-aist-1.1.0-RC2.tar.gz</a>(No corresponding page available.)<br>MD5:86bab7c5153e9d0a3ab12311471e36d3</td>
    <td>2011.06.06</td>
  </tr>
  <tr>
    <td>C++ source code for Windows</td>
    <td><a href="">OpenRTM-aist-1.1.0-RC2-win32.zip</a>(No corresponding page available.)<br>MD5:5dfb2359c90f86e4674483b19839eaac</td>
    <td>2011.06.06</td>
  </tr>
</table>

<br>
## Packages
### Windows installer
<table class="table-alt">
  <tr>
    <td colspan="3" style="text-align: center;">CENTER:**for Visual Studio 2008**</td>
  </tr>
  <tr>
    <td>Windows installer</td>
    <td><a href="">OpenRTM-aist-1.1.0-RC2_vc9.msi</a>(No corresponding page available.)<br>MD5:f4f605d8ff3375929a7ab296d792d8bc</td>
    <td>2011.06.06</td>
  </tr>
  <tr>
    <td>Python Windows installer</td>
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


- <span style="color:red;">The Windows installer includes OpenRTM-aist (DLL,header,samples,commands), omniORB-4.1.4, and RTSystemEditor (RCP version). Installing omniORB and the Eclipse tools separately is not necessary.</span>;
- <span style="color:red;">OpenRTM-aist built for Visual Studio 2005 cannot be used with Visual Studio 2008. Download and install the correct package for your development environment.</span>;

<br>
### Linux packages (not provided for RC2)

Linux packages will be provided in the RELEASE version. See the following instructions to build OpenRTM-aist from source code.

- [Building from source]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/build_source_linux_1_1/)

Now the deb packages for Ubuntu and Debian, and the rpm packages for Fedora and Vine, are officially supported by distribution source code.
You can build OpenRTM-aist packages from source code according to the following process.
When you need to make OpenRTM-aist packages, other dependent packages have to be installed before you build it.


```
 $ tar xvzf OpenRTM-aist-1.1.0-RC1.tar.gz
 $ cd OpenRTM-aist-1.1.0
 $ ./configure --prefix=/usr
 $ cd packages
 $ make
```

Packages will be generated under the "pacakges" directory.

<!-- Vine Linux, Fedora, Ubuntu, Debianの各ディストリビューション用のパッケージを www.openrtm.org 上のリポジトリサーバにて配布しています。 -->
<!-- 詳細は、以下のドキュメントを参照してください。 -->

<!-- -[[Vine Linux:/ja/node/1000]] -->
<!-- -[[Fedora:/ja/node/1002/]] -->
<!-- -[[Debian/Ubuntu:/ja/node/1001]] -->

You can install all dependent packages at once by using the following scripts.

<table class="table-alt">
  <tr>
    <td>Distributions</td>
    <td>Supported versions</td>
    <td>Installation scripts</td>
  </tr>
  <tr>
    <td>Vine Linux</td>
    <td>4.0, 4.2, 5.0</td>
    <td><a href="http://openrtm.org/svnroot/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_vine.sh">pkg_install_vine.sh </a></td>
  </tr>
  <tr>
    <td>Fedora</td>
    <td>10, 11, 12 (i386/x86_64)</td>
    <td><a href="http://openrtm.org/svnroot/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_fedora.sh">pkg_install_fedora.sh </a></td>
  </tr>
  <tr>
    <td>Ubuntu</td>
    <td>8.04, 8.10, 9.04, 9.10, 10.04 (i386/x86_64)</td>
    <td><a href="http://openrtm.org/svnroot/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian</td>
    <td>3.1 (i386), 4.0, 5.0 (i386/x86_64)</td>
    <td><a href="http://openrtm.org/svnroot/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_debian.sh">pkg_install_debian.sh </a></td>
  </tr>
</table>

<!-- &br; -->
<!-- ***MacPorts -->
<!-- MacPorts用Portfileが利用可能です。あらかじめXcodeおよびMacPortsをインストールした上でご利用ください。 -->
<!-- - [[Portfile (ports.tgz) :http://www.openrtm.org/pub/MacOSX/macports/ports.tgz]] -->
<!-- - [[インストールスクリプト (port_install.sh) :http://www.openrtm.org/pub/MacOSX/macports/port_install.sh]]: ports.tgz のダウンロード、OpenRTM-aistのビルド・インストールまで自動で行います。 -->

<br>
## Tools
<table class="table-alt">
  <tr>
    <td>Windows all in one<br>(RTSystemEditor1.1.0+RTCBUilder1.1.0)</td>
    <td><a href="">eclipse342_rtmtools110release_win32_ja.zip</a>(No corresponding page available.)<br>MD5:f5619616be753fef7bae9ef863e5b33f</td>
    <td>2011.05.24</td>
  </tr>
  <tr>
    <td>Linux all in one<br>(RTSystemEditor1.1.0+RTCBUilder1.1.0)</td>
    <td><a href="">eclipse342_rtmtools110release_linux_ja.tar.gz</a>(No corresponding page available.)<br>MD5:062355b5963cd0f0a42fb3b8ad43ddc2</td>
    <td>2011.05.24</td>
  </tr>
</table>

<br>
## Release note: 1.1.0-RC1
OpenRTM-aist-1.1.0 release candidate version 2 (RC2) has been released in 6 June, 2011.
From the OpenRTM-aist Official Website, source code and Windows installer package are available under LGPL license or individual licnese.

- [OpenRTM-aist-1.1.0-RC2.tar.gz](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.0/OpenRTM-aist-1.1.0-RC2.tar.gz) -- released in 2011.06.06
  - Some APIs have been added.
    - Call back APIs.
    - Call backs for execution contexts.
  - SDO service frameworks
  - Misc bug fixes.
  - Experimental
    - Observer SDO service has been introduced.
    - CMake file "OpenRTMConfig.cmake" has been introduced (Linux/Windows)
  - Windows installer
    - OpenCV2.1 and some examples are included.
  - Supported OS (build verified)
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
## Old versions
- [1.0.0-RELEASE>OpenRTM-aist-1.0.0-RELEASE]
- [1.0.0-RC1>OpenRTM-aist-1.0.0-RC1]
- [0.4.2-RELESE>OpenRTM-aist-0.4.2-RELEASE]
- [0.4.2-RC2>OpenRTM-aist-0.4.2-RC2]
- [0.4.1-RELEASE>OpenRTM-aist-0.4.1-RELEASE]
- [0.4.0-RELEASE>OpenRTM-aist-0.4.0-RELEASE]
- [0.4.0-RC2>OpenRTM-aist-0.4.0-RC2]
