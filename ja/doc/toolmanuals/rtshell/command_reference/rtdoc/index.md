---
layout: page
title: rtdoc
---

<!-- Title: rtdoc -->

## 書式
```
 rtdoc [OPTION ...] PATH
```

## 注意
本セクションでは本Webサイトのシステムの都合上連続するアンダースコアがうまく記述できないところがあるため、そこでは"_ _"と間に空白をいれた形で表記しますが、これは"__"を意味しますので、置き換えてお読みください。

## 概要
RTコンポーネントの埋め込みドキュメンテーションを表示します。

あるRTコンポーネントはドキュメントを埋込むことができ、隠しコンフィグレーションセットとして実装されています。このコマンドでその埋め込みドキュメンテーションを複数のフォーマットで表示できます。対応フォーマットはreStructuredText、HTML、LaTex(PDF化を考慮して)です。

## オプション
```
 -f FORMAT、--format=FORMAT
 　　　　　　フォーマットを選択します。rst、htmlおよびlatexから選択してください。
 -g、--graph 　コンポーネントのグラフを表示させます。
 --version　　　プログラムのバージョン番号を表示して終了する
 -h、--help　 　ヘルプを表示して終了する
 -v、--verbose より詳細な情報を出力する
```

### RTコンポーネントのドキュメンテーション
このコマンドによって取り扱われる埋め込みドキュメントは、_ _doc_ _コンフィギュレーションセットに記述します。このセット内のパラメータ(隠しでないもの)はセクションとして追加されます。

一般的なセクションは:

- **intro**
  - コンポーネントの紹介。その動作目的などの概要を記載します。(Title:  Introduction.)
- **reqs**
  - コンポーネントを使用するための、事前にインストールされていなければいけないソフトウエアのような事前準備が必要yな事項を記載します。(Title:  Pre-requisites.)
- **install**
  - コンポーネントのインストール方法を記載します。(Title:  Installation.)
- **usage**
  - コンポーネントを起動したり使用したりする方法を記載します。 (Title:  Usage.)
- **misc**
  - コンポーネントを使用するにあたって知っておいたほうがよい他の重要な情報を記載します。(Title:  Miscellaneous.)
- **changelog**
  - |コンポーネントの変更履歴を記載します。(Title:  Changelog.)

また、コンポーネントがポートやコンフィギュレーションを持っていれば、そのデフォルトのコンフィギュレーションセットの中にportセクションとconfigセクションが自動的に作られます。_ _doc_ _セット内の他のセクションはすべてこの埋め込みドキュメントとして追加されます。

また、以下の３つのパラメータを追加の情報としてドキュメントの先頭部分に追加できます。

- _ _license_ _
  - GPLやBSDなどのライセンス情報
- _ _contact_ _
  - 作者のemailアドレスなどの連絡先情報
- _ _url_ _
  - コンポーネントに関するホームページのURL

パラメータはコンポーネントソース内にもコンポーネント起動時に読込まれるコンフィギュレーション・ファイル内で記述できます。ソース内に埋め込まれたドキュメントは、使用法や連絡先の短い情報以外は、コンポーネントのバイナリ・データ・サイズを消費するためコンフィギュレーション・ファイルに記載する方法を推奨します。

ソースコード内では例えば以下のように記述します:

```
 'conf.__doc__.__license__', 'LGPL',
 'conf.__doc__.__contact__', 'a@example.com',
 'conf.__doc__.__url__', 'http://www.openrtm.org',
 'conf.__doc__.intro', 'This is the introduction.',
 'conf.__doc__.reqs', 'This component requires nothing.',
 'conf.__doc__.install', 'Type "make install"',
 'conf.__doc__.usage', 'Run comp_standalone.',
 'conf.__doc__.misc', 'Extra information.',
 'conf.__doc__.changelog', 'No changes.',
 'conf.__doc__.Another', 'A non-standard section.',
```

デフォルトではセクションは以下の順番でインクルードされます。
```
 intro, reqs, usage, ports, config, misc, changelog, [other sections]
```

この順番は＿ ＿doc_ _セット内の_ _order_ _パラメータで変更でき、ドキュメントのセクション中の各パラメータの名をコンマで分離したリストで指定し、例えば以下のようににします:
```
 'conf.__doc__.__order__', 'intro,ports,config,reqs,Another'
```

そこで指定されなかったセクションは、指定されたセクションの後になり、それぞれの順番は定義されません。

ポートへのドキュメントはポートのプロパティーの記述を追加し、例えば以下のようにします:
```
 self._inport.addProperty('description', 'This port receives stuff.')
```

