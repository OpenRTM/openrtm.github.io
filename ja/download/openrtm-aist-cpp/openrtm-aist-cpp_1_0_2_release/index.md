---
layout: page
title: openrtm-aist c++ 1.0.2-release
---

<!-- Title: 1.0.2-RELEASE -->
<div align="left"><a href="cpp_logo.png"><img src="cpp_logo.png" width="15%;" align="right"></a></div>

#contents(4)



## ソースコード
<table class="table-alt">
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.2/OpenRTM-aist-1.0.2.tar.bz2">OpenRTM-aist-1.0.2.tar.bz2</a><br>MD5:0acac3810c57c9d0f3eaba67759cdba4</td>
    <td>2012.01.11</td>
  </tr>
  <tr>
    <td>C++版ソースコード</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.2/OpenRTM-aist-1.0.2.tar.gz">OpenRTM-aist-1.0.2.tar.gz</a><br>MD5:31ff5a9876e0aea3666e42210159af34</td>
    <td>2011.01.11</td>
  </tr>
  <tr>
    <td>C++版 Windows 専用ソース</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.2/OpenRTM-aist-1.0.2-win32.zip">OpenRTM-aist-1.0.2-win32.zip</a><br>MD5:fb5bca403dbee7814dc238190afc43b0</td>
    <td>2011.01.11</td>
  </tr>
</table>

<br>
## パッケージ
### Windows インストーラー

<table class="table-alt">
  <tr>
    <th colspan="3">Visual Studio 2008 用</th>
  </tr>
  <tr>
    <td>Windows インストーラー</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/cxx/OpenRTM-aist-1.0.2-1_vc9.msi">OpenRTM-aist-1.0.2-1_vc9.msi</a><br>MD5:1b291a8b466ce20d383a07b61c3d1ccc</td>
    <td>2011.01.11</td>
  </tr>
  <tr>
    <td>Python Windows 用インストーラー</td>
    <td><a href="http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi">python-2.6.4.msi</a></td>
    <td><a href="http://www.python.org/">python.org</a></td>
  </tr>
  <tr>
    <td>PyYAML (rtc-templateに必要)</td>
    <td><a href="http://pyyaml.org/download/pyyaml/PyYAML-3.09.win32-py2.6.exe">PyYAML-3.09.win32-py2.6.exe</a></td>
    <td><a href="http://pyyaml.org/">pyyaml.org</a></td>
  </tr>
  <tr>
    <td>OpenCV Windows 用インストーラー</td>
    <td><a href="http://downloads.sourceforge.net/opencvlibrary/OpenCV_1.0.exe?modtime=1161287502&big_mirror=1">OpenCV_1.0.exe</a></td>
    <td><a href="http://sourceforge.net/projects/opencvlibrary/">sourceforge</a></td>
  </tr>
  <tr>
    <td>CMake 用設定ファイル(RTCB1.1以降)</td>
    <td><div align="center"><a href="rtm_config.cmake">rtm_config.cmake(右クリックで保存)</a></div><br>%RTM_ROOT%\etcにコピーしてご利用ください。</td>
    <td>2011.05.30</td>
  </tr>
</table>


<br>

