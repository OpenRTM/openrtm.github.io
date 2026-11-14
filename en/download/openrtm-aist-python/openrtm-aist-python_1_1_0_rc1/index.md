---
layout: page
title: openrtm-aist-python-1.1.0-rc1
---

<!-- Title: OpenRTM-aist-Python-1.1.0-RC1 -->
<div align="left"><a href="python-logo.png"><img src="python-logo.png" width="15%;" align="left"></a></div>
<br>
<br>
<br>
#contents
#clear

## Important notice

If you already have version 0.4.x installed, it must be uninstalled prior to installing version 1.x. Even after uninstalling 0.4.x, some files may remain. The folder containing these must be removed manually.

- Windows:
```
 C:\Python[24,25,26]\Lib\site-packages\OpenRTM
```
- Linux:
```
  /usr/lib/python[2.4,2.5,2.6]/site-packages/OpenRTM
```

## &aname(source){Source-code};
<table class="table-alt">
  <tr>
    <td>Python版 source code</td>
    <td><a href="">OpenRTM-aist-Python-1.1.0-RC1.tar.gz</a>(No corresponding page available.) <br> MD5:bbc9c4915d13cef0f5a925a070bab0aa</td>
    <td>11/10/04</td>
  </tr>
  <tr>
    <td>Python版 source code (Win32)</td>
    <td><a href="">OpenRTM-aist-Python-1.1.0-RC1.zip</a>(No corresponding page available.) <br> MD5:513f9a80ab7ce3c4d831c509e2252a8b</td>
    <td>11/10/04</td>
  </tr>
</table>


<br>
## Packages
### &aname(winpkg){Windows installer (For Python 2.4,2.5 and 2.6)};

To install using OpenRTM-aist-Python-1.1.0.msi, Python version 2.4, 2.5 or 2.6 is necessary. The OpenRTM-aist-Python-1.1.0.msi installer will detect the installed Python versions and install OpenRTM-aist and omniORBpy into each of them. There is no need to install omniORBpy separately.


<table class="table-alt">
  <tr>
    <td>Windows installer</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python-1.1.0-RC1.msi">OpenRTM-aist-Python-1.1.0-RC1.msi</a> <br> MD5:1faaf9c25bcb879628da3d23f851a4cd</td>
    <td>11/010/04</td>
  </tr>
  <tr>
    <td>Python-2.4.4</td>
    <td><a href="http://www.python.org/ftp/python/2.4.4/python-2.4.4.msi">python-2.4.4.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-2.5.1</td>
    <td><a href="http://www.python.org/ftp/python/2.5.1/python-2.5.1.msi">python-2.5.1.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-2.6.2</td>
    <td><a href="http://www.python.org/ftp/python/2.6.2/python-2.6.2.msi">python-2.6.2.msi</a></td>
    <td><a href="http://www.python.org">python.org</a></td>
  </tr>
</table>

<br>
### &aname(linuxpkg){Linux packages};
Openrtm.org provides repositories containing packages for Debian, Ubuntu. Please see the following pages for details.

- [Fedora]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/install_fedora_python_1_1/)
- [Ubuntu/Debian]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/install_ubuntu_python_1_1/)
- [Vine Linux]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/install_vine_python_1_1/)


<table class="table-alt">
  <tr>
    <td>Distribution</td>
    <td>Supported versions</td>
    <td>Install script</td>
  </tr>
</table>
<!-- | Fedora | 11, 12 (i386/x86_64) |[[pkg_install_python_fedora.sh >http://www.openrtm.org/pub/OpenRTM-aist/python/install_scripts/pkg_install_python_fedora.sh]]| -->
<table class="table-alt">
  <tr>
    <th>Ubuntu</th>
    <th>8.04, 10.04, 10.10, 11.04 (i386/x86_64)</th>
    <th><a href="http://www.openrtm.org/pub/OpenRTM-aist/python/install_scripts/pkg_install_python_ubuntu.sh">pkg_install_python_ubuntu.sh </a></th>
  </tr>
  <tr>
    <td>Debian</td>
    <td>5.0 (i386, x86_64)</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/python/install_scripts/pkg_install_python_debian.sh">pkg_install_python_debian.sh </a></td>
  </tr>
</table>


<br>
## Release notes: 1.1.0-RC1&aname(note);

1.1.0-RC1, the newest version of OpenRTM-aist for Python, was released on the 4th of Oct 2011. 

Source code, Windows installers, and Linux packages are available from the OpenRTM-aist official website under the LGPL or a separate commercial license purchased from the National Institute of Advanced Science and Technology.

Prior releases required installing many tools to create the build environment. This release includes installers, particularly for Windows, that combine all tools and necessary libraries, such as omniORBpy, into one. It is simple to install the entire OpenRTM-aist environment with a single action.

- [OpenRTM-aist-Python-1.1.0-RC1.tar.gz]()(No corresponding page available.) -- released 2011.10.04 
  - Some APIs have been added.
    - Call back APIs.
    - Call backs for execution contexts.
  - SDO service frameworks
  - Misc bug fixes.
  - Experimental
    - Observer SDO service has been introduced.

  - Supported version of Python
    - 2.4
    - 2.5
    - 2.6
  - Supported operating systems (verified).
    - Debian5.0-i386
    - Ubuntu 8.04-i386
    - Ubuntu 10.04LTS-i386
    - Ubuntu 10.10-i386
    - Ubuntu 11.04-i386
    - Windows XP
    - Windows Vista
    - Windows7

