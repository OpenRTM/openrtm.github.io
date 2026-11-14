---
layout: page
title: "using opensplice communication functions"
---
<!-- Title: OpenSplice通信機能の利用 -->
#contents

Vortex OpenSplice is communication middleware developed by ADLINK that conforms to the OMG DDS 1.4 and DDSI-RTPS 2.3 specifications.

- [Data Distribution Service | Vortex OpenSplice | ADLINK](https://www.adlinktech.com/jp/vortex-opensplice-data-distribution-service)

The following explains how to install and use the OpenSplice plugin for OpenRTM-aist.
## C++ Version
### Windows
#### Obtaining OpenSplice
Download OpenSplice from the following and extract it to an appropriate location.

- [Releases · ADLINK-IST/opensplice](https://github.com/ADLINK-IST/opensplice/releases)

#### Obtaining RapidXml
Download RapidXml from the following and extract it to an appropriate location.

- [RapidXml](http://rapidxml.sourceforge.net/)

After extracting it, create a new **rapidxml** folder and move the header files (.hpp) there.
At this time, the extracted path should look like the following.

```
 rapidxml-1.13
    - rapidxml
      | - rapidxml.hpp
      | - rapidxml_iterators.hpp
      | - rapidxml_print.hpp
      | - rapidxml_utils.hpp
```


#### Building OpenRTM-aist
Before building OpenRTM-aist, run the OpenSplice **release.bat**.

```
 %OpenSplice_DIR%\x86.win32\release.bat
```

When running CMake, set the **OPENSPLICE_ENABLE** option to **ON**, and specify the path where RapidXml was extracted in the **RAPIDXML_DIR** option.

```
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc16 -G "Visual Studio 16 2019" -DOPENSPLICE_ENABLE=ON -DRAPIDXML_DIR=%RAPIDXML_DIR% ..
```

The other steps are the same as usual.

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

Install it in an appropriate location.

The installation directory is set with the **CMAKE_INSTALL_PREFIX** option.

```
 cmake .. -DCMAKE_INSTALL_PREFIX=C:/workspace/OpenRTM-aist/build/install
 cmake --build . --config Release --target install
```

#### Operation Check


Run the sample components in **{installed path}\2.0.0\Components\C++\Examples\vc16**.
Before starting the RTCs, run the OpenSplice **release.bat**.

Create rtc.conf with the following content.


```
 manager.modules.load_path: {installed path}\\2.0.0\\ext\\transport
 manager.modules.preload: OpenSpliceTransport.dll
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice, ConsoleIn0.out?interface_type=opensplice
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

First, **OpenSpliceTransport.dll** must be loaded.
This setting can be configured with the **manager.modules.preload** option.

Next, when creating the connector, the interface type must be set to **opensplice**.
Connector creation is configured with the **manager.components.preconnect** option.
In this example, connectors are created for the **in** port of the **ConsoleOut0** component and the **out** port of the **ConsoleIn0** component.

Communication becomes possible by running **ConsoleInComp.exe** and **ConsoleOutComp.exe**.

### Ubuntu
#### Obtaining OpenSplice
Download OpenSplice from the following and extract it to an appropriate location.

- https://github.com/ADLINK-IST/opensplice/releases

```
 wget https://github.com/ADLINK-IST/opensplice/releases/download/OSPL_V6_9_210323OSS_RELEASE/PXXX-VortexOpenSplice-6.9.210323OSS-HDE-x86_64.linux-gcc7-glibc2.27-installer.tar
 tar xf PXXX-VortexOpenSplice-6.9.210323OSS-HDE-x86_64.linux-gcc7-glibc2.27-installer.tar 
```

#### Installing RapidXml
Install RapidXml with the following command.

```
 sudo apt install librapidxml-dev
```

#### Building OpenRTM-aist
Before building OpenRTM-aist, run the OpenSplice **release.com**.

```
 source ${OPENSPLICE_DIR}/x86_64.linux/release.com
```

When running CMake, set the **OPENSPLICE_ENABLE** option to **ON**.

```
 cmake -DOPENSPLICE_ENABLE=ON ..
```

The other steps are the same as usual.

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

Install it in an appropriate location.

The installation directory is set with the **CMAKE_INSTALL_PREFIX** option.

```
 cmake .. -DCMAKE_INSTALL_PREFIX=~/workspace/OpenRTM-aist/build/install
 cmake --build . --config Release --target install
```

#### Operation Check
Run the sample components in **{installed path}/share/openrtm-2.0/components/c++/examples**.
Before starting the RTCs, run the OpenSplice **release.com**.

Create rtc.conf with the following content.


```
 manager.modules.load_path: {installed path}/lib/openrtm-2.0
 manager.modules.preload: OpenSpliceTransport.so
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice, ConsoleIn0.out?interface_type=opensplice
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

First, **OpenSpliceTransport.so** must be loaded.
This setting can be configured with the **manager.modules.preload** option.

Next, when creating the connector, the interface type must be set to **opensplice**.
Connector creation is configured with the **manager.components.preconnect** option.
In this example, connectors are created for the **in** port of the **ConsoleOut0** component and the **out** port of the **ConsoleIn0** component.

Communication becomes possible by running **ConsoleInComp** and **ConsoleOutComp**.

## Python Version
### Windows
#### Installing OpenSplice
First, you need to install the OpenSplice Python wrapper library.

Extract the prebuilt OpenSplice to an appropriate location.

- https://github.com/ADLINK-IST/opensplice/releases

Next, run the following commands in **HDE\x86_64.win64\tools\python\src** in the extracted folder to install it.

```
 {directory where OpenSplice was extracted}\HDE\x86_64.win64\release.bat
 python setup.py build
 python setup.py install
```

If Cython is not installed, run the following command.

```
 pip install cython
```

* Building with setup.py above requires the same version of Visual Studio as the one used to build Python.
Python 2.7 requires Visual Studio 2008, and Python 3.7 requires Visual Studio 2017.

#### Installing OpenRTM-aist
Install OpenRTM-aist 1.2 or similar using the installer in advance.
Obtain the source code of the Python version of OpenRTM-aist.

- https://github.com/OpenRTM/OpenRTM-aist-Python

Install the Python version of OpenRTM-aist with the following commands.

```
 python setup.py build
 python setup.py install
```

#### Operation Check
Before operation, run the following command.

```
  {directory where OpenSplice was extracted}\HDE\x86_64.win64\release.bat
```

Create an rtc.conf like the following, load **OpenSpliceTransport.py**, specify **opensplice** as the interface type, and start the RTC.

```
 manager.modules.load_path: C:\\Python37\\Lib\\site-packages\\OpenRTM_aist\\ext\\transport\\OpenSplice
 manager.modules.preload: OpenSpliceTransport.py
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice&marshaling_type=opensplice, ConsoleIn0.out?interface_type=opensplice&marshaling_type=opensplice
```



### Ubuntu
#### Installing OpenSplice
First, you need to install the OpenSplice Python wrapper library.
Download OpenSplice from the following and extract it to an appropriate location.

- https://github.com/ADLINK-IST/opensplice/releases

```
 wget https://github.com/ADLINK-IST/opensplice/releases/download/OSPL_V6_9_210323OSS_RELEASE/PXXX-VortexOpenSplice-6.9.210323OSS-HDE-x86_64.linux-gcc7-glibc2.27-installer.tar
 tar xf PXXX-VortexOpenSplice-6.9.210323OSS-HDE-x86_64.linux-gcc7-glibc2.27-installer.tar 
```

Next, run the following commands in **HDE/x86_64.linux/tools/python/src** in the extracted folder to install it.

```
 source ${OPENSPLICE_DIR}/x86_64.linux/release.com
 python3 setup.py build
 sudo su
 # source ${OPENSPLICE_DIR}/x86_64.linux/release.com
 # python3 setup.py install
 # exit
```

If Cython is not installed, run the following command.

```
 sudo apt install python3-pip
 pip3 install cython
```

#### Installing omniORB-python
Install the Python version of omniORB.

```
 sudo su
 # echo "deb http://openrtm.org/pub/Linux/ubuntu/ $code_name main" >> /etc/apt/sources.list
 # wget -O- --secure-protocol=TLSv1_2 --no-check-certificate https://openrtm.org/pub/openrtm.key | apt-key add -
 # apt update
 # apt install python3-omniorb python3-omniorb-omg omniidl-python3
 # exit
```

#### Installing OpenRTM-aist
Install OpenRTM-aist 1.2 or similar using the installer in advance.
Obtain the source code of the Python version of OpenRTM-aist.

- https://github.com/OpenRTM/OpenRTM-aist-Python

Install the Python version of OpenRTM-aist with the following commands.

```
 sudo apt install doxygen
 python3 setup.py build
 sudo python3 setup.py install
```

#### Operation Check
Before operation, run **release.com**.

Create an rtc.conf like the following, load **OpenSpliceTransport.py**, specify **opensplice** as the interface type, and start the RTC.

```
 manager.modules.load_path: /usr/local/lib/python3.6/dist-packages/OpenRTM_aist/ext/transport/OpenSplice
 manager.modules.preload: OpenSpliceTransport.py
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice&marshaling_type=opensplice, ConsoleIn0.out?interface_type=opensplice&marshaling_type=opensplice
```

## Startup Options
### C++

The following options can be set in rtc.conf when starting the OpenRTM-aist manager.
* These options can be used in OpenRTM-aist under development, but may not be implemented in released versions.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Setting Example</th>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>opensplice.uri</td>
    <td>file://OpenSpliceQoSExample.xml</td>
    <td></td>
    <td>Specifies the OpenSplice QoS configuration file.</td>
  </tr>
  <tr>
    <td>opensplice.profile</td>
    <td>testProfile</td>
    <td></td>
    <td>Specifies the QoS profile name.</td>
  </tr>
  <tr>
    <td>opensplice.participant_qos.name</td>
    <td>testParticipant</td>
    <td></td>
    <td>Profile name of the DomainParticipant to load</td>
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
    <td>Profile name of the Publisher to load</td>
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
    <td>Profile name of the Subscriber to load</td>
  </tr>
</table>

A description example is shown below.

```
 opensplice.uri: file://OpenSpliceQoSExample.xml
 opensplice.profile: testProfile
```

### Python

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Setting Example</th>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>opensplice.uri</td>
    <td>file://OpenSpliceQoSExample.xml</td>
    <td></td>
    <td>Specifies the OpenSplice QoS configuration file.</td>
  </tr>
  <tr>
    <td>opensplice.profile</td>
    <td>testProfile</td>
    <td></td>
    <td>Specifies the QoS profile name.</td>
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


A description example is shown below.

```
 opensplice.uri: file://OpenSpliceQoSExample.xml
 opensplice.profile: testProfile
```


## Connection Options
### C++

The options that can be set in the connector profile when connecting data ports are as follows.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Default Value</th>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>opensplice.topic</td>
    <td>chatter</td>
    <td></td>
    <td>Name of the DDS topic</td>
  </tr>
  <tr>
    <td>opensplice.reader_qos.id</td>
    <td></td>
    <td></td>
    <td>Profile name of the Reader to load</td>
  </tr>
  <tr>
    <td>opensplice.writer_qos.id</td>
    <td></td>
    <td></td>
    <td>Profile name of the Writer to load</td>
  </tr>
  <tr>
    <td>opensplice.topic_qos.id</td>
    <td></td>
    <td></td>
    <td>Profile name of the Topic to load</td>
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


A setting example is shown below.

```
 manager.components.preconnect: ConsoleOut0.in?interface_type=opensplice&opensplice.topic=testtopic
```

### Python

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Default Value</th>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>opensplice.topic</td>
    <td>chatter</td>
    <td></td>
    <td>Name of the DDS topic</td>
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


## Other
### OpenSplice Configuration File
The OpenSplice configuration file is set with the environment variable **${OSPL_URI}**.

- [14. Configuration — The OpenSplice Deployment Guide](http://download.prismtech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html)

By default, **${OSPL_URI}/etc/config/ospl.xml** is set.

For example, to change the domain ID, change the following part of ospl.xml.

```
 <OpenSplice>
     <Domain>
         <Name>ospl_sp_ddsi</Name>
         <!-- 以下を変更する -->
         <Id>1</Id>
         <SingleProcess>true</SingleProcess>
```

To output detailed logs, add the following part.

```
    <DDSI2Service name="ddsi2">
        <!-- 以下を追加する -->
        <Tracing>
             <Verbosity>FINEST</Verbosity>
        </Tracing>
        <!-- ここまで -->
        <General>
```

