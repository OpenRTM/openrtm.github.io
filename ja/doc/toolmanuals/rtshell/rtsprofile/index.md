---
layout: page
title: rtsprofileモジュール
---

init
<!-- Title: rtsprofileモジュール -->
#contents

rtsprofile は Python で RTSProfile 仕様を利用するためのライブラリです。

## 概要

rtsprofile は RTシステムプロファイル（RTSProfile）の仕様のインタフェースライブラリです。
この仕様は完全な RTシステムを記述し、システムを復元することや管理することができます。XML も YAML を利用可能です。

このソフトウエアは NEDO (独立行政法人 新エネルギー・産業技術総合開発機構) の次世代ロボット知能化技術開発プロジェクトの支援により、独立行政法人産業技術総合研究所によって開発されています。

## 必要条件

- Python 2.5 以下では存在しない機能を使うので、Python 2.6 以上が必要となります。
- Ubuntu 9.04 を使っていたら、手動で Python 2.6 をインストールする必要があります。Ubuntu 9.04 以上をおすすめします。

## インストール

インストールはいくつかの方法が利用可能です。

- リポジトリ（参照：以下の[リポジトリ](#repo)）またはソースアーカイブからダウンロード後、適当なディレクトリーで解凍し、インストールする：

  1. ソースを展開する。
```
 $ cd /home/blurgle/src/
 $ tar -xvzf rtsprofile-2.0.0-tar.gz
```
  1. setup.pyを実行する。
```
 $ python setup.py install
```
  1. 必要に応じて、環境変数を設定します。これはデフォルトで設定されていますが、設定されていない場合は自分で設定する必要があります。
Windows上では、Python の site-packages ディレクトリーが **PYTHONPATH** 環境変数に、Python スクリプトのディレクトリーが **PATH** 環境変数に設定されていることを確認してください。
通常これらは **C:\\Python26\\Lib\\site-packages\\** と **C:\\Python26\\Scripts\\** です（Pythonが**C:\\Python26\\**にインストールされた場合）。

- Windows ではインストーラーの使用を推奨します。setup.py を利用すれば結果より容易に設定することができます。ただし、環境によってはさらに環境変数の設定が必要な場合があります。

## 使い方

ライブラリは **RtsProfle** のクラスを提供します。このクラスのインスタンスを作った後、RTSProfile のファイルを渡すことで完全な RTシステムプロファイルが作られます。
もしくは、手動で既存の RTシステムの RTシステムプロファイルを作成し、ファイル名を渡し、そのファイルに RTSProfile を保存します。

クラスの情報は Python の property でアクセスします。メソッドではありません。

API の詳細は Doxygen で構成されたドキュメンテーションを参照してください。

## テストの実行

ソースにサンプルファイルとテストのスクリプトが含めています。以下のようなコマンドで実行が可能です。

```
 $ python test/test.py ./test/rtsystem.xml
 $ python test/test.py ./test/rtsystem.yaml
```

PYTHONPATH の値によって、テストはインストールされた rtsprofile を使う可能性はあります。

## API naming conventions

rtsprofile は Python の標準スタイルに従います。[PEP8](http://www.python.org/dev/peps/pep-0008/)に参照してください。

最も重要な点は、プライベートな内部 API 関数はアンダースコア（「_」）で始まることです。アンダースコアで始まる関数はクラス外から証すべきではありません。
もし使用した場合には、未定義の振る舞いを引き起こす可能性があります。アンダースコアで始まらず、docstring がある関数だけを使ってください。

## より詳細なドキュメンテーションとサンプル

より詳細なドキュメンテーションは Doxygen で記述されたドキュメンテーションを参照してください。

サンプルは[rtshellのソース](https://github.com/OpenRTM/rtshell)を参照してください。

&aname(repo);
<a name="repo">
## リポジトリ 

最新版のソースは[githubでGitのリポジトリ](http://github.com/gbiggs/rtsprofile)にあります。「Download source」をクリックしてダウンロードをすることができます。
「git clone」を使うこともできます。パッチを送るなら、この方法がおすすめします。

```
 $ git clone git://github.com/gbiggs/rtsprofile.git
```

## Changelog
### 2.0

- Message Sending の情報の解析を修正しました。
- PrecedingCondition のタイムアウトのデータ型を整数にしました。
- YAML フォーマットを使えるようにしました。
- テストを追加しました。
- Preceding Conditions のデフォルトを"SYNC"に変更しました。
- バグフィクス

