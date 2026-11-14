---
layout: page
title: "using the ros2 communication feature"
---

<!-- Using the ROS2 Communication Feature -->
#contents

## C++ Version

### Windows

#### Installing Chocolatey

Install it by following the instructions on the following page.

- [Chocolatey](https://chocolatey.org/install#installing-chocolatey)

#### Installing Python3

Install it using the following command.

```
> choco install -y python
```

#### Installing OpenSSL

Download **Win64OpenSSL-1_0_2r.exe** from the following page, then run it to install.

- [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)

Set the following environment variable.

<table class="table-alt">
  <tr>
    <td>OPENSSL_CONF</td>
    <td>C:\OpenSSL-Win64\bin\openssl.cfg</td>
  </tr>
</table>

<br>

Add **C:\OpenSSL-Win64\bin** to the PATH environment variable.

#### Installing asio, eigen, tinyxml, tinyxml-usestl, and log4cxx

Download the NuGet package (**.nupkg**) files from the following page.

- https://github.com/ros2/choco-packages/releases

Install them using the following command. Since additional dependent NuGet packages may be required, modify the command as appropriate.

```
> choco install -y -s <**'Downloaded path**'> asio eigen tinyxml-usestl tinyxml2 log4cxx
```

#### Installing Python Packages

Install them using the following command.

```
> python -m pip install -U catkin_pkg empy pyparsing pyyaml setuptools
```

#### Installing ROS2

Download **ros2-****-********-windows-release-amd64.zip** from the following page.

- https://github.com/ros2/ros2/releases

Extract it to **C:\dev\ros2** or another suitable location to complete the installation.

#### Building OpenRTM-aist

Before running CMake, execute the script to configure the ROS2 environment.

```
> call C:\dev\ros2\local_setup.bat
```

Turn ON the **FASTRTPS_ENABLE** and **ROS2_ENABLE** options when running CMake.

```
> cmake -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc14 -G "Visual Studio 16 2019" -A x64 -DFASTRTPS_ENABLE=ON -DROS2_ENABLE=ON ..
```

The remaining steps are the same as the standard build procedure.

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

Install it to an appropriate location.

Specify the installation directory using the **CMAKE_INSTALL_PREFIX** option.

```
> cmake .. -DCMAKE_INSTALL_PREFIX=C:/workspace/OpenRTM-aist/build_omni/install
> cmake --build . --config Release --target install
```

#### Operation Check

Run the sample components located in **<**'Installation path**'>\2.0.0\Components\C++\Examples\vc14**.

Create an rtc.conf file with the following contents.

```
manager.modules.load_path: {Installation path}\\2.0.0\\ext\\transport
manager.modules.preload: FastRTPSTransport.dll, ROS2Transport.dll
manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps&marshaling_type=ros2:std_msgs/Float32&fast-rtps.topic=chatter, ConsoleIn0.out?interface_type=fast-rtps&marshaling_type=ros2:std_msgs/Float32&fast-rtps.topic=chatter
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: manager.module.load_path | Location where the serializer modules (FastRTPSTransport.dll and ROS2Transport.dll) are stored
: manager.modules.preload | Specifies the order in which the serializer modules are loaded
: manager.components.preconnect | Describes the settings for connector creation. Specify **fast-rtps** for interface_type (interface type), the corresponding serializer name for marshaling_type (marshaling type), and any arbitrary name for fast-rtps.topic (topic).

The relationship between the serializers for ROS/ROS2 and the corresponding ROS/ROS2 message types is shown at the following link.

- [Serializer Names and ROS/ROS2 Message Types]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

Connector creation is configured using the **manager.components.preconnect** option.

In this example, connectors are created for the **in** port of the **ConsoleOut0** component and the **out** port of the **ConsoleIn0** component.

Before execution, add the following directories to the PATH environment variable.

- <**'Installation path**'>\2.0.0\bin\vc14
- <**'Installation path**'>\2.0.0\omniORB\4.2.3_vc14\bin\x86_win32
- C:\dev\ros2\bin
- C:\ProgramData\chocolatey\lib\tinyxml2\lib
- C:\ProgramData\chocolatey\lib\log4cxx\lib

Communication becomes available after running **ConsoleInComp.exe** and **ConsoleOutComp.exe**.

### Ubuntu

#### Installing ROS2

Install it using the following commands.

```
$ curl http://repo.ros2.org/repos.key | sudo apt-key add -
$ sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
$ export ROS_DISTRO=crystal
$ sudo apt update
$ sudo apt install ros-${ROS_DISTRO}-ros-core
```

Configure bash for ROS2 as follows. (This sets up both future bash sessions and the currently running bash session.)

```
echo "source /opt/ros/crystal/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

#### Building OpenRTM-aist

Turn ON the **FASTRTPS_ENABLE** and **ROS2_ENABLE** options when running CMake.

```
$ cmake -DCORBA=omniORB -DCMAKE_BUILD_TYPE=Release -DFASTRTPS_ENABLE=ON -DROS2_ENABLE=ON ..
```

The remaining steps are the same as the standard build procedure.

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

Install it after building.

```
$ cmake --build . --target install
```

#### Operation Check

Create the following rtc.conf.

```
manager.modules.load_path: /usr/local/lib/openrtm-2.0/transport/
manager.modules.preload: FastRTPSTransport.so, ROS2Transport.so
manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps&marshaling_type=ros2:std_msgs/Float32&fast-rtps.topic=chatter, ConsoleIn0.out?interface_type=fast-rtps&marshaling_type=ros2:std_msgs/Float32&fast-rtps.topic=chatter
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: manager.module.load_path | Location where the serializer modules (FastRTPSTransport.so and ROS2Transport.so) are stored
: manager.modules.preload | Specifies the order in which the serializer modules are loaded
: manager.components.preconnect | Describes the settings for connector creation. Specify **fast-rtps** for interface_type (interface type), the corresponding serializer name for marshaling_type (marshaling type), and any arbitrary name for fast-rtps.topic (topic).

The message types supported by the OpenRTM-aist serializers are shown below.

- [Serializer Names and ROS/ROS2 Message Types]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

Start the RTCs to verify operation.

Start each one from a separate terminal.

```
/usr/local/share/openrtm-2.0/components/c++/examples/ConsoleInComp
```

```
/usr/local/share/openrtm-2.0/components/c++/examples/ConsoleOutComp
```

## Python Version

### Windows

Install ROS2 using the same procedure as for the C++ version.

#### Installing OpenRTM-aist

Install OpenRTM-aist 1.2 or later using the installer.

Obtain the source code for the Python version of OpenRTM-aist.

- [Python Source Code](https://github.com/OpenRTM/OpenRTM-aist-Python)

Install the Python version of OpenRTM-aist using the following commands.

```sh
python setup.py build
python setup.py install
```

#### Operation Check

Execute the following command before running.

```sh
call C:\dev\ros2\setup.bat
```

Create an rtc.conf file as shown below, load **ROS2Transport.py**, and start it with **opensplice** specified as the interface type.

```text
manager.modules.load_path: C:\\Python37\\Lib\\site-packages\\OpenRTM_aist\\ext\\transport\\ROS2Transport
manager.modules.preload: ROS2Transport.py
manager.components.preconnect: ConsoleOut0.in?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32&ros2.topic=chatter, ConsoleIn0.out?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32&ros2.topic=chatter
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: manager.module.load_path | Location where the serializer module (ROS2Transport.py) is stored
: manager.modules.preload | Specifies the order in which the serializer module is loaded
: manager.components.preconnect | Describes the settings for connector creation. Specify **ros2** for interface_type (interface type), the corresponding serializer name for marshaling_type (marshaling type), and any arbitrary name for ros2.topic (topic).

### Ubuntu

#### Installing ROS2

Install it using the following commands.

```sh
$ curl http://repo.ros2.org/repos.key | sudo apt-key add -
$ sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
$ export ROS_DISTRO=crystal
$ sudo apt update
$ sudo apt install ros-${ROS_DISTRO}-desktop
```

Configure bash to load the ROS2 environment.

```sh
$ echo "source /opt/ros/crystal/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

```sh
$ sudo apt-get install python-omniorb-omg omniidl-python doxygen
```

#### Installing OpenRTM-aist

Obtain the source code for the Python version of OpenRTM-aist.

- [Python Source Code](https://github.com/OpenRTM/OpenRTM-aist-Python)

Build and install the Python version of OpenRTM-aist using the following commands.

```sh
$ python setup.py build
$ python setup.py install
```

#### Operation Check

Executing ros2's setup.bash appears to overwrite PYTHONPATH, so execute the following commands.

```sh
$ export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/site-packages
$ export PATH=$PATH:/usr/local/lib/python3.6/site-packages/
```

Modify the paths according to the directory where omniORBpy is installed.

Create an rtc.conf file as shown below, load **ROS2Transport.py**, and configure it to start with **ros2** as the interface type and **ros2:std_msgs/Float32** as the serializer.

```text
manager.modules.load_path: /usr/local/lib/python3.6/site-packages/OpenRTM_aist/ext/transport/ROS2Transport/
manager.modules.preload: ROS2Transport.py
manager.components.preconnect: ConsoleOut0.in?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32&ros2.topic=chatter, ConsoleIn0.out?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32&ros2.topic=chatter
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

The message types supported by the OpenRTM-aist serializers are shown below.

- [Serializer Names and ROS/ROS2 Message Types]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

Verify operation by starting the RTCs with the following commands.

```sh
$ python /usr/local/share/openrtm-2.0/components/python/SimpleIO/ConsoleIn.py
```

```sh
$ python /usr/local/share/openrtm-2.0/components/python/SimpleIO/ConsoleOut.py
```

## Startup Options

### C++

Configure the [Fast DDS Communication Feature Options]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/dds_comm_use/fast-rtps#起動時のオプション).

### Python

The following options can be configured.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Example Setting</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>ros2.args</td>
    <td></td>
    <td><strong>args</strong> argument of <code>rclpy.init</code></td>
  </tr>
  <tr>
    <td>ros2.node.name</td>
    <td>node_name</td>
    <td>Node name</td>
  </tr>
</table>

## Connection Options

### C++

Configure the [Fast DDS Communication Feature Options]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/dds_comm_use/fast-rtps#接続時のオプション).

### Python

The items that can be configured at connection time are as follows.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Default Value</th>
    <th>Option</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>marshaling_type</td>
    <td></td>
    <td></td>
    <td>Type of serializer. Values such as <strong>ros:std_msgs/Float32</strong> can be set.</td>
  </tr>
  <tr>
    <td>ros2.topic</td>
    <td>chatter</td>
    <td></td>
    <td>DDS topic name</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, SYSTEM_DEFAULT_QOS</td>
    <td>Durability on the sending side (VOLATILE_DURABILITY_QOS: volatile, TRANSIENT_LOCAL_DURABILITY_QOS: transient local setting)</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.deadline.period.sec</td>
    <td>0</td>
    <td></td>
    <td>Minimum period on the receiving side</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.deadline.period.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUT0TOMATIC_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS, SYSTEM_DEFAULT_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.liveliness.lease_duration.sec</td>
    <td>0</td>
    <td></td>
    <td>Heartbeat period on the receiving side</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.liveliness.lease_duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.reliability.kind</td>
    <td>RELIABLE_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS, SYSTEM_DEFAULT_RELIABILITY_QOS</td>
    <td>Reliability on the receiving side (RELIABLE_RELIABILITY_QOS: high reliability, BEST_EFFORT_RELIABILITY_QOS: maximum speed)</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.history.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS, SYSTEM_DEFAULT_HISTORY_QOS</td>
    <td>How received data is retained (KEEP_ALL_HISTORY_QOS: retain all data, KEEP_LAST_HISTORY_QOS: retain only the number of data items specified)</td>
    <td>KEEP_LAST</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td>Number of data items retained on the receiving side</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.lifespan.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.lifespan.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.avoid_ros_namespace_conventions</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, SYSTEM_DEFAULT_QOS</td>
    <td>Durability on the sending side (VOLATILE_DURABILITY_QOS: volatile, TRANSIENT_LOCAL_DURABILITY_QOS: transient local setting)</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.deadline.period.sec</td>
    <td>0</td>
    <td></td>
    <td>Minimum period on the sending side</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.deadline.period.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>


  <tr>
    <td>ros2.writer_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS, SYSTEM_DEFAULT_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.liveliness.lease_duration.sec</td>
    <td>0</td>
    <td></td>
    <td>Heartbeat period on the sending side</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.liveliness.lease_duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.reliability.kind</td>
    <td>RELIABLE_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS, SYSTEM_DEFAULT_RELIABILITY_QOS</td>
    <td>Reliability on the sending side (RELIABLE_RELIABILITY_QOS: high reliability, BEST_EFFORT_RELIABILITY_QOS: maximum speed)</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.history.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS, SYSTEM_DEFAULT_HISTORY_QOS</td>
    <td>How sent data is retained (KEEP_ALL_HISTORY_QOS: retain all data, KEEP_LAST_HISTORY_QOS: retain only the number of data items specified)</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td>Number of data items retained on the sending side</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.lifespan.duration.sec</td>
    <td>0</td>
    <td></td>
    <td>Retention time for unsent data on the sending side</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.lifespan.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.avoid_ros_namespace_conventions</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
</table>

The following shows a configuration example.

```
manager.components.preconnect: ConsoleOut0.in?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32, ConsoleIn0.out?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32
```

## Simple Operation Check

When OpenRTM-aist is built and installed, a configuration file for a simple operation check of ROS2Transport is installed.

```
D:\ros2-windows\setup.bat
%RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
%RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\transport\rtc.ros2.conf
```

```
source /opt/ros/dashing/setup.sh
source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/transport/rtc.ros2.conf
```

