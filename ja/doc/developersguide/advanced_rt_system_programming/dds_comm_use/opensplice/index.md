---
layout: page
title: "opensplice通信機能の利用"
---
<!-- Title: OpenSplice通信機能の利用 -->
#contents

Vortex OpenspliceはADLINK社が開発しているOMG DDS 1.4、DDSI-RTPS 2.3仕様の通信ミドルウェアです。

- [Data Distribution Service | Vortex OpenSplice | ADLINK](https://www.adlinktech.com/jp/vortex-opensplice-data-distribution-service)

以下ではOpenRTM-aistのOpenSpliceプラグインのインストール、使用手順を説明します。
## C++版
### Windows
#### OpenSpliceの入手
以下からOpenSpliceをダウンロードして適当な場所に展開してください。

- [Releases · ADLINK-IST/opensplice](https://github.com/ADLINK-IST/opensplice/releases)

#### RapidXmlの入手
以下からRapidXmlをダウンロードして適当な場所に展開してください。

- [RapidXml](http://rapidxml.sourceforge.net/)

展開したら新たに**rapidxml**フォルダを作成してヘッダーファイル(.hpp)をそこに移動させてください。
この時、展開したパスは以下のようになっています。

```
 rapidxml-1.13
    - rapidxml
      | - rapidxml.hpp
      | - rapidxml_iterators.hpp
      | - rapidxml_print.hpp
      | - rapidxml_utils.hpp
```


#### OpenRTM-aistのビルド
OpenRTM-aistをビルドする前に、OpenSpliceの**release.bat**を実行します。

```
 %OpenSplice_DIR%\x86.win32\release.bat
```

CMake実行時に**OPENSPLICE_ENABLE**オプションを**ON**に設定し、**RAPIDXML_DIR**オプションにRapidXmlを展開したパスを指定します。

```
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc16 -G "Visual Studio 16 2019" -DOPENSPLICE_ENABLE=ON -DRAPIDXML_DIR=%RAPIDXML_DIR% ..
```

その他の手順は通常と同じです。

- [OpenRTM-aistのビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

適当な場所にインストールしてください。

インストールするディレクトリは**CMAKE_INSTALL_PREFIX**のオプションで設定します。

```
 cmake .. -DCMAKE_INSTALL_PREFIX=C:/workspace/OpenRTM-aist/build/install
 cmake --build . --config Release --target install
```

#### 動作確認


**{インストールしたパス}\2.0.0\Components\C++\Examples\vc16**のサンプルコンポーネントを実行します。
RTC起動前にOpenSpliceの**release.bat**を実行してください。

以下の内容のrtc.confを作成してください。


```
 manager.modules.load_path: {インストールしたパス}\\2.0.0\\ext\\transport
 manager.modules.preload: OpenSpliceTransport.dll
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice, ConsoleIn0.out?interface_type=opensplice
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

まず**OpenSpliceTransport.dll**のロードが必要になります。
この設定は**manager.modules.preload**のオプションで設定できます。

次にコネクタ生成時にインターフェース型を**opensplice**に設定する必要があります。
コネクタの生成は**manager.components.preconnect**オプションにより設定します。
この例では**ConsoleOut0**コンポーネントの**in**のポート、**ConsoleIn0**コンポーネントの**out**のポートにそれぞれコネクタを生成しています。

**ConsoleInComp.exe**、**ConsoleOutComp.exe**を実行すると通信ができるようになります。

### Ubuntu
#### OpenSpliceの入手
以下からOpenSpliceをダウンロードして適当な場所に展開してください。

- https://github.com/ADLINK-IST/opensplice/releases

```
 wget https://github.com/ADLINK-IST/opensplice/releases/download/OSPL_V6_9_210323OSS_RELEASE/PXXX-VortexOpenSplice-6.9.210323OSS-HDE-x86_64.linux-gcc7-glibc2.27-installer.tar
 tar xf PXXX-VortexOpenSplice-6.9.210323OSS-HDE-x86_64.linux-gcc7-glibc2.27-installer.tar 
```

#### RapidXmlのインストール
以下のコマンドでRapidXmlをインストールしてください。

```
 sudo apt install librapidxml-dev
```

#### OpenRTM-aistのビルド
OpenRTM-aistをビルドする前に、OpenSpliceの**release.com**を実行します。

```
 source ${OPENSPLICE_DIR}/x86_64.linux/release.com
```

CMake実行時に**OPENSPLICE_ENABLE**オプションを**ON**に設定します。

```
 cmake -DOPENSPLICE_ENABLE=ON ..
```

その他の手順は通常と同じです。

- [OpenRTM-aistのビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

適当な場所にインストールしてください。

インストールするディレクトリは**CMAKE_INSTALL_PREFIX**のオプションで設定します。

```
 cmake .. -DCMAKE_INSTALL_PREFIX=~/workspace/OpenRTM-aist/build/install
 cmake --build . --config Release --target install
```

#### 動作確認
**{インストールしたパス}/share/openrtm-2.0/components/c++/examples**のサンプルコンポーネントを実行します。
RTC起動前にOpenSpliceの**release.com**を実行してください。

以下の内容のrtc.confを作成してください。


```
 manager.modules.load_path: {インストールしたパス}/lib/openrtm-2.0
 manager.modules.preload: OpenSpliceTransport.so
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice, ConsoleIn0.out?interface_type=opensplice
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

まず**OpenSpliceTransport.so**のロードが必要になります。
この設定は**manager.modules.preload**のオプションで設定できます。

次にコネクタ生成時にインターフェース型を**opensplice**に設定する必要があります。
コネクタの生成は**manager.components.preconnect**オプションにより設定します。
この例では**ConsoleOut0**コンポーネントの**in**のポート、**ConsoleIn0**コンポーネントの**out**のポートにそれぞれコネクタを生成しています。

**ConsoleInComp**、**ConsoleOutComp**を実行すると通信ができるようになります。

## Python版
### Windows
#### OpenSpliceのインストール
まずはOpenSpliceのPythonラッパーライブラリをインストールする必要があります。

適当な場所にビルド済みのOpenSpliceを展開してください。

- https://github.com/ADLINK-IST/opensplice/releases

次に展開したフォルダの**HDE\x86_64.win64\tools\python\src**で以下のコマンドを実行するとインストールされます。

```
 {OpenSpliceを展開したディレクトリ}\HDE\x86_64.win64\release.bat
 python setup.py build
 python setup.py install
```

Cythonをインストールしていない場合は以下のコマンドを実行してください。

```
 pip install cython
```

※上記のsetup.pyによるビルドにはPythonをビルドしたVisual Studioと同じバージョンのVisual Studioがインストールされている必要があります。
Python 2.7ではVisual Studio 2008、Python 3.7ではVisual Studio 2017が必要になります。

#### OpenRTM-aistのインストール
OpenRTM-aist 1.2等をインストーラーでインストールしておいてください。
OpenRTM-aist Python版のソースコードを入手してください。

- https://github.com/OpenRTM/OpenRTM-aist-Python

以下のコマンドでOpenRTM-aist Python版をインストールしてください。

```
 python setup.py build
 python setup.py install
```

#### 動作確認
動作前に以下のコマンドを実行してください。

```
  {OpenSpliceを展開したディレクトリ}\HDE\x86_64.win64\release.bat
```

以下のようなrtc.confを作成し、**OpenSpliceTransport.py**をロード後、インターフェース型に**opensplice**を指定してRTCを起動します。

```
 manager.modules.load_path: C:\\Python37\\Lib\\site-packages\\OpenRTM_aist\\ext\\transport\\OpenSplice
 manager.modules.preload: OpenSpliceTransport.py
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice&marshaling_type=opensplice, ConsoleIn0.out?interface_type=opensplice&marshaling_type=opensplice
```



### Ubuntu
#### OpenSpliceのインストール
まずはOpenSpliceのPythonラッパーライブラリをインストールする必要があります。
以下からOpenSpliceをダウンロードして適当な場所に展開してください。

- https://github.com/ADLINK-IST/opensplice/releases

```
 wget https://github.com/ADLINK-IST/opensplice/releases/download/OSPL_V6_9_210323OSS_RELEASE/PXXX-VortexOpenSplice-6.9.210323OSS-HDE-x86_64.linux-gcc7-glibc2.27-installer.tar
 tar xf PXXX-VortexOpenSplice-6.9.210323OSS-HDE-x86_64.linux-gcc7-glibc2.27-installer.tar 
```

次に展開したフォルダの**HDE/x86_64.linux/tools/python/src**で以下のコマンドを実行するとインストールされます。

```
 source ${OPENSPLICE_DIR}/x86_64.linux/release.com
 python3 setup.py build
 sudo su
 # source ${OPENSPLICE_DIR}/x86_64.linux/release.com
 # python3 setup.py install
 # exit
```

Cythonをインストールしていない場合は以下のコマンドを実行してください。

```
 sudo apt install python3-pip
 pip3 install cython
```

#### omniORB-pythonのインストール
omniORBのPython版をインストールします。

```
 sudo su
 # echo "deb http://openrtm.org/pub/Linux/ubuntu/ $code_name main" >> /etc/apt/sources.list
 # wget -O- --secure-protocol=TLSv1_2 --no-check-certificate https://openrtm.org/pub/openrtm.key | apt-key add -
 # apt update
 # apt install python3-omniorb python3-omniorb-omg omniidl-python3
 # exit
```

#### OpenRTM-aistのインストール
OpenRTM-aist 1.2等をインストーラーでインストールしておいてください。
OpenRTM-aist Python版のソースコードを入手してください。

- https://github.com/OpenRTM/OpenRTM-aist-Python

以下のコマンドでOpenRTM-aist Python版をインストールしてください。

```
 sudo apt install doxygen
 python3 setup.py build
 sudo python3 setup.py install
```

#### 動作確認
動作前に**release.com**を実行してください。

以下のようなrtc.confを作成し、**OpenSpliceTransport.py**をロード後、インターフェース型に**opensplice**を指定してRTCを起動します。

```
 manager.modules.load_path: /usr/local/lib/python3.6/dist-packages/OpenRTM_aist/ext/transport/OpenSplice
 manager.modules.preload: OpenSpliceTransport.py
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice&marshaling_type=opensplice, ConsoleIn0.out?interface_type=opensplice&marshaling_type=opensplice
```

## 起動時のオプション
### C++

rtc.confでOpenRTM-aistのマネージャ起動時に以下のオプションを設定可能です。
※開発中のOpenRTM-aistでは使用可能ですが、リリースしたバージョンでは未実装の場合があります。

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>設定例</th>
    <th>オプション</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>opensplice.uri</td>
    <td>file://OpenSpliceQoSExample.xml</td>
    <td></td>
    <td>OpenSpliceのQoS設定ファイルを指定する。</td>
  </tr>
  <tr>
    <td>opensplice.profile</td>
    <td>testProfile</td>
    <td></td>
    <td>QoSのプロファイル名を指定する。</td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.name</td>
    <td>testParticipant</td>
    <td></td>
    <td>ロードするDomainParticipantのプロファイル名</td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.entity_factory.autoenable_created_entities</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.listener_scheduling.scheduling_class.kind</td>
    <td>SCHEDULE_DEFAULT</td>
    <td>SCHEDULE_DEFAULT,SCHEDULE_TIMESHARING,SCHEDULE_REALTIME</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.listener_scheduling.scheduling_priority</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.listener_scheduling.scheduling_priority_kind.kind</td>
    <td>PRIORITY_RELATIVE</td>
    <td>PRIORITY_RELATIVE,PRIORITY_ABSOLUTE</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.watchdog_scheduling.scheduling_class.kind</td>
    <td>SCHEDULE_DEFAULT</td>
    <td>SCHEDULE_DEFAULT,SCHEDULE_TIMESHARING,SCHEDULE_REALTIME</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.watchdog_scheduling.scheduling_priority</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.watchdog_scheduling.scheduling_priority_kind.kind</td>
    <td>PRIORITY_RELATIVE</td>
    <td>PRIORITY_RELATIVE,PRIORITY_ABSOLUTE</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.publisher_qos.entity_factory.autoenable_created_entities</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.publisher_qos.presentation.access_scope</td>
    <td>INSTANCE_PRESENTATION_QOS</td>
    <td>INSTANCE_PRESENTATION_QOS,TOPIC_PRESENTATION_QOS,GROUP_PRESENTATION_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.publisher_qos.presentation.coherent_access</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.publisher_qos.presentation.ordered_access</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.publisher_qos.id</td>
    <td>testPublisher</td>
    <td></td>
    <td>ロードするPublisherのプロファイル名</td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.entity_factory.autoenable_created_entities</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.presentation.access_scope</td>
    <td>INSTANCE_PRESENTATION_QOS</td>
    <td>INSTANCE_PRESENTATION_QOS,TOPIC_PRESENTATION_QOS,GROUP_PRESENTATION_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.presentation.coherent_access</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.presentation.ordered_access</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.share.enable</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.id</td>
    <td>testSubscriber</td>
    <td></td>
    <td>ロードするSubscriberのプロファイル名</td>
  </tr>
</table>

以下に記述例を記載します。

```
 opensplice.uri: file://OpenSpliceQoSExample.xml
 opensplice.profile: testProfile
```

### Python

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>設定例</th>
    <th>オプション</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>opensplice.uri</td>
    <td>file://OpenSpliceQoSExample.xml</td>
    <td></td>
    <td>OpenSpliceのQoS設定ファイルを指定する。</td>
  </tr>
  <tr>
    <td>opensplice.profile</td>
    <td>testProfile</td>
    <td></td>
    <td>QoSのプロファイル名を指定する。</td>
  </tr>
  <tr>
    <td>opensplice.publisher_qos.presentation.access_scope</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.publisher_qos.presentation.coherent_access</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.publisher_qos.presentation.ordered_access</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.presentation.access_scope</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.presentation.coherent_access</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.subscriber_qos.presentation.ordered_access</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>


以下に記述例を記載します。

```
 opensplice.uri: file://OpenSpliceQoSExample.xml
 opensplice.profile: testProfile
```


## 接続時のオプション
### C++

データポート接続時のコネクタプロファイルに設定できるオプションは以下の通りです。

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>デフォルト値</th>
    <th>オプション</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>opensplice.topic</td>
    <td>chatter</td>
    <td></td>
    <td>DDSトピックの名前</td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.id</td>
    <td></td>
    <td></td>
    <td>ロードするReaderのプロファイル名</td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.id</td>
    <td></td>
    <td></td>
    <td>ロードするWriterのプロファイル名</td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.id</td>
    <td></td>
    <td></td>
    <td>ロードするTopicのプロファイル名</td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, TRANSIENT_DURABILITY_QOS, PERSISTENT_DURABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.deadline.period.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.deadline.period.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.latency_budget.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.latency_budget.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_PARTICIPANT_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.liveliness.lease_duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.liveliness.lease_duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reliability.kind</td>
    <td>BEST_EFFORT_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reliability.max_blocking_time.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reliability.max_blocking_time.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reliability.synchronous</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.destination_order.kind</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS, BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.history.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.resource_limits.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.resource_limits.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.resource_limits.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.ownership.kind</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.time_based_filter.minimum_separation.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.time_based_filter.minimum_separation.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.autopurge_disposed_samples_delay.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.autopurge_disposed_samples_delay.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.autopurge_dispose_all</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.autopurge_nowriter_samples_delay.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.autopurge_nowriter_samples_delay.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.enable_invalid_samples</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.invalid_sample_visibility.kind</td>
    <td>MINIMUM_INVALID_SAMPLES</td>
    <td>NO_INVALID_SAMPLES, MINIMUM_INVALID_SAMPLES, ALL_INVALID_SAMPLES</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, TRANSIENT_DURABILITY_QOS, PERSISTENT_DURABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.deadline.period.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.deadline.period.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.latency_budget.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.latency_budget.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_PARTICIPANT_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.liveliness.lease_duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.liveliness.lease_duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.reliability.kind</td>
    <td>RELIABLE_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.reliability.max_blocking_time.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.reliability.max_blocking_time.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.reliability.synchronous</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.destination_order.kind</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS, BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.history.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.resource_limits.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.resource_limits.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.resource_limits.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.transport_priority.value</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.lifespan.duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.lifespan.duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.ownership.kind</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.ownership_strength.value</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.writer_data_lifecycle.autodispose_unregistered_instances</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.writer_data_lifecycle.autopurge_suspended_samples_delay.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.writer_data_lifecycle.autopurge_suspended_samples_delay.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.writer_data_lifecycle.autounregister_instance_dela.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.writer_data_lifecycle.autounregister_instance_dela.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, TRANSIENT_DURABILITY_QOS, PERSISTENT_DURABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.deadline.period.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.deadline.period.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.latency_budget.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.latency_budget.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_PARTICIPANT_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.liveliness.lease_duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.liveliness.lease_duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.reliability.kind</td>
    <td>RELIABLE_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.reliability.max_blocking_time.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.reliability.max_blocking_time.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.reliability.synchronous</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.destination_order.kind</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS, BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.history.kind</td>
    <td>KEEP_ALL_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.resource_limits.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.resource_limits.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.resource_limits.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.transport_priority.value</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.lifespan.duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.lifespan.duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.ownership.kind</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.transport_priority.value</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.history_depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.history_kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.service_cleanup_delay.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.service_cleanup_delay.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
</table>


以下に設定例を記載します。

```
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice&opensplice.topic=testtopic
```

### Python

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>デフォルト値</th>
    <th>オプション</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>opensplice.topic</td>
    <td>chatter</td>
    <td></td>
    <td>DDSトピックの名前</td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, TRANSIENT_DURABILITY_QOS, PERSISTENT_DURABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.deadline.period.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.deadline.period.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.latency_budget.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.latency_budget.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_PARTICIPANT_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.liveliness.lease_duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.liveliness.lease_duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reliability.kind</td>
    <td>BEST_EFFORT_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reliability.max_blocking_time.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reliability.max_blocking_time.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.destination_order.kind</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS, BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.history.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.resource_limits.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.resource_limits.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.resource_limits.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.ownership.kind</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.time_based_filter.minimum_separation.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.time_based_filter.minimum_separation.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.autopurge_disposed_samples_delay.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.autopurge_disposed_samples_delay.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.autopurge_nowriter_samples_delay.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.reader_data_lifecycle.autopurge_nowriter_samples_delay.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, TRANSIENT_DURABILITY_QOS, PERSISTENT_DURABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.deadline.period.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.deadline.period.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.latency_budget.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.latency_budget.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_PARTICIPANT_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.liveliness.lease_duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.liveliness.lease_duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.reliability.kind</td>
    <td>BEST_EFFORT_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.reliability.max_blocking_time.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.reliability.max_blocking_time.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.destination_order.kind</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS, BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.history.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.resource_limits.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.resource_limits.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.resource_limits.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.transport_priority.value</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.lifespan.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.lifespan.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.ownership.kind</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.ownership_strength.value</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.writer_data_lifecycle.autodispose_unregistered_instances</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, TRANSIENT_DURABILITY_QOS, PERSISTENT_DURABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.deadline.period.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.deadline.period.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.latency_budget.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.latency_budget.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_PARTICIPANT_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.liveliness.lease_duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>opensplice.topic_qos.liveliness.lease_duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.reliability.kind</td>
    <td>RELIABLE_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.reliability.max_blocking_time.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.reliability.max_blocking_time.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.destination_order.kind</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS, BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.history.kind</td>
    <td>KEEP_ALL_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.resource_limits.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.resource_limits.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.resource_limits.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.transport_priority.value</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.lifespan.duration.sec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.lifespan.duration.nanosec</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.ownership.kind</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.transport_priority.value</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.history_depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.history_kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.service_cleanup_delay.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.durability_service.service_cleanup_delay.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
</table>


```
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice&opensplice.topic=testtopic
```


## その他
### OpenSpliceのコンフィギュレーションファイル
OpenSpliceのコンフィギュレーションファイルは環境変数**${OSPL_URI}**で設定している。

- [14. Configuration — The OpenSplice Deployment Guide](http://download.prismtech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html)

デフォルトでは**${OSPL_URI}/etc/config/ospl.xml**が設定されている。

例えば、ドメインIDを変更するためにはospl.xmlの以下の部分を変更する。

```
 <OpenSplice>
     <Domain>
         <Name>ospl_sp_ddsi</Name>
         <!-- 以下を変更する -->
         <Id>1</Id>
         <SingleProcess>true</SingleProcess>
```

詳細なログを出力するためには以下の部分を追加する。

```
    <DDSI2Service name="ddsi2">
        <!-- 以下を追加する -->
        <Tracing>
             <Verbosity>FINEST</Verbosity>
        </Tracing>
        <!-- ここまで -->
        <General>
```


