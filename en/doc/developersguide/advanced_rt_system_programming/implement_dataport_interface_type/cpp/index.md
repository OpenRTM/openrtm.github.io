---
layout: page
title: "implementation procedure for a custom interface type (c++)"
---

<!-- Title: 独自インターフェース型の実装手順(C++) -->
#contents

This page explains how to create a custom interface in C++.

Since the non-essential parts are omitted in the following source code examples, please obtain the complete source code from the following repository.

- https://github.com/Nobu19800/openrtm_testinterface

## Creating CMakeLists.txt

Create the following CMakeLists.txt for building.
The configuration for detecting the OpenRTM-aist libraries is required.
Also, the names of the generated shared libraries must be **${target}.dll** and **${target}.so**.
Since Linux adds the prefix **lib** (libTestIF.so), the following example removes the **lib** prefix.

```cmake
cmake_minimum_required(VERSION 3.1)

set(target TestIF)
project(${target} CXX)

find_package(OpenRTM REQUIRED)

add_definitions(${OPENRTM_CFLAGS})
link_directories(${OPENRTM_LIBRARY_DIRS})

add_library(${target} SHARED ${target}.cpp TestInPortConsumer.cpp TestInPortConsumer.h TestInPortProvider.cpp TestInPortProvider.h TestOutPortConsumer.cpp TestOutPortConsumer.h
TestOutPortProvider.cpp TestOutPortProvider.h)
target_link_libraries(${target} ${OPENRTM_LIBRARIES})
target_include_directories(${target} SYSTEM PRIVATE ${OPENRTM_INCLUDE_DIRS})
set_target_properties(${target} PROPERTIES PREFIX "")
```

However, when implementing Push communication, TestInPortConsumer and TestInPortProvider are required, while TestOutPortConsumer and TestOutPortProvider are required for Pull communication. Therefore, if you implement only one communication type, you do not need to create the unnecessary files.

### Push Communication

To implement Push communication, implement TestInPortConsumer (InPortConsumer) and TestInPortProvider (InPortProvider).

#### Implementing InPortConsumer

First, prepare the following header file (TestInPortConsumer.h) and source file (TestInPortConsumer.cpp).

```cpp
#ifndef TESTINPORTCONSUMER_H
#define TESTINPORTCONSUMER_H

#include <rtm/InPortConsumer.h>

class TestInPortConsumer
  : public RTC::InPortConsumer
{
public:
  TestInPortConsumer();
  ~TestInPortConsumer() override;
  void init(coil::Properties& prop) override;
  RTC::DataPortStatus put(RTC::ByteData& data) override;
  void publishInterfaceProfile(SDOPackage::NVList& properties) override;
  bool subscribeInterface(const SDOPackage::NVList& properties) override;
  void unsubscribeInterface(const SDOPackage::NVList& properties) override;
};

#endif
```

```cpp
#include "TestInPortConsumer.h"

TestInPortConsumer::TestInPortConsumer()
{
}

TestInPortConsumer::~TestInPortConsumer()
{
}

void TestInPortConsumer::init(coil::Properties& prop)
{
}

RTC::DataPortStatus TestInPortConsumer::put(RTC::ByteData& data)
{
    return RTC::DataPortStatus::PORT_OK;
}

void TestInPortConsumer::publishInterfaceProfile(SDOPackage::NVList& properties)
{
}

bool TestInPortConsumer::subscribeInterface(const SDOPackage::NVList& properties)
{
    return true;
}

void TestInPortConsumer::unsubscribeInterface(const SDOPackage::NVList& properties)
{
}
```

In this example, a custom interface that transfers data by reading from and writing to files is implemented here.

First, the **init** function is called when the connector is initialized.
The variable **prop** contains the connector connection information configured in RTSystemEditor and other tools.
In the following example, the **testif.filename** parameter is obtained from **prop** and used as the file name.
Since the **init** function may be called multiple times, this should be taken into consideration.

```cpp
void TestInPortConsumer::init(coil::Properties& prop)
{
    if (prop.propertyNames().size() == 0)
    {
        return;
    }

    m_filename = prop.getProperty("testif.filename", "test.dat");
}
```

The **put** function is called when data is written.
The variable **data** contains the serialized byte stream.