コンフィグレーション・パラメータのドキュメントは、_ _description_ _セットでパラメータを設定し、例えば以下のようにします:,
```
 'conf.default.param', '0',
 'conf.__description__.param', 'A test parameter.',
```

## パス
rtshellはパスでRTCツリーのオブジェクトを示します。ネームサーバーとネームコンテクストはディレクトリ名として指定され、マネージャとRTコンポーネントはファイル名として指定されます。コマンドに渡したパスはrtshellの現在の作業ディレクトリを元に指定されます。(相対パスの場合)。rtshellの現在の作業ディレクトリはRTCSH_CWDという環境変数に保存されて、rtcwdというコマンドで変更できます。(現時点でrtcwdコマンドはLinux環境では動作していません)

利用できるパスはコマンド実行時に参照しているネームサーバーによって変わります。ネームサーバーが実行されているホスト名はRTCTREE_NAMESERVERSという環境変数で指定できます。また、直接ルート直下のパスとして/<ホスト名>/....のような形でネームサーバーが実行されているホストを指定できます。

例えば、/localhost/comp0.rtcはlocalhostにあるネームサーバーに登録されたcomp0.rtcというRTコンポーネントを示します。/localhost/manager/comp0.rtcはlocalhostにあるネームサーバーの下のmanagerというディレクトリに登録されたcomp0.rtcというRTコンポーネントを示します。./comp0.rtcは現在の作業ディレクトリにあるcomp0.rtcというRTコンポーネントを示します。

RTコンポーネントのポートを示す場合、パスの後にコロン（「:」）で区切って指定します。例えば、/localhost/comp0.rtc:dataはcomp0.rtcというRTコンポーネントのdataというポートを意味します。

新しいポートを作れるコマンドもあり、この場合、オプションでそれらをパスに追加できます。使えるオプションは作られるポートの名前とフォーマッタです。指定方法は以下の通りです:

```
 <path>:<port>.<new_port_name>#<formatter>
```

### 例:
```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff#a_printer
```

新たに作られるポートの名前はstuffで、データはa_printerという関数(フォーマッター)でターミナルに表示するように指定しています。(a_printerの関数はPythonが利用可能な場所に存在する必要があります。普通はユーザーがモジュールで提供します)。作られたポートはcomp0.rtcのinputというポートに接続されます。

`<new_port_name>`という部分は必須ではありません。指定しない場合は"."も指定しないでください。例:

```
 /localhost/blurg.host_cxt/comp0.rtc:input#a_printer
```

`<formatter>`という部分は必須ではありません。書いていない場合は"."も指定しないでください。例:

```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff
```

## 環境変数
- **RTCTREE_ORB_ARGS**
  - ORBを作る時に渡す変数です。セミコロンで区切ります。必須ではありません。
- **RTCTREE_NAMESERVERS**
  - RTCツリーを作る時に参照するネームサーバーのアドレスです。アドレスをセミコロンで区切ります。リストされたアドレスはRTCツリーに追加されrtshellで参照できるようになります。ルート下のディレクトリ名としてパスで指定することもできるので必須ではありません。
- **RTSH_CWD**
  - rtshellの現在のワーキングディレクトリ。rtshellが自動的に設定します。設定しないでください。

一般的な利用ではユーザーが設定する変数はRTCTREE_NAMESERVERSのみです。よく使うネームサーバーを設定しておくと便利です。例えば、Bashシェルの場合、以下のコマンドはlocalhostとポート192.168.0.1:65346およびホストexample.comにあるネームサーバーをrtshellが参照できるようにします。

```
 $ export RTCTREE_NAMESERVERS=localhost;192.168.0.1:65346;example.com
```


## 返り値
成功の場合はゼロを返します。失敗の場合はゼロではない値を返します。

デバッグ情報とエラーはstderrに出力されます。

## 例
- ConsoleOut0.rtcのドキュメンテーションを標準出力に表示します。
```
 $ rtdoc /localhost/ConsoleOut0.rtc
```

- ConsoleOut0.rtcのドキュメンテーションをdoc.htmlというファイルに保存します。
```
 $ rtdoc /localhost/ConsoleOut0.rtc > doc.html
```

- ConsoleOut0.rtcのドキュメンテーションをreStructuredTextフォーマットで表示します。
```
 $ rtdoc /localhost/ConsoleOut0.rtc -f rst
```

- ConsoleOut0.rtcのドキュメンテーションをrubberツールによってPDF形式で保存します。
```
 $ rtdoc /localhost/ConsoleOut0.rtc -f latex > doc.tex && rubber -d doc.tex
```


