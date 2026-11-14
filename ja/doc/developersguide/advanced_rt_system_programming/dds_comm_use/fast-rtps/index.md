---
layout: page
title: "fast dds通信機能の利用"
---

<!-- Title: Fast DDS通信機能の利用 -->
#contents

Fast DDS(以前のバージョンではFast RTPS)はeProsima社が開発しているOMG DDS 2.0、RTPS 2.2仕様の通信ミドルウェアです。

- [eProsima Fast DDS](https://www.eprosima.com/index.php/products-all/eprosima-fast-dds)

以下ではOpenRTM-aistのFast RTPSプラグインのインストール手順、使用方法を説明します。

※[ROS2通信機能]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ros2_comm_use)がインストール済みの場合、Fast DDS通信機能も利用可能になっているため以下の手順は不要です。

C++版のみの対応です。

## Windows
### Fast DDSのインストール
以下のサイトからインストーラーをダウンロードしてインストールしてください。

- [eProsima Fast DDS](https://www.eprosima.com/index.php/products-all/eprosima-fast-dds)

### OpenRTM-aistのビルド

CMake実行時に**FASTRTPS_ENABLE**のオプションをONにします。

```
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc16 -G "Visual Studio 16 2019" -DFASTRTPS_ENABLE=ON ..
```

その他の手順は通常と同じです。

- [OpenRTM-aistのビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

適当な場所にインストールしてください。

インストールするディレクトリは**CMAKE_INSTALL_PREFIX**のオプションで設定します。

```
 cmake .. -DCMAKE_INSTALL_PREFIX=C:/workspace/OpenRTM-aist/build/install
 cmake --build . --config Release --target install
```

### 動作確認

**{インストールしたパス}\2.0.0\Components\C++\Examples\vc16**のサンプルコンポーネントを実行します。

以下の内容のrtc.confを作成してください。


```
 manager.modules.load_path: {インストールしたパス}\\2.0.0\\ext\\transport
 manager.modules.preload: FastRTPSTransport.dll
 manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps, ConsoleIn0.out?interface_type=fast-rtps
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

まず**FastRTPSTransport.dll**のロードが必要になります。
この設定は**manager.modules.preload**のオプションで設定できます。

次にコネクタ生成時にインターフェース型を**fast-rtps**に設定する必要があります。
コネクタの生成は**manager.components.preconnect**オプションにより設定します。
この例では**ConsoleOut0**コンポーネントの**in**のポート、**ConsoleIn0**コンポーネントの**out**のポートにそれぞれコネクタを生成しています。

**ConsoleInComp.exe**、**ConsoleOutComp.exe**を実行すると通信ができるようになります。

## Ubuntu

### Fast DDSのインストール

#### 依存ライブラリのインストール

asio、TinyXML-2をインストールします。

```
 sudo apt install libasio-dev libtinyxml2-dev
```

Fast-CDRをビルド、インストールします。

```
 export $OPENRTM_INSTALL_DIR=~/fastdds_install
 export FASTCDR_VERSION=1.0.23
 wget https://github.com/eProsima/Fast-CDR/archive/refs/tags/v${FASTCDR_VERSION}.tar.gz
 tar xf v${FASTCDR_VERSION}.tar.gz
 cd Fast-CDR-${FASTCDR_VERSION}/
 mkdir build
 cd build/
 cmake .. -DCMAKE_INSTALL_PREFIX=${OPENRTM_INSTALL_DIR}
 cmake --build . --config Release -- -j$(nproc)
 cmake --build . --config Release --target install
```

foonathan/memoryをビルド、インストールします。

```
 export FOONATHAN_MEMORY_VERSION=1.2.1
 wget https://github.com/eProsima/foonathan_memory_vendor/archive/refs/tags/v${FOONATHAN_MEMORY_VERSION}.tar.gz
 tar xf v${FOONATHAN_MEMORY_VERSION}.tar.gz
 cd foonathan_memory_vendor-${FOONATHAN_MEMORY_VERSION}/
 mkdir build
 cd build
 cmake .. -DCMAKE_INSTALL_PREFIX=${OPENRTM_INSTALL_DIR}
 cmake --build . --config Release -- -j$(nproc)
 cmake --build . --config Release --target install
```

#### Fast DDSのビルド

Fast DDSのビルドにはCMake 3.11以上のバージョンが必要です。
Ubuntu 18.04環境ではaptでインストールされるCMakeのバージョンが3.10のため、新しいバージョンのCMakeをダウンロードしてPATHを設定してください。

```
 wget https://github.com/Kitware/CMake/releases/download/v3.22.3/cmake-3.22.3-linux-x86_64.tar.gz
 tar xf cmake-3.22.3-linux-x86_64.tar.gz
 export PATH=~/cmake-3.22.3-linux-x86_64/bin:$PATH
```

以下のコマンドでFast DDSをビルド、インストールしてください。

```
 export FASTDDS_VERSION=2.5.1
 wget https://github.com/eProsima/Fast-DDS/archive/refs/tags/v${FASTDDS_VERSION}.tar.gz
 tar xf v${FASTDDS_VERSION}.tar.gz
 cd Fast-DDS-${FASTDDS_VERSION}/
 mkdir build
 cd build
 cmake .. -Dfastcdr_DIR=${OPENRTM_INSTALL_DIR}/lib/cmake -Dfoonathan_memory_DIR=${OPENRTM_INSTALL_DIR}/lib/foonathan_memory -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=${OPENRTM_INSTALL_DIR}
 cmake --build . --config Release -- -j$(nproc)
 cmake --build . --config Release --target install
```

### OpenRTM-aistのビルド

CMake実行時に**FASTRTPS_ENABLE**のオプションをONにします。

```
 cmake .. -DFASTRTPS_ENABLE=ON -Dfastrtps_DIR=${OPENRTM_INSTALL_DIR}/share/fastrtps/cmake
```

その他の手順は通常と同じです。

- [OpenRTM-aistのビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

適当な場所にインストールしてください。

インストールするディレクトリは**CMAKE_INSTALL_PREFIX**のオプションで設定します。

```
 cmake .. -DCMAKE_INSTALL_PREFIX=${OPENRTM_INSTALL_DIR}
 cmake --build . --config Release --target install
```

### 動作確認

**{インストールしたパス}/share/openrtm-2.0/components/c++/examples**のサンプルコンポーネントを実行します。

以下の内容のrtc.confを作成してください。


```
 manager.modules.load_path: {インストールしたパス}/lib/openrtm-2.0/transport
 manager.modules.preload: FastRTPSTransport.so
 manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps, ConsoleIn0.out?interface_type=fast-rtps
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

まず**FastRTPSTransport.so**のロードが必要になります。
この設定は**manager.modules.preload**のオプションで設定できます。

次にコネクタ生成時にインターフェース型を**fast-rtps**に設定する必要があります。
コネクタの生成は**manager.components.preconnect**オプションにより設定します。
この例では**ConsoleOut0**コンポーネントの**in**のポート、**ConsoleIn0**コンポーネントの**out**のポートにそれぞれコネクタを生成しています。

**ConsoleInComp**、**ConsoleOutComp**を実行すると通信ができるようになります。


## 起動時のオプション
&aname(runoption);
rtc.confでOpenRTM-aistのマネージャ起動時に以下のオプションを設定可能です。
※開発中のOpenRTM-aistでは使用可能ですが、リリースしたバージョンでは未実装の場合があります。

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>設定例</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>fast-rtps.xmlprofile.filename</td>
    <td>C:/openrtminstall/2.0.0/ext/transport/FastRTPsQoSExample.xml</td>
    <td><a href="https://fast-dds.docs.eprosima.com/en/latest/fastdds/xml_configuration/xml_configuration.html">Fast DDSの設定ファイル</a>を指定する。</td>
  </tr>
  <tr>
    <td>fast-rtps.participant.name</td>
    <td>participant_openrtm</td>
    <td>ロードするDomainParticipantのプロファイル名</td>
  </tr>
  <tr>
    <td>fast-rtps.domain.id</td>
    <td>0</td>
    <td>ドメインのID</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.auth.plugin</td>
    <td>builtin.PKI-DH</td>
    <td>認証プラグインの名前</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.auth.XXX</td>
    <td></td>
    <td>認証プラグインの設定</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.access.plugin</td>
    <td>builtin.Access-Permissions</td>
    <td>アクセス制御プラグインの名前</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.access.XXX</td>
    <td></td>
    <td>アクセス制御プラグインの設定</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.crypto.plugin</td>
    <td>builtin.AES-GCM-GMAC</td>
    <td>暗号化プラグインの名前</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.crypto.XXX</td>
    <td></td>
    <td>暗号化プラグインの設定</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.log.plugin</td>
    <td>builtin.DDS_LogTopic</td>
    <td>セキュリティロギングプラグインの名前</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.log.XXX</td>
    <td></td>
    <td>セキュリティロギングプラグインの設定</td>
  </tr>
</table>

以下に設定例を記載します。

```
 fast-rtps.xmlprofile.filename: ${OPENRTM_INSTALL_DIR}/transport/FastRTPsQoSExample.xml
 fast-rtps.participant.name: participant_openrtm
```


## 接続時のオプション
&aname(connectoption);
データポート接続時のコネクタプロファイルに設定できるオプションは以下の通りです。

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>デフォルト値</th>
    <th>オプション</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>fast-rtps.topic</td>
    <td>chatter</td>
    <td></td>
    <td>DDSトピックの名前。ROS2シリアライザを使う場合は先頭に<strong>rt/</strong>を付けた名前に自動的に変更する。</td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.name</td>
    <td></td>
    <td></td>
    <td>ロードするSubscriberのプロファイル名</td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.deadline.period.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td>受信側の最小周期</td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.deadline.period.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.destinationOrder</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS, BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.disablePositiveACKs.enabled</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.disablePositiveACKs.duration.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.disablePositiveACKs.duration.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.durability.kind</td>
    <td>VOLATILE_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, TRANSIENT_DURABILITY_QOS, PERSISTENT_DURABILITY_QOS</td>
    <td>受信側の堅牢性(VOLATILE_DURABILITY_QOS：変わりやすい、TRANSIENT_LOCAL_DURABILITY_QOS：一時的なローカル設定）</td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.durabilityService.history_depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.durabilityService.history_kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.durabilityService.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.durabilityService.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.durabilityService.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.durabilityService.service_cleanup_delay.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.durabilityService.service_cleanup_delay.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.latencyBudget.duration.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.latencyBudget.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.lifespan.duration.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.lifespan.duration.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.liveliness.announcement_period.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.liveliness.announcement_period.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_PARTICIPANT_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.liveliness.lease_duration.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td>受信側のハートビートの周期</td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.liveliness.lease_duration.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.ownership.kind</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.presentation.access_scope</td>
    <td>INSTANCE_PRESENTATION_QOS</td>
    <td>INSTANCE_PRESENTATION_QOS, TOPIC_PRESENTATION_QOS, GROUP_PRESENTATION_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.presentation.coherent_access</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.presentation.ordered_access</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.reliability.kind</td>
    <td>BEST_EFFORT_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS</td>
    <td>受信側の信頼性(RELIABLE_RELIABILITY_QOS：高信頼、BEST_EFFORT_RELIABILITY_QOS：最高速度)</td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.reliability.max_blocking_time.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.reliability.max_blocking_time.nanosec</td>
    <td>100000000</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.timeBasedFilter.minimum_separation.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.timeBasedFilter.minimum_separation.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.type_consistency.force_type_validation</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.type_consistency.ignore_member_names</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.type_consistency.ignore_sequence_bounds</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.type_consistency.ignore_string_bounds</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.type_consistency.kind</td>
    <td>ALLOW_TYPE_COERCION</td>
    <td>DISALLOW_TYPE_COERCION, ALLOW_TYPE_COERCION</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.type_consistency.prevent_type_widening</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.history_memory_policy</td>
    <td>PREALLOCATED_WITH_REALLOC_MEMORY_MODE</td>
    <td>PREALLOCATED_MEMORY_MODE, PREALLOCATED_WITH_REALLOC_MEMORY_MODE, DYNAMIC_RESERVE_MEMORY_MODE, DYNAMIC_REUSABLE_MEMORY_MODE</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.topic.historyQos.depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.topic.historyQos.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.times.heartbeatResponseDelay.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.times.heartbeatResponseDelay.nanosec</td>
    <td>5000000</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.times.initialAcknackDelay.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.times.initialAcknackDelay.nanosec</td>
    <td>70000000</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.name</td>
    <td></td>
    <td></td>
    <td>ロードするPublisherのプロファイル名</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.deadline.period.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td>送信側の最小周期</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.deadline.period.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.destinationOrder</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td>BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS, BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.disablePositiveACKs.enabled</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.disablePositiveACKs.duration.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.disablePositiveACKs.duration.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.durability.kind</td>
    <td>VOLATILE_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, TRANSIENT_DURABILITY_QOS, PERSISTENT_DURABILITY_QOS</td>
    <td>送信側の堅牢性(VOLATILE_DURABILITY_QOS：変わりやすい、TRANSIENT_LOCAL_DURABILITY_QOS：一時的なローカル設定）</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.durabilityService.history_depth</td>
    <td>1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.durabilityService.history_kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.durabilityService.max_instances</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.durabilityService.max_samples</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.durabilityService.max_samples_per_instance</td>
    <td>-1</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.durabilityService.service_cleanup_delay.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.durabilityService.service_cleanup_delay.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.latencyBudget.duration.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.latencyBudget.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.lifespan.duration.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td>送信側の未送信データの保持時間</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.lifespan.duration.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.liveliness.announcement_period.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.liveliness.announcement_period.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_PARTICIPANT_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.liveliness.lease_duration.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td>送信側のハートビートの周期</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.liveliness.lease_duration.nanosec</td>
    <td>4294967295</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.ownership.kind</td>
    <td>SHARED_OWNERSHIP_QOS</td>
    <td>SHARED_OWNERSHIP_QOS, EXCLUSIVE_OWNERSHIP_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.presentation.access_scope</td>
    <td>INSTANCE_PRESENTATION_QOS</td>
    <td>INSTANCE_PRESENTATION_QOS, TOPIC_PRESENTATION_QOS, GROUP_PRESENTATION_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.presentation.coherent_access</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.presentation.ordered_access</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.publishMode.kind</td>
    <td>SYNCHRONOUS_PUBLISH_MODE</td>
    <td>SYNCHRONOUS_PUBLISH_MODE, ASYNCHRONOUS_PUBLISH_MODE</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.reliability.kind</td>
    <td>BEST_EFFORT_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS</td>
    <td>送信側の信頼性(RELIABLE_RELIABILITY_QOS：高信頼、BEST_EFFORT_RELIABILITY_QOS：最高速度、SYSTEM_DEFAULT)</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.reliability.max_blocking_time.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.reliability.max_blocking_time.nanosec</td>
    <td>100000000</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.timeBasedFilter.minimum_separation.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.timeBasedFilter.minimum_separation.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.type_consistency.force_type_validation</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.type_consistency.ignore_member_names</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.type_consistency.ignore_sequence_bounds</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.type_consistency.ignore_string_bounds</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.type_consistency.kind</td>
    <td>ALLOW_TYPE_COERCION</td>
    <td>DISALLOW_TYPE_COERCION, ALLOW_TYPE_COERCION</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.type_consistency.prevent_type_widening</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.history_memory_policy</td>
    <td>PREALLOCATED_WITH_REALLOC_MEMORY_MODE</td>
    <td>PREALLOCATED_MEMORY_MODE, PREALLOCATED_WITH_REALLOC_MEMORY_MODE, DYNAMIC_RESERVE_MEMORY_MODE, DYNAMIC_REUSABLE_MEMORY_MODE</td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.topic.historyQos.depth</td>
    <td>1</td>
    <td></td>
    <td>送信側の保持するデータ数</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.topic.historyQos.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td>送信データの保持方法（KEEP_LAST_HISTORY_QOS：すべてのデータを保持、KEEP_LAST_HISTORY_QOS：depthで指定したデータ数だけ保持）</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.times.heartbeatPeriod.seconds</td>
    <td>3</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.times.heartbeatPeriod.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.times.initialHeartbeatDelay.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.times.initialHeartbeatDelay.nanosec</td>
    <td>12000000</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.times.nackResponseDelay.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.times.nackResponseDelay.nanosec</td>
    <td>5000000</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.times.nackSupressionDuration.seconds</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.times.nackSupressionDuration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
</table>

以下に設定例を記載します。

```
 manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps&fast-rtps.subscriber.name=subscriber_openrtm
```

## セキュア通信機能の利用
Fast DDSは[DDS Security仕様](https://www.omg.org/spec/DDS-SECURITY/1.1/About-DDS-SECURITY/)のセキュア通信機能を提供しています。

- [8. Security — Fast DDS 2.5.1 documentation](https://fast-dds.docs.eprosima.com/en/latest/fastdds/security/security.html)

OpenRTM-aistのFast DDSプラグインでセキュア通信機能を使用するためには起動時のオプションを設定する必要があります。
以下に設定例を記載します。

```
 fast-rtps.dds.sec.auth.plugin: builtin.PKI-DH
 fast-rtps.dds.sec.auth.builtin.PKI-DH.identity_ca: file://C:/workspace/openrtm_test/build/install/2.0.0/ext//transport/mainexamplecacert.pem
 fast-rtps.dds.sec.auth.builtin.PKI-DH.identity_certificate: file://C:/workspace/openrtm_test/build/install/2.0.0/ext//transport/appexamplecert.pem
 fast-rtps.dds.sec.auth.builtin.PKI-DH.private_key: file://C:/workspace/openrtm_test/build/install/2.0.0/ext//transport/appexamplekey.pem
 fast-rtps.dds.sec.crypto.plugin: builtin.AES-GCM-GMAC
```


### 秘密鍵、証明書の作成
[Fast DDSのマニュアル](https://fast-dds.docs.eprosima.com/en/1.5.0/security.html)の手順で秘密鍵、証明書を作成します。

以下で秘密鍵、自己署名証明書を作成するコマンドを掲載します。
maincaconf.cnfはFast DDSのマニュアルのものを使用します。
出力するファイル名を変更したい場合は適宜maincaconf.cnfの以下の項目を変更してください。

```
 certificate = $dir/mainexamplecacert.pem
 private_key = $dir/mainexamplecakey.pem
```


また、req_distinguished_nameの項目は変更して、その内容に応じて変更したappconf.cnfを用意してください。

以下のコマンドを実行します。

```
 type nul > index.txt
 openssl ecparam -name prime256v1 > ecdsaparam
 openssl req -nodes -x509 -days 3650 -newkey ec:ecdsaparam -keyout mainexamplecakey.pem -out mainexamplecacert.pem -config maincaconf.cnf
 
 openssl ecparam -name prime256v1 > ecdsaparam
 openssl req -nodes -new -newkey ec:ecdsaparam -config appconf.cnf -keyout appexamplekey.pem -out appexamplereq.pem
 openssl ca -batch -create_serial -config maincaconf.cnf -days 3650 -in appexamplereq.pem -out appexamplecert.pem
```


秘密鍵appexamplekey.pem、証明書mainexamplecacert.pem、appexamplecert.pemを使用します。


