---
layout: page
title: raspberry pi osへのインストール
---

<!-- Title: Raspberry Pi OSへのインストール -->

#contents

## 対応バージョン

現在パッケージが用意されている Raspberry Pi OS のバージョンは

- Bookworm (64bit)

です。

## SDカードの準備

OSイメージの書き込みは、公式サイトでダウンロードできるツール、Raspberry Pi Imager を使うのが便利です。<br>
https://www.raspberrypi.com/software/


下記を選択してダウンロード、書き込みが可能です。
- ベースのDebian GNU/Linuxのバージョン (最新 / Legacy)
- GUI の有無 (Desktop / Lite)
- システムアーキテクチャー (32-bit / 64-bit)

## 2.1系での変更点

新しく [SSM通信機能]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ssm_comm_use) をインストールできるようになりました。<br>
SSMライブラリを静的リンクしているので、別途SSMをインストール必要はありません。openrtm2-ssm-tpのdebパッケージで下記がインストールされます。

```
 usr/
 ├── bin
 │   ├── killssm
 │   ├── lsssm
 │   ├── psssm
 │   ├── ssm-advance-player
 │   ├── ssm-coordinator
 │   ├── ssm-date
 │   ├── ssm-graph
 │   ├── ssm-logger
 │   ├── ssm-monitor
 │   ├── ssm-player
 │   ├── ssm-proxy
 │   ├── ssm-transporter
 │   └── topssm
 ├── etc
 │   └── transport
 │       └── rtc.ssm.conf
 └── share
     └── openrtm-2.1
         └── transport
             └── SSMTransport.so
```

この機能は次の項で説明している「一括インストールスクリプト」をオプション無しで実行した場合はインストールされません。<br>
オプションとして「-l c++ --ssm」と指定するとインストールできます。 --help で確認できます。


## 一括インストールスクリプト

2.1系のインストールは、下記をシェルプロンプトに貼り付けて実行してください。　C++版、 Python版、 Java版、 rtshell、JDK8 がインストールされます。　スクリプトはローカルに保存されません。<br>
※Javaの複数バージョンがインストールされても、Java８ 使用に切り替わっています。 <br>


```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh)
```

この実行により以下のパッケージがインストールされます。

```
 $ dpkg -l | grep openrt
 ii  openrtm2:arm64                         2.1.0-0             arm64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:arm64                  2.1.0-0              arm64       OpenRTM-aist headers for development
 ii  openrtm2-doc                             2.1.0-0              all             Documentation for openrtm2
 ii  openrtm2-example:arm64            2.1.0-0             arm64       OpenRTM-aist examples
 ii  openrtm2-idl:arm64                     2.1.0-0             arm64       OpenRTM-aist idls for development
 ii  openrtm2-java:arm64                  2.1.0-0             arm64       OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-example:arm64     2.1.0-0            arm64        OpenRTM-aist-Java examples
 ii  openrtm2-naming:arm64              2.1.0-0            arm64        OpenRTM-aist name server launcher
 ii  openrtm2-python3                       2.1.0-0            arm64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-example          2.1.0-0            arm64        OpenRTM-aist-Python examples
```

デフォルトのpipバージョン利用で、 rtshellのインストールに失敗します。<br>
インストールスクリプトが表示している黄文字のメッセージに従い、　/etc/pip.conf へ（存在しなければ 新規作成して）下記を追記して下さい。

```
 $ vi /etc/pip.conf
 [global]
 break-system-packages = true
```

上記設定後に再度インストールスクリプトを実行するとrtshellをインストールできます。

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python        2.1.0
 rtctree-aist                       4.2.5
 rtshell-aist                       4.2.10
 rtsprofile-aist                    4.1.6
```

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。 help は下記で確認できます。

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh) --help
```

## パッケージの詳細
各パッケージの内容は以下の通りです。
### openrtm2
openrtm-aistにはランタイムライブラリとコマンド群が含まれています。

- コマンド
```
 /usr/bin/openrtmNames
 /usr/bin/rtcd2
 /usr/bin/rtcprof2
 /usr/bin/rtm2-config
```

