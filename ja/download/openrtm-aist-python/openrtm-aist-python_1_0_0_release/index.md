---
layout: page
title: openrtm-aist-python-1.0.0-release
---
<!-- Title: OpenRTM-aist-Python-1.0.0-RELEASE -->
<div align="left"><a href="python-logo.png"><img src="python-logo.png" width="15%;" align="left"></a></div>
#contents
#clear
<br>
<br>
<br>

## 注意事項

バージョン0.4系をインストール済みの環境に1.0系をインストールする場合は、一度0.4系を削除してから1.0系のインストールを行ってください。
0.4系をアンインストールした後に0.4系の残骸が残っている場合がございますので、残骸が残っている場合は手動でOpenRTMフォルダの削除を行って下さい。

- 削除するフォルダ
  - Windows環境の場合:
```
 C:\Python[24,25,26]\Lib\site-packages\OpenRTM
```
  - Linux環境の場合:
```
  /usr/lib/python[2.4,2.5,2.6]/site-packages/OpenRTM
```

&aname(source);
## ソースコード
<table class="table-alt">
  <tr>
    <td>Python版ソースコード</td>
    <td><a href="">OpenRTM-aist-Python-1.0.0-RELEASE.tar.gz</a>（リンク切れです） <br> MD5:dd11ef6a2e6277fa095e0fbd3210a2a5</td>
    <td>10/05/07</td>
  </tr>
  <tr>
    <td>Python版ソースコード(Win32)</td>
    <td><a href="">OpenRTM-aist-Python-1.0.0-RELEASE.zip</a>（リンク切れです） <br> MD5:371b427288cb0f69ab3dcf71d8eda169</td>
    <td>10/05/07</td>
  </tr>
</table>

<span style="color:red;">※ OpenRTM-aist-Python-1.0.0には以下のバグがありますので、1.0.1をインストールされることをお勧めします。</span>;

- OpenRTM-aist-Python-1.0.0-RELEASEバグ情報
  - InPortCorbaCdrConsumer.put(),OutPortCorbaCdrConsumer.get()での_narrow処理の問題(ML 01304)
  - examples/*/run.py内のrtm-naming.pyのパス修正
  - rtcd_pythonでのコマンドライン引数のパーシングの問題(ML 01527)
  - example/ExtTriggerでExtTrigExecutionContextが正常に動作しない問題(ML 01587)

<table class="table-alt">
  <tr>
    <td>Python版ソースコード</td>
    <td><a href="">OpenRTM-aist-Python-1.0.1.tar.gz</a>（リンク切れです） <br> MD5:00cde340c2903f455b62f1e64d5c968d</td>
    <td>11/02/23</td>
  </tr>
  <tr>
    <td>Python版ソースコード(Win32)</td>
    <td><a href="">OpenRTM-aist-Python-1.0.1.zip</a>（リンク切れです） <br> MD5:8ed1fc66b6b49f605103fc61d1e9b750</td>
    <td>11/02/23</td>
  </tr>
</table>


<br>
## パッケージ
&aname(winpkg);
### Windowsインストーラ (Python 2.4,2.5,2.6 共通)

OpenRTM-aist-Python-1.0.0.msiを使用してOpenRTM-aist-Pythonをインストールする場合、Pythonのバージョン2.4、2.5、2.6のいずれかが必要です。
OpenRTM-aist-Python-1.0.0.msiでは、インストールされているPythonのバージョンを検出し、それぞれにOpenRTM-aist-Python-1.0.0とomniORBpyをインストールします。別途omniORBpyをインストールする必要はありません。

<span style="color:red;">※ OpenRTM-aist-Python-1.0.0にはバグがありますので、1.0.1をインストールされることをお勧めします。</span>;

<table class="table-alt">
  <tr>
    <td>Windows用インストーラ</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python-1.0.0.msi">OpenRTM-aist-Python-1.0.0.msi</a> <br> MD5:4afe4de69c9b56086fc97e9697334a36</td>
    <td>10/05/07</td>
  </tr>
  <tr>
    <td>Windows用インストーラ</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python-1.0.1.msi">OpenRTM-aist-Python-1.0.1.msi</a> <br> MD5:ad9653ab2a07a4247b7b4ad0cf069002</td>
    <td>11/02/23</td>
  </tr>
  <tr>
    <td>Python-2.4.4</td>
    <td><a href="http://www.python.org/ftp/python/2.4.4/python-2.4.4.msi">python-2.4.4.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-2.5.1</td>
    <td><a href="http://www.python.org/ftp/python/2.5.1/python-2.5.1.msi">python-2.5.1.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-2.6.2</td>
    <td><a href="http://www.python.org/ftp/python/2.6.2/python-2.6.2.msi">python-2.6.2.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
</table>

<br>
&aname(linuxpkg);
### Linuxパッケージ
Vine Linux, Fedora, Ubuntu, Debianの各ディストリビューション用のパッケージを www.openrtm.org 上のリポジトリサーバにて配布しています。
詳細は、以下のドキュメントを参照してください。

- [Vine Linuxへのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_vine_python_1_1)
- [Fedoraへのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_fedora_python_1_1)
- [Ubuntu/Debianへのインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/install_ubuntu_python_1_1)


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
## リリースノート: 1.0.0-RELEASE

RTミドルウエア：OpenRTM-aist のPython言語版最新バージョン 1.0.0 を5月7日にリリースいたしました。今回のリリースでは、2008年4月に公式な国際標準となった OMG RTC Specification version 1.0 へ正式に準拠いたしました。

OpenRTM-aist Official Website からソースコード、Windowsインストーラ、Linux用パッケージ等が EPL (Eclipse Public License) ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

これまでは、実行・開発環境を構築するには、いくつかのパッケージをインストールする必要がありましたが、今回のリリースでは、特にWindows用には、omniORBpyやツール等を含むインストーラを提供することにより、どなたでもすぐにサンプルを実行して試用可能となりました。ぜひお試しください。

- [OpenRTM-aist-Python-1.0.0-RELEASE.tar.gz]()（リンク切れです） -- 2010.05.07リリース
  - OMG RTC Specification v1.0 準拠
  - 新データポート導入 (corba_cdrインターフェース型)
    - push型・pull型データフローの導入
    - サブスクリプション型の導入
    - 送信ポリシの導入
    - バッファリングポリシとタイムアウトの導入
  - 雑多なバグフィックス
  - コンフィギュレーション機能の充実
    - rtc.conf新オプションの導入 
    - より多くの項目を設定可能に
  - ManagerのCORBAサービス化(試験的) 
    - マスタ、スレーブマネージャ方式 
    - マスタマネージャのINS(Interoperable naming service)対応 
    - コンポーネントのリモート管理機能の導入 
  - Windows版 インストーラの提供
    - omniORBpyの同梱
    - RTSystemEditor (RCP版) の同梱

  - 動作条件
  - サポートするPythonバージョン
    - 2.4
    - 2.5
    - 2.6
  - 動作確認済みOS
    - Debian4.0-i386
    - Debian5.0-i386
    - Fedora release 11 (Leonidas)-i386
    - Fedora release 12 (Constantine)-i386
    - Ubuntu 8.04-i386
    - Ubuntu 8.10-i386
    - Ubuntu 9.04-i386
    - Ubuntu 9.10-i386
    - Ubuntu 10.04LTS-i386
    - Vine Linux 4.0 (Latour)-i386
    - Vine Linux 4.2 (Lynch Bages)-i386
    - Vine Linux 5.0 (Lafite)-i386
    - Windows XP
    - Windows Vista
    - Windows7

