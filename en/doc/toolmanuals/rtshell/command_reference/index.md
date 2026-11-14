---
layout: page
title: rtshell command reference
---

<!-- Title: rtshellコマンド・リファレンス -->
## Overview
Many of the commands allow components and managers running on a name server to be treated like a file system. You can enter directories, read components as if using cat, activate them, and connect ports. Other commands are used in relation to RTSProfile files for managing RT systems.

## Commands
<table class="table-alt">
  <tr>
    <td>Command Name</td>
    <td>Overview</td>
  </tr>
  <tr>
    <td><a href="./rtact">rtact</a></td>
    <td>Activates an RT Component.</td>
  </tr>
  <tr>
    <td><a href="./rtcat">rtcat</a></td>
    <td>Displays metadata of an RT Component.</td>
  </tr>
  <tr>
    <td><a href="./rtcheck">rtcheck</a></td>
    <td>Compares a running RT system with loaded RTSProfile data.</td>
  </tr>
  <tr>
    <td><a href="./rtcomp">rtcomp</a></td>
    <td>Creates a composite component.</td>
  </tr>
  <tr>
    <td><a href="./rtcon">rtcon</a></td>
    <td>Connects ports.</td>
  </tr>
  <tr>
    <td><a href="./rtconf">rtconf</a></td>
    <td>Queries/sets component configurations.</td>
  </tr>
  <tr>
    <td><a href="./rtcryo">rtcryo</a></td>
    <td>Outputs RTSProfile data of a running RT system to a file or stdout.</td>
  </tr>
  <tr>
    <td><a href="./rtcwd">rtcwd</a></td>
    <td>Changes the current working directory.</td>
  </tr>
  <tr>
    <td><a href="./rtdeact">rtdeact</a></td>
    <td>Deactivates a component.</td>
  </tr>
  <tr>
    <td><a href="./rtdel">rtdel</a></td>
    <td>Deletes an object from the name server.</td>
  </tr>
  <tr>
    <td><a href="./rtdis">rtdis</a></td>
    <td>Disconnects ports.</td>
  </tr>
  <tr>
    <td><a href="./rtdoc">rtdoc</a></td>
    <td>Displays RT Component documentation.</td>
  </tr>
  <tr>
    <td><a href="./rtexit">rtexit</a></td>
    <td>Stops an RT Component.</td>
  </tr>
  <tr>
    <td><a href="./rtfind">rtfind</a></td>
    <td>Finds running RT Components, managers, and other objects.</td>
  </tr>
  <tr>
    <td><a href="./rtinject">rtinject</a></td>
    <td>Sends data to a port.</td>
  </tr>
  <tr>
    <td><a href="./rtlog">rtlog</a></td>
    <td>Saves data sent by a port to a log and replays it.</td>
  </tr>
  <tr>
    <td><a href="./rtls">rtls</a></td>
    <td>Lists objects in the current working directory.</td>
  </tr>
  <tr>
    <td><a href="./rtmgr">rtmgr</a></td>
    <td>Manages RT Components with a manager.</td>
  </tr>
  <tr>
    <td><a href="./rtprint">rtprint</a></td>
    <td>Displays data sent by a port on the terminal.</td>
  </tr>
  <tr>
    <td><a href="./rtpwd">rtpwd</a></td>
    <td>Displays the current working directory.</td>
  </tr>
  <tr>
    <td><a href="./rtreset">rtreset</a></td>
    <td>Resets an RT Component.</td>
  </tr>
  <tr>
    <td><a href="./rtresurrect">rtresurrect</a></td>
    <td>Restores RT system connections using RTSProfile data.</td>
  </tr>
  <tr>
    <td><a href="./rtstart">rtstart</a></td>
    <td>Starts an RT system using RTSProfille data.</td>
  </tr>
  <tr>
    <td><a href="./rtstodot">rtstodot</a></td>
    <td>Displays a running RT system as a graph.</td>
  </tr>
  <tr>
    <td><a href="./rtstop">rtstop</a></td>
    <td>Stops an RT system using RTSProfiel data.</td>
  </tr>
  <tr>
    <td><a href="./rtteardown">rtteardown</a></td>
    <td>Deletes an RT system using RTSProfile data.</td>
  </tr>