```cpp
RTC::DataPortStatus TestInPortConsumer::put(RTC::ByteData& data)
{

    std::ofstream fout;
    fout.open(m_filename, std::ios::out | std::ios::binary | std::ios::trunc);

    if (fout.fail())
    {
        return RTC::DataPortStatus::PORT_ERROR;
    }
    else
    {
        m_dataid += 1;
        fout.write((const char*)&m_dataid, sizeof(unsigned long));

        const unsigned long size = data.getDataLength();
        fout.write((const char*)&size, sizeof(unsigned long));

        if (size > 0)
        {
            fout.write((const char*)data.getBuffer(), size);
        }
    }

    return RTC::DataPortStatus::PORT_OK;
}
```

In this example, the data ID, data size, and byte stream are written to the file.
The **getDataLength** function of the **data** variable obtains the data size, and the **getBuffer** function obtains the byte stream. The obtained data is then transmitted to InPortProvider by some method.
The **readData** function can also be used to read data.

The other functions generally do not require implementation. However, if additional information is set on the InPortProvider side, that information must be obtained in the **subscribeInterface** function.
Since **unsubscribeInterface** is called when the connector is disconnected, describe any necessary cleanup processing related to **subscribeInterface** there.

#### Implementing InPortProvider

First, prepare the following header file (TestInPortProvider.h) and source file (TestInPortProvider.cpp).

```cpp
#ifndef TESTINPORTPROVIDER_H
#define TESTINPORTPROVIDER_H

#include <rtm/InPortProvider.h>
#include <thread>

class TestInPortProvider
  : public RTC::InPortProvider
{
public:
  TestInPortProvider();
  ~TestInPortProvider() override;
  void init(coil::Properties& prop) override;
  void setBuffer(RTC::BufferBase<RTC::ByteData>* buffer) override;
  void setListener(RTC::ConnectorInfo& info,
                   RTC::ConnectorListenersBase* listeners) override;
  void setConnector(RTC::InPortConnector* connector) override;
private:
  RTC::InPortConnector* m_connector;
};

#endif
```

```cpp
#include "TestInPortProvider.h"
#include <fstream>

TestInPortProvider::TestInPortProvider() : m_connector(nullptr)
{
    setInterfaceType("testif");
}

TestInPortProvider::~TestInPortProvider()
{
}

void TestInPortProvider::init(coil::Properties& prop)
{
}

void TestInPortProvider::setBuffer(RTC::BufferBase<RTC::ByteData>* buffer)
{
}

void TestInPortProvider::setListener(RTC::ConnectorInfo& info,
    RTC::ConnectorListenersBase* listeners)
{
}

void TestInPortProvider::setConnector(RTC::InPortConnector* connector)
{
    m_connector = connector;
}
```

Processing is added here.
In this example, the **init** function creates a thread that polls whether the specified file has been modified.



```cpp
void TestInPortProvider::init(coil::Properties& prop)
{
    if (prop.propertyNames().size() == 0)
    {
        return;
    }

    const std::string filename = prop.getProperty("testif.filename", "test.dat");

    if (!m_running)
    {
        m_thread = std::thread([this, filename] {
            this->m_running = true;
            unsigned long lastid = 0;
            while (this->m_running)
            {
                if (this->m_connector != nullptr)
                {
                    std::ifstream fin(filename, std::ios::in | std::ios::binary);
                    if (!fin.fail())
                    {
                        unsigned long id = 0;
                        fin.read((char*)&id, sizeof(unsigned long));

                        if (id != lastid)
                        {
                            lastid = id;
                            unsigned long size = 0;
                            fin.read((char*)&size, sizeof(unsigned long));
                            if (size > 0)
                            {
                                RTC::ByteData data;
                                data.setDataLength(size);
                                fin.read((char*)data.getBuffer(), size);
                                this->m_connector->write(data);
                            }
                        }
                    }
                }
            }
        });
    }
}
```

After reading the data from the file, the **write** function of **m_connector** is called to pass the data to the InPortConnector.
By writing the data from InPortConsumer to a file and reading it from the file in InPortProvider, data transfer has been implemented.

### Pull Communication

