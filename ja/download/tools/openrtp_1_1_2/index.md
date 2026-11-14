---
layout: page
title: openrtp 1.1.2
---

init
<!-- Title: OPenRTP 1.1.2 -->
<div align="right"><a href="eclipse_logo.png"><img src="eclipse_logo.png" width="15%;" align="right"></a></div>

<!-- 1.1.0 からRTCBUilder および RTSystemEditor を含むツールの名称を OpenRTP (Open RT Platform) としました。  RC5 は Eclipse-3.8 ベースです。 -->

<!-- #clear -->
#contents(5)
<!-- #clear -->

<!-- -&color(red){まだリリースしておりません。準備中です。もうしばらくお待ち下さい。}; -->

&aname(package);
## パッケージ

1.1.2版は Eclipse-4.4.2 ベースです。

### Windows インストーラー

#### 32bit 用
<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist C++、Python、Java版,<br> および OpenRTP、RTShell (4.1.0) 含む)</td>
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
- <span style="color:red;">※ 古い RTShell は事前に削除しておいてください。</span>;

#### 64bit 用
<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist C++、Python、Java版<br> および OpenRTP、RTShell (4.1.0)含む)</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/1.1/OpenRTM-aist-1.1.2-RELEASE_x86_64.msi">OpenRTM-aist-1.1.2-RELEASE_x86_64.msi</a> <br>MD5:ee8db7c1682cb21dce963207e0484fb3</td>
    <td>2016/05/27</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.amd64.msi">python-2.7.10.amd64.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python 2.7.10 推奨。2.7.11 は PYTHONPATH 等環境変数の設定が必要な場合があります。</span>;
- <span style="color:red;">※ 古い RTShell は事前に削除しておいてください。</span>;

インストールについては、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/quick_start_1_1_2) のページで手順を紹介しています。<br>

&aname(dl_allinone_linux);
### Linux パッケージ

#### 32bit 用

<table class="table-alt">
  <tr>
    <td>日本語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-ja-linux-gtk.tar.gz">eclipse442-openrtp112v20160526-ja-linux-gtk.tar.gz</a> <br> MD5: f941e7316da51d6727274793dd1a9b93</td>
    <td>2016.05.26</td>
  </tr>
  <tr>
    <td>英語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk.tar.gz">eclipse442-openrtp112v20160526-linux-gtk.tar.gz</a> <br> MD5:38896917b9c827a0f1eec99da869047e</td>
    <td>2016.05.26</td>
  </tr>
</table>

#### 64bit 用

<table class="table-alt">
  <tr>
    <td>日本語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-ja-linux-gtk-x86_64.tar.gz">eclipse442-openrtp112v20160526-ja-linux-gtk-x86_64.tar.gz</a> <br> MD5:b17f13c49626988cbe8b811b0de79d48</td>
    <td>2016.05.26</td>
  </tr>
  <tr>
    <td>英語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz">eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz</a> <br> MD5:a3a15088978e5f6afcca8d41e9c6ba6e</td>
    <td>2016.05.26</td>
  </tr>
</table>

### Mac パッケージ

#### 32bit 用
<table class="table-alt">
  <tr>
    <td>日本語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-ja-macosx-cocoa.tar.gz">eclipse442-openrtp112v20160526-ja-macosx-cocoa.tar.gz</a> <br> MD5:cff0e09517000ecb09c6d5591a1c7056</td>
    <td>2016.05.26</td>
  </tr>
  <tr>
    <td>英語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-macosx-cocoa.tar.gz">eclipse442-openrtp112v20160526-macosx-cocoa.tar.gz</a> <br> MD5:0a7a7d64ce2fade2fd93b163cab915b7</td>
    <td>2016.05.26</td>
  </tr>
</table>

#### 64bit 用
<table class="table-alt">
  <tr>
    <td>日本語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-ja-macosx-cocoa-x86_64.tar.gz">eclipse442-openrtp112v20160526-ja-macosx-cocoa-x86_64.tar.gz</a> <br> MD5:20d8ae41d0421f3e26ef3bae70eff100</td>
    <td>2016.05.26</td>
  </tr>
  <tr>
    <td>英語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-macosx-cocoa-x86_64.tar.gz">eclipse442-openrtp112v20160526-macosx-cocoa-x86_64.tar.gz</a> <br> MD5:f1a16a3baf2fcffed73d41bb139f682e</td>
    <td>2016.05.26</td>
  </tr>
</table>


### OpenRTP の起動方法
&aname(dl_allinone_win);

#### Windows でのダウンロードと起動

OpenRTM-aist (C++版)および JDK1.7 をインストール後、下記の Windows用パッケージを任意の場所に保存し、展開してください。
eclipse というディレクトリーが展開されますので、その中の eclipse.exe をダブルクリックして起動してください。

