---

layout: page
title: raspbianへのインストール

---
<br>
<a>No English version available.
</a>

<!-- Titile: Raspbianへのインストール -->
<div align="right"><a href="Raspberry_Pi_Logo.svg_.png"><img src="Raspberry_Pi_Logo.svg_.png" width="15%; margin:10px;" align="right"></a></div>

#contents

C++版OpenRTM-aistはRaspberry Pi用Raspbianl用debパッケージが提供されています。
Raspbianへの対応およびそのバージョンは、予告なしに変更または停止されることがありますので、あらかじめご了承ください。

## 対応バージョン

現在パッケージが用意されているRaspbianのバージョンは

- Buster

です。

## SDカードの準備

### OSイメージのダウンロード
以下のリンクからRasbianのイメージ(「Raspbian Buster with desktop and recommended software」のイメージを推奨しますが、必要に応じて他のイメージを選択してもかまいません)をダウンロードし、解凍し、SDカードに書き込みます。SDカードの容量は4GB以上はあったほうがよいでしょう。
- [Raspbian Downloads](https://www.raspberrypi.org/downloads/raspbian/)

### SDカードへの書き込み
SDカードへの書き込み方法については [RPi Easy SD Card Setup](http://elinux.org/RPi_Easy_SD_Card_Setup) を参照してください。

このリンクではいくつかの方法が説明されています。そのうちのいくつかの概要を示すと:

#### Windowsの場合
- [Win32 Disk Imager](https://forest.watch.impress.co.jp/docs/review/1067836.html)などを利用して書き込みます。

Windowsを用いる方法の方がLinuxやMac OSを用いるより簡単なので、初心者にはWindowsを用いる方法を推奨します。

#### LinuxやMac OSの場合
- **dd**コマンドを以下のように利用して書き込みます。

```
 $ sudo dd of=/dev/<SDカードのデバイスファイル> if=<ダウンロード・解凍したイメージファイル> bs=4M status=progress
 $ sudo sync
```

上記コマンドによるSDカードへの書き込みはかなり長い時間を必要とします。(数分から10数分)。また、SDカードのデバイスファイル名を見つけるには
```
 $ df -h
```
と入力し、表示されるデバイスのサイズからどのデバイスがSDカードかを見つけます。例えば、現在Rasbianがインストールされている16GBのSDカードを用いている場合、あるデバイスが14GBのデバイスとして表示され、そのデバイスが/dev/sdf7と表示されます。他にも/dev/sdf5、/dev/sdf6などの後尾の数字だけが違うデバイスが表示されます。これらがSDカードで使われているデバイス名です。これらのデバイス全て以下のようにumountしてください。
```
 $ umount /dev/sdf5
 $ umount /dev/sdf6
 $ umount /dev/sdf7
```

その後、上記の**dd**コマンドを実行しますが、この例でのデバイスファイル名は/dev/sdfになります。


## OpenRTM-aist (C++)インストール

OpenRTM-aist (C++)のインストールの方法には大きく分けて以下の2種類のインストール方法があります。

- openrtm.orgが提供する一括インストールスクリプトを使用
- apt-getやsynapticパッケージマネージャを使用

好みの方法でインストールしてください。

### 一括インストールスクリプトを使う方法

openrtm.orgが提供するインストールスクリプト**pkg_install_raspbian.sh**をダウンロードページからダウンロードし、root権限で実行します。このスクリプトは、必要なパッケージを順次apt-getでインストールしていきます。

OpenRTM-aistを開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。初めてOpenRTM-aistをインストールしてみる方に推奨します。

一括インストール・スクリプトをダウンロードした後、ダウンロードしたディレクトリに移動して
```
  $ sudo sh pkg_install_raspbian.sh -l c++ --yes
```

でインストールできます。

一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種類につきましては、「[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)」のページをご確認ください。

### apt-getを使う方法

#### source.listの編集

openrtm.orgではapt-getから利用可能なパッケージリポジトリを提供しています。ただし、デフォルトのパッケージリポジトリには含まれていませんので、apt-getの設定を変更する必要があります。そのためには/etc/apt/sources.listを編集して以下の行を追加します。

```
  deb http://www.openrtm.org/pub/Linux/raspbian/ buster main
```

#### apt-getによるインストール

次の手順でインストールを行います。途中、いくつかの応答を求められるので、**y**を入力しながら完了させてください。

```
 # apt-get update
 # apt-get install gcc g++ make uuid-dev
 # apt-get install libomniorb4-1 libomniorb4-dev omniidl omniorb-nameserver
 # apt-get install openrtm-aist openrtm-aist-doc openrtm-aist-dev openrtm-aist-example
```

なお、インストール済みのOpenRTM-aistを特定バージョンのまま保持したい場合には、**/etc/apt/preferences**を編集して以下の行を追加します。（この例では1.1系列にバージョンを固定します。）

```
 Package: OpenRTM-aist
 Pin: version 1.1.*
```

詳しくは
http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.ja.html#s-pin
を参照してください。

## rtshellのインストール
rtshellはPythonのプログラムのため、OpenRTM-Pythonのインストールが必要です。OpenRTM-aist(Python版)のインストールでの[Raspbianへのインストール]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2/raspbian_python_1_2)のページの手順を実行してください。

## インストールの確認

インストールを確認します。

```
 pi@raspberrypi ~ $ dpkg -l 'openrt*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
    状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリガ待ち/(T)トリガ保留
    / エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
    / 名前                       バージョン   アーキテクチ 説明
 +++-==========================-============-============-===============================================
 ii  openrtm-aist:armhf         1.2.1-0      armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-dev:armhf     1.2.1-0      armhf        OpenRTM-aist headers for development
 ii  openrtm-aist-doc           1.2.1-0      all          Documentation for openrtm-aist
 ii  openrtm-aist-example:armhf 1.2.1-0      armhf        OpenRTM-aist examples
 ii  openrtm-aist-idl:armhf     1.2.1-0      armhf        OpenRTM-aist idls for development
```

## パッケージの詳細
各パッケージの内容は以下の通りです。
### openrtm-aist
openrtm-aistにはランタイムライブラリとコマンド群が含まれています。

- コマンド
```
 /usr/bin/rtcd
 /usr/bin/rtcprof
 /usr/bin/rtm-config
 /usr/bin/rtm-naming
```

- ライセンスなど
```
 /usr/share/doc/openrtm-aist/changelog.gz
 /usr/share/doc/openrtm-aist/README.Debian
 /usr/share/doc/openrtm-aist/README
 /usr/share/doc/openrtm-aist/README.jp
 /usr/share/doc/openrtm-aist/copyright
 /usr/share/doc/openrtm-aist/changelog.Debian.gz
```

- 設定ファイルサンプル
```
 /usr/etc/rtc.conf.sample
 /usr/lib/arm-linux-gnueabihf/pkgconfig/openrtm-aist.pc
 /usr/etc/fluent-bit/fluent-bit.conf
 /usr/etc/fluent-bit/parsers.conf
```

- ライブラリ
```
 /usr/lib/arm-linux-gnueabihf/libRTC-1.2.1.so
 /usr/lib/arm-linux-gnueabihf/libRTC.a
 中略
 /usr/lib/arm-linux-gnueabihf/librtmManipulator.so.0.0.0
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/ec/FileNameservice.la
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/ec/FileNameservice.so
 中略
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/ec/RTPreemptEC.so.0.0.0
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/logger/FluentBit.la
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/logger/FluentBit.so
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/logger/FluentBit.so.0
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/logger/FluentBit.so.0.0.0
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/sdo/LoggerConsumer.la
 中略
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/sdo/LoggerConsumer.so.0.0.0
 /usr/lib/libfluent-bit.so
```

- ヘッダ
```
 /usr/include/fluent-bit/flb_api.h
 /usr/include/fluent-bit/flb_bits.h
 中略
 /usr/include/fluent-bit/flb_worker.h
 /usr/include/fluent-bit.h
```

### openrtm-aist-dev
openrtm-aist-devには、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/coil-config
 /usr/bin/rtc-template
 /usr/bin/rtm-skelwrapper
```

- ライセンスなど
```
 /usr/share/doc/README
 /usr/share/doc/README.Debian
 /usr/share/doc/README.jp
 /usr/share/doc/openrtm-aist-dev/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-dev/changelog.gz
 /usr/share/doc/openrtm-aist-dev/copyright
```

- ヘッダ
```
 /usr/include/coil-1.2/coil/Affinity.h
 /usr/include/coil-1.2/coil/Allocator.h
 中略
 /usr/include/coil-1.2/coil/stringutil.h
 /usr/include/openrtm-1.2/rtm/BufferBase.h
 /usr/include/openrtm-1.2/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-1.2/rtm/config_rtc.h
 /usr/include/openrtm-1.2/rtm/ext/CameraCommonInterface.hh
 /usr/include/openrtm-1.2/rtm/ext/CameraCommonInterfaceDynSK.cc
 中略
 /usr/include/openrtm-1.2/rtm/ext/ManipulatorCommonInterface_MiddleStub.h
 /usr/include/openrtm-1.2/rtm/ext/ec/artlinux/ArtExecutionContext.h
 /usr/include/openrtm-1.2/rtm/ext/ec/artlinux/rtc.conf.sample
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/LogicalTimeTriggeredEC.h
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/LogicalTimeTriggeredEC.idl
 中略
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/LogicalTimeTriggeredECStub.h
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredEC.hh
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredEC.idl
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredECDynSK.cc
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredECSK.cc
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt/RTPreemptEC.h
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt/rtc.conf.sample
 /usr/include/openrtm-1.2/rtm/ext/local_service/nameservice_file
 /usr/include/openrtm-1.2/rtm/ext/local_service/nameservice_file/FileNameservice.h
 /usr/include/openrtm-1.2/rtm/ext/logger/fluentbit_stream/FluentBit.h
 /usr/include/openrtm-1.2/rtm/ext/logger/fluentbit_stream/fluentbit.conf
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/Logger.hh
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/Logger.idl
 中略
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/LoggerStub.h
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserver.idl
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserverConsumer.h
 中略
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserverStub.h
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserver.hh
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserver.idl
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserverDynSK.cc
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserverSK.cc
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.hh
 /usr/include/openrtm-1.2/rtm/idl/BasicDataTypeDynSK.cc
 中略
 /usr/include/openrtm-1.2/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-1.2/rtm/version.h
 /usr/include/openrtm-1.2/rtm/version.txt
```

- ライブラリ・その他
```
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/cmake/OpenRTMConfig.cmake
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/py_helper/README_gen.py
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/py_helpver/cxx_gen.py
 中略
 /usr/lib/arm-linux-gnueabihf/openrtm-1.2/py_helpver/yat.py
 /usr/lib/arm-linux-gnueabihf/pkgconfig/libcoil.pc
```

### openrtm-aist-idl
- スクリプトファイル
```
 /etc/profile.d/openrtm-aist-idl.sh
```

- ライセンスなど
```
 /usr/share/doc/openrtm-aist-idl/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-idl/changelog.gz
 /usr/share/doc/openrtm-aist-idl/copyright
```

- idlファイル
```
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.idl
 /usr/include/openrtm-1.2/rtm/idl/CameraCommonInterface.idl
 中略
 /usr/include/openrtm-1.2/rtm/idl/SharedMemory.idl
 /usr/share/openrtm-1.2/idl/BasicDataType.idl
 /usr/share/openrtm-1.2/idl/CameraCommonInterface.idl
 /usr/share/openrtm-1.2/idl/DataPort.idl
 中略
 /usr/share/openrtm-1.2/idl/SharedMemory.idl
```

### openrtm-aist-example
openrtm-aist-exampleにはスタンドアロンRTC、ローダブルRTCそれぞれのサンプルと、サンプルRTCのソースが含まれています。

- サンプル(スタンドアロンRTC)

```
 /usr/share/openrtm-1.2/components/c++/examples/ConsoleOutComp
 /usr/share/openrtm-1.2/components/c++/examples/ConsoleInComp
 中略
 /usr/share/openrtm-1.2/components/c++/examples/consout.conf
 /usr/share/openrtm-1.2/components/c++/examples/rtc.composite.linux.conf
 /usr/share/openrtm-1.2/components/c++/examples/rtc.conf
```

- サンプル(ソース)

```
 /usr/share/openrtm-1.2/components/c++/examples/src/Composite/README.Motor
 /usr/share/openrtm-1.2/components/c++/examples/src/Composite/Makefile.Sensor
 /usr/share/openrtm-1.2/components/c++/examples/src/Composite/Motor.cpp
 中略
 /usr/share/openrtm-1.2/components/c++/examples/src/Throughput/rtc.conf
 /usr/share/openrtm-1.2/Components/c++/examples/src/Throughput/run.sh
 /usr/share/openrtm-1.2/Componnets/c++/examples/templates/AIO.xml
 /usr/share/openrtm-1.2/Components/c++/examples/templates/ActArray.xml
 中略
 /usr/share/openrtm-1.2/Components/c++/examples/templates/VelocityControl3D.xml
```

- サンプル(ローダブルRTC)

```
 /usr/share/openrtm-1.2/components/c++/examples/rtc/ConfigSample.a
 /usr/share/openrtm-1.2/components/c++/examples/rtc/ConfigSample.la
 中略
 /usr/share/openrtm-1.2/components/c++/examples/rtc/Throughput.so.X.X.X
 /usr/share/openrtm-1.2/components/c++/examples/rtc/Cofig.sample.so
 /usr/share/openrtm-1.2/components/c++/examples/rtc/Cofig.sample.so.X
 中略
 /usr/share/openrtm-1.2/components/c++/examples/rtc/Troughput.so.X
```

- ライセンスなど
```
 /usr/share/doc/openrtm-aist-example/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-example/changelog.gz
 /usr/share/doc/openrtm-aist-example/copyright
```

### openrtm-aist-idl
- idlファイルなど
```
 /etc/profile.d/openrtm-aist-idl.sh
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.idl
 /usr/include/openrtm-1.2/rtm/idl/CameraCommonInterface.idl
 中略
 /usr/include/openrtm-1.2/rtm/idl/SharedMemory.idl
 /usr/share/openrtm-1.2/idl/BasicDataType.idl
 /usr/share/openrtm-1.2/idl/CameraCommonInterface.idl
 中略
 /usr/share/openrtm-1.2/idl/SharedMemory.idl
```

- ライセンスなど
```
 /usr/share/doc/openrtm-aist-idl/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-idl/changelog.gz
 /usr/share/doc/openrtm-aist-idl/copyright
```

### openrtm-aist-doc
openrtm-aist-docには、日本語と英語のクラスリファレンス、IDLインターフェース定義リファレンスが含まれています。

- クラスリファレンス
```
 /usr/share/openrtm-1.2/doc/c++/ClassReference/html/Affinity_8h.html
 /usr/share/openrtm-1.2/doc/c++/ClassReference/html/Affinity_8h__dep__incl.dot
 中略
 /usr/share/openrtm-1.2/doc/c++/ClassReference/html/version_8h_source.html
```

- IDLリファレンス
```
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/BasicDataType_8idl.html
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/BasicDataType_8idl__dep__incl.dot
 中略
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/unionSDOPackage_1_1Numeric.html
```

- クラスリファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/c++/ClassReference-en/html/Affinity_8h.html
 /usr/share/openrtm-1.2/doc/c++/ClassReference-en/html/Affinity_8h__dep__incl.dot
 中略
 /usr/share/openrtm-1.2/doc/c++/ClassReference-en/html/version_8h_source.html
```

- IDLリファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/BasicDataType_8idl__dep__incl.dot
 中略
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
```
- ライセンスなど
```
 /usr/share/doc/openrtm-aist-doc/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-doc/changelog.gz
 /usr/share/doc/openrtm-aist-doc/copyright
```





