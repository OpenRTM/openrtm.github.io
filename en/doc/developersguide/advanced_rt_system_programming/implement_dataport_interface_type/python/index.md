---
layout: page
title: "implementation procedure for a custom interface type (python)"
---

<!-- Title: 独自インターフェース型の実装手順(Python) -->
#contents

This page explains how to create a custom interface in Python.

Since the non-essential parts are omitted in the following source code examples, please obtain the complete source code from the following repository.

- [https://github.com/Nobu19800/openrtm_testinterface](https://github.com/Nobu19800/openrtm_testinterface)

### Push Communication

To implement Push communication, implement TestInPortConsumer (InPortConsumer) and TestInPortProvider (InPortProvider).

#### Implementing InPortConsumer

First, prepare the following Python file (TestInPortConsumer.py).

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import OpenRTM_aist


class TestInPortConsumer(
        OpenRTM_aist.InPortConsumer):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def init(self, prop):
        if not prop.propertyNames():
            return

    def put(self, data):
            return self.PORT_OK

    def publishInterfaceProfile(self, properties):
        pass

    def subscribeInterface(self, properties):
        return True

    def unsubscribeInterface(self, properties):
        pass


def TestInPortConsumerInit():
    factory = OpenRTM_aist.InPortConsumerFactory.instance()
    factory.addFactory("testif",
                       TestInPortConsumer)
```

In this example, a custom interface that transfers data by reading from and writing to files is implemented here.

First, the **init** function is called when the connector is initialized.
The variable **prop** contains the connector connection information configured in RTSystemEditor and other tools.
In the following example, the **testif.filename** parameter is obtained from **prop** and used as the file name.
Since the **init** function may be called multiple times, this should be taken into consideration.

```python
def init(self, prop):
    if not prop.propertyNames():
        return
    self._filename = prop.getProperty("testif.filename", "test.dat")
```

The **put** function is called when data is written.
The variable **data** contains serialized data of type **bytes**.

```python
def put(self, data):
    with open(self._filename, 'wb') as fout:
        self._dataid += 1
        try:
            fout.write(struct.pack('L', self._dataid))
            fout.write(struct.pack('L', len(data)))
            fout.write(data)
        except BaseException:
            return self.PORT_ERROR
        return self.PORT_OK
```

In this example, the data ID, data size, and byte stream are written to the file.
Obtain the data size using the **getDataLength** function of the **data** variable, obtain the byte stream using the **getBuffer** function, and transfer the acquired data to InPortProvider by some method.

The other functions generally do not require implementation. However, if additional information is set on the InPortProvider side, that information must be obtained in the **subscribeInterface** function.
Since **unsubscribeInterface** is called when the connector is disconnected, describe any necessary cleanup processing related to **subscribeInterface** there.

#### Implementing InPortProvider

First, prepare the following Python file (TestInPortProvider.py).

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import OpenRTM_aist


class TestInPortProvider(OpenRTM_aist.InPortProvider):

    def __init__(self):
        OpenRTM_aist.InPortProvider.__init__(self)

        self.setInterfaceType("testif")

    def __del__(self):
        pass

    def exit(self):
        pass

    def init(self, prop):
        if not prop.propertyNames():
            return

    def setBuffer(self, buffer):
        pass

    def setListener(self, info, listeners):
        pass

    def setConnector(self, connector):
        self._connector = connector


def TestInPortProviderInit():
    factory = OpenRTM_aist.InPortProviderFactory.instance()
    factory.addFactory("testif",
                       TestInPortProvider)
```

Processing is added here.
In this example, the **init** function creates a thread that polls whether the specified file has been modified.

```python
def init(self, prop):
    if not prop.propertyNames():
        return
    filename = prop.getProperty("testif.filename", "test.dat")

    def polling():
        self._running = True
        lastid = 0
        while self._running:
            if self._connector:
                if os.path.exists(filename):
                    with open(filename, 'rb') as fin:
                        try:
                            id = struct.unpack("L", fin.read(struct.calcsize("L")))[0]
                            if id != lastid:
                                lastid = id
                                size = struct.unpack("L", fin.read(struct.calcsize("L")))[0]
                                if size > 0:
                                    data = fin.read(size)
                                    self._connector.write(data)
                        except BaseException:
                            pass

    self._thread = threading.Thread(target=polling)
    self._thread.start()
```

After reading the data from the file, the **write** function of **m_connector** is called to pass the data to the InPortConnector.
By writing the data from InPortConsumer to a file and reading it from the file in InPortProvider, data transfer has been implemented.

### Pull Communication

To implement Pull communication, implement TestOutPortConsumer (OutPortConsumer) and TestOutPortProvider (OutPortProvider).
If you implement only Push communication, you can skip this section.

#### Implementing OutPortConsumer

First, prepare the following Python file (TestOutPortConsumer.py).

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import OpenRTM_aist


class TestOutPortConsumer(
        OpenRTM_aist.OutPortConsumer):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def init(self, prop):
        if not prop.propertyNames():
            return

    def setBuffer(self, buffer):
        pass

    def setListener(self, info, listeners):
        pass

    def get(self):
        return self.PORT_ERROR, ""

    def subscribeInterface(self, properties):
        return True

    def unsubscribeInterface(self, properties):
        pass


def TestOutPortConsumerInit():
    factory = OpenRTM_aist.OutPortConsumerFactory.instance()
    factory.addFactory("testif",
                       TestOutPortConsumer)
    return
```

In this example, the file names used for reading and writing are specified in the **init** function.

```python
def init(self, prop):
    if not prop.propertyNames():
        return
    self._filename_in = prop.getProperty(
        "testif.filename_in", "test_in.dat")
    self._filename_out = prop.getProperty(
        "testif.filename_out", "test_out.dat")
```

Processing is added here.
In Pull communication, the **get** function is called when data is read. In the following example, the request ID is written to file A.
Next, the data size and byte stream are read from file B and returned.


```python
def get(self):
    with open(self._filename_in, 'wb') as fout:
        self._dataid += 1
        try:
            print(self._dataid)
            fout.write(struct.pack('L', self._dataid))
        except BaseException:
            return self.PORT_ERROR

    for i in range(100):
        if os.path.exists(self._filename_out):
            with open(self._filename_out, 'rb') as fin:
                try:
                    id = struct.unpack("L", fin.read(struct.calcsize("L")))[0]
                    if id == self._dataid:
                        self._dataid = id
                        size = struct.unpack("L", fin.read(struct.calcsize("L")))[0]
                        if size > 0:
                            data = fin.read(size)
                            return self.PORT_OK, data
                except BaseException:
                    pass

    return self.PORT_ERROR, ""
```

#### Implementing OutPortProvider

First, prepare the following Python file (TestOutPortProvider.py).

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import OpenRTM_aist


class TestOutPortProvider(OpenRTM_aist.OutPortProvider):

    def __init__(self):
        OpenRTM_aist.OutPortProvider.__init__(self)
        self.setInterfaceType("testif")

        self._thread = None
        self._running = False
        self._connector = None

    def __del__(self):
        pass

    def exit(self):
        if self._running:
            self._running = False
            self._thread.join()

    def init(self, prop):
        if not prop.propertyNames():
            return

    def setBuffer(self, buffer):
        pass

    def setListener(self, info, listeners):
        pass

    def setConnector(self, connector):
        self._connector = connector


def TestOutPortProviderInit():
    factory = OpenRTM_aist.OutPortProviderFactory.instance()
    factory.addFactory("testif",
                       TestOutPortProvider)
```

Processing is added here.
In the following example, the **init** function starts a thread that polls whether the file has been modified and writes data to another file when a change is detected.

```python
def init(self, prop):
    if not prop.propertyNames():
        return

    filename_in = prop.getProperty("testif.filename_in", "test_in.dat")
    filename_out = prop.getProperty("testif.filename_out", "test_out.dat")

    def polling():
        self._running = True
        lastid = 0
        while self._running:
            if self._connector:
                if os.path.exists(filename_in):
                    with open(filename_in, 'rb') as fin:
                        try:
                            id = struct.unpack("L", fin.read(struct.calcsize("L")))[0]
                            if id == lastid:
                                continue
                        except BaseException:
                            continue
                    with open(filename_out, 'wb') as fout:
                        try:
                            fout.write(struct.pack('L', id))
                            ret, data = self._connector.read()
                            fout.write(struct.pack('L', len(data)))
                            if ret == OpenRTM_aist.BufferStatus.BUFFER_OK:
                                fout.write(data)
                                lastid = id
                        except BaseException:
                            pass
```

First, the **read** function of **m_connector** is called to obtain the data to be transferred from OutPortConnector.
The data size is obtained with the **getDataLength** function, and the byte stream data is obtained with the **getBuffer** function and written to the file.

As a result, after OutPortConsumer writes the data ID to file A, OutPortProvider reads the ID from file A and determines whether it matches the previously read data ID.
If it determines that the data is new, it writes the data to file B, and OutPortConsumer determines whether file B contains new data and passes the data to OutPortConnector.

### Registering the Custom Interface

To make the custom interface implemented so far available, register it with the factory.
Create **TestIF.py** with the following contents.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-


import TestInPortConsumer
import TestInPortProvider
import TestOutPortConsumer
import TestOutPortProvider


def TestIFInit(mgr):
    TestInPortConsumer.TestInPortConsumerInit()
    TestInPortProvider.TestInPortProviderInit()
    TestOutPortConsumer.TestOutPortConsumerInit()
    TestOutPortProvider.TestOutPortProviderInit()
```

In the TestInPortProviderInit, TestInPortConsumerInit, TestOutPortProviderInit, and TestOutPortConsumerInit functions, the implemented custom interface is registered using the **addFactory** function of **InPortProviderFactory**, **InPortConsumerFactory**, **OutPortProviderFactory**, and **OutPortConsumerFactory**.
It can be used by specifying the name **testif** when connecting ports.
The TestIFInit function is called when the Python module is loaded. For example, if the file is 〇〇.py, name the initialization function **〇〇Init**, using the Python file name + Init.
If you implement only Push communication or only Pull communication, register only the required modules.

### Operation Check

Create the following rtc.conf.
Specify the path to the folder containing TestIF.py in ${TestIF_DIR}.


## Part 3/3

```conf
manager.modules.load_path: .
manager.modules.preload: TestIF.py
```

Start the ConsoleIn and ConsoleOut sample components by specifying the created rtc.conf. This causes OpenRTM-aist to load TestIF.py.

```sh
python ConsoleIn.py -f rtc.conf
```

```sh
python ConsoleOut.py -f rtc.conf
```

When you try to connect data ports in RTSystemEditor, **testif** can be selected as the Interface Type, as shown below.

<br>

<div align="center"><a href="if4.png"><img src="if4.png" width="40%;"></a></div>

<br>

When you select **testif** as the Interface Type and connect the ports, you can confirm that data transfer using the implemented file reading and writing works.

When checking the operation of Pull communication, the **isNew** function of InPort cannot be used in Pull communication, so it is not possible to check whether new data exists.
Therefore, you need to comment out the part that executes the **isNew** function in the ConsoleOut component.

```python
# if self._inport.isNew():
```

### Setting Options at Connection

In this example, the file names used for reading and writing can be specified with the options **testif.filename**, **testif.filename_in**, and **testif.filename_out**. You can also add settings so that these option values are obtained from the data port profile. However, this may not be available in the release version of OpenRTM-aist 2.0, so build OpenRTM-aist from source code.

```python
testifpush_option = [
    "filename_in.__value__", "test_in.dat",
    "filename_in.__widget__", "text",
    "filename_in.__constraint__", "none",
    "filename_out.__value__", "test_out.dat",
    "filename_out.__widget__", "text",
    "filename_out.__constraint__", "none",
    ""
]


def TestInPortProviderInit():
    prop = OpenRTM_aist.Properties(defaults_str=testifpush_option)
    factory = OpenRTM_aist.InPortProviderFactory.instance()
    factory.addFactory("testif",
                       TestInPortProvider,
                       prop)
```