##### 32bit 用
<table class="table-alt">
  <tr>
    <td>日本語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-ja-win32.zip">eclipse442-openrtp112v20160526-ja-win32.zip</a> <br> MD5:6f9e266a73d13e56dda140828b9da328</td>
    <td>2016.05.26</td>
  </tr>
  <tr>
    <td>英語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-win32.zip">eclipse442-openrtp112v20160526-win32.zip</a> <br> MD5:b727b26c386e8292ef8f28cc280bb6a5</td>
    <td>2016.05.26</td>
  </tr>
</table>

##### 64bit 用
<table class="table-alt">
  <tr>
    <td>日本語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-ja-win32-x86_64.zip">eclipse442-openrtp112v20160526-ja-win32-x86_64.zip</a> <br> MD5:bbd06decec6953fe1464290557ed9ba4</td>
    <td>2016.05.26</td>
  </tr>
  <tr>
    <td>英語版</td>
    <td><a href="http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-win32-x86_64.zip">eclipse442-openrtp112v20160526-win32-x86_64.zip</a> <br> MD5:d4674b15a1f4b514f8319bb69c3bebfe</td>
    <td>2016.05.26</td>
  </tr>
</table>

#### Linux でのダウンロードと起動

OpenRTM-aist (C++版)および JDK1.7 または OpenJDK をインストール後、Linux 用パッケージを任意の場所に保存し、展開してください。
eclipse というディレクトリーが展開されますので、そのなかの openrtp というコマンドから起動します。パスの通っている場所に openrtp へのシンボリックリンクをを張るとよいでしょう。<br>

RTCBuilderでは、OpenRTM-aist (C++版) に付属の IDL を参照しています。
Linux版ではこれら IDL の場所を得るために、<span style="color:red;">環境変数を設定するか、openrtp というコマンドから起動する必要があります。</span>;<br>

各ディストリビューションについて JDK 7 のインストール方法を [JDK インストールのためのヒント ]({{ site.baseurl }}/ja/doc/installation/install_1_1/java_1_1/tips_jdk) にまとめましたので参考にしてください。<br>

```
 $ cd /usr/share/openrtm-1.1.2
 $ sudo wget http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp
 112v20160526-linux-gtk.tar.gz
 $ sudo tar xvzf eclipse442-openrtp112v20160526-linux-gtk.tar.gz
 $ cd /usr/bin
 $ sudo ln -s /usr/share/openrtm-1.1.2/eclipse/openrtp .
 $ cd 
 $ openrtp
```

#### Mac OS X でのダウンロードと起動

OpenRTM-aist (C++版) および JDK1.7 または OpenJDK をインストール後、Mac OS X 用パッケージを任意の場所に保存し、展開してください。
eclipse というディレクトリーが展開されますので、Linux 版と同様に、そのなかの Eclipse.app/Contents/MacOSX/openrtp というコマンドから起動します。パスの通っている場所に openrtp へのシンボリックリンクをを張るとよいでしょう。<br>

RTCBuilderでは、OpenRTM-aist (C++版) に付属の IDL を参照しています。
Linux 版や Mac OS X 版ではこれら IDL の場所を得るために、<span style="color:red;">環境変数を設定するか、openrtp というコマンドから起動する必要があります。</span>;<br>

```
 $ cd /usr/lib/openrtm-1.1.2
 $ sudo wget http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp
 112v20160526-ja-macosx-cocoa.tar.gz
 $ sudo tar xvzf eclipse442-openrtp112v20160526-ja-macosx-cocoa.tar.gz
 $ cd /usr/bin
 $ sudo ln -s /usr/lib/openrtm-1.1.2/eclipse/Eclipse.app/Contents/MacOSX/openrtp .
 $ cd 
 $ openrtp
```

## 更新サイト
<!-- このバージョンから Eclipse の更新サイトを利用したインストールに対応しています。 -->
以下の URL を更新サイト一覧に追加することで、お使いの Eclipse の OpenRTP をインストールすることができます。

- OpenRTP 更新サイト: http://openrtm.org/pub/openrtp/stable/updates/

手順については[更新方法]({{ site.baseurl }}/ja/doc/toolmanuals/rtcbuilder-1_1_0/update_rtcb_1_1_0)のページをご覧下さい。

<br>
&aname(binary);
## jar ファイル

<table class="table-alt">
  <tr>
    <th>jar ファイル(RTSE+RTCB)</th>
    <th><a href="http://openrtm.org/pub/openrtp/openrtp/1.1.2v20160526/openrtp-1.1.2v20160526.zip">openrtp-1.1.2v20160526.zip</a><br>MD5: 56686cc687edb13e98f0c25567213ad6</th>
    <th>2016.05.26</th>
  </tr>
