---
layout: page
title: ソースからのビルド
---

<!-- Title: ソースからのビルド -->
#contents

OpenRTM-aist-Java本体のソースを変更して利用したい場合には、ソースからコンパイルできます。

## 配布ソースのビルド

OpenRTM-aist(Java版)はEclipseを利用したビルド環境を提供しています。


### 依存ライブラリ

OpenRTM-aistのビルドには下記の開発環境およびライブラリが必要です。

- Eclipse SDK 3.3.x以上<br>
　Eclipseの入手先<br>
　[Eclipse Foundation](https://www.eclipse.org/)<br>
　日本語版<br>
　[MergeDoc Project](https://mergedoc.osdn.jp/)<br>

- JDK8<br>
　[JDK8のインストール]({{ site.baseurl }}/ja/doc/toolmanuals/rtc_builder-1_2_0/update_rtcb_1_2_0)

それぞれのライブラリなどのドキュメントに従いインストールを行ってください。

### ソースのダウンロード

OpenRTM-aist-Javaのソースをダウンロードします。


- [OpenRTM-aist-Java-1.2.1](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/tag/v1.2.1)


### ソースコードの展開

まずソースコードを適当なディレクトリに展開します。
- Linuxの場合
```
 $ tar xvzf OpenRTM-aist-Java-X.X.X.tar.gz
```
- Windowsの場合は、tgzを展開できるツールを使用して展開します。

### ビルド
#### プロジェクトのインポート
ビルド方法を説明します。(図はWindows版のEclipse3.4.2です。)
Eclipseを起動し、プロジェクトをワークスペースへインポートします。
[ファイル]>[インポート]を選択します。
<div align="center"><a href="rtm16.png"><img src="rtm16.png" width="60%;"></a></div>
<div align="center"><strong>[ファイル]>[インポート]を選択</strong></div>
インポートの[選択]ウィンドウが開きます。ここで、[一般]>[既存プロジェクトをワークスペースへ]を選択して[次へ]ボタンをクリックします。
<div align="center"><a href="rtm17.png"><img src="rtm17.png" width="60%;"></a></div>
<div align="center"><strong>インポートの「選択」ウィンドウ</strong></div>
[プロジェクトのインポート]ウィンドウが開きます。[ルート・ディレクトリの選択]へ展開したディレクトリを指定して[完了]ボタンをクリックします。
<div align="center"><a href="rtm18.png"><img src="rtm18.png" width="60%;"></a></div>
<div align="center"><strong>[プロジェクトのインポート]ウィンドウ</strong></div>
これで、プロジェクトをワークスペースへインポートできます。

#### JDEの設定
ビルドに使用するJDKの設定を行います。
まず[ウィンドウ]>[設定]で設定画面を開きます。

<div align="center"><a href="rtm19.png"><img src="rtm19.png" width="60%;"></a></div>
<div align="center"><strong>[ウィンドウ]>[設定]を選択</strong></div>

左側のツリーから[Java]>[インストール済みのJRE]を選択して追加ボタンを押します。

<div align="center"><a href="rtm20.png"><img src="rtm20.png" width="60%;"></a></div>
<div align="center"><strong>インストール済みのJRE</strong></div>

[標準VM]を選択して次へ進みます。

<div align="center"><a href="rtm21.png"><img src="rtm21.png" width="60%;"></a></div>
<div align="center"><strong>JREの追加</strong></div>

JREホームにJDKインストールフォルダー以下のjreフォルダーのパスを指定して完了する。

<div align="center"><a href="rtm22.png"><img src="rtm22.png" width="60%;"></a></div>
<div align="center"><strong>JREの設定</strong></div>

インストール済みJREで設定したJDKのチェックボックスをオンにすれば完了です。

<div align="center"><a href="rtm23.png"><img src="rtm23.png" width="60%;"></a></div>
<div align="center"><strong>JDKの設定</strong></div>

パッケージ・エクスプローラーから「build.xml」を右クリックして[実行]>[2 Antビルド...]を選択します。
<div align="center"><a href="rtm25.png"><img src="rtm25.png" width="60%;"></a></div>
<div align="center"><strong>[実行]>[2 Antビルド...]を選択</strong></div>
構成編集のウィンドウが表示さます。ここで、**jar**、**idlCompile**、**idlCompileEtc**、**clean**、**compile_win**を選択して[実行]ボタンをクリックします。
<div align="center"><a href="rtm26.png"><img src="rtm26.png" width="60%;"></a></div>
<div align="center"><strong>構成編集のウィンドウ</strong></div>
ビルドが始まります。

コンソールウィンドウに**BUILD SUCCESSFUL**や**ビルド成功**の表示がでれば完了です。<br>
日本語が文字化けしている場合は、メニューの[実行]→[外部ツール]→[外部ツールの構成]で共通タブを開き、文字コードを**MS932**に変更（[その他]の入力ボックスで手動入力）します。


