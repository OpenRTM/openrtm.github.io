---
layout: page
title: fedoraへのインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: Fedoraへのインストール -->
現在、1.2系のOpenRTM-aistはFedoraの対応が不完全です。よって、本ページの情報はあくまでも参考情報として使用してください。

C++版OpenRTM-aistはFedora Linuxで利用可能なRPMパッケージが提供されています。
対応しているFedora Linuxのバージョンは、ダウンロードページから確認できます。
Fedora Linuxへの対応およびそのバージョンは、予告なしに変更または停止されることがありますので、あらかじめご了承ください。

Fedora Linuxへのインストールの方法には大きく分けて以下の二種類のインストール方法があります。
- openrtm.orgが提供する一括インストールスクリプトを使用
- yumパッケージマネージャを使用

#contents

## 一括インストール・スクリプト

openrtm.orgが提供するインストール・スクリプト**pkg_install_fedora.sh**をダウンロードページからダウンロードし、root権限で実行します。このスクリプトは、必要なパッケージを順次yumを用いてインストールしていきます。

OpenRTM-aistを開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。オプションを指定することで、目的に合わせたパッケージをインストールできるので、初めてOpenRTM-aistをインストールしてみる方にもソースをコンパイルしてみる方にも推奨します。

一括インストールスクリプトは、ダウンロードした後、ダウンロード先ディレクトリに移動し、
```
 $ sudo sh pkg_install_fedora.sh -l c++ --yes
```
でインストールできます。

一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種類につきましては、[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)のページをご確認ください。<!-- //英語版は/node/6990-->

## OpenRTPのインストール
一般的なFedora環境での開発にはRTC BuilderやRTSystem Editorを使用しますが、その場合にはOpenRTPが必要ですので、一括インストールスクリプトを用いてOpenRTPをインストールしてください。Fedoraではpkg_install_fedora.shが置いてあるディレクトリで
```
 $ sudo sh pkg_install_fedora.sh -l openrtp --yes
```
と入力するとOpenRTPをインストールできます。

## JDK8のインストール

OpenRTP(RTSystem EditorやRTC Builderなど)の実行にはJDK8相当のJava環境が必要です。現時点でFedoraの環境では、一括インストールスクリプトがFedoraのrpmリポジトリよりOpenJDK8をインストールします。他のJDK8をインストールしたい場合は下記のリンクを参照してください。
- [JDK8のインストール]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

## yumを用いる方法

### /etc/yum.repos.d/openrtm.repoの作成

openrtm.orgではyumから利用可能なパッケージリポジトリを提供しています。
ただし、デフォルトのパッケージリポジトリには含まれていませんので、yumの設定を変更する必要があります。

以下のような設定を記録したファイル**/etc/yum.repos.d/openrtm.repo**を作成しておきます。作成には通常root権限が必要です。

```
 [openrtm]
 name=Fedora $releasever - $basearch
 failovermethod=priority
 baseurl=http://openrtm.org/pub/Linux/Fedora/releases/$releasever/Fedora/$basearch/os/Packages
 enabled=1
 gpgcheck=0
 gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora file:///etc/pki/rpm-gpg/RPM-GPG-KEY
```
<div align="center"><strong>/etc/yum.repos.d/openrtm.repo</strong></div>

### yumによるインストール

openrtm.repoを作成したら、次の手順でインストールを行います。
途中、いくつかの応答を求められるので、**y**を入力しながら完了させます。

```
 $ sudo yum install gcc-c++ python
 $ sudo yum install omniORB omniORB-devel omniORB-doc omniORB-servers omniORB-utils
 $ sudo yum install OpenRTM-aist OpenRTM-aist-devel OpenRTM-aist-doc OpenRTM-aist-example OpenRTP
```

## インストールの確認

最後に以下のコマンドでインストールの確認をします。

```
 $ rpm -qa|grep OpenRT*
 OpenRTM-aist-1.2.0-0.fc29.x86_64
 OpenRTM-aist-devel-1.2.0-0.fc29.x86_64
 OpenRTM-aist-example-1.2.0-0.fc29.x86_64
 OpenRTM-aist-doc-1.2.0-0.fc29.x86_64
 OpenRTP-1.2.0-1.fc29.x86_64
```


