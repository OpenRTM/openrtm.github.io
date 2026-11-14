---
layout: page
title: ソースからのビルド
---
<br>
<a>No English version available.
</a>

<!-- Title: ソースからのビルド -->
#contents

OpenRTM-aist-Java 本体のソースを変更して利用したい場合には、ソースからコンパイルすることができます。

## 配布ソースのビルド

OpenRTM-aist (Java版) は Eclipse を利用したビルド環境を提供しています。

<!-- ***対応 OS およびディストリビューション  -->
<!-- OpenRTM-aist は下記の OS および Linux ディストリビューションで動作することが確認されています。 -->
<!--  -->
<!-- - FreeBSD -->
<!-- - Vine Linux -->
<!-- - Fedora -->
<!-- - Debian -->
<!-- - Ubuntu -->
<!--  -->
<!-- これ以外の環境でも、一般的Linux/UNIX環境であれば、ビルドできる可能性があります。 -->
<!--  -->
### 依存ライブラリ

OpenRTM-aist のビルドには下記の開発環境およびライブラリが必要です。

- Eclipse SDK 3.3.x以上
- jdk1.7.0_xx以上
<!-- -Apache Ant version 1.6.5以上 -->
<!-- -ant4eclipse -->


それぞれのライブラリ等のドキュメントに従いインストールを行ってください。
<!-- これらのパッケージが、標準のディレクトリー(/usr, /usr/local 等)下にインストールされていると、以降の OpenRTM-aist のコンパイル作業を比較的簡単に行うことができます。 -->

### ソースのダウンロード

OpenRTM-aist-Java のソースをダウンロードします。

