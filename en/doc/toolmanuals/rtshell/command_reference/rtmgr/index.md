---
layout: page
title: rtmgr
---

<!-- Title: rtmgr -->

## Format
```
rtmgr [OPTION ...] PATH
```

## Overview
Controls the manager by adding/deleting shared libraries (shared modules) and components. It instantiates components from shared libraries (modules) loaded into the manager.

Use rtconf to configure the manager. Manager information can be displayed with rtcat.

If multiple commands are executed, they are executed in the order entered on the command line.

## Options (OPTION)
```
 -c MOD_NAME, -create=MOD_NAME
 　　　　　　　Creates a component instance from a loaded module. Properties can be added to the module name.
 　　　　　　　Specify properties by prefixing them with "?”.
 -d INSTANCE_NAME, --delete=INSTANCE_NAME
 　　　　　　　Terminates and deletes a component instance.
 -l MOD_PATH, --load=MOD_PATH
 　　　　　　　Loads a module into the manager. Specify the initialization function after the module path, separated by ":".
 -u MOD_PATH_U, --unload=MOD_PATH_U
 　　　　　　　Deletes a module from the manager.
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


Return Values
Returns zero on success. Returns a non-zero value on failure.

Debug information and errors are output to stderr.

## Examples
```
 $ rtmgr /localhost/manager.mgr -l /usr/local/lib/mycomp.so:mycomp_init
```
Loads a module named mycomp.so into the manager.

```
 $ rtmgr /localhost/manager.mgr -c mycomp
```
Creates a component instance from a module named mycomp.

```
 $ rtmgr /localhost/manager.mgr -d MyComp0
```
Terminates and deletes the component named MyComp0 running in the manager.

```
 $ rtmgr /localhost/manager.mgr -u /usr/local/lib/mycomp.so
```
Deletes the module named mycomp.so from the manager.

```
 $ rtmgr /localhost/manager.mgr -l /usr/local/lib/mycomp.so:mycomp_init  -c mycomp
```
Loads a module named mycomp.so into the manager and then creates a component instance.

