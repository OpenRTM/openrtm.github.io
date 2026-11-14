---
layout: page

title: ubuntu/debianへのインストール
---
<br>
<a>No English version available.
</a>

<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="100;" align="right"></a></div>


C++版のOpenRTM-aistは、UbuntuやDebian GNU Linuxにおいて利用可能なdebパッケージが提供されて>います。
それぞれのリリースが対応しているOSのディストリビューション・バージョンは、ダウンロードペー>ジで確認できます。
Ubuntu/Debian GNU Linuxへのサポートバージョンや対応の有無は、予告なしに変更されることがあり
ますので、あらかじめご了承ください。

#contents

## 一括インストールスクリプト
openrtm.orgが提供するインストール・スクリプト**pkg_install_ubuntu.sh**または**pkg_install_debian.sh**を指定のURLからダウンロードし、root 権限で実行します。このスクリプトでは必要なパ>ッケージを順次apt-getを用いてインストールしていきます。

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。

一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種>類につきましては、「[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)」のページをご確認ください。<br>
<span style="color:red;">※最新バージョンが「1.2.2」である場合は、オプション指定で「1.2.1」>のインストール、「1.2.2」から「1.2.1」へのダウングレードができます。</span>;

一括インストールスクリプトは、ダウンロードした後、ダウンロード先ディレクトリに移動し、

Ubuntuの場合は
```
 $ sudo sh pkg_install_ubuntu.sh -l c++ --yes
```

Debianの場合はsuでroot権限を得た後に
```
 # sh pkg_install_debian.sh -l c++ --yes
```

でインストールできます。



## OpenRTPのインストール
一般的なUbuntu/Debian環境での開発にはRTC BuilderやRTSystem Editorを使用しますが、その場合に
はOpenRTPが必要ですので、一括インストールスクリプトを用いてOpenRTPをインストールしてくださ>い。Ubuntuではpkg_install_ubuntu.shが置いてあるディレクトリで

Ubuntuは:
```
 $ sudo sh pkg_install_ubuntu.sh -l openrtp --yes
```
Debianはsuでroot権限を得た後に:
```
 # sh pkg_install_debian.sh -l openrtp --yes
```

と入力するとOpenRTPをインストールできます。

## JDK8のインストール

OpenRTP(RTSystem EditorやRTC Builderなど)の実行にはJDK8相当のJava環境が必要です。(デフォル>トの環境でJDK8がインストールされている場合もありますが、Ubuntu 18.04ではJDK11がインストール
されているため、JDK8のインストールが必要です。)  JDK8の入手やインストールについては以下を参
照してください。
- [JDK8のインストール]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

### インストールの確認
インストールを確認します。

```
 $ dpkg -l 'openrt*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
    状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリ>ガ待ち/(T)トリガ保留
    / エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
    / 名前                     バージョン        アーキテクチャ    説明
 +++-========================-=================-+++-======================-================-
 ii  openrtm-aist:amd64     1.2.1-0          amd64            OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-dev:amd64 1.2.1-0          amd64            OpenRTM-aist headers for development
 ii  openrtm-aist-doc       1.2.1-0          all              Documentation for openrtm-aist
 ii  openrtm-aist-example:a 1.2.1-0          amd64            OpenRTM-aist examples
 ii  openrtm-aist-idl:amd64 1.2.1-0          amd64            OpenRTM-aist idls for development
 ii  openrtp:amd64          1.2.1-0          amd64            OpenRTP, Open RT Platform distributed by AIST
```

Debianはsuでroot権限を得た後に:
```
 # sh pkg_install_debian.sh -l openrtp --yes
```

と入力するとOpenRTPをインストールできます。

## JDK8のインストール

OpenRTP(RTSystem EditorやRTC Builderなど)の実行にはJDK8相当のJava環境が必要です。(デフォル>トの環境でJDK8がインストールされている場合もありますが、Ubuntu 18.04ではJDK11がインストール
されているため、JDK8のインストールが必要です。)  JDK8の入手やインストールについては以下を参
照してください。
- [JDK8のインストール]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

### インストールの確認
インストールを確認します。

```
 $ dpkg -l 'openrt*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
 状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリ>ガ待ち/(T)トリガ保留
    / エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
    / 名前                     バージョン        アーキテクチャ    説明
 +++-========================-=================-+++-======================-================-
 ii  openrtm-aist:amd64     1.2.1-0          amd64            OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-dev:amd64 1.2.1-0          amd64            OpenRTM-aist headers for development
 ii  openrtm-aist-doc       1.2.1-0          all              Documentation for openrtm-aist
 ii  openrtm-aist-example:a 1.2.1-0          amd64            OpenRTM-aist examples
 ii  openrtm-aist-idl:amd64 1.2.1-0          amd64            OpenRTM-aist idls for development
 ii  openrtp:amd64          1.2.1-0          amd64            OpenRTP, Open RT Platform dtributed by AIST
```

## パッケージの詳細
各パッケージの内容は以下の通りです。
### openrtm-aist
openrtm-aist にはランタイムライブラリとコマンド群が含まれています。

- コマンド
```
 /usr/bin/fluent-bit
 /usr/bin/rtcd
 /usr/bin/rtcprof
 /usr/bin/rtm-config
 /usr/bin/rtm-naming
```

- ライセンスなど
```
 /usr/share/doc/openrtm-aist/README
 /usr/share/doc/openrtm-aist/README.Debian
 /usr/share/doc/openrtm-aist/README.jp
 /usr/share/doc/openrtm-aist/changelog.Debian.gz
 /usr/share/doc/openrtm-aist/changelog.gz
 /usr/share/doc/openrtm-aist/copyright
```

