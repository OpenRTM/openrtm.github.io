---
layout: page
title: raspberry pi osへのインストール
---

<hr>
<!-- Title: Raspberry Pi OSへのインストール -->

#contents

## 対応バージョン

現在パッケージが用意されている Raspberry Pi OS のバージョンは

- Bullseye (32bit / 64bit)
- Bookworm (32bit / 64bit)

です。

## SDカードの準備

OSイメージの書き込みは、公式サイトでダウンロードできるツール、Raspberry Pi Imager を使うのが便利です。<br>
https://www.raspberrypi.com/software/


下記を選択してダウンロード、書き込みが可能です。
- ベースのDebian GNU/Linuxのバージョン (最新 / Legacy)
- GUI の有無 (Desktop / Lite)
- システムアーキテクチャー (32-bit / 64-bit)

## 2.0系での変更点

C++ は 1.2系と2.0系の共存が可能となりました。　ただし、1.2系は Buster(32bit) のみインストール可能です。 <br>
この対応で、インストールに関しては下記が変更となっています。

- 2.0系のdebパッケージ名を変更しました
- Python と Java は1.2系と2.0系の共存はできません
  - 一括インストールスクリプトを使用すれば、インストール済みの異なるバージョンを自動でアンインストールします
- 1.2系と2.0系の一括インストールスクリプトを分けました
  - 1.2系のインストール : pkg_install_raspbian.sh
  - 2.0系のインストール : openrtm2_install_raspbian.sh

また、インストールスクリプト（1.2系、2.0系どちらも）は、ダウンロードからインストールまでの一括処理に対応しました。

## 一括インストールスクリプト

2.0系のインストールは、下記をシェルプロンプトに貼り付けて実行してください。　C++版、 Python版、 Java版、 rtshell、JDK8（32-bit環境のみ） がインストールされます。　スクリプトはローカルに保存されません。<br>
※32-bit環境ではスクリプトの実行でJavaの複数バージョンがインストールされても、Java８ 使用に切り替わっています。 <br>
※64-bit環境では下記ををご覧ください。 <br>
- [JDK8のインストール・リポジトリからのパッケージ入手以外の方法]({{ site.baseurl }}/ja/doc/installation/common/install_jdk8#toc9)

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh)
```

この実行により以下のパッケージがインストールされます。(32bit版の場合）

```
 $ dpkg -l | grep openrt
 ii  openrtm2:armhf                     2.0.1-0                         armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:armhf               2.0.1-0                         armhf        OpenRTM-aist headers for development
 ii  openrtm2-doc                         2.0.1-0                         all          Documentation for openrtm2
 ii  openrtm2-example:armhf        2.0.1-0                         armhf        OpenRTM-aist examples
 ii  openrtm2-idl:armhf                 2.0.1-0                         armhf        OpenRTM-aist idls for development
 ii  openrtm2-java:armhf               2.0.1-0                        armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-doc                  2.0.1-0                        all          Documentation for openrtm2-java
 ii  openrtm2-java-example:armhf  2.0.1-0                       armhf        OpenRTM-aist-Java examples
 ii  openrtm2-python3                  2.0.1-0                         armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-doc            2.0.1-0                         all          Documentation for openrtm2-python3
 ii  openrtm2-python3-example     2.0.1-0                         armhf        OpenRTM-aist-Python examples
```

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python 2.0.1
 rtctree-aist        4.2.3
 rtshell-aist         4.2.9
 rtsprofile-aist     4.1.5
```

## パッケージの詳細
各パッケージの内容は以下の通りです。
### openrtm2
openrtm-aistにはランタイムライブラリとコマンド群が含まれています。

- コマンド
```
 /usr/bin/rtcd2
 /usr/bin/rtcprof2
 /usr/bin/rtm2-config
 /usr/bin/rtm2-naming
```

