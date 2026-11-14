---
layout: page
title: openrtm-aist-python-1.1.2-release
---

<!-- Title: OpenRTM-aist-Python-1.1.2-RELEASE -->
<div align="right"><a href="python-logo.png"><img src="python-logo.png" width="15%;" align="right"></a></div>
#contents

<!-- -&color(red){まだリリースしておりません。準備中です。もうしばらくお待ち下さい。}; -->

<br>
## パッケージ
### Windows インストーラー

<!-- 本バージョンから Python版だけでなく、C++版、Java版、rtshell も同時にインストール可能になりました。これらの古いバージョンをインストールされている場合は、あらかじめすべてアンインストールしてください。 -->
<!-- -&color(red){rtshell は 4.1.0 版がインストールされます。合わせて rtctree と rtsprofile も自動でインストールされます。rtshell、rtctree、rtsprofile の古いバージョンは完全に削除されていることを確認してください。}; -->


<!-- Python版だけをインストールしたい場合は、カスタムセットアップで選択して下さい。その際 IDL ファイルも同時にインストールされますので、ツールの OpenRTP も選択すれば開発は可能です。 -->

<!-- OpenRTM-aist-1.1.2-RELEASE_***.msiを使用してOpenRTM-aist-Python をインストールする場合、Python のバージョンは 2.7 が必要です。 -->
<!-- インストールされている Python のバージョンを検出し、それぞれに OpenRTM-aist-Python-1.1.2 と omniORBpy をインストールします。別途 omniORBpy をインストールする必要はありません。 -->

#### 32bit 用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist C++、Python、Java版<br> および OpenRTP、rtshell (4.1.0) 含む)</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/1.1/OpenRTM-aist-1.1.2-RELEASE_x86.msi">OpenRTM-aist-1.1.2-RELEASE_x86.msi</a> <br>MD5:59be8603f3fc007c2aed4476052886ce</td>
    <td>2016/05/27</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi">python-2.7.10.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python 2.7.10 推奨。2.7.11 は PYTHONPATH 等環境変数の設定が必要な場合があります。</span>;
- <span style="color:red;">※ 古い rtshell は事前に削除しておいてください。</span>;

#### 64bit 用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist C++、Python、Java版<br> および OpenRTP、rtshell (4.1.0) 含む)</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/1.1/OpenRTM-aist-1.1.2-RELEASE_x86_64.msi">OpenRTM-aist-1.1.2-RELEASE_x86_64.msi</a> <br>MD5:ee8db7c1682cb21dce963207e0484fb3</td>
    <td>2016/05/27</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.amd64.msi">python-2.7.10.amd64.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python 2.7.10 推奨。2.7.11は PYTHONPATH 等環境変数の設定が必要な場合があります。</span>;
- <span style="color:red;">※ 古い rtshell は事前に削除しておいてください。</span>;

インストールについては、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/quick_start_1_1_2) のページで手順を紹介しています。<br>


<!-- **** omnipy が import できない旨のエラーが出る場合 -->

<!-- MSVCR71.dll、MSVCP71.dll がインストールされていないため、omnipy が import できない旨のエラーが出る場合があります。 -->
<!-- 下記よりMSVCR71.dll、MSVCP71.dll をダウンロードしてインストールしてください。 -->

<!-- - http://www.vector.co.jp/soft/win95/util/se435079.html -->

<!-- ダウンロード後解凍して、MSVCR71.dll、MSVCP71.dll を -->
<!-- - 32bit Windows の場合 C:\Windows\system32  -->
<!-- - 64bit Windows の場合 C:\Windows\SysWow64 -->
<!-- にインストールしてください。 -->


<br>

### Linux パッケージ
Ubuntu、Debian、Fedora の各ディストリビューション用パッケージを openrtm.org 上のリポジトリサーバーにて配布しています。
詳細は、以下のドキュメントを参照してください。~

- [Ubuntu/Debian へのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_ubuntu_python_1_1)
- [Fedora へのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_fedora_python_1_1)

<!-- [[古pkg_install_ubuntu.sh >http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-aist/build/pkg_install_ubuntu.sh]]  -->
<!-- [[古pkg_install_debian.sh >http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-aist/build/pkg_install_debian.sh]] -->
<!-- [[古pkg_install_fedora.sh >http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_fedora.sh]]  -->