<!-- |LEFT:200|LEFT|LEFT:100|c -->
<!-- |>|>|CENTER:''Visual Studio 2005 用''| -->
<!-- |Windowsインストーラ|[[OpenRTM-aist-1.0.0-RELEASE_vc8_100212.msi>http://www.openrtm.org/pub/Windows/OpenRTM-aist/cxx/OpenRTM-aist-1.0.0-//RELEASE_vc8_100212.msi]]&br;MD5:fd0bf260fc39b34bb9c82978c22889c9|2010.02.12| -->
<!-- |Python Windows用インストーラ|[[python-2.6.4.msi:http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi]]|[[python.org:http://www.python.org/]]| -->
<!-- |PyYAML (rtc-templateに必要)|[[PyYAML-3.09.win32-py2.6.exe:http://pyyaml.org/download/pyyaml/PyYAML-3.09.win32-py2.6.exe]]|//[[pyyaml.org:http://pyyaml.org/]]| -->
<!-- |OpenCV Windows用インストーラ|[[OpenCV_1.0.exe>http://downloads.sourceforge.net/opencvlibrary/OpenCV_1.0.exe?modtime=1161287502&big_mirror=1]]|//[[sourceforge>http://sourceforge.net/projects/opencvlibrary/]]| -->
<!-- |CMake用設定ファイル(RTCB1.1以降)|&ref(rtm_config.cmake);(右クリックで保存)&br;%RTM_ROOT%\etcにコピーしてご利用ください。|2011.05.30| -->


- <span style="color:red;">Windowsインストーラには、''OpenRTM-aist (DLL、ヘッダ、サンプル,コマンド)、omniORB-4.1.4,、RTSystemEditor (RCP版) が含まれていますので、omniORB やツールを別途インストールする必要はありません。</span>;
- <span style="color:red;">※Visual Studio 2005 でビルドした OpenRTM-aist と Visual Studio 2008 でビルドしたものは混在できません。お使いの開発環境に合わせて適切なパッケージをダウンロードしてください。</span>;

#### Windows Vista/7でお使いの方へ

1.0.0系の RTSystemEditor は新しいWindowsでは動作しないケースがあります。以下の作業を行うことでVistaやWindows7でも動作させることができます。

- 32bit版 JRE6 のインストール
  - RTSystemEditor は JRE7 には対応していません。[こちら](http://java.com/ja/download/manual_v6.jsp)から[JRE6(32bit版)](http://java.com/ja/download/manual_v6.jsp)をダウンロードしてインストールしてください。
- 起動オプションの変更
  - スタートメニューに登録されている RTSystemEditor の起動オプションを変更してください。
  - [スタート] > [OpenRTM-aist] > [tools] > [RTSystemEditor] を右クリック
  - [ショートカット] > [リンク先] を以下のように変更

```
 (32bit版 Windows をお使いの場合)
 "C:\Program Files\OpenRTP\RTSystemEditor\RTSystemEditorRCP.exe" -vm "C:\Program Files\Java\jre6\bin\javaw.exe" -data "%USERPROFILE%\workspace"
 (64bit版 Windows をお使いの場合)
 "C:\Program Files (x86)\OpenRTP\RTSystemEditor\RTSystemEditorRCP.exe" -vm "C:\Program Files (x86)\Java\jre6\bin\javaw.exe" -data "%USERPROFILE%\workspace"
```


<br>
### Linux パッケージ
Vine Linux、Fedora、Ubuntu、Debian の各ディストリビューション用のパッケージを www.openrtm.org 上のリポジトリサーバーにて配布しています。
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
<!-- | Vine Linux | 4.0, 4.2, 5.0 |[[pkg_install_vine.sh >http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_vine.sh]]| -->
<!-- | Fedora | 10, 11, 12 (共にi386/x86_64) |[[pkg_install_fedora.sh >http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_fedora.sh]]| -->
  <tr>
    <td>Ubuntu</td>
    <td>10.04, 10.10, 11.04, 11.10 (共にi386/x86_64)</td>
    <td><a href="http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
</table>
<!-- | Debian |3.1 (i386), 4.0, 5.0 (共にi386, x86_64)|[[pkg_install_debian.sh >http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_debian.sh]]| -->

<!-- &br; -->
<!-- ***MacPorts -->
<!-- MacPorts 用 Portfile が利用可能です。あらかじめ Xcode および MacPorts をインストールした上でご利用ください。 -->
<!-- - [[Portfile (ports.tgz) :http://www.openrtm.org/pub/MacOSX/macports/ports.tgz]] -->
<!-- - [[インストールスクリプト (port_install.sh) :http://www.openrtm.org/pub/MacOSX/macports/port_install.sh]]: ports.tgz のダウンロード、OpenRTM-aist のビルド・インストールまで自動で行います。 -->

<br>
## ツール
<table class="table-alt">
  <tr>
    <td>Windows 用全部入り</td>
    <td><a href="">eclipse342_rtmtools100release_win32_ja.zip</a>（リンク切れです）<br>MD5:A52450B24F0A1C59402D5340D9FA8D56</td>
    <td>2010.06.01</td>
  </tr>
</table>

<br>
## リリースノート: 1.0.2-RELEASE
RTミドルウエア：OpenRTM-aist の C++言語版バージョン 1.0.0 のバグフィックス版を1月11日にリリースいたしました。

OpenRTM-aist Official Website からソースコード、Windows インストーラー、Linux 用パッケージ等が EPL (Eclipse Public License) ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

これまでは、実行・開発環境を構築するには、いくつかのパッケージをインストールする必要がありましたが、今回のリリースでは、特に Windows 用には、omniORB やツール等全てを含む all-in-one インストーラーを提供することにより、どなたでもすぐにサンプルを実行して試用可能となりました。
ぜひお試しください。

- [OpenRTM-aist-1.0.2.tar.gz](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.2/OpenRTM-aist-1.0.2.tar.gz) -- 2011.01.11リリース
  - RingBuffer のデッドロックの修正
  - cleanupComponent() 時にコンポーネントが強制終了するバグの修正
  - 対応(ビルド検証済)OS
    - Ubuntu 10.04-i686
    - Ubuntu 10.04-x86_64
    - Ubuntu 10.10-i686
    - Ubuntu 10.10-x86_64
    - Ubuntu 11.04-i686
    - Ubuntu 11.04-x86_64
    - Ubuntu 11.10-i686
    - Ubuntu 11.10-x86_64
    - Windows-Vista-VC2008-i386

<br>

<!-- 
## 過去のバージョン
- [[1.0.0-RELEASE>OpenRTM-aist-1.0.0-RELEASE]]
- [[1.0.0-RC1>OpenRTM-aist-1.0.0-RC1]]
- [[0.4.2-RELESE>OpenRTM-aist-0.4.2-RELEASE]]
- [[0.4.2-RC2>OpenRTM-aist-0.4.2-RC2]]
- [[0.4.1-RELEASE>OpenRTM-aist-0.4.1-RELEASE]]
- [[0.4.0-RELEASE>OpenRTM-aist-0.4.0-RELEASE]]
- [[0.4.0-RC2>OpenRTM-aist-0.4.0-RC2]] -->
