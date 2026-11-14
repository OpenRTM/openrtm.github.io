---
layout: page
title: "rtc operation function (corba_rtcutil) user manual"
---

#contents

This page explains how to use the **CORBA_RTCUtil** RTC operation function group of OpenRTM-aist.

The source code used here can be obtained from the following.

- https://github.com/Nobu19800/testCORBA_RTCUtil

## Preparation
### C++
For C++, you need an environment for building programs linked with OpenRTM-aist.

Create the following CMakeLists.txt.

```
 cmake_minimum_required(VERSION 3.1)
 
 set(target CORBA_RTCUtil_test)
 project(${target} CXX)
 
 find_package(OpenRTM REQUIRED)
 
 add_definitions(${OPENRTM_CFLAGS})
 link_directories(${OPENRTM_LIBRARY_DIRS})
 
 add_executable(${target} ${target}.cpp)
 target_link_libraries(${target} ${OPENRTM_LIBRARIES})
 target_include_directories(${target} SYSTEM PRIVATE ${OPENRTM_INCLUDE_DIRS})
```

Also, create the source file **CORBA_RTCUtil_test.cpp** and run CMake.
If you are using OpenRTM-aist built from source code, run **environment-setup.omniorb.vc**.bat**.

```
 %OPENRTM_INSTALL_DIR%\2.0.0\ext\environment-setup.omniorb.vc16.bat
 mkdir build
 cd build
 cmake ..
```

Write the following content in CORBA_RTCUtil_test.cpp.

```
 #include <rtm/Manager.h>
 #include <rtm/NamingManager.h>
 #include <rtm/CORBA_RTCUtil.h>
 #include <iostream>
 
 
 int main (int argc, char** argv)
{
  RTC::Manager* manager;
  manager = RTC::Manager::init(argc, argv);
 
  manager->activateManager();
  manager->runManager(true);
 
  RTC::RTObject_var consolein = RTC::RTObject::_nil();
  RTC::RTObject_var consoleout = RTC::RTObject::_nil();
 
  RTC::NamingManager* nm = RTC::Manager::instance().getNaming();
  RTC::RTCList consoleinlist = nm->string_to_component("rtcname://localhost:2809/*/ConsoleIn0");
 
  if (consoleinlist.length() > 0)
  {
    consolein = consoleinlist[0];
  }
  else
  {
    std::cout << "Could not found ConsoleIn0" << std::endl;
    return 1;
  }
 
  RTC::RTCList consoleoutlist = nm->string_to_component("rtcname://localhost:2809/*/ConsoleOut0");
  
  if (consoleoutlist.length() > 0)
  {
    consoleout = consoleoutlist[0];
  }
  else
  {
    std::cout << "Could not found ConsoleOut0" << std::endl;
    return 1;
  }
  
  RTC::RTObject_var configsample = RTC::RTObject::_nil();
  RTC::RTCList configsamplelist = nm->string_to_component("rtcname://localhost:2809/*/ConfigSample0");
 
  if (configsamplelist.length() > 0)
  {
    configsample = configsamplelist[0];
  }
  else
  {
    std::cout << "Could not found ConfigSample0" << std::endl;
    return 1;
  }
  
  RTC::RTObject_var myserviceprovider = RTC::RTObject::_nil();
  RTC::RTCList myserviceproviderlist = nm->string_to_component("rtcname://localhost:2809/*/MyServiceProvider0");
 
  if (myserviceproviderlist.length() > 0)
  {
    myserviceprovider = myserviceproviderlist[0];
  }
  else
  {
    std::cout << "Could not found MyServiceProvider0" << std::endl;
    return 1;
  }
  
  RTC::RTObject_var myserviceconsumer = RTC::RTObject::_nil();
  RTC::RTCList myserviceconsumerlist = nm->string_to_component("rtcname://localhost:2809/*/MyServiceConsumer0");
 
  if (myserviceconsumerlist.length() > 0)
  {
    myserviceconsumer = myserviceconsumerlist[0];
  }
  else
  {
    std::cout << "Could not found MyServiceConsumer0" << std::endl;
    return 1;
  }
 
  //以降の処理はここに記述する
 
  manager->terminate();
  manager->join();
 
  return 0;
}
```


### Python
For Python, prepare the following **CORBA_RTCUtil_test.py**.

```
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # -*- Python -*-
 
 import sys
 
 import OpenRTM_aist
 import OpenRTM_aist.CORBA_RTCUtil
 from omniORB import CORBA
 
 def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.activateManager()
    mgr.runManager(True)
 
 
    nm = OpenRTM_aist.Manager.instance().getNaming()
    consoleinlist = nm.string_to_component(
        "rtcname://localhost:2809/*/ConsoleIn0")
 
    if consoleinlist:
        consolein = consoleinlist[0]
    else:
        print("Could not found ConsoleIn0")
        sys.exit(1)
 
    consoleoutlist = nm.string_to_component(
        "rtcname://localhost:2809/*/ConsoleOut0")
    if consoleoutlist:
        consoleout = consoleoutlist[0]
    else:
        print("Could not found ConsoleOut0")
        sys.exit(1)
    
    configsamplelist = nm.string_to_component(
        "rtcname://localhost:2809/*/ConfigSample0")
    if consoleoutlist:
        configsample = consoleoutlist[0]
    else:
        print("Could not found ConfigSample0")
        sys.exit(1)
 
    myserviceproviderlist = nm.string_to_component(
        "rtcname://localhost:2809/*/MyServiceProvider0")
    if myserviceproviderlist:
        myserviceprovider = myserviceproviderlist[0]
    else:
        print("Could not found MyServiceProvider0")
        sys.exit(1)
 
    myserviceconsumerlist = nm.string_to_component(
        "rtcname://localhost:2809/*/ConsoleOut0")
    if myserviceconsumerlist:
        myserviceconsumer = myserviceconsumerlist[0]
    else:
        print("Could not found ConsoleOut0")
        sys.exit(1)
 
    #以降の処理はここに記述する
 
    mgr.shutdown()
 
 
 if __name__ == "__main__":
    main()
```

