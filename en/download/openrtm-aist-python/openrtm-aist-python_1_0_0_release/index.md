---
layout: page
title: openrtm-aist-python-1.0.0-release
---
<!-- Title: OpenRTM-aist-Python-1.0.0-RELEASE -->
#contents
<div align="left"><a href="python-logo.png"><img src="python-logo.png" width="15%;" align="left"></a></div>

## Important notice

If you already have version 0.4.x installed, it must be uninstalled prior to installing version 1.x. Even after uninstalling 0.4.x, some files may remain. The folder containing these must be removed manually:

- Windows:
```
 C:\Python[24,25,26]\Lib\site-packages\OpenRTM
```
- Linux:
```
  /usr/lib/python[2.4,2.5,2.6]/site-packages/OpenRTM
```

## &aname(source){Source code};
<table class="table-alt">
  <tr>
    <td>Python source code</td>
    <td><a href="">OpenRTM-aist-Python-1.0.0-RELEASE.tar.gz</a>(No corresponding page available.) <br> MD5:dd11ef6a2e6277fa095e0fbd3210a2a5</td>
    <td>10/05/07</td>
  </tr>
  <tr>
    <td>Python source code (Windows)</td>
    <td><a href="">OpenRTM-aist-Python-1.0.0-RELEASE.zip</a>(No corresponding page available.) <br> MD5:371b427288cb0f69ab3dcf71d8eda169</td>
    <td>10/05/07</td>
  </tr>
</table>

## Packages
### &aname(winpkg){Windows installer (For Python 2.4, 2.5 and 2.6)};

To install using OpenRTM-aist-Python-1.0.0.msi, Python version 2.4, 2.5 or 2.6 is necessary. The OpenRTM-aist-Python-1.0.0.msi installer will detect the installed Python versions and install OpenRTM-aist and omniORBpy into each of them. There is no need to install omniORBpy separately.

<table class="table-alt">
  <tr>
    <td>Windows installer</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python-1.0.0.msi">OpenRTM-aist-Python-1.0.0.msi</a> <br> MD5:4afe4de69c9b56086fc97e9697334a36</td>
    <td>10/05/07</td>
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

### &aname(linuxpkg){Linux packages};

Openrtm.org provides repositories containing packages for Debian, Fedora, Ubuntu and Vine Linux. Please see the following pages for details.

- [Fedora]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/install_fedora_python_1_1/)
- [Ubuntu/Debian]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/install_ubuntu_python_1_1/)
- [Vine Linux]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/install_vine_python_1_1/)

<table class="table-alt">
  <tr>
    <td>Distribution</td>
    <td>Supported versions</td>
    <td>Install script</td>
  </tr>
  <tr>
    <td>Vine Linux</td>
    <td>4.0, 4.2(i386 only), 5.0 (i386, x86_64)</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/python/install_scripts/pkg_install_python_vine.sh">pkg_install_python_vine.sh </a></td>
  </tr>
  <tr>
    <td>Fedora</td>
    <td>11, 12 (i386/x86_64)</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/python/install_scripts/pkg_install_python_fedora.sh">pkg_install_python_fedora.sh </a></td>
  </tr>
  <tr>
    <td>Ubuntu</td>
    <td>8.04, 8.10, 9.04, 9.10, 10.04 (i386/x86_64)</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/python/install_scripts/pkg_install_python_ubuntu.sh">pkg_install_python_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian</td>
    <td>3.1 (i386), 4.0, 5.0 (i386, x86_64)</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/python/install_scripts/pkg_install_python_debian.sh">pkg_install_python_debian.sh </a></td>
  </tr>
</table>

## Release notes: 1.0.0-RELEASE&aname(note);

1.0.0, the newest version of OpenRTM-aist for Python, was released on the 7th of May 2010. This release conforms with the OMG RTC Specification version 1.0 released in April, 2008.

Source code, Windows installers, and Linux packages are available from the OpenRTM-aist official website under the Eclipse Public License (EPL) or a separate commercial license purchased from the National Institute of Advanced Science and Technology.

Prior releases required installing many tools to create the build environment. This release includes installers, particularly for Windows, that combine all tools and necessary libraries, such as omniORBpy, into one. It is simple to install the entire OpenRTM-aist environment with a single action.

- [OpenRTM-aist-Python-1.0.0-RELEASE.tar.gz]()(No corresponding page available.) -- released 2010.05.07
  - Compliant with the OMG RTC specification version 1.0.
  - New data port has been introduced. 
    - Push/pull data flow types are supported.
    - Subscription types have been implemented.
    - Publisher policies have been implemented.
    - Buffering policy and time-out functionality have been implemented.
  - Miscellaneous bug fixes.
  - Completed configuration system.
    - New options in rtc.conf.
    - より多くの項目を設定可能に
  - Manager CORBA service has been implemented (experimental). 
    - Master-slave managers.
    - The Interoperable Naming Service (INS) CORBA object is supported.
    - Remote management of components.
  - Windows installer.
    - Includes omniORBpy.
    - Includes RTSystemEditor (RCP version).

  - Supported version of Python
    - 2.4
    - 2.5
    - 2.6
  - Supported operating systems (verified).
    - Debian4.0-i386
    - Debian5.0-i386
    - Fedora release 11 (Leonidas)-i386
    - Fedora release 12 (Constantine)-i386
    - Ubuntu 8.04-i386
    - Ubuntu 8.10-i386
    - Ubuntu 9.04-i386
    - Ubuntu 9.10-i386
    - Ubuntu 10.04LTS-i386
    - Vine Linux 4.0 (Latour)-i386
    - Vine Linux 4.2 (Lynch Bages)-i386
    - Vine Linux 5.0 (Lafite)-i386
    - Windows XP
    - Windows Vista
    - Windows7

