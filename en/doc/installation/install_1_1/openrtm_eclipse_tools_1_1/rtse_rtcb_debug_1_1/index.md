---
layout: page
title: rtsystemeditor、rtcbuilder のデバッグ
---
<br>
<a>No English version available.
</a>

<!-- #contents -->
<!-- RTSystemEditor、RTCBuilder のデバッグ -->

このページではRTSystemEditor、RTCBuilderのデバッグの手順を説明します。

## 必要なソフトウェアの入手

### eclipse

RTSystemEditor、RTCBuilderはeclipseのプラグインとして動作します。
以下のサイトからから、eclipseをダウンロードしてください。
その際にパッケージはUltimateのFull Edisionを選択してください。
Standard Editionだとプラグイン開発環境を手動でインストールする必要があります。


- [http://mergedoc.osdn.jp/](http://mergedoc.osdn.jp/)


### JDK

JRE 1.8以上が必要なため、以下から最新版のJDKのインストーラーを入手してインストールしてください。

- [http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)


### RTSystemEditor、RTCBuilderのソースコード

以下から[TortoiseSVN](https://tortoisesvn.net/)等によりチェックアウトしてください。


- [http://svn.openrtm.org/rtmtools/trunk/rtmtools/](http://svn.openrtm.org/rtmtools/trunk/rtmtools/)


## ビルド

eclipse.exeを実行してください。

### JREの設定
使用するJREを設定します。

「ウインドウ」→「設定」→「Java」→「インストール済みのJRE」で、「追加」→「標準 VM」を選択後にJREのパス(例：C:\Program Files (x86)\Java\jdk1.8.0_131\jre)を追加後にチェックを入れる

<br>

<div align="center"><a href="plugin4_1.png"><img src="plugin4_1.png" width="60%;"></a></div>

<br>

<div align="center"><a href="plugin5_1.png"><img src="plugin5_1.png" width="60%;"></a></div>

<br>

<div align="center"><a href="plugin6.png"><img src="plugin6.png" width="60%;"></a></div>

<br>

<div align="center"><a href="plugin7_1.png"><img src="plugin7_1.png" width="60%;"></a></div>

<br>

<div align="center"><a href="plugin8_1.png"><img src="plugin8_1.png" width="80%;"></a></div>

<br>



### コンパイラー準拠レベルの設定
初期の状態でコンパイラー準拠レベルが1.6に設定されている場合があるようなので、「ウインドウ」→「設定」→「Java」→「コンパイラー」でコンパイラー準拠レベルを1.8に設定してください。

<br>

<div align="center"><a href="plugin9_1.png"><img src="plugin9_1.png" width="80%;"></a></div>

<br>


### RTSystemEditor、RTCBuilderプロジェクトのインポート
RT System Editor、RTC Builderを開発環境のeclipseにインポートします。
「ファイル」→「インポート」→「プラグイン開発」→「プラグインおよびフラグメント」を選択後「次へ」を押してください。

<br>

<div align="center"><a href="plugin12.png"><img src="plugin12.png" width="60%;"></a></div>

<br>

<br>

<div align="center"><a href="plugin13.png"><img src="plugin13.png" width="60%;"></a></div>

<br>

「インポート先」の「ディレクトリー」をオンにして、rtmtoolsをチェックアウトしたディレクトリを設定して次へ進んでください。

<br>

<div align="center"><a href="plugin14_1.png"><img src="plugin14_1.png" width="60%;"></a></div>

<br>

全て追加を選択して、完了ボタンを押してください。



<br>

<div align="center"><a href="plugin15_1.png"><img src="plugin15_1.png" width="60%;"></a></div>

<br>


### IDLコンパイル
IDLファイルのコンパイルを行います。
パッケージエクスプローラーでjp.go.aist.rtm.toolscommonプロジェクトの「buildForCliant」を右クリックして「実行」→「Antビルド」を選択すれば開始します。


<br>

<div align="center"><a href="plugin2_1.png"><img src="plugin2_1.png" width="60%;"></a></div>

<br>

#### Antビルドで文字化けする場合
Antビルドで文字化けする場合は、「実行」→「外部ツール」→「外部ツールの構成」→「Antビルド」をダブルクリックして、「共通」タブ→「エンコード」でその他「MS932」に設定してください。


<br>

<div align="center"><a href="plugin10.png"><img src="plugin10.png" width="60%;"></a></div>

<br>

<br>

<div align="center"><a href="plugin11_1.png"><img src="plugin11_1.png" width="60%;"></a></div>

<br>


### クラスパスの修正
環境によってはクラスパスが正しく設定されない場合があります。
その場合はデバッグ時にClassNotFoundExceptionの例外が発生するため、rtmtoolsに存在するplugin.xml全てを修正してください。
パッケージエクスプローラーでplugin.xmlをダブルクリックして、「ランタイム」タブから「クラスパス」に「.」を追加してください。(「MANIFEST.MF」の「Bundle-ClassPath」に追加しても可)


<br>

<div align="center"><a href="plugin1_1.png"><img src="plugin1_1.png" width="60%;"></a></div>

<br>

これで準備完了です。


## デバッグ実行
上部の虫のマークのボタンから、「デバッグ」→「Eclipse アプリケーション」でデバッグが開始します。

<br>

<div align="center"><a href="plugin3_1.png"><img src="plugin3_1.png" width="60%;"></a></div>

<br>

