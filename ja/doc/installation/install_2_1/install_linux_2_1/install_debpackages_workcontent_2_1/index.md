---
layout: page
title: openrtm-aist-2.1 debパッケージの詳しい内容
---

<!-- OpenRTM-aist-2.1 debパッケージの詳しい内容 -->

#contents

## OpenRTM-2.1 debパッケージの詳しい内容

各パッケージの内容は以下の通りです。

### openrtm2
openrtm2 にはランタイムライブラリとコマンド群が含まれています。

- コマンド
```
 /usr/bin/openrtmNames
 /usr/bin/rtcd2
 /usr/bin/rtcprof2
 /usr/bin/rtm2-config
```

- 設定ファイルサンプルなど
```
 /usr/etc/http/rtc.http.conf
 /usr/etc/http/rtc.https.conf
 /usr/etc/http/rtc.ws.conf
 /usr/etc/http/rtc.wss.conf
 /usr/etc/logger/rtc.fluentbit_stream.conf
 /usr/etc/rtc.names.http.conf
 /usr/etc/ssl/rtc.ssl.conf
 /usr/etc/transport/rtc.ros2.ssl.conf
```


- ライブラリなど
```
 /usr/lib/x86_64-linux-gnu/libRTC2.a
 /usr/lib/x86_64-linux-gnu/libRTC2.so.2.1.0
 中略
 /usr/lib/x86_64-linux-gnu/librtmCamera2.so
 /usr/lib/x86_64-linux-gnu/librtmManipulator2.so
 中略
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/ec/LogicalTimeTriggeredEC.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/local_service/FileNameservice.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/logger/FluentBit.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/sdo/ComponentObserverConsumer.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/sdo/ExtendedFsmServiceProvider.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/sdo/LoggerConsumer.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/ssl/SSLTransport.so
```

### openrtm2-naming
ネームサーバを起動 

```
 /usr/bin/rtm2-naming
```

### openrtm2-dev 
openrtm2-devには、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/rtm2-skelwrapper
```

- ヘッダなど
```
 /usr/include/coil-2.1/coil/Affinity.h
 /usr/include/coil-2.1/coil/Async.h
 中略
 /usr/include/openrtm-2.1/rtm/BufferBase.h
 /usr/include/openrtm-2.1/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-2.1/rtm/config_rtc.h
 /usr/include/openrtm-2.1/rtm/ext/FastRTPSMessageInfo.h
 /usr/include/openrtm-2.1/rtm/ext/ROSMessageInfo.h
 /usr/include/openrtm-2.1/rtm/idl/BasicDataType.hh 
 /usr/include/openrtm-2.1/rtm/idl/BasicDataTypeSkel.h
 中略
 /usr/include/openrtm-2.1/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-2.1/rtm/version.h
```

- ライブラリ・その他
```
 /usr/lib/x86_64-linux-gnu/cmake/openrtm-2.1/OpenRTMConfig.cmake
 /usr/lib/x86_64-linux-gnu/cmake/openrtm-2.1/OpenRTMConfigVersion.cmake
 /usr/share/openrtm-2.1/py_helper/skel_wrapper.py
 /usr/share/openrtm-2.1/py_helper/yat.py
```

### openrtm2-example
openrtm2-example にはスタンドアロン RTC、ローダブル RTC それぞれのサンプルが含まれています。

- サンプル(スタンドアロンRTC)
```
 /usr/share/openrtm-2.1/components/c++/examples/CompositeComp
 /usr/share/openrtm-2.1/components/c++/examples/ConfigSampleComp
 中略
 /usr/share/openrtm-2.1/components/c++/examples/rtc.conf
```

- サンプル(ローダブルRTC)
```
 /usr/share/openrtm-2.1/components/c++/examples/rtc/ConfigSample.so
 /usr/share/openrtm-2.1/components/c++/examples/rtc/ConsoleIn.so
 中略
 /usr/share/openrtm-2.1/components/c++/examples/rtc/Throughput.so
```

### openrtm2-ros2-tp

ROS2通信機能ライブラリがインストールされます。

```
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/transport/FastRTPSTransport.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/transport/ROS2Transport.so
```

### openrtm2-ssm-tp

SSMとSSM通信機能ライブラリがインストールされます。

```
 /usr/bin/ssm-coordinator
 /usr/bin/ssm-date
 中略
 /usr/share/openrtm-2.1/transport/SSMTransport.so
```

### openrtm2-doc
openrtm2-doc には、日本語と英語のクラスリファレンス、IDL インターフェース定義リファレンスが含まれています。

- クラスリファレンス
```
 /usr/share/openrtm-2.1/doc/c++/ClassReference/html/BufferBase_8h.html
 /usr/share/openrtm-2.1/doc/c++/ClassReference/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.1/doc/c++/ClassReference/html/structSDOPackage_1_1Organization__impl_1_1sdo__id.html
```

- IDL リファレンス
```
 /usr/share/openrtm-2.1/doc/idl/IDLReference/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.1/doc/idl/IDLReference/html/BasicDataType_8idl_dep_incl.map
 中略
 /usr/share/openrtm-2.1/doc/idl/IDLReference/html/unionSDOPackage_1_1Numeric.html
