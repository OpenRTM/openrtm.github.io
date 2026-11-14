---
layout: page
title: openrtm-aist-java-1.2.1-release
---

<!-- Title: OpenRTM-aist-Java-1.2.1-RELEASE -->
<div align="right"><a href="java_logo.png"><img src="java_logo.png" width="10%;" align="right"></a></div>
#contents(4)

<br>
インストール手順については以下のページを参照してください。

- [OpenRTM-aist(Java版)1.2系のインストール]({{ site.baseurl }}/ja/doc/installation/install_1_2/java_1_2)
## パッケージ
### Windowsインストーラー
msiファイルは900MB以上のサイズがあります。ダウンロードを数分で行うためにはある程度高速な回線(50Mbps以上)を用いてください。

#### 64bit用

<table class="table-alt">
  <tr>
    <td>Windows用インストーラー<br> (OpenRTM-aist、C++、Python、<br>Java版、およびOpenRTP、<br> rtshell(4.2.2)を含む)<br>(Visual Studio 2010、2012、<br> 2013、2015、2017、2019共通)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1-RELEASE_x86_64.msi">OpenRTM-aist-1.2.1-RELEASE_x86_64.msi</a> <br>MD5:be6b346d61768435d812cc032bc7a529</td>
    <td>2019/11/25</td>
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
    <td><a href="https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe">python-3.7.5-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.15.5/cmake-3.15.5-win64-x64.msi">cmake-3.15.5-win64-x64.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="https://www.doxygen.nl/files/doxygen-1.9.2-setup.exe">doxygen-1.9.2-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">※Pythonは、"3.7"、"3.6"、"2.7"のいずれかのバージョンをインストールしてください。</span>;
