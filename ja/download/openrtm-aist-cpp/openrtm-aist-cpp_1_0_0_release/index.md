---
layout: page
title: openrtm-aist-1.0.0-release
---

<!-- Title: OpenRTM-aist-1.0.0-RELEASE -->
<div align="left"><a href="cpp_logo.png"><img src="cpp_logo.png" width="15%;" align="right"></a></div>
<br>
<br>
<br>
#contents



## ソースコード
<table class="table-alt">
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.0/OpenRTM-aist-1.0.0-RELEASE.tar.bz2">OpenRTM-aist-1.0.0-RELEASE.tar.bz2</a><br>MD5:950b5726e87f29d1c3abe6a85ef0d4cb</td>
    <td>2010.01.28</td>
  </tr>
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.0/OpenRTM-aist-1.0.0-RELEASE.tar.gz">OpenRTM-aist-1.0.0-RELEASE.tar.gz</a><br>MD5:dc399aa818fa57f5d24fd752a3a2257b</td>
    <td>2010.01.28</td>
  </tr>
  <tr>
    <td>C++版Windows専用ソース</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.0/OpenRTM-aist-1.0.0-RELEASE-win32.zip">OpenRTM-aist-1.0.0-RELEASE-win32.zip</a><br>MD5:248f98271baaac7fb2fcc885549b7524</td>
    <td>2010.01.28</td>
  </tr>
</table>

<br>

## パッケージ
### Windowsインストーラ

<table class="table-alt">
  <tr>
    <th colspan="3">Visual Studio 2008 用</th>
  </tr>
  <tr>
    <td>Windowsインストーラ</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/cxx/OpenRTM-aist-1.0.0-RELEASE_vc9_100212.msi">OpenRTM-aist-1.0.0-RELEASE_vc9_100212.msi</a><br>MD5:abfc1c2a6a7f6997f7c7ffc2ecaff094</td>
    <td>2010.02.12</td>
  </tr>
  <tr>
    <td>Python Windows用インストーラ</td>
    <td><a href="http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi">python-2.6.4.msi</a></td>
    <td><a href="http://www.python.org/">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML (rtc-templateに必要)</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.09.win32-py2.6.exe">PyYAML-3.09.win32-py2.6.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
  <tr>
    <td>OpenCV Windows用インストーラ</td>
    <td><a href="http://downloads.sourceforge.net/opencvlibrary/OpenCV_1.0.exe?modtime=1161287502&big_mirror=1">OpenCV_1.0.exe</a></td>
    <td><a href="http://sourceforge.net/projects/opencvlibrary/">sourceforge</a></td>
  </tr>
  <tr>
    <td>CMake用設定ファイル(RTCB1.1以降)</td>
    <td><div align="center"><a href="rtm_config.cmake">rtm_config.cmake(右クリックで保存)</a></div><br>%RTM_ROOT%\etcにコピーしてご利用ください。</td>
    <td>2011.05.30</td>
  </tr>
</table>


<br>

<table class="table-alt">
  <tr>
    <th colspan="3">Visual Studio 2005 用</th>
  </tr>
  <tr>
    <td>Windowsインストーラ</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/cxx/OpenRTM-aist-1.0.0-RELEASE_vc8_100212.msi">OpenRTM-aist-1.0.0-RELEASE_vc8_100212.msi</a><br>MD5:fd0bf260fc39b34bb9c82978c22889c9</td>
    <td>2010.02.12</td>
  </tr>
  <tr>
    <td>Python Windows用インストーラ</td>
    <td><a href="http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi">python-2.6.4.msi</a></td>
    <td><a href="http://www.python.org/">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML (rtc-templateに必要)</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.09.win32-py2.6.exe">PyYAML-3.09.win32-py2.6.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
  <tr>
    <td>OpenCV Windows用インストーラ</td>
    <td><a href="http://downloads.sourceforge.net/opencvlibrary/OpenCV_1.0.exe?modtime=1161287502&big_mirror=1">OpenCV_1.0.exe</a></td>
    <td><a href="http://sourceforge.net/projects/opencvlibrary/">sourceforge</a></td>
  </tr>
  <tr>
    <td>CMake用設定ファイル(RTCB1.1以降)</td>
    <td><div align="center"><a href="rtm_config.cmake">rtm_config.cmake(右クリックで保存)</a></div><br>%RTM_ROOT%\etcにコピーしてご利用ください。</td>
    <td>2011.05.30</td>
  </tr>
</table>


- <span style="color:red;">Windowsインストーラには、''OpenRTM-aist (DLL,ヘッダ,サンプル,コマンド), omniORB-4.1.4, RTSystemEditor (RCP版) が含まれていますので、omniORBやツールを別途インストールする必要はありません。</span>;
- <span style="color:red;">※Visual Studio 2005でビルドしたOpenRTM-aistとVisual Studio 2008でビルドしたものは混在できません。お使いの開発環境に合わせて適切なパッケージをダウンロードしてください。</span>;

<br>
### Linuxパッケージ
Vine Linux, Fedora, Ubuntu, Debianの各ディストリビューション用のパッケージを www.openrtm.org 上のリポジトリサーバにて配布しています。
詳細は、以下のドキュメントを参照してください。

- [Vine Linux]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_vine_1_1)
- [Fedora]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_fedora_1_1)
- [Debian/Ubuntu]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_ubuntu_1_1)

また、以下で配布しているインストールスクリプトを利用すれば、必要なパッケージを一括でインストールすることができます。

