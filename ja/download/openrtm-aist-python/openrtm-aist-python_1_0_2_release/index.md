---
layout: page
title: openrtm-aist-python-1.0.2-release
---

<!-- Title: OpenRTM-aist-Python-1.0.2-RELEASE -->
<div align="left"><a href="python-logo.png"><img src="python-logo.png" width="15%;" align="left"></a></div>
#contents
#clear
<br>
<br>
<br>

## 注意事項

バージョン 0.4 系をインストール済みの環境に 1.0 系をインストールする場合は、一度 0.4 系を削除してから 1.0 系のインストールを行ってください。
0.4 系をアンインストールした後に 0.4 系の残骸が残っている場合がございますので、残骸が残っている場合は手動で OpenRTM フォルダーの削除を行ってください。

:削除するフォルダー|
- Windows 環境の場合:
```
 C:\Python[24,25,26]\Lib\site-packages\OpenRTM
```
- Linux 環境の場合:
```
  /usr/lib/python[2.4,2.5,2.6]/site-packages/OpenRTM
```

&aname(source)
## ソースコード
<table class="table-alt">
  <tr>
    <td>Python版ソースコード</td>
    <td><a href="">OpenRTM-aist-Python-1.0.2-RELEASE.tar.gz</a>（リンク切れです） <br> MD5:f0305d41777a0397ea2beed85e3f5c27</td>
    <td>12/02/20</td>
  </tr>
  <tr>
    <td>Python版ソースコード(Win32)</td>
    <td><a href="">OpenRTM-aist-Python-1.0.2-RELEASE.zip</a>（リンク切れです） <br> MD5:1d139a712614487c13b47315c878dddf</td>
    <td>12/02/20</td>
  </tr>
</table>


<br>
<!-- **パッケージ -->
<!-- ***&aname(winpkg){Windows インストーラー (Python 2.4、2.5、2.6 共通)}; -->

<!-- OpenRTM-aist-Python-1.0.0.msi を使用して OpenRTM-aist-Python をインストールする場合、Python のバージョン2.4、2.5、2.6 のいずれかが必要です。 -->
<!-- OpenRTM-aist-Python-1.0.0.msi では、インストールされている Python のバージョンを検出し、それぞれに OpenRTM-aist-Python-1.0.0 と omniORBpy をインストールします。別途 omniORBpy をインストールする必要はありません。 -->


<!-- |LEFT:200|LEFT|LEFT:100|c -->
<!-- |Windows 用インストーラー|[[OpenRTM-aist-Python-1.0.0.msi:http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python-1.0.0.msi]] &br; MD5:4afe4de69c9b56086fc97e9697334a36 | 10/05/07 | -->
<!-- |Windows 用インストーラー|[[OpenRTM-aist-Python-1.0.1.msi:http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python-1.0.1.msi]] &br; MD5:ad9653ab2a07a4247b7b4ad0cf069002 | 11/02/23 | -->
<!-- |Python-2.4.4|[[python-2.4.4.msi:http://www.python.org/ftp/python/2.4.4/python-2.4.4.msi]]|[[python.org:http://www.python.org]]| -->
<!-- |Python-2.5.1|[[python-2.5.1.msi:http://www.python.org/ftp/python/2.5.1/python-2.5.1.msi]]|[[python.org:http://www.python.org]]| -->
<!-- |Python-2.6.2|[[python-2.6.2.msi:http://www.python.org/ftp/python/2.6.2/python-2.6.2.msi]]|[[python.org:http://www.python.org]]| -->

<br>
&aname(linuxpkg)
### Linux パッケージ
Vine Linux、Fedora、Ubuntu、Debian の各ディストリビューション用のパッケージを www.openrtm.org 上のリポジトリサーバーにて配布しています。
詳細は、以下のドキュメントを参照してください。

- [Vine Linux へのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_vine_python_1_1)
- [Fedora へのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_fedora_python_1_1)
- [Ubuntu/Debian へのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_ubuntu_python_1_1)


<table class="table-alt">
  <tr>
    <th>ディストリビューション</th>
    <th>対応バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Vine Linux</td>
    <td>4.0, 4.2(i386のみ), 5.0 (i386, x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_vine.sh">pkg_install_python_vine.sh </a></td>
  </tr>
  <tr>
    <td>Fedora</td>
    <td>11, 12 (共にi386/x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_fedora.sh">pkg_install_python_fedora.sh </a></td>
  </tr>
  <tr>
    <td>Ubuntu</td>
    <td>8.04, 8.10, 9.04, 9.10, 10.04 (共にi386/x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh">pkg_install_python_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian</td>
    <td>3.1 (i386), 4.0, 5.0 (共にi386, x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_debian.sh">pkg_install_python_debian.sh </a></td>
  </tr>
</table>


<br>
&aname(note);
## リリースノート: 1.0.2-RELEASE

- [OpenRTM-aist-Python-1.0.2-RELEASE.tar.gz]()（リンク切れです） -- 2012.02.20リリース
  - Python 2.7 での SystemLogger の問題修正
  - 動作条件
  - サポートする Python バージョン
    - 2.4
    - 2.5
    - 2.6