## パッケージの詳細
各パッケージの内容は以下の通りです(64bit版Fedoraの場合)

### OpenRTM-aist
openrtm-aistにはランタイムライブラリとコマンド群が含まれています。

- サンプル設定ファイル
```
 /etc/rtc.conf.sample
```

- コマンド
```
 /usr/bin/rtcd
 /usr/bin/rtcprof
 /usr/bin/rtm-config
 /usr/bin/rtm-naming
```

- ライブラリ
```
 /usr/lib64/libRTC-1.2.0.so
 /usr/lib64/libRTC.a
 /usr/lib64/libRTC.la
 中略
 /usr/lib64/librtmManipulator.so.0.0.0
 /usr/lib64/openrtm-1.2/ec/FileNameservice.la
 /usr/lib64/openrtm-1.2/ec/FileNameservice.so
 中略
 /usr/lib64/openrtm-1.2/ec/RTPreemptEC.so.0.0.0
 /usr/lib64/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib64/openrtm-1.2/sdo/LoggerConsumer.la
 中略
 /usr/lib64/openrtm-1.2/sdo/LoggerConsumer.so.0.0.0
 /usr/lib64/openrtm-1.2/ssl/SSLTransport.la
 /usr/lib64/openrtm-1.2/ssl/SSLTransport.so
 /usr/lib64/openrtm-1.2/ssl/SSLTransport.so.0
 /usr/lib64/openrtm-1.2/ssl/SSLTransport.so.0.0.0
```


### OpenRTM-aist-devel
openrtm-aist-devには、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/coil-config
 /usr/bin/rtc-template
 /usr/bin/rtm-skelwrapper
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
 /usr/include/openrtm-1.2/rtm/version.txt
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
```

- IDL およびスタブ・スケルトン

```
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserver.idl
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserverConsumer.h
 中略
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserverStub.h
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredEC.hh
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredEC.idl
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredECDynSK.cc
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredECSK.cc
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserver.hh
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserver.idl
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserverDynSK.cc
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserverSK.cc
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.hh
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.idl
 中略
 /usr/include/openrtm-1.2/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-1.2/rtm/idl/device_interfaces/AIO.idl
 /usr/include/openrtm-1.2/rtm/idl/device_interfaces/ActArray.idl
 中略
 /usr/include/openrtm-1.2/rtm/idl/device_interfaces/Ranger.idl
```

- ライブラリなど

```
 /usr/lib64/openrtm-1.2/cmake/OpenRTMConfig.cmake
 /usr/lib64/openrtm-1.2/py_helper/README_gen.py
 /usr/lib64/openrtm-1.2/py_helper/cxx_gen.py
 中略
 /usr/lib64/openrtm-1.2/py_helper/yat.py
 /usr/lib64/pkgconfig/libcoil.pc
 /usr/lib64/pkgconfig/openrtm-aist.pc
```

### OpenRTM-aist-doc
openrtm-aist-docには、日本語と英語のクラスリファレンス、IDLインターフェース定義リファレンスが含まれています。

- クラスリファレンス
```
 /usr/share/openrtm-1.2/doc/C++/ClassReference/html/Affinity-8h.html
 /usr/share/openrtm-1.2/doc/C++/ClassReference/html/Affinity_8h__dep__incl.map
 中略
 /usr/share/openrtm-1.2/doc/C++/ClassReference/html/version_8h_source.html
```

- IDL リファレンス
```
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/BasicDataType_8idl.html
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/BasicDataType_8idl__dep__incl.map
 中略
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/unionSDOPackage_1_1Numeric.html
```

- クラスリファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/C++/ClassReference-en/html/Affinity-8h.html
 /usr/share/openrtm-1.2/doc/C++/ClassReference-en/html/Affinity_8h__dep__incl.map
 中略
 /usr/share/openrtm-1.2/doc/C++/ClassReference-en/html/version_8h_source.html
```

