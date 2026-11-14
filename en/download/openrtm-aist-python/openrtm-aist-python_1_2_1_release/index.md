---
layout: page
title: openrtm-aist-python 1.2.1-release
---
<!-- Title: OpenRTM-aist-Python 1.2.1-RELEASE -->
<div align="right"><a href="python-logo.png"><img src="python-logo.png" width="10%;" align="right"></a></div>
#contents(4)

<br>
(G) Please refer to the following page for the installation procedure.

- [OpenRTM-aist (Python) 1.2 installation]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2)

## Package
### Windows Installer
The msi file is over 900MB in size. Use a high-speed line (50Mbps or more) to download in minutes.

#### For 64bit

<!-- | LEFT:300 | LEFT | LEFT:120 | -->
<table class="table-alt">
  <tr>
    <td>Installer for Windows <br> (including OpenRTM-aist, C ++, Python, <br> Java version and OpenRTP, <br> RTShell (4.2.2)) <br> (Visual Studio 2010, 2012, <br> 2013, 2015, 2017 , 2019))</td>
    <td>.msi]] <br> MD5: be6b346d61768435d812cc032bc7a529</td>
    <td>November 25, 2019</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi">python-2.7.16.amd64.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe">python-3.6.8-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe">python-3.7.5-amd64.exe</a></td>
    <td><a href="https://www.python.org">[python.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.15.5/cmake-3.15.5-win64-x64.msi">cmake-3.15.5-win64-x64.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="https://www.doxygen.nl/files/doxygen-1.9.2-setup.exe">doxygen-1.9.2-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">* Install Python version "3.7", "3.6", or "2.7". </span>;
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [[doxygen: http: //www.doxygen.nl/index.html]] and download and install the latest "doxygen-X.X.X-setup.exe".

#### For 32bit

<table class="table-alt">
  <tr>
    <td>Windows installer <br> (including OpenRTM-aist, C ++, Python, <br> Java version and OpenRTP, <br> RTShell (4.2.2)) <br> (Visual Studio 2010, 2012, <br> 2013, 2015, 2017, 2019 Common)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1-RELEASE_x86. msi">OpenRTM-aist-1.2.1-RELEASE_x86.msi</a> <br> MD5: a9186d409cafc039432a0e1c6e7e02ef</td>
    <td>November 25, 2019</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi">python-2.7.16.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe">python-3.6.8.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.5/python-3.7.5.exe">python-3.7.5.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.15.5/cmake-3.15.5-win32-x86.msi">cmake-3.15.5-win32-x86.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="https://www.doxygen.nl/files/doxygen-1.9.2-setup.exe">doxygen-1.9.2-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">* Install Python version "3.7", "3.6", or "2.7". </span>;
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [[doxygen: http: //www.doxygen.nl/index.html]] and download and install the latest "doxygen-X.X.X-setup.exe".


For installation, [Start OpenRTM-aist in 10 minutes!]({{ site.baseurl }}/en/doc/installation/lets_start121) page for instructions. 

### Linux package
<!-- Linux packages will be provided sequentially. Please refer to the following for how to build from source. -->

We currently offer packages in the following distribution versions. You can use the installation script distributed below to install the required packages at once.


<table class="table-alt">
  <tr>
    <th>Distribution version</th>
    <th>Bulk installation script (right click to get URL)</th>
  </tr>
  <tr>
    <td>Ubuntu 16.04 (xenial) i386 / amd64 <br> Ubuntu 18.04 (bionic) amd64 <br></td>
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



By specifying options, you can now install packages that meet your needs. Please refer to [Bulk installation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script) for installation method, options and package types.


If you have already installed 1.2.0-RELEASE, you can update it.

For Ubuntu / Debian

$ sudo apt-get update
 $ sudo apt-get upgrade

<!-- For Fedora -->
<!--  -->
<!-- # dnf update -->

See [OpenRTM-aist (Python version) 1.2 system installation]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2) for download and installation methods.

&aname(src);
## Source code

<table class="table-alt">
  <tr>
    <td>Python version source code</td>
    <td><a href="//github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.1/OpenRTM-aist- Python-1.2.1.tar.gz">OpenRTM-aist-Python-1.2.1.tar.gz: https</a> <br> MD5: 88c83d2b3dfc70b8eb0b3377be3d51f9</td>
    <td>2019/11/25</td>
  </tr>
  <tr>
    <td>Python source code (Win32)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.1/OpenRTM-aist -Python-1.2.1.zip">OpenRTM-aist-Python-1.2.1.zip</a> <br> MD5: 84ad916e98e2eeb7b65450c57e15a0d1</td>
    <td>2019/11/25</td>
  </tr>
</table>


### Build from source

For details on how to build from source, see [Building from source (Windows)]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2/build_source_python_windows_1_2) or [Building from source (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2/build_source_python_linux_1_2) .

### Create deb / rpm package

From 1.1, the creation of deb packages for Ubuntu and Debian and rpm packages for Fedora from the above source code is officially supported. <br>
You can create a package by following the steps below. When creating a package, use the Bulk installation script (pkg_install _ ***. Sh) to install the necessary packages in advance.

 $ tar xvzf OpenRTM-aist-Python-1.2.1.tar.gz
 $ cd OpenRTM-aist-Python-1.2.1/packages
 $ make

Packages are created in the pacakges directory.

<span style="color:red;">* Install tools such as "dpkg-dev build-essential debhelper devscripts" when creating deb packages on Ubuntu and Debian, and "rpm-build createrepo" before creating rpm packages on Fedora. Must be kept. </span>;
These can be installed by executing [Bulk nstallation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script) with the -c option.


## Release notes
OpenRTM-aist Official Website can use source code, Windows installer, Linux package, etc. in dual license system which can be selected from LGPL license or individual contract with AIST.

- [1.2.1-RELEASE](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/tag/v1.2.1)

### Supported (build verified) OS
- Ubuntu 16.04 i386, amd64
- Ubuntu 18.04 amd64
- Raspian Buster armhf
- Windows 10 (32 / 64bit)

