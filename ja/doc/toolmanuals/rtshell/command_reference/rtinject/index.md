---
layout: page
title: rtinject
---
<!-- Tilte: rtinject -->

## 書式
```
rtinject [OPTIONS ...] PATH:PORT [PATH:PORT ...]
```

## 概要
値を一つ以上のポートに送ります。デフォルトは一回のみ送ります。複数回や定期的に送ることもできます。

目的のポートにデフォルトの接続を作ります。

## オプション(OPTION)
```
 -c CONST、--const=CONST
 　　　　　　Pythonフォーマットでデータを指定します。POSIX系では「'」でデータ記述文字列を囲みます。
 　　　　　　Windowsでは「”」でデータ記述文字列を囲みます。このオプションが指定されなかった場合は、
 　　　　　　標準入力からデータをデータ記述文字列と見立てて動作します。データ記述文字列中の{time}の
 　　　　　　表記は現在の時刻を意味するものとして取扱われます。
 -m MODULES、--mod=MODULES
 　　　　　　Importするythonモジュールを指定します。値の必要なモジュールが自動的にロード
 　　　　　　されていない場合、このオプションで指定してください。モジュールとそのモジュー
 　　　　　　ルの__POAのモジュールもImportされます。
 -n NUMBER、--number=NUMBER
 　　　　　　データを何回送るかを指定します。-1を設定した場合、強制停止なされるまで送り続けます。
 -p PATHS、--path=PATHS
 　　　　　　モジュールのサーチパス。PythonのPYTHONPATH変数に追加されます。
 -r RATE、--rate=RATE
 　　　　　　頻度を指定します。単位は(回/sec)です。
 -t TIMEOUT、--timeout=TIMEOUT
 　　　　　　タイムアウト時間(コマンドの実行を停止するまでの時間)を秒単位で指定します。このオプ
 　　　　　　ションは --number と一緒に使用で来ません。
 --version　　 プログラムのバージョン番号を表示します。
 -h、--help　　ヘルプを表示します。
 -v、--verbose 冗長な情報を出力します。
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
- stdinからの値をConsoleOut0.rtcのinポートに送ります。
```
 $ rtinject /localhost/ConsoleOut0.rtc:in
```

- 42と現在の時刻をタイムスタンプとconsoleout0.rtcのinポートに送ります。「’」使ってpython形式のデータ指定を囲みます。(Windowsでは「"」を使ってください。)
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -c 'RTC.TimedLong({time}, 42)'
```

- 42をタイムスタンプ1秒としてConsoleOut0.rtcのinポートに送ります。
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -c 'RTC.TimedLong(RTC.Time(1, 0), 42)'
```

- stdinからの値を五回ConsoleOut0.rtcのinポートに送ります。
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -n 5
```

- 42を現在の時刻を元にconsoleout0.rtcのinポートに５回送ります。
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -n 5 -c 'RTC.TimedLong({time}, 42)'
```

- 42と現在の時刻を元に10回/secの頻度でconsoleout0.rtcのinポートに秒間送ります。
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -t 5 -r 10 -c 'RTC.TimedLong({time}, 42)'
```

- MyData.MyVal(84)をMyComp0.rtcのinポートに送ります。クラスはPythonのサーチパス(PYTHONPATH)に存在するモジュールに指定されています。そのモジュールはOMG IDLファイルからジェネレートされました。
```
 $ rtinject /localhost/MyComp0.rtc:in -c 'MyData.MyVal(84)'
```

- MyData.MyVal(84)をMyComp0.rtcのinポートに送ります。クラスはPythonのサーチパス(PYTHONPATH)に存在しないモジュールに指定されています。モジュールのパスは**-p**で指定されます。
```
 $ rtinject /localhost/MyComp0.rtc:in -p /usr/local/mods -c 'MyData.MyVal(84)'
```

- MyData.MyVal(84)をMyComp0.rtcのinポートに送ります。クラスはPythonのサーチパス(PYTHONPATH)に存在するmymodというモジュールを指定します。
```
 $ rtinject /localhost/MyComp0.rtc:in -p /usr/local/mods -m mymod -c 'MyData.MyVal(84)'
```