### Creating rtc.conf
Create rtc.conf with the following content.

```
 manager.shutdown_auto: NO
```

### Starting Sample Components

Start the sample components ConsoleIn, ConsoleOut, ConfiguSample, MyServiceProvider, and MyServiceConsumer.


## Using CORBA_RTCUtil
### Port Operations
#### Getting a Port Object Reference

To connect data ports, use the **get_port_by_name** function to obtain the port object reference.

<table class="table-alt">
  <tr>
    <th colspan="2">Function Name</th>
    <th>get_port_by_name</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>name</td>
    <td>std::string&</td>
    <td>RTC name.port name</td>
  </tr>
  <tr>
    <td colspan="2">Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::PortService_ptr</td>
    <td colspan="2">Port object reference</td>
  </tr>
</table>

```
  RTC::PortService_var port_in_var = CORBA_RTCUtil::get_port_by_name(consoleout.in(), "ConsoleOut0.in");
 
  if (CORBA::is_nil(port_in_var))
  {
    std::cout << "Could not found ConsoleOut0.in" << std::endl;
    return 1;
  }
 
  RTC::PortService_var port_out_var = CORBA_RTCUtil::get_port_by_name(consolein.in(), "ConsoleIn0.out");
 
  if (CORBA::is_nil(port_out_var))
  {
    std::cout << "Could not found ConsoleIn0.out" << std::endl;
    return 1;
  }
```

```
    port_in_var = OpenRTM_aist.CORBA_RTCUtil.get_port_by_name(
        consoleout, "ConsoleOut0.in")
    if CORBA.is_nil(port_in_var):
        print("Could not found ConsoleOut0.in")
        sys.exit(1)
 
    port_out_var = OpenRTM_aist.CORBA_RTCUtil.get_port_by_name(
        consolein, "ConsoleIn0.out")
    if CORBA.is_nil(port_out_var):
        print("Could not found ConsoleOut0.in")
        sys.exit(1)
```



Also, by using the **get_port_by_url** function, you can obtain an object reference from a string in **rtcname** format or **rtcloc** format.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">get_port_by_url</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>port_name</td>
    <td>std::string&</td>
    <td>Port URI</td>
  </tr>
  <tr>
    <td colspan="3">Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::PortService_ptr</td>
    <td>></td>
    <td>Port object reference</td>
  </tr>
</table>


```
  RTC::PortService_var port_in_var = CORBA_RTCUtil::get_port_by_url("rtcname://localhost:2809/*/ConsoleOut0.in");
 
  if (CORBA::is_nil(port_in_var))
  {
    std::cout << "Could not found ConsoleOut0.in" << std::endl;
    return 1;
  }
 
  RTC::PortService_var port_out_var = CORBA_RTCUtil::get_port_by_url("rtcname://localhost:2809/*/ConsoleIn0.out");
 
  if (CORBA::is_nil(port_out_var))
  {
    std::cout << "Could not found ConsoleIn0.out" << std::endl;
    return 1;
  }
```

```
    port_in_var = OpenRTM_aist.CORBA_RTCUtil.get_port_by_url(
        "rtcname://localhost:2809/*/ConsoleOut0.in")
    if CORBA.is_nil(port_in_var):
        print("Could not found ConsoleOut0.in")
        sys.exit(1)
 
    port_out_var = OpenRTM_aist.CORBA_RTCUtil.get_port_by_url(
        "rtcname://localhost:2809/*/ConsoleIn0.out")
    if CORBA.is_nil(port_out_var):
        print("Could not found ConsoleOut0.in")
        sys.exit(1)
```

#### Connector Creation

Connect the acquired data ports with the **connect** function.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">connect</th>
  </tr>
  <tr>
    <td colspan="3">CENTER:Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>name</td>
    <td>std::string&</td>
    <td>Connector name</td>
  </tr>
  <tr>
    <td>prop</td>
    <td>coil::Properties&</td>
    <td>Connector setting information</td>
  </tr>
  <tr>
    <td>port0</td>
    <td>RTC::PortService_ptr</td>
    <td>Port 1 to connect</td>
  </tr>
  <tr>
    <td>port1</td>
    <td>RTC::PortService_ptr</td>
    <td>Port 2 to connect</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">CENTER:Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  coil::Properties prop;
  prop["dataport.dataflow_type"] = "push";
  prop["dataport.interface_type"] = "corba_cdr";
  prop["dataport.subscription_type"] = "new";
  CORBA_RTCUtil::connect("test_connector", prop, port_in_var.in(), port_out_var.in());
```


```
    prop = OpenRTM_aist.Properties()
    prop.setProperty("dataport.dataflow_type", "push")
    prop.setProperty("dataport.interface_type", "corba_cdr")
    prop.setProperty("dataport.subscription_type", "new")
    OpenRTM_aist.CORBA_RTCUtil.connect(
        "test_connector", prop, port_in_var, port_out_var)
```

#### Connector Deletion

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">disconnect_connector_name</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>port_ref</td>
    <td>RTC::PortService_ptr</td>
    <td>Connected port</td>
  </tr>
  <tr>
    <td>conn_name</td>
    <td>std::string&</td>
    <td>Connector name</td>
  </tr>
  <tr>
    <td colspan="3">Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>


To delete a connector by specifying the connector name, use the **disconnect_connector_name** function.

```
  CORBA_RTCUtil::disconnect_connector_name(port_in_var.in(), "test_connector");
