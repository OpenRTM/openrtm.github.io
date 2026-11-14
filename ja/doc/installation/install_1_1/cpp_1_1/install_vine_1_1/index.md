---
layout: page
title: vine linuxへのインストール
---

<!-- Title: Vine Linuxへのインストール -->
#contents
<div align="right"><a href="vine_logo.png"><img src="vine_logo.png" width="15%;" align="right"></a></div>

C++版 OpenRTM-aist は Vine Linux で利用可能な RPM パッケージが提供されています。
対応している Vine Linux のバージョンは、ダウンロードページから確認できます。
Vine Linux への対応およびそのバージョンは、予告なしに変更または停止されることがありますので、予めご了承ください。

Vine Linux へのインストールの方法には大きく分けて以下の二種類のインストール方法があります。

- openrtm.org が提供する一括インストールスクリプトを使用
- apt-get や synaptic パッケージマネージャを使用


## Vine Linux 一括インストール・スクリプト

openrtm.org が提供するインストール・スクリプト **pkg_install[バージョン番号]_vine.sh** をダウンロードページからダウンロードし、root 権限で実行します。
このスクリプトは、必要なパッケージを順次 apt-get でインストールしていきます。

- [パッケージインストールスクリプト](http://www.openrtm.org/pub/OpenRTM-aist/cxx/install_scripts/)

OpenRTM-aist を開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。
初めて OpenRTM-aist をインストールしてみる方にお勧めします。
ただし、OpenRTM-aist 関係のすべてのパッケージをインストールするので、必要ないものもインストールされる可能性があります。
より詳しくわかっている人は、手動でインストールした方がよいでしょう。
以下、一括インストールスクリプトを使用したインストールの手順です。

```
 > wget [pkg_installXXX.sh のダウンロードURL]
 > su
 # sh pkg_install1XX_vine.sh
 //途中、いくつかの質問をたずねられるので、''y'' あるいは ''Y'' を入力しながら完了させる。
```

## apt-get を使う方法

### sources.list の修正

openrtm.org では apt-get から利用可能なパッケージリポジトリを提供しています。
ただし、デフォルトのパッケージリポジトリには含まれていませんので、apt-get の設定を変更する必要があります。
まず、**/etc/apt/sources.list** の末尾に次の一文を追記します。このとき root 権限が必要ですので注意してください。

```
 rpm http://www.openrtm.org/pub/Linux/Vine/apt x.x/$(ARCH) main
```

ここで、**x.x** の部分はバージョン番号です。例えば、**Vine5.0** なら
**x.x** を **5.0** と置き換えます。

```
 rpm http://www.openrtm.org/pub/Linux/Vine/apt 5.0/$(ARCH) main
```

sources.list を書き変えたら、次の手順でインストールを行います。

```
 > su
 # apt-get update
 # apt-get install gcc-c++ python
 # apt-get install omniORB omniORB-devel omniORB-servers omniORB-doc
 # apt-get install e2fsprogs e2fsprogs-devel
 # apt-get install OpenRTM-aist OpenRTM-aist-devel OpenRTM-aist-doc OpenRTM-aist-example
```

途中、いくつかの質問を尋ねられるので、**y** あるいは **Y** を入力して完了させます。apt-get は 現在は synaptic コマンドで置き換えることが推奨されています。

### インストールの確認

インストールの確認を以下のようにして行います。

```
 # rpm -q OpenRTM-aist
 OpenRTM-aist-1.0.0-0.vl50
```

## パッケージの詳細

### OpenRTM-aist
openrtm-aist にはランタイムライブラリとコマンド群が含まれています。

- サンプル設定ファイル
```
 /etc/rtc.conf.sample
```

- ライブラリ
```
 /usr/lib/libRTC-1.0.0.so.0
 /usr/lib/libRTC-1.0.0.so.0.0.4
 /usr/lib/libRTC.a
 /usr/lib/libRTC.la
 /usr/lib/libRTC.so
 /usr/lib/libcoil.a
 /usr/lib/libcoil.la
 /usr/lib/libcoil.so
 /usr/lib/libcoil.so.0
 /usr/lib/libcoil.so.0.0.0
```

### OpenRTM-aist-devel
openrtm-aist-dev には、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/coil-config
 /usr/bin/rtc-template
 /usr/bin/rtcd
 /usr/bin/rtcprof
 /usr/bin/rtm-config
 /usr/bin/rtm-naming
 /usr/bin/rtm-skelwrapper
```

- ヘッダ
```
 /usr/include/coil/Allocator.h
 /usr/include/coil/Async.h
 中略
 /usr/include/coil/memory.h
 /usr/include/coil/stringutil.h
 中略
 /usr/include/rtm/BufferBase.h
 /usr/include/rtm/BufferStatus.h
 中略
 /usr/include/rtm/Typename.h
 /usr/include/rtm/config_rtc.h
```

- IDL およびスタブ・スケルトン
```
 /usr/include/rtm/idl/BasicDataType.hh
 /usr/include/rtm/idl/BasicDataType.idl
 中略
 /usr/include/rtm/idl/device_interfaces/RFID.idl
 /usr/include/rtm/idl/device_interfaces/Ranger.idl
```

- ライブラリ
```
 /usr/lib/OpenRTM-aist/py_helper/README_gen.py
 /usr/lib/OpenRTM-aist/py_helper/README_gen.pyc
 中略
 /usr/lib/OpenRTM-aist/py_helper/yat.pyc
 /usr/lib/OpenRTM-aist/py_helper/yat.pyo
 /usr/lib/pkgconfig/libcoil.pc
 /usr/lib/pkgconfig/openrtm-aist.pc
```


### OpenRTM-aist-doc
openrtm-aist-doc には、日本語と英語のクラスリファレンス、IDL インターフェース定義リファレンスが含まれています。

- クラスリファレンス
```
 /usr/share/OpenRTM-aist/docs/ClassReference/html/ConnectorBase_8h-source.html
 /usr/share/OpenRTM-aist/docs/ClassReference/html/RTC_8h.html
 中略
 /usr/share/OpenRTM-aist/docs/ClassReference/html/FactoryInit_8h-source.html
```

- IDL リファレンス
```
 /usr/share/OpenRTM-aist/docs/IDLReference/html/BasicDataType_8idl-source.html
 中略
 /usr/share/OpenRTM-aist/docs/IDLReference/html/interfaceOpenRTM_1_1InPortCdr-members.html
```

- クラスリファレンス(英語)
```
 /usr/share/OpenRTM-aist/docs/ClassReference-en/html/ConnectorBase_8h-source.html
 /usr/share/OpenRTM-aist/docs/ClassReference-en/html/RTC_8h.html
 中略
 /usr/share/OpenRTM-aist/docs/ClassReference-en/html/FactoryInit_8h-source.html
```

- IDL リファレンス(英語)
```
 /usr/share/OpenRTM-aist/docs/IDLReference-en/html/BasicDataType_8idl-source.html
 /usr/share/OpenRTM-aist/docs/IDLReference-en/html/structRTC_1_1FsmProfile.html
 中略
 /usr/share/OpenRTM-aist/docs/IDLReference-en/html/interfaceOpenRTM_1_1InPortCdr-members.html
```

### OpenRTM-aist-example
openrtm-aist-example にはスタンドアロン RTC、ローダブル RTC それぞれのサンプルと、サンプル RTC のソースが含まれています。

- サンプル(スタンドアロン RTC)
```
 /usr/share/OpenRTM-aist/examples/ConsoleOutComp
 /usr/share/OpenRTM-aist/examples/ConsoleInComp
 中略
```

- サンプル(ソース)
```
 /usr/share/OpenRTM-aist/examples/src/Composite/README.Motor
 /usr/share/OpenRTM-aist/examples/src/Composite/Makefile.Sensor
 /usr/share/OpenRTM-aist/examples/src/Composite/Motor.cpp
 中略
 /usr/share/OpenRTM-aist/examples/src/SimpleService/Makefile.MyServiceProvider
 /usr/share/OpenRTM-aist/examples/src/SimpleService/rtc.conf
```

- サンプル(ローダブルRTC)
```
 /usr/share/OpenRTM-aist/examples/rtcs/MyServiceConsumer.so.0.0.0
 /usr/share/OpenRTM-aist/examples/rtcs/SeqIn.so.0.0.0
 中略
 /usr/share/OpenRTM-aist/examples/rtcs/ConfigSample.so.0.0.0
 /usr/share/OpenRTM-aist/examples/rtcs/ConsoleOut.so.0.0.0
```