</table>


## RTC Tree

All commands run on the RTC tree. The RTC tree is a mechanism that allows contexts, components, managers, and other objects on a name server to be treated like a file system. It can be handled in the same way as a normal file system.

Name servers are treated as subdirectories directly under the root directory "/". Files and subdirectories exist under them. Subdirectories correspond to naming contexts on the name server. Files correspond to components and managers.

There are two ways to provide the name servers used to construct the tree. One is a path relative to the name server passed to the rtshell command. This is a path relative to the current working directory. If an absolute path is specified, the directory directly under the root is the host name where the name server exists (it may also be an IP address).

The other is the RTCTREE_NAMESERVERS environment variable. You can also pass a list of name server host addresses separated by semicolons. If you specify hosts that have multiple name servers, each host will appear directly under the root.

## Shell Completion
If you use the Bash shell, the completion script included with rtshell can make rtshell easier to use by enabling command input completion. The script is installed in /usr/local/lib/pythonX.Y/dist-packages/rtshell. Load it with the following command:
```
 $ source /usr/local/lib/pythonX.Y/dist-packages/rtshell/bash_completion
```

Also, if you add the above line to a file named `/.bashrc`, it will be loaded automatically when the terminal starts.`

### Completion Examples:
```
 $ rtcwd /localhost/[TAB]
 $ rtcwd /localhost/ubuntu.host_cxt/
```

```
 $ rtcwd /localhost/ubuntu.host_cxt/[TAB][TAB]
 /localhost/ubuntu.host_cxt/ConfigSample0.rtc
 /localhost/ubuntu.host_cxt/ConsoleIn0.rtc
 /localhost/ubuntu.host_cxt/ConsoleOut0.rtc
 /localhost/ubuntu.host_cxt/manager.mgr/
```

```
 $ rtcwd localhost/ubuntu.host_cxt/[ENTER]
```

```
 $ rtconf ConfigSample0.rtc set [TAB]
 double_param0  int_param0     str_param0     vector_param0  
 double_param1  int_param1     str_param1
```

```
 $ rtcon ConsoleIn0.rtc:[TAB]
 $ rtcon ConsoleIn0.rtc:out
```


## System Requirements
- rtshell requires rtctree. If it is not installed, the commands will not start.
- Commands that use RTSProfile data require rtsprofile. If it is not installed, these commands will not start.
- rtshell requires Python 3.7/3.6/2.7.
- rtinject, rtlog, and rtprint require OpenRTM-python.

## Paths
rtshell indicates objects in the RTC tree using paths. Name servers and name contexts are specified as directory names, and managers and RT Components are specified as file names. Paths passed to commands are specified based on the current working directory of rtshell (for relative paths). The current working directory of rtshell is stored in an environment variable named RTCSH_CWD, and can be changed with the rtcwd command. (At present, the rtcwd command does not work in Linux environments.)

Available paths depend on the name servers referenced when commands are executed. The host names where name servers are running can be specified with the RTCTREE_NAMESERVERS environment variable. You can also specify the host where a name server is running directly as a path under the root, such as /<host name>/....

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

<hr>

- [rtact](./rtact)
- [rtcat](./rtcat)
- [rtcheck](./rtcheck)
- [rtcomp](./rtcomp)
- [rtcon](./rtcon)
- [rtconf](./rtconf)
- [rtcryo](./rtcryo)
- [rtcwd](./rtcwd)
- [rtdeact](./rtdeact)
- [rtdel](./rtdel)
- [rtdis](./rtdis)
- [rtdoc](./rtdoc)
- [rtexit](./rtexit)
- [rtfind](./rtfind)
- [rtinject](./rtinject)
- [rtlog](./rtlog)
- [rtls](./rtls)
- [rtmgr](./rtmgr)
- [rtprint](./rtprint)
- [rtpwd](./rtpwd)
- [rtreset](./rtreset)
- [rtresurrect](./rtresurrect)
- [rtstart](./rtstart)
- [rtstodot](./rtstodot)
- [rtstop](./rtstop)
- [rtteardown](./rtteardown)