- 設定ファイルサンプル
```
 /usr/etc/rtc.conf.sample2
 /usr/etc/rtc.names.ssl.conf
 /usr/etc/ssl/rtc.ssl.conf
 /usr/lib/aarch64-linux-gnu/pkgconfig/openrtm2.pc
```


- ライブラリなど
```
 /usr/lib/aarch64-linux-gnu/libRTC2.a
 /usr/lib/aarch64-linux-gnu/libRTC2.so.2.1.0
 中略
 /usr/lib/aarch64-linux-gnu/librtmCamera2.so
 /usr/lib/aarch64-linux-gnu/librtmManipulator2.so
 中略
 /usr/lib/aarch64-linux-gnu/openrtm-2.1/ec/LogicalTimeTriggeredEC.so
 /usr/lib/aarch64-linux-gnu/openrtm-2.1/local_service/FileNameservice.so
 /usr/lib/aarch64-linux-gnu/openrtm-2.1/sdo/ComponentObserverConsumer.so
 /usr/lib/aarch64-linux-gnu/openrtm-2.1/sdo/ExtendedFsmServiceProvider.so
 /usr/lib/aarch64-linux-gnu/openrtm-2.1/sdo/LoggerConsumer.so
 /usr/lib/aarch64-linux-gnu/openrtm-2.1/ssl/SSLTransport.so
 中略
 /usr/lib/aarch64-linux-gnu/openrtm-2.1/sdo/LoggerConsumer.so
```


### openrtm2-dev
開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/rtm2-skelwrapper
```

- ヘッダ
```
 /usr/include/coil-2.1/coil/Affinity.h
 /usr/include/coil-2.1/coil/Async.h
 中略
 /usr/include/openrtm-2.1/rtm/BufferBase.h
 /usr/include/openrtm-2.1/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-2.1/rtm/config_rtc.h
 /usr/include/openrtm-2.1/rtm/idl/BasicDataType.hh 
 /usr/include/openrtm-2.1/rtm/idl/BasicDataTypeSkel.h
 中略
 /usr/include/openrtm-2.1/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-2.1/rtm/version.h
```

- ライブラリ・その他
```
 /usr/lib/aarch64-linux-gnu/cmake/openrtm-2.1/OpenRTMConfig.cmake
 /usr/lib/aarch64-linux-gnu/cmake/openrtm-2.1/OpenRTMConfigVersion.cmake
 /usr/share/openrtm-2.1/py_helper/skel_wrapper.py
 /usr/share/openrtm-2.1/py_helper/yat.py
```

### openrtm2-idl
- idlファイルなど
```
 /usr/include/openrtm-2.1/rtm/idl/BasicDataType.idl
 /usr/include/openrtm-2.1/rtm/idl/CameraCommonInterface.idl
 中略
 /usr/include/openrtm-2.1/rtm/idl/SharedMemory.idl
 /usr/share/openrtm-2.1/idl/BasicDataType.idl
 /usr/share/openrtm-2.1/idl/CameraCommonInterface.idl
 中略
 /usr/share/openrtm-2.1/idl/SharedMemory.idl
```

### openrtm2-example
openrtm-aist-exampleにはスタンドアロンRTC、ローダブルRTCそれぞれのサンプルと、サンプルRTCのソースが含まれています。

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

### openrtm2-doc
openrtm-aist-docには、日本語と英語のクラスリファレンス、IDLインターフェース定義リファレンスが含まれています。

- クラスリファレンス
```
 /usr/share/openrtm-2.1/doc/c++/ClassReference/html/BufferBase_8h.html
 /usr/share/openrtm-2.1/doc/c++/ClassReference/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.1/doc/c++/ClassReference/html/structSDOPackage_1_1Organization__impl_1_1sdo__id.html
```

- IDLリファレンス
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

- IDLリファレンス(英語)
```
 /usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/BasicDataType_8idl__dep__incl.map
 中略
 /usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
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
