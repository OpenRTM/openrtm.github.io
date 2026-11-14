---
layout: page
title: detailed contents of openrtm-aist-2.0 deb packages
---

<hr>

<!-- OpenRTM-aist-2.0 debパッケージの詳しい内容 -->

#contents

## Detailed Contents of OpenRTM-2.0 deb Packages

The contents of each package are as follows.

### openrtm2
openrtm2 includes runtime libraries and commands.

- Commands
```
 /usr/bin/rtcd2
 /usr/bin/rtcprof2
 /usr/bin/rtm2-config
 /usr/bin/rtm2-naming
```

- Configuration file samples
```
 /usr/etc/logger/rtc.fluentbit_stream.conf
 /usr/etc/rtc.conf.sample2
 /usr/etc/rtc.names.ssl.conf
 /usr/etc/ssl/rtc.ssl.conf
 /usr/lib/x86_64-linux-gnu/pkgconfig/openrtm2.pc
```

- Libraries, etc.
```
 /usr/lib/x86_64-linux-gnu/libRTC2.a
 /usr/lib/x86_64-linux-gnu/libRTC2.so.2.0.0
 中略
 /usr/lib/x86_64-linux-gnu/librtmCamera2.so
 /usr/lib/x86_64-linux-gnu/librtmManipulator2.so
 中略
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/ec/LogicalTimeTriggeredEC.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/local_service/FileNameservice.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/logger/FluentBit.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/sdo/ComponentObserverConsumer.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/sdo/ExtendedFsmServiceProvider.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/sdo/LoggerConsumer.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/ssl/SSLTransport.so
```

### openrtm2-dev
openrtm2-dev includes commands and headers required for development.

- Commands
```
 /usr/bin/rtm2-skelwrapper
```

- Headers, etc.
```
 /usr/include/coil-2.0/coil/Affinity.h
 /usr/include/coil-2.0/coil/Async.h
 中略
 /usr/include/openrtm-2.0/rtm/BufferBase.h
 /usr/include/openrtm-2.0/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-2.0/rtm/config_rtc.h
 /usr/include/openrtm-2.0/rtm/ext/FastRTPSMessageInfo.h
 /usr/include/openrtm-2.0/rtm/ext/ROSMessageInfo.h
 /usr/include/openrtm-2.0/rtm/idl/BasicDataType.hh 
 /usr/include/openrtm-2.0/rtm/idl/BasicDataTypeSkel.h
 中略
 /usr/include/openrtm-2.0/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-2.0/rtm/version.h
```

- Libraries and others
```
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/cmake/OpenRTMConfig.cmake
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/cmake/OpenRTMConfigVersion.cmake
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/py_helper/skel_wrapper.py
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/py_helper/yat.py
```

### openrtm2-example
openrtm2-example includes samples for both standalone RTCs and loadable RTCs.

- Samples (Standalone RTCs)
```
 /usr/share/openrtm-2.0/components/c++/examples/CompositeComp
 /usr/share/openrtm-2.0/components/c++/examples/ConfigSampleComp
 中略
 /usr/share/openrtm-2.0/components/c++/examples/rtc.conf
```

- Samples (Loadable RTCs)
```
 /usr/share/openrtm-2.0/components/c++/examples/rtc/ConfigSample.so
 /usr/share/openrtm-2.0/components/c++/examples/rtc/ConsoleIn.so
 中略
 /usr/share/openrtm-2.0/components/c++/examples/rtc/Throughput.so
```

### openrtm2-ros-tp

Installs the ROS communication function library.

```
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/transport/ROSTransport.so
```

### openrtm2-ros2-tp

Installs ROS2 communication function libraries.

```
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/transport/FastRTPSTransport.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/transport/ROS2Transport.so
```

### openrtm2-doc
openrtm2-doc includes Japanese and English class references and IDL interface definition references.

- Class Reference
```
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/BufferBase_8h.html
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/c++/ClassReference/html/structSDOPackage_1_1Organization__impl_1_1sdo__id.html
```

- IDL Reference
```
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/BasicDataType_8idl_dep_incl.map
 中略
 /usr/share/openrtm-2.0/doc/idl/IDLReference/html/unionSDOPackage_1_1Numeric.html
```

- Class Reference (English)
```
 /usr/share/openrtm-2.0/doc/c++/ClassReference-en/html/BufferBase_8h.html
 /usr/share/openrtm-2.0/doc/c++/ClassReference-en/html/BufferBase_8h__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/C++/ClassReference-en/html/version_8h_source.html
```

- IDL Reference (English)
```
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/BasicDataType_8idl.html
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/BasicDataType_8idl__dep__incl.map
 中略
 /usr/share/openrtm-2.0/doc/idl/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
```

### openrtm2-idl

- IDL files, etc.
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

### openrtm2-python3

- Commands
```
 /usr/bin/rtcd2_python3
 /usr/bin/rtcprof2_python3
```

- Python modules of OpenRTM-aist
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

- Class Reference
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
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/License.txt
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/LogicalTimeTriggeredEC.jar
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/NameserviceFile.jar
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/OpenRTM-aist-2.0.0.jar
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/commons-cli-1.1.jar
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/jna-4.2.2.jar
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/jna-platform-4.2.2.jar
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/rtcd.jar
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/jar/rtcprof.jar
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

### openrtm2-java-doc

openrtm2-java-doc includes Japanese and English class references.

```
 /usr/share/openrtm-2.0/doc/java/JavaDoc/OpenRTM/*
 ...
 /usr/share/openrtm-2.0/doc/java/JavaDocEn/*
```

### openrtp2

Since openrtp installs a large number of files, they are not listed here. If necessary, enter

```
 $ dpkg -L openrtp2
```

and check the contents yourself.

