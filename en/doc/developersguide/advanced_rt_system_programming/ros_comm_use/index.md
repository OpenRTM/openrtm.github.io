---
layout: page
title: "using ros communication features"
---

<!-- Title: ROS通信機能の利用 -->
#contents

## C++ Version

### Windows

#### Installing ROS

Follow the instructions on the following website to install Ros4Win onto a USB drive.

- [Ros4Win](http://hara-jp.com/_default/en/Topics/ROS_Windows_Install.html)

If **rpt** does not work correctly because the repository URL has changed, first modify the **src\rpt\ros4win.py** file if it has not already been updated.

```python
#PKG_REPO_BASE="http://hara.jpn.com/cgi/" #Before modification
PKG_REPO_BASE="http://hara-jp.com/cgi/"  #After modification
```

Install Ros4Win using the following commands.

```sh
git clone https://github.com/haraisao/rpt
cd rqt
python src\rpt\rpt.py update
python src\rpt\rpt.py install ros_base
python src\rpt\rpt.py install ros_setup
```

#### Building OpenRTM-aist

First, set the **CMAKE_PREFIX_PATH** and **ROS_HOME_DRIVE** environment variables with the following commands.

The following example assumes that the USB drive is mounted as drive **D:**. If your USB drive is assigned a different drive letter, replace **D:** with the appropriate drive letter.

```sh
set ROS_HOME_DRIVE=D:
set CMAKE_PREFIX_PATH=%CMAKE_PREFIX_PATH%;%ROS_HOME_DRIVE%/opt/ros/melodic/share
```

Before proceeding with the remaining steps, configure the ROS environment with the following command.

```sh
D:\opt\ros\melodic\ros_setup.bat
```

Enable the **ROS_ENABLE** option when running CMake.

```sh
cmake -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc14 -DCORBA=omniORB -G "Visual Studio 16 2019" -A x64 -DROS_ENABLE=ON ..
```

The remaining steps are the same as the standard build procedure.

- [Building OpenRTM-aist]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

After building, install OpenRTM-aist.

```sh
cmake --build . --config Release --target install
```

#### Operation Check

Create the following **rtc.conf**.

```conf
manager.modules.load_path: C:\\workspace\\openrtm\\build_omni\\devel\\bin\\Release
manager.modules.preload: ROSTransport.dll
manager.components.preconnect: ConsoleOut0.in?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleOut0, ConsoleIn0.out?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleIn0
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: **manager.modules.load_path** | Specifies the location of the serializer module (**ROSTransport.dll**).

: **manager.modules.preload** | Specifies the serializer module used for ROS communication. On Windows, specify **ROSTransport.dll**.

: **manager.components.preconnect** | Configures connector creation. Set **ros** for **interface_type**, specify the corresponding serializer name for **marshaling_type**, and assign any desired topic name to **ros.topic**.

The message types supported by the OpenRTM-aist serializer module (**ROSTransport.dll**) are listed below.

- [Serializer Names and ROS/ROS2 Message Types]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

Start the RTCs to verify operation.

Launch **Clink** with the following command.

```sh
D:\opt\start_ros.bat
```

Perform the remaining steps from the Clink environment.

Run the following files.
Place the modified **rtc.conf** in the same directory as the executable file corresponding to the Visual Studio version specified when OpenRTM-aist was installed (by default, under the **VC14** directory in **Examples**).

```sh
${OpenRTM_INSTALL_DIR}\2.0\Components\C++\Examples\ConsoleInComp.exe
${OpenRTM_INSTALL_DIR}\2.0\Components\C++\Examples\ConsoleOutComp.exe
```

### Ubuntu

#### Installing ROS

Install ROS using the following commands.

```sh
$ export ROS_DISTRO=melodic
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
$ sudo apt-get -y update
$ sudo apt-get -y install ros-${ROS_DISTRO}-ros-base
$ sudo rosdep init
$ rosdep update
```

Configure your shell for ROS as follows. This configures both future bash sessions and the currently running shell.

```sh
$ echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

#### Building OpenRTM-aist

Enable the **ROS_ENABLE** option when running CMake.

```sh
$ cmake -DCORBA=omniORB -DCMAKE_BUILD_TYPE=Release -DROS_ENABLE=ON ..
```

The remaining steps are the same as the standard build procedure.

- [Building OpenRTM-aist]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

After building, install OpenRTM-aist.

```sh
$ cmake --build . --target install
```

#### Operation Check

Create the following **rtc.conf**.
Place this file in the current working directory from which the following RTC components will be started.

```conf
manager.modules.load_path: /usr/local/lib/openrtm-2.0/transport/
manager.modules.preload: ROSTransport.so
manager.components.preconnect: ConsoleOut0.in?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleOut0, ConsoleIn0.out?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleIn0
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: **manager.modules.load_path** | Specifies the location of the serializer module (**ROSTransport.so**).

: **manager.modules.preload** | Specifies the serializer module used for ROS communication. On Ubuntu, specify **ROSTransport.so**.

: **manager.components.preconnect** | Configures connector creation. Set **ros** for **interface_type**, specify the corresponding serializer name for **marshaling_type**, and assign any desired topic name to **ros.topic**.

The message types supported by the OpenRTM-aist serializer module (**ROSTransport.so**) are listed below.

- [Serializer Names and ROS/ROS2 Message Types]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

Start **ConsoleInComp** and **ConsoleOutComp** to verify operation.

Start each component from a separate terminal.

```sh
$ /usr/local/share/openrtm-2.0/components/c++/examples/ConsoleInComp
```

```sh
$ /usr/local/share/openrtm-2.0/components/c++/examples/ConsoleOutComp
```

## Python Version

### Windows

#### Installing ROS

Install ROS on a USB drive by following the instructions on the following page.

- [ROS_Windows_Install](http://www.hara-jp.com/_default/en/Topics/ROS_Windows_Install.html)

#### Installing OpenRTM-aist

Install OpenRTM-aist 1.2 or later using the installer.

Obtain the OpenRTM-aist Python source code.

- [OpenRTM-aist Python Source Code](https://github.com/OpenRTM/OpenRTM-aist-Python)

Install the OpenRTM-aist Python version with the following commands.

```sh
python setup.py build
python setup.py install
```

#### Operation Check

Run **start_ros.bat** twice to open two command windows configured for the ROS environment.

```sh
D:\opt\start_ros.bat
```

In one of the windows, start **roscore**.

```sh
roscore
```

In the other window, add the directory where OpenRTM-aist is installed to **PYTHONPATH**.

```sh
set PYTHONPATH=%PYTHONPATH%;C:\Python37\Lib\site-packages;C:\Python37\Lib\site-packages\OpenRTM_aist;C:\Python37\Lib\site-packages\OpenRTM_aist\utils;C:\Python37\Lib\site-packages\OpenRTM_aist\RTM_IDL
```

Create the following **rtc.conf**.
(Create **rtc.conf** in the directory from which the RTC executable is run. If you use the sample batch files, place it in the directory containing the executable started by the batch file.)

```conf
manager.modules.load_path: C:\\Python37\\Lib\\site-packages\\OpenRTM_aist\\ext\\transport\\ROSTransport
manager.modules.preload: ROSTransport.py
manager.components.preconnect: ConsoleOut0.in?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleOut0, ConsoleIn0.out?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleIn0
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: **manager.modules.load_path** | Specifies the location of the serializer module (**ROSTransport.py**).

: **manager.modules.preload** | Specifies the serializer module used for ROS communication. For Python, specify **ROSTransport.py**.

: **manager.components.preconnect** | Configures connector creation. Set **ros** for **interface_type**, specify the corresponding serializer name for **marshaling_type**, and assign any desired topic name to **ros.topic**.

The message types supported by the OpenRTM-aist serializer module (**ROSTransport.py**) are listed below.

- [Serializer Names and ROS/ROS2 Message Types]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

Start the RTCs using the above **rtc.conf** to verify operation.


### Ubuntu

#### Installing ROS

Install ROS by following the same procedure as for the C++ version.

#### Installing OpenRTM-aist

Install the following packages.

```sh
$ sudo apt-get install python-omniorb-omg omniidl-python doxygen
```

Install the Python version of OpenRTM-aist with the following commands.

```sh
$ git clone https://github.com/OpenRTM/OpenRTM-aist-Python
$ cd OpenRTM-aist-Python
$ python setup.py build
$ sudo python setup.py install
```

#### Operation Check

Create the following **rtc.conf**.
(Create **rtc.conf** in the current working directory from which the RTC is executed.)

```conf
manager.modules.load_path: /usr/local/lib/python2.7/dist-packages/OpenRTM_aist/ext/transport/ROSTransport/
manager.modules.preload: ROSTransport.py
manager.components.preconnect: ConsoleOut0.in?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleOut0, ConsoleIn0.out?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleIn0
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: **manager.modules.load_path** | Specifies the location of the serializer module (**ROSTransport.py**).

: **manager.modules.preload** | Specifies the serializer module used for ROS communication. For Python, specify **ROSTransport.py**.

: **manager.components.preconnect** | Configures connector creation. Set **ros** for **interface_type**, specify the corresponding serializer name for **marshaling_type**, and assign any desired topic name to **ros.topic**.

The message types supported by the OpenRTM-aist serializer module (**ROSTransport.py**) are listed below.

- [Serializer Names and ROS/ROS2 Message Types]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

Start the RTCs with the following commands to verify operation.

```sh
$ python /usr/local/share/openrtm-2.0/components/python/SimpleIO/ConsoleIn.py
```

```sh
$ python /usr/local/share/openrtm-2.0/components/python/SimpleIO/ConsoleOut.py
```

## Connection Options

### C++

The following options can be specified in the connector profile when connecting data ports.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Default Value</th>
    <th>Available Values</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>marshaling_type</td>
    <td></td>
    <td></td>
    <td>Serializer type. Values such as <strong>ros:std_msgs/Float32</strong> can be specified.</td>
  </tr>
  <tr>
    <td>ros.topic</td>
    <td>chatter</td>
    <td></td>
    <td>Topic name</td>
  </tr>
  <tr>
    <td>ros.roscore.host</td>
    <td>localhost</td>
    <td></td>
    <td>Host name of the ROS Master</td>
  </tr>
  <tr>
    <td>ros.roscore.port</td>
    <td>11311</td>
    <td></td>
    <td>Port number of the ROS Master</td>
  </tr>
  <tr>
    <td>ros.node.name</td>
    <td></td>
    <td></td>
    <td>Name of the ROS node</td>
  </tr>
  <tr>
    <td>ros.node.anonymous</td>
    <td>NO</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.so_keepalive</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_nodelay</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td>YES: Set the ROS node name to a UUID. NO: Set the ROS node name to <strong>rtcomp</strong>.</td>
  </tr>
  <tr>
    <td>ros.tcp_keepcnt</td>
    <td>9</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_keepidle</td>
    <td>60</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_keepintvl</td>
    <td>10</td>
    <td></td>
    <td></td>
  </tr>
</table>


### Python

The following options can be specified in the connector profile when connecting data ports.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Default Value</th>
    <th>Available Values</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>marshaling_type</td>
    <td></td>
    <td></td>
    <td>Serializer type. Values such as <strong>ros:std_msgs/Float32</strong> can be specified.</td>
  </tr>
  <tr>
    <td>ros.topic</td>
    <td>chatter</td>
    <td></td>
    <td>Topic name</td>
  </tr>
  <tr>
    <td>ros.roscore.host</td>
    <td>localhost</td>
    <td></td>
    <td>Host name of the ROS Master</td>
  </tr>
  <tr>
    <td>ros.roscore.port</td>
    <td>11311</td>
    <td></td>
    <td>Port number of the ROS Master</td>
  </tr>
  <tr>
    <td>ros.node.name</td>
    <td></td>
    <td></td>
    <td>Name of the ROS node</td>
  </tr>
  <tr>
    <td>ros.node.anonymous</td>
    <td>NO</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.so_reuseaddr</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.so_keepalive</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_nodelay</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td>YES: Set the ROS node name to a UUID. NO: Set the ROS node name to <strong>rtcomp</strong>.</td>
  </tr>
  <tr>
    <td>ros.tcp_keepcnt</td>
    <td>9</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_keepidle</td>
    <td>60</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_keepintvl</td>
    <td>10</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.sock.timeout</td>
    <td>60</td>
    <td></td>
    <td></td>
  </tr>
</table>

## Simple Operation Check

When OpenRTM-aist is built and installed, a configuration file for a simple operation check of **ROSTransport** is also installed.

Start **roscore** with the following commands.

### Windows

```sh
D:\opt\ros\melodic\ros_setup.bat
roscore
```

Start **ConsoleOutComp** using the following commands.

```sh
D:\opt\ros\melodic\ros_setup.bat
%RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
%RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\transport\rtc.ros.conf
```

### Ubuntu

Start **roscore** with the following commands.

```sh
source /opt/ros/melodic/setup.bash
roscore
```

Start **ConsoleOutComp** using the following commands.

```sh
source /opt/ros/melodic/setup.bash
source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/transport/rtc.ros.conf
```

