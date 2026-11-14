## Part 1/2

---
layout: page
title: "How to Implement a Custom Logger"
---

<!-- Title: 独自ロガーの実装方法 -->
#contents

OpenRTM-aist can extend logging functionality other than the default OpenRTM-aist logger, such as the [Fluent Bit Plugin]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/fluent_logger_use).

This page explains how to create and use a custom logger.

The source code created in this example can be obtained from the following repository.

- [https://github.com/Nobu19800/testlopenrtmlogger](https://github.com/Nobu19800/testlopenrtmlogger)

## How to Create a Custom Logger

### C++

#### Creating a Custom Logger

For C++, prepare the following CMakeLists.txt for building. In this example, the logger is created with the name **TestLogger**.

```cmake
cmake_minimum_required(VERSION 3.1)

set(target TestLogger)
project(${target} CXX)

find_package(OpenRTM REQUIRED)

add_definitions(${OPENRTM_CFLAGS})
link_directories(${OPENRTM_LIBRARY_DIRS})

add_library(${target} SHARED ${target}.cpp ${target}.h)
target_link_libraries(${target} ${OPENRTM_LIBRARIES})
target_include_directories(${target} SYSTEM PRIVATE ${OPENRTM_INCLUDE_DIRS})
set_target_properties(${target} PROPERTIES PREFIX "")
```

Prepare the header file (TestLogger.h) and source file (TestLogger.cpp).
Implement the **TestLoggerStream** class, which inherits from **coil::LogStreamBuffer**, and the **TestLogger** class, which inherits from **RTC::LogstreamBase**.
**TestLoggerStream** implements the logging process, while **TestLogger** creates a **TestLoggerStream** instance and makes it available externally.

```cpp
#ifndef TESTLOGGER_H
#define TESTLOGGER_H

#include <rtm/LogstreamBase.h>

class TestLoggerStream
  : public coil::LogStreamBuffer
{
public:
  TestLoggerStream();
  ~TestLoggerStream() override;
  bool init(const coil::Properties& prop);
  void write(int level, const std::string& name, const std::string& date, const std::string& mes) override;
private:
  std::string header;
};

class TestLogger
  : public RTC::LogstreamBase
{
public:
  TestLogger();
  ~TestLogger() override;
  bool init(const coil::Properties& prop) override;
  coil::LogStreamBuffer* getStreamBuffer() override;
private:
  TestLoggerStream m_logstream;
};

extern "C"
{
  void DLL_EXPORT TestLoggerInit();
}

#endif
```

```cpp
#include "TestLogger.h"
#include <iostream>

TestLoggerStream::TestLoggerStream()
{
}

TestLoggerStream::~TestLoggerStream()
{
}

bool TestLoggerStream::init(const coil::Properties& prop)
{
  header = prop["header"];
  return true;
}

void TestLoggerStream::write(int level, const std::string& name, const std::string& date, const std::string& mes)
{
  std::cout << header << ":" << mes << std::endl;
}

TestLogger::TestLogger()
{
}

TestLogger::~TestLogger()
{
}

bool TestLogger::init(const coil::Properties& prop)
{
  m_logstream.init(prop);
  return true;
}

coil::LogStreamBuffer* TestLogger::getStreamBuffer()
{
  return &m_logstream;
}

extern "C"
{
  void TestLoggerInit()
  {
    ::RTC::LogstreamFactory::
      instance().addFactory("testlogger",
                           ::coil::Creator< ::RTC::LogstreamBase,
                                            TestLogger>,
                           ::coil::Destructor< ::RTC::LogstreamBase,
                                               TestLogger>);
  }
}
```

The **init** function of the **TestLogger** class performs initialization, and the **getStreamBuffer** function returns the LogStreamBuffer object.
Unless there is a specific reason, the **TestLogger** class does not need to be modified.

The **write** function of the **TestLoggerStream** class outputs log messages.
In this example, the string specified in the **header** property is added to the beginning of each log message and output to the standard output.

The **TestLoggerInit** function is called when the dynamic library is loaded. For example, if the library is named **〇〇.dll**, the initialization function should be named **〇〇Init**, using the dynamic library name followed by **Init**.
A logger can be added by calling the **addFactory** function of **LogstreamFactory** inside the **TestLoggerInit** function.

#### Operation Check

After building and generating **TestLogger.dll** or **TestLogger.so**, verify the operation.

Create the following **rtc.conf**.

```conf
logger.enable: YES
logger.log_level: VERBOSE

logger.plugins: TestLogger.dll

logger.logstream.testlogger.enable: ON
logger.logstream.testlogger.header: example
```

First, configure the **logger.plugins** option so that **TestLogger** is loaded.
Simply loading the logger does not enable it, so you must also set the **logger.logstream.testlogger.enable** option.

*As implemented in OpenRTM-aist, a logger is enabled whenever any option under **logger.logstream.${module_name}** is specified. Therefore, it is not necessarily required to use the **enable** option.*

The **logger.logstream.testlogger.header** option specifies the string to be added to the beginning of each log message.

When you start an RTC with this **rtc.conf**, you can confirm that log messages are output to the standard output.

### Python

Prepare the Python file (TestLogger.py).
Implement the **TestLogger** class, which inherits from **OpenRTM_aist.LogstreamBase**.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import OpenRTM_aist


class TestLogger(OpenRTM_aist.LogstreamBase):

    def __init__(self):
        OpenRTM_aist.LogstreamBase.__init__(self)
        self._header = ""

    def __del__(self):
        pass

    def init(self, prop):
        self._header = prop.getProperty("header")
        return True

    def log(self, msg, level, name):
        print(self._header+":"+msg)
        return True

    def setLogLevel(self, level):
        pass

    def shutdown(self):
        return True


def TestLoggerInit(mgr):
    OpenRTM_aist.LogstreamFactory.instance().addFactory("testlogger",
                                                        TestLogger)
```
## Part 2/2

The **init** function of the **TestLogger** class performs initialization, the **log** function outputs log messages, the **setLogLevel** function sets the log level, and the **shutdown** function performs termination processing.
In this example, the string specified in the **header** property is added to the beginning of each log message and output to the standard output.

The **TestLoggerInit** function is called when the Python module is loaded. For example, if the file is named **〇〇.py**, the initialization function should be named **〇〇Init**, using the Python file name followed by **Init**.
A logger can be added by calling the **addFactory** function of **LogstreamFactory** inside the **TestLoggerInit** function.

#### Operation Check

Create the following **rtc.conf**.

```conf
logger.enable: YES
logger.log_level: VERBOSE

logger.plugins: TestLogger.py

logger.logstream.testlogger.enable: ON
logger.logstream.testlogger.header: example
```

First, configure the **logger.plugins** option so that **TestLogger** is loaded.
Simply loading the logger does not enable it, so you must also set the **logger.logstream.testlogger.enable** option.

The **logger.logstream.testlogger.header** option specifies the string to be added to the beginning of each log message.

When you start an RTC with this **rtc.conf**, you can confirm that log messages are output to the standard output.

