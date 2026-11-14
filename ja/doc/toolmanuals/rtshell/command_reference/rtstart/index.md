---
layout: page
title: rtstart
---

<!-- Title: rtstart -->

## 書式
```
rtstart [OPTION ...] [RTSPROFILE_FILE]
```

## 概要
指定されたRTSProfileファイルの情報を元にすべてのコンポーネントをアクティブ化することによりRTシステムを起動します。コンポーネントはRTSProfileファイル内で指定された順番でアクティブ化されます。RTSProfileに”required"とマークされていないコンポ―ネントは無視されます。

ファイル名を指定されなかった場合、RTSProfile形式の情報でstdinから読込みます。

## オプション(OPTION)
```
 --dry-run　　 実行する内容を表示する（実際には起動は行われない）
 -x、--xml　　 XMLフォーマットを使う
 -y、--yaml　　YAMLフォーマットを使う
 --version　　 プログラムのバージョン番号を表示して終了する
 -h、--help　　ヘルプを表示して終了する
 -v、--verbose より詳細な情報を出力します
```

## ステート変更の実行シーケンス
RTSProfileファイルでは、RTシステムのコンポーネントの開始/停止の順番を指定するこが可能です。コンポーネント間で依存関係がある場合(例えば、あるコンポーネントの開始前に、別のコンポーネントの実行を開始する必要がある場合など)に、その順番を指定することが可能です。

rtstartとrtstopはこの情報を利用します。実際のところrtstartはActivationブロックに含まれている情報を利用し、rtstopはDeactivationブロックに記述されている情報を利用します。ここに記載された情報を元にしたコンポーネントのアクティブ化/非アクティブ化処理は全ての処理が完了するかエラーが発生するまで、継続します。

オプション--dry-runが指定された場合、このオプションが指定されなかった場足にどのような処理がなされるかを表示します。実際の処理はなされません。出力は以下のようになります。
```
 {1} Activate /localhost/ConfigSample0.rtc in execution context 0 (Required) 
 {2} [Order 1] Activate /localhost/Motor0.rtc in execution context 0 (Required)
 {4} [Order 3/Wait 5000ms] Activate /localhost/Controller0.rtc in execution context 0 (Required)
 {3} [Order 2/Sync to Motor0, Order 5/Sync to Controller0] Activate /localhost/Sensor0.rtc in execution context 0 (Required)
 {5} [Order 4/After ConfigSample0's action] Activate /localhost/ConsoleIn0.rtc in execution context 0 (Required)
```

各ラインの初めの括弧の中の数字は*アクションID*です。これらは実行の時にも表 示され、これによりアクションの簡単な識別が可能です。
その後に続く角括弧で囲まれた部分はその後に続くアクションを実行するにあたって必要な条件が示されていてその中で使われる特定の単語は以下のような意味を持っています:

- **Order**
  - 順番を管理します。RTSProfileのconditionのrts: sequence値で設定可能です。他の前条件がない場合、アクションはこの順番によってなされます。
- **Wait**
  - 指定された時間が経過した後にアクションが実行されます。
- **Sync**
  - 指定されたコンポーネントがターゲット状態になるまで待ち、その後指定のアクションが実行されます。
- **After**
  - Syncと似てます。違いは、アクションが指定の別のコンポーネント上で行われるまで待つということです。言いかえれば、そのアクションは、指定の別コンポーネントが目標状態に達する前でも、そのコンポーネントでアクションが行われれば実行されます。
行のその後の部分はアクションの説明です。

## 返り値
成功の場合はゼロを返します。失敗の場合はゼロではない値を返します。

デバッグ情報とエラーはstderrに出力されます。

# 例
- sys.rtsysというファイルの情報を元にRTシステムを起動します。
```
 $ rtstart sys.rtsys
```

- sys.rtsysというファイルの情報を元にRTシステムを起動するためにどのような処理がなされるかをを表示します。（実際の起動は行われません。）
```
 $ rtstart sys.rtsys --dry-run
```


