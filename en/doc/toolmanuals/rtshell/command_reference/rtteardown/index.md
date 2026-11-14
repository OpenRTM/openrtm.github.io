---
layout: page
title: rtteardown
---

<!-- Title: rtteardown -->

## Format
```
 rtteardown [OPTION ...] [RTSPROFILE_FILE]
```

# Overview
Deletes the connections of a running RT system using the connection information described in the RTSProfile file.

If no file name is specified, RTSProfile information is read from stdin.

## Options
```
 --dry-run　　 Displays what will be executed. (Deletion is not actually performed.)
 -x, --xml　　 Uses XML format.
 -y, --yaml 　 Uses YAML format.
 --version　　 Displays the program version number.
 -h, --help　　Displays help.
 -v, --verbose Outputs more detailed information.
```

## Return Values
Returns zero on success. Returns a non-zero value on failure.

Debug information and errors are output to stderr.

## Examples
- Deletes the connections of the currently running RT system using the information in the sys.rtsys file.
```
 $ rtteardown sys.rtsys
```

- Displays what will be done when deleting the connections of the currently running RT system using the information in the sys.rtsys file. (Deletion is not actually performed.)
```
 $ rtteardown sys.rtsys --dry-run
```

