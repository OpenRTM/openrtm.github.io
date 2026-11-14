---
layout: page
title: raspberry pi (rasbian) へのインストール
---
<br>
<a>No English version available.
</a>


<!-- Title: Raspberry Pi (Rasbian) へのインストール -->
<div align="right"><a href="Raspberry_Pi_Logo.svg_.png"><img src="Raspberry_Pi_Logo.svg_.png" width="15%; margin:10px;" align="right"></a></div>

#contents

C++版 OpenRTM-aist は Raspberry Pi 用 Raspbian の armhf、armel用 deb パッケージが提供されています。
Raspberry Pi でセルフコンパイルを行うと約3時間くらいかかりますので、パッケージが利用できる場合はこれを利用することをお勧めします。
ただし、Raspbian への対応およびそのバージョンは、予告なしに変更または停止されることがありますので、予めご了承ください。




## はじめに
### 対応バージョン

現在のところパッケージが用意されている Raspbian のバージョンは

- Raspbian "wheezy" (armhf アーキテクチャ)
- Soft-float Debian "wheezy" (armel アーキテクチャ)

です。

### SDメモリーカードの準備

以下のページからイメージをダウンロードして、SDメモリーカードに書き込みます。SDメモリーカードは **4GB** 以上はあったほうがよいでしょう。
SDメモリーカードへの書き込み方法については [RPi SD Card Setup](http://elinux.org/RPi_Easy_SD_Card_Setup) を参照してください。

- [Raspberry Pi ダウンロード](http://www.raspberrypi.org/downloads)
- [RPi SD Card Setup](http://elinux.org/RPi_Easy_SD_Card_Setup)

Windowsでは、[Win32DiskImager](https://launchpad.net/win32-image-writer/+download) などを利用して書き込みます。
Linux や Mac OS では dd を利用して書き込みます。

```
 $ sudo dd if=/dev/<SDメモリーカードのデバイスファイル> of=<ダウンロード・解凍したイメージファイル> bs=1m
```

## OpenRTM-aist のインストール

OpenRTM-aist のインストールの方法には大きく分けて以下の2種類のインストール方法があります。

- openrtm.org が提供する一括インストールスクリプトを使用
- apt-get や synaptic パッケージマネージャを仕様

好みの方法でインストールしてください。



### 一括インストール・スクリプトを使う方法

<!-- [[移動ロボットKobukiの制御:http://openrtm.org/openrtm/ja/node/273/]] のページでもセットアップスクリプトを紹介しています。 -->

openrtm.org が提供するインストール・スクリプト **pkg_install_raspbian.sh**をダウンロードページからダウンロードし、root 権限で実行します。このスクリプトは、必要なパッケージを順次 apt-get でインストールしていきます。

<!-- -[[一括インストールスクリプト:http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_raspbian.sh]] -->

OpenRTM-aist を開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。初めて OpenRTM-aist をインストールしてみる方やソースをコンパイルしてみる方にもお勧めします。

詳しいインストール方法や、オプション・パッケージの種類につきましては、「[一括インストール・スクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script/)」のページをご確認ください。

<!-- 以下、一括インストールスクリプトを使用したインストールの手順です。 -->


<!-- > wget [pkg_install_raspbian.sh のダウンロードURL] -->
<!-- > su -->
<!-- # ./pkg_install_raspbian.sh -l c++ -->
<!-- //途中、いくつかの質問をたずねられるので、''y'' あるいは ''Y'' を入力しながら完了させる。 -->
<!-- //オプション "--yes" を追加することで、省略も可能。 -->


### apt-get を使う方法

#### source.list の編集

openrtm.org では apt-get から利用可能なパッケージリポジトリを提供してい
ます。ただし、デフォルトのパッケージリポジトリには含まれていませんので、
apt-get の設定を変更する必要があります。

/etc/apt/sources.list に以下の行を追加します。

```
 > su
 # vi /etc/apt/sources.list # "sources.list" を編集
```

```
  deb http://www.openrtm.org/pub/Linux/raspbian/ (code name) main
```

の1行を追加。"(code name)" の部分には以下の raspbian のバージョンに対応したコードネームを指定します。

<table class="table-alt">
  <tr>
    <th>バージョン</th>
    <th>code name</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Debian GNU Linux</td>
  </tr>
  <tr>
    <td>Debian 7.0</td>
    <td>wheezy</td>
  </tr>
</table>

Raspbianの過去・現在のバージョン/コードネームは、http://www.raspberrypi.org/downloads から確認できます。

#### apt-get によるインストール

次の手順でインストールを行います。途中、いくつかの応答を求められるので、**y** を入力しながら完了させてください。

```
 # apt-get update
 # apt-get install gcc g++ make uuid-dev
 # apt-get install libomniorb4-1 libomniorb4-dev omniidl omniorb-nameserver
 # apt-get install openrtm-aist openrtm-aist-doc openrtm-aist-dev openrtm-aist-example
```

なお、インストール済みの OpenRTM-aist を特定バージョンのまま保持したい場合には、**/etc/apt/preferences**を編集して以下の行を追加します。（この例では1.1系列にバージョンを固定します。）

```
 Package: OpenRTM-aist
 Pin: version 1.1.*
```

詳しくは
[http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.ja.html#s-pin](http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.ja.html#s-pin)
を参照してください。


### インストールの確認

インストールを確認します。


<!-- $ dpkg -l 'openrtm*' -->
<!-- Desired=Unknown/Install/Remove/Purge/Hold -->
<!-- | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend -->
<!-- |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)  -->
<!-- ||/ Name           Version        Description -->
<!-- +++-==============-==============-============================================ -->
<!-- ii  openrtm-aist   1.1.0-0        OpenRTM-aist, RT-Middleware distributed by A -->
<!-- ii  openrtm-aist-d 1.1.0-0        OpenRTM-aist headers for development -->
<!-- ii  openrtm-aist-d 1.1.0-0        Documentation for openrtm-aist -->
<!-- ii  openrtm-aist-e 1.1.0-0        OpenRTM-aist examples -->

```
 pi@raspberrypi ~ $ dpkg -l 'openrtm*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
 | 状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリガ待ち/(T)トリガ保留
 |/ エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
 ||/ 名前                  バージョン      アーキテクチャ  説明
 +++-=====================-===============-===============-===============================================
 ii  openrtm-aist          1.1.0-0         armhf           OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-dev      1.1.0-0         armhf           OpenRTM-aist headers for development
 ii  openrtm-aist-doc      1.1.0-0         all             Documentation for openrtm-aist
 ii  openrtm-aist-example  1.1.0-0         armhf           OpenRTM-aist examples
```


## パッケージの詳細
各パッケージの内容は以下の通りです。

### openrtm-aist
openrtm-aist にはランタイムライブラリとコマンド群が含まれています。

- コマンド
```
 /usr/bin/rtcd
 /usr/bin/rtm-naming
```

- ライセンス等
```
 /usr/share/doc/openrtm-aist/changelog.gz
 /usr/share/doc/openrtm-aist/README.Debian
 /usr/share/doc/openrtm-aist/README
 /usr/share/doc/openrtm-aist/README.jp
 /usr/share/doc/openrtm-aist/NEWS.gz
 /usr/share/doc/openrtm-aist/copyright
 /usr/share/doc/openrtm-aist/changelog.Debian.gz
```

- 設定ファイルサンプル
```
 /usr/etc/rtc.conf.sample
```

- ライブラリ
```
 /usr/lib/libRTC.la
 /usr/lib/libRTC.so
 /usr/lib/libRTC-X.X.X.so.X
 /usr/lib/libRTC-X.X.X.so
```

### openrtm-aist-dev
openrtm-aist-dev には、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/rtc-template
 /usr/bin/rtm-config
 /usr/bin/rtm-skelwrapper
```

- ライセンス等
```
 /usr/share/doc/openrtm-aist-dev/changelog.gz
 /usr/share/doc/openrtm-aist-dev/copyright
 /usr/share/doc/openrtm-aist-dev/changelog.Debian.gz
```

- ヘッダ
```
 /usr/include/openrtm-1.1/rtm/DefaultPeriodicTask.h
 /usr/include/openrtm-1.1/rtm/OutPortPullConnector.h
 中略
 /usr/include/openrtm-1.1/rtm/ExecutionContextBase.h
 /usr/include/openrtm-1.1/rtm/Manager.h
 /usr/include/coil-1.1/coil/OS.h
 /usr/include/coil-1.1/coil/UUID.h
 中略
 /usr/include/coil-1.1/coil/Properties.h
```


- ライブラリ・その他
<!-- /usr/lib/OpenRTM-aist/py_helper/cxx_svc_impl.py -->
<!-- /usr/lib/OpenRTM-aist/py_helper/profile_gen.py -->
<!-- 中略 -->
<!-- /usr/lib/OpenRTM-aist/py_helper/gen_base.py -->
<!-- /usr/lib/OpenRTM-aist/py_helper/yat.py -->
<!-- /usr/lib/pkgconfig/libcoil.pc -->
<!-- /usr/lib/pkgconfig/libRTM.pc -->
```
 /usr/lib/openrtm-1.1/py_helper/cxx_svc_impl.py
 /usr/lib/openrtm-1.1/py_helper/profile_gen.py
 中略
 /usr/lib/openrtm-1.1/py_helper/gen_base.py
 /usr/lib/openrtm-1.1/py_helper/yat.py
 /usr/lib/pkgconfig/libcoil.pc
 /usr/lib/pkgconfig/libRTM.pc
```

### openrtm-aist-example
openrtm-aist-example にはスタンドアロンRTC、ローダブルRTC それぞれのサンプルと、サンプルRTC のソースが含まれています。

- サンプル(スタンドアロンRTC)
<!-- /usr/share/OpenRTM-aist/examples/ConsoleOutComp -->
<!-- /usr/share/OpenRTM-aist/examples/ConsoleInComp -->
<!-- 中略 -->
```
 /usr/share/openrtm-1.1/examples/ConsoleOutComp
 /usr/share/openrtm-1.1/examples/ConsoleInComp
 中略
```

- サンプル(ソース)
<!-- /usr/share/OpenRTM-aist/examples/src/Composite/README.Motor -->
<!-- /usr/share/OpenRTM-aist/examples/src/Composite/Makefile.Sensor -->
<!-- /usr/share/OpenRTM-aist/examples/src/Composite/Motor.cpp -->
<!-- 中略 -->
<!-- /usr/share/OpenRTM-aist/examples/src/SimpleService/Makefile.MyServiceProvider -->
<!-- /usr/share/OpenRTM-aist/examples/src/SimpleService/rtc.conf -->
```
 /usr/share/openrtm-1.1/examples/src/Composite/README.Motor
 /usr/share/openrtm-1.1/examples/src/Composite/Makefile.Sensor
 /usr/share/openrtm-1.1/examples/src/Composite/Motor.cpp
 中略
 /usr/share/openrtm-1.1/examples/src/SimpleService/Makefile.MyServiceProvider
 /usr/share/openrtm-1.1/examples/src/SimpleService/rtc.conf
```



- サンプル(ローダブルRTC)
<!-- /usr/share/OpenRTM-aist/examples/rtcs/MyServiceConsumer.so.0.0.0 -->
<!-- /usr/share/OpenRTM-aist/examples/rtcs/SeqIn.so.0.0.0 -->
<!-- 中略 -->
<!-- /usr/share/OpenRTM-aist/examples/rtcs/ConfigSample.so.0.0.0 -->
<!-- /usr/share/OpenRTM-aist/examples/rtcs/ConsoleOut.so.0.0.0 -->
```
 /usr/share/openrtm-1.1/example/rtc/MyServiceConsumer.so.0.0.0
 /usr/share/openrtm-1.1/example/rtc/SeqIn.so.0.0.0
 中略
 /usr/share/openrtm-1.1/example/rtc/ConfigSample.so.0.0.0
 /usr/share/openrtm-1.1/example/rtc/ConsoleOut.so.0.0.0
```


- ライセンス等
```
 /usr/share/doc/openrtm-aist-example/changelog.gz
 /usr/share/doc/openrtm-aist-example/copyright
 /usr/share/doc/openrtm-aist-example/changelog.Debian.gz
```

### openrtm-aist-doc
openrtm-aist-doc には、日本語と英語のクラスリファレンス、IDLインターフェース定義リファレンスが含まれています。

- クラスリファレンス
<!-- /usr/share/OpenRTM-aist/docs/ClassReference/html/ConnectorBase_8h-source.html -->
<!-- /usr/share/OpenRTM-aist/docs/ClassReference/html/RTC_8h.html -->
<!-- 中略 -->
<!-- /usr/share/OpenRTM-aist/docs/ClassReference/html/FactoryInit_8h-source.html -->
```
 /usr/share/openrtm-1.1/doc/ClassReference/html/ConnectorBase_8h_source.html
 /usr/share/openrtm-1.1/doc/ClassReference/html/RTC_8h.html
 中略
 /usr/share/openrtm-1.1/doc/ClassReference/html/FactoryInit_8h_source.html
```


- IDLリファレンス
<!-- /usr/share/OpenRTM-aist/docs/IDLReference/html/BasicDataType_8idl-source.html -->
<!-- 中略 -->
<!-- /usr/share/OpenRTM-aist/docs/IDLReference/html/interfaceOpenRTM_1_1InPortCdr-members.html -->
```
 /usr/share/openrtm-1.1/doc/IDLReference/html/BasicDataType_8idl_source.html
 中略
 /usr/share/openrtm-1.1/doc/IDLReference/html/interfaceOpenRTM_1_1InPortCdr-members.html
```

- クラスリファレンス(英語)
<!-- /usr/share/OpenRTM-aist/docs/ClassReference-en/html/ConnectorBase_8h-source.html -->
<!-- /usr/share/OpenRTM-aist/docs/ClassReference-en/html/RTC_8h.html -->
<!-- 中略 -->
<!-- /usr/share/OpenRTM-aist/docs/ClassReference-en/html/FactoryInit_8h-source.html -->
```
 /usr/share/openrtm-1.1/doc/ClassReference-en/html/ConnectorBase_8h_source.html
 /usr/share/openrtm-1.1/doc/ClassReference-en/html/RTC_8h.html
 中略
 /usr/share/openrtm-1.1/doc/ClassReference-en/html/FactoryInit_8h-source.html
```


- IDLリファレンス(英語)
<!-- /usr/share/OpenRTM-aist/docs/IDLReference-en/html/BasicDataType_8idl-source.html -->
<!-- /usr/share/OpenRTM-aist/docs/IDLReference-en/html/structRTC_1_1FsmProfile.html -->
<!-- 中略 -->
<!-- /usr/share/OpenRTM-aist/docs/IDLReference-en/html/interfaceOpenRTM_1_1InPortCdr-members.html -->
```
 /usr/share/openrtm-1.1/doc/IDLReference-en/html/BasicDataType_8idl_source.html
 /usr/share/openrtm-1.1/doc/IDLReference-en/html/structRTC_1_1FsmProfile.html
 中略
 /usr/share/openrtm-1.1/doc/IDLReference-en/html/interfaceOpenRTM_1_1InPortCdr-members.html
```

- ライセンス等
```
 /usr/share/doc/openrtm-aist-doc/changelog.gz
 /usr/share/doc/openrtm-aist-doc/copyright
 /usr/share/doc/openrtm-aist-doc/changelog.Debian.gz
```


## 履歴

- 2015-02-17 15:43:30 +0900: 「パッケージの詳細」のディレクトリーの修正
- 2012-12-26 15:43:30 +0900: Raspberry Pi (Raspbian) へのインストール、新規作成

