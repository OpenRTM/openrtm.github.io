---
layout: page
title: raspbianへのインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: Raspbianへのインストール -->

Java版のOpenRTM-aistは、Raspbianで利用可能なdebパッケージが提供されています。
対応しているディストリビューションのバージョンは、ダウンロードページで確認できます。
Raspbianへのサポートバージョンや対応の有無は、予告なしに変更されることがありますので、あらかじめご了承ください。

#contents

## JDK8のインストール
Java版OpenRTM-aistの使用にはJDK8相当のJava環境が必要です。以下のリンクを参照にJDK8を入手してインストールしてください。
- [JDK8のインストール]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

## 一括インストールスクリプト
openrtm.orgが提供するインストール・スクリプト**pkg_install_raspbian.sh**を指定のURLからダウンロードし、root権限で実行します。このスクリプトでは必要なパッケージを順次apt-getを用いてインストールしていきます。

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。

一括インストールスクリプトを用いると、ダウンロードした後、ダウンロード先ディレクトリに移動し、
```
 $ sudo sh pkg_install_raspbian.sh -l java --yes
```
でJava版OpenRTM-aistをインストールできます。

一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種類につきましては、「[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)」のページをご確認ください。


## rtshellのインストール
Raspbianの環境では現在OpenRTPの対応がありません。よってRaspianの環境では、ローカルでGUI(RTSystemEditor)を用いたRTCの制御ができません。RTCの制御を行うための方法としては、リモートで他の対応ホスト上でRTSystemEditorを起動してそこから制御を行うという方法と、ローカルでrtshellというツールを用いて制御を行うという方法があります。rtshellのインストールについては以下のリンクを参照してください。
[rtshellのインストール方法]({{ site.baseurl }}/en/doc/toolmanuals/rtshell/command_reference/rtstodot)

### インストールの確認
インストールを確認します。

```
 $ dpkg -l 'openrt*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
    状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリガ待ち/(T)トリガ保留
    / エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
    / 名前                            バージョン   アーキテクチ 説明
 +++-===============================-============-============-===============================================
 ii  openrtm-aist:armhf              1.2.1-0      armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-dev:armhf          1.2.1-0      armhf        OpenRTM-aist headers for development
 ii  openrtm-aist-idl:armhf          1.2.1-0      armhf        OpenRTM-aist idls for development
 ii  openrtm-aist-java:armhf         1.2.1-0      armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-java-doc           1.2.1-0      all          Documentation for openrtm-aist-java
 ii  openrtm-aist-java-example:armhf 1.2.1-0      armhf        OpenRTM-aist-Java examples
 ii  openrtm-aist-python             1.2.1-0      armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-python-example     1.2.1-0      armhf        OpenRTM-aist-Python examples
```

```
 $ pip show rtshell-aist
 Name: rtshell-aist
 Version: 4.2.2
 Summary: Shell commands for managing RT Components and RT Systems.
 Home-page: http://github.com/gbiggs/rtshell
 Author: Geoffrey Biggs and contributors
 Author-email: geoffrey.biggs@aist.go.jp
 License: LGPL3
 Location: /usr/local/lib/python2.7/dist-packages
 Requires: rtsprofile-aist, rtctree-aist
 Required-by:
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

### openrtm-aist-python
- コマンド
```
 /usr/bin/rtcd_python
 /usr/bin/rtcprof_python
```

- OpenRTM-aist 本体の Python モジュール
```
 usr/lib/python2.7/dist-packages/OpenRTM-aist/*
```

- OpenRTM-aist用Python検索パスファイル
```
 /usr/lib/python2.7/dist-packages/OpenRTM_aist.ph
```

- ユーティリティ
```
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/__init__.py
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtc-template/*
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtcd/*
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtcprof/*
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtm-naming/*
```
<!-- /usr/lib/python2.7/dist-packages/OpenRTM_aist_Python-1.2.0.egg-info -->

### openrtm-aist-python-example
```
 /usr/share/openrtm-1.2/components/python/__init__.py
 /usr/share/openrtm-1.2/components/python/rtcd.conf
 /usr/share/openrtm-1.2/components/python/components.conf
 /usr/share/openrtm-1.2/components/python/AutoControl/*
 /usr/share/openrtm-1.2/components/python/AutoTest/*
 /usr/share/openrtm-1.2/components/python/Composite/*
 /usr/share/openrtm-1.2/components/python/ConfigSample/*
 /usr/share/openrtm-1.2/components/python/ExtTrigger/*
 /usr/share/openrtm-1.2/components/python/MobileRobotCanvas/*
 /usr/share/openrtm-1.2/components/python/SeqIO/*
 /usr/share/openrtm-1.2/components/python/SimpleIO/*
 /usr/share/openrtm-1.2/components/python/SimpleService/*
 /usr/share/openrtm-1.2/components/python/Slider_and_Motor/*
 /usr/share/openrtm-1.2/components/python/Templates/*
 /usr/share/openrtm-1.2/components/python/Throughput/*
 /usr/share/openrtm-1.2/components/python/TkJoyStick/
 /usr/share/openrtm-1.2/components/python/TkLRFViewer/*
```

### openrtm-aist-python-doc
- クラスリファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/python/ClassReference-en/html/_async_8py.html
 /usr/share/openrtm-1.2/doc/python/ClassReference-en/html/_buffer_base_8py.html
 中略
 /usr/share/openrtm-1.2/doc/python/ClassReference-en/html/uuid_8py.html
```
- クラスリファレンス(日本語)
```
 /usr/share/openrtm-1.2/doc/python/ClassReference-jp/html/_async_8py.html
 /usr/share/openrtm-1.2/doc/python/ClassReference-jp/html/_buffer_base_8py.html
 中略
 /usr/share/openrtm-1.2/doc/python/ClassReference-jp/html/uuid_8py.html 
```

### rtshell
- コマンド用スクリプト
```
 /usr/local/bin/rtact
 /usr/local/bin/rtcat
 /usr/local/bin/rtcheck
 /usr/local/bin/rtcomp
 /usr/local/bin/rtcon
 /usr/local/bin/rtconf
 /usr/local/bin/rtcryo
 /usr/local/bin/rtdeact
 /usr/local/bin/rtdel
 /usr/local/bin/rtdis
 /usr/local/bin/rtdoc
 /usr/local/bin/rtexit
 /usr/local/bin/rtfind
 /usr/local/bin/rtfsm
 /usr/local/bin/rtinject
 /usr/local/bin/rtlog
 /usr/local/bin/rtls
 /usr/local/bin/rtmgr
 /usr/local/bin/rtprint
 /usr/local/bin/rtpwd
 /usr/local/bin/rtreset
 /usr/local/bin/rtresurrect
 /usr/local/bin/rtshell_post_install
 /usr/local/bin/rtstart
 /usr/local/bin/rtstodot
 /usr/local/bin/rtstop
 /usr/local/bin/rtteardown
 /usr/local/bin/rtvlog
 /usr/local/bin/rtwatch
```

- コマンド本体
```
 /usr/local/lib/python2.7/dist-packages/rtctree/*
 /usr/local/lib/python2.7/dist-packages/rtshell/*
 /usr/local/lib/python2.7/dist-packages/rtsprofile/*
```

- パッケージ情報
```
 /usr/local/lib/python2.7/dist-packages/rtctree_aist-4.2.0.egg-info/*
 /usr/local/lib/python2.7/dist-packages/rtshell_aist-4.2.2.dist-info/*
 /usr/local/lib/python2.7/dist-packages/rtsprofile_aist-4.1.2.dist-info/*
```



