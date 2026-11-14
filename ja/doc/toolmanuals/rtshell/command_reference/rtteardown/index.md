---
layout: page
title: rtteardown
---

<!-- Title: rtteardown -->

## 書式
```
 rtteardown [OPTION ...] [RTSPROFILE_FILE]
```

# 概要
RTSProfileファイルに記述された接続情報を用いて、動作中のRTシステムの接続を削除します。

ファイル名を指定しなかった場合、RTSProfile情報をstdinから読みこみます。

## オプション
```
 --dry-run　　 実行する内容を表示します(実際には削除は行われません)。
 -x、--xml　　 XMLフォーマットを使います。
 -y、--yaml 　 YAMLフォーマットを使います。
 --version　　 プログラムのバージョン番号を表示します。
 -h、--help　　ヘルプを表示します。
 -v、--verbose より詳細な情報を出力します。
```

## 返り値
成功の場合はゼロを返します。失敗の場合はゼロではない値を返します。

デバッグ情報とエラーはstderrに出力されます。

## 例
- sys.rtsysファイルの情報を用いて現在実行中のRTシステムの接続を削除します。
```
 $ rtteardown sys.rtsys
```

- sys.rtsysファイルの情報を用いて現在実行中のRTシステムの接続を削除する場合、どのようなことがなされるかを表示します。(実際には、削除は行われません。)
```
 $ rtteardown sys.rtsys --dry-run
```