```

```
    OpenRTM_aist.CORBA_RTCUtil.disconnect_by_portref_connector_name(
        port_in_var, "test_connector")
```

When obtaining an object reference from a connector URI and deleting the connector, use the **disconnect_connector_name** function.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">disconnect_connector_name</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>port_name</td>
    <td>std::string&</td>
    <td>Port URI</td>
  </tr>
  <tr>
    <td>conn_name</td>
    <td>std::string&</td>
    <td>Connector name</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::disconnect_connector_name("rtcname://localhost:2809/*/ConsoleOut0.in", "test_connector");
```

```
    OpenRTM_aist.CORBA_RTCUtil.disconnect_by_portname_connector_name(
        "rtcname://localhost:2809/*/ConsoleOut0.in", "test_connector")
```

#### Connecting Multiple Ports at Once
To connect multiple ports at once, use the **connect_multi** function.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">connect_multi</th>
  </tr>
  <tr>
    <td colspan="3">CENTER:Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>name</td>
    <td>std::string&</td>
    <td>Connector name</td>
  </tr>
  <tr>
    <td>prop</td>
    <td>coil::Properties&</td>
    <td>Connector setting information</td>
  </tr>
  <tr>
    <td>port0</td>
    <td>RTC::PortService_ptr</td>
    <td>Port 1 to connect</td>
  </tr>
  <tr>
    <td>target_ports</td>
    <td>RTC::PortServiceList&</td>
    <td>List of ports to connect to port 1</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  RTC::PortServiceList target_ports;
  target_ports.length(1);
  target_ports[0] = RTC::PortService::_duplicate(port_out_var.in());
  CORBA_RTCUtil::connect_multi("test_connector", prop, port_in_var.in(), target_ports);
```

```
    OpenRTM_aist.CORBA_RTCUtil.connect_multi(
        "test_connector", prop, port_in_var, [port_out_var])
```

#### Deleting All Connectors
To delete all connectors of the target port, use the **disconnect_all** function.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">disconnect_all</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>port_ref</td>
    <td>RTC::PortService_ptr</td>
    <td>Connected port</td>
  </tr>
  <tr>
    <td colspan="3">Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::disconnect_all(port_in_var.in());
```

```
    OpenRTM_aist.CORBA_RTCUtil.disconnect_all_by_ref(port_in_var)
```


<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">disconnect_all</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>port_name</td>
    <td>std::string&</td>
    <td>Port URI</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::disconnect_all("rtcname://localhost:2809/*/ConsoleIn0.out");
```

```
    OpenRTM_aist.CORBA_RTCUtil.disconnect_all_by_name(
        "rtcname://localhost:2809/*/ConsoleIn0.out")
