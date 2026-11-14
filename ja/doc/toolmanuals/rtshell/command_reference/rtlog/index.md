---
layout: page
title: rtlog
---

<!-- Title: rtlog -->

## 書式
```
rtlog [OPTION ...] PATH:PORT [PATH:PORT ...]
```

## 概要
コンポーネントがデータポートで送るデータをログファイルに保存したり、ログファイルに記録したデータをコンポーネントに送ったり(再生)します。複数のポートでも記録が可能です。ログされたコンポーネントの出力データを再現するためにログファイルを再生しコンポーネントに送ることもできます。

ログの複数データストリームから再生されたストリームを選択できます。例えばログに複数のレーザセンサーからのデータが保存されてる場合、その中から特定の1つのみのレーザセンサー・データを再生できます。再生はログの始まりだけではなくて途中から途中までをという形や、再生レートを変えたりできます。また出力されたデータのタイムスタンプを編集できます。

デフォルトはログの保存です。コマンドで指定したポートはすべてOutPortである必要があります。再生モードの場合は、ポートはすべてInPortの必要があり、また、ログされたデータの型にポートが受付可能な型は一致している必要があります。

ログで記録されるそれぞれのポートは一つのデータストリームを作ります。再生時、このデータストリームはそれぞれ複数のInPortに送ることができます。データストリームは名前で区別されます。名前はコマンドラインで指定できますが、指定されなかった場合は、デフォルトの名前が自動的に使われます。

ログツールから目的のポートまでの接続はデフォルトのプロパティーで作られます。

## オプション
```
 -a、--absolute-times
 　　　　　　ログデータからのタイムスタンプは記録されたままの値を送るようにします。
 　　　　　　指定しない場合、タイムスタンプは現在の時刻でオフセットされます。
 -d、--display-info
 　　　　　　ログの情報を表示して終了します。
 -e END、--end=END
 　　　　　　記録や再生を止めるタイムスタンプまたはインデクスを指定します。再生の
 　　　　　　場合は記録されているログ中の先頭と最後のデータの間の数値を指定してく
 　　　　　　ださい。-1を指定した場合は強制終了されるまで記録するか、ログの最後ま
 　　　　　　で再生します。インデクスで指定したい場合は--indexも指定してください。
 -f FILENAME、--filename=FILENAME
 　　　　　　ログファイルの名前を指定します。指定しない場合、現在の時刻をファイル名
 　　　　　　とします。再生の時は必須です。
 --path=PATHS	
 　　　　　　モジュールのサーチパスを指定します。PythonのPYTHONPATH変数に追加されます。
 -i、--index
 　　　　　　--startオプションや--endオプションで指定する値をタイムスタンプではなく
 　　　　　　インデクスとして扱うようにします。
 -l LOGGER、--logger=LOGGER
 　　　　　　ログ種類を選択します。デフォルトはSimplePickle(simpkl)です。テキストログ
 　　　　　　(text)を使うこともできます。テキストログは再生できません。
 -m MODULES、--mod=MODULES
 　　　　　　ImportするPythonモジュールを指定します。データを取扱うために必要な
 　　　　　　モジュールが自動的にロードされていない場合、このオプションで指定してくだ
 　　　　　　さい。モジュールとそのモジュールの__POAのモジュールもImportします。
 -n、--ignore-times
 　　　　　　(再生のみ)ログに記録されたタイムスタンプを無視して一定の周期でログデータ
 　　　　　　を再生します。周期を変える場合、--exec-rateを使ってください。
 -p、--play　再生モードにします。
 -r RATE、--rate=RATE
 　　　　　　(再生のみ)再生速度の倍数を指定します。
 -s START、--start=START
 　　　　　　(再生のみ)再生を始めるタイムスタンプまたはインデクスを指定します。ログの
 　　　　　　最初と最後のデータの間にすることは必須です。インデクスで指定する場合、
 　　　　　　--indexも指定してください。
 -t TIMEOUT、--timeout=TIMEOU
 　　　　　　記録または再生のタイムアウト時間を指定します。このオプションを使う場合、
 　　　　　　--startと--endを使うことはできません。
 -x EXEC_RATE、--exec-rate=EXEC_RATE
 　　　　　　コンポーネントの実行レートを指定します。単位はヘルツです。
 --version　 プログラムのバージョン番号を表示して終了する
 -h、--help　ヘルプを表示して終了する
 -v、--verbose より詳細な情報を出力します。
```

## パス
rtshellはパスでRTCツリーのオブジェクトを示します。ネームサーバーとネームコンテクストはディレクトリ名として指定され、マネージャとRTコンポーネントはファイル名として指定されます。コマンドに渡したパスはrtshellの現在の作業ディレクトリを元に指定されます。(相対パスの場合)。rtshellの現在の作業ディレクトリはRTCSH_CWDという環境変数に保存されて、rtcwdというコマンドで変更できます。(現時点でrtcwdコマンドはLinux環境では動作していません)

利用できるパスはコマンド実行時に参照しているネームサーバーによって変わります。ネームサーバーが実行されているホスト名はRTCTREE_NAMESERVERSという環境変数で指定できます。また、直接ルート直下のパスとして/<ホスト名>/....のような形でネームサーバーが実行されているホストを指定できます。