To implement Pull communication, implement TestOutPortConsumer (OutPortConsumer) and TestOutPortProvider (OutPortProvider).
If you implement only Push communication, you can skip this section.

#### Implementing OutPortConsumer

First, prepare the following header file (TestOutPortConsumer.h) and source file (TestOutPortConsumer.cpp).

```cpp
#ifndef TESTOUTPORTCONSUMER_H
#define TESTOUTPORTCONSUMER_H

#include <rtm/SystemLogger.h>
#include <rtm/OutPortConsumer.h>

class TestOutPortConsumer
  : public RTC::OutPortConsumer
{
public:
  TestOutPortConsumer();
  ~TestOutPortConsumer() override;
  void init(coil::Properties& prop) override;
  void setBuffer(RTC::CdrBufferBase* buffer) override;
  void setListener(RTC::ConnectorInfo& info,
      RTC::ConnectorListenersBase* listeners) override;
  RTC::DataPortStatus get(RTC::ByteData& data) override;
  bool subscribeInterface(const SDOPackage::NVList& properties) override;
  void unsubscribeInterface(const SDOPackage::NVList& properties) override;
};

#endif
```

```cpp
#include "TestOutPortConsumer.h"

TestOutPortConsumer::TestOutPortConsumer()
{
}

TestOutPortConsumer::~TestOutPortConsumer()
{
}

void TestOutPortConsumer::init(coil::Properties& prop)
{
}

void TestOutPortConsumer::setBuffer(RTC::CdrBufferBase* buffer)
{
}

void TestOutPortConsumer::setListener(RTC::ConnectorInfo& info,
    RTC::ConnectorListenersBase* listeners)
{
}

RTC::DataPortStatus TestOutPortConsumer::get(RTC::ByteData& data)
{
    return RTC::DataPortStatus::PORT_OK;
}

bool TestOutPortConsumer::subscribeInterface(const SDOPackage::NVList& properties)
{
    return true;
}

void TestOutPortConsumer::unsubscribeInterface(const SDOPackage::NVList& properties)
{
}
```

In this example, the file names used for reading and writing are specified in the **init** function.

```cpp
void TestOutPortConsumer::init(coil::Properties& prop)
{
    if (prop.propertyNames().size() == 0)
    {
        return;
    }

    m_filename_in = prop.getProperty("testif.filename_in", "test_in.dat");
    m_filename_out = prop.getProperty("testif.filename_out", "test_out.dat");
}
```

Processing is added here.

In Pull communication, the **get** function is called when data is read. In the following example, the request ID is first written to file A.

Next, the data size and byte stream are read from file B and stored in the variable **data**.

Use the **setDataLength** function to set the data size.

To store the data, either write to the pointer returned by the **getBuffer** function or use the **writeData** function.

```cpp
RTC::DataPortStatus TestOutPortConsumer::get(RTC::ByteData& data)
{
    std::ofstream fout;
    fout.open(m_filename_out, std::ios::out | std::ios::binary | std::ios::trunc);

    if (fout.fail())
    {
        return RTC::DataPortStatus::PORT_ERROR;
    }
    else
    {
        m_dataid += 1;
        fout.write((const char*)&m_dataid, sizeof(unsigned long));
        fout.close();

        for (int i = 0; i < 100; i++)
        {
            std::ifstream fin(m_filename_in, std::ios::in | std::ios::binary);
            if (!fin.fail())
            {
                unsigned long id = 0;
                fin.read((char*)&id, sizeof(unsigned long));

                if (id == m_dataid)
                {
                    unsigned long size = 0;
                    fin.read((char*)&size, sizeof(unsigned long));
                    if (size > 0)
                    {
                        data.setDataLength(size);
                        fin.read((char*)data.getBuffer(), size);
                        return RTC::DataPortStatus::PORT_OK;
                    }

                }
            }
        }
    }

    return RTC::DataPortStatus::PORT_ERROR;
}
```

#### Implementing OutPortProvider

First, prepare the following header file (TestOutPortProvider.h) and source file (TestOutPortProvider.cpp).