- 設定ファイルサンプル
```
 /usr/etc/fluent-bit/fluent-bit.conf
 /usr/etc/fluent-bit/parsers.conf
 /usr/etc/rtc.conf.sample
 /usr/lib/x86_64-linux-gnu/pkgconfig/openrtm-aist.pc
```

- ヘッダなど
```
 /usr/include/fluent-bit.h
 /usr/include/fluent-bit/flb_api.h
 /usr/include/fluent-bit/flb_bits.h
 中略
 /usr/include/fluent-bit/flb_worker.h
```

- ライブラリなど
```
 /lib/systemd/system/fluent-bit.service
 /usr/lib/libfluent-bit.so
```

  - 32bit
```
 /usr/lib/i386-linux-gnu/libRTC-1.2.1.so
 /usr/lib/i386-linux-gnu/libRTC.a
 中略
 /usr/lib/i386-linux-gnu/librtmManipulator.so.0.0.0
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/FileNameservice.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/FileNameservice.so
 中略
  /usr/lib/i386-linux-gnu/openrtm-1.2/ec/RTPreemptEC.so.0.0.0
 /usr/lib/i386-linux-gnu/openrtm-1.2/logger/FluentBit.la
 中略
 /usr/lib/i386-linux-gnu/openrtm-1.2/logger/FluentBit.so.0.0.0
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.la
 中略
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.so.0.0.0
 /usr/lib/i386-linux-gnu/libRTC-X.X.X.so
 /usr/lib/i386-linux-gnu/libRTC.a
 中略
 /usr/lib/i386-linux-gnu/librtmManipulator.so.X.X.X
```
  - 64 bit
```
 /usr/lib/x86_64-linux-gnu/libRTC-1.2.1.so
 /usr/lib/x86_64-linux-gnu/libRTC.a
 中略
 /usr/lib/x86_64-linux-gnu/librtmManipulator.so.0.0.0
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/FileNameservice.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/FileNameservice.so
 中略
  /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/RTPreemptEC.so.0.0.0
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/logger/FluentBit.la
 中略
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/logger/FluentBit.so.0.0.0
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.la
 中略
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.so.0.0.0
 /usr/lib/x86_64-linux-gnu/libRTC-X.X.X.so
 /usr/lib/x86_64-linux-gnu/libRTC.a
 中略
 /usr/lib/x86_64-linux-gnu/librtmManipulator.so.X.X.X
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
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/py_helper/cxx_gen.py
 中略
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/py_helper/yat.py
 /usr/lib/x86_64-linux-gnu/pkgconfig/libcoil.pc
```

### openrtm-aist-example
openrtm-aist-example にはスタンドアロン RTC、ローダブル RTC それぞれのサンプルと、サンプル RTC のソースが含まれています。

- サンプル(スタンドアロンRTC)
```
 /usr/share/openrtm-1.2/components/c++/examples/Composite
 /usr/share/openrtm-1.2/components/c++/examples/ConfigSampleComp
 中略
 /usr/share/openrtm-1.2/components/c++/examples/rtc.conf
```

- サンプル(ローダブルRTC)
```
 /usr/share/openrtm-1.2/Components/C++/examples/rtc/ConfigSample.a
 /usr/share/openrtm-1.2/Components/C++/examples/rtc/ConfigSample.la
 中略
 /usr/share/openrtm-1.2/Components/C++/examples/rtc/Throughput.so.X.X.X
```

- サンプル(ソース)
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
 中略
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
 /usr/share/openrtm-1.2/components/c++/examples/templates/AIO.xml
 /usr/share/openrtm-1.2/components/c++/examples/templates/ActArray.xml
 中略
 /usr/share/openrtm-1.2/components/c++/examples/templates/VelocityControl3D.xml
```

- ライセンスなど
```
 /usr/share/doc/openrtm-aist-example/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-example/changelog.gz
 /usr/share/doc/openrtm-aist-example/copyright
```

### openrtm-aist-doc
openrtm-aist-doc には、日本語と英語のクラスリファレンス、IDL インターフェース定義リファレン
スが含まれています。

- クラスリファレンス
```
 /usr/share/openrtm-1.2/doc/C++/ClassReference/html/Affinity_8h.html
 /usr/share/openrtm-1.2/doc/C++/ClassReference/html/Affinity_8h_dep_incl.map
 中略
 /usr/share/openrtm-1.2/doc/C++/ClassReference/html/version_8h_source.html
```

- IDL リファレンス
```
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/BasicDataType_8idl.html
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/BasicDataType_8idl_dep_incl.map
 中略
 /usr/share/openrtm-1.2/doc/idl/IDLReference/html/unionSDOPackage_1_1Numeric.html
```

- クラスリファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/C++/ClassReference-en/html/Affinity_8h.html
 /usr/share/openrtm-1.2/doc/C++/ClassReference-en/html/Affinity_8h_dep_incl.map
 中略
 /usr/share/openrtm-1.2/doc/C++/ClassReference-en/html/version_8h_source.html
```

- IDL リファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/BasicDataType_8idl_dep_incl.map
 中略
 /usr/share/openrtm-1.2/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
```

- ライセンスなど
```
 /usr/share/doc/openrtm-aist-doc/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-doc/changelog.gz
 /usr/share/doc/openrtm-aist-doc/copyright
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


### openrtp
openrtpでは大量のファイルがインストールされるため、ここではリストしません。必要に応じて
```
 $ dpkg -L openrtp
```
と入力して各自での確認をしてください。







