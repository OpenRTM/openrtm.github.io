---
layout: page
title: "list of rtc.conf setting items"
---

#contents(3)

## General Settings

### config.version
Configuration file version.

This parameter is the internally set configuration version.
Normally, it is the same version as OpenRTM-aist. It does not need to be set in rtc.conf and is a read-only parameter.
By reading this version, you can know the versions of rtc.conf and OpenRTM-aist.

- Setting: Read-only. No effect from setting.
- Default: Same as the current OpenRTM-aist version.
- Example:
```
 config.version: 2.0
```

### openrtm.name

This parameter is the name of OpenRTM-aist, including the version set internally.
It is a read-only parameter and does not need to be set in rtc.conf.
By reading this parameter, you can know the name and version of OpenRTM-aist.

- Setting: Read-only. No effect from setting.
- Default: OpenRTM-aist name with the current version
- Example:
openrtm.name: OpenRTM-aist-2.0.0

### openrtm.version
OpenRTM-aist version.
- Example:
```
 openrtm.version: 1.0.0
```

## Settings Related to the Name Service

### naming.enable

This option enables or disables functions related to the naming service.
If YES is specified, the RTC reference is registered with the name service. If NO is specified, the RTC reference is not registered with the name service.

- Specification: **YES** or **NO**
- Default value: YES
- Example:
```
 manager.is_master: NO
```

### naming.type

This option specifies the type of name service. Currently, only corba is supported.
- Specification: Name service type
- Default value: corba
- Example:
```
 naming.type: corba
```

### naming.formats

