---
layout: page
title: rtcon
---

<!-- Title: rtcon -->

## Format
```
 rtcon [OPTION ...] PATH PATH [PATH]
```

## Overview
Connects two or more data ports or service ports.

## Options
```
 -i ID, --id=ID
 　　　　　　　Specifies the connection (connector) ID.
 -n NAME, --name=NAME
 　　　　　　　Specifies the connection name.
 -p PROPERTY=PROPERTY_VALUE, --property PROPERTY=PROPERTY_VALUE
 　　　　　　　Specifies a connection property.
 --version　　 Displays the program version number.
 -h, --help　　Displays help.
 -v, --verbose Outputs more detailed information. 
```

The following properties are valid for data ports:
```
 dataport.data_type
 dataport.dataflow_type
 dataport.interface_type
 dateport.subscription_type
```

The following properties are valid for service ports:
```
 port.port_type
```

Depending on the version of OpenRTM, other properties may also be valid.

## Paths
rtshell indicates objects in the RTC tree using paths. Name servers and name contexts are specified as directory names, and managers and RT Components are specified as file names. Paths passed to commands are specified based on the current working directory of rtshell (for relative paths). The current working directory of rtshell is stored in an environment variable named RTCSH_CWD, and can be changed with the rtcwd command. (At present, the rtcwd command does not work in Linux environments.)

Available paths depend on the name servers referenced when commands are executed. The host name where a name server is running can be specified with the RTCTREE_NAMESERVERS environment variable. You can also specify the host where a name server is running directly as a path under the root, such as /<host name>/....

For example, /localhost/comp0.rtc indicates an RT Component named comp0.rtc registered with the name server on localhost. /localhost/manager/comp0.rtc indicates an RT Component named comp0.rtc registered in a directory named manager under the name server on localhost. ./comp0.rtc indicates an RT Component named comp0.rtc in the current working directory.

To indicate a port of an RT Component, specify it after the path separated by a colon (":"). For example, /localhost/comp0.rtc:data means the port named data of the RT Component named comp0.rtc.

Some commands can create new ports. In this case, you can add them to the path with options. The available options are the name of the created port and the formatter. Specify them as follows:

```
 <path>:<port>.<new_port_name>#<formatter>
```

### Example:
```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff#a_printer
```

This specifies that the name of the newly created port is stuff, and that the data is displayed on the terminal using a function (formatter) named a_printer. (The a_printer function must exist somewhere Python can use it. Normally, the user provides it in a module.) The created port is connected to the input port of comp0.rtc.

The `<new_port_name>` part is not required. If it is not specified, do not specify "." either. Example:

```
 /localhost/blurg.host_cxt/comp0.rtc:input#a_printer
```

The `<formatter>` part is not required. If it is not written, do not specify "." either. Example:

```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff
```

## Environment Variables
- ** RTCTREE_ORB_ARGS**
  - Variables passed when creating the ORB. Separate them with semicolons. This is not required.
-  **RTCTREE_NAMESERVERS**
  - Addresses of name servers referenced when creating the RTC tree. Separate addresses with semicolons. The listed addresses are added to the RTC tree and can be referenced by rtshell. This is not required because they can also be specified as directory names under the root in paths.
- **RTSH_CWD**
  - The current working directory of rtshell. rtshell sets it automatically. Do not set it manually.

In typical use, the only variable that users set is RTCTREE_NAMESERVERS. It is convenient to set frequently used name servers. For example, in the Bash shell, the following command allows rtshell to reference name servers on localhost, port 192.168.0.1:65346, and host example.com.

```
 $ export RTCTREE_NAMESERVERS=localhost;192.168.0.1:65346;example.com
```

## Return Values
Returns zero on success. Returns a non-zero value on failure.

Debug information and errors are output to stderr.

## Examples
- Connects the out port of ConsoleIn0.rtc to the in port of ConsoleOut0.rtc using the default properties.
```
 $ rtcon /localhost/ConsoleIn0.rtc:out /localhost/ConsoleOut0.rtc:in
```

- Connects the out port of Motor0.rtc to the in port of Sensor0.rtc using a Pull-type connection.
```
 $ rtcon Motor0.rtc:out Sensor0.rtc:in --property dataport.dataflow_type=pull
```

- Connects the out port of Motor0.rtc to the in port of Sensor0.rtc. The connection name is motor_data and the ID is con1.
```
 $ rtcon Motor0.rtc:out Sensor0.rtc:in -i con1 -n motor_data
```

- Connects the out port of ConsoleIn0.rtc to the in port of ConsoleOut0.rtc and the in port of ConsoleOut1.rtc using the default properties.
```
 $ rtcon ConsoleIn0.rtc:out ConsoleOut0.rtc:in ConsoleOut1.rtc:in
```

