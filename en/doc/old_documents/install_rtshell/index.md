---
layout: page
title: rtshell のインストール
---


#contents

<br>
<a>No English version available.
</a>

## はじめに

このドキュメントでは、Windows で rtshell のインストール方法について説明します。


### rtshellとは

[rtshell]({{ site.baseurl }}/en/doc/toolmanuals/rtshell) はネームサーバー上に登録されている RTコンポーネントを、シェル (コマンドプロンプト) から管理することができるツールです。
コンポーネントを activate/deactivate/reset したり、ポートの接続を行うことができます。RTシステム全体を管理することも可能です。


### インストールの流れ

- OpenRTM-aist Python版と PyYAML のインストール
- rtctree（支援ライブラリ）のインストール
- rtsprofile（支援ライブラリ）のインストール
- rtshell のインストール
- 実行確認


### OpenRTM-aist Python版 と PyYAMLのインストール

rtshell の一部の機能（システム管理）には OpenRTM-aist-Python が必要です。

OpenRTM-aist-Python のインストールドキュメントに従って Python 2.6 または 2.7と OpenRTM-aist-Python をインストールします。
[ドキュメント]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/install_windows_python_1_1) を参照してください。

PyYAML は[PyYAMLのウェブサイト](http://pyyaml.org/) からダウンロードしてインストールします。バージョンは一番最新でも大丈夫です。


### rtctree のインストール

openrtm.org の[ダウンロードサイト]()から
rtctree-3.1 のパッケージ (rtctree-3.1.0.win32.exe) をダウンロードします。

パッケージを実行すると、以下のようなダイアログが表示されるので、[次へ] をクリックします。

<div align="center"><a href="rtctree_installer_1.png"><img src="rtctree_installer_1.png" width="100%;"></a></div><br>

Python のバージョンを選択するダイアログが表示されます。Python の正しいバージョンが選択されていることを確認し、[次へ] をクリックします。
以下の例では Python2.6 が選択されています。

<div align="center"><a href="rtctree_installer_2.png"><img src="rtctree_installer_2.png" width="100%;"></a></div><br>

「インストール準備完了」ダイアログが表示されます。さらに [次へ] をクリックします。

<div align="center"><a href="rtctree_installer_3.png"><img src="rtctree_installer_3.png" width="100%;"></a></div><br>

インストールが行われます。終わったら、[完了] をクリックしてインストールを終了します。

<div align="center"><a href="rtctree_installer_4.png"><img src="rtctree_installer_4.png" width="100%;"></a></div><br>


### rtsprofile のインストール

openrtm.org の[ダウンロードサイト]()から
rtsprofile-3.1 のパッケージ (rtsprofile-3.1.0.win32.exe) をダウンロードします。

パッケージを実行すると、以下のようなダイアログが表示されるので、[次へ] をクリックします。

<div align="center"><a href="rtsprofile_installer_1.png"><img src="rtsprofile_installer_1.png" width="100%;"></a></div><br>

Python のバージョンを選択するダイアログが表示されます。Python の正しいバージョンが選択されていることを確認し、[次へ] をクリックします。
以下の例では Python2.6 が選択されています。

<div align="center"><a href="rtsprofile_installer_2.png"><img src="rtsprofile_installer_2.png" width="100%;"></a></div><br>

「インストール準備完了」ダイアログが表示されます。さらに [次へ] をクリックします。

<div align="center"><a href="rtsprofile_installer_3.png"><img src="rtsprofile_installer_3.png" width="100%;"></a></div><br>

インストールが行われます。終わったら、[完了] をクリックしてインストールが終了します。

<div align="center"><a href="rtsprofile_installer_4.png"><img src="rtsprofile_installer_4.png" width="100%;"></a></div><br>


### rtshell のインストール

openrtm.org の [ダウンロードサイト]() から
rtshell-3.0.0 のパッケージ (rtshell-3.1.0.win32.exe)をダウンロードします。

パッケージを実行すると、以下のようなダイアログが表示されるので、[次へ] をクリックします。

<div align="center"><a href="rtshell_installer_1.png"><img src="rtshell_installer_1.png" width="100%;"></a></div><br>

Python のバージョンを選択するダイアログが表示されます。Python の正しいバージョンが選択されていることを確認し、[次へ] をクリックします。
以下の例では Python2.6 が選択されています。

<div align="center"><a href="rtshell_installer_2.png"><img src="rtshell_installer_2.png" width="100%;"></a></div><br>

「インストール準備完了」ダイアログが表示されます。さらに [次へ] をクリックします。

<div align="center"><a href="rtshell_installer_3.png"><img src="rtshell_installer_3.png" width="100%;"></a></div><br>

インストールが行われます。終わったら、[完了] をクリックしてインストールを終了します。

<div align="center"><a href="rtshell_installer_4.png"><img src="rtshell_installer_4.png" width="100%;"></a></div><br>


### 実行確認

実行確認のために、rtshell のコマンド群のうち rtls コマンドを実行して rtshell が正しくインストールされているかどうかをテストします。

はじめに、OpenRTM-aist の ネームサービスを起動して、ConsoleIn を起動します。

コンポーネントを起動したら、Windows のコマンドプロンプトを起動します。

<div align="center"><a href="start_command_prompt.png"><img src="start_command_prompt.png" width="25%;"></a></div>

コマンドプロンプトで以下のコマンドを実行します。

```
  set RTCTREE_NAMESERVERS=127.0.0.1
  rtls -R
```

１行目は環境変数を設定します。「RTCTREE_NAMESERVERS」は、rtshell の支援ライブラリ rtctree が使う変数で、rtshell が見るネームサーバーを指定します。

２行目はすべてのネームサーバーに登録されているコンポーネントを表示します。成功の場合は以下のように表示されます。

<div align="center"><a href="rtls_output.png"><img src="rtls_output.png" width="100%;"></a></div>

### 動かない場合

コマンドが見つけられない場合は、PATH が設定されていない可能性があります。
PATH 環境変数に以下のような二つのパスを追加すると動きます。（例は Python 2.6がインストールされている場合です。）

```
  C:\Python26
  C:\Python26\Scripts
```