例えば、/localhost/comp0.rtcはlocalhostにあるネームサーバーに登録されたcomp0.rtcというRTコンポーネントを示します。/localhost/manager/comp0.rtcはlocalhostにあるネームサーバーの下のmanagerというディレクトリに登録されたcomp0.rtcというRTコンポーネントを示します。./comp0.rtcは現在の作業ディレクトリにあるcomp0.rtcというRTコンポーネントを示します。

RTコンポーネントのポートを示す場合、パスの後にコロン(「:」)で区切って指定します。例えば、/localhost/comp0.rtc:dataはcomp0.rtcというRTコンポーネントのdataというポートを意味します。

新しいポートを作れるコマンドもあり、この場合、オプションでそれらをパスに追加できます。使えるオプションは作られるポートの名前とフォーマッタです。指定方法は以下の通りです:

```
 <path>:<port>.<new_port_name>#<formatter>
```

### 例:
```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff#a_printer
```

新たに作られるポートの名前はstuffで、データはa_printerという関数(フォーマッター)でターミナルに表示するように指定しています。(a_printerの関数はPythonが利用可能な場所に存在する必要があります。普通はユーザーがモジュールで提供します)。作られたポートはcomp0.rtcのinputというポートに接続されます。これはストリーム名を指定するのにもつかわれます。

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
- ConsoleIn0.rtcコンポーネントのoutポートからのデータをファイルlog.rtlogに記録します。データストリームはnumbersという名前がつけられます。
```
 $ rtlog -f log.rtlog /localhost/ConsoleIn0.rtc:out.numbers
```

- ログファイルlog.rtlogからnumbersというデータストリームを再生しConsoleOut0.rtc:inポートへ送ります。
```
 $ rtlog -f log.rtlog -p /localhost/ConsoleOut0.rtc:in.numbers
```

- ログの情報を表示します。ログの開始時間、終了時間、データストリームなどが含まれています。
```
 $ rtlog -f log.rtlog -d
```

- コンピューターの時計が”1292489690”になるまで記録し、終了します。
```
 $ rtlog -f log.rtlog -e 1292489690 /localhost/ConsoleIn0.rtc:out.numbers
```

- 10個のデータを記録して終了します。
```
 $ rtlog -f log.rtlog -e 10 -i /localhost/ConsoleIn0.rtc:out.numbers
```

- 10秒間記録して終了します。
```
 $ rtlog -f log.rtlog -t 10 /localhost/ConsoleIn0.rtc:out.numbers
```

- "1292489690"のタイムスタンプから再生を始めます。
```
 $ rtlog -f log.rtlog -p -s 1292489690 /localhost/ConsoleOut0.rtc:in.numbers
```

- 先頭のデータから”1292489700”のタイムスタンプまで再生します。
```
 $ rtlog -f log.rtlog -p -e 1292489700 /localhost/ConsoleOut0.rtc:in.numbers
```

- "1292489690"のタイムスタンプから"1292489700"のタイムスタンプまで再生します.(大体10秒のデータ。)
```
 $ rtlog -f log.rtlog -p -s 1292489690 -e 1292489700 /localhost/ConsoleOut0.rtc:in.numbers
```

- ５番目のデータから再生を始めます。
```
 $ rtlog -f log.rtlog -p -s 5 -i /localhost/ConsoleOut0.rtc:in.numbers
```

- 最初のデータから10番目のデータまで再生します。
```
 $ rtlog -f log.rtlog -p -e 10 /localhost/ConsoleOut0.rtc:in.numbers
```

- 5番目のデータから10番目のデータまで再生します。
```
 $ rtlog -f log.rtlog -p -s 5 -e 10 /localhost/ConsoleOut0.rtc:in.numbers
```

- 先頭から10秒間のデータを再生します。
```
 $ rtlog -f log.rtlog -p -t 10 /localhost/ConsoleOut0.rtc:in.numbers
```

- ログを5倍速で再生します。
```
 $ rtlog -f log.rtlog -p -r 5 /localhost/ConsoleOut0.rtc:in.numbers
```

- ログを0.2倍速で再生します。
```
 $ rtlog -f log.rtlog -p -r 0.2 /localhost/ConsoleOut0.rtc:in.numbers
```

- 1秒に1個づつ再生して、最終的に5個のデータを再生します。
```
 $ rtlog -f log.rtlog -p -n 5 -x 1 /localhost/ConsoleOut0.rtc:in.numbers
```

- 一つのファイルに三つのデータストリームを記録します。ストリームの名前はsensorとctrlとmotorです。
```
 $ rtlog -f log.rtlog /localhost/Sensor0.rtc:out.sensor /localhost/Controller0.rtc:out.ctrl /localhost/Motor0.rtc:out.motor
```

- 一つのログから二つのデータストリームを再生し、それぞれ別々のポートへ送ります。
```
 $ rtlog -f log.rtlog -p /localhost/Sensor0.rtc:in.motor /localhost/Motor0.rtc:in.ctrl
```

- 一つのログから二つのデータストリームを再生し同じポートへ送ります。
```
 $ rtlog -f log.rtlog -p /localhost/Controller0.rtc:in.sensor /localhost/Controller0.rtc:in.motor
```

- ログから一つのデータストリームを再生し複数のポートへ送ります。
```
 $ rtlog -f log.rtlog -p /localhost/Sensor0.rtc:in.motor /localhost/Controller0.rtc:in.motor
```




