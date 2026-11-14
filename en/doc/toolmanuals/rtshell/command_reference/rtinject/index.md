---
layout: page
title: rtinject
---
<!-- Tilte: rtinject -->

## Format
```
rtinject [OPTIONS ...] PATH:PORT [PATH:PORT ...]
```

## Overview
Sends values to one or more ports. By default, it sends only once. It can also send multiple times or periodically.

Creates a default connection to the target port.

## Options (OPTION)
```
 -c CONST, --const=CONST
 　　　　　　Specifies data in Python format. On POSIX systems, enclose the data description string with "'".
 　　　　　　On Windows, enclose the data description string with """. If this option is not specified,
 　　　　　　data from standard input is treated as the data description string. The {time}
 　　　　　　notation in the data description string is treated as meaning the current time.
 -m MODULES, --mod=MODULES
 　　　　　　Specifies Python modules to import. If a module required for the value is not automatically loaded,
 　　　　　　specify it with this option. The module and its __POA module are also imported.
 -n NUMBER, --number=NUMBER
 　　　　　　Specifies how many times to send data. If -1 is set, data continues to be sent until forcibly stopped.
 -p PATHS, --path=PATHS
 　　　　　　Module search path. It is added to Python's PYTHONPATH variable.
 -r RATE, --rate=RATE
 　　　　　　Specifies the frequency. The unit is times/sec.
 -t TIMEOUT, --timeout=TIMEOUT
 　　　　　　Specifies the timeout time (time until command execution is stopped) in seconds. This option
 　　　　　　cannot be used together with --number.
 --version　　 Displays the program version number.
 -h, --help　　Displays help.
 -v, --verbose Outputs verbose information.
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
- Sends a value from stdin to the in port of ConsoleOut0.rtc.
```
 $ rtinject /localhost/ConsoleOut0.rtc:in
```

- Sends 42 and the current time as a timestamp to the in port of consoleout0.rtc. Use "'" to enclose the data specification in Python format. (On Windows, use `"`.
)
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -c 'RTC.TimedLong({time}, 42)'
```

- Sends 42 to the in port of ConsoleOut0.rtc with the timestamp set to 1 second.
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -c 'RTC.TimedLong(RTC.Time(1, 0), 42)'
```

- Sends the value from stdin five times to the in port of ConsoleOut0.rtc.
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -n 5
```

- Sends 42 to the in port of consoleout0.rtc five times based on the current time.
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -n 5 -c 'RTC.TimedLong({time}, 42)'
```

- Sends 42 and the current time to the in port of consoleout0.rtc at a frequency of 10 times/sec.
```
 $ rtinject /localhost/ConsoleOut0.rtc:in -t 5 -r 10 -c 'RTC.TimedLong({time}, 42)'
```

- Sends MyData.MyVal(84) to the in port of MyComp0.rtc. The class is specified in a module that exists in Python's search path (PYTHONPATH). That module was generated from an OMG IDL file.
```
 $ rtinject /localhost/MyComp0.rtc:in -c 'MyData.MyVal(84)'
```

- Sends MyData.MyVal(84) to the in port of MyComp0.rtc. The class is specified in a module that does not exist in Python's search path (PYTHONPATH). The module path is specified with **-p**.
```
 $ rtinject /localhost/MyComp0.rtc:in -p /usr/local/mods -c 'MyData.MyVal(84)'
```

- Sends MyData.MyVal(84) to the in port of MyComp0.rtc. The class specifies a module named mymod that exists in Python's search path (PYTHONPATH).
```
 $ rtinject /localhost/MyComp0.rtc:in -p /usr/local/mods -m mymod -c 'MyData.MyVal(84)'
```
