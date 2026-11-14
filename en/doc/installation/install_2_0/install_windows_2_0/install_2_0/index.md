---
layout: page
title: installation
---

<!-- Title: Installation -->
#contents

## Installation of Required Software

To use OpenRTM-aist, you need to install software such as Python, CMake, Doxygen, and Visual Studio.

<div align="right"><a href="windows10-logo.png"><img src="windows10-logo.png" width="10%; margin:50 50 50 50:w!px;" align="right"></a></div>

### Visual Studio

Visual Studio is required not only for C++ development, but also for building installers when creating RTCs in Python or Java.
Install the free Community Edition below, or obtain and install Visual Studio 2015/2017/2019/2022 separately.

- [Microsoft **Download Visual Studio 2022**](https://visualstudio.microsoft.com/ja/downloads/?utm_source=mscom&utm_campaign=msdocs)

The latest version of Visual Studio currently verified to work is 2022. <br>
It is common to forget to install the C++ development environment. We recommend reading the following guide.
  - [Installing Visual Studio Community 2022]({{ site.baseurl }}/en/doc/installation/install_1_2/cpp_1_2/install_windows_1_2/visual_studio_1_2/visual_studio_2022)

### Python

Python is required not only for developing RTCs in Python but also for various OpenRTM-aist tools.
The versions of Python supported by OpenRTM-aist are 3.8, 3.9, 3.10, 3.11, and 3.12.
We recommend installing the latest version.

- [Python Releases for Windows](https://www.python.org/downloads/windows/)
  - [python-3.11.1-amd64.exe (64-bit version)](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)

Please note the following when installing:

  - The Python installation directory can be specified by selecting [Customize installation] during installation.
  - For instructions on specifying the installation directory using [Customize installation], refer to the following page:
    - [Get Started with OpenRTM-aist in 10 Minutes! - Installing Python]({{ site.baseurl }}/en/doc/installation/lets_start#toc1)

### CMake

CMake is required to automatically generate build files such as Visual Studio project files on Windows and Makefiles on Linux. <br>
Install the latest version whenever possible.

- [CMake (Version 3.11 or later recommended)](https://cmake.org/download/)
  - [cmake-3.29.3-windows-x86_64.msi (64-bit version)](https://github.com/Kitware/CMake/releases/download/v3.29.3/cmake-3.29.3-windows-x86_64.msi)
  - During installation, it is recommended to select [Add CMake to the system PATH for all users] on the [Install Option] screen.

### Doxygen & Graphviz

Doxygen is a tool that automatically generates documentation from source code comments. <br>
Graphviz is required for generating diagrams such as class diagrams when creating documentation with Doxygen. <br>
In OpenRTM-aist, RTCBuilder allows you to enter various design information during RTC design, which is output as source code comments.
Processing these comments with Doxygen enables the generation of well-formatted RTC documentation. <br>
Install the latest versions whenever possible.

- [Doxygen](https://doxygen.nl/download.html#latestsrc)
  - [doxygen-1.11.0-setup.exe](https://www.doxygen.nl/files/doxygen-1.11.0-setup.exe) (No distinction between 32-bit and 64-bit versions)
  - If you cannot download it using Microsoft Edge, refer to the OpenRTM-aist download instructions:
    - [Get Started with OpenRTM-aist in 10 Minutes! - Downloading OpenRTM-aist]({{ site.baseurl }}/en/doc/installation/lets_start#toc2)

&aname(Graphviz);
- [Graphviz](https://graphviz.gitlab.io/download/)
  - [windows_10_cmake_Release_graphviz-install-11.0.0-win64.exe](https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/11.0.0/windows_10_cmake_Release_graphviz-install-11.0.0-win64.exe)

During installation, you will be asked how to configure the system PATH under [Install Options]. It is recommended to select "Add Graphviz to the system PATH for all users".

Download and run the Windows binary executable from the website above to install Graphviz.

After installation, run `dot -v` from the command prompt and verify that plugin information is displayed.

```text
 >dot -v
dot - graphviz version 11.0.0 (20240428.1522)
libdir = "C:\Program Files\Graphviz\bin"
Activated plugin library: gvplugin_dot_layout.dll
Using layout: dot:dot_layout
Activated plugin library: gvplugin_core.dll
Using render: dot:core
Using device: dot:dot:core
The plugin configuration file:
        C:\Program Files\Graphviz\bin\config6
                was successfully loaded.
    render      :  cairo dot dot_json fig gdiplus json json0 map mp pic pov ps svg svg_inline tk xdot xdot_json
    layout      :  circo dot fdp neato nop nop1 nop2 osage patchwork sfdp twopi
    textlayout  :  textlayout
    device      :  bmp canon cmap cmapx cmapx_np dot dot_json emf emfplus eps fig gif gv imap imap_np ismap jpe jpeg jpg json json0 metafile mp pdf pic plain plain-ext png pov ps ps2 svg svg_inline svgz tif tiff tk xdot xdot1.2 xdot1.4 xdot_json
    loadimage   :  (lib) bmp eps gif jpe jpeg jpg png ps svg
```

### JDK8

Required for Java development. Please refer to the following page:

- [Installing JDK8]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

## Installing OpenRTM-aist

Once the software above has been installed, proceed with the installation of OpenRTM-aist.

### Downloading the Installer

Download the Windows installer (MSI format) for OpenRTM-aist.

<table class="table-alt">
  <tr>
    <th><a href="https://openrtm.org/pub/Windows/OpenRTM-aist/2.0/OpenRTM-aist-2.0.2-RELEASE_x86_64.msi">OpenRTM-aist-2.0.2-RELEASE_x86_64.msi</a></th>
    <th>MD5:a03eebe388dd4d63f4b91bf98afc5884</th>
    <th>851MB</th>
  </tr>
</table>

If you cannot download the installer using Microsoft Edge, refer to the following page:

- [Get Started with OpenRTM-aist in 10 Minutes! - Downloading OpenRTM-aist]({{ site.baseurl }}/en/doc/installation/lets_start#toc2)

This installer includes the following:

- Development environment for C++
  - OpenCV 4.5.0
  - Legacy C++ DLLs (required for running older RTCs)
- Development environment for Python
- Development environment for Java
- omniORB 4.3.2
- OpenRTP (GUI tools, RTCBuilder, RTSystemEditor)
  - JRE8 environment (required for OpenRTP)
- VCVerChanger (GUI tool)
- rtshell (CUI tool)

### Installation

For details of the installation procedure, refer to the following page:

- [Get Started with OpenRTM-aist in 10 Minutes! - Installing OpenRTM-aist]({{ site.baseurl }}/en/doc/installation/lets_start#toc3)

To verify that the installation was successful, try running the sample components:

- [Get Started with OpenRTM-aist in 10 Minutes! - Running Sample Components]({{ site.baseurl }}/en/doc/installation/lets_start#toc5)

For details on system environment variables configured by the installer and installed files, refer to:

- [OpenRTM-aist Installer Operations]({{ site.baseurl }}/en/doc/installation/install_2_0/install_windows_2_0/install_workcontent_2_0)

### Specifying the Visual Studio Version

The system environment variable **RTM_VC_VERSION** is configured according to the installed Visual Studio version.

If you want to change it after installation, you can use a GUI tool. See the [VCVerChanger]({{ site.baseurl }}/en/content/vc_version_changer/) page for instructions.

<br>

<table class="table-alt">
  <tr>
    <th>Visual Studio Version</th>
    <th>Value for the RTM_VC_VERSION System Environment Variable</th>
    <th></th>
  </tr>
  <tr>
    <td>2015, 2017</td>
    <td>vc14</td>
    <td></td>
  </tr>
  <tr>
    <td>2019, 2022</td>
    <td>vc16</td>
    <td>Default Setting</td>
  </tr>
</table>

After installation, even if you do not change the Visual Studio version, verify the system environment variable settings using [VCVerChanger]({{ site.baseurl }}/en/content/vc_version_changer/).
If unnecessary paths remain, remove them.

<br>