Specifies the format used when registering an RTC with the name server. The following specifiers starting with **%** can be used. The delimiter for the name hierarchy is **/**, and the delimiter between name and kind is **.**.

<table class="table-alt">
  <tr>
    <td>%n</td>
    <td>RTC instance name</td>
  </tr>
  <tr>
    <td>%t</td>
    <td>RTC type name</td>
  </tr>
  <tr>
    <td>%m</td>
    <td>RTC module name</td>
  </tr>
  <tr>
    <td>%v</td>
    <td>RTC version</td>
  </tr>
  <tr>
    <td>%V</td>
    <td>RTC vendor name</td>
  </tr>
  <tr>
    <td>%c</td>
    <td>RTC category name</td>
  </tr>
  <tr>
    <td>%h</td>
    <td>Host name</td>
  </tr>
  <tr>
    <td>%M</td>
    <td>Manager name</td>
  </tr>
  <tr>
    <td>%p</td>
    <td>Process ID</td>
  </tr>
</table>

- Specification: /<name>.<kind>/<name>.<kind>/...
- Default value: %h.host_cxt/%n.mgr
- Example:
```
 naming.formats: %h.host/%n.rtc
```

### naming.update.enable

Registration of an RTC with the name server is normally performed when the instance is created. Therefore, the RTC name and reference are not registered with a name server that is started after the RTC is created. By specifying this option, the name server is checked periodically, and if the name server is confirmed to have started, the name and reference are registered again.

- Specification: **YES** or **NO**
- Default value: YES
- Example:
```
 naming.update.enable: YES
```

### naming.update.interval

When naming.update.enable is YES, this specifies the cycle for checking and re-registering with the name server.

- Specification: Specify the registration cycle in [s].
- Default value: 10.0
- Example:
```
 naming.update.interval: 10.0
```

### naming.update.rebind

If YES is specified for this option, registration is performed again even when the name has been deleted on a name server where the name and reference are already registered.

- Specification: **YES** or **NO**
- Default value: NO
- Example:
```
 naming.update.rebind: NO
```

<!-- Logger configurations -->

## Logger-Related Settings

### logger.enable

Specifies whether to enable or disable the logger.

- Specification: **YES** or **NO**
- Default value: YES
- Example:
```
 logger.enable: YES
```

### logger.file_name

Specifies the log file name. Output to multiple files can also be specified by separating them with commas. The specifier %p, which replaces the process ID, can be used. Also, if the file name is set to **stdout**, logs are output to standard output.

- Specification: File name including path
- Default value: ./rtc%p.log
- Example:
```
 logger.file_name: /tmp/rtc%p.log
 logger.file_name: /tmp/rtc%p.log, stdout
```

### logger.date_format

Specifies the date and time format written to the log. The following format specifiers similar to strftime(3) can be used. If the time is not specified, specify **No** or **Disable**.

<table class="table-alt">
  <tr>
    <td>%a</td>
    <td>abbreviated weekday name</td>
  </tr>
  <tr>
    <td>%A</td>
    <td>full weekday name</td>
  </tr>
  <tr>
    <td>%b</td>
    <td>abbreviated month name</td>
  </tr>
  <tr>
    <td>%B</td>
    <td>full month name</td>
  </tr>
  <tr>
    <td>%c</td>
    <td>the standard date and time string</td>
  </tr>
  <tr>
    <td>%d</td>
    <td>day of the month, as a number (1-31)</td>
  </tr>
  <tr>
    <td>%H</td>
    <td>hour, 24 hour format (0-23)</td>
  </tr>
  <tr>
    <td>%I</td>
    <td>hour, 12 hour format (1-12)</td>
  </tr>
  <tr>
    <td>%j</td>
    <td>day of the year, as a number (1-366)</td>
  </tr>
  <tr>
    <td>%m</td>
    <td>month as a number (1-12). <br> Note: some versions of Microsoft Visual C++ may use values that range from 0-11.</td>
  </tr>
  <tr>
    <td>%M</td>
    <td>minute as a number (0-59)</td>
  </tr>
  <tr>
    <td>%p</td>
    <td>locale's equivalent of AM or PM</td>
  </tr>
  <tr>
    <td>%S</td>
    <td>second as a number (0-59)</td>
  </tr>
  <tr>
    <td>%U</td>
    <td>week of the year, sunday as the first day</td>
  </tr>
  <tr>
    <td>%w</td>
    <td>weekday as a decimal (0-6, sunday=0)</td>
  </tr>
  <tr>
    <td>%W</td>
    <td>week of the year, monday as the first day</td>
  </tr>
  <tr>
    <td>%x</td>
    <td>standard date string</td>
  </tr>
  <tr>
    <td>%X</td>
    <td>standard time string</td>
  </tr>
  <tr>
    <td>%y</td>
    <td>year in decimal, without the century (0-99)</td>
  </tr>
  <tr>
    <td>%Y</td>
    <td>year in decimal, with the century</td>
  </tr>
  <tr>
    <td>%Z</td>
    <td>time zone name</td>
  </tr>
  <tr>
    <td>%%</td>
    <td>a percent sign</td>
  </tr>
</table>

- Specification: /<name>.<kind>/<name>.<kind>/...
- Default value: %b %d %H:%M:%S
- Example:
```
 logger.date_format: No
 logger.date_format: Disable
 logger.date_format: [%Y-%m-%dT%H.%M.%S%Z]     // W3C standard format
 logger.date_format: [%b %d %H:%M:%S]          // Syslog format
 logger.date_format: [%a %b %d %Y %H:%M:%S %Z] // RFC2822 format
 logger.date_format: [%a %b %d %H:%M:%S %Z %Y] // data command format
 logger.date_format: [%Y-%m-%d %H.%M.%S]
```

### logger.log_level

The following log levels can be specified.

- SILENT
- FATAL
- ERROR
- WARN
- INFO
- DEBUG
- TRACE
- VERBOSE
- PARANOID

The actual levels of log messages recorded when each log level is specified are as follows.

<table class="table-alt">
  <tr>
    <td>SILENT</td>
    <td>completely silent</td>
  </tr>
  <tr>
    <td>FATAL</td>
    <td>includes (FATAL)</td>
  </tr>
  <tr>
    <td>ERROR</td>
    <td>includes (FATAL, ERROR)</td>
  </tr>
  <tr>
    <td>WARN</td>
    <td>includes (FATAL, ERROR, WARN)</td>
  </tr>
  <tr>
    <td>INFO</td>
    <td>includes (FATAL, ERROR, WARN, INFO)</td>
  </tr>
  <tr>
    <td>DEBUG</td>
    <td>includes (FATAL, ERROR, WARN, INFO, DEBUG)</td>
  </tr>
  <tr>
    <td>TRACE</td>
    <td>includes (FATAL, ERROR, WARN, INFO, DEBUG, TRACE)</td>
  </tr>
  <tr>
    <td>VERBOSE</td>
    <td>includes (FATAL, ERROR, WARN, INFO, DEBUG, TRACE, VERBOSE)</td>
  </tr>
  <tr>
    <td>PARANOID</td>
    <td>includes (FATAL, ERROR, WARN, INFO, DEBUG, TRACE, VERBOSE, PARA)</td>
  </tr>
</table>

The log levels **TRACE**, **VERBOSE**, and **PARANOID** usually generate huge log files. If **PARANOID** is specified, the log format may be broken.

- Specification: (SILENT|FATAL|ERROR|WARN|INFO|DEBUG|TRACE|VERBOSE|PARANOID)
- Default value: INFO
- Example:
```
 logger.log_level: DEBUG
```

### logger.clock_type

The logger.clock_type option specifies the type of clock to use for log message timestamps.
Currently, the following three clock types are available.

- system: system clock [default]
- logical: logical clock
- adjusted: adjusted clock

To use the logical time clock, specify the following somewhere in the program.
```
 coil::ClockManager::instance().getClock("logical").settime()
```

- Setting: system, logical, adjusted
- Default: system
- Example:
```
 logger.clock_type: system
```

### logger.escape_sequence_enable

This option specifies whether to color log output. If logger.file_name: stdout is specified and the terminal supports escape sequences, log output is displayed in color. It is not recommended to color output to files.

- Setting: YES or NO
- Default: NO
- Example:
```
 logger.escape_sequence_enable: NO
```


## Settings Related to CORBA

### corba.args

Specifies arguments to pass to CORBA. CORBA has command-line options that differ by implementation. Normally, command-line arguments are passed to ORB_init(), which is a CORBA API function, and this option passes the specified string to this ORB_init() function.

- Specification: String
- Default: Empty string
- Example:
```
 corba.args: -ORBInitialHost myhost -ORBInitialPort 8888
```

#### Specification Example 1

When sending image data or similar through a data port, care is required if the data size sent at one time exceeds about 2 MB.
In omniORB, the size that can be handled by giop (General Inter-ORB Protocol) is "2097152B (2 MB)" by default, and if you try to send data exceeding this size, correct data cannot be sent due to the giop limit.
The maximum size can be changed using the corba.args option. This specification must be made for both OutPort and InPort.

```
 corba.args: -ORBgiopMaxMsgSize 3145728 # この行を追加
                                        # Maxサイズを3Mに指定
```

In addition to specifying this in corba.args, this limit can also be relaxed by specifying the environment variable as follows.

```
  export ORBgiopMaxMsgSize=3145728
```

- (Reference) (omniORB configuration and API) http://omniorb.sourceforge.net/omni41/omniORB/omniORB004.html


### corba.endpoint [Deprecated]

This option has been replaced by corba.endpoints. Deprecated.


### corba.endpoints

In CORBA, remote objects are accessed using a reference called an IOR, and the IOR usually contains only one set of the address and port number of the node on which the object operates. If the node running OpenRTM has two or more network interfaces, an unintended address may be assigned as the node address included in the IOR.

To resolve this, this option can specify the network address used by CORBA. It is specified as **host address:port number**, but the port number can be omitted.

Depending on the ORB implementation, multiple addresses can be included in the IOR. However, in JavaIDL, the standard CORBA for Java, problems such as slow operation have been reported when accessing an object through an IOR that specifies multiple addresses, so caution is required.

Multiple **address:port** pairs can be specified by separating them with **, (comma)**. By specifying **all** as a special string, all addresses of the node can also be included in the IOR.

- Specification: <host_addr>:<port>, <host_addr>:<port>, ... or all
- Default: Empty string
- Example:
```
 corba.endpoints: 192.168.1.10:1111, 192.168.10.11:2222
 corba.endpoints: 192.168.1.10, 192.168.10.11
 corba.endpoints: all
```

corba.endpoints:

### corba.endpoints_ipv4: [readonly]

This parameter is read-only and is set to the IPv4 endpoint currently used by the current process.
By reading this parameter, you can know the endpoint currently being used.

- Setting: Read-only
- Default: none
- Example:
```
 corba.endpoints_ipv6: [readonly]
```

### corba.endpoints_ipv6: [readonly]

This parameter is read-only and is set to the IPv6 endpoint currently used by the current process.
By reading this parameter, you can know the endpoint currently being used.

- Setting: Read-only
- Default: none
- Example:
```
 corba.endpoints_ipv6: [readonly]
```

### corba.endpoint_property

This option specifies which available endpoint address is to be used as either an IPv4 or IPv6 address.

- Setting: {ipv4|ipv6}(<number of endpoint address>, ...), 
- Default: none
- Example:
```
 corba.endpoint_property: ipv4
 corba.endpoint_property: ipv4, ipv6(0)
 corba.endpoint_property: ipv6
 corba.endpoint_property: ipv4(0,1), ipv6(2,3)
```

### corba.nameservers

This option specifies the name server to which RTCs and similar objects are registered. Multiple name servers can be specified by separating them with commas. Even if there is no name server at the specified address and port number, no particular error occurs, and RTC names are registered only with existing name servers.
If the port number is omitted, the default port number 2809 is used.

- Specification: <host_addr>:<port>, <host_addr>:<port>, ...
- Default: localhost
- Example:
```
 corba.nameservers: openrtm.aist.go.jp:9876
 corba.nameservers: rtm0.aist.go.jp, rtm1.aist.go.jp, rtm2.aist.go.jp
 corba.nameservers: localhost
```

### corba.nameservice.replace_endpoint

When a node has multiple NICs, the address included in the RTC's IOR registered on the name server may be inappropriate. For example, if a node has two addresses, 192.168.0.10 and 192.168.1.10, and is registered on two name servers located at 192.168.0.1 and 192.168.1.1, and if 192.168.0.10 is the network interface used by default on that node, the IOR registered on the above two name servers will include only 192.168.0.10. In this case, on the 192.168.1.0 network, the IOR on the name server becomes meaningless because it contains an unreachable address.

When this option is specified, in a case like the above, the address of the IOR registered with the 192.168.1.1 name server is replaced with 192.168.1.10.

However, by specifying this option, other nodes on the 192.168.1.0 network can use the profile and similar information of the RTC, but cannot perform port connections and similar operations.

- Specification: **YES** or **NO**
- Default: NO
- Example:
```
 corba.nameservice.replace_endpoint: NO
```


### corba.alternate_iiop_addresses

This option adds alternate IIOP addresses to the IOR profile.
The IOR can include additional endpoints for the servant (the CORBA object server). This is almost equivalent to the "corba.endpoints" option, but differs in that it does not actually create endpoints.
(The "corba.endpoints" option attempts to create actual endpoints, and returns an error if it cannot.) This option simply adds alternate IIOP endpoint address information to the IOR.

This option is used when placing an RTC inside a NAT or router.
In general, RTCs inside a private network cannot connect to RTCs on the global network. However, if port forwarding on the NAT or router is configured appropriately, RTCs on the global side can connect to RTCs in the private network.

Configure it as follows.

1. Configure port forwarding on the NAT or router appropriately.
  - Here, configure it so that port 2810 on the global side is forwarded to port 2810 of an address on the private side.
1. Configure rtc.conf of the RTC on the private side as follows.
```
  corba.nameservers: my.global.nameserver.com <- グローバル側のネームサーバを設定
  corba.endpoints: :2810 <- コンポーネントのポート番号
  corba.alternate_iiop_addresses: w.x.y.z:2810 <- ルータのグローバル側のIPアドレスとポート番号
```
1. Start the RTC on the global side and the RTC on the private side

In RTSystemEditor, access to the RTC on the private side may become extremely slow. This is thought to be because Java's IOR additional profile function is not sufficiently implemented, so it takes time to reach the private side. Using rtshell or similar tools can reduce the time required for connection. Also, even if connection with RTSystemEditor or rtshell takes time, the communication speed between ports once connected is usually almost unchanged.

- Specification: address:port
- Default: Unspecified
- Example:
```
 corba.alternate_iiop_addresses: addr:port
```

## Settings Related to manager

### manger.name

Name of the manager. When the manager is registered with the name server, it is registered with the name set here.
This "manager.name" is used to group master/slave managers by the stringified CORBA object name. If "manager.name" is set to "manager" and the manager is the master, the object reference is placed as follows.

```
 corbaloc::<hostname>:2810/manager 
```

Other slave managers have the following stringified IOR.
```
 corbaloc::<hostname>:<port_number>/manager
```

- Specification: Any name that can be registered with a name server, etc.
- Default value: manager
- Example:
```
 manager.name: manager
```

### manager.instance_name

Instance name of the manager.

This "manager.instance_name" is used as the name of the manager when registering with the name service. Normally, the master manager reference is registered with the name "manager|mgr" in the name server. If this option is set to "foobar", the registered master manager name becomes "foobar|mgr".
- Setting: Any manager name string
- Default: manager
- Example:
```
 manager.instance_name: manager
```

### manager_naming_formats

Specifies the format used when registering the manager with the name server. The following specifiers starting with **%** can be used.

<table class="table-alt">
  <tr>
    <th>Specifier</th>
    <th>Meaning</th>
  </tr>
  <tr>
    <td>%n</td>
    <td>Manager name</td>
  </tr>
  <tr>
    <td>%h</td>
    <td>Host name</td>
  </tr>
  <tr>
    <td>%M</td>
    <td>Manager name</td>
  </tr>
  <tr>
    <td>%p</td>
    <td>Manager process ID</td>
  </tr>
</table>

- Specification: /<name>.<kind>/<name>.<kind>/...
- Default value: %h.host_cxt/%n.mgr
- Example:
```
 manager.name: %h.host_cxt/%n.mgr
```

### manager.is_master

Specifies whether to make the process a master manager. If the command-line option **-d** is specified, this becomes the master manager even if this value is set to NO.

- Specification: **YES** or **NO**
- Default value: NO
- Example:
```
 manager.is_master: NO
```

### manager.corba_servant

Specifies whether to start the manager's CORBA servant. If YES is set, the manager's CORBA servant starts, allowing the manager to be operated remotely. If NO is set, the CORBA servant does not start, so the manager cannot be operated via CORBA.

- Specification: **YES** or **NO**
- Default value: YES
- Example:
```
 manager.corba_servant: YES
```

### corba.master_manager

Address and port number of the master manager. The master manager can be accessed using a corbaloc-format URL specification, and this specifies the port number to use at that time. The slave manager also interprets the master manager specified here as its own master manager, accesses the master manager at startup, and performs negotiation.

- Specification: <host_name>:<port>
- Default: localhost:2810
- Example:
```
 corba.master_manager: localhost:2810
```

### manager.update_master_manager.enable

Automatic update of master manager registration with the slave manager

This option is valid for slave managers. A slave manager must register itself with the master manager. If this option is set to "YES", the slave manager periodically registers with the master manager. If "NO" is set, the slave manager is registered with the master manager only once at startup.

- Setting: YES/NO (Read/Write)
- Default: YES
- Example:
```
 manager.update_master_manager.enable:YES
```

### manager.update_master_manager.interval

Registration update cycle of the slave manager to the master manager

This option is related to corba.update_master_manager.enable.
If the "corba.update_master_manager.enable" option is set to YES, the update interval is set by this option. The default interval is 10 seconds.
- Setting: seconds (Read/Write)
- Default: 10.0
- Example:
manager.update_master_manager.interval: 10.0

### manager.components.naming_policy

This option specifies the naming (numbering) policy for RTCs. When an RTC instance is created, a name is assigned by adding an incremental number to the component type name (type_name) as follows.

```
 <type_name> <number>
 example: ConsoleOut0、ConsoleOut1、ConsoleOut2、...
```

By default, components of the same type in the same process are numbered sequentially from 0, so RTCs created in different processes or on different nodes (computers) may have the same name. When these RTCs are registered with the name server (ns), RTCs with the same path and same name overwrite each other's object references, making it impossible to access the desired RTC. Therefore, two policies are provided: "node_unique", which assigns a unique number to each node, and "ns_unique", which assigns a unique number on the name server.

By default, the following three options can be specified.

- process_unique: Specifies a name (number) unique within the process
- node_unique: Specifies a name (number) unique within the node
- ns_unique: Specifies a name (number) unique within the name server

The policy can be extended by the user.

- Setting: Read/Write, {process_unique, node_unique, ns_unique}
- Default: process_unique
- Example:
```
 manager.components.naming_policy: process_unique
```

### manager.components.precreate

Pre-creation of components

This option specifies the names (module names) of components to create in advance before starting the manager event loop. Component factories must be registered with the "manager.module.preload" option or statically linked to the manager.

- Setting: Read/Write, <component class name>, ...
- Default: None
- Example:
```
 manager.components.precreate: ConsoleIn, ConsoleOut, SeqIn, SeqOut
```

### manager.components.preconnect
&aname(preconnect);

Pre-creation of connections. This option specifies the connectors to create before starting the manager event loop.
The target components and ports must have been created in advance using the "manager.components.precreate" option.
Ports are specified in the format "<comp0>.<Port0>?port=<comp1>.<port1>&<option_key>=<option_value>&...".
If dataflow_type or interface_type is not specified, "dataflow_type = push" and "interface_type = corba_cdr" are automatically specified.

- Setting: <comp0>.<Port0>?port=<comp1>.<port1>&<option_key>=<option_value>&...
- Default: none
- Example:
```
 manager.components.preconnect: ConsoleIn0.out?port=ConsoleOut0.in& \ 
                                                    dataflow_type=push&interface_type=corba_cdr, \ 
                                                    SeqIn0.octet?port=SeqOut0.octet& \ 
                                                    dataflow_type=push&interface_type=direct
```

### manager.components.preactivation
&aname(preactivation);

Pre-activation of components. This option specifies the names (module names) of components to activate in advance before starting the manager event loop. The target components must be created in advance with the manager.components.precreate option.

- Setting: Read/Write, <component class name>, ...
- Default: None
- Example:
```
 manager.components.preactivation: ConsoleIn0, ConsoleOut0
```

### manager.cpu_affinity

This option binds the manager process to a specific CPU.
The option argument must be one or more CPU IDs separated by commas.
CPU IDs start from 0, and the maximum value is the number of CPU cores minus 1.
If an invalid CPU ID is specified, this process is configured to use all CPUs.

- Specification: Specify CPU IDs to bind, separated by commas
- Default: none
- Example:
```
 manager.cpu_affinity: 0,1
```


## Manager Lifecycle Options

### manager.shutdown_on_nortcs:

Specifies whether to shut down the manager and terminate the process when there are no RTCs left in the process, that is, when the last RTC in the same process has terminated. If YES, the process terminates when there are no RTCs left. If NO, the manager and process continue running even when there are no RTCs.

- Specification: **YES** or **NO**
- Default: YES
- Example:
```
 manager.shutdown_on_nortcs: YES
```

### manager.shutdown_auto

Checks at regular intervals whether there are RTCs in the process, and specifies whether to shut down the manager and process if there are no RTCs. If YES, the manager and process are automatically shut down if there are no RTCs. If NO, the manager and process continue operating even if there are no RTCs.

The difference from manager.shutdown_on_nortcs is that the shutdown trigger is RTC deletion for manager.shutdown_on_nortcs, whereas it is time for manager.shutdown_auto.
- Specification: **YES** or **NO**
- Default: YES
- Example:
```
 manager.shutdown_auto: YES
```

### manager.auto_shutdown_duration

Cycle for checking whether RTCs exist in the process. The unit is seconds. If manager.shutdown_auto above is set to YES, this option is used as the cycle for checking whether RTCs exist.

- Specification: Numeric value (unit [s])
- Default: 10.0
- Example:
```
 manager.auto_shutdown_duration: 10.0
```

### manager.termination_waittime

Specifies the manager termination wait time. This option specifies the time from a termination request to the manager until the actual termination thread starts execution. The unit is seconds. Normally, you do not need to specify or change this option. However, if an exception occurs because another termination process is executed before CORBA termination processing finishes normally, adjusting this time may solve the problem.

- Setting: Read/Write, duration [s]
- Default: 0.5
- Example:
manager.termination_waittime: 0.5

## Options Related to Module Management

### manager.modules.load_path

The manager searches for modules from the search path list specified by this option. Paths are listed separated by commas. The path delimiter is / on both UNIX and Windows.

- Specification: /dir_name0/dir_name1/..., /dir_name0/dir_name1/...
- Default value: ./
- Example:
```
 manager.modules.load_path: C:/Program Files/OpenRTM-aist
 manager.modules.load_path: /usr/lib, /usr/local/lib,       \
                            /usr/local/lib/OpenRTM-aist/libs
```

### manager.modules.preload:

The manager can load loadable modules in advance at startup.
The loadable modules specified by this option are searched for from the search paths specified by **manager.modules.load_path**.
If YES is specified for **manager.modules.abs_path_allowed**, loadable modules can also be specified with absolute paths.

- Specification: <module_name>.dll, <module_name>.dll, ...
- Default value: Empty
- Example:
```
 manager.modules.preload: ConsoleIn.dll, ConsoleOut.dll
 manager.modules.preload: ConsoleIn.so, ConsoleOut.so
 manager.modules.abs_path_allowed: YES
 manager.modules.preload: /usr/lib/OpenRTM-aist/ConsoleIn.so
```

### manager.modules.abs_path_allowed

Flag allowing absolute path specification for modules. If this option is YES, absolute path specification for modules is allowed.

- Specification: **YES** or **NO**
- Default value: YES
- Example:
```
 manager.modules.abs_path_allowed: YES
```

### manager.modules.search_auto

Enables automatic module search functionality.
This option specifies whether to automatically search for RTC loadable modules. If this option is set to "YES", when RTC instantiation is requested of the manager, the target RTC loadable module (such as a DLL) is automatically searched for, loaded from the module search path, and the component is instantiated. If NO, the loadable module of the target RTC must be loaded in advance.

- Setting: Read/Write, YES / NO
- Default: YES
- Example:
```
 manager.modules.search_auto: YES
```

### manager.preload.modules: none
List of modules to load before CORBA initialization

This option specifies modules to load before CORBA initialization. Loadable modules that implement some functions must be loaded before CORBA initialization, and such modules are specified with this option. The method of specifying modules is the same as manager.modules.preload.

- Setting: <module_name>(.<extention>) (init_func_name), ...
- Default: none
- Example: 
```
   manager.preload.modules: SSLTransport.dll
   manager.preload.modules: SSLTransport.py
   manager.preload.modules: SSLTransport
   manager.preload.modules: \
   C:\\Python27\\Lib\\site-packages\\OpenRTM_aist\\ext\\SSLTransport
```

<!-- # -->
<!-- # The following options are not implemented yet.  -->
<!-- # -->
<!-- # manager.modules.config_ext: -->
<!-- # manager.modules.config_path: -->
<!-- # manager.modules.detect_loadable: -->
<!-- # manager.modules.init_func_suffix: -->
<!-- # manager.modules.init_func_prefix: -->
<!-- # manager.modules.download_allowed: -->
<!-- # manager.modules.download_dir: -->
<!-- # manager.modules.download_cleanup: -->
<!-- # -->

## Manager Language Support Options

### manager.supported_languages

The master manager starts slave managers and RTCs in response to requests from remote applications and the like. Slave managers may be not only the C++ language version, but also the Java version, Python version, and so on.


- Specification: Specify languages such as C++, Java, Python separated by commas
- Default: C++, Java, Python3
- Example:
```
 manager.supported_languages: C++, Python3, Java
```

### manager.modules.`<lang>`.suffixes

RTC module extensions for each language.
This option specifies the extensions of loadable module RTCs.

```
  manager.modules.<lang>.suffixes
```

The `<lang>` part must be specified in manager.supported_languages. The "." (dot) is not required. Appropriate default extensions are specified for the C++, Python / Python3, and Java languages respectively, so normally no setting is required.

- Specification: Extension name of shared object
- Default:
  - Windows: dll
  - Linux, etc.: so
  - Mac OS X: dylib
- Example
```
 manager.modules.C++.suffixes: dll
 manager.modules.C++.suffixes: so
 manager.modules.C++.suffixes: dylib
```

### manager.modules.`<lang>`.manager_cmd

Manager program name for each language.
This option specifies the name of the executable manager for each language. When the master manager is requested to instantiate an RTC, the slave manager is executed, and the RTC is instantiated in the slave manager process. C++ version RTCs use the C++ version manager (rtcd), and Python version RTCs use the Python version manager (rtcd_python). Default executables in the command search path are specified for the C++, Python / Python3, and Java languages respectively. Normally, no setting is required.

- Specification: Manager command name
- Default:
  - C++: rtcd
  - Python: rtcd_python
  - Java: rtc_java
- Example
```
 manager.modules.C++.manager_cmd: rtcd
 manager.modules.Python.manager_cmd: rtcd_python
 manager.modules.Java.manager_cmd: rtcd_java
```

### manager.modules.`<lang>`.profile_cmd

Profile acquisition command name for each language.
This option specifies, for each language, the name of the profile executable, which is the command for acquiring RTC profiles. When searching for RTCs from existing loadable modules, the master manager executes the profile command to acquire the profile of each component from the loadable module. C++ version RTCs use the C++ version profile command (rtcprof), and Python version RTCs use the Python version manager (rtcprof_python). The command search path must be set to the specified executable file. Appropriate default executables are specified for the C++, Python / Python3, and Java languages respectively, so normally no setting is required.

- Specification: Profile acquisition command name
- Default:
  - C++: rtcprof
  - Python: rtcprof_python
  - Python3: rtcprof_python3
  - Java: rtc_java
- Example
```
 manager.modules.C++.profile_cmd: rtcprof
 manager.modules.Python.profile_cmd: rtcprof_python
 manager.modules.Java.profile_cmd: rtcprof_java
```

### manager.modules.`<lang>`.load_paths

RTC module load paths for each language.
This option specifies the load paths for loadable module RTCs in each language. When the master manager searches for RTCs from somewhere, the specified load paths are used.

- Specification: RTC module load path.
- Default:
  - C++: ./
  - Python: ./
  - Java: ./
- Example
```
 manager.modules.C++.load_paths: ./, /usr/share/openrtm-1.2/components/cxx
 manager.modules.Python.load_paths: ./, /usr/share/openrtm-1.2/components/python
 manager.modules.Python3.load_paths: ./, /usr/share/openrtm-1.2/components/python3
 manager.modules.Java.load_paths: ./, /usr/share/openrtm-1.2/components/java
```

<!-- Timer configuration -->

## Timer-Related Settings

### timer.enable

Enables/disables the timer function. If the timer is disabled, functions using the timer, such as periodic checking and re-registration with the name server, are disabled.

- Specification: **YES** or **NO**
- Default value: YES
- Example:
```
 timer.enable: YES
```

### timer.tick

Specifies timer precision.

- Specification: Specify timer precision in [s].
- Default value: 0.1 [s], (= 100 ms)
- Example:
```
 timer.tick: 1.0
```

## Execution Context Options

### exec_cxt.periodic.type

Default execution context type.
By default, the following execution contexts can be specified.

- PeridicExecutionContext: Default EC. This is the most common EC and is used if no EC is specified.
- ExtTrigExecutionContext:   EC driven by an external trigger. Built in by default.
- OpenHRPExecutionContext:  EC driven in parallel by an external trigger. Built in by default. Used with OpenHRP3.
- SimulatorExecutionContext: EC driven in parallel by an external trigger. Built in by default. Used with Choreonoid.
- RTPreemptEC: (Soft) real-time execution context. Used with the Linux RT-preemptive kernel.

- Specification: Default execution context name
- Default value: PeriodicExecutionContext
- Example:
```
 exec_cxt.periodic.type: PeriodicExecutionContext
 exec_cxt.periodic.type: ArtExecutionContext
```

### exec_cxt.periodic.rate

Default execution context cycle. This option specifies the EC cycle for the entire system. If the RTC does not explicitly specify the EC cycle, this cycle is used.

- Specification: Specify the default execution context cycle in [Hz]
- Default value: 1000
- Example:
```
 exec_cxt.periodic.rate: 100
```

### exec_cxt.sync_transition
### exec_cxt.sync_activation
### exec_cxt.sync_deactivation
### exec_cxt.sync_reset

The state of an RTC transitions through activation, deactivation, and reset. Some execution contexts execute the main logic in a different thread. If these flags are set to YES, activation, deactivation, and reset are executed synchronously. In other words, when these flags are YES, it is guaranteed that the activation/deactivation/reset operation call returns after the state transition is complete.

"sync_transition" sets the synchronous transition flag collectively for all other synchronous transition flags (sync_activation / deactivation / resetting).

- Setting: YES or NO
- Default: YES (default setting recommended)
- Example:
```
 exec_cxt.sync_transition: YES
 exec_cxt.sync_activation: YES
 exec_cxt.sync_deactivation: YES
 exec_cxt.sync_reset: YES
```

### exec_cxt.transition_timeout
### exec_cxt.activation_timeout
### exec_cxt.deactivation_timeout
### exec_cxt.reset_timeout

Timeout specification during synchronous transitions.
When the synchronous transition flag is set to YES, the following timeout settings become valid. If the "timeout_transition" option is set, the timeout values for activation/deactivation/reset are set collectively.

- Setting: Read/Write, seconds [s]
- Default: 0.5 [s]
- Example:
```
 exec_cxt.transition_timeout: 0.5
 exec_cxt.activation_timeout: 0.5
 exec_cxt.deactivation_timeout: 0.5
 exec_cxt.reset_timeout: 0.5
```

## SDO Service Options

### sdo.service.provider.available_services

This parameter contains the list of currently available SDO services (providers).

- Setting: Read-only, `<sdo service0>`, `<sdo service1>`, ... 
- Default: None
- Example:
```
 sdo.service.provider.available_services: <利用可能なSDOサービス（プロバイダ）のリスト>
```

### sdo.service.provider.enabled_services

This option specifies the SDO services (providers) to enable.
Specify a specific service by service type name, or specify "ALL" to enable all.

- Setting: Read/Write, `<sdo service0>`, `<sdo service1>`, ... or ALL
- Default: ALL
- Example:
```
 sdo.service.provider.enabled_services: <有効にするSDOサービスのリスト>
```

### sdo.service.provider.providing_services

This option contains the SDO services (providers) that are currently instantiated and provided.

- Setting: Read-only, `<sdo service0>`, `<sdo service1>`, ... 
- Default: None
- Example:
```
 sdo.service.provider.enabled_services: <現在インスタンス化されているDOサービスのリスト>
```

### sdo.service.consumer.available_services

This parameter contains the list of currently available SDO services (consumers).

- Setting: Read-only, `<sdo service0>`, `<sdo service1>`, ... 
- Default: None
- Example:
```
 sdo.service.consumer.available_services: <利用可能なSDOサービス（コンシューマ）のリスト>
```


### sdo.service.consumer.enabled_services

This option specifies the SDO services (consumers) to use.
Specify a specific service by service type name, or specify "ALL" to enable all.

- Setting: Read/Write, `<sdo service0>`, `<sdo service1>`, ... or ALL
- Default: ALL
- Example:
```
 sdo.service.consumer.enabled_services: <有効にするSDOサービスのリスト>
```


## Local Service Options

### manager.local_service.modules

Loads local service modules.
A local service mechanism is provided to provide user-defined services to RTCs within the same process.
Components can obtain and use local services from the manager.
For example, this mechanism can be used to access common resources among multiple RTCs.

Local service modules often need to be initialized before components are loaded or instantiated.
Therefore, local service modules must be specified with this option and loaded and initialized in advance.

- Setting: Read/Write, module load path
- Default: None
- Example:
manager.local_service.modules: IEEE1394CameraService.so

### manager.local_service.enabled_services

Specifies the local services to enable. By default, all local services are set to be activated and available. This option specifies particular local services to enable.

- Setting: Read/Write, local service name to enable
- Default: None
- Example:
manager.local_service.enabled_services: IEEE1394CameraService


## Port Settings


Port settings can be configured by specifying the item name after the following strings: **port.inport.dataport**, **port.{port type}.{port name}**, and **{category name}.{instance name}.port.inport.{port name}.{setting item}**.
If the same setting is specified in the connector profile at connection time, the connector profile setting overrides it, so the rtc.conf setting becomes invalid.

```
 port.{ポート型}.dataport.{設定項目}: {設定値}
 port.{ポート型}.{ポート名}.{設定項目}: {設定値}
 {カテゴリ名}.{インスタンス名}.port.inport.{ポート名}.{設定項目}: {設定値}
```

### allow_dup_connection
Prevents multiple connectors from being created between two ports.
If set to NO (not allowed), when port A and port B are connected, trying to connect port A and port B again by executing the connect function returns PRECONDITION_NOT_MET and the connection fails.

- Setting: Specifies whether multiple connectors are allowed or not allowed
- Default: NO
- Example:
```
 port.inport.in.allow_dup_connection: NO
```

### fan_in
Specifies the maximum number of connectors for an InPort. For example, if this is set to 100, when the number of ports connected to InPort A becomes 100 or more, executing the connect function returns PRECONDITION_NOT_MET and the connection fails.

- Setting: Sets the maximum number of connectors for an InPort
- Default: 100
- Example:
```
 port.inport.in.fan_in: 100
```


### fan_out
Specifies the maximum number of connectors for an OutPort. For example, if this is set to 100, when the number of ports connected to OutPort A becomes 100 or more, executing the connect function returns PRECONDITION_NOT_MET and the connection fails.

- Setting: Sets the maximum number of connectors for an OutPort
- Default: 100
- Example:
```
 port.outport.out.fan_out: 100
```


### buffer.length
Specifies the buffer size of the ring buffer for InPort and OutPort. For OutPort, this is valid when the subscription type is New or Periodic. For InPort, it is always valid.

- Setting: Sets the buffer size
- Default: 8
- Example:
```
 port.inport.in.buffer.length: 8
```


### buffer.write.full_policy
Specifies the policy when overwriting the ring buffer of InPort and OutPort. For OutPort, this is valid when the subscription type is New or Periodic. For InPort, it is always valid.

- Setting: Policy when overwriting
- Default: overwrite
- Example:
```
 port.inport.in.buffer.write.full_policy: block
 port.inport.in.buffer.write.full_policy: do_nothing
```

### buffer.read.empty_policy
Specifies the policy when reading from the ring buffer of InPort and OutPort. For OutPort, this is valid when the subscription type is New or Periodic. For InPort, it is always valid.

- Setting: Policy when reading
- Default: readback
- Example:
```
 port.inport.in.buffer.read.empty_policy: block
 port.inport.in.buffer.read.empty_policy: do_nothing
```
