---
layout: page
title: rtresurrect
---
<!-- Title: rtresurrect -->

## 書式
```
rtresurrect [OPTION ...] [RTSPROFILE_FILE]
```

## 概要
RTSProfileファイルをロードし、実行中のコンポーネントを使ってRTシステム を復元します。コンポーネントの間の接続とコンポーネントのコンフィグレーションパラメータはRTSProfileファイルに記述されたものが反映されます。 RTSProfileファイルに"required"とマークされておらず実行中ではないコンポーネントは無視されます。

ファイル名を指定しない場合、RTSProfile形式のデータをstdinから読込みます。

## オプション(OPTION)
```
 --dry-run　　 復元するために何をするかを表示して終了する(実際には復元しない)
 -x, --xml　　 XMLフォーマットを使う
 -y, --yaml　　YAMLフォーマットを使う
 --version　　 プログラムのバージョン番号を表示して終了する
 -h, --help　　ヘルプを表示して終了する
 -v, --verbose 冗長な情報を出力する [デフォルト： False]
```

## 返り値
成功の場合はゼロを返します。失敗の場合はゼロではない値を返します。

デバッグ情報とエラーはstderrに出力されます。

## 例
- sys.rtsysというファイルを用いRTシステムを復元します。
```
 $ rtresurrect sys.rtsys
```

- sys.rtsys というファイルを用いて復元処理をする場合に何がなされるかを表示します。(実際の復元処理は行われません。)
```
 $ rtresurrect sys.rtsys --dry-run
```