</table>

<br>
- アーカイブに含まれている jar ファイルを eclipse の plugins ディレクトリーにコピーします。
- 更新後は eclipse の起動時に -clean オプションを付けることを推奨します。
- Eclipse SDK パッケージをダウンロードして、独自にこれ等のプラグインを追加する際は、RTSE、RTCBが依存している
  - EMF ランタイム
  - EMF Xcore ランタイム
  - GEF
  - XSD
各プラグインを追加でインストールする必要があります。
- また、Eclipse Platform SDK と Eclipse Plug-in Development Environment がインストールされていることを確認してください。インストールされていない場合、パースペクティブに RTSE と RTCB が現れません。

<br>

<!-- **RTSytemEditor/RTCBuilderデイリービルド -->

<!-- RTSystemEditor および RTCBuilder は、日々改良が行われており、入れ替えも比較的簡単ですので、デイリービルドを提供することにいたしました。  -->

<!-- -リポジトリの最新ソースからビルドされた RTSsytemEditor/RTCBuilder がダウンロード可能です。 -->
<!-- -ただし、開発版をビルドしただけのものですので、動かない場合もあります。導入は自己責任でお願いいたします。  -->
<!-- -アーカイブに含まれている jar ファイルを eclipse の plugins ディレクトリーにコピーするだけで更新可能です。  -->
<!-- -更新後は eclipse の起動時に -clean オプションを付けることを推奨します。 -->
<!-- -ダウンロードはこちらから：http://www.openrtm.org/pub/OpenRTM-aist/dailybuild/tools/1.1.0/ -->
<!-- --Eclipse SDK パッケージをダウンロードして、独自にこれ等のプラグインを追加する際は、RTSE、RTCBが依存している EMF SDOランタイム、GEF、XSD ランタイムプラグインを追加でインストールする必要があります。 -->

<br>

## Eclipse/JDK/JRE 等 

<table class="table-alt">
  <tr>
    <td>JDK</td>
    <td><a href="http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html">http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html</a></td>
  </tr>
  <tr>
    <td>JRE</td>
    <td><a href="http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html">http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html</a></td>
  </tr>
  <tr>
    <td>Eclipse 4.4.2</td>
    <td><a href="https://eclipse.org/downloads/packages/release/luna/sr2">https://eclipse.org/downloads/packages/release/luna/sr2</a></td>
  </tr>
</table>

## リリースノート：1.1.2
### RTSystemEditor
- ポート名称の表示位置をポートとの関係が分かりやすい位置に修正
- ポート接続を行うためにドラッグを開始時に，選択した対象ポートと接続可能なポートの枠線を太く表示するように修正
- ネームサービスビューにおい，ツリー表示されるオブジェクトリファレンスやネーミングコンテキストを右クリックする事で，IORやIORに含まれる情報（IPアドレス，ポート番号，ObjectKey等）を表示するように修正
- コンフィギュレーションセットビューに詳細モードを追加し，アンダーバーから始まるコンフィギュレーションセット，コンフィギュレーションパラメーターの表示/非表示を切り替えられるように修正
- システムリストア時に，マネージャーの機能を利用してコンポーネントの起動まで行えるように修正
- ログの出力先をユーザーが指定できるように修正
<!-- - 雑多なバグフィックス -->

### RTCBuilder
- 「アクティビティ」タブのコールバック名をダブルクリックすることで，ON/OFF を切り替えられるように修正
- サービスポートに設定した IDL ファイル内で，#include の前にスペースがある場合でも内容をパースするように修正
- 「基本」タブ内の ExecutionContext テキストボックスに文字入力を行った際の処理を修正
- コンフィギュレーションパラメーターの型情報をアンダーバー付き隠しパラメーターとして生成するように修正
- Java 版の生成コードに，データポート変数を初期化する処理を追加
- C++ 版生成コードの using ディレクティブの位置を変更
- ログの出力先をユーザーが指定できるように修正

## 過去のバージョン
- [OpenRTP-1.1.0-RC5]()（リンク切れです）
<!-- - [[OpenRTP-1.1.0-RC4:/ja/download/openrtp/openrtp-110-rc4-ja]] -->
<!-- - [[OpenRTP-1.1.0-RC3:/ja/download/openrtp/openrtp-110-rc3-ja]] -->
<!-- - [[RTSystemEditor・RTCBuilder-1.0.0-RELEASE>/node/941]] -->
<!-- - [[RTSystemEditor・RTCBuilder-1.0.0-RC1>/node/75]] -->
<!-- - [[RTSystemEditor・RTCBuilder-0.4.2-RELEASE>/node/76]] -->
