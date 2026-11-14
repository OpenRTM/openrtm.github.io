---
layout: page
title: openrtp 1.2.1
---

<!-- Title: OpenRTP 1.2.1 -->
<div align="right"><a href="eclipse_logo.png"><img src="eclipse_logo.png" width="15%;" align="right"></a></div>
#contents(5)

&aname(package);
## パッケージ

1.2.1版はEclipse-4.7.3ベースです。

### Windowsインストーラー
msiファイルは900MB以上のサイズがあります。ダウンロードを数分で行うためにはある程度高速な回線(50Mbps以上)を用いてください。

#### 64bit用

<table class="table-alt">
  <tr>
    <td>Windows用インストーラー<br> (OpenRTM-aist、C++、Python、<br>Java版、および OpenRTP、<br> rtshell (4.2.2)を含む)<br>(Visual Studio 2010、2012、<br> 2013、2015、2017、2019 共通)</td>
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
    <td><a href="http://doxygen.nl/files/doxygen-1.8.16-setup.exe">doxygen-1.8.16-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">※Pythonは、"3.7"、"3.6"、"2.7"のいずれかのバージョンをインストールしてください。</span>;
<!-- -&color(red){※古いrtshellは事前に削除しておいてください。ただし、OpenRTM-aist 1.1.2版をmsiを用いてでインストールしている場合は対応不要です。}; -->

#### 32bit用

<table class="table-alt">
  <tr>
    <td>Windows用インストーラー<br> (OpenRTM-aist、C++、Python、<br>Java版、および OpenRTP、<br>rtshell(4.2.2) 含む)<br>(Visual Studio 2010、2012、<br>2013、2015、2017、2019 共通)</td>
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
    <td><a href="http://doxygen.nl/files/doxygen-1.8.16-setup.exe">doxygen-1.8.16-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">※Pythonは、"3.7"、"3.6"、"2.7"のいずれかのバージョンをインストールしてください。</span>;
<!-- -&color(red){※古いrtshellは事前に削除しておいてください。ただし、OpenRTM-aist 1.1.2版をmsiを用いてインストールしている場合は対応不要です。}; -->


インストールについては、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/lets_start121)のページで手順を紹介しています。<br>


&aname(dl_allinone_linux);
### Linuxパッケージ

現在のところ、以下のディストリビューション・バージョンでパッケージを提供しています。<br>
以下で配布しているインストールスクリプトを利用すれば、必要なパッケージを一括でインストールできます。


<table class="table-alt">
  <tr>
    <th>ディストリビューション・バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Ubuntu 16.04 (xenial) i386/amd64 <br> Ubuntu 18.04 (bionic) amd64 <br></td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
</table>
<!-- | Debian  8.0  (jessie) i386/amd64 &br; Debian  9.0  (stretch) i386/amd64| [[pkg_install_debian.sh >https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_debian.sh]] | -->
<!-- | Fedora 27 i686/x86_64 &br; Fedora 28 i686/x86_64 &br; Fedora 29 i686/x86_64| [[pkg_install_fedora.sh >https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_fedora.sh]] | -->

<!-- ※Fedora用一括インストール・スクリプトはOpenRTM-aist 1.2.0版以降対応予定です。 -->

オプションを指定することで、目的に合わせたパッケージをインストールできるようになりました。インストール方法やオプション、パッケージの種類につきましては、[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)をご確認ください。
### JDK8のインストール
OpenRTPの実行にはJDK8を別途インストールする必要がある場合があります。
```
 Java -version
```
コマンドで1.8.0等のJDK8を意味するバージョンが表示されない場合や、ライセンス等の理由により違ったディストリビューションをインストールしたい場合は下記のリンクを参考にしてインストールしてください。
- [JDK8のインストール]({{ site.baseurl }}/ja/doc/installation/common/install_jdk8)

### OpenRTPの起動方法
&aname(dl_allinone_win);

#### Windowsでの起動

デスクトップのショートカットをクリックして起動します。スタートメニューでは、[OpenRTM-aist 1.2.1 ***]をクリックすると表示されるメニュー群からOpenRTPをクリックします。
[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/lets_start121)のページで手順を紹介しています。

#### Linuxでの起動

任意のディレクトリで、openrtpコマンドで起動できます。

## リリースノート

- [1.2.1-RELEASE ](https://github.com/OpenRTM/OpenRTP-aist/releases/tag/v1.2.1)

### 対応(ビルド検証済)OS
- Ubuntu 16.04 i386、 amd64
- Ubuntu 18.04 amd64
- Windows-10 (32/64bit)


