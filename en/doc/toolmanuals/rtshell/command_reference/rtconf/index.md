---
layout: page
title: rtconf
---

<!-- Title: rtconf -->

## Format
```
 rtconf PATH [OPTION...] [list|set|get|act] [ARGS]
```

## Overview
Displays and sets configuration parameters and configuration sets. If list|set|get|act is not specified, list is assumed to be specified.

- **list**
  - The list command displays configuration sets and parameters. It does not display hidden configuration sets (configuration sets whose set names start with `__`).
- **set PARAMETER_NAME VALUE**
  - Sets the value of a configuration parameter. Specify the parameter name and the new value. If the --set (-s) option is not specified, the parameter of the currently active configuration set is set.
- **get PARAMETER_NAME**
  - Displays the value of a parameter. Specify the parameter name. If the --set (-s) option is not specified, the value of the parameter in the currently active configuration set is displayed.
- **act**
  - Activates the configuration set specified with --set=SET_NAME (-s SET_NAME).

### Options (OPTION)
```
 -a, --all　　　Do not ignore hidden configuration sets. Specify this option if you want to edit hidden configuration sets.
 -l　　　　　　 Displays detailed information.
 -s <set name>, --set=SET_NAME
 　　　　　　Selects a configuration set. If not specified, the currently active set is used.
 --version	　　Displays the program version number.
 -h, --help　　Displays help.
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

## Examples
- Displays the configuration sets of ConfigSample0.rtc.
```
 $ rtconf /localhost/ConfigSample0.rtc list
 +default*
 +mode0
 +mode1
```

- Displays the configuration sets and parameters of ConfigSample0.rtc.
```
 $ rtconf /localhost/ConfigSample0.rtc -l list
  -default*
  double_param0  0.99
  double_param1  -0.99
```

- Displays the sets of ConfigSample0.rtc, including hidden configuration sets.
```
 $ rtconf /localhost/ConfigSample0.rtc -a list
 +__constraints__
 +__widget__
 +default*
 +mode0
 +mode1
```

- Displays the parameters of the default set of ConfigSample0.rtc.
```
 $ rtconf /localhost/ConfigSample0.rtc -l -s default list
 -__constraints__
  double_param0  0<=x<=100
  double_param1
  ...
```

- Sets the value of the int_param0 parameter in the currently active configuration set to 42.
```
 $ rtconf /localhost/ConfigSample0.rtc set int_param0 42
```

- Sets int_param0 in the configuration set named mode0 to 42.
```
 $ rtconf /localhost/ConfigSample0.rtc -s mode0 set int_param0 42
```

- Displays the value of the int_param0 parameter in the currently active configuration set.
```
 $ rtconf /localhost/ConfigSample0.rtc get int_param0
 0
```

- Displays the value of the int_param0 parameter in the configuration set named mode0.
```
 $ rtconf /localhost/ConfigSample0.rtc -s mode0 get int_param0
 12345
```

- Sets the configuration set to the configuration set named mode1.
```
 $ rtconf /localhost/ConfigSample0.rtc act mode1
```

- Sets the configuration set to the set named __widget__.
```
 $ rtconf /localhost/ConfigSample0.rtc -a act __widget__
```
