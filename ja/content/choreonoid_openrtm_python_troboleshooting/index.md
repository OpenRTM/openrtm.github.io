---
layout: page
title: "choreonoid用openrtm連携プラグイン python版 トラブルシューティング"
---
#contents

## Choreonoidが起動しない
以下の原因が考えられます。

### Pythonの問題

まずPython 2.7の**64bit版**がインストールされていることを確認してください。

- [Python 2.7.14](https://www.python.org/downloads/release/python-2714/)

それでも起動しない場合は、**PYTHONHOME**をPythonインストールディレクトリに設定してください。

```
 set PYTHONHOME=C:\python27
```

これで動かない場合は下のコメント欄でお知らせください。


### PCの対応しているOpenGLバージョンの問題

Choreonoid内部のライブラリの問題でOpenGL 1.1にしか対応していないPCでは起動できません。
以下のサイトで**OpenGLバージョンチェックプログラム**を入手して確認してください。

- [http://skomo.o.oo7.jp/f53/hp53_9.htm](http://skomo.o.oo7.jp/f53/hp53_9.htm)



## OpenRTMプラグインがロードできない

現在、調査中です。



## どのプラグインもロードできない

パスに日本語が含まれているとロードできません。

これはChoreonoid自体の問題なので、こちらでは対処しません。

## RTCEditorアイテム追加時にプロセスが落ちる

この問題についても調査中です。



