---
layout: page
title: rtfind
---

<!-- Title: rtfind -->

## Format
```
rtfind SEARCH_PATH [OPTION ...]
```

## Overview
Searches for components, managers, and other objects on name servers in the RTC tree. Conditions can also be specified.

## Options (OPTION)
```
 -i INAME, --iname=INAME
 　　　　　　Searches by name without distinguishing between lowercase and uppercase letters. This can be specified multiple times.
 -m MAX_DEPTH, --maxdepth=MAX_DEPTH
 　　　　　　Limits the search depth. By default, the entire tree is searched.
 -n NAME, --name=NAME
 　　　　　　Searches by name, distinguishing between lowercase and uppercase letters. This can be specified multiple times.
 -t TYPE, --type=TYPE
 　　　　　　Specifies the object type. Specify it using characters. The following can be specified.
 　　　　　　c: Component
 　　　　　　d: Directory
 　　　　　　m: Manager
 　　　　　　n: Name server
 　　　　　　z: Zombie
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
- Searches for all components in the RTC tree. The search starts from the root directory.
```
 $ rtfind / -t c
```

- Searches for all components and managers under the current working directory.
```
 $ rtfind . -t cm
```

- Searches for components whose names start with Conso under the current working directory.
```
 $ rtfind . -n 'Conso*' -type c
```

- Searches for components under the current working directory whose names start with console, end with .rtc, and have only one character in between. Lowercase and uppercase letters are not distinguished.
```
 $ rtfind . -i 'console?.rtc' -type c
```

- (POSIX only) Activates all components in the current working directory.
```
 $ for c in `rtfind . -type c -m 1`; do rtact ${c}; done
```
