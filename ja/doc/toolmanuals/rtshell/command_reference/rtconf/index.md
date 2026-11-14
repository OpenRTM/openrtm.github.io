---
layout: page
title: rtconf
---

<!-- Title: rtconf -->

## 書式
```
 rtconf PATH [OPTION...] [list|set|get|act] [ARGS]
```

## 概要
コンフィグレーションパラメータとコンフィギュレーションセットを表示、設定します。list|set|get|actは、指定されていない場合はlistが指定されているものとします。

- **list**
  - list コマンドはコンフィグレーションセットとパラメータを表示します。隠しコンフィグレーションセット（`__`で始まるセット名のコンフィギュレーションセット）は表示しません。
- **set PARAMETER_NAME VALUE**
  - コンフィグレーションパラメータの値を設定します。パラメータ名と新しい値を指定してください。--set (-s)オプションが指定されていない場合、現在のアクティブなコンフィギュレーションセットのパラメータが設定されます。
- **get PARAMETER_NAME**
  - パラメータの値を表示します。パラメータ名を指定してください。--set (-s)オプションが指定されていない場合、現在のアクティブなコンフィギュレーションセット内のパラメータの値を表示します。
- **act**
  - --set=SET_NAME (-s SET_NAME)で指定したコンフィギュレーションセットをアクティブにします。

### オプション(OPTION)
```
 -a、--all　　　隠しコンフィギュレーションセットを無視しない。隠しコンフィギュレーションセットを編集したい方はこのオプションを指定してください。
 -l　　　　　　 詳しい情報を表示します。
 -s <set name>、--set=SET_NAME
 　　　　　　コンフィギュレーションセットを選択する。指定されていない場合、現在アクティブになっているセットを使います。
 --version	　　プログラムのバージョン番号を表示します。
 -h、--help　　ヘルプを表示します。
 -v、--verbose より詳細な情報を出力します。
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

新たに作られるポートの名前はstuffで、データはa_printerという関数(フォーマッター)でターミナルに表示するように指定しています。(a_printerの関数はPythonが利用可能な場所に存在する必要があります。普通はユーザーーがモジュールで提供します)。作られたポートはcomp0.rtcのinputというポートに接続されます。

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
- ConfigSample0.rtcのコンフィギュレーションセットを表示します。
```
 $ rtconf /localhost/ConfigSample0.rtc list
 +default*
 +mode0
 +mode1
```

- ConfigSample0.rtcのコンフィギュレーションセットとパラメータを表示します。
```
 $ rtconf /localhost/ConfigSample0.rtc -l list
  -default*
  double_param0  0.99
  double_param1  -0.99
```

- 隠しコンフィギュレーションセットを含めてConfigSample0.rtc のセットを表示します。
```
 $ rtconf /localhost/ConfigSample0.rtc -a list
 +__constraints__
 +__widget__
 +default*
 +mode0
 +mode1
```

- ConfigSample0.rtcのdefaultセットのパラメータを表示します。
```
 $ rtconf /localhost/ConfigSample0.rtc -l -s default list
 -__constraints__
  double_param0  0<=x<=100
  double_param1
  ...
```

- 現在アクティブなコンフィギュレーションセットのint_param0パラメータの値を42に設定します。
```
 $ rtconf /localhost/ConfigSample0.rtc set int_param0 42
```

- mode0というコンフィギュレーションセットのint_param0を42に設定します。
```
 $ rtconf /localhost/ConfigSample0.rtc -s mode0 set int_param0 42
```

- 現在アクティブなコンフィギュレーションセットのint_param0パラメータの値を表示します。
```
 $ rtconf /localhost/ConfigSample0.rtc get int_param0
 0
```

- mode0というコンフィギュレーションセットのint_param0パラメータの値を表示します。
```
 $ rtconf /localhost/ConfigSample0.rtc -s mode0 get int_param0
 12345
```

- コンフィギュレーションセットをmode1というコンフィギュレーションセットにします。
```
 $ rtconf /localhost/ConfigSample0.rtc act mode1
```

- コンフィギュレーションセットを_ _widget_ _というセットにします。
```
 $ rtconf /localhost/ConfigSample0.rtc -a act __widget__
```

