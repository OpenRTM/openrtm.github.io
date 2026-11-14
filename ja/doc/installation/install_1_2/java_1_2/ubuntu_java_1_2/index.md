---
layout: page
title:  ubuntu/debianへのインストール
---

<!-- Title: Ubuntu/Debianへのインストール -->
<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="100;" align="right"></a></div>


Java版のOpenRTM-aistは、UbuntuやDebian GNU Linuxで利用可能なdebパッケージが提供されています。
対応しているディストリビューションのバージョンは、ダウンロードページで確認できます。
Ubuntu/Debian GNU Linuxへのサポートバージョンや対応の有無は、予告なしに変更されることがありますので、あらかじめご了承ください。

#contents

## 一括インストールスクリプト
openrtm.orgが提供するインストール・スクリプト**pkg_install_ubuntu.sh**または**pkg_install_debian.sh**を指定のURLからダウンロードし、root権限で実行します。このスクリプトでは必要なパッケージを順次apt-getを用いてインストールしていきます。

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。

一括インストールスクリプトは、ダウンロードした後、ダウンロード先ディレクトリに移動し、

Ubuntuの場合は

```
 $ sudo sh pkg_install_ubuntu.sh -l java --yes
```
Debianの場合はsuでroot権限を得た後に

```
 # sh pkg_install_debian.sh -l java --yes
```
でインストールできます。

一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種類につきましては、「[一括インストールスクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)」のページをご確認ください。

## OpenRTPのインストール
一般的なUbuntu/Debian環境での開発にはRTC BuilderやRTSystem Editorを使用しますが、その場合にはOpenRTPが必要です。一括インストールスクリプトを用いてOpenRTPをインストールしてください。Ubuntuではpkg_install_ubuntu.shが置いてあるディレクトリで

Ubuntuの場合は
```
 $ sudo sh ./pkg_install_ubuntu.sh -l openrtp --yes
```

Debianの場合はsuでroot権限を得た後に
```
 # sh pkg_install_debian.sh -l openrtp --yes
```

と入力するとOpenRTPをインストールできます。

## JDK8のインストール

Java版OpenRTM-aistの使用にはJDK8相当のJava環境が必要です。(デフォルトの環境でJDK8がインストールされている場合もありますが、Ubuntu 18.04ではJDK11がインストールされているため、JDK8のインストールが必要です。)　JDK8の入手やインストールについては以下を参照してください。
- [JDK8のインストール]({{ site.baseurl }}/ja/doc/installation/common/install_jdk8)

### インストールの確認
インストールを確認します。

```
 $ dpkg -l 'openrt*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
    状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリガ待ち/(T)トリガ保留
    / エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
    / 名前                     バージョン        アーキテクチャ    説明
 +++-========================-=================-=================-======================================================
 ii  openrtm-aist:amd64       1.2.1-0           amd64             OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-dev:amd64   1.2.1-0           amd64             OpenRTM-aist headers for development
 ii  openrtm-aist-idl:amd64   1.2.1-0           amd64             OpenRTM-aist idls for development
 ii  openrtm-aist-java:amd64  1.2.1-0           amd64             OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-java-doc    1.2.1-0           all               Documentation for openrtm-aist-java
 ii  openrtm-aist-java-exampl 1.2.1-0           amd64             OpenRTM-aist-Java examples
 ii  openrtp:amd64            1.2.1-0           amd64             OpenRTP, Open RT Platform distributed by AIST
```

<!-- ***環境変数の設定 -->
<!-- OpenRTM-aist-1.2.0の場合は、RTM_JAVA_ROOTという環境変数の設定が必要です。現在ログイン中のユーザーのみへの設定とする場合は、~/.bash_profileに、そのシステムを使用するすべてのユーザー用として設定する場合は、/etc/profileに以下の行を付け加えてください。(OpenRTM-1.2.1ではこの操作は必要なくなる予定です。) -->
<!--  -->
<!-- RTM_JAVA_ROOT=/usr/lib/x86_64-linux-gnu/opertm-1.2 -->
<!-- export RTM_JAVA_ROOT -->
<!--  -->

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
```

- ライブラリ
  - 32bit
```
 /usr/lib/i386-linux-gnu/libRTC-X.X.X.so
 /usr/lib/i386-linux-gnu/libRTC.a
 /usr/lib/i386-linux-gnu/libRTC.la
 /usr/lib/i386-linux-gnu/libcoil-X.X.X.so
 /usr/lib/i386-linux-gnu/libcoil.a
 /usr/lib/i386-linux-gnu/librtmCamera.a
 /usr/lib/i386-linux-gnu/librtmCamera.la
 /usr/lib/i386-linux-gnu/librtmCamera.so.X.X.X
 /usr/lib/i386-linux-gnu/librtmManipulator.a
 /usr/lib/i386-linux-gnu/librtmManipulator.la
 /usr/lib/i386-linux-gnu/librtmManipulator.so.X.X.X
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/FileNameservice.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/FileNameservice.so.X.X.X
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.a
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.so.X.X.X
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.so.X.X.X
 /usr/lib/i386-linux-gnu/openrtm-1.2/ssl/SSLTransport.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/ssl/SSLTransport.so.X.X.X
 /usr/lib/i386-linux-gnu/pigconfig/openrtm-aist.pc