```cpp
#ifndef TESTOUTPORTPROVIDER_H
#define TESTOUTPORTPROVIDER_H

#include <rtm/OutPortProvider.h>

class TestOutPortProvider
  : public RTC::OutPortProvider
{
public:
  TestOutPortProvider();
  ~TestOutPortProvider() override;
  void init(coil::Properties& prop) override;
  void setBuffer(RTC::CdrBufferBase* buffer) override;
  void setListener(RTC::ConnectorInfo& info,
      RTC::ConnectorListenersBase* listeners) override;
  void setConnector(RTC::OutPortConnector* connector) override;
private:
  RTC::OutPortConnector* m_connector;
};

#endif
```

```cpp
#include "TestOutPortProvider.h"

TestOutPortProvider::TestOutPortProvider() : m_connector(nullptr)
{
    setInterfaceType("testif");
}

TestOutPortProvider::~TestOutPortProvider()
{
}

void TestOutPortProvider::init(coil::Properties& prop)
{
}

void TestOutPortProvider::setBuffer(RTC::CdrBufferBase* buffer)
{
}

void TestOutPortProvider::setListener(RTC::ConnectorInfo& info,
    RTC::ConnectorListenersBase* listeners)
{
}

void TestOutPortProvider::setConnector(RTC::OutPortConnector* connector)
{
    m_connector = connector;
}
```

Processing is added here.

In the following example, the **init** function starts a thread that polls whether the file has been modified and writes data to another file when a change is detected.
```


```cpp
void TestOutPortProvider::init(coil::Properties& prop)
{
    if (prop.propertyNames().size() == 0)
    {
        return;
    }

    const std::string filename_in = prop.getProperty("testif.filename_in", "test_in.dat");
    const std::string filename_out = prop.getProperty("testif.filename_out", "test_out.dat");

    if (!m_running)
    {
        m_thread = std::thread([this, filename_in, filename_out] {
            this->m_running = true;
            unsigned long lastid = 0;
            while (this->m_running)
            {
                if (this->m_connector != nullptr)
                {
                    std::ifstream fin(filename_out, std::ios::in | std::ios::binary);
                    if (!fin.fail())
                    {
                        unsigned long id = 0;
                        fin.read((char*)&id, sizeof(unsigned long));
                        fin.close();

                        if (lastid != id)
                        {
                            std::ofstream fout;
                            fout.open(filename_in, std::ios::out | std::ios::binary | std::ios::trunc);
                            if (!fout.fail())
                            {
                                fout.write((const char*)&id, sizeof(unsigned long));

                                RTC::ByteData data;
                                m_connector->read(data);

                                const unsigned long size = data.getDataLength();
                                fout.write((const char*)&size, sizeof(unsigned long));

                                if (size > 0)
                                {
                                    fout.write((const char*)data.getBuffer(), size);
                                }
                            }

                            lastid = id;
                        }
                    }
                }
            }
        });
    }
}
```

First, the **read** function of **m_connector** is called to obtain the data to be transferred from OutPortConnector.
The data size is obtained with the **getDataLength** function, and the byte stream data is obtained with the **getBuffer** function and written to the file.

As a result, after OutPortConsumer writes the data ID to file A, OutPortProvider reads the ID from file A and determines whether it matches the previously read data ID.
If it determines that the data is new, it writes the data to file B, and OutPortConsumer determines whether file B contains new data and passes the data to OutPortConnector.

### Registering the Custom Interface

To make the custom interface implemented so far available, register it with the factory.
Create **TestIF.cpp** with the following contents.

```cpp
#include "TestInPortConsumer.h"
#include "TestInPortProvider.h"
#include "TestOutPortConsumer.h"
#include "TestOutPortProvider.h"
#include <rtm/Manager.h>

