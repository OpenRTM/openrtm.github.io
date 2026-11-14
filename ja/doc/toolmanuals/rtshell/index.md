---
layout: page
title:  rtshell
---

<!-- Title: rtshell -->
#contents

## イントロダクション

rtshellは、ネームサーバー上に登録されているRTコンポーネントをシェルから管理できるツールです。
コンポーネントをactivate/deactivate/resetしたり、ポートの接続を行うことができます。
RTシステムの管理もできます。

このツールは、リソースの少ないシステム、GUIの利用ができない環境(特にコンポーネントを管理する他のPCとネットワークでつながっていない環境など)や、RTSystemEditorの利用ができない環境、スクリプトでRT Systemを構築する場合などで有効です。コマンドラインの利用に精通している人にも便利なツールです。

<!-- このソフトウエアはNEDO(独立行政法人新エネルギー産業技術総合開発機構)の次世代ロボット知能化技術開発プロジェクトの支援により、独立行政法人産業技術総合研究所によって開発されています。 -->
<!-- 管理番号H23PRO-1214。 -->

<!-- This software is licensed under the GNU Lesser General Public License version 3 -->
<!-- (LGPL3). See LICENSE.txt. -->
<!--  -->

## 必要条件

- rtctreeが必要です。
- rtsprofileが必要です。
- Python3以上、OpenRTM-aist-Pythonが必要です。
  - 詳細な対応しているPythonバージョンについては[ダウンロードページ]({{ site.baseurl }}/ja/download/openrtm-aist-cpp/openrtm-aist-cpp_1_2_2_release#toc1)をご確認ください。


<!-- pipによりインストールする場合は、trctreeとrtsprofileは自動的にインストールされます。 -->


## インストール

インストール方法については[rtshellのインストール]({{ site.baseurl }}/ja/doc/installation/install_rtshell)のページを参照してください。
<!-- インストールはいくつかの方法が利用可能です。 -->
<!--  -->
<!-- - (好ましい方法) pipを利用してPyPiからインストールする。 -->
<!--  -->
<!-- ++ 必要にお応じてpipをインストールします。 -->
<!-- https://pip.pypa.io/en/latest/installing/を参照してください。 -->
<!-- ++ pipを実行します。 -->
<!-- $ pip install rtshell -->
<!-- ++ 以下のコマンドを実行し、インストール後のアクションを行います。 -->
<!-- $ rtshell_post_install -->
<!-- ++ Windows上では、必要に応じて環境変数を設定します。通常デフォルトで設定されていますが、設定されていない場合は自分で設定する必要があります。 -->
<!-- PythonスクリプトのディレクトリがPATH環境変数に設定されていることを確認してください。通常、これらはC:\Python27\Scripts\です（PythonがC:\Python27\にインストールされた場合）。 -->
<!-- ++ リポジトリまたはソースアーカイブからダウンロード後、適当なディレクトリで解凍し、インストールする。 -->
<!-- ++ ソースを展開します。 -->
<!-- $ cd /home/blurgle/src/ -->
<!-- $ tar -xvzf rtshell.tar.gz -->
<!-- ++ setup.pyを実行します。 -->
<!-- $ python setup.py install -->
<!-- ++ 以下のコマンドを実行し、インストール後のアクションを行います。 -->
<!-- $ rtshell_post_install -->
<!-- ++ Windows上では、必要に応じて環境変数を設定します。通常デフォルトで設定されていますが、設定されていない場合は自分で設定する必要があります。 -->
<!-- PythonスクリプトのディレクトリがPATH環境変数に設定されていることを確認してください。通常、これらはC:\Python27\Scripts\です（PythonがC:\Python27\にインストールされた場合）。 -->
<!-- Windows上では、インストーラープログラムを利用してインストール可能です。 -->
<!--  -->

## リポジトリ

最新版のソースはgithubのリポジトリにあります（URL:http://github.com/OpenRTM/rtshell）。
[Download ZIP]をクリックしてダウンロードできます。下記のように"git clone"コマンドを使うこともできます。(gitが前もってインストールされている必要があります)。

```
  $ git clone git://github.com/OpenRTM/rtshell.git
```


## ドキュメント

ドキュメントはLinuxではmanページとして提供し、/usr/local/share/manにインストールされます。Windowsの場合はHTMLにて提供し、<pythonディレクトリ>\Lib\site-packages\rtshell\data\doc\htmlの下のen、jaディレクトリの下に英語版、日本語版がそれぞれコピーされます。また本Webサイト上にも掲載しています。

<!-- このパスを$MANPATHという環境変数に追加する必要な場合があります。例えば、rtshellのmanページが/usr/local/share/manにインストールされた場合、以下の行を.bashrcに追加してください。 -->
<!-- export MANPATH=/usr/local/share/man:${MANPATH} -->

<!-- **テストの実行 -->
<!--  -->
<!-- コマンドのテストはソースディレクトリから実行できます: -->
<!--  -->
<!-- ~/src/rtshell $ ./test/test_cmds.py ~/share/OpenRTM-aist/examples/rtcs/ -->
<!--  -->
<!-- 変数はRTCのモジュールを持つディレクトリです。Motor、ControllerおよびSensorのモジュールが必要です。 -->
<!--  -->
<!-- 一つのコマンドのテストだけを実行するの場合、そのテストの名を変数に追加してください。: -->
<!--  -->
<!-- $ ./test/test_cmds.py ~/share/OpenRTM-aist/examples/rtcs/ rtactTests -->

<hr>

以下未作成。

- [rtshellコマンド・リファレンス](./command_reference)
- [rtctreeモジュール](./rtctree)
- [rtsprofileモジュール](./rtsprofile)