```

### RTC State Operations
#### Activation
To activate an RTC, use the **activate** function.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">activate</th>
  </tr>
  <tr>
    <td colspan="3">CENTER:Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>Execution context ID</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

Since an RTC has a state for each execution context, specify ec_id when changing the state in an execution context other than the default execution context (ID: 0).

```
  CORBA_RTCUtil::activate(consolein.in(), 0);
  CORBA_RTCUtil::activate(consoleout.in(), 0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.activate(consoleout, 0)
    OpenRTM_aist.CORBA_RTCUtil.activate(consolein, 0)
```


#### Deactivation
To deactivate an RTC, use the **deactivate** function.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">deactivate</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>Execution context ID</td>
  </tr>
  <tr>
    <td colspan="3">Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::deactivate(consolein.in(), 0);
  CORBA_RTCUtil::deactivate(consoleout.in(), 0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.deactivate(consoleout, 0)
    OpenRTM_aist.CORBA_RTCUtil.deactivate(consolein, 0)
```

#### Reset
To reset an RTC, use the **reset** function.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">reset</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>Execution context ID</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::reset(consolein.in(), 0);
  CORBA_RTCUtil::reset(consoleout.in(), 0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.reset(consoleout, 0)
    OpenRTM_aist.CORBA_RTCUtil.reset(consolein, 0)
```

#### Getting the RTC State
To get the current state of an RTC, use the **get_state** function.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th colspan="2">get_state</th>
  </tr>
  <tr>
    <td colspan="3">CENTER:Arguments</td>
  </tr>
  <tr>
    <td>Argument Name</td>
    <td>Type Name</td>
    <td>Meaning</td>
  </tr>
  <tr>
    <td>state</td>
    <td>RTC::LifeCycleState</td>
    <td>State</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>Execution context ID</td>
  </tr>
  <tr>
    <td colspan="3">Return Value</td>
  </tr>
  <tr>
    <td>Type Name</td>
    <td colspan="2">Meaning</td>
  </tr>
  <tr>
    <td>bool</td>
    <td colspan="2">true: state retrieval succeeded, false: state retrieval failed</td>
  </tr>
</table>

```
  RTC::LifeCycleState state;
  CORBA_RTCUtil::get_state(state, consoleout.in(), 0);
  std::cout << state << std::endl;
```

```
    ret, state = OpenRTM_aist.CORBA_RTCUtil.get_state(consoleout, 0)
    print(state)
```

Also, you can determine whether the current state is inactive, active, or error using the **is_in_inactive**, **is_in_active**, and **is_in_error** functions.

if (CORBA_RTCUtil::is_in_inactive(consoleout.in()))
```
 {
    std::cout << "Inactive State" << std::endl;
  }
  else if (CORBA_RTCUtil::is_in_active(consoleout.in()))
  {
    std::cout << "Active State" << std::endl;
  }
  else if (CORBA_RTCUtil::is_in_error(consoleout.in()))
  {
    std::cout << "Error State" << std::endl;
  }
```

```
    if OpenRTM_aist.CORBA_RTCUtil.is_in_inactive(consoleout):
        print("Inactive State")
    elif OpenRTM_aist.CORBA_RTCUtil.is_in_active(consoleout):
        print("Active State")
    elif OpenRTM_aist.CORBA_RTCUtil.is_in_error(consoleout):
        print("Error State")
```

### Execution Context Operations
#### Operating the Execution Period
To change the execution period of an execution context, use the **set_default_rate** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>set_default_rate</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>rate</td>
    <td>CORBA::Double</td>
    <td>Execution period</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td>></td>
  </tr>
</table>

```
  CORBA_RTCUtil::set_default_rate(consoleout.in(), 20.0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.set_default_rate(consoleout, 20.0)
```

The set_default_rate function gets the execution period of the default execution context, but to get the execution period from the execution context with the specified ID, use the **set_current_rate** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>set_current_rate</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>Execution context ID</td>
  </tr>
  <tr>
    <td>rate</td>
    <td>CORBA::Double</td>
    <td>Execution period</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td>></td>
  </tr>
</table>

```
  CORBA_RTCUtil::set_current_rate(consoleout.in(), 0, 50.0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.set_current_rate(consoleout, 0, 50.0)
```

To get the current execution period, use the **get_default_rate** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_default_rate</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>CORBA::Double</td>
    <td>></td>
    <td>Execution period</td>
  </tr>
</table>


```
  std::cout << CORBA_RTCUtil::get_default_rate(consoleout.in()) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_default_rate(consoleout))
```

To get the execution period from the execution context with the specified ID, use the **get_current_rate** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_current_rate</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>Execution context ID</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>CORBA::Double</td>
    <td>></td>
    <td>Execution period</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_current_rate(consoleout.in(), 0) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_current_rate(consoleout, 0))
```


#### Attaching and Detaching Execution Contexts

Normally, the execution context generated by the RTC at startup is associated (attached), but by attaching an external execution context to the RTC, the RTC can be driven by the attached execution context.

To attach an execution context to the specified RTC, use the **add_rtc_to_default_ec** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>add_rtc_to_default_ec</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>localcomp</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC that has the execution context to attach as its default execution context</td>
  </tr>
  <tr>
    <td>othercomp</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC to attach</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td>></td>
  </tr>
</table>

```
  CORBA_RTCUtil::add_rtc_to_default_ec(consoleout.in(), consolein.in());
```

```
    OpenRTM_aist.CORBA_RTCUtil.add_rtc_to_default_ec(consoleout, consolein)
```

To detach the attached execution context, use the **remove_rtc_to_default_ec** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>remove_rtc_to_default_ec</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>localcomp</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC that has the execution context to detach as its default execution context</td>
  </tr>
  <tr>
    <td>othercomp</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC to detach</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td>></td>
  </tr>
</table>

```
  CORBA_RTCUtil::remove_rtc_to_default_ec(consoleout.in(), consolein.in());
```

```
    OpenRTM_aist.CORBA_RTCUtil.remove_rtc_to_default_ec(consoleout, consolein)
```

To get a list of attached external RTCs, use the **get_participants_rtc** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_participants_rtc</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC that has the target execution context as its default execution context</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>RTC::RTCList</td>
    <td>></td>
  </tr>
</table>

```
  RTC::RTCList rtclist = CORBA_RTCUtil::get_participants_rtc(consoleout.in());
  for(CORBA::ULong i=0;i < rtclist.length();i++)
  {
    
    std::cout << i << "\t" << CORBA_RTCUtil::get_component_profile(rtclist[i].in()) << std::endl;
  }
```

```
   i = 0
    for rtc in OpenRTM_aist.CORBA_RTCUtil.get_participants_rtc(consoleout):
        print(i, OpenRTM_aist.CORBA_RTCUtil.get_component_profile(rtc))
        i += 1
```

### Configuration Parameter Operations
To set configuration parameters, use the **set_active_configuration** function.
This function sets the parameters of the currently active configuration set.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>set_active_configuration</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>value_name</td>
    <td>std::string&</td>
    <td>Parameter name</td>
  </tr>
  <tr>
    <td>value</td>
    <td>std::string&</td>
    <td>Set value</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>bool</td>
    <td>></td>
    <td>true: setting succeeded, false: setting failed</td>
  </tr>
</table>

```
  CORBA_RTCUtil::set_active_configuration(configsample.in(), "int_param1", "100");
```

```
    OpenRTM_aist.CORBA_RTCUtil.set_active_configuration(
        configsample, "int_param1", "100")
```


When setting a parameter by specifying a configuration set, use the **set_configuration** function.
When this function is executed, the active configuration set is changed.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>set_configuration</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>confset_name</td>
    <td>std::string&</td>
    <td>Configuration set name</td>
  </tr>
  <tr>
    <td>value_name</td>
    <td>std::string&</td>
    <td>Parameter name</td>
  </tr>
  <tr>
    <td>value</td>
    <td>std::string&</td>
    <td>Set value</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>bool</td>
    <td>></td>
    <td>true: setting succeeded, false: setting failed</td>
  </tr>
</table>

```
  CORBA_RTCUtil::set_configuration(configsample.in(), "mode0", "str_param1", "test");
```

```
    OpenRTM_aist.CORBA_RTCUtil.set_configuration(
        configsample, "mode0", "str_param1", "test")
```


To get the name of the currently active configuration set, use the **get_active_configuration_name** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_active_configuration_name</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>std::string</td>
    <td>></td>
    <td>Configuration set name</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_active_configuration_name(configsample.in()) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_active_configuration_name(configsample))
```

To get a list of parameters in the active configuration set, use the **get_active_configuration** function.


<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_active_configuration</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>coil::Properties</td>
    <td>></td>
    <td>Parameter list</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_active_configuration(configsample.in()) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_active_configuration(configsample))
```

To get a list of parameters by specifying a configuration set, use the **get_configuration** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_configuration</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>conf_name</td>
    <td>std::string&</td>
    <td>Configuration set name</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>coil::Properties</td>
    <td>></td>
    <td>Parameter list</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_configuration(configsample.in(), "mode1") << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_configuration(configsample, "mode1"))
```

To get only a specified parameter, use the **get_parameter_by_key** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_parameter_by_key</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>conf_name</td>
    <td>std::string&</td>
    <td>Configuration set name</td>
  </tr>
  <tr>
    <td>value_name</td>
    <td>std::string&</td>
    <td>Parameter name</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>std::string</td>
    <td>></td>
    <td>Parameter value</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_parameter_by_key(configsample.in(), "mode1", "int_param1") << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_parameter_by_key(
        configsample, "mode1", "int_param1"))
```

### Getting RTC and Port Information

#### Getting RTC Information

To get a component profile, use the **get_component_profile** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_component_profile</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>coil::Properties</td>
    <td>></td>
    <td>Component profile information</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_component_profile(consolein.in()) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_component_profile(consolein))
