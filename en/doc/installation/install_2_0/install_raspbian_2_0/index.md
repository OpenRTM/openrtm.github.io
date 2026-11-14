---
layout: page
title: installation on raspberry pi os
---

<hr>
<!-- Title: Raspberry Pi OSへのインストール -->

#contents

## Supported Versions

The versions of Raspberry Pi OS for which packages are currently available are

- Bullseye (32bit / 64bit)
- Bookworm (32bit / 64bit)

.

## Preparing the SD Card

For writing the OS image, it is convenient to use Raspberry Pi Imager, a tool that can be downloaded from the official website.<br>
https://www.raspberrypi.com/software/


You can select the following items to download and write the image.
- Base Debian GNU/Linux version (latest / Legacy)
- Whether GUI is included (Desktop / Lite)
- System architecture (32-bit / 64-bit)

## Changes in the 2.0 Series

C++ can now coexist between the 1.2 series and the 2.0 series. However, the 1.2 series can be installed only on Buster (32bit). <br>
With this support, the following installation-related items have changed.

- The deb package names for the 2.0 series have been changed
- Python and Java cannot coexist between the 1.2 series and the 2.0 series
  - If you use the batch installation script, installed different versions are automatically uninstalled
- The batch installation scripts for the 1.2 series and the 2.0 series have been separated
  - Installation of the 1.2 series: pkg_install_raspbian.sh
  - Installation of the 2.0 series: openrtm2_install_raspbian.sh

In addition, the installation scripts (for both the 1.2 series and the 2.0 series) now support batch processing from download to installation.

## Batch Installation Script

To install the 2.0 series, paste the following into the shell prompt and execute it. The C++ version, Python version, Java version, rtshell, and JDK8 (32-bit environment only) will be installed. The script is not saved locally.<br>
* In a 32-bit environment, even if multiple versions of Java are installed by running the script, it is switched to use Java 8. <br>
* For a 64-bit environment, see the following. <br>
- [Installing JDK8: Methods Other Than Obtaining Packages from the Repository]({{ site.baseurl }}/en/doc/installation/common/install_jdk8#toc9)

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh)
```

The following packages are installed by this execution. (For the 32bit version)

```
 $ dpkg -l | grep openrt
 ii  openrtm2:armhf                     2.0.1-0                         armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:armhf               2.0.1-0                         armhf        OpenRTM-aist headers for development
 ii  openrtm2-doc                         2.0.1-0                         all          Documentation for openrtm2
 ii  openrtm2-example:armhf        2.0.1-0                         armhf        OpenRTM-aist examples
 ii  openrtm2-idl:armhf                 2.0.1-0                         armhf        OpenRTM-aist idls for development
 ii  openrtm2-java:armhf               2.0.1-0                        armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-doc                  2.0.1-0                        all          Documentation for openrtm2-java
 ii  openrtm2-java-example:armhf  2.0.1-0                       armhf        OpenRTM-aist-Java examples
 ii  openrtm2-python3                  2.0.1-0                         armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-doc            2.0.1-0                         all          Documentation for openrtm2-python3
 ii  openrtm2-python3-example     2.0.1-0                         armhf        OpenRTM-aist-Python examples
```

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python 2.0.1
 rtctree-aist        4.2.3
 rtshell-aist         4.2.9
 rtsprofile-aist     4.1.5
```

## Package Details
The contents of each package are as follows.
### openrtm2
openrtm-aist includes runtime libraries and commands.

- Commands
```
 /usr/bin/rtcd2
 /usr/bin/rtcprof2
 /usr/bin/rtm2-config
 /usr/bin/rtm2-naming
```

- Configuration file samples
```
 /usr/etc/rtc.conf.sample2
 /usr/etc/rtc.names.ssl.conf
 /usr/etc/ssl/rtc.ssl.conf
 /usr/lib/arm-linux-gnueabihf/pkgconfig/openrtm2.pc
```