<table class="table-alt">
  <tr>
    <th>ディストリビューション・バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Ubuntu 14.04 (trusty) i386/amd64/arm64 <br>  Ubuntu 16.04 (xenial) i386/amd64/arm64 <br> Ubuntu 16.10 (yakkety) i386/amd64 <br> Ubuntu 17.04 (zesty) i386/amd64 <br> Ubuntu 17.10 (artful) i386/amd64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian  7.0  (wheezy) i386/amd64 <br> Debian  8.0  (jessie) i386/amd64 <br> Debian  9.0  (stretch) i386/amd64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_debian.sh">pkg_install_debian.sh </a></td>
  </tr>
  <tr>
    <td>Fedora 23 i386/amd64 <br> Fedora 24 i386/amd64 <br> Fedora 25 i386/amd64<br> Fedora 26 i386/amd64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_fedora.sh">pkg_install_fedora.sh </a></td>
  </tr>
</table>

<!-- ※ Fedora用一括インストール・スクリプトはOpenRTM-aist 1.2.0版以降対応予定です。 -->

オプションを指定することで、目的に合わせたパッケージをインストールすることができるようになりました。インストール方法やオプション、パッケージの種類につきましては、[こちら]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)をご確認ください。

<!-- | ディストリビューション・バージョン | 一括インストールスクリプト | -->
<!-- | Ubuntu 12.04 (precise) i386/amd64 &br; Ubuntu 14.04 (trusty) i386/amd64/arm64 &br; Ubuntu 15.10 (wily) i386/amd64 &br; Ubuntu 16.04 (xenial) i386/amd64/arm64| [[pkg_install_python_ubuntu.sh >http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_2/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh]] | -->
<!-- | Debian  7.0  (wheezy) i386/amd64 &br; Debian  8.0  (jessie) i386/amd64| [[pkg_install_python_debian.sh >http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_2/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_debian.sh]] | -->
<!-- | Fedora 21 i386/amd64 &br; Fedora 22 i386/amd64 &br; Fedora 23 i386/amd64| [[pkg_install_python_fedora.sh >http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_fedora.sh]] | -->

## ソースコード

<table class="table-alt">
  <tr>
    <td>Python版ソースコード</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/python/1.1.2/OpenRTM-aist-Python-1.1.2.tar.gz">OpenRTM-aist-Python-1.1.2.tar.gz</a> <br>MD5:15e107e73dd5a60bebb675b561b86633</td>
    <td>2016/05/27</td>
  </tr>
  <tr>
    <td>Python版ソースコード(Win32)</td>
    <td><a href="http://openrtm.org/pub/OpenRTM-aist/python/1.1.2/OpenRTM-aist-Python-1.1.2.zip">OpenRTM-aist-Python-1.1.2.zip</a> <br>MD5:0641a1e6f3f21b89ac62e35ffcf8d73d</td>
    <td>2016/05/27</td>
  </tr>
</table>



<br>

## リリースノート: 1.1.2-RELEASE

RTミドルウエア：OpenRTM-aist の Python言語版最新バージョン 1.1.2-RELEASE をリリースいたしました。

OpenRTM-aist Official Website からソースコード、Windows インストーラー、Linux 用パッケージ等が LGPL ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

- 雑多なバグフィックス
- 64bit Windowsへの対応
- 64bit Linuxへの対応
- Windows インストーラーで Python版、C++版、Java版、rtshell も同時にインストール可能
- Windows インストーラーで omniORBpy を 4.2.x に更新
- 動作条件
  - サポートする Python バージョン： 2.7
- 動作確認済みOS
  - Debian 7.0 i386, x86_64
  - Debian 8.0 i386, x86_64
  - Fedora release 21 i386, x86_64
  - Fedora release 22 i386, x86_64
  - Ubuntu 12.04 i386, x86_64
  - Ubuntu 14.04 i386, x86_64
  - Ubuntu 15.10 i386, x86_64
  - Ubuntu 16.04 i386, x86_64
  - Windows-7 (32/64bit)
  - Windows-8.1 (32/64bit)