<!-- -http://www.openrtm.org/pub/OpenRTM-aist/java/ -->
- [OpenRTM-aist-Java-1.1.0-RELEASE.tar.gz](http://openrtm.org/pub/OpenRTM-aist/java/1.1.0/OpenRTM-aist-Java-1.1.0-RELEASE.tar.gz)


### ソースコードの展開 

まずソースコードを適当なディレクトリーに展開します。
- Linux の場合
```
 $ tar xvzf OpenRTM-aist-Java-X.X.X.tar.gz
```
- Windows の場合は、tgz を展開できるツールを使用して展開します。

### ビルド 
ビルド方法を説明します。（図は Windows 版の Eclipse3.4.2 です。）
Eclipse を起動し、プロジェクトをワークスペースへインポートします。
[ファイル] > [インポート] を選択します。
<div align="center"><a href="eclipse_open_import_ja.png"><img src="eclipse_open_import_ja.png" width="40%;"></a></div>
<div align="center"><strong>[ファイル] > [インポート]を選択</strong></div>
インポートの「選択」ウィンドウが開きます。ここで、[一般] > [既存プロジェクトをワークスペースへ] を選択して [次へ] ボタンをクリックします。
<div align="center"><a href="eclipse_select_import_ja.png"><img src="eclipse_select_import_ja.png" width="60%;"></a></div>
<div align="center"><strong>インポートの「選択」ウィンドウ</strong></div>
「プロジェクトのインポート」ウィンドウが開きます。「ルート・ディレクトリーの選択」へ展開したディレクトリーを指定して [完了] ボタンをクリックします。
<div align="center"><a href="eclipse_select_project_ja.png"><img src="eclipse_select_project_ja.png" width="60%;"></a></div>
<div align="center"><strong>「プロジェクトのインポート」ウィンドウ</strong></div>
これで、プロジェクトをワークスペースへインポートできます。
<div align="center"><a href="eclipse_open_project_ja.png"><img src="eclipse_open_project_ja.png" width="60%;"></a></div>
<div align="center"><strong>プロジェクトのインポート</strong></div>
パッケージ・エクスプローラーから build.xml を右クリックして [デバッグ] > -[2 Antビルド...] を選択します。
<div align="center"><a href="eclipse_select_ant_built_ja.png"><img src="eclipse_select_ant_built_ja.png" width="60%;"></a></div>
<div align="center"><strong>[デバッグ] > -[2 Antビルド...] を選択</strong></div>
構成編集のウィンドウが表示さます。ここで、buildAllLinux を選択して [デバッグ] ボタンをクリックします。
<div align="center"><a href="eclipse_execute_ant_ja.png"><img src="eclipse_execute_ant_ja.png" width="60%;"></a></div>
<div align="center"><strong>構成編集のウィンドウ</strong></div>
ビルドが始まります。
<div align="center"><a href="eclipse_execution_result_ja.png"><img src="eclipse_execution_result_ja.png" width="80%;"></a></div>
<div align="center"><strong>ビルド実行結果</strong></div>
コンソールウィンドウに以上の表示がでれば完了です。 <br>
日本語が文字化けしている場合は、メニューの「実行」→「外部ツール」→「外部ツールの構成」で共通タブを開き、文字コードを MS932 に変更（その他の欄に入力）します。


## リポジトリのソースのビルド

OpenRTM-aist は開発に利用している subversion リポジトリを一般に公開しています。
リポジトリからチェックアウトしたソースコードからビルドを行うこともできます。

### 必要なツール
Eclipse でリポジトリにアクセスするために Subclipse が必要です。
Subclipse：Eclipse のプラグイン（http://subclipse.tigris.org/update_1.0.x/）<br>
最初のビルドの時には ant4eclipse が必要です。
ant4eclipse：Eclipse のプラグイン(http://ant4eclipse.sourceforge.net)<br>

Windows ではこれに加えて、<br>
Python 及び PyYAML が必要です。[OpenRTM-aist の C++版のダウンロードのページ]({{ site.baseurl }}/en/download/openrtm-aist-cpp/openrtm-aist-cpp_1_1_1_release) からダウンロードして、
環境変数を設定してください。 
PATH に追加 C:\Python27 など<br>
[JSmooth](https://ja.osdn.net/projects/sfnet_jsmooth/) が必要です。インストールして環境変数 JSMOOTH_HOME を設定してください。JSMOOTH_HOME=C:\Program Files (x86)\JSmooth 0.9.9-7 など<br>
<!-- Wix のインストールが必要です。(http://sourceforge.net/project/showfiles.php?group_id=105970) -->

### ソースのチェックアウト
ソースのチェックアウト方法を説明します。（図は Windows 版の Eclipse3.4.2 です。）
Eclipse でソースをチェックアウトして、ワークスペースへインポートします。
[ファイル] > [インポート] でインポートの「選択」ウィンドウが開きます。ここで、[その他] > [SVNからプロジェクトをチェックアウト] を選択して [次へ] ボタンをクリックすると「SVNからチェックアウト」ウィンドウが開きます。
「新規リポジトリー・ロケーションを生成」を選択して「プロジェクトのインポート」[次へ] ボタンをクリックします。「Url」に **http://svn.openrtm.org/OpenRTM-aist-Java/trunk/** と入力し [次へ] ボタンをクリックします。
「フォルダの選択」ウィンドウが開きますので、「jp.go.aist.rtm.RTC」を選択して [完了] ボタンをクリックします。<br>
初回のみ(http://svn.openrtm.org/OpenRTM-aist-Java/trunk)からスクリプトファイルまたはバッチファイルをダウンロードして実行してください。<br>
これらのファイル Subclipse ではチェックアウトできません。<br>
idl ファイルから必要な java ソースファイルが生成されます。<br>
現状の trunk には不備があり、TEST ファイル等の一部でエラーが出るほか、Windows では msi ファイルが生成されません。

### ビルド(2回目以降) 
ビルド方法を説明します。（図は Windows 版の Eclipse 3.4.2です。）
パッケージ・エクスプローラーから build.xml を右クリックして [デバッグ] > [2 Antビルド...] を選択します。
<div align="center"><a href="eclipse_select_ant_built_ja.png"><img src="eclipse_select_ant_built_ja.png" width="40%;"></a></div>
<div align="center"><strong>[デバッグ] > -[2 Antビルド...] を選択</strong></div>
構成編集のウィンドウが表示さます。
ここで、buildAllLinux を選択して [デバッグ] ボタンをクリックします。
<div align="center"><a href="eclipse_execute_ant_ja.png"><img src="eclipse_execute_ant_ja.png" width="60%;"></a></div>
<div align="center"><strong>構成編集のウィンドウ</strong></div>
ビルドが始まります。
<div align="center"><a href="eclipse_execution_result_ja.png"><img src="eclipse_execution_result_ja.png" width="80%;"></a></div>
<div align="center"><strong>ビルド実行結果</strong></div>
コンソールウィンドウに以上の表示がでれば完了です。


