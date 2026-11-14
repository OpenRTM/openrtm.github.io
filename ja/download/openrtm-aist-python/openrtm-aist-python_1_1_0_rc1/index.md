---
layout: page
title: openrtm-aist-python-1.1.0-rc1
---

<!-- OpenRTM-aist-Python-1.1.0-RC1 -->
<div align="left"><a href="python-logo.png"><img src="python-logo.png" width="15%;" align="left"></a></div>
#contents
#clear
<br>
<br>
<br>
## 注意事項

バージョン0.4系をインストール済みの環境に1.x系をインストールする場合は、一度0.4系を削除してから1.x系のインストールを行ってください。
0.4系をアンインストールした後に0.4系の残骸が残っている場合がございますので、残骸が残っている場合は手動でOpenRTMフォルダの削除を行って下さい。

:削除するフォルダ|
- Windows環境の場合:
```
 C:\Python[24,25,26]\Lib\site-packages\OpenRTM
```
- Linux環境の場合:
```
  /usr/lib/python[2.4,2.5,2.6]/site-packages/OpenRTM
```

## ソースコード
<table class="table-alt">
  <tr>
    <td>Python版ソースコード</td>
    <td><a href="">OpenRTM-aist-Python-1.1.0-RC1.tar.gz</a>（リンク切れです） <br> MD5:bbc9c4915d13cef0f5a925a070bab0aa</td>
    <td>11/10/04</td>
  </tr>
  <tr>
    <td>Python版ソースコード(Win32)</td>
    <td><a href="">OpenRTM-aist-Python-1.1.0-RC1.zip</a>（リンク切れです） <br> MD5:513f9a80ab7ce3c4d831c509e2252a8b</td>
    <td>11/10/04</td>
  </tr>
</table>


<br>
## パッケージ
### Windowsインストーラ (Python 2.4,2.5,2.6 共通)

OpenRTM-aist-Python-1.1.0-RC1.msiを使用してOpenRTM-aist-Pythonをインストールする場合、Pythonのバージョン2.4、2.5、2.6のいずれかが必要です。
OpenRTM-aist-Python-1.1.0-RC1.msiでは、インストールされているPythonのバージョンを検出し、それぞれにOpenRTM-aist-Python-1.1.0とomniORBpyをインストールします。別途omniORBpyをインストールする必要はありません。


<table class="table-alt">
  <tr>
    <td>Windows用インストーラ</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python-1.1.0-RC1.msi">OpenRTM-aist-Python-1.1.0-RC1.msi</a> <br> MD5:1faaf9c25bcb879628da3d23f851a4cd</td>
    <td>11/010/04</td>
  </tr>
  <tr>
    <td>Python-2.4.4</td>
    <td><a href="http://www.python.org/ftp/python/2.4.4/python-2.4.4.msi">python-2.4.4.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-2.5.4</td>
    <td><a href="http://www.python.org/ftp/python/2.5.4/python-2.5.4.msi">python-2.5.1.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-2.6.6</td>
    <td><a href="http://www.python.org/ftp/python/2.6.6/python-2.6.6.msi">python-2.6.2.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Java: Windows (32bit) 用 JRE</td>
    <td><a href="http://javadl.sun.com/webapps/download/AutoDL?BundleId=63691">インストーラ</a></td>
    <td><a href="http://java.com/ja/download/manual.jsp">java.com</a></td>
  </tr>
</table>

- &color(red){※ RTSystemEditor(RCP 版 ) を動作させるために、32 ビット版の Java 動作環境 (JRE) または Java 開発環境 (JDK) が必要となります。
- <span style="color:red;">※ Pythonのバージョンによってpython.exe にパスが通らないケースがあります。パスをチェックしてください。</span>;


#### omnipy が importできない旨のエラーが出る場合

MSVCR71.dll, MSVCP71.dll がインストールされていないため、omnipy が importできない旨のエラーが出る場合があります。
下記よりMSVCR71.dll, MSVCP71.dllをダウンロードしてインストールしてください。

- http://www.vector.co.jp/soft/win95/util/se435079.html

ダウンロード後解凍して、MSVCR71.dll, MSVCP71.dllを
- 32bit Windows の場合 C:\Windows\system32 
- 64bit Windows の場合 C:\Windows\SysWow64
にインストールしてください。


<br>

### Linuxパッケージ
Ubuntu, Debianの各ディストリビューション用のパッケージを www.openrtm.org 上のリポジトリサーバにて配布しています。
詳細は、以下のドキュメントを参照してください。~
Fedora版は、もうしばらくお待ちください。

- [Vine Linuxへのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_vine_python_1_1)
- [Fedoraへのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_fedora_python_1_1)
- [Ubuntu/Debianへのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_ubuntu_python_1_1)


<table class="table-alt">
  <tr>
    <th>ディストリビューション</th>
    <th>対応バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
<!-- | Fedora | 11, 12 (共にi386/x86_64) |[[pkg_install_python_fedora.sh >http://www.openrtm.org/pub/OpenRTM-aist/python/install_scripts/pkg_install_python_fedora.sh]]| -->
  <tr>
    <th>Ubuntu</th>
    <th>8.04, 10.04, 10.10, 11.04 (共にi386/x86_64)</th>
    <th><a href="http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh">pkg_install_python_ubuntu.sh </a></th>
  </tr>
  <tr>
    <td>Debian</td>
    <td>5.0 (i386, x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_debian.sh">pkg_install_python_debian.sh </a></td>
  </tr>
</table>


<br>

## リリースノート: 1.1.0-RC1

RTミドルウエア：OpenRTM-aist のPython言語版最新バージョン 1.1.0-RC1 を10月4日にリリースいたしました。

OpenRTM-aist Official Website からソースコード、Windowsインストーラ、Linux用パッケージ等が LGPL ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

これまでは、実行・開発環境を構築するには、いくつかのパッケージをインストールする必要がありましたが、今回のリリースでは、特にWindows用には、omniORBpyやツール等を含むインストーラを提供することにより、どなたでもすぐにサンプルを実行して試用可能となりました。ぜひお試しください。

- [OpenRTM-aist-Python-1.1.0-RC1.tar.gz]()（リンク切れです） -- 2011.10.04リリース
  - APIの追加
    - コールバックAPI
    - 実行コンテキストに関するコールバック
  - rtc.conf新オプション(-o)の導入
  - ECのrateをrtc.confで与えられるよう変更
  - SDOサービスフレームワーク
  - オブザーバSDOサービスの導入(実験的)
  - 雑多なバグフィックス

  - 動作条件
  - サポートするPythonバージョン
    - 2.4
    - 2.5
    - 2.6
  - 動作確認済みOS
    - Debian5.0-i386
    - Ubuntu 8.04-i386
    - Ubuntu 10.04LTS-i386
    - Ubuntu 10.10-i386
    - Ubuntu 11.04-i386
    - Windows XP
    - Windows Vista
    - Windows7