```

#### Getting Port Names

To get a list of names of ports held by the specified RTC, use the **get_port_names** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_port_names</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>coil::vstring</td>
    <td>></td>
    <td>Port name list</td>
  </tr>
</table>

```
  coil::vstring portlist = CORBA_RTCUtil::get_port_names(consolein.in());
  for (auto& port : portlist)
  {
    std::cout << port << std::endl;
  }
```

```
    for port in OpenRTM_aist.CORBA_RTCUtil.get_port_names(consolein):
        print(port)
```

To get a list of InPort names, use the **get_inport_names** function. To get a list of OutPort names, use the **get_outport_names** function. To get a list of service port names, use the **get_svcport_names** function.

```
  coil::vstring inportlist = CORBA_RTCUtil::get_inport_names(consoleout.in());
  for (auto& port : inportlist)
  {
    std::cout << port << std::endl;
  }
```

```
  coil::vstring outportlist = CORBA_RTCUtil::get_outport_names(consolein.in());
  for (auto& port : outportlist)
  {
    std::cout << port << std::endl;
  }
  
  coil::vstring svcportlist = CORBA_RTCUtil::get_svcport_names(myserviceprovider.in());
  for (auto& port : svcportlist)
  {
    std::cout << port << std::endl;
  }
```

```
    for port in OpenRTM_aist.CORBA_RTCUtil.get_inport_names(consoleout):
        print(port)
    for port in OpenRTM_aist.CORBA_RTCUtil.get_outport_names(consolein):
        print(port)
    for port in OpenRTM_aist.CORBA_RTCUtil.get_svcport_names(myserviceprovider):
        print(port)
```

#### Getting a List of Connector Names

To get a list of connector names for a specified port, use the **get_connector_names** function.

<table class="table-alt">
  <tr>
    <th>CENTER:Function Name</th>
    <th>></th>
    <th>get_connector_names</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>port</td>
    <td>RTC::PortService_ptr</td>
    <td>Port object reference</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>coil::vstring</td>
    <td>></td>
    <td>Connector name list</td>
  </tr>
</table>

```
  coil::vstring inconlist = CORBA_RTCUtil::get_connector_names(port_in_var.in());
  for (auto& connector : inconlist)
  {
    std::cout << connector << std::endl;
  }
```

```
    for connector in OpenRTM_aist.CORBA_RTCUtil.get_connector_names_by_portref(port_in_var):
        print(connector)
```

You can also get a list of connector names by specifying the port name.

<table class="table-alt">
  <tr>
    <th colspan="2">Function Name</th>
  </tr>
  <tr>
    <td colspan="3">Arguments</td>
  </tr>
  <tr>
    <td>CENTER:Argument Name</td>
    <td>CENTER:Type Name</td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTC object reference</td>
  </tr>
  <tr>
    <td>port_name</td>
    <td>std::string&</td>
    <td>Port name</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:Return Value</td>
  </tr>
  <tr>
    <td>CENTER:Type Name</td>
    <td>></td>
    <td>CENTER:Meaning</td>
  </tr>
  <tr>
    <td>coil::vstring</td>
    <td>></td>
    <td>Connector name list</td>
  </tr>
</table>

```
  coil::vstring outconlist = CORBA_RTCUtil::get_connector_names(consolein.in(), "ConsoleIn0.out");
  for (auto& connector : outconlist)
  {
    std::cout << connector << std::endl;
  }
```

```
    for connector in OpenRTM_aist.CORBA_RTCUtil.get_connector_names(consolein, "ConsoleIn0.out"):
        print(connector)
```

  </tr>
  <tr>
    <td colspan="3">引数</td>
  </tr>
  <tr>
    <td>引数名</td>
    <td>型名</td>
    <td>意味</td>
  </tr>
  <tr>
    <td>port_ref</td>
    <td>RTC::PortService_ptr</td>
    <td>接続中のポート</td>
  </tr>
  <tr>
    <td colspan="3">戻り値</td>
  </tr>
  <tr>
    <td>型名</td>
    <td colspan="2">意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::disconnect_all(port_in_var.in());
```

```
    OpenRTM_aist.CORBA_RTCUtil.disconnect_all_by_ref(port_in_var)
```


