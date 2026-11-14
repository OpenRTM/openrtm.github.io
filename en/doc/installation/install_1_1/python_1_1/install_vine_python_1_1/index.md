---
layout: page
title: vine linuxへのインストール
---
<br>
<a>No English version available.
</a>

init
<!-- Title: Vine Linuxへのインストール -->
#contents

Python 版 OpenRTM-aist は Vine Linux で利用可能な RPM パッケージが提供されています。
対応している Vine Linux のバージョンは、ダウンロードページから確認できます。
Vine Linux への対応およびそのバージョンは、予告なしに変更または停止されることがありますので、予めご了承ください。

Vine Linux へのインストールの方法には大きく分けて以下の二種類のインストール方法があります。

- openrtm.org が提供する一括インストールスクリプトを使用
- apt-get や synaptic パッケージマネージャを使用

## Vine Linux 一括インストール・スクリプト

openrtm.org が提供するインストール・スクリプト **pkg_install_python_vine.sh** をダウンロードページからダウンロードし、root 権限で実行します。
このスクリプトは、必要なパッケージを順次 apt-get でインストールしていきます。

- [パッケージインストールスクリプト]()(No corresponding page available.)

OpenRTM-aist を開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。
初めて OpenRTM-aist をインストールしてみる方にお勧めします。
ただし、OpenRTM-aist 関係のすべてのパッケージをインストールするので、必要ないものもインストールされる可能性があります。
より詳しくわかっている人は、手動でインストールした方がよいでしょう。
以下、一括インストールスクリプトを使用したインストールの手順です。

```
 > wget [pkg_install_python_vine.sh のダウンロード URL ]
 > su
 # sh pkg_install1_python_vine.sh
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

ここで、**x.x** の部分はバージョン番号です。例えば、**Vine5.0** なら **x.x** を **5.0** と置き換えます。

```
 rpm http://www.openrtm.org/pub/Linux/Vine/apt 5.0/$(ARCH) main
```

sources.list を書き変えたら、次の手順でインストールを行います。

```
 > su
 # apt-get update
 # apt-get install python
 # apt-get install omniORB-servers omniORBpy omniORBpy-devel omniORBpy-standarda
 # apt-get install OpenRTM-aist-Python OpenRTM-aist-Python-example
```

途中、いくつかの質問を尋ねられるので、**y** あるいは **Y** を入力して完了させます。apt-get は 現在は synaptic コマンドで置き換えることが推奨されています。

### インストールの確認

インストールの確認を以下のようにして行います。

```
 # rpm -qa | grep OpenRTM-aist-Python
 OpenRTM-aist-Python-example-1.0.0-RELEASE.vlXX
 OpenRTM-aist-Python-1.0.0-RELEASE0.vlXX
```

## パッケージの詳細
各パッケージの内容は以下の通りです

### OpenRTM-aist-Python
OpenRTM-aist-Python には Python モジュールとコマンド群が含まれています。

- コマンド
```
 /usr/bin/rtcprof_python
 /usr/bin/rtcd_python
```

- サンプル設定ファイル
```
 /usr/lib/python<version>/site-packages/OpenRTM_aist/examples/rtc.conf.sample
```

- OpenRTM-aist 本体の Python モジュール
```
 /usr/lib/python<version>/site-packages/OpenRTM_aist/*
```

- OpenRTM-aistのユーティリティモジュール
```
 /usr/lib/python<version>/site-packages/OpenRTM_aist/utils/rtcprof
 /usr/lib/python<version>/site-packages/OpenRTM_aist/utils/rtcd
 /usr/lib/python<version>/site-packages/OpenRTM_aist/utils/rtc-template
 /usr/lib/python<version>/site-packages/OpenRTM_aist/utils/rtm-naming
```

### OpenRTM-aist-Python-example
OpenRTM-aist-Python-example には RTC のサンプルが含まれています。

- サンプル
```
 /usr/share/OpenRTM-aist/examples/python/SimpleIO/
 /usr/share/OpenRTM-aist/examples/python/SimpleService/
 中略
```


以上、インストールが終了しましたら、[動作確認]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/test_linux_python_1_1)へ進みましょう。

