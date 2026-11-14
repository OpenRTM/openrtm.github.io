---
layout: page
title: rtstodot
---
<!-- Title: -->

## Format
```
rtstodot [OPTION ...] [RTSPROFILE_FILE]
```

## Overview
Displays an RT system as a graph in Graphviz dot format. If no file is specified, information is read from stdin in RTSProfile format.

## Options (OPTION)
```
 -x, --xml　　 Uses XML format.
 -y, --yaml　　Uses YAML format.
 --version　　 Displays the program version number.
 -h, --help　　Displays help.
 -v, --verbose Outputs more detailed information.
```

## Return Values
Returns zero on success. Returns a non-zero value on failure.

Debug information and errors are output to stderr.

## Examples
- Displays an RT system based on the sys.rtsys file.
```
 $ rtstodot sys.rtsys | dot -T xlib
```

- Displays an RT system based on the sys.rtsys file and saves it to the sys.eps file in Encapsulated PostScript format.
```
 $ rtstodot sys.rtsys | dot -T eps > sys.eps
```

- Displays the currently running RT system.
```
 $ rtcryo | rtstodot | dot -T xlib
```