<!-- -&color(red){※古いrtshellは事前に削除しておいてください。ただし、OpenRTM-aist 1.1.2版をmsiファイルを用いてインストールしている場合は対応不要です。}; -->
- Doxygenは最新版がリリースされると上記のダウンロードリンクが切れることがあります。その際は[doxygen](http://www.doxygen.nl/index.html)のダウンロードページに移動し、最新の "doxygen-X.X.X-setup.exe" をダウンロード・インストールしてください。

#### 32bit用

<table class="table-alt">
  <tr>
    <td>Windows用インストーラー<br> (OpenRTM-aist、C++、Python、<br>Java版、およびOpenRTP、<br>rtshell(4.2.2)を含む)<br>(Visual Studio 2010、2012、<br>2013、2015、2017、2019 共通)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1-RELEASE_x86.msi">OpenRTM-aist-1.2.1-RELEASE_x86.msi</a> <br>MD5:a9186d409cafc039432a0e1c6e7e02ef</td>
    <td>2019/11/25</td>
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
    <td><a href="https://www.python.org/ftp/python/3.7.5/python-3.7.5.exe">python-3.7.5.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.15.5/cmake-3.15.5-win32-x86.msi">cmake-3.15.5-win32-x86.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="https://www.doxygen.nl/files/doxygen-1.9.2-setup.exe">doxygen-1.9.2-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">※Pythonは、"3.7"、"3.6"、"2.7"のいずれかのバージョンをインストールしてください。</span>;
<!-- -&color(red){※古いrtshellは事前に削除しておいてください。ただし、OpenRTM-aist 1.1.2版をmsiファイルを用いてインストールしている場合は対応不要です。}; -->
- Doxygenは最新版がリリースされると上記のダウンロードリンクが切れることがあります。その際は[doxygen](http://www.doxygen.nl/index.html)のダウンロードページに移動し、最新の "doxygen-X.X.X-setup.exe" をダウンロード・インストールしてください。

インストールについては、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/lets_start121)のページで手順を紹介しています。<br>

<br>
### Linuxパッケージ

現在のところ、以下のディストリビューション・バージョンでパッケージを提供しています。<br>
以下で配布しているインストールスクリプトを利用すれば、必要なパッケージを一括でインストールできます。


<table class="table-alt">
  <tr>
    <th>ディストリビューション・バージョン</th>
    <th>一括インストールスクリプト(右クリックでURLを入手)</th>
  </tr>
  <tr>
    <td>Ubuntu 16.04 (xenial) i386/amd64 <br> Ubuntu 18.04 (bionic) amd64 <br></td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Raspbian Buster armhf</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_raspbian.sh">pkg_install_raspbian.sh</a></td>
  </tr>
</table>
<!-- | Debian  8.0  (jessie) i386/amd64 &br; Debian  9.0  (stretch) i386/amd64| [[pkg_install_debian.sh >https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_debian.sh]] | -->
<!-- | Fedora 27 i686/x86_64 &br; Fedora 28 i686/x86_64 &br; Fedora 29 i686/x86_64| [[pkg_install_fedora.sh >https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_fedora.sh]] | -->

<!-- ※Fedora用一括インストール・スクリプトはOpenRTM-aist 1.2.0版以降対応予定です。 -->

オプションを指定することで、目的に合わせたパッケージをインストールできるようになりました。インストール方法やオプション、パッケージの種類につきましては、[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)をご確認ください。

## Java開発環境

OpenRTM-aist-Java-1.2.1の動作および開発には以下のJDKが必要です。
- JDK8(1.8): [JDK8のインストール]({{ site.baseurl }}/ja/doc/installation/common/install_jdk8)

&aname(src);
## ソースコード

<table class="table-alt">
  <tr>
    <td>Java版ソースコード</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.1/OpenRTM-aist-Java-1.2.1.tar.gz">OpenRTM-aist-Java-1.2.1.tar.gz</a> <br>MD5:0db80c61d07d69d5790116f95c7dfbfd</td>
    <td>2019/11/25</td>
  </tr>
  <tr>
    <td>Java版ソースコード</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.1/OpenRTM-aist-Java-1.2.1.zip">OpenRTM-aist-Java-1.2.1.zip</a> <br>MD5:be5082e762ec45f17434a9072ed2ba7d</td>
    <td>2019/11/25</td>
  </tr>
  <tr>
    <td>jarファイルおよびサンプル</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.1/OpenRTM-aist-Java-1.2.1-jar.zip">OpenRTM-aist-Java-1.2.1-jar.zip</a> <br>MD5:359384b4be31524ad84ed06cf6477c39</td>
    <td>2019/11/25</td>
  </tr>
</table>


### ソースからのビルド

ソースからビルドする方法については、[ソースからのビルド]({{ site.baseurl }}/ja/doc/installation/install_1_2/java_1_2/build_source_java_1_2)をご覧くだい。

### deb/rpmパッケージ作成

jarファイルおよびサンプルからのUbuntu、Debian用debパッケージ、Fedora用rpmパッケージの作成が正式にサポートされました。<br>
以下の手順でパッケージを作成できます。パッケージ作成に当たっては、一括インストールスクリプト（pkg_install_***.sh）を利用して必要なパッケージをあらかじめインストールしておいてください。
```
 $ tar xvzf OpenRTM-aist-Java-1.2.1.tar.gz
 $ unzip OpenRTM-aist-Java-1.2.1-jar.zip
 $ cd OpenRTM-aist/1.2/
 $ cp -r ../../OpenRTM-aist-Java/packages .
```

```
 debパッケージを作成する場合
 $ cd packages/deb
 $ sh dpkg_build.sh
```

```
 rpmパッケージを作成する場合
 $ cd packages/rpm
 $ sh rpm_build.sh
```

パッケージはpacakgesディレクトリ内に作成されます。

<span style="color:red;">※UbuntuやDebianにてdebパッケージを作成する場合は"dpkg-dev build-essential debhelper devscripts"、Fedoraにてrpmパッケージを作成する場合は"rpm-build createrepo"といったツールをあらかじめインストールしておく必要があります。</span>;
これらは、[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)を-cオプションで実行すればインストールされます。

## リリースノート
- [1.2.1-RELEASE ](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/tag/v1.2.1)

### 対応(ビルド検証済)OS
- Ubuntu 16.04 i386、 amd64
- Ubuntu 18.04 amd64
- Raspbian Buster armhf
- Windows-10 (32/64bit)
