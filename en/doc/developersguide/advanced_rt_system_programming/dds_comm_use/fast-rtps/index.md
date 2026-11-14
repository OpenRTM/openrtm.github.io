---
layout: page
title: "using fast dds communication functions"
---

<!-- Title: Fast DDS通信機能の利用 -->
#contents

Fast DDS (Fast RTPS in earlier versions) is communication middleware developed by eProsima that conforms to the OMG DDS 2.0 and RTPS 2.2 specifications.

- [eProsima Fast DDS](https://www.eprosima.com/index.php/products-all/eprosima-fast-dds)

The following explains how to install and use the Fast RTPS plugin for OpenRTM-aist.

* If [ROS2 Communication Functions]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ros2_comm_use) are already installed, the Fast DDS communication function is also available, so the following procedure is unnecessary.

Only the C++ version is supported.

## Windows
### Installing Fast DDS
Download and install the installer from the following site.

- [eProsima Fast DDS](https://www.eprosima.com/index.php/products-all/eprosima-fast-dds)

### Building OpenRTM-aist

Set the **FASTRTPS_ENABLE** option to ON when running CMake.

```
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc16 -G "Visual Studio 16 2019" -DFASTRTPS_ENABLE=ON ..
```

The other steps are the same as usual.

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

Install it in an appropriate location.

The installation directory is set with the **CMAKE_INSTALL_PREFIX** option.

```
 cmake .. -DCMAKE_INSTALL_PREFIX=C:/workspace/OpenRTM-aist/build/install
 cmake --build . --config Release --target install
```

### Operation Check

Run the sample components in **{installed path}\2.0.0\Components\C++\Examples\vc16**.

Create rtc.conf with the following content.


```
 manager.modules.load_path: {installed path}\\2.0.0\\ext\\transport
 manager.modules.preload: FastRTPSTransport.dll
 manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps, ConsoleIn0.out?interface_type=fast-rtps
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

First, **FastRTPSTransport.dll** must be loaded.
This setting can be configured with the **manager.modules.preload** option.

Next, when creating the connector, the interface type must be set to **fast-rtps**.
Connector creation is configured with the **manager.components.preconnect** option.
In this example, connectors are created for the **in** port of the **ConsoleOut0** component and the **out** port of the **ConsoleIn0** component.

Communication becomes possible by running **ConsoleInComp.exe** and **ConsoleOutComp.exe**.

## Ubuntu

### Installing Fast DDS

#### Installing Dependent Libraries

Install asio and TinyXML-2.

```
 sudo apt install libasio-dev libtinyxml2-dev
```

Build and install Fast-CDR.

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

Build and install foonathan/memory.

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

#### Building Fast DDS

Building Fast DDS requires CMake version 3.11 or later.
In an Ubuntu 18.04 environment, the version of CMake installed with apt is 3.10, so download a newer version of CMake and set PATH.

```
 wget https://github.com/Kitware/CMake/releases/download/v3.22.3/cmake-3.22.3-linux-x86_64.tar.gz
 tar xf cmake-3.22.3-linux-x86_64.tar.gz
 export PATH=~/cmake-3.22.3-linux-x86_64/bin:$PATH
```

Build and install Fast DDS with the following commands.

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

### Building OpenRTM-aist

Set the **FASTRTPS_ENABLE** option to ON when running CMake.

```
 cmake .. -DFASTRTPS_ENABLE=ON -Dfastrtps_DIR=${OPENRTM_INSTALL_DIR}/share/fastrtps/cmake
```

The other steps are the same as usual.

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

Install it in an appropriate location.

The installation directory is set with the **CMAKE_INSTALL_PREFIX** option.

```
 cmake .. -DCMAKE_INSTALL_PREFIX=${OPENRTM_INSTALL_DIR}
 cmake --build . --config Release --target install
```

### Operation Check

Run the sample components in **{installed path}/share/openrtm-2.0/components/c++/examples**.

Create rtc.conf with the following content.


```
 manager.modules.load_path: {installed path}/lib/openrtm-2.0/transport
 manager.modules.preload: FastRTPSTransport.so
 manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps, ConsoleIn0.out?interface_type=fast-rtps
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

First, **FastRTPSTransport.so** must be loaded.
This setting can be configured with the **manager.modules.preload** option.

Next, when creating the connector, the interface type must be set to **fast-rtps**.
Connector creation is configured with the **manager.components.preconnect** option.
In this example, connectors are created for the **in** port of the **ConsoleOut0** component and the **out** port of the **ConsoleIn0** component.

Communication becomes possible by running **ConsoleInComp** and **ConsoleOutComp**.


## Startup Options
&aname(runoption);
The following options can be set in rtc.conf when starting the OpenRTM-aist manager.
* These options can be used in OpenRTM-aist under development, but may not be implemented in released versions.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Setting Example</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>fast-rtps.xmlprofile.filename</td>
    <td>C:/openrtminstall/2.0.0/ext/transport/FastRTPsQoSExample.xml</td>
    <td>Specifies the <a href="https://fast-dds.docs.eprosima.com/en/latest/fastdds/xml_configuration/xml_configuration.html">Fast DDS configuration file</a>.</td>
  </tr>
  <tr>
    <td>fast-rtps.participant.name</td>
    <td>participant_openrtm</td>
    <td>Profile name of the DomainParticipant to load</td>
  </tr>
  <tr>
    <td>fast-rtps.domain.id</td>
    <td>0</td>
    <td>Domain ID</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.auth.plugin</td>
    <td>builtin.PKI-DH</td>
    <td>Name of the authentication plugin</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.auth.XXX</td>
    <td></td>
    <td>Authentication plugin settings</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.access.plugin</td>
    <td>builtin.Access-Permissions</td>
    <td>Name of the access control plugin</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.access.XXX</td>
    <td></td>
    <td>Access control plugin settings</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.crypto.plugin</td>
    <td>builtin.AES-GCM-GMAC</td>
    <td>Name of the encryption plugin</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.crypto.XXX</td>
    <td></td>
    <td>Encryption plugin settings</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.log.plugin</td>
    <td>builtin.DDS_LogTopic</td>
    <td>Name of the security logging plugin</td>
  </tr>
  <tr>
    <td>fast-rtps.dds.sec.log.XXX</td>
    <td></td>
    <td>Security logging plugin settings</td>
  </tr>
</table>

A setting example is shown below.

```
 fast-rtps.xmlprofile.filename: ${OPENRTM_INSTALL_DIR}/transport/FastRTPsQoSExample.xml
 fast-rtps.participant.name: participant_openrtm
```


## Connection Options
&aname(connectoption);
The options that can be set in the connector profile when connecting data ports are as follows.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Default Value</th>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>fast-rtps.topic</td>
    <td>chatter</td>
    <td></td>
    <td>Name of the DDS topic. When using the ROS2 serializer, it is automatically changed to a name prefixed with <strong>rt/</strong>.</td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.name</td>
    <td></td>
    <td></td>
    <td>Profile name of the Subscriber to load</td>
  </tr>
  <tr>
    <td>fast-rtps.subscriber.qos.deadline.period.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td>Minimum period on the receiving side</td>
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
    <td>Durability on the receiving side (VOLATILE_DURABILITY_QOS: volatile, TRANSIENT_LOCAL_DURABILITY_QOS: temporary local setting)</td>
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
    <td>Heartbeat period on the receiving side</td>
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
    <td>Reliability on the receiving side (RELIABLE_RELIABILITY_QOS: highly reliable, BEST_EFFORT_RELIABILITY_QOS: highest speed)</td>
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
    <td>Profile name of the Publisher to load</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.qos.deadline.period.seconds</td>
    <td>2147483647</td>
    <td></td>
    <td>Minimum period on the sending side</td>
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
    <td>Durability on the sending side (VOLATILE_DURABILITY_QOS: volatile, TRANSIENT_LOCAL_DURABILITY_QOS: temporary local setting)</td>
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
    <td>Retention time for unsent data on the sending side</td>
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
    <td>Heartbeat period on the sending side</td>
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
    <td>Reliability on the sending side (RELIABLE_RELIABILITY_QOS: highly reliable, BEST_EFFORT_RELIABILITY_QOS: highest speed, SYSTEM_DEFAULT)</td>
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
    <td>Number of data samples retained on the sending side</td>
  </tr>
  <tr>
    <td>fast-rtps.publisher.topic.historyQos.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS</td>
    <td>Method for retaining sent data (KEEP_LAST_HISTORY_QOS: retains all data, KEEP_LAST_HISTORY_QOS: retains only the number of data samples specified by depth)</td>
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

A setting example is shown below.

```
 manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps&fast-rtps.subscriber.name=subscriber_openrtm
```

## Using Secure Communication Functions
Fast DDS provides secure communication functions based on the [DDS Security specification](https://www.omg.org/spec/DDS-SECURITY/1.1/About-DDS-SECURITY/).

- [8. Security — Fast DDS 2.5.1 documentation](https://fast-dds.docs.eprosima.com/en/latest/fastdds/security/security.html)

To use secure communication functions with the OpenRTM-aist Fast DDS plugin, startup options must be configured.
A setting example is shown below.

```
 fast-rtps.dds.sec.auth.plugin: builtin.PKI-DH
 fast-rtps.dds.sec.auth.builtin.PKI-DH.identity_ca: file://C:/workspace/openrtm_test/build/install/2.0.0/ext//transport/mainexamplecacert.pem
 fast-rtps.dds.sec.auth.builtin.PKI-DH.identity_certificate: file://C:/workspace/openrtm_test/build/install/2.0.0/ext//transport/appexamplecert.pem
 fast-rtps.dds.sec.auth.builtin.PKI-DH.private_key: file://C:/workspace/openrtm_test/build/install/2.0.0/ext//transport/appexamplekey.pem
 fast-rtps.dds.sec.crypto.plugin: builtin.AES-GCM-GMAC
```


### Creating Private Keys and Certificates
Create the private keys and certificates according to the procedure in the [Fast DDS manual](https://fast-dds.docs.eprosima.com/en/1.5.0/security.html).

The commands for creating a private key and self-signed certificate are shown below.
Use the maincaconf.cnf file from the Fast DDS manual.
If you want to change the output file names, modify the following items in maincaconf.cnf as needed.

```
 certificate = $dir/mainexamplecacert.pem
 private_key = $dir/mainexamplecakey.pem
```


Also, change the req_distinguished_name items and prepare an appconf.cnf file modified according to those contents.

Run the following commands.

```
 type nul > index.txt
 openssl ecparam -name prime256v1 > ecdsaparam
 openssl req -nodes -x509 -days 3650 -newkey ec:ecdsaparam -keyout mainexamplecakey.pem -out mainexamplecacert.pem -config maincaconf.cnf
 
 openssl ecparam -name prime256v1 > ecdsaparam
 openssl req -nodes -new -newkey ec:ecdsaparam -config appconf.cnf -keyout appexamplekey.pem -out appexamplereq.pem
 openssl ca -batch -create_serial -config maincaconf.cnf -days 3650 -in appexamplereq.pem -out appexamplecert.pem
```


Use the private key appexamplekey.pem and the certificates mainexamplecacert.pem and appexamplecert.pem.

