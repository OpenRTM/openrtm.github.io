---
layout: page
title: rtprint
---

<!-- Title: rtprint -->

## Format
```
rtprint [OPTION ...] PATH:PORT [PATH:PORT ...]
```

## Overview
Displays data sent by an OutPort to standard output.

By default, it displays received values until forcibly stopped. You can specify the number of data items to receive, the frequency at which to read them, and the amount of time until receiving is stopped. If the number of data items is specified but that number of data items is not ready at that point, it waits until they are ready and displays that number of times.

To display data that cannot be displayed using Python's native functions, you need to use a formatter function. The user can define this function. The formatter function takes one input argument (the data to be displayed), for example as shown below.

```
 def rawpy(data):
     return data.__repr__()
```

The connection to the port is made with settings compatible with the default settings of that port.

## Options (OPTION)
```
 -m MODULES, --mod=MODULES
 　　　　　　　Specifies Python modules that need to be imported. If a module required to display the data of the port to connect to
 　　　　　　　has not been loaded, specify it with this option. The module and its __POA
 　　　　　　　module are also imported.
 -n NUMBER, --number=NUMBER
 　　　　　　　Number of times to read.
 -p PATHS, --path=PATHS
 　　　　　　　Module search path. It is added to Python's PYTHONPATH variable.
 -r RATE, --rate=RATE
 　　　　　　　Read frequency (times/sec).
 -t TIMEOUT, --timeout=TIMEOUT
 　　　　　　　Time until reading stops. When using this option, --number cannot be used.
 --version　　 Displays the program version number.
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
- Displays output data from the out port of ConsoleIn0.rtc.
```
 $ rtprint /localhost/ConsoleIn0.rtc:out
```

- Displays 5 data items from the out port of ConsoleIn0.rtc.
```
 $ rtprint /localhost/ConsoleIn0.rtc:out -n 5
```

- Displays data from the out port of ConsoleIn0.rtc for 5 seconds.
```
 $ rtprint /localhost/ConsoleIn0.rtc:out -t 5
```

- Reads and displays data from the out port of ConsoleIn0.rtc for 5 seconds at a frequency of 10 times per second.
```
 $ rtprint /localhost/ConsoleIn0.rtc:out -t 5 -r 10
```

- Sends output data from the out port of ConsoleIn0.rtc to the my_formatter function in the printers module and displays the result.
```
 $ rtprint /localhost/ConsoleIn0.rtc:out#printers.my_formatter
```