- IDL リファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/BasicDataType_8idl__dep__incl.map
 中略
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
```


### OpenRTM-aist-example
openrtm-aist-exampleにはスタンドアロンRTC、ローダブルRTCそれぞれのサンプルと、サンプルRTCのソースが含まれています。

- サンプル(スタンドアロンRTC)
```
 /usr/share/openrtm-1.2/components/c++/examples/Composite
 /usr/share/openrtm-1.2/components/c++/examples/ConfigSampleComp
 中略
 /usr/share/openrtm-1.2/components/c++/examples/ThroughputComp
 /usr/share/openrtm-1.2/components/c++/examples/component.conf
 /usr/share/openrtm-1.2/components/c++/examples/composite.conf
 中略
 /usr/share/openrtm-1.2/components/c++/examples/rtc.conf
```

- サンプル(ローダブルRTC)
```
 /usr/share/openrtm-1.2/components/c++/examples/rtc/ConfigSample.a
 /usr/share/openrtm-1.2/components/c++/examples/rtc/ConfigSample.la
 /usr/share/openrtm-1.2/components/c++/examples/rtc/Throughput.so.0.0.0
```

- ソース
```
 /usr/share/openrtm-1.2/components/c++/examples/src/Composite/Composite.cpp
 /usr/share/openrtm-1.2/components/c++/examples/src/Composite/Controller.cpp
 中略
 /usr/share/openrtm-1.2/components/c++/examples/src/Composite/rtc.conf
 /usr/share/openrtm-1.2/components/c++/examples/src/ConfigSample/ConfigSample.cpp
 /usr/share/openrtm-1.2/components/c++/examples/src/ConfigSample/ConfigSample.h
 中略
 /usr/share/openrtm-1.2/components/c++/examples/src/ConfigSample/rtc.conf
 /usr/share/openrtm-1.2/components/c++/examples/src/ExtTrigger/ConnectorComp.cpp
 /usr/share/openrtm-1.2/components/c++/examples/src/ExtTrigger/ConsoleIn.cpp
 中略k
 /usr/share/openrtm-1.2/components/c++/examples/src/ExtTrigger/rtc.conf
 /usr/share/openrtm-1.2/components/c++/examples/src/ExtTrigger/run.sh
 /usr/share/openrtm-1.2/components/c++/examples/src/SeqIO/Makefile.SeqIn
 /usr/share/openrtm-1.2/components/c++/examples/src/SeqIO/Makefile.SeqOut
 中略
 /usr/share/openrtm-1.2/components/c++/examples/src/SeqIO/rtc.conf
 /usr/share/openrtm-1.2/components/c++/examples/src/SimpleIO/ConnectorComp.cpp
 /usr/share/openrtm-1.2/components/c++/examples/src/SimpleIO/ConsoleIn.cpp
 中略
 /usr/share/openrtm-1.2/components/c++/examples/src/SimpleIO/run.sh
 /usr/share/openrtm-1.2/components/c++/examples/src/SimpleService/Makefile.MyServiceConsumer
 /usr/share/openrtm-1.2/components/c++/examples/src/SimpleService/Makefile.MyServiceProvider 
 中略
 /usr/share/openrtm-1.2/components/c++/examples/src/SimpleService/rtc.conf
 /usr/share/openrtm-1.2/components/c++/examples/src/Throughput/CMakeLists.txt
 /usr/share/openrtm-1.2/components/c++/examples/src/Throughput/Throughput.cpp
 中略
 /usr/share/openrtm-1.2/components/c++/examples/src/Throughput/run.sh
```

- テンプレート
```
 /usr/share/openrtm-1.2/components/c++/examples/templates/AIO.xml
 /usr/share/openrtm-1.2/components/c++/examples/templates/ActArray.xml
 中略
 /usr/share/openrtm-1.2/components/c++/examples/templates/VelocityControl3D.xml
```

### OpenRTP
OpenRtpでは大量のファイルがインストールされるため、ここではリストしません。必要に応じて
```
 $ rpm -ql  OpenRTP
```
と入力して各自での確認をしてください。




