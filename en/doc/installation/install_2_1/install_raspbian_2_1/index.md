---
layout: page
title: installation on raspberry pi os
---

<!-- Title: Raspberry Pi OSへのインストール -->

#contents

## Supported Version

The currently supported version of Raspberry Pi OS is:

- Bookworm (64-bit)

## Preparing the SD Card

To write the OS image, it is convenient to use Raspberry Pi Imager, which can be downloaded from the official website.<br>
https://www.raspberrypi.com/software/

You can select and download the following options:

- Base Debian GNU/Linux version (Latest / Legacy)
- GUI option (Desktop / Lite)
- System architecture (32-bit / 64-bit)

## Changes in Version 2.1

You can now install the new [SSM Communication Feature]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ssm_comm_use).<br>
Since the SSM library is statically linked, you do not need to install SSM separately. The following files are installed by the openrtm2-ssm-tp deb package.

```
 usr/
 ├── bin
 │   ├── killssm
 │   ├── lsssm
 │   ├── psssm
 │   ├── ssm-advance-player
 │   ├── ssm-coordinator
 │   ├── ssm-date
 │   ├── ssm-graph
 │   ├── ssm-logger
 │   ├── ssm-monitor
 │   ├── ssm-player
 │   ├── ssm-proxy
 │   ├── ssm-transporter
 │   └── topssm
 ├── etc
 │   └── transport
 │       └── rtc.ssm.conf
 └── share
     └── openrtm-2.1
         └── transport
             └── SSMTransport.so
```

This feature is **not** installed when the "Bulk Installation Script" described in the next section is executed without any options.<br>
It can be installed by specifying the option `-l c++ --ssm`. You can check the available options with `--help`.

## Bulk Installation Script

To install Version 2.1, paste and execute the following command at the shell prompt. It installs the C++ edition, Python edition, Java edition, rtshell, and JDK 8. The script is not saved locally.<br>
*Even if multiple Java versions are installed, the default Java version is automatically switched to Java 8.*<br>

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh)
```

The following packages will be installed.

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

The installation of rtshell fails when using the default pip version.<br>
Follow the yellow message displayed by the installation script and add the following lines to `/etc/pip.conf` (create the file if it does not exist).

```
 $ vi /etc/pip.conf
 [global]
 break-system-packages = true
```

After applying the above setting, run the installation script again to install rtshell.

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python        2.1.0
 rtctree-aist                       4.2.5
 rtshell-aist                       4.2.10
 rtsprofile-aist                    4.1.6
```

By specifying options, you can install packages that match your requirements. The available options can be checked with the following command.

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh) --help
```

## Package Details

The contents of each package are as follows.

### openrtm2

openrtm-aist includes runtime libraries and commands.

- Commands
```
 /usr/bin/openrtmNames
 /usr/bin/rtcd2
 /usr/bin/rtcprof2
 /usr/bin/rtm2-config
```

- Sample configuration files
```
 /usr/etc/rtc.conf.sample2
 /usr/etc/rtc.names.ssl.conf
 /usr/etc/ssl/rtc.ssl.conf
 /usr/lib/aarch64-linux-gnu/pkgconfig/openrtm2.pc
```

- Libraries, etc.
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

Includes the commands and headers required for development.

- Commands
```
 /usr/bin/rtm2-skelwrapper
```

- Headers
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

- Libraries and other files
```
 /usr/lib/aarch64-linux-gnu/cmake/openrtm-2.1/OpenRTMConfig.cmake
 /usr/lib/aarch64-linux-gnu/cmake/openrtm-2.1/OpenRTMConfigVersion.cmake
 /usr/share/openrtm-2.1/py_helper/skel_wrapper.py
 /usr/share/openrtm-2.1/py_helper/yat.py
```
````

```markdown
## Part 2/2

### openrtm2-idl

- IDL files, etc.
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

openrtm-aist-example includes samples of standalone RTCs, loadable RTCs, and the source code for the sample RTCs.

- Samples (standalone RTCs)
```

/usr/share/openrtm-2.1/components/c++/examples/CompositeComp
/usr/share/openrtm-2.1/components/c++/examples/ConfigSampleComp
中略
/usr/share/openrtm-2.1/components/c++/examples/rtc.conf

```

- Samples (loadable RTCs)
```

/usr/share/openrtm-2.1/components/c++/examples/rtc/ConfigSample.so
/usr/share/openrtm-2.1/components/c++/examples/rtc/ConsoleIn.so
中略
/usr/share/openrtm-2.1/components/c++/examples/rtc/Throughput.so

```

### openrtm2-doc

openrtm-aist-doc includes Japanese and English class references and IDL interface definition references.

- Class reference
```

/usr/share/openrtm-2.1/doc/c++/ClassReference/html/BufferBase_8h.html
/usr/share/openrtm-2.1/doc/c++/ClassReference/html/BufferBase_8h__dep__incl.map
中略
/usr/share/openrtm-2.1/doc/c++/ClassReference/html/structSDOPackage_1_1Organization__impl_1_1sdo__id.html

```

- IDL reference
```

/usr/share/openrtm-2.1/doc/idl/IDLReference/html/BasicDataType_8idl.html
/usr/share/openrtm-2.1/doc/idl/IDLReference/html/BasicDataType_8idl_dep_incl.map
中略
/usr/share/openrtm-2.1/doc/idl/IDLReference/html/unionSDOPackage_1_1Numeric.html

```

- Class reference (English)
```

/usr/share/openrtm-2.1/doc/c++/ClassReference-en/html/BufferBase_8h.html
/usr/share/openrtm-2.1/doc/c++/ClassReference-en/html/BufferBase_8h__dep__incl.map
中略
/usr/share/openrtm-2.1/doc/C++/ClassReference-en/html/version_8h_source.html

```

- IDL reference (English)
```

/usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
/usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/BasicDataType_8idl__dep__incl.map
中略
/usr/share/openrtm-2.1/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html

```

### openrtm2-python3

- Commands
```

/usr/bin/rtcd2_python3
/usr/bin/rtcprof2_python3

```

- Python modules for OpenRTM-aist
```

/usr/lib/python3/dist-packages/OpenRTM_aist/*

```

- Python search path file for OpenRTM-aist
```

/usr/lib/python3/dist-packages/OpenRTM-aist.pth

```

- Utilities
```

/usr/lib/python3/dist-packages/OpenRTM_aist/utils/**init**.py
/usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtc-template/*
/usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcd/*
/usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcprof/*
/usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtm-naming/*

```

### openrtm2-python3-example

```

/usr/share/openrtm-2.1/components/python3/**init**.py
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


