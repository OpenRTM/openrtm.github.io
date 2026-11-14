---
layout: page
title: rtstart
---

<!-- Title: rtstart -->

## Format
```
rtstart [OPTION ...] [RTSPROFILE_FILE]
```

## Overview
Starts an RT system by activating all components based on the information in the specified RTSProfile file. Components are activated in the order specified in the RTSProfile file. Components that are not marked as "required" in the RTSProfile are ignored.

If no file name is specified, RTSProfile-format information is read from stdin.

## Options (OPTION)
```
 --dry-run　　 Displays what will be executed. (The system is not actually started.)
 -x, --xml　　 Uses XML format.
 -y, --yaml　　Uses YAML format.
 --version　　 Displays the program version number and exits.
 -h, --help　　Displays help and exits.
 -v, --verbose Outputs more detailed information.
```

## Execution Sequence of State Changes
In an RTSProfile file, it is possible to specify the order in which components in an RT system are started/stopped. When there are dependencies between components (for example, when one component must be started before another component starts), that order can be specified.

rtstart and rtstop use this information. In practice, rtstart uses the information contained in the Activation block, and rtstop uses the information described in the Deactivation block. Based on the information described here, component activation/deactivation processing continues until all processing is completed or an error occurs.

If the --dry-run option is specified, the command displays what processing would be performed if this option were not specified. The actual processing is not performed. The output is as follows.
```
 {1} Activate /localhost/ConfigSample0.rtc in execution context 0 (Required) 
 {2} [Order 1] Activate /localhost/Motor0.rtc in execution context 0 (Required)
 {4} [Order 3/Wait 5000ms] Activate /localhost/Controller0.rtc in execution context 0 (Required)
 {3} [Order 2/Sync to Motor0, Order 5/Sync to Controller0] Activate /localhost/Sensor0.rtc in execution context 0 (Required)
 {5} [Order 4/After ConfigSample0's action] Activate /localhost/ConsoleIn0.rtc in execution context 0 (Required)
```

The number in braces at the beginning of each line is the *action ID*. These are also displayed during execution, making it easy to identify actions.
The part enclosed in square brackets that follows indicates the conditions required to execute the following action. Specific words used in it have the following meanings:

- **Order**
  - Manages the order. It can be set with the rts: sequence value of the condition in RTSProfile. If there are no other preconditions, actions are performed according to this order.
- **Wait**
  - The action is executed after the specified time has elapsed.
- **Sync**
  - Waits until the specified component reaches the target state, and then executes the specified action.
- **After**
  - Similar to Sync. The difference is that it waits until an action is performed on another specified component. In other words, the action is executed if the action is performed on that component, even before the specified other component reaches the target state.
The remaining part of the line is the description of the action.

## Return Values
Returns zero on success. Returns a non-zero value on failure.

Debug information and errors are output to stderr.

# Examples
- Starts the RT system based on the information in a file named sys.rtsys.
```
 $ rtstart sys.rtsys
```

- Displays what processing will be performed to start the RT system based on the information in a file named sys.rtsys. (The actual startup is not performed.)
```
 $ rtstart sys.rtsys --dry-run
```