<table class="table-alt">
  <tr>
    <th>ディストリビューション</th>
    <th>対応バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Vine Linux</td>
    <td>4.0, 4.2, 5.0</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_vine.sh">pkg_install_vine.sh </a></td>
  </tr>
  <tr>
    <td>Fedora</td>
    <td>10, 11, 12 (共にi386/x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_fedora.sh">pkg_install_fedora.sh </a></td>
  </tr>
  <tr>
    <td>Ubuntu</td>
    <td>8.04, 8.10, 9.04, 9.10, 10.04 (共にi386/x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian</td>
    <td>3.1 (i386), 4.0, 5.0 (共にi386, x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_debian.sh">pkg_install_debian.sh </a></td>
  </tr>
</table>

<br>
### MacPorts
MacPorts用Portfileが利用可能です。あらかじめXcodeおよびMacPortsをインストールした上でご利用ください。
- [Portfile (ports.tgz) ]()（リンク切れです）
- [インストールスクリプト (port_install.sh) ]()（リンク切れです）: ports.tgz のダウンロード、OpenRTM-aistのビルド・インストールまで自動で行います。

<br>
## ツール
<table class="table-alt">
  <tr>
    <td>Windows用全部入り</td>
    <td><a href="">eclipse342_rtmtools100release_win32_ja.zip</a>（リンク切れです）<br>MD5:A52450B24F0A1C59402D5340D9FA8D56</td>
    <td>2010.06.01</td>
  </tr>
</table>

<br>
## リリースノート: 1.0.0-RELEASE
RTミドルウエア：OpenRTM-aist のC++言語版最新バージョン 1.0.0 を1月28日にリリースいたしました。今回のリリースでは、2008年4月に公式な国際標準となった OMG RTC Specification version 1.0 へ正式に準拠いたしました。

OpenRTM-aist Official Website からソースコード、Windowsインストーラ、Linux用パッケージ等が EPL (Eclipse Public License) ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

これまでは、実行・開発環境を構築するには、いくつかのパッケージをインストールする必要がありましたが、今回のリリースでは、特にWindows用には、omniORBやツール等全てを含む all-in-one インストーラを提供することにより、どなたでもすぐにサンプルを実行して試用可能となりました。ぜひお試しください。

- [OpenRTM-aist-1.0.0-RELEASE.tar.gz](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.0/OpenRTM-aist-1.0.0-RELEASE.tar.gz) -- 2010.01.28リリース
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
  - CORBA関連のメモリリークの修正 
  - ManagerのCORBAサービス化(試験的) 
    - マスタ、スレーブマネージャ方式 
    - マスタマネージャのINS(Interoperable naming service)対応 
    - コンポーネントのリモート管理機能の導入 
    - 共有オブジェクト(.so,.dll)のオートローディング
  - Windows版 all-in-one インストーラの提供
    - omniORBの同梱
    - RTSystemEditor (RCP版) の同梱
    - Visual C 再配布ライブラリの同梱
  - coil (Common Object Infrastructure Layer) 導入
    - ACE が不要に
    - ライブラリの小型化
    - uITRON 系 OS へも対応可能に
  - 対応(ビルド検証済)OS
    - Debian4.0-i686
    - Debian4.0-x86_64
    - Debian5.0-i686
    - Debian5.0-x86_64
    - Fedora release 10 (Cambridge)-i686
    - Fedora release 10 (Cambridge)-x86_64
    - Fedora release 11 (Leonidas)-i686
    - Fedora release 11 (Leonidas)-x86_64
    - Fedora release 12 (Constantine)-i686
    - Fedora release 12 (Constantine)-x86_64
    - FreeBSD5.5-RELEASE-amd64
    - FreeBSD5.5-RELEASE-i386
    - FreeBSD6.0-RELEASE-amd64
    - FreeBSD6.0-RELEASE-i386
    - FreeBSD6.2-RELEASE-amd64
    - FreeBSD6.2-RELEASE-i386
    - FreeBSD7.0-RELEASE-amd64
    - FreeBSD7.0-RELEASE-i386
    - FreeBSD7.2-RELEASE-amd64
    - FreeBSD7.2-RELEASE-i386
    - Ubuntu 8.04-i686
    - Ubuntu 8.04-x86_64
    - Ubuntu 8.10-i686
    - Ubuntu 8.10-x86_64
    - Ubuntu 9.04-i686
    - Ubuntu 9.04-x86_64
    - Ubuntu 9.10-i686
    - Ubuntu 9.10-x86_64
    - Ubuntu 10.04-i686
    - Ubuntu 10.04-x86_64
    - Ubuntu 10.10-i686
    - Ubuntu 10.10-x86_64
    - Vine Linux 4.0 (Latour)-i686
    - Vine Linux 4.2 (Lynch Bages)-i686
    - Vine Linux 5.0 (Lafite)-i686
    - Windows-XP-VC2005-i386
    - Windows-Vista-VC2008-i386

<br>

<!-- 
## 過去のバージョン
- [[1.0.0-RC1>OpenRTM-aist-1.0.0-RC1]]
- [[0.4.2-RELESE>OpenRTM-aist-0.4.2-RELEASE]]
- [[0.4.2-RC2>OpenRTM-aist-0.4.2-RC2]]
- [[0.4.1-RELEASE>OpenRTM-aist-0.4.1-RELEASE]]
- [[0.4.0-RELEASE>OpenRTM-aist-0.4.0-RELEASE]]
- [[0.4.0-RC2>OpenRTM-aist-0.4.0-RC2]]
-->
