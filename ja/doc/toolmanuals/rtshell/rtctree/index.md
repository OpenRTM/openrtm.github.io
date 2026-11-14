---
layout: page
title: rtctreeモジュール
---

<!-- Title: rtctreeモジュール -->
#contents

rtctree は Python で RTコンポーネントの管理をするためのライブラリです。

## 概要 

rtctree は簡単な API で RTコンポーネントの管理をするための Python用のライブラリです。開発者は CORBA の API を知らなくとも、他のプログラムから、RTコンポーネントのシステムを管理することができます。
コンポーネントを activate したり deactivate したり、コンポーネント間の接続を行うことが可能です。

このソフトウエアは NEDO (独立行政法人 新エネルギー・産業技術総合開発機構) の次世代ロボット知能化技術開発プロジェクトの支援により、独立行政法人産業技術総合研究所によって開発されています。

## 必要条件

- ominorb-py 及び omniidl と omniidl用の Python モジュールが必要となります。
- Python 2.5 以下では存在しない機能を使うので、Python 2.6 以上が必要となります。
- Ubuntu 9.04 を使っていたら、手動で Python 2.6 をインストールすることが必要となります。そのため、Ubuntu 9.04 以上をおすすめします。

## インストール

インストールはいくつかの方法が利用可能です。

