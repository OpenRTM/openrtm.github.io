---
layout: page
title: openrtm-aist-python 1.2.2-release
---

<!-- Title: OpenRTM-aist-Python 1.2.1-RELEASE -->
<div align="right"><a href="python-logo.png"><img src="python-logo.png" width="15%;" align="right"></a></div>
#contents(4)

<br>
(G) Please refer to the following page for the installation procedure.

- [OpenRTM-aist (Python) 1.2 installation]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2)

## Package
### Windows Installer
The msi file is 800MB in size. Use a high-speed line (50Mbps or more) to download in minutes.

#### For 64bit

<table class="table-alt">
  <tr>
    <td>Windows Installer <br> (including OpenRTM-aist, C++, Python, <br> Java version and OpenRTP, <br> rtshell (4.2.2)) <br> (Visual Studio 2012, 2013, <br> 2015, 2017, 2019)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.2/OpenRTM-aist-1.2.2-RELEASE_x86_64.msi">OpenRTM-aist-1.2.2-RELEASE_x86_64.msi</a> <br> MD5:3275df2f82252e6c6a33249ce2170563</td>
    <td>2020/08/26</td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe">python-3.6.8-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe">python-3.7.9-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.8</td>
    <td><a href="https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe">python-3.8.5-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.18.1/cmake-3.18.1-win64-x64.msi">cmake-3.18.1-win64-x64.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="https://www.doxygen.nl/files/doxygen-1.9.2-setup.exe">doxygen-1.9.2-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">* Install Python version "3.8", "3.7", or "3.6". </span>;
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [[doxygen: http: //www.doxygen.nl/index.html]] and download and install the latest "doxygen-X.X.X-setup.exe".


#### For 32bit

<table class="table-alt">
  <tr>
    <td>Installer for Windows<br> (OpenRTM-aist、C++、Python、<br>Java version, and OpenRTP、<br>including rtshell(4.2.2))<br>(Visual Studio 2012、2013、<br>2015、2017、2019)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.2/OpenRTM-aist-1.2.2-RELEASE_x86.msi">OpenRTM-aist-1.2.2-RELEASE_x86.msi</a> <br>MD5:5e3f29853dedf0bf5af69675657a5c04</td>
    <td>2020/08/26</td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe">python-3.6.8.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.9/python-3.7.9.exe">python-3.7.9.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.8</td>
    <td><a href="https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe">python-3.8.5.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.18.1/cmake-3.18.1-win32-x86.msi">cmake-3.18.1-win32-x86.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="https://www.doxygen.nl/files/doxygen-1.9.2-setup.exe">doxygen-1.9.2-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">* Install Python version "3.8", "3.7" or "3.6". </span>;
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [[doxygen: http: //www.doxygen.nl/index.html]] and download and install the latest "doxygen-X.X.X-setup.exe".


For installation, [Start OpenRTM-aist in 10 minutes!](/ja/doc/installation/lets_start) page for instructions. 

### Linux package
<!-- Linux packages will be provided sequentially. Please refer to the following for how to build from source. -->

We currently offer packages in the following distribution versions. You can use the installation script distributed below to install the required packages at once.


<table class="table-alt">
  <tr>
    <th>Distribution version</th>
    <th>Bulk installation script (right click to get URL)</th>
  </tr>
  <tr>
    <td>Ubuntu 16.04 (xenial) i386 / amd64 <br> Ubuntu 18.04 (bionic) amd64 <br> Ubuntu 20.04 (focal) amd64 <br></td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh</a></td>
  </tr>
  <tr>
    <td>Raspbian Buster armhf</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_raspbian.sh">pkg_install_raspbian.sh</a></td>
  </tr>
</table>
<!-- | Debian 8.0 (jessie) i386 / amd64 &br; Debian 9.0 (stretch) i386 / amd64 | [(pkg_install_debian.sh>https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_debian.sh]] | -->
<!-- | Fedora 27 i686 / x86_64 &br; Fedora 28 i686 / x86_64 &br; Fedora 29 i686 / x86_64 | [(pkg_install_fedora.sh>https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_fedora.sh]] | -->

<!-- * The bulk installation script for Fedora will be compatible with OpenRTM-aist 1.2.0 or later. -->



By specifying options, you can now install packages that meet your needs. <br>
<span style="color:red;">※You can install the old version "1.2.1". You can also downgrade from "1.2.2" to "1.2.1".</span>; <br>
Please refer to [Bulk installation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script) for installation method, options and package types.


If you have already installed 1.2.1-RELEASE, please install the package for Python3 by the following procedure.

For Ubuntu / Debian (Except Ubuntu 16.04)

```
 $ sudo apt update
 $ sudo apt install omniidl-python3 openrtm-aist-python3 openrtm-aist-python3-example openrtm-aist-python3-doc
 
```
For Ubuntu 16.04

```
 $ sudo apt update
 $ sudo apt install omniidl-python3 openrtm-aist-python3 openrtm-aist-python3-example
 
```

<!-- For Fedora -->
<!--  -->
<!-- # dnf update -->

See [OpenRTM-aist (Python version) 1.2 system installation]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2) for download and installation methods.

&aname(src);
## Source code

<table class="table-alt">
  <tr>
    <td>Python version source code</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.2/OpenRTM-aist-Python-1.2.2.tar.gz">OpenRTM-aist-Python-1.2.2.tar.gz</a> <br> MD5: d64ba0ba2ba65cf5a1eb60f03394fc29</td>
    <td>2020/08/26</td>
  </tr>
  <tr>
    <td>Python source code (Win32)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.2/OpenRTM-aist-Python-1.2.2.zip">OpenRTM-aist-Python-1.2.2.zip</a> <br> MD5: b36f289bdf8933978316090bd2729931</td>
    <td>2020/08/26</td>
  </tr>
</table>


### Build from source

For details on how to build from source, see [Building from source (Windows)]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2/build_source_python_windows_1_2) or [Building from source (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2/build_source_python_linux_1_2) .

### Create deb / rpm package

From 1.1, the creation of deb packages for Ubuntu and Debian and rpm packages for Fedora from the above source code is officially supported. <br>
You can create a package by following the steps below. When creating a package, use the Bulk installation script (pkg_install_***.sh) to install the necessary packages in advance.

```
 $ tar xvzf OpenRTM-aist-Python-1.2.2.tar.gz
 $ cd OpenRTM-aist-Python-1.2.2/packages
 $ make
```

Packages are created in the pacakges directory.

<span style="color:red;">* Install tools such as "dpkg-dev build-essential debhelper devscripts" when creating deb packages on Ubuntu and Debian, and "rpm-build createrepo" before creating rpm packages on Fedora. Must be kept. </span>;
These can be installed by executing [Bulk nstallation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script) with the -c option.


## Release notes
OpenRTM-aist Official Website can use source code, Windows installer, Linux package, etc. in dual license system which can be selected from LGPL license or individual contract with AIST.

- [1.2.2-RELEASE](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/tag/v1.2.2)

### Supported (build verified) OS
- Ubuntu 16.04 i386, amd64
- Ubuntu 18.04 amd64
- Ubuntu 20.04 amd64
- Raspian Buster armhf
- Windows 10 (32 / 64bit)