- 設定ファイルサンプル
```
 /usr/etc/rtc.conf.sample2
 /usr/etc/rtc.names.ssl.conf
 /usr/etc/ssl/rtc.ssl.conf
 /usr/lib/arm-linux-gnueabihf/pkgconfig/openrtm2.pc
```


- ライブラリなど
```
 /usr/lib/arm-linux-gnueabihf/libRTC2.a
 /usr/lib/arm-linux-gnueabihf/libRTC2.so.2.0.0
 中略
 /usr/lib/arm-linux-gnueabihf/librtmCamera2.so
 /usr/lib/arm-linux-gnueabihf/librtmManipulator2.so
 中略
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/ec/LogicalTimeTriggeredEC.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/local_service/FileNameservice.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/sdo/ComponentObserverConsumer.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/sdo/ExtendedFsmServiceProvider.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/sdo/LoggerConsumer.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/ssl/SSLTransport.so
 中略
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/sdo/LoggerConsumer.so.0.0.0
 /usr/lib/libfluent-bit.so
```

### openrtm2-dev
開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/rtm2-skelwrapper
```

- ヘッダ
```
 /usr/include/coil-2.0/coil/Affinity.h
 /usr/include/coil-2.0/coil/Async.h
 中略
 /usr/include/openrtm-2.0/rtm/BufferBase.h
 /usr/include/openrtm-2.0/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-2.0/rtm/config_rtc.h
 /usr/include/openrtm-2.0/rtm/idl/BasicDataType.hh 
 /usr/include/openrtm-2.0/rtm/idl/BasicDataTypeSkel.h
 中略
 /usr/include/openrtm-2.0/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-2.0/rtm/version.h
```

- ライブラリ・その他
```
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/cmake/OpenRTMConfig.cmake
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/cmake/OpenRTMConfigVersion.cmake
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/py_helper/skel_wrapper.py
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/py_helper/yat.py
```

### openrtm2-idl
- idlファイルなど
```
 /etc/profile.d/openrtm2-idl.sh
 /usr/include/openrtm-2.0/rtm/idl/BasicDataType.idl
 /usr/include/openrtm-2.0/rtm/idl/CameraCommonInterface.idl
 中略
 /usr/include/openrtm-2.0/rtm/idl/SharedMemory.idl
 /usr/share/openrtm-2.0/idl/BasicDataType.idl
 /usr/share/openrtm-2.0/idl/CameraCommonInterface.idl
 中略
 /usr/share/openrtm-2.0/idl/SharedMemory.idl
```

### openrtm2-example
openrtm-aist-exampleにはスタンドアロンRTC、ローダブルRTCそれぞれのサンプルと、サンプルRTCのソースが含まれています。

- サンプル(スタンドアロンRTC)
```
 /usr/share/openrtm-2.0/components/c++/examples/CompositeComp
 /usr/share/openrtm-2.0/components/c++/examples/ConfigSampleComp
 中略
 /usr/share/openrtm-2.0/components/c++/examples/rtc.conf
```

- サンプル(ローダブルRTC)
```
 /usr/share/openrtm-2.0/components/c++/examples/rtc/ConfigSample.so
 /usr/share/openrtm-2.0/components/c++/examples/rtc/ConsoleIn.so
 中略
 /usr/share/openrtm-2.0/components/c++/examples/rtc/Throughput.so
```

### openrtm2-doc
openrtm-aist-docには、日本語と英語のクラスリファレンス、IDLインターフェース定義リファレンスが含まれています。

- クラスリファレンス
```
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/BufferBase_8h.html
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/structSDOPackage_1_1Organization__impl_1_1sdo__id.html
```

- IDLリファレンス
```
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/BasicDataType_8idl_dep_incl.map
 中略
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/unionSDOPackage_1_1Numeric.html
```

- クラスリファレンス(英語)
```
 /usr/share/openrtm-2.0/doc/c++/ClassReference-en/html/BufferBase_8h.html
 /usr/share/openrtm-2.0/doc/c++/ClassReference-en/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/C++/ClassReference-en/html/version_8h_source.html
