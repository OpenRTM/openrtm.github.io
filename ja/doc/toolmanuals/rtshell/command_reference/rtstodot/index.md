---
layout: page
title: rtstodot
---
<!-- Title: -->

## 書式
```
rtstodot [OPTION ...] [RTSPROFILE_FILE]
```

## 概要
GraphvizのdotフォーマットでRTシステムをグラフとして表示します。 ファイルが指定されていない場合RTSProfile形式で情報をstdinから読みます。

## オプション(OPTION)
```
 -x、--xml　　 XMLフォーマットを使います
 -y、--yaml　　YAMLフォーマットを使います
 --version　　 プログラムのバージョン番号を表示します
 -h、--help　　ヘルプを表示します
 -v、--verbose より詳細な情報を出力します
```

## 返り値
成功の場合はゼロを返します。失敗の場合はゼロではない値を返します。

デバッグ情報とエラーはstderrに出力されます。

## 例
- sys.rtsysファイルを元にRTシステムを表示します。
```
 $ rtstodot sys.rtsys | dot -T xlib
```

- sys.rtsysファイルを元にRTシステムを表示してEncapsulated PostScriptフォーマットでsys.epsファイルに保存します。
```
 $ rtstodot sys.rtsys | dot -T eps > sys.eps
```

- 現在実行中のRTシステムを表示します。
```
 $ rtcryo | rtstodot | dot -T xlib
```