extern "C"
{
    DLL_EXPORT void TestIFInit(RTC::Manager* manager)
    {
        {
            RTC::InPortProviderFactory& factory(RTC::InPortProviderFactory::instance());
            factory.addFactory("testif",
                       ::coil::Creator< ::RTC::InPortProvider,
                                         TestInPortProvider>,
                       ::coil::Destructor< ::RTC::InPortProvider,
                                         TestInPortProvider>);
        }

        {
            RTC::InPortConsumerFactory& factory(RTC::InPortConsumerFactory::instance());
            factory.addFactory("testif",
                       ::coil::Creator< ::RTC::InPortConsumer,
                                         TestInPortConsumer>,
                       ::coil::Destructor< ::RTC::InPortConsumer,
                                         TestInPortConsumer>);
        }

        {
            RTC::OutPortProviderFactory& factory(RTC::OutPortProviderFactory::instance());
            factory.addFactory("testif",
                       ::coil::Creator< ::RTC::OutPortProvider,
                                         TestOutPortProvider>,
                       ::coil::Destructor< ::RTC::OutPortProvider,
                                         TestOutPortProvider>);
        }

        {
            RTC::OutPortConsumerFactory& factory(RTC::OutPortConsumerFactory::instance());
            factory.addFactory("testif",
                       ::coil::Creator< ::RTC::OutPortConsumer,
                                        TestOutPortConsumer>,
                       ::coil::Destructor< ::RTC::OutPortConsumer,
                                         TestOutPortConsumer>);
        }
    }
}
```

The implemented custom interface is registered using the **addFactory** function of **InPortProviderFactory**, **InPortConsumerFactory**, **OutPortProviderFactory**, and **OutPortConsumerFactory**.
In this example, it can be used by specifying the name **testif** when connecting ports.
If you implement only Push communication or only Pull communication, register only the required modules.
The TestIFInit function is called when the dynamic library is loaded. For example, if the file is 〇〇.dll, name the initialization function **〇〇Init**, using the dynamic library name + Init.

### Operation Check

After building and generating **TestIF.dll** or **TestIF.so**, create the following rtc.conf.
Specify the path to the folder containing TestIF.dll or TestIF.so in ${TestIF_DIR}.

```conf
manager.modules.load_path: ${TestIF_DIR}
manager.preload.modules: TestIF.dll
```

Start the ConsoleIn and ConsoleOut sample components by specifying the created rtc.conf. This causes OpenRTM-aist to load TestIF.dll.

```sh
ConsoleIn -f rtc.conf
```

```sh
ConsoleOut -f rtc.conf
```

When you try to connect data ports in RTSystemEditor, **testif** can be selected as the Interface Type, as shown below.

<br>

<div align="center"><a href="if4.png"><img src="if4.png" width="70%;"></a></div>

<br>

When you select **testif** as the Interface Type and connect the ports, you can confirm that data transfer using the implemented file reading and writing works.

When checking the operation of Pull communication, the **isNew** function of InPort cannot be used in Pull communication, so it is not possible to check whether new data exists.
Therefore, you need to comment out the part that executes the **isNew** function in the ConsoleOut component and rebuild it.

```cpp
//if (m_inIn.isNew())
```

### Setting Options at Connection

In this example, the file names used for reading and writing can be specified with the options **testif.filename**, **testif.filename_in**, and **testif.filename_out**. You can also add settings so that these option values are obtained from the data port profile. However, this may not be available in the release version of OpenRTM-aist 2.0, so build OpenRTM-aist from source code.

```cpp
static const char* const testifpush_option[] =
{
    "filename.__value__", "test.dat",
    "filename.__widget__", "text",
    "filename.__constraint__", "none",
    ""
};

extern "C"
{
    DLL_EXPORT void TestIFInit(RTC::Manager* manager)
    {
        {
            coil::Properties prop(testifpush_option);
            RTC::InPortProviderFactory& factory(RTC::InPortProviderFactory::instance());
            factory.addFactory("testif",
                      ::coil::Creator< ::RTC::InPortProvider,
                                        TestInPortProvider>,
                      ::coil::Destructor< ::RTC::InPortProvider,
                                        TestInPortProvider>,
                      prop);
        }
```

```cpp
static const char* const testifpush_option[] =
{
    "filename.__value__", "test.dat",
    "filename.__widget__", "text",
    "filename.__constraint__", "none",
    ""
};

extern "C"
{
    DLL_EXPORT void TestIFInit(RTC::Manager* manager)
    {
        {
            coil::Properties prop(testifpush_option);
            RTC::InPortProviderFactory& factory(RTC::InPortProviderFactory::instance());
            factory.addFactory("testif",
                      ::coil::Creator< ::RTC::InPortProvider,
                                        TestInPortProvider>,
                      ::coil::Destructor< ::RTC::InPortProvider,
                                        TestInPortProvider>,
                      prop);
        }
    }
}
```
