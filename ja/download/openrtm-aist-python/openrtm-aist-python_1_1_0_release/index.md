---
layout: page
title: openrtm-aist-python-1.1.0-release
---

<!-- Title: OpenRTM-aist-Python-1.1.0-RELEASE -->
<div align="right"><a href="python-logo.png"><img src="python-logo.png" width="15%;" align="right"></a></div>
#contents

<!-- -&color(red){まだリリースしておりません。準備中です。もうしばらくお待ち下さい。}; -->

## ソースコード

<table class="table-alt">
  <tr>
    <td>Python 版ソースコード</td>
    <td><a href="">OpenRTM-aist-Python-1.1.0-RELEASE.tar.gz</a>（リンク切れです）<br>MD5:745cc9a2de717f52ef63b614cf4ad68d</td>
    <td>2015/03/03</td>
  </tr>
  <tr>
    <td>Python 版ソースコード(Win32)</td>
    <td><a href="">OpenRTM-aist-Python-1.1.0-RELEASE.zip</a>（リンク切れです）<br>MD5:cfb11e4111108759265909428e34d91c</td>
    <td>2015/03/03</td>
  </tr>
</table>

<br>
## パッケージ
### Windows インストーラー

OpenRTM-aist-Python-1.1.0-RELEASE.msi を使用して OpenRTM-aist-Python をインストールする場合、Python のバージョンは 2.6、2.7 のいずれかが必要です。
OpenRTM-aist-Python-1.1.0-RELEASE_***.msi では、インストールされている Pythonの バージョンを検出し、それぞれに OpenRTM-aist-Python-1.1.0 と omniORBpy をインストールします。別途 omniORBpy をインストールする必要はありません。

#### 32bit 用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python_1.1.0-RELEASE_x86.msi">OpenRTM-aist-Python_1.1.0-RELEASE_x86.msi</a><br>MD5: 2403500ecd278199e2483742e59faa73</td>
    <td>2015/03/20</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi">python-2.7.10.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

<!-- -&color(red){※ RTSystemEditor(RCP 版 ) を動作させるために、32bit 版の Java 動作環境 (JRE) または Java 開発環境 (JDK) が必要となります。}; -->
- <span style="color:red;">※ Python 2.7.11 は PYTHONPATH 等環境変数を設定しないと動作しないケースがあるようなので、当面は 2.7.10 をお使いください。</span>;

#### 64bit 用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python_1.1.0-RELEASE_x86_64.msi">OpenRTM-aist-Python_1.1.0-RELEASE_x86_64.msi</a><br>MD5: 73791f692a29dbee891e2e0fc9900202</td>
    <td>2015/03/20</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.amd64.msi">python-2.7.10.amd64.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python 2.7.11 は PYTHONPATH 等環境変数を設定しないと動作しないケースがあるようなので、当面は 2.7.10 をお使いください。</span>;

#### omnipy が import できない旨のエラーが出る場合

MSVCR71.dll、MSVCP71.dll がインストールされていないため、omnipy が import できない旨のエラーが出る場合があります。
下記よりMSVCR71.dll、MSVCP71.dll をダウンロードしてインストールしてください。

- http://www.vector.co.jp/soft/win95/util/se435079.html

ダウンロード後解凍して、MSVCR71.dll、MSVCP71.dll を
- 32bit Windows の場合 C:\Windows\system32 
- 64bit Windows の場合 C:\Windows\SysWow64
にインストールしてください。


<br>

### Linux パッケージ
Ubuntu、Debian、Fedora の各ディストリビューション用パッケージを openrtm.org 上のリポジトリサーバーにて配布しています。
詳細は、以下のドキュメントを参照してください。~

- [Ubuntu/Debian へのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_ubuntu_python_1_1)
- [Fedora へのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_fedora_python_1_1)


<table class="table-alt">
  <tr>
    <th>ディストリビューション・バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Ubuntu 12.04 (precise) i386/amd64 <br> Ubuntu 14.04 (trusty) i386/amd64 <br> Ubuntu 14.10 (utopic) i386/amd64 <br> Ubuntu 15.04 (vivid) i386/amd64</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh">pkg_install_python_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian  6.0  (squeeze) i386/amd64 <br> Debian  7.0  (wheezy) i386/amd64</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_debian.sh">pkg_install_python_debian.sh </a></td>
  </tr>
  <tr>
    <td>Fedora 19 i386/amd64 <br> Fedora 20 i386/amd64 <br> Fedora 21 i386/amd64</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_fedora.sh">pkg_install_python_fedora.sh </a></td>
  </tr>
</table>


<br>

## リリースノート: 1.1.0-RELEASE

RTミドルウエア：OpenRTM-aist の Python言語版最新バージョン 1.1.0-RELEASE をリリースいたしました。

OpenRTM-aist Official Website からソースコード、Windowsインストーラー、Linux 用パッケージ等が LGPL ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

- 雑多なバグフィックス
- 64bit Windows への対応
- 64bit Linux への対応
- Windows インストーラーで RTSystemEditorRCP をマージモジュールで組込む
- Windows インストーラーへ JRE を追加
- deb パッケージ利用環境で OpenRTM-aist C++と共存時のアンインストール動作の見直し
- 動作条件
- サポートする Pythonバージョン
 - 2.6
 - 2.7
- 動作確認済み OS
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