```

- IDLリファレンス(英語)
```
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/BasicDataType_8idl__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
```

### openrtm2-python3

- コマンド
```
 /usr/bin/rtcd2_python3
 /usr/bin/rtcprof2_python3
```

- OpenRTM-aist 本体の Python モジュール
```
 /usr/lib/python3/dist-packages/OpenRTM_aist/* 
```
- OpenRTM-aist用Python検索パスファイル
```
 /usr/lib/python3/dist-packages/OpenRTM-aist.pth 
```
- ユーティリティ
```
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/__init__.py
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtc-template/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcd/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcprof/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtm-naming/*
```

### openrtm2-python3-example

```
 /usr/share/openrtm-2.0/components/python3/__init__.py
 /usr/share/openrtm-2.0/components/python3/component.conf
 /usr/share/openrtm-2.0/components/python3/rtcd.conf
 /usr/share/openrtm-2.0/components/python3/AutoControl/*
 /usr/share/openrtm-2.0/components/python3/AutoTest/*
 /usr/share/openrtm-2.0/components/python3/CSPSample/*
 /usr/share/openrtm-2.0/components/python3/CSPSelectSample/*
 /usr/share/openrtm-2.0/components/python3/CSPStaticFsmSample/*
 /usr/share/openrtm-2.0/components/python3/Composite/*
 /usr/share/openrtm-2.0/components/python3/ConfigSample/*
 /usr/share/openrtm-2.0/components/python3/ExtTrigger/*
 /usr/share/openrtm-2.0/components/python3/MobileRobotCanvas/*
 /usr/share/openrtm-2.0/components/python3/SeqIO/*
 /usr/share/openrtm-2.0/components/python3/Serializer/*
 /usr/share/openrtm-2.0/components/python3/SimpleIO/*
 /usr/share/openrtm-2.0/components/python3/SimpleService/*
 /usr/share/openrtm-2.0/components/python3/Slider_and_Motor/*
 /usr/share/openrtm-2.0/components/python3/Throughput/*
 /usr/share/openrtm-2.0/components/python3/TkJoyStick/
 /usr/share/openrtm-2.0/components/python3/TkLRFViewer/*
```

### openrtm2-python3-doc
英語・日本語のクラスリファレンスをインストールします。

- クラスリファレンス
```
 /usr/share/openrtm-2.0/doc/python3/ClassReference-en/html/_async_8py.html
 /usr/share/openrtm-2.0/doc/python3/ClassReference-en/html/_buffer_base_8py.html
 中略
 /usr/share/openrtm-2.0/doc/python3/ClassReference-jp/html/_async_8py.html
 /usr/share/openrtm-2.0/doc/python3/ClassReference-jp/html/_buffer_base_8py.html
 /usr/share/openrtm-2.0/doc/python3/ClassReference-jp/html/_buffer_status_8py.html
 以下略
```

### openrtm2-java

```
 /etc/profile.d/openrtm-java.sh
 /usr/bin/rtcd2_java
 /usr/bin/rtcprof2_java
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/License.txt
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/LogicalTimeTriggeredEC.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/NameserviceFile.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/OpenRTM-aist-2.0.1.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/commons-cli-1.1.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/jna-4.2.2.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/jna-platform-4.2.2.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/rtcd.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/rtcprof.jar
```

### openrtm2-java-example

Java版サンプルRTC、Classファイル、ソースファイル、起動スクリプト

```
 /usr/share/openrtm-2.0/components/java/* 
 /usr/share/openrtm-2.0/components/java/RTMExamples/AutoTest/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/Composite/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/ConfigSample/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/ExtTrigger/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/Fsm/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/GUIIn/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/GUIIn/control/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/GUIIn/model/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/GUIIn/view/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/MyService.idl
 /usr/share/openrtm-2.0/components/java/RTMExamples/SeqIO/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/SeqIO/view/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/SimpleIO/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/SimpleService/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/SinCosOut/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/StaticFsm/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/Throughput/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/TopicTest/*
```




