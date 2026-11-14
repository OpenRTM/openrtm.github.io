---
layout: page
title: openrtm-aist installer operations
---

<!-- Title: OpenRTM-aistインストーラ作業内容 -->

<br>

## Installer Operations

The installer copies files and configures system settings according to the following procedures.

The details below are provided as a reference when verifying that installation and uninstallation have been completed correctly.

- Copies various files under the installation directory (`C:\Program Files`)
- Creates an OpenRTM-aist folder under the Start Menu and configures various shortcuts
- Configures environment variables (when OpenRTM-aist 2.1.0 is installed with default settings)

```text
RTM_BASE=C:\Program Files\OpenRTM-aist\\
RTM_ROOT=C:\Program Files\OpenRTM-aist\2.1.0\\
RTM_VC_VERSION=vc16
RTM_JAVA_ROOT=C:\Program Files\OpenRTM-aist\2.1.0\\
RTM_IDL_DIR=C:\Program Files\OpenRTM-aist\2.1.0\rtm\idl\\
OMNI_ROOT=C:\Program Files\OpenRTM-aist\2.1.0\omniORB\4.3.4_vc16\\
OpenCV_DIR=C:\Program Files\OpenRTM-aist\2.1.0\OpenCV4.13.0\\
OpenRTM_DIR=C:\Program Files\OpenRTM-aist\2.1.0\cmake\\
```

- Adds the following entries to the PATH environment variable (when OpenRTM-aist 2.1.0 is installed with default settings)

```text
C:\Program Files\OpenRTM-aist\2.1.0\bin\vc16\\
C:\Program Files\OpenRTM-aist\2.1.0\omniORB\4.3.4_vc16\bin\x86_win32\\
C:\Program Files\OpenRTM-aist\2.1.0\OpenCV4.13.0\x64\vc16\bin\\
```

## Installed Files

Files are installed with the following directory structure.<br>

<!-- By running the script that verifies the installation environment settings above, a log file containing the OpenRTM-aist directory structure generated using the tree command is saved, allowing detailed inspection. -->

```text
<install_dir>
  + OpenRTM-aist
     + 1.x.x  : Runtime files for older versions
     + 2.0.x  : Runtime files for older versions
     + 2.1.x
        + bin: DLLs, libraries, and various commands
        + cmake: OpenRTMConfig.cmake
        + coil: coil header files
        + Components
           + C++
              + Examples: C++ sample components
              + OpenCV: OpenCV C++ sample components
           + Java: Java sample components
           + Python: Python sample components
        + ext: Files for extension modules
        + hrtm: Wrapper libraries for HRTM
        + jar: JAR files
        + jre: AdoptOpenJDK JRE
        + omniORB 4.3.4
        + OpenCV 4.13.0
        + rtm: OpenRTM-aist header files
           + idl: OpenRTM-aist IDL files
        + util
           + OpenRTP: RTCBuilder and RTSystemEditor tools
           + RTSystemEditor: Files for RTSystem Editor only
           + VCVerChanger: Tool for specifying the Visual Studio version in use
```