<table class="table-alt">
  <tr>
    <th>関数名</th>
    <th colspan="2">disconnect_all</th>
  </tr>
  <tr>
    <td colspan="3">引数</td>
  </tr>
  <tr>
    <td>引数名</td>
    <td>型名</td>
    <td>意味</td>
  </tr>
  <tr>
    <td>port_name</td>
    <td>std::string&</td>
    <td>ポートのURI</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:戻り値</td>
  </tr>
  <tr>
    <td>型名</td>
    <td colspan="2">意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::disconnect_all("rtcname://localhost:2809/*/ConsoleIn0.out");
```

```
    OpenRTM_aist.CORBA_RTCUtil.disconnect_all_by_name(
        "rtcname://localhost:2809/*/ConsoleIn0.out")
```

### RTCの状態操作
#### アクティブ化
RTCをアクティブ化するためには**activate**関数を使用します。

<table class="table-alt">
  <tr>
    <th>関数名</th>
    <th colspan="2">activate</th>
  </tr>
  <tr>
    <td colspan="3">CENTER:引数</td>
  </tr>
  <tr>
    <td>引数名</td>
    <td>型名</td>
    <td>意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>実行コンテキストのID</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:戻り値</td>
  </tr>
  <tr>
    <td>型名</td>
    <td colspan="2">意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

RTCは状態を実行コンテキストごとに持っているため、デフォルトの実行コンテキスト(ID:0)以外で状態を変更する場合はec_idを指定します。

```
  CORBA_RTCUtil::activate(consolein.in(), 0);
  CORBA_RTCUtil::activate(consoleout.in(), 0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.activate(consoleout, 0)
    OpenRTM_aist.CORBA_RTCUtil.activate(consolein, 0)
```


#### 非アクティブ化
RTCを非アクティブ化するためには**deactivate**関数を使用します。

<table class="table-alt">
  <tr>
    <th>関数名</th>
    <th colspan="2">deactivate</th>
  </tr>
  <tr>
    <td colspan="3">引数</td>
  </tr>
  <tr>
    <td>引数名</td>
    <td>型名</td>
    <td>意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>実行コンテキストのID</td>
  </tr>
  <tr>
    <td colspan="3">戻り値</td>
  </tr>
  <tr>
    <td>型名</td>
    <td colspan="2">意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::deactivate(consolein.in(), 0);
  CORBA_RTCUtil::deactivate(consoleout.in(), 0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.deactivate(consoleout, 0)
    OpenRTM_aist.CORBA_RTCUtil.deactivate(consolein, 0)
```

#### リセット
RTCをリセットするためには**reset**関数を使用します。

<table class="table-alt">
  <tr>
    <th>関数名</th>
    <th colspan="2">reset</th>
  </tr>
  <tr>
    <td colspan="3">引数</td>
  </tr>
  <tr>
    <td>引数名</td>
    <td>型名</td>
    <td>意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>実行コンテキストのID</td>
  </tr>
  <tr>
    <td colspan="3">CENTER:戻り値</td>
  </tr>
  <tr>
    <td>型名</td>
    <td colspan="2">意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td colspan="2">></td>
  </tr>
</table>

```
  CORBA_RTCUtil::reset(consolein.in(), 0);
  CORBA_RTCUtil::reset(consoleout.in(), 0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.reset(consoleout, 0)
    OpenRTM_aist.CORBA_RTCUtil.reset(consolein, 0)
```

#### RTCの状態取得
RTCの現在の状態を取得するためには**get_state**関数を使用します。

<table class="table-alt">
  <tr>
    <th>関数名</th>
    <th colspan="2">get_state</th>
  </tr>
  <tr>
    <td colspan="3">CENTER:引数</td>
  </tr>
  <tr>
    <td>引数名</td>
    <td>型名</td>
    <td>意味</td>
  </tr>
  <tr>
    <td>state</td>
    <td>RTC::LifeCycleState</td>
    <td>状態</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>実行コンテキストのID</td>
  </tr>
  <tr>
    <td colspan="3">戻り値</td>
  </tr>
  <tr>
    <td>型名</td>
    <td colspan="2">意味</td>
  </tr>
  <tr>
    <td>bool</td>
    <td colspan="2">true：状態取得成功、false：状態取得失敗</td>
  </tr>
</table>

```
  RTC::LifeCycleState state;
  CORBA_RTCUtil::get_state(state, consoleout.in(), 0);
  std::cout << state << std::endl;
```

```
    ret, state = OpenRTM_aist.CORBA_RTCUtil.get_state(consoleout, 0)
    print(state)
```

また、**is_in_inactive**関数、**is_in_active**関数、**is_in_error**関数で現在の状態が非アクティブ状態、アクティブ状態、エラー状態かを判定できます。

if (CORBA_RTCUtil::is_in_inactive(consoleout.in()))
```
  {
    std::cout << "Inactive State" << std::endl;
  }
  else if (CORBA_RTCUtil::is_in_active(consoleout.in()))
  {
    std::cout << "Active State" << std::endl;
  }
  else if (CORBA_RTCUtil::is_in_error(consoleout.in()))
  {
    std::cout << "Error State" << std::endl;
  }
```

```
    if OpenRTM_aist.CORBA_RTCUtil.is_in_inactive(consoleout):
        print("Inactive State")
    elif OpenRTM_aist.CORBA_RTCUtil.is_in_active(consoleout):
        print("Active State")
    elif OpenRTM_aist.CORBA_RTCUtil.is_in_error(consoleout):
        print("Error State")
```

### 実行コンテキストの操作
#### 実行周期の操作
実行コンテキストの実行周期を変更するには、**set_default_rate**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>set_default_rate</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>rate</td>
    <td>CORBA::Double</td>
    <td>実行周期</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td>></td>
  </tr>
</table>

```
  CORBA_RTCUtil::set_default_rate(consoleout.in(), 20.0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.set_default_rate(consoleout, 20.0)
```

set_default_rate関数はデフォルトの実行コンテキストの実行周期を取得しますが、指定IDの実行コンテキストから実行周期を取得するためには**set_current_rate**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>set_current_rate</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>実行コンテキストのID</td>
  </tr>
  <tr>
    <td>rate</td>
    <td>CORBA::Double</td>
    <td>実行周期</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td>></td>
  </tr>
</table>

```
  CORBA_RTCUtil::set_current_rate(consoleout.in(), 0, 50.0);
```

```
    OpenRTM_aist.CORBA_RTCUtil.set_current_rate(consoleout, 0, 50.0)
```

現在の実行周期を取得するためには、**get_default_rate**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_default_rate</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>CORBA::Double</td>
    <td>></td>
    <td>実行周期</td>
  </tr>
</table>


```
  std::cout << CORBA_RTCUtil::get_default_rate(consoleout.in()) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_default_rate(consoleout))
```

指定IDの実行コンテキストから実行周期を取得するためには**get_current_rate**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_current_rate</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>ec_id</td>
    <td>RTC::UniqueId</td>
    <td>実行コンテキストのID</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>CORBA::Double</td>
    <td>></td>
    <td>実行周期</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_current_rate(consoleout.in(), 0) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_current_rate(consoleout, 0))