- リポジトリ（参照：以下の[リポジトリ](#repo)）またはソースアーカイブからダウンロード後、適当なディレクトリーで解凍し、インストールする：
  1. ソースを展開する。
```
 $ cd /home/blurgle/src/
 $ tar -xvzf rtctree-2.0.0.tar.gz
```
  1. setup.pyを実行する。
```
 $ python setup.py install
```
  1. 必要に応じて、環境変数を設定します。これはデフォルトで設定されていますが、設定されていない場合は自分で設定する必要があります。Windows上では、Python の site-packages ディレクトリーが **PYTHONPATH** 環境変数に、Python スクリプトのディレクトリが **PATH** 環境変数に設定されていることを確認してください。通常、これらは **C:\\Python26\\Lib\\site-packages\\** と **C:\\Python26\\Scripts\\** です（Pythonが**C:\\Python26\\**にインストールされた場合）。

- Windows ではインストーラーの使用を推奨します。setup.py を利用すれば結果より容易に設定することができます。ただし、環境によってはさらに環境変数の設定が必要な場合があります。


## 環境変数

以下の環境変数が使われます。

<table class="table-alt">
  <tr>
    <td><strong>RTCTREE_ORB_ARGS</strong></td>
    <td>ORB作成時に与えるセミコロンで区切られた引数のリスト。設定することは必要となりません。</td>
  </tr>
  <tr>
    <td><strong>RTCTREE_NAMESERVERS</strong></td>
    <td>セミコロンで区切った RTC ツリーのためのネームサーバーのアドレスのリスト。この変数に書いたサーバーはツリーに追加します。設定することは必要となりません。</td>
  </tr>
</table>

普通の場合、RTCTREE_ORB_ARGS を設定することは必要となりません。RTCTREE_NAMESERVERS を設定したら、rtctree を使うときにもっと便利となります。例えば、Bash シェルでしたら：

```
 $ export RTCTREE_NAMESERVERS=localhost;192.168.0.1:65346;example.com
```

## RTC ツリー

ライブラリの主要部分は RTC ツリーです。
```
 import rtctree.tree
 tree = rtctree.tree.RTCTree()
```
これはネーミングコンテキスト、コンポーネントおよびマネージャを取得するためにネームサーバ〜を検索して作成したファイルシステムのようなツリーです。通常のファイルシステムを扱う場合とまったく同じように扱うことができます。ツリーはすべての既知のネームサーバーに登録されたネーミングコンテキスト、マネージャ、およびコンポーネントをツリー構造で表します。

```
 \  
 |-+localhost
 | |-+naming_context
 | | |--ConsoleIn0.rtc</td>
 | | |--ConsoleOut0.rtc</td>
 | |
 | |--another_naming_context</td>
 | |--Sensor0.rtc</td>
 | 
 |-+192.168.0.5</td>
   |--Motor0.rtc</td>
   |--Controller0.rtc</td>
```

ツリー内の各ディレクトリーは、通常のネーミングコンテキストまたはネームサーバーのルートコンテキストです。ネームサーバーのルートコンテキストは **NameServer** クラスで示します。また、ネーミングコンテクストは **'Directory'** クラスで示し、マネージャは **Manager** クラスで示します。

ネームサーバーは、ルートディレクトリーからのディレクトリーとして扱われます。その下はファイルとサブディレクトリーです。サブディレクトリーはルートコンテクストの下のネーミングコンテクスト及びマネージャを示します。

ファイルはコンポーネントとマネージャです。コンポーネントは Componentクラスで示します。

コンポーネントオブジェクトが表しているコンポーネントに関するさまざまな情報を格納します。コンポーネントを activate や deactivate したり、コンポーネントのポートを管理したり、ポートを接続したり、構成設定を設定したりができます。

マネージャで新しいコンポーネントインスタンスを作ったり、コンポーネントを消したりことができます。

ツリー内のすべてのノードにも、それらが表すオブジェクトには、CORBA オブジェクトの参照を格納します。このオブジェクトにアクセスすることで、IDL のメソッドを呼び出すことができます。もし現在 rtctree で実現不可能な機能があったとしても、この CORBA オブジェクトを利用し IDL メソッドを直接的に呼び出すことができます。


### ツリーの構築

ツリーのファクトリ関数の引数（**create_tree()**）は、ツリーを構築するための解析対象となるネームサーバーを指定します。詳しくは当該関数のドキュメンテーションに参照してください。一般的に、ネームサーバーのアドレスのリストまたはパスのリストを渡してツリーを構築することができます。環境変数 **RTCTREE_NAMESERVERS** もチェックされます。

### パス 

ツリー内のノードはパスで指定されます。パスはストリングのリストです。一つ右のレベルは、左のものより1レベル深くなります。絶対パスは、ツリーオブジェクトを指定するために必要となります。もしパスがノード以下に存在する場合、ノードからの相対パス指定も可能です。

これらのパス文字列は、ファイルシステムパス指定と似ています。ツリーのルートは`/`で示します（Windowsの場合は`\`）。最初のレベルはネームサーバーのアドレスです。その下のレベルはコンポーネント、マネージャ及びネーミングコンテクスト（ディレクトリーとしてしめす）です。**parse_path**と言う関数は文字列のパスを RTC ツリー用のパスに変更します。

例えば、以下のパス：
```
 /localhost/naming_context/ConsoleIn0.rtc
```
は**localhost**上で起動しているネームサーバーの**naming_context**の下に登録された **ConsoleIn0.rtc** と言うコンポーネントを示します。ツリーからそのコンポーネントのオブジェクトを取得したい時、パスを **parse_path** で Python のリストに変更する必要があります。
```
 ['/', 'localhost', 'naming_context', 'ConsoleIn0.rtc']
```

### ヘルパー関数

以下は RTCTree クラス及びさまざまなノードクラスのためのヘルパー関数です。以下はすべての API を示しているわけではありません。Doxygen で記述されたAPIのドキュメンテーションを参照してください。例は rtcshell のソースを参照してください。

<table class="table-alt">
  <tr>
    <td><strong>RTCTree.has_path</strong></td>
    <td>ツリーのパスがあるかどうかをチェックします。コンポーネントの存在をチェックするには、この関数を使うと便利です。</td>
  </tr>
  <tr>
    <td><strong>RTCTree.get_node</strong></td>
    <td>ツリーからノードを取得します。コンポーネント、ディレクトリなどを取得するためにこの関数を使ってください。</td>
  </tr>
  <tr>
    <td><strong>RTCTree.is_component</strong></td>
    <td>パスはコンポーネントを指しているかどうかを調べます。ノードクラスは<strong>is_component</strong>という同じ機能のプロパティーを持っています。<strong>is_directory</strong>、<strong>is_manager</strong>及び<strong>is_nameserver</strong>という関数およびプロパティーもあります。</td>
  </tr>
  <tr>
    <td><strong>RTCTree.iterate()</strong></td>
    <td>ツリーのすべてのノードに同じ関数を実行します。すべての結果はリストとして返されます。例はrtcshellの<strong>rtls</strong>を参照してください。</td>
  </tr>
</table>

<br>
<table class="table-alt">
  <tr>
    <td><strong>Node.children</strong></td>
    <td>ノードのすべての子ノード。例：ディレクトリーの下のコンポーネントのリストを取得するために利用することができます。</td>
  </tr>
  <tr>
    <td><strong>Node.full_path</strong></td>
    <td>ツリーのルートからこのノードまでのパス。</td>
  </tr>
  <tr>
    <td><strong>Node.name</strong></td>
    <td>ノードの名前。例：ディレクトリの名前。</td>
  </tr>
  <tr>
    <td><strong>Node.parent_name</strong></td>
    <td>ノードの親の名前。</td>
  </tr>
  <tr>
    <td><strong>Node.root</strong></td>
    <td>このノードのツリーのルートノード。返されたオブジェクトでツリーのほとんどすべての機能ができます。</td>
  </tr>
</table>

<br>

<table class="table-alt">
  <tr>
    <td><strong>Component.activate_in_ec()</strong></td>
    <td>コンポーネントをactivateします。通常は ec_index は 0 で構いません。</td>
  </tr>
  <tr>
    <td><strong>Component.deactivate_in_ec()</strong></td>
    <td>コンポーネントをdeactivateします。</td>
  </tr>
  <tr>
    <td><strong>Component.reset_in_ec()</strong></td>
    <td>コンポーネントをresetします。</td>
  </tr>
  <tr>
    <td><strong>Component.state_in_ec()</strong></td>
    <td>あるexecution contextでコンポーネントのステートを得ます。</td>
  </tr>
  <tr>
    <td><strong>Component.alive</strong></td>
    <td>コンポーネントがaliveかどうかをチェックします。</td>
  </tr>
  <tr>
    <td><strong>Component.owned_ecs</strong></td>
    <td>コンポーネントが持っているexecution contextのリストです。</td>
  </tr>
  <tr>
    <td><strong>Component.participating_ecs</strong></td>
    <td>コンポーネントが使っているexecution contextのリストです。</td>
  </tr>
  <tr>
    <td><strong>Component.state</strong></td>
    <td>コンポーネントのステートです。</td>
  </tr>
  <tr>
    <td><strong>Component.state_string</strong></td>
    <td>文字列にしたコンポーネントのステートです。</td>
  </tr>
  <tr>
    <td><strong>Component.disconnect_all()</strong></td>
    <td>コンポーネントのすべてのポートのすべての接続を切断します。</td>
  </tr>
  <tr>
    <td><strong>Component.get_port_by_name()</strong></td>
    <td>コンポーネントのポートを名前で探す。</td>
  </tr>
  <tr>
    <td><strong>Component.ports</strong></td>
    <td>コンポーネントのポートのリストです。入力ポート、出力ポート、及びサービスポートのリストが含まれ、かつ現在接続状態のポートのリストも取得できます。</td>
  </tr>
  <tr>
    <td><strong>Component.object</strong></td>
    <td>コンポーネントのCORBAの**LightweightRTObject**オブジェクトです。</td>
  </tr>
  <tr>
    <td><strong>Component.activate_conf_set</strong></td>
    <td>コンフィグレーションセットをactivateします。</td>
  </tr>
  <tr>
    <td><strong>Component.set_conf_set_value</strong></td>
    <td>コンフィグレーションセットの変数を設定します。</td>
  </tr>
  <tr>
    <td><strong>Component.active_conf_set</strong></td>
    <td>現在のactiveコンフィグレーションセットです。</td>
  </tr>
  <tr>
    <td><strong>Component.active_conf_set_name</strong></td>
    <td>現在のactiveコンフィグレーションセットの名前です。</td>
  </tr>
  <tr>
    <td><strong>Component.conf_sets</strong></td>
    <td>コンフィグレーションセットのリストです。</td>
  </tr>
</table>

<br>
<table class="table-alt">
  <tr>
    <td><strong>Port.connect()</strong></td>
    <td>このポートを別のポートに接続します。</td>
  </tr>
  <tr>
    <td><strong>Port.disconnect_all()</strong></td>
    <td>このポートのすべての接続を切断します。</td>
  </tr>
  <tr>
    <td><strong>Port.get_connection_by_dest()</strong></td>
    <td>このポートの接続を他のポートで探します。</td>
  </tr>
  <tr>
    <td><strong>Port.get_connection_by_name()</strong></td>
    <td>このポートの接続を名前で探します。</td>
  </tr>
  <tr>
    <td><strong>Port.connections</strong></td>
    <td>このポートの接続リストです。</td>
  </tr>
  <tr>
    <td><strong>Port.is_connected</strong></td>
    <td>このポートは接続の状態かどうかをチェックします。</td>
  </tr>
  <tr>
    <td><strong>Port.name</strong></td>
    <td>ポートの名前です。</td>
  </tr>
  <tr>
    <td><strong>Port.objecti</strong></td>
    <td>このポートのCORBAの<strong>PortService</strong>オブジェクトです。</td>
  </tr>
  <tr>
    <td><strong>Port.name</strong></td>
    <td>ポートのオーナー（通常は<strong>Component</strong>オブジェクト）です。</td>
  </tr>
  <tr>
    <td><strong>Port.porttype</strong></td>
    <td>ポートの種類（<strong>DataInPort</strong>、<strong>DataOutPort</strong>及び<strong>CorbaPort</strong>）。</td>
  </tr>
</table>

<table class="table-alt">
  <tr>
    <td><strong>Connection.disconnect()</strong></td>
    <td>この接続を切断します。</td>
  </tr>
  <tr>
    <td><strong>Connection.ports</strong></td>
    <td>この接続のソースや目的ポートのリストです。</td>
  </tr>
</table>
<br>
<table class="table-alt">
  <tr>
    <td><strong>ConfigurationSet.has_param()</strong></td>
    <td>このセットに変数があるかどうかをチェックします。</td>
  </tr>
  <tr>
    <td><strong>ConfigurationSet.set_param()</strong></td>
    <td>このセットの変数を設定します。</td>
  </tr>
</table>
<br>
<table class="table-alt">
  <tr>
    <td><strong>ExecutionContext.activate_component()</strong></td>
    <td>このexecution contextでコンポーネントをactivateします。</td>
  </tr>
  <tr>
    <td><strong>ExecutionContext.deactivate_component()</strong></td>
    <td>このexecution contextでコンポーネントをdeactivateします。</td>
  </tr>
  <tr>
    <td><strong>ExecutionContext.reset_component()</strong></td>
    <td>このexecution contextでコンポーネントをresetします。</td>
  </tr>
  <tr>
    <td><strong>ExecutionContext.get_component_state()</strong></td>
    <td>このexecution contextの中のコンポーネントのステートをとります。</td>
  </tr>
  <tr>
    <td><strong>ExecutionContext.running</strong></td>
    <td>このexecution contextは起動しているかどうかをチェックします。</td>
  </tr>
</table>
<br>
<table class="table-alt">
  <tr>
    <td><strong>Manager.create_component()</strong></td>
    <td>新しいコンポーネントインスタンスを作ります。</td>
  </tr>
  <tr>
    <td><strong>Manager.delete_component()</strong></td>
    <td>コンポーネントインスタンスを削除します。</td>
  </tr>
</table>

<br>
<table class="table-alt">
  <tr>
    <td><strong>dict_to_nvlist()</strong></td>
    <td>PythonのdictをCORBAのnamevalueリストに変更します。</td>
  </tr>
  <tr>
    <td><strong>nvlist_to_dict()</strong></td>
    <td>CORBAのnamevalueリストをPythonのdictに変更します。</td>
  </tr>
</table>

## APIのスタイル

rtctreeはPythonの標準スタイルに従います。[PEP8](http://www.python.org/dev/peps/pep-0008/)に参照してください。

最も重要な点は、プライベートな内部API関数はアンダースコア（「_」）で始まることです。アンダースコアで始まる関数はクラス外から証すべきではありません。もし使用した場合には、未定義の振る舞いを引き起こす可能性があります。アンダースコアで始まらず、docstringがある関数だけを使ってください。

&aname(repo);
<a name="repo">
## リポジトリ

最新版のソースは[githubでGitのリポジトリ](http://github.com/gbiggs/rtctree)にあります。「Download source」をクリックしてダウンロードをすることができます。「git clone」を使うこともできます。パッチを送りたがったら、この方法がおすすめします。

```
 $ git clone git://github.com/gbiggs/rtctree.git
```

## より詳細なドキュメンテーションとサンプル

より詳細なドキュメンテーションはDoxygenで記述されたドキュメンテーションを参照してください。

サンプルは[rtshellのソース](https://github.com/OpenRTM/rtshell)を参照してください。これらはRTSystemEditorで実現可能なことをrtctreeで行う方法のほぼ全てを示しています。

## Changelog 

### 3.0
- 例外を警告にしました。
- ゾンビの扱いを改善しました。
- ゾンビ検出マネージャ。
- コンポジットコンポーネントの情報を得るAPIを追加しました。
- ポートからIDによってコネクションを得るAPIを追加しました。
- ORBを渡すAPIを追加しました。
- パスフォーマッタを追加しました。
- 例外を読みやすく表示するようにしました。
- パフォーマンスの向上
- 解析するパスを制限する機能を追加しました。
- ゾンビノードを追加しました。
- コンポーネントを終了するAPIを追加しました。
- create_rtctree()関数を削除しました。RTCTree()を使ってください。
- remove_node()APIを追加しました。
- node.full_path をリストに変更し、node.full_path_str を追加しました。

### 2.0

- 実行コンテキストに関してより多くの情報を解析するようにしました。
- ORBオブジェクトを外部から与えられるようにしました。
- reparse_connections()関数をpublicにしました。
- ノードで使用されているORBを取得するための新しいAPIを追加しました。
- コンテキストから名前をアンバインドするための新しいAPIを追加しました。
- より多くのCORBAオブジェクトへのアクセスを可能にしました。
- ゾンビの認識効率が向上しました。
- 未知なCORBAオブジェクトの扱い方を修正しました。
- オーナーが未知なポートの扱い方を修正しました。
- rtctreeオブジェクトをスレッドセーフにするためのロックを追加しました。
- ツリーのオブジェクトを再ロードするためのAPIを追加しました。
- 適切なinheritence取り扱いのために<u>init</u>関数を修正しました。
- 特定のECの中のコンポーネントの状態を得るための新しいAPIを追加しました。
- 特定のECの中のコンポーネントの状態を更新するための新しいAPIを追加しました。


