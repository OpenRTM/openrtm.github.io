---
layout: page
title: rtresurrect
---
<!-- Title: rtresurrect -->

## Format
```
rtresurrect [OPTION ...] [RTSPROFILE_FILE]
```

## Overview
Loads an RTSProfile file and restores an RT system using running components. Connections between components and component configuration parameters are reflected according to what is described in the RTSProfile file. Components that are not marked as "required" in the RTSProfile file and are not running are ignored.

If no file name is specified, RTSProfile-format data is read from stdin.

## Options (OPTION)
```
 --dry-run　　 Displays what will be done to restore the system and exits. (It does not actually restore the system.)
 -x, --xml　　 Uses XML format.
 -y, --yaml　　Uses YAML format.
 --version　　 Displays the program version number and exits.
 -h, --help　　Displays help and exits.
 -v, --verbose Outputs verbose information. [Default: False]
```

## Return Values
Returns zero on success. Returns a non-zero value on failure.

Debug information and errors are output to stderr.

## Examples
- Restores the RT system using a file named sys.rtsys.
```
 $ rtresurrect sys.rtsys
```

- Displays what will be done when restoring using a file named sys.rtsys. (The actual restore process is not performed.)
```
 $ rtresurrect sys.rtsys --dry-run
```