```


#### 実行コンテキストのアタッチ、デタッチ

通常はRTCが起動時に生成する実行コンテキストが関連付け(アタッチ)されていますが、、外部の実行コンテキストをRTCにアタッチすると、アタッチした実行コンテキストでRTCを駆動できるようになります。

実行コンテキストを指定のRTCにアタッチするためには**add_rtc_to_default_ec**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>add_rtc_to_default_ec</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>localcomp</td>
    <td>RTC::RTObject_ptr</td>
    <td>アタッチする実行コンテキストをデフォルト実行コンテキストとして持つRTC</td>
  </tr>
  <tr>
    <td>othercomp</td>
    <td>RTC::RTObject_ptr</td>
    <td>アタッチするRTC</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td>></td>
  </tr>
</table>

```
  CORBA_RTCUtil::add_rtc_to_default_ec(consoleout.in(), consolein.in());
```

```
    OpenRTM_aist.CORBA_RTCUtil.add_rtc_to_default_ec(consoleout, consolein)
```

アタッチした実行コンテキストの関連付け解除(デタッチ)するためには**remove_rtc_to_default_ec**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>remove_rtc_to_default_ec</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>localcomp</td>
    <td>RTC::RTObject_ptr</td>
    <td>デタッチする実行コンテキストをデフォルト実行コンテキストとして持つRTC</td>
  </tr>
  <tr>
    <td>othercomp</td>
    <td>RTC::RTObject_ptr</td>
    <td>デタッチするRTC</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>RTC::ReturnCode_t</td>
    <td>></td>
  </tr>
</table>

```
  CORBA_RTCUtil::remove_rtc_to_default_ec(consoleout.in(), consolein.in());
```

```
    OpenRTM_aist.CORBA_RTCUtil.remove_rtc_to_default_ec(consoleout, consolein)
```

アタッチした外部RTCの一覧を取得するためには**get_participants_rtc**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_participants_rtc</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>対象の実行コンテキストをデフォルト実行コンテキストとして持つRTC</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>RTC::RTCList</td>
    <td>></td>
  </tr>
</table>

```
  RTC::RTCList rtclist = CORBA_RTCUtil::get_participants_rtc(consoleout.in());
  for(CORBA::ULong i=0;i < rtclist.length();i++)
  {
    
    std::cout << i << "\t" << CORBA_RTCUtil::get_component_profile(rtclist[i].in()) << std::endl;
  }
```

```
    i = 0
    for rtc in OpenRTM_aist.CORBA_RTCUtil.get_participants_rtc(consoleout):
        print(i, OpenRTM_aist.CORBA_RTCUtil.get_component_profile(rtc))
        i += 1
```

### コンフィギュレーションパラメータの操作
コンフィギュレーションパラメータの設定をするためには**set_active_configuration**関数を使用します。
この関数では現在アクティブなコンフィギュレーションセットのパラメータが設定されます。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>set_active_configuration</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>value_name</td>
    <td>std::string&</td>
    <td>パラメータ名</td>
  </tr>
  <tr>
    <td>value</td>
    <td>std::string&</td>
    <td>設定値</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>bool</td>
    <td>></td>
    <td>true：設定成功、false：設定失敗</td>
  </tr>
</table>

```
  CORBA_RTCUtil::set_active_configuration(configsample.in(), "int_param1", "100");
```

```
    OpenRTM_aist.CORBA_RTCUtil.set_active_configuration(
        configsample, "int_param1", "100")
```


コンフィギュレーションセットを指定してパラメータを設定する場合は**set_configuration**関数を使用します。
この関数を実行すると、アクティブなコンフィギュレーションセットが変更されます。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>set_configuration</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>confset_name</td>
    <td>std::string&</td>
    <td>コンフィギュレーションセット名</td>
  </tr>
  <tr>
    <td>value_name</td>
    <td>std::string&</td>
    <td>パラメータ名</td>
  </tr>
  <tr>
    <td>value</td>
    <td>std::string&</td>
    <td>設定値</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>bool</td>
    <td>></td>
    <td>true：設定成功、false：設定失敗</td>
  </tr>
</table>

```
  CORBA_RTCUtil::set_configuration(configsample.in(), "mode0", "str_param1", "test");
```

```
    OpenRTM_aist.CORBA_RTCUtil.set_configuration(
        configsample, "mode0", "str_param1", "test")
