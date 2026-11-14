---
layout: page
title: detailed contents of the openrtm-aist-2.0 deb packages
---

<!-- OpenRTM-aist-2.0 debパッケージの詳しい内容 -->

#contents

## Detailed Contents of the OpenRTM-2.1 deb Packages

The contents of each package are as follows.

### openrtm2
openrtm2 includes runtime libraries and commands.

- Commands
```
 /usr/bin/openrtmNames
 /usr/bin/rtcd2
 /usr/bin/rtcprof2
 /usr/bin/rtm2-config
```

- Sample configuration files, etc.
```
 /usr/etc/http/rtc.http.conf
 /usr/etc/http/rtc.https.conf
 /usr/etc/http/rtc.ws.conf
 /usr/etc/http/rtc.wss.conf
 /usr/etc/logger/rtc.fluentbit_stream.conf
 /usr/etc/rtc.names.http.conf
 /usr/etc/ssl/rtc.ssl.conf
 /usr/etc/transport/rtc.ros2.ssl.conf
```


- Libraries, etc.
```
 /usr/lib/x86_64-linux-gnu/libRTC2.a
 /usr/lib/x86_64-linux-gnu/libRTC2.so.2.1.0
 中略
 /usr/lib/x86_64-linux-gnu/librtmCamera2.so
 /usr/lib/x86_64-linux-gnu/librtmManipulator2.so
 中略
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/ec/LogicalTimeTriggeredEC.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/local_service/FileNameservice.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/logger/FluentBit.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/sdo/ComponentObserverConsumer.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/sdo/ExtendedFsmServiceProvider.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/sdo/LoggerConsumer.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/ssl/SSLTransport.so
```

### openrtm2-naming
Starts the name server.

```
 /usr/bin/rtm2-naming
```

### openrtm2-dev 
openrtm2-dev includes the commands and headers required for development.

- Commands
```
 /usr/bin/rtm2-skelwrapper
```

- Headers, etc.
```
 /usr/include/coil-2.1/coil/Affinity.h
 /usr/include/coil-2.1/coil/Async.h
 中略
 /usr/include/openrtm-2.1/rtm/BufferBase.h
 /usr/include/openrtm-2.1/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-2.1/rtm/config_rtc.h
 /usr/include/openrtm-2.1/rtm/ext/FastRTPSMessageInfo.h
 /usr/include/openrtm-2.1/rtm/ext/ROSMessageInfo.h
 /usr/include/openrtm-2.1/rtm/idl/BasicDataType.hh 
 /usr/include/openrtm-2.1/rtm/idl/BasicDataTypeSkel.h
 中略
 /usr/include/openrtm-2.1/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-2.1/rtm/version.h
```

- Libraries and other files
```
 /usr/lib/x86_64-linux-gnu/cmake/openrtm-2.1/OpenRTMConfig.cmake
 /usr/lib/x86_64-linux-gnu/cmake/openrtm-2.1/OpenRTMConfigVersion.cmake
 /usr/share/openrtm-2.1/py_helper/skel_wrapper.py
 /usr/share/openrtm-2.1/py_helper/yat.py
```

### openrtm2-example
openrtm2-example includes samples of both standalone RTCs and loadable RTCs.

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

### openrtm2-ros2-tp

The ROS2 communication feature libraries are installed.

```
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/transport/FastRTPSTransport.so
 /usr/lib/x86_64-linux-gnu/openrtm-2.1/transport/ROS2Transport.so
```

### openrtm2-ssm-tp

SSM and the SSM communication feature library are installed.

```
 /usr/bin/ssm-coordinator
 /usr/bin/ssm-date
 中略
 /usr/share/openrtm-2.1/transport/SSMTransport.so
```

### openrtm2-doc
openrtm2-doc includes Japanese and English class references and IDL interface definition references.

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

### openrtm2-idl

- IDL files, etc.
```
 /etc/profile.d/openrtm2-idl.sh
 /usr/include/openrtm-2.1/rtm/idl/BasicDataType.idl
 /usr/include/openrtm-2.1/rtm/idl/CameraCommonInterface.idl
 中略
 /usr/include/openrtm-2.1/rtm/idl/SharedMemory.idl
 /usr/share/openrtm-2.1/idl/BasicDataType.idl
 /usr/share/openrtm-2.1/idl/CameraCommonInterface.idl
 中略
 /usr/share/openrtm-2.1/idl/SharedMemory.idl
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
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/__init__.py
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtc-template/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcd/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcprof/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtm-naming/*
```

### openrtm2-python3-example

```
 /usr/share/openrtm-2.1/components/python3/__init__.py
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
 /etc/profile.d/openrtm-java.sh
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

Java sample RTCs, class files, source files, and startup scripts
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

### openrtm2-java-doc

openrtm2-java-doc includes Japanese and English class references.

```
 /usr/share/openrtm-2.1/doc/java/JavaDoc/OpenRTM/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDoc/RTC/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDoc/RTM/class-use/*
 中略
 /usr/share/openrtm-2.1/doc/java/JavaDoc/jp/go/aist/rtm/Constants.html
 /usr/share/openrtm-2.1/doc/java/JavaDoc/jp/go/aist/rtm/RTC/buffer/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDoc/jp/go/aist/rtm/RTC/executionContext/class-use/*
 中略
 /usr/share/openrtm-2.1/doc/java/JavaDocEn/OpenRTM/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDocEn/RTC/class-use/*
 /usr/share/openrtm-2.1/doc/java/JavaDocEn/RTM/class-use/*
```



### openrtp2
Since openrtp installs a large number of files, they are not listed here. To check them as needed, enter the following command:

```
 $ dpkg -L openrtp2
```