```
  - 64bit
```
 /usr/lib/x86_64-linux-gnu/libRTC-X.X.X.so
 /usr/lib/x86_64-linux-gnu/libRTC.a
 /usr/lib/x86_64-linux-gnu/libRTC.la
 /usr/lib/x86_64-linux-gnu/libcoil-X.X.X.so
 /usr/lib/x86_64-linux-gnu/libcoil.a
 /usr/lib/x86_64-linux-gnu/librtmCamera.a
 /usr/lib/x86_64-linux-gnu/librtmCamera.la
 /usr/lib/x86_64-linux-gnu/librtmCamera.so.X.X.X
 /usr/lib/x86_64-linux-gnu/librtmManipulator.a
 /usr/lib/x86_64-linux-gnu/librtmManipulator.la
 /usr/lib/x86_64-linux-gnu/librtmManipulator.so.X.X.X
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/FileNameservice.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/FileNameservice.so.X.X.X
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.a
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.so.X.X.X
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.so.X.X.X
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ssl/SSLTransport.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ssl/SSLTransport.so.X.X.X
 /usr/lib/x86_64-linux-gnu/pigconfig/openrtm-aist.pc
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
 /usr/share/doc/openrtm-aist-dev/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-dev/changelog.gz
 /usr/share/doc/openrtm-aist-dev/copyright
```

- ヘッダなど

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
 /usr/include/openrtm-1.2/rtm/ext/CameraCommonInterface.idl
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
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt/RTPreemptEC.h
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt/rtc.conf.sample
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
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.idl
 中略
 /usr/include/openrtm-1.2/rtm/idl/device_interfaces/Ranger.idl
 /usr/include/openrtm-1.2/rtm/version.h
 /usr/include/openrtm-1.2/rtm/version.txt
```

- ライブラリ・その他
 - 32bit

```
 /usr/lib/i386-linux-gnu/openrtm-1.2/cmake/OpenRTMConfig.cmake
 /usr/lib/i386-linux-gnu/openrtm-1.2/py_helper/README_gen.py
 /usr/lib/i386-linux-gnu/openrtm-1.2/py_helpver/cxx_gen.py
 中略
 /usr/lib/i386-linux-gnu/openrtm-1.2/py_helpver/yat.py
 /usr/lib/i386-linux-gnu/pkgconfig/libcoil.pc
```

 - 64bit

```
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/cmake/OpenRTMConfig.cmake
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/py_helper/README_gen.py
 /usr/lib/x86-64-linux-gnu/openrtm-1.2/py_helpver/cxx_gen.py
 中略
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/py_helpver/yat.py
 /usr/lib/x86_64-linux-gnu/pkgconfig/libcoil.pc
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

### openrtm-aist-java
- コマンド
```
 /usr/bin/rtcd_java
 /usr/bin/rtcprof_java
```

- 環境変数設定用スクリプト
```
 /etc/profile.d/openrtm-aist-java.sh
```

- jarファイル
  - 64 bit
```
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/License.txt
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/LogicalTimeTriggeredEC.jar
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/NameserviceFile.jar
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/OpenRTM-aist-1.2.0.jar
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/commons-cli-1.1.jar
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/jna-4.2.2.jar
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/jna-platform-4.2.2.jar
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/rtcd.jar
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/jar/rtcprof.jar
```
  - 32 bit
```
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/License.txt
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/jna-platform-4.2.2.jar
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/rtcprof.jar
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/rtcd.jar
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/commons-cli-1.1.jar
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/NameserviceFile.jar
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/LogicalTimeTriggeredEC.jar
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/jna-4.2.2.jar
 /usr/lib/i386-linux-gnu/openrtm-1.2/jar/OpenRTM-aist-1.2.1.jar
```

### openrtm-aist-java-example
Java版サンプルRTC、Classファイル、ソースファイル、起動スクリプト
```
 /usr/share/openrtm-1.2/components/java/* 
 /usr/share/openrtm-1.2/components/java/RTMExamples/AutoTest/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/Composite/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/ConfigSample/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/ExtTrigger/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/GUIIn/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/GUIIn/control/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/GUIIn/model/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/GUIIn/view/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/MyService.idl
 /usr/share/openrtm-1.2/components/java/RTMExamples/SeqIO/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/SeqIO/view/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/SimpleIO/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/SimpleService/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/SinCosOut/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/Throughput/*
 /usr/share/openrtm-1.2/components/java/RTMExamples/TopicTest/*
```

### openrtm-aist-java-doc
openrtm-aist-java-doc には、日本語と英語のクラスリファレンスが含まれています。
```
 /usr/share/openrtm-1.2/doc/java/JavaDoc/OpenRTM/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/OpenRTM/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/RTC/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/RTC/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/RTM/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/RTM/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/_SDOPackage/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/_SDOPackage/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/Constants.html
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/buffer/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/buffer/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/executionContext/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/executionContext/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/log/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/port/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/port/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/port/publisher/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/port/publisher/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/util/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/util/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/util/clock/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/RTC/util/clock/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/Version.html
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/class-use
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/jp/go/aist/rtm/*
 /usr/share/openrtm-1.2/doc/java/JavaDoc/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/OpenRTM/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/OpenRTM/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/RTC/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/RTC/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/RTM/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/RTM/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/_SDOPackage/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/_SDOPackage/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/index-files/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/Constants.html
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/buffer/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/buffer/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/executionContext/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/executionContext/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/log/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/log/class-use/Logbuf.html
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/port/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/port/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/port/publisher/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/port/publisher/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/util/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/util/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/util/clock/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/RTC/util/clock/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/jp/go/aist/rtm/class-use/*
 /usr/share/openrtm-1.2/doc/java/JavaDocEn/*
```

### openrtp
openrtpでは大量のファイルがインストールされるため、ここではリストしません。必要に応じて
```
 $ dpkg -L openrtp
```
と入力して各自での確認をしてください。



