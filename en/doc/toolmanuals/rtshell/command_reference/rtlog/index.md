---
layout: page
title: rtlog
---

<!-- Title: rtlog -->

## Format
```
rtlog [OPTION ...] PATH:PORT [PATH:PORT ...]
```

## Overview
Saves data sent by a component through a data port to a log file, or sends data recorded in a log file to a component (playback). Recording is also possible for multiple ports. You can also play back a log file and send it to a component in order to reproduce the output data of the logged component.

You can select a stream played back from multiple data streams in the log. For example, if data from multiple laser sensors is saved in a log, you can play back only one specific laser sensor data stream from among them. Playback can be performed not only from the beginning of the log, but also from partway through to partway through, and the playback rate can also be changed. You can also edit the timestamp of the output data.

The default is log recording. All ports specified by the command must be OutPorts. In playback mode, all ports must be InPorts, and the types accepted by the ports must match the types of the logged data.

Each port recorded in the log creates one data stream. During playback, each of these data streams can be sent to multiple InPorts. Data streams are distinguished by name. The name can be specified on the command line, but if it is not specified, a default name is automatically used.

Connections from the log tool to the target ports are created with default properties.

## Options
```
 -a, --absolute-times
 　　　　　　Timestamps from the log data are sent using the values as recorded.
 　　　　　　If not specified, timestamps are offset by the current time.
 -d, --display-info
 　　　　　　Displays log information and exits.
 -e END, --end=END
 　　　　　　Specifies the timestamp or index at which to stop recording or playback. For playback,
 　　　　　　specify a value between the first and last data in the recorded log.
 　　　　　　If -1 is specified, recording continues until forcibly terminated, or playback continues
 　　　　　　until the end of the log. If you want to specify an index, also specify --index.
 -f FILENAME, --filename=FILENAME
 　　　　　　Specifies the name of the log file. If not specified, the current time is used as the file name.
 　　　　　　This is required for playback.
 --path=PATHS	
 　　　　　　Specifies the module search path. It is added to Python's PYTHONPATH variable.
 -i, --index
 　　　　　　Treats the values specified with the --start and --end options as indexes instead of
 　　　　　　timestamps.
 -l LOGGER, --logger=LOGGER
 　　　　　　Selects the log type. The default is SimplePickle (simpkl). Text logs
 　　　　　　(text) can also be used. Text logs cannot be played back.
 -m MODULES, --mod=MODULES
 　　　　　　Specifies Python modules to import. If a module required to handle the data
 　　　　　　is not loaded automatically, specify it with this option.
 　　　　　　The module and its __POA module are also imported.
 -n, --ignore-times
 　　　　　　(Playback only) Ignores timestamps recorded in the log and plays back log data
 　　　　　　at a fixed period. To change the period, use --exec-rate.
 -p, --play　Enables playback mode.
 -r RATE, --rate=RATE
 　　　　　　(Playback only) Specifies the playback speed multiplier.
 -s START, --start=START
 　　　　　　(Playback only) Specifies the timestamp or index at which to start playback. It must be
 　　　　　　between the first and last data in the log. If specifying an index,
 　　　　　　also specify --index.
 -t TIMEOUT, --timeout=TIMEOU
 　　　　　　Specifies the timeout time for recording or playback. When using this option,
 　　　　　　--start and --end cannot be used.
 -x EXEC_RATE, --exec-rate=EXEC_RATE
 　　　　　　Specifies the component execution rate. The unit is hertz.
 --version　 Displays the program version number and exits.
 -h, --help　Displays help and exits.
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

This specifies that the name of the newly created port is stuff, and that the data is displayed on the terminal using a function (formatter) named a_printer. (The a_printer function must exist somewhere Python can use it. Normally, the user provides it in a module.) The created port is connected to the input port of comp0.rtc. This is also used to specify the stream name.

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
- Records data from the out port of the ConsoleIn0.rtc component to the file log.rtlog. The data stream is named numbers.
```
 $ rtlog -f log.rtlog /localhost/ConsoleIn0.rtc:out.numbers
```

- Plays back the data stream named numbers from the log file log.rtlog and sends it to the ConsoleOut0.rtc:in port.
```
 $ rtlog -f log.rtlog -p /localhost/ConsoleOut0.rtc:in.numbers
```

- Displays log information. This includes the log start time, end time, data streams, and other information.
```
 $ rtlog -f log.rtlog -d
```

- Records until the computer clock reaches "1292489690", then exits.
```
 $ rtlog -f log.rtlog -e 1292489690 /localhost/ConsoleIn0.rtc:out.numbers
```

- Records 10 data items, then exits.
```
 $ rtlog -f log.rtlog -e 10 -i /localhost/ConsoleIn0.rtc:out.numbers
```

- Records for 10 seconds, then exits.
```
 $ rtlog -f log.rtlog -t 10 /localhost/ConsoleIn0.rtc:out.numbers
```

- Starts playback from the timestamp "1292489690".
```
 $ rtlog -f log.rtlog -p -s 1292489690 /localhost/ConsoleOut0.rtc:in.numbers
```

- Plays back from the first data to the timestamp "1292489700".
```
 $ rtlog -f log.rtlog -p -e 1292489700 /localhost/ConsoleOut0.rtc:in.numbers
```

- Plays back from the timestamp "1292489690" to the timestamp "1292489700". (Approximately 10 seconds of data.)
```
 $ rtlog -f log.rtlog -p -s 1292489690 -e 1292489700 /localhost/ConsoleOut0.rtc:in.numbers
```

- Starts playback from the 5th data item.
```
 $ rtlog -f log.rtlog -p -s 5 -i /localhost/ConsoleOut0.rtc:in.numbers
```

- Plays back from the first data item to the 10th data item.
```
 $ rtlog -f log.rtlog -p -e 10 /localhost/ConsoleOut0.rtc:in.numbers
```

- Plays back from the 5th data item to the 10th data item.
```
 $ rtlog -f log.rtlog -p -s 5 -e 10 /localhost/ConsoleOut0.rtc:in.numbers
```

- Plays back 10 seconds of data from the beginning.
```
 $ rtlog -f log.rtlog -p -t 10 /localhost/ConsoleOut0.rtc:in.numbers
```

- Plays back the log at 5x speed.
```
 $ rtlog -f log.rtlog -p -r 5 /localhost/ConsoleOut0.rtc:in.numbers
```

- Plays back the log at 0.2x speed.
```
 $ rtlog -f log.rtlog -p -r 0.2 /localhost/ConsoleOut0.rtc:in.numbers
```

- Plays back one data item per second, and finally plays back 5 data items.
```
 $ rtlog -f log.rtlog -p -n 5 -x 1 /localhost/ConsoleOut0.rtc:in.numbers
```

- Records three data streams into one file. The stream names are sensor, ctrl, and motor.
```
 $ rtlog -f log.rtlog /localhost/Sensor0.rtc:out.sensor /localhost/Controller0.rtc:out.ctrl /localhost/Motor0.rtc:out.motor
```

- Plays back two data streams from one log and sends each to a different port.
```
 $ rtlog -f log.rtlog -p /localhost/Sensor0.rtc:in.motor /localhost/Motor0.rtc:in.ctrl
```

- Plays back two data streams from one log and sends them to the same port.
```
 $ rtlog -f log.rtlog -p /localhost/Controller0.rtc:in.sensor /localhost/Controller0.rtc:in.motor
```

- Plays back one data stream from the log and sends it to multiple ports.
```
 $ rtlog -f log.rtlog -p /localhost/Sensor0.rtc:in.motor /localhost/Controller0.rtc:in.motor
```
