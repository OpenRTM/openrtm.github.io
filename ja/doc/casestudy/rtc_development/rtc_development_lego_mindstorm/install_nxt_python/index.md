---
layout: page
title: nxt python のインストール
---

<!-- Title: NXT Python のインストール -->
#contents


# NXT Python のインストール


NXT RTC を作成する前に、Python から Bluetooth を使用するためのモジュール PyBlues と、NXT を制御するためのモジュール NXT Python をインストールします。
- [PyBlues](http://code.google.com/p/pybluez/)
  - [PyBluez-0.18.win32-py2.4](http://pybluez.googlecode.com/files/PyBluez-0.18.win32-py2.4.exe)
  - [PyBluez-0.18.win32-py2.5](http://pybluez.googlecode.com/files/PyBluez-0.18.win32-py2.5.exe)
  - [PyBluez-0.18.win32-py2.6](http://pybluez.googlecode.com/files/PyBluez-0.18.win32-py2.6.exe)
  - [PyBluez-0.18.tar](http://pybluez.googlecode.com/files/PyBluez-0.18.tar.gz)
- [NXT Python](http://home.comcast.net/`dplau/nxt_python/)`
  - [nxt_python-0.7.zip](http://home.comcast.net/`dplau/nxt_python/download/nxt_python-0.7.zip)`
  - [nxt_python-0.7.tar.gz](http://home.comcast.net/`dplau/nxt_python/download/nxt_python-0.7.tar.gz)`


## PyBlues のインストール
上記リンクからWindows用 のインストーラをダウンロードします。
ダウンロードした実行ファイルを実行すればインストールは完了です。

## NXT Python のインストール
上記リンクから zip ファイルをダウンロードします。
NXT Python は setup.py スクリプトを使用してインストールします。
- .pyに関連付けがされている場合
```
 setup.py install
```
- 関連づけされていない場合:
```
 c:\Python24\python setup.py install
```

```
 Microsoft Windows XP [Version 5.1.2600]
 (C) Copyright 1985-2001 Microsoft Corp.
 
 C:\tmp\nxt_python-0.7>setup.py install
 running install
 running build
 running build_py
 ...
 copying build\scripts-2.4\nxt_filer -> c:\python24\Scripts
 copying build\scripts-2.4\nxt_push -> c:\python24\Scripts
 copying build\scripts-2.4\nxt_test -> c:\python24\Scripts
 
 C:\tmp\nxt_python-0.7>
```

## NXT Python のテスト
NXT を ON にしてPCに接続されている状態で、example 以下のサンプルを実行し、NXT Python から NXT が制御できるかどうか確認します。

example ディレクトリーには以下のサンプルがあります。

- latency.py: センサー読出しのレイテンシを計測する。
- mary.py: NXT のサウンド機能で「メリーさんの羊」を演奏する
- message_test.py: インテリジェントブロックの液晶画面にメッセージを表示する
- spin.py: PortB, PortC のモーターを動かしスピンさせる
- test_sensors.py: 全センサーの値を表示する

これらのテストを実行する際には、それぞれのサンプルが使用するモーター、センサーなどが接続された状態で実行しなければなりません。&aname(miyamoto);