- Libraries, etc.
```
 /usr/lib/arm-linux-gnueabihf/libRTC2.a
 /usr/lib/arm-linux-gnueabihf/libRTC2.so.2.0.0
 中略
 /usr/lib/arm-linux-gnueabihf/librtmCamera2.so
 /usr/lib/arm-linux-gnueabihf/librtmManipulator2.so
 中略
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/ec/LogicalTimeTriggeredEC.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/local_service/FileNameservice.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/sdo/ComponentObserverConsumer.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/sdo/ExtendedFsmServiceProvider.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/sdo/LoggerConsumer.so
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/ssl/SSLTransport.so
 中略
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/sdo/LoggerConsumer.so.0.0.0
 /usr/lib/libfluent-bit.so
```

### openrtm2-dev
This package includes commands and headers required for development.

- Command
```
 /usr/bin/rtm2-skelwrapper
```

- Headers
```
 /usr/include/coil-2.0/coil/Affinity.h
 /usr/include/coil-2.0/coil/Async.h
 中略
 /usr/include/openrtm-2.0/rtm/BufferBase.h
 /usr/include/openrtm-2.0/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-2.0/rtm/config_rtc.h
 /usr/include/openrtm-2.0/rtm/idl/BasicDataType.hh 
 /usr/include/openrtm-2.0/rtm/idl/BasicDataTypeSkel.h
 中略
 /usr/include/openrtm-2.0/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-2.0/rtm/version.h
```

- Libraries and other files
```
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/cmake/OpenRTMConfig.cmake
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/cmake/OpenRTMConfigVersion.cmake
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/py_helper/skel_wrapper.py
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/py_helper/yat.py
```

### openrtm2-idl
- idl files, etc.
```
 /etc/profile.d/openrtm2-idl.sh
 /usr/include/openrtm-2.0/rtm/idl/BasicDataType.idl
 /usr/include/openrtm-2.0/rtm/idl/CameraCommonInterface.idl
 中略
 /usr/include/openrtm-2.0/rtm/idl/SharedMemory.idl
 /usr/share/openrtm-2.0/idl/BasicDataType.idl
 /usr/share/openrtm-2.0/idl/CameraCommonInterface.idl
 中略
 /usr/share/openrtm-2.0/idl/SharedMemory.idl
```

### openrtm2-example
openrtm-aist-example includes samples of both standalone RTCs and loadable RTCs, as well as the source code for sample RTCs.

- Samples (standalone RTCs)
```
 /usr/share/openrtm-2.0/components/c++/examples/CompositeComp
 /usr/share/openrtm-2.0/components/c++/examples/ConfigSampleComp
 中略
 /usr/share/openrtm-2.0/components/c++/examples/rtc.conf
```

- Samples (loadable RTCs)
```
 /usr/share/openrtm-2.0/components/c++/examples/rtc/ConfigSample.so
 /usr/share/openrtm-2.0/components/c++/examples/rtc/ConsoleIn.so
 中略
 /usr/share/openrtm-2.0/components/c++/examples/rtc/Throughput.so
```

### openrtm2-doc
openrtm-aist-doc includes Japanese and English class references and IDL interface definition references.

- Class reference
```
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/BufferBase_8h.html
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/structSDOPackage_1_1Organization__impl_1_1sdo__id.html
```

- IDL reference
```
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/BasicDataType_8idl_dep_incl.map
 中略
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/unionSDOPackage_1_1Numeric.html
```

- Class reference (English)
```
 /usr/share/openrtm-2.0/doc/c++/ClassReference-en/html/BufferBase_8h.html
 /usr/share/openrtm-2.0/doc/c++/ClassReference-en/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/C++/ClassReference-en/html/version_8h_source.html
```

- IDL reference (English)
```
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/BasicDataType_8idl__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
```

### openrtm2-python3

- Commands
```
 /usr/bin/rtcd2_python3
 /usr/bin/rtcprof2_python3
```

