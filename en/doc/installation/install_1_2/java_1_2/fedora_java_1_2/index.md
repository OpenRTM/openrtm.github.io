---
layout: page
title: 
---
<br>
<a>No English version available.
</a>

<!-- Title: Fedoraへのインストール -->
Java版OpenRTM-aistはFedora Linuxで利用可能なRPMパッケージが提供されています。
対応しているFedora Linuxのバージョンは、ダウンロードページから確認できます。
Fedora Linuxへの対応およびそのバージョンは、予告なしに変更または停止されることがありますので、あらかじめ了承ください。

Fedora Linuxへのインストールの方法には大きく分けて以下の二種類のインストール方法があります。
- openrtm.orgが提供する一括インストールスクリプトを使用
- yumパッケージマネージャを使用

#contents

## 一括インストール・スクリプト

openrtm.orgが提供するインストール・スクリプト**pkg_install_fedora.sh**をダウンロードページからダウンロードし、root権限で実行します。
このスクリプトは、必要なパッケージを順次yumを用いてインストールしていきます。

OpenRTM-aistを開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。
オプションを指定することで、目的に合わせたパッケージをインストールできるようになったので、
初めてOpenRTM-aistをインストールしてみる方にもソースをコンパイルしてみる方にも推奨します。

一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種類につきましては、「[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)」のページをご確認ください。

現状一括インストールスクリプトを-l javaオプションで使った場合、必要なOpenRTM-aistパッケージがインストールされないという問題が報告されています。以下の手順によりインストールしてください。
```
 sudo yum install OpenRTM-aist OpenRTM-aist-devel
```

## OpenRTPのインストール
一般的なUbuntu/Debian環境での開発にはRTC BuilderやRTSystem Editorを使用しますが、その場合にはOpenRTPが必要ですので、一括インストールスクリプトを用いてOpenRTPをインストールしてください。pkg_install_fedora.shが置いてあるディレクトリで
```
 $ sudo sh ./pkg_install_fedora.sh -l openrtp --yes
```
と入力するとOpenRTPをインストールできます。

## yumを使う方法

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
 $ sudo yum install OpenRTM-aist OpenRTM-aist-devel OpenRTM-aist-Java OpenRTM-aist-Java-doc OpenRTM-aist-Java-example
 $ sudo yum install OpenRTP
```

### 環境変数の設定
環境変数の設定が必要です。ホームディレクトリにある.bashrcに以下の行を付け加えてください。(64ビット版を使用する場合)
```
 export RTM_JAVA_ROOT=/usr/lib64/openrtｍ-1.2
```
この設定を有効にするためにはインストール作業終了後、再ログインしてください。
### JDK8について
Fedora用のOpenRTM-aist-Javaパッケージのインストールは自動的にFedoraの標準リポジトリよりOpenJDK8をインストールし、それを使用するJava環境として設定しますが、ライセンス条件やサポート条件のために他のJDKを使いたい場合は、以下のリンクを参照してください。
- [JDKのインストール]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)
### インストールの確認

最後に以下のコマンドでインストールの確認をします。

```
 # rpm -q OpenRTM-aist
 OpenRTM-aist-1.2.0-0.fcXX.x86_64
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

- 設定ファイルサンプル
```
 /etc/rtc.conf.sample
```

- ライブラリ
```
 /usr/lib64/libRTC-1.2.0.so
 /usr/lib64/libRTC.a
 中略
 /usr/lib64/librtmManipulator.so.0.0.0
 /usr/lib64/openrtm-1.2/ec/FileNameservice.la
 /usr/lib64/openrtm-1.2/ec/FileNameservice.so
 中略
 /usr/lib64/openrtm-1.2/ec/RTPreemptEC.so.0.0.0
 /usr/lib64/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib64/openrtm-1.2/sdo/LoggerConsumer.la
 /usr/lib64/openrtm-1.2/sdo/LoggerConsumer.so
 /usr/lib64/openrtm-1.2/sdo/LoggerConsumer.so.0
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

### OpenRTM-aist-Java
- コマンド
```
 /usr/bin/rtcd_java
 /usr/bin/rtcprof_java
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

### OpenRTM-aist-Java-example
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

### OpenRTM-aist-Java-doc
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
 $ rpm -ql OpenRTP
```
と入力して各自での確認をしてください。