```

- クラスリファレンス(英語)
```
 /usr/share/openrtm-2.1/doc/c++/ClassReference-en/html/BufferBase_8h.html
 /usr/share/openrtm-2.1/doc/c++/ClassReference-en/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.1/doc/C++/ClassReference-en/html/version_8h_source.html
```

- IDL リファレンス(英語)
```
 /usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/BasicDataType_8idl__dep__incl.map
 中略
 /usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
```

### openrtm2-idl

- idlファイルなど
```
 /etc/profile.d/openrtm2-idl.sh
 /usr/include/openrtm-2.1/rtm/idl/BasicDataType.idl
 /usr/include/openrtm-2.1/rtm/idl/CameraCommonInterface.idl
 中略
 /usr/include/openrtm-2.1/rtm/idl/SharedMemory.idl
 /usr/share/openrtm-2.1/idl/BasicDataType.idl
 /usr/share/openrtm-2.1/idl/CameraCommonInterface.idl
 中略
 /usr/share/openrtm-2.1/idl/SharedMemory.idl
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
 /usr/share/openrtm-2.1/components/python3/__init__.py
 /usr/share/openrtm-2.1/components/python3/component.conf
 /usr/share/openrtm-2.1/components/python3/rtcd.conf
 /usr/share/openrtm-2.1/components/python3/AutoControl/*
 /usr/share/openrtm-2.1/components/python3/AutoTest/*
 /usr/share/openrtm-2.1/components/python3/CSPSample/*
 /usr/share/openrtm-2.1/components/python3/CSPSelectSample/*
 /usr/share/openrtm-2.1/components/python3/CSPStaticFsmSample/*
 /usr/share/openrtm-2.1/components/python3/Composite/*
 /usr/share/openrtm-2.1/components/python3/ConfigSample/*
 /usr/share/openrtm-2.1/components/python3/ExtTrigger/*
 /usr/share/openrtm-2.1/components/python3/MobileRobotCanvas/*
 /usr/share/openrtm-2.1/components/python3/SeqIO/*
 /usr/share/openrtm-2.1/components/python3/Serializer/*
 /usr/share/openrtm-2.1/components/python3/SimpleIO/*
 /usr/share/openrtm-2.1/components/python3/SimpleService/*
 /usr/share/openrtm-2.1/components/python3/Slider_and_Motor/*
 /usr/share/openrtm-2.1/components/python3/Throughput/*
 /usr/share/openrtm-2.1/components/python3/TkJoyStick/
 /usr/share/openrtm-2.1/components/python3/TkLRFViewer/*
```


### openrtm2-java

```
 /etc/profile.d/openrtm-java.sh
 /usr/bin/rtcd2_java
 /usr/bin/rtcprof2_java
 /usr/share/openrtm-2.1/jar/License.txt
 /usr/share/openrtm-2.1/jar/LogicalTimeTriggeredEC.jar
 /usr/share/openrtm-2.1/jar/NameserviceFile.jar
 /usr/share/openrtm-2.1/jar/OpenRTM-aist-2.1.0.jar
 /usr/share/openrtm-2.1/jar/commons-cli-1.1.jar
 /usr/share/openrtm-2.1/jar/jna-4.2.2.jar
 /usr/share/openrtm-2.1/jar/jna-platform-4.2.2.jar
 /usr/share/openrtm-2.1/jar/rtcd.jar
 /usr/share/openrtm-2.1/jar/rtcprof.jar
```

### openrtm2-java-example

Java版サンプルRTC、Classファイル、ソースファイル、起動スクリプト
```
 /usr/share/openrtm-2.1/components/java/* 
 /usr/share/openrtm-2.1/components/java/RTMExamples/AutoTest/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/Composite/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/ConfigSample/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/ExtTrigger/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/Fsm/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/GUIIn/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/MyService.idl
 /usr/share/openrtm-2.1/components/java/RTMExamples/SeqIO/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/SimpleIO/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/SimpleService/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/SinCosOut/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/StaticFsm/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/Throughput/*
 /usr/share/openrtm-2.1/components/java/RTMExamples/TopicTest/*
```

### openrtm2-java-doc

openrtm2-java-doc には、日本語と英語のクラスリファレンスが含まれています。

```
 /usr/share/openrtm-2.1/doc/java/JavaDoc/OpenRTM/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDoc/RTC/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDoc/RTM/class-use/*
 中略
 /usr/share/openrtm-2.1/doc/java/JavaDoc/jp/go/aist/rtm/Constants.html
 /usr/share/openrtm-2.1/doc/java/JavaDoc/jp/go/aist/rtm/RTC/buffer/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDoc/jp/go/aist/rtm/RTC/executionContext/class-use/*
 中略
 /usr/share/openrtm-2.1/doc/java/JavaDocEn/OpenRTM/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDocEn/RTC/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDocEn/RTM/class-use/*
```



### openrtp2
openrtpでは大量のファイルがインストールされるため、ここではリストしません。必要に応じて
```
 $ dpkg -L openrtp2
```
と入力して各自での確認をしてください。
