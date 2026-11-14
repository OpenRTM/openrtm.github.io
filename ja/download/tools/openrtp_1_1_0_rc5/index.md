---
layout: page
title: openrtp 1.1.0-rc5
---

<!-- Title: OpenRTP 1.1.0-RC5 -->
<div align="left"><a href="eclipse_logo.png"><img src="eclipse_logo.png" width="100;" align="left"></a></div>

1.1.0からRTCBUilder および RTSystemEditorを含むツールの名称を OpenRTP (Open RT Platform) としました。  RC5はEclipse-3.8ベースです。

#clear
#contents
#clear

## 更新サイト

このバージョンからEclipseの更新サイトを利用したインストールに対応しています。
以下のURLを更新サイト一覧に追加することで、お使いのEclipseのOpenRTPをインストールすることができます。

- OpenRTP 更新サイト: [http://openrtm.org/pub/openrtp/stable/updates/]()（リンク切れです）

手順については[更新方法]({{ site.baseurl }}/ja/doc/toolmanuals/rtcbuilder-1_1_0/update_rtcb_1_1_0)のページをご覧下さい。

&aname(package);
## 全部入りパッケージ

### Eclipse-3.8ベース

<table class="table-alt">
  <tr>
    <td colspan="3" style="text-align: center;">Eclipse-3.8</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 <br>**Windows用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-ja-win32.zip</a>（リンク切れです） <br> MD5: 45a20287855b8ae51294f48b69fd7a9d</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 (英語版) <br>**Windows用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-win32.zip</a>（リンク切れです） <br> MD5: cf108e4fdf9644cb829498dae4b5e9de</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 <br>**Windows(64bit)用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-ja-win32-x86_64.zip</a>（リンク切れです） <br> MD5: 9125054bba8e5bca3547423a2cf5fead</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 (英語版) <br>**Windows(64bit)用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-win32-x86_64.zip</a>（リンク切れです） <br> MD5: 9c6da560c9736d117b3695d6e0cfe057</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 <br>**Linux用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-ja-linux-gtk.tar.gz</a>（リンク切れです） <br> MD5: 20c71861fcd585aee65d676adc3efbc7</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 (英語版) <br>**Linux用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-linux-gtk.tar.gz</a>（リンク切れです） <br> MD5: 9250b5b08b21ee06e03db74474b8655e</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 <br>**Linux(64bit)用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-ja-linux-gtk-x86_64.tar.gz</a>（リンク切れです） <br> MD5: eaa4b9ef00af81e05b6d02e93a8e3e85</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 (英語版) <br>**Linux(64bit)用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-linux-gtk-x86_64.tar.gz</a>（リンク切れです） <br> MD5: ead8c9ffb7bdc835b883c326f5df7e9f</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 <br>**Mac OS X用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-ja-macosx-cocoa.tar.gz</a>（リンク切れです） <br> MD5: 3d7415c4d22e49db94ad1c36479b0072</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 (英語版) <br>**Mac OS X用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-macosx-cocoa.tar.gz</a>（リンク切れです） <br> MD5: e2f0b9c39c7fe3cbce1bc0315decbfe2</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 <br>**Mac OS X(64bit)用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-ja-macosx-cocoa-x86_64.tar.gz</a>（リンク切れです） <br> MD5: b3b3286d81eae267f1e7da5d7aa4a920</td>
    <td>2015.03.17</td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1 (英語版) <br>**Mac OS X(64bit)用全部入り**</td>
    <td><a href="">eclipse381-openrtp110rc5v20151111-macosx-cocoa-x86_64.tar.gz</a>（リンク切れです） <br> MD5: d0e6115a7f6d50e1457d8850f2e8c830</td>
    <td>2015.03.17</td>
  </tr>
</table>

#### Windowsでのインストール

OpenRTM-aist (C++版)および JDK1.7をインストール後、Windows用パッケージを任意の場所に展開してください。
eclipseというディレクトリが展開されますので、その中のeclipse.exeをクリックするなどして起動してください。

#### Linuxでのインストール

OpenRTM-aist (C++版)および JDK1.7 またはOpenJDKをインストール後、Linux用パッケージを任意の場所に展開してください。
eclipseというディレクトリが展開されますので、そのなかのopenrtpというコマンドから起動します。パスの通っている場所にopenrtpへのシンボリックリンクをを張るとよいでしょう。<br>
各ディストリビューションについてJDK 7のインストール方法を [JDKインストールのためのヒント ]({{ site.baseurl }}/ja/doc/installation/install_1_1/java_1_1/tips_jdk) にまとめましたので参考にしてください。

```
 $ cd /usr/share/openrtm-1.1
 $ sudo wget http://openrtm.org/pub/openrtp/packages/1.1.0.rc5v20150317/eclipse381-openrtp110rc5v20150317-ja-linux-gtk.tar.gz
 $ sudo tar xvzf eclipse381-openrtp110rc5v20150317-ja-linux-gtk.tar.gz
 $ cd /usr/bin
 $ sudo ln -s /usr/share/openrtm-1.1/eclipse/openrtp .
 $ cd 
 $ openrtp
```

RTCBuilderでは、OpenRTM-aist (C++版) に付属のIDLを参照しています。
Linux版ではこれらIDLの場所を得るために、環境変数を設定するか、openrtpというコマンドから起動する必要があります。


#### Mac OS Xでのインストール

OpenRTM-aist (C++版)および JDK1.7 またはOpenJDKをインストール後、Mac OS X用パッケージを任意の場所に展開してください。
eclipseというディレクトリが展開されますので、Linux版と同様に、そのなかのEclipse.app/Contents/MacOSX/openrtpというコマンドから起動します。パスの通っている場所にopenrtpへのシンボリックリンクをを張るとよいでしょう。

```
 $ cd /usr/lib/openrtm-1.1
 $ sudo wget http://openrtm.org/pub/openrtp/packages/1.1.0.rc5v20150317/eclipse381-openrtp110rc5v20150317-ja-macosx-cocoa.tar.gz
 $ sudo tar xvzf eclipse381-openrtp110rc5v20150317-ja-macosx-cocoa.tar.gz
 $ cd /usr/bin
 $ sudo ln -s /usr/lib/openrtm-1.1/eclipse/Eclipse.app/Contents/MacOSX/openrtp .
 $ cd 
 $ openrtp
```

RTCBuilderでは、OpenRTM-aist (C++版) に付属のIDLを参照しています。
Linux版やMac OS X版ではこれらIDLの場所を得るために、環境変数を設定するか、openrtpというコマンドから起動する必要があります。


<br>
&aname(binary);
## jarファイル

<table class="table-alt">
  <tr>
    <th>jar ファイル(RTSE+RTCB)</th>
    <th><a href="http://openrtm.org/pub/openrtp/openrtp/1.1.0.rc5v20150317/openrtp-1.1.0.rc5v20150317.zip">openrtp-1.1.0.rc5v20150317.zip</a><br>MD5: 38019521f6e8574c03e1cab6e8f954cd</th>
    <th>2015.03.17</th>
  </tr>
</table>

<br>
- アーカイブに含まれている jar ファイルを eclipse の plugins ディレクトリにコピーします。
- 更新後は eclipse の起動時に -clean オプションを付けることを推奨します。
- Eclipse SDKパッケージをダウンロードして、独自にこれ等のプラグインを追加する際は、RTSE、RTCBが依存している
  - EMF ランタイム
  - EMF Xcore ランタイム
  - GEF
  - XSD
各プラグインを追加でインストールする必要があります。
- また、Eclipse Platform SDK と Eclipse Plug-in Development Environment がインストールされていることを確認してください。インストールされていない場合、パースペクティブに RTSE と RTCB が現れません。

<br>

<!-- **RTSytemEditor/RTCBuilderデイリービルド -->

<!-- RTSystemEditorおよびRTCBuilderは、日々改良が行われており、入れ替えも比較的簡単ですので、デイリービルドを提供することにいたしました。  -->

<!-- -リポジトリの最新ソースからビルドされたRTSsytemEditor/RTCBuilderがダウンロード可能です。 -->
<!-- -ただし、開発版をビルドしただけのものですので、動かない場合もあります。導入は自己責任でお願いいたします。  -->
<!-- -アーカイブに含まれている jar ファイルを eclipse の plugins ディレクトリにコピーするだけで更新可能です。  -->
<!-- -更新後は eclipse の起動時に -clean オプションを付けることを推奨します。 -->
<!-- -ダウンロードはこちらから：http://www.openrtm.org/pub/OpenRTM-aist/dailybuild/tools/1.1.0/ -->
<!-- --Eclipse SDKパッケージをダウンロードして、独自にこれ等のプラグインを追加する際は、RTSE、RTCBが依存している EMF SDOランタイム, GEF, XSD ランタイムプラグインを追加でインストールする必要があります。 -->

<br>

## Eclipse/JDK/JRE等 

<table class="table-alt">
  <tr>
    <td>JDK</td>
    <td><a href="http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html">http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html</a></td>
  </tr>
  <tr>
    <td>JRE</td>
    <td><a href ="http://www.oracle.com/technetwork/jp/java/javase/downloads/jre7-downloads-1880261.html">http://www.oracle.com/technetwork/jp/java/javase/downloads/jre7-downloads-1880261.html</a></td>
  </tr>
  <tr>
    <td>Eclipse 3.8.1</td>
    <td><a href="http://archive.eclipse.org/eclipse/downloads/drops/R-3.8.1-201209141540/">http://archive.eclipse.org/eclipse/downloads/drops/R-3.8.1-201209141540/</a></td>
  </tr>
</table>

## リリースノート：1.1.0-RC5
- C++コンポーネントをLinux+OpenRTP(64bit) で作成時、cmake可能に
- Pythonコンポーネント作成時、Description.txt, License.txtを含めるように変更
- CMake3で追加されたcmake-policiesに対応
- ヘッダーファイル順序の見直し
- Python版コンポーネントのonFinalize引数の修正
- 雑多なバグフィックス

## 過去のバージョン
- [OpenRTP-1.1.0-RC4]()（リンク切れです）
- [OpenRTP-1.1.0-RC3]()（リンク切れです）
- [RTSystemEditor・RTCBuilder-1.0.0-RELEASE]()（リンク切れです）
- [RTSystemEditor・RTCBuilder-1.0.0-RC1]()（リンク切れです）
- [RTSystemEditor・RTCBuilder-0.4.2-RELEASE]()（リンク切れです）
