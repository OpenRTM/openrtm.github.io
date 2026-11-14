---
layout: page
title: rtcomp
---
<!-- Title: rtcomp -->

## Format
```
rtcomp [OPTION...] MANAGER
```
## Overview
Configures multiple running components as a single composite component on the same manager, and exports the selected ports externally. It is also possible to select an Execution context. Components whose ports are exported are automatically included in the configuration.

## Options
```
 -c COMPONENT_NAME, --comp=COMPONENT_NAME
 　　　　　　Specifies a component to include in the composite component. This option can be specified multiple times.
 -n NAME, --name=NAME
 　　　　　　Specifies the instance name of the composite component (the name of the generated component). [Default: CompositeRTC]
 -o OPTIONS, --options=OPTIONS
 　　　　　　Additional options when creating the component. Start with "&".
 -p PORTS, --port=PORTS
 　　　　　　Specifies ports to export (make public externally). Components whose ports are exported are automatically included in the composite component (same as -c).
 -t TYPE, --type=TYPE
 　　　　　　Specifies the Execution context type. [Default: PeriodicECSharedComposite]
 --version　　Displays the program version number and exits.
 -h, --help　　Displays help and exits.
 -v, --verbose Outputs more detailed information.
```

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
- **RTCTREE_ORB_ARGS**
  - Variables passed when creating the ORB. Separate them with semicolons. This is not required.
- **RTCTREE_NAMESERVERS**
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

## Example
- Creates a composite component with Motor0.rtc and Controller0.rtc by exporting the in port of Controller0.rtc and the out port of Motor0.rtc. The instance name of the composite component is MotorUnit.
```
 $ rtcomp /localhost/manager.mgr -c /localhost/Motor0.rtc -p /localhost/Controller0.rtc:in -p /localhost/Motor0.rtc:out -n MotorUnit
```

