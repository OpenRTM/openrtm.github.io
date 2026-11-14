---
layout: page
title: "master manager and slave manager"
---

<!-- Title: マスターマネージャ、スレーブマネージャ -->
#contents

## Overview

### Manager

A manager is a mechanism for managing RTCs.
One manager runs in each process.

### Master Manager and Slave Manager

There are two types of managers: the **Master Manager** and the **Slave Manager**.
The Master Manager is a higher-level manager that manages Slave Managers, while the Slave Manager is responsible for creating and executing RTCs.

<div align="center"><a href="manager1.jpg"><img src="manager1.jpg" width="80%;"></a></div>

By calling the Master Manager API from external tools such as RTSystemEditor, operations such as creating and deleting RTCs can be performed.
RTCs are not started directly on the Master Manager. Instead, the Master Manager calls the API of a Slave Manager and instructs it to start the RTC.

<div align="center"><a href="manager2.jpg"><img src="manager2.jpg" width="60%;"></a></div>

The following is an example of a Python program that instructs the Master Manager to create an RTC.

```python
import sys
from omniORB import CORBA
import RTM

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
obj = orb.string_to_object("corbaloc:iiop:localhost:2810/manager")
mgr = obj._narrow(RTM.Manager)

rtc = mgr.create_component("ConsoleIn&manager_name=samplemaneger")
```

To start the Master Manager, execute **rtcd** with the **-d** option.

```sh
rtcd -d -f rtc.conf
```

The module search path must be configured in **rtc.conf**.

```conf
manager.modules.load_path: C:/Program Files/OpenRTM-aist/1.2.2/Components/C++/OpenCV/vc14
```

To start a Slave Manager, no special options are required. However, configure the manager name and module search path in **rtc.conf**.
Also, the default configuration automatically shuts down the manager when no RTCs are running, so disable this feature.

```conf
manager.instance_name: samplemaneger
manager.modules.load_path: C:/Program Files/OpenRTM-aist/1.2.2/Components/C++/OpenCV/vc14
manager.shutdown_auto:NO
```

## API

### load_module

### unload_module

### get_loadable_modules

### get_loaded_modules

### get_factory_profiles

### create_component

**create_component** is the API used to create an RTC.
Specify the vendor name, category name, component name, language name, and version number of the RTC to be started as follows.

```python
mgr.create_component("RTC:AIST:Example:ConsoleIn:C++:1.0.0")
```

The argument string has the following format.

```text
RTC:[vendor]:[category]:[implementation_id]:[version]
```

However, all fields except **implementation_id** can be omitted, so you can create an RTC by specifying only the RTC name as follows.

```python
mgr.create_component("ConsoleIn")
```

Although the RTC runs on a Slave Manager, you can specify the Slave Manager on which to start the RTC by using the **manager_name** option.

```python
mgr.create_component("ConsoleIn&manager_name=samplemaneger")
```

To start an RTC on a Slave Manager specified by its address and port number, use the **manager_address** option.

```python
mgr.create_component("Flip&manager_address=localhost:2811")
```

#### Manager Behavior

##### When a Slave Manager name is specified but the specified Slave Manager is not running

If a Slave Manager name is specified with the **manager_name** option and the specified Slave Manager is not running, the Master Manager starts a Slave Manager with the specified name.
For example, if the Slave Manager named **samplemaneger** is not running, a new Slave Manager named **samplemaneger** is started.

```python
mgr.create_component("ConsoleIn&manager_name=samplemaneger")
```

##### When no Slave Manager name is specified

If the **manager_name** option is not specified as shown below, a new Slave Manager named **manager_[process ID]** is started.

```python
mgr.create_component("ConsoleIn")
```

##### When RTCs with the same component name are available

For example, the OpenRTM-aist sample components include three versions of the **ConsoleIn** component implemented in C++, Python, and Java.
To distinguish and start RTCs with the same component name, specify the language name as follows.

```python
mgr.create_component("RTC:AIST:Example:ConsoleIn:Python:1.0.0")
```

If the language name is still insufficient to distinguish the RTC, start the Slave Manager that will execute the RTC in advance, and specify the manager name in **create_component**.

### delete_component

### get_components

### get_component_profiles

### get_components_by_name

### get_profile

### get_configuration

### set_configuration

### is_master

### get_master_managers

### add_master_manager

### remove_master_manager

### get_slave_managers

To call the API of a Slave Manager directly, obtain the Slave Manager from the Master Manager by using **get_slave_managers**, and then invoke its API.
The following example loads a module and starts an RTC on a Slave Manager with the specified name.

```python
import sys
from omniORB import CORBA
import RTM
import OpenRTM_aist

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
obj = orb.string_to_object("corbaloc:iiop:localhost:2810/manager")
mgr = obj._narrow(RTM.Manager)
print(mgr.create_component("Flip&manager_name=samplemaneger"))


def getSlaveManager(master, slavename):
    slavemgrs = master.get_slave_managers()
    for slavemgr in slavemgrs:
        prof = slavemgr.get_configuration()
        prop = OpenRTM_aist.Properties()
        OpenRTM_aist.NVUtil.copyToProperties(prop, prof)
        name = prop.getProperty("manager.instance_name")
        if name == slavename:
            return slavemgr
    return None


samplemaneger = getSlaveManager(mgr, "samplemaneger")
samplemaneger.load_module(
    "C:\\Program Files\\OpenRTM-aist\\1.2.2\\Components\\C++\\Examples\\vc14\\ConsoleIn.dll", "ConsoleInInit")
samplemaneger.create_component("ConsoleIn")
```


### add_slave_manager

### remove_slave_manager

### fork

### shutdown

### restart

### get_service
