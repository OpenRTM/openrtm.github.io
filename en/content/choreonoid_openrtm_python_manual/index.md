---
layout: page
title: "openrtm integration plugin for choreonoid, python version manual"
---

#contents


The Python version of the Choreonoid OpenRTM integration plugin is a plugin for linking robots on [Choreonoid](http://choreonoid.org/ja/) with RTCs developed in Python.
The following main functions are available.

## Efficient Development of RTCs That Link with Simulators on Choreonoid Using Python

The OpenRTM integration plugin included standard with Choreonoid enables RTC development in C++, but there have been issues in that building the development environment is difficult and compilation takes time, making it inefficient.
Therefore, by distributing the prebuilt Choreonoid + OpenRTM integration plugin Python version, you can develop RTCs that link with simulators on Choreonoid immediately after downloading.

<br>

<div align="center"><a href="cnoid-rtm-py1.png"><img src="cnoid-rtm-py1.png" width="70%;"></a></div>
<br>


## Fast Development with a Dynamic Python Code Editing Tool

This plugin includes a Python editor that runs on Choreonoid.

<br>

<div align="center"><a href="cnoid-rtm-py2-2.png"><img src="cnoid-rtm-py2-2.png" width="70%;"></a></div>
<br>

Simply editing and saving code in the Python editor immediately reflects the changes in the RTC.
It also supports settings for data ports, service ports, and configuration parameters, enabling RTC development and operation checks using only Choreonoid and Python.


<br>

<div align="center"><a href="cnoid-rtm-py4.png"><img src="cnoid-rtm-py4.png" width="70%;"></a></div>
<br>


## RTC Launcher

A launcher that displays RTCs in a list and can start them with a single button runs on Choreonoid.
This plugin includes 73 types of RTCs as sample components, allowing you to develop various RT Systems on Choreonoid.



<br>

<div align="center"><a href="cnoid-rtm-py3.png"><img src="cnoid-rtm-py3.png" width="70%;"></a></div>
<br>


### RTC Registration Procedure
Create a folder with an appropriate name (for example, TestRTC) under **share/rtc** in the Choreonoid installation directory.

Then place **RTC.xml** and the Python file, executable file, or dll for running the RTC under it, and registration is complete.
The Python file, executable file, and dll can be found by search even if they are not directly under the TestRTC folder.

* When registering a C++ RTC, since this plugin is developed with Visual Studio 2015 (64-bit), dll files cannot be loaded unless they are built with the same Visual Studio. It can be started from an executable file, but in that case, the folder containing the required dll files (RTC120_vc12.dll, etc.) must be added to PATH.

```
 choreonoid
    |-share
      |-rtc
        |-TestRTC
          |-RTC.xml
            |-TestRTC.py(もしくはTestRTCComp.exe、TestRTC.dll)
```


## Installation Procedure and Tutorials
The installation procedure and tutorials are described on the following pages.

- [Installation Procedure for the OpenRTM Integration Plugin for Choreonoid, Python Version]({{ site.baseurl }}/ja/content/choreonoid_openrtm_python_install)
- [OpenRTM Integration Plugin for Choreonoid, Python Version Tutorial (TankJoystick)]({{ site.baseurl }}/ja/content/choreonoid_openrtm_python_tutorial1)
- [OpenRTM Integration Plugin for Choreonoid, Python Version Tutorial (Quadruped Robot)]({{ site.baseurl }}/ja/content/choreonoid_openrtm_python_tutorial2)
- [Troubleshooting for the OpenRTM Integration Plugin for Choreonoid, Python Version]({{ site.baseurl }}/ja/content/choreonoid_openrtm_python_troboleshooting)
- [OpenRTM Integration Plugin for Choreonoid, Python Version (Notes)]({{ site.baseurl }}/ja/content/choreonoid_openrtm_python_note)