- Python modules of the OpenRTM-aist main body
```
 /usr/lib/python3/dist-packages/OpenRTM_aist/* 
```
- Python search path file for OpenRTM-aist
```
 /usr/lib/python3/dist-packages/OpenRTM-aist.pth 
```
- Utilities
```
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/__init__.py
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtc-template/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcd/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcprof/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtm-naming/*
```

### openrtm2-python3-example

```
 /usr/share/openrtm-2.0/components/python3/__init__.py
 /usr/share/openrtm-2.0/components/python3/component.conf
 /usr/share/openrtm-2.0/components/python3/rtcd.conf
 /usr/share/openrtm-2.0/components/python3/AutoControl/*
 /usr/share/openrtm-2.0/components/python3/AutoTest/*
 /usr/share/openrtm-2.0/components/python3/CSPSample/*
 /usr/share/openrtm-2.0/components/python3/CSPSelectSample/*
 /usr/share/openrtm-2.0/components/python3/CSPStaticFsmSample/*
 /usr/share/openrtm-2.0/components/python3/Composite/*
 /usr/share/openrtm-2.0/components/python3/ConfigSample/*
 /usr/share/openrtm-2.0/components/python3/ExtTrigger/*
 /usr/share/openrtm-2.0/components/python3/MobileRobotCanvas/*
 /usr/share/openrtm-2.0/components/python3/SeqIO/*
 /usr/share/openrtm-2.0/components/python3/Serializer/*
 /usr/share/openrtm-2.0/components/python3/SimpleIO/*
 /usr/share/openrtm-2.0/components/python3/SimpleService/*
 /usr/share/openrtm-2.0/components/python3/Slider_and_Motor/*
 /usr/share/openrtm-2.0/components/python3/Throughput/*
 /usr/share/openrtm-2.0/components/python3/TkJoyStick/
 /usr/share/openrtm-2.0/components/python3/TkLRFViewer/*
```

### openrtm2-python3-doc
Installs English and Japanese class references.

- Class reference
```
 /usr/share/openrtm-2.0/doc/python3/ClassReference-en/html/_async_8py.html
 /usr/share/openrtm-2.0/doc/python3/ClassReference-en/html/_buffer_base_8py.html
 中略
 /usr/share/openrtm-2.0/doc/python3/ClassReference-jp/html/_async_8py.html
 /usr/share/openrtm-2.0/doc/python3/ClassReference-jp/html/_buffer_base_8py.html
 /usr/share/openrtm-2.0/doc/python3/ClassReference-jp/html/_buffer_status_8py.html
 以下略
```

### openrtm2-java

```
 /etc/profile.d/openrtm-java.sh
 /usr/bin/rtcd2_java
 /usr/bin/rtcprof2_java
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/License.txt
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/LogicalTimeTriggeredEC.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/NameserviceFile.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/OpenRTM-aist-2.0.1.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/commons-cli-1.1.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/jna-4.2.2.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/jna-platform-4.2.2.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/rtcd.jar
 /usr/lib/arm-linux-gnueabihf/openrtm-2.0/jar/rtcprof.jar
```

### openrtm2-java-example

Java sample RTCs, Class files, source files, and startup scripts

```
 /usr/share/openrtm-2.0/components/java/* 
 /usr/share/openrtm-2.0/components/java/RTMExamples/AutoTest/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/Composite/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/ConfigSample/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/ExtTrigger/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/Fsm/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/GUIIn/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/GUIIn/control/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/GUIIn/model/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/GUIIn/view/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/MyService.idl
 /usr/share/openrtm-2.0/components/java/RTMExamples/SeqIO/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/SeqIO/view/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/SimpleIO/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/SimpleService/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/SinCosOut/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/StaticFsm/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/Throughput/*
 /usr/share/openrtm-2.0/components/java/RTMExamples/TopicTest/*
```
