---
layout: page
title: "troubleshooting for the openrtm integration plugin for choreonoid, python version"
---
#contents

## Choreonoid Does Not Start
The following causes are possible.

### Python Problem

First, confirm that the **64-bit version** of Python 2.7 is installed.

- [Python 2.7.14](https://www.python.org/downloads/release/python-2714/)

If it still does not start, set **PYTHONHOME** to the Python installation directory.

```
 set PYTHONHOME=C:\python27
```

If it still does not work, please let us know in the comments section below.


### Problem with the OpenGL Version Supported by the PC

Due to a problem with an internal Choreonoid library, Choreonoid cannot start on PCs that support only OpenGL 1.1.
Obtain and run the **OpenGL version check program** from the following site to confirm.

- [http://skomo.o.oo7.jp/f53/hp53_9.htm](http://skomo.o.oo7.jp/f53/hp53_9.htm)



## The OpenRTM Plugin Cannot Be Loaded

This is currently under investigation.



## None of the Plugins Can Be Loaded

Plugins cannot be loaded if the path contains Japanese characters.

This is an issue with Choreonoid itself, so it will not be handled here.

## The Process Crashes When Adding an RTCEditor Item

This issue is also under investigation.