```


現在アクティブなコンフィギュレーションセットの名前を取得するには**get_active_configuration_name**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_active_configuration_name</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>std::string</td>
    <td>></td>
    <td>コンフィギュレーションセット名</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_active_configuration_name(configsample.in()) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_active_configuration_name(configsample))
```

アクティブなコンフィギュレーションセットのパラメータ一覧を取得するには**get_active_configuration**関数を使用します。


<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_active_configuration</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>coil::Properties</td>
    <td>></td>
    <td>パラメータ一覧</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_active_configuration(configsample.in()) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_active_configuration(configsample))
```

コンフィギュレーションセットを指定してパラメータ一覧を取得するには**get_configuration**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_configuration</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>conf_name</td>
    <td>std::string&</td>
    <td>コンフィギュレーションセット名</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>coil::Properties</td>
    <td>></td>
    <td>パラメータ一覧</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_configuration(configsample.in(), "mode1") << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_configuration(configsample, "mode1"))
```

指定のパラメータのみを取得する場合は**get_parameter_by_key**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_parameter_by_key</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>conf_name</td>
    <td>std::string&</td>
    <td>コンフィギュレーションセット名</td>
  </tr>
  <tr>
    <td>value_name</td>
    <td>std::string&</td>
    <td>パラメータ名</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>std::string</td>
    <td>></td>
    <td>パラメータの値</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_parameter_by_key(configsample.in(), "mode1", "int_param1") << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_parameter_by_key(
        configsample, "mode1", "int_param1"))
```

### RTC、ポートの情報取得

#### RTCの情報取得

コンポーネントプロファイルを取得するには**get_component_profile**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_component_profile</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>coil::Properties</td>
    <td>></td>
    <td>コンポーネントプロファイルの情報</td>
  </tr>
</table>

```
  std::cout << CORBA_RTCUtil::get_component_profile(consolein.in()) << std::endl;
```

```
    print(OpenRTM_aist.CORBA_RTCUtil.get_component_profile(consolein))
```

#### ポート名取得

指定のRTCが保持しているポートの名前一覧を取得するには**get_port_names**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_port_names</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>coil::vstring</td>
    <td>></td>
    <td>ポート名一覧</td>
  </tr>
</table>

```
  coil::vstring portlist = CORBA_RTCUtil::get_port_names(consolein.in());
  for (auto& port : portlist)
  {
    std::cout << port << std::endl;
  }
```

```
    for port in OpenRTM_aist.CORBA_RTCUtil.get_port_names(consolein):
        print(port)
```

InPortの名前一覧を取得するには**get_inport_names**関数、OutPortの名前一覧を取得するには**get_outport_names**関数、サービスポートの名前一覧を取得するには**get_svcport_names**関数を使用します。

```
  coil::vstring inportlist = CORBA_RTCUtil::get_inport_names(consoleout.in());
  for (auto& port : inportlist)
  {
    std::cout << port << std::endl;
  }
```

```
  coil::vstring outportlist = CORBA_RTCUtil::get_outport_names(consolein.in());
  for (auto& port : outportlist)
  {
    std::cout << port << std::endl;
  }
  
  coil::vstring svcportlist = CORBA_RTCUtil::get_svcport_names(myserviceprovider.in());
  for (auto& port : svcportlist)
  {
    std::cout << port << std::endl;
  }
```

```
    for port in OpenRTM_aist.CORBA_RTCUtil.get_inport_names(consoleout):
        print(port)
    for port in OpenRTM_aist.CORBA_RTCUtil.get_outport_names(consolein):
        print(port)
    for port in OpenRTM_aist.CORBA_RTCUtil.get_svcport_names(myserviceprovider):
        print(port)
```

#### コネクタの名前一覧取得

指定ポートのコネクタの名前一覧を取得するには**get_connector_names**関数を使用します。

<table class="table-alt">
  <tr>
    <th>CENTER:関数名</th>
    <th>></th>
    <th>get_connector_names</th>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>port</td>
    <td>RTC::PortService_ptr</td>
    <td>ポートのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>coil::vstring</td>
    <td>></td>
    <td>コネクタ名一覧</td>
  </tr>
</table>

```
  coil::vstring inconlist = CORBA_RTCUtil::get_connector_names(port_in_var.in());
  for (auto& connector : inconlist)
  {
    std::cout << connector << std::endl;
  }
```

```
    for connector in OpenRTM_aist.CORBA_RTCUtil.get_connector_names_by_portref(port_in_var):
        print(connector)
```

ポート名を指定してコネクタの名前一覧を取得することもできます。

<table class="table-alt">
  <tr>
    <th colspan="2">関数名</th>
  </tr>
  <tr>
    <td colspan="3">引数</td>
  </tr>
  <tr>
    <td>CENTER:引数名</td>
    <td>CENTER:型名</td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>rtc</td>
    <td>RTC::RTObject_ptr</td>
    <td>RTCのオブジェクトリファレンス</td>
  </tr>
  <tr>
    <td>port_name</td>
    <td>std::string&</td>
    <td>ポート名</td>
  </tr>
  <tr>
    <td>></td>
    <td>></td>
    <td>CENTER:戻り値</td>
  </tr>
  <tr>
    <td>CENTER:型名</td>
    <td>></td>
    <td>CENTER:意味</td>
  </tr>
  <tr>
    <td>coil::vstring</td>
    <td>></td>
    <td>コネクタ名一覧</td>
  </tr>
</table>

```
  coil::vstring outconlist = CORBA_RTCUtil::get_connector_names(consolein.in(), "ConsoleIn0.out");
  for (auto& connector : outconlist)
  {
    std::cout << connector << std::endl;
  }
```

```
    for connector in OpenRTM_aist.CORBA_RTCUtil.get_connector_names(consolein, "ConsoleIn0.out"):
        print(connector)
```



-------jp page!!-------
