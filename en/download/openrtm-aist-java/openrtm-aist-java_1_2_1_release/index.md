---
layout: page
title: openrtm-aist-java-1.2.1-release
---

<!-- Title: OpenRTM-aist-Java-1.2.1-RELEASE -->
<div align="right"><a href="java_logo.png"><img src="java_logo.png" width="10%;" align="right"></a></div>
#contents(4)

<br>
(G) Please refer to the following page for the installation procedure.

- [Installing OpenRTM-aist (Java version) 1.2 series]({{ site.baseurl }}/en/doc/installation/install_1_2/java_1_2)
## Package
### Windows Installer
The msi file is over 900MB in size. Use a high-speed line (50Mbps or more) to download in minutes.

#### For 64bit

<table class="table-alt">
  <tr>
    <td>Windows Installer <br> (including OpenRTM-aist, C ++, Python, <br> Java version and OpenRTP, <br> rtshell (4.2.2)) <br> (Visual Studio 2010, 2012, <br> 2013, 2015, 2017 , 2019 common)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1-RELEASE_x86_64 .msi">OpenRTM-aist-1.2.1-RELEASE_x86_64.msi</a> <br> MD5: be6b346d61768435d812cc032bc7a529</td>
    <td>November 25, 2019</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi">python-2.7.16.amd64.msi</a></td>
    <td><a href="https://www.python.org">python .org</a></td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe">python-3.6.8-amd64.exe</a></td>
    <td><a href="https://www.python.org">python .org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe">python-3.7.5-amd64.exe</a></td>
    <td><a href="https://www.python.org">python .org</a></td>
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
<!-- - &color(red){* Please delete the old rtshell beforehand. However, if the OpenRTM-aist 1.1.2 version is installed using the msi file, no action is required. }; -->
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [doxygen](http://www.doxygen.nl/index.html) and download and install the latest "doxygen-X.X.X-setup.exe".

#### For 32bit

<table class="table-alt">
  <tr>
    <td>Windows Installer <br> (including OpenRTM-aist, C ++, Python, <br> Java version and OpenRTP, <br> rtshell (4.2.2)) <br> (Visual Studio 2010, 2012, <br> 2013, 2015, 2017 , 2019 common)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1-RELEASE_x86 .msi">OpenRTM-aist-1.2.1-RELEASE_x86.msi</a> <br> MD5: a9186d409cafc039432a0e1c6e7e02ef</td>
    <td>November 25, 2019</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi">python-2.7.16.msi</a></td>
    <td><a href="//www.python.org">python.org:https </a></td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe">python-3.6.8.exe</a></td>
    <td><a href="//www.python.org">python.org:https </a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.5/python-3.7.5.exe">python-3.7.5.exe</a></td>
    <td><a href="//www.python.org">python.org:https </a></td>
  </tr>
  <tr>
    <td>CMake</td>
    <td><a href="https://github.com/Kitware/CMake/releases/download/v3.15.5/cmake-3.15.5-win32-x86.msi">cmake-3.15.5-win32-x86.msi</a></td>
    <td><a href="https://cmake.org/">cmake</a></td>
  </tr>
  <tr>
    <td>Doxygen</td>
    <td><a href="http://doxygen.nl/files/doxygen-1.8.16-setup.exe">doxygen-1.8.16-setup.exe</a></td>
    <td><a href="http://www.doxygen.nl/index.html">doxygen</a></td>
  </tr>
</table>

- <span style="color:red;">* Install Python version "3.7", "3.6", or "2.7". </span>;
<!-- - &color(red){* Please delete the old rtshell beforehand. However, if the OpenRTM-aist 1.1.2 version is installed using the msi file, no action is required. }; -->


For installation, [Start OpenRTM-aist in 10 minutes!]({{ site.baseurl }}/en/doc/installation/lets_start121) page for instructions. <br>

<br>
### Linux package

We currently offer packages in the following distribution versions: <br>
You can use the installation script distributed below to install the required packages at once.


Distribution version | Batch installation script (right click to get URL) |
<table class="table-alt">
  <tr>
    <th>Ubuntu 16.04 (xenial) i386 / amd64 <br> Ubuntu 18.04 (bionic) amd64 <br></th>
    <th><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh</a></th>
  </tr>
  <tr>
    <td>Raspbian Buster armhf</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_raspbian.sh">pkg_install_raspbian.sh</a></td>
  </tr>
</table>
<!-- | Debian 8.0 (jessie) i386 / amd64 &br; Debian 9.0 (stretch) i386 / amd64 | [(pkg_install_debian.sh>https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_debian. sh]] | -->
<!-- | Fedora 27 i686 / x86_64 &br; Fedora 28 i686 / x86_64 &br; Fedora 29 i686 / x86_64 | [(pkg_install_fedora.sh>https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_fedora .sh]] | -->

<!-- * The batch installation script for Fedora will be compatible with OpenRTM-aist 1.2.0 or later. -->

By specifying options, you can now install packages that meet your needs. Please refer to [Batch installation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script) for installation method, options and package types.

## Java development environment

The following JDK is required for the operation and development of OpenRTM-aist-Java-1.2.1.
- JDK8 (1.8): [Install JDK8]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

&aname(src);
## Source code

<table class="table-alt">
  <tr>
    <td>Java version source code</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.1/OpenRTM-aist- Java-1.2.1.tar.gz">OpenRTM-aist-Java-1.2.1.tar.gz</a> <br> MD5: 0db80c61d07d69d5790116f95c7dfbfd</td>
    <td>2019/11/25</td>
  </tr>
  <tr>
    <td>Java version source code</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.1/OpenRTM-aist-Java- 1.2.1.zip">OpenRTM-aist-Java-1.2.1.zip</a> <br> MD5: be5082e762ec45f17434a9072ed2ba7d</td>
    <td>2019/11/25</td>
  </tr>
  <tr>
    <td>jar file and sample</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.1/OpenRTM-aist- Java-1.2.1-jar.zip">OpenRTM-aist-Java-1.2.1-jar.zip</a> <br> MD5: 359384b4be31524ad84ed06cf6477c39</td>
    <td>2019/11/25</td>
  </tr>
</table>


### Build from source

For information on how to build from source, see [Building from source]({{ site.baseurl }}/en/doc/installation/install_1_2/java_1_2/build_source_java_1_2).

### Create deb / rpm package

Creation of deb packages for Ubuntu, Debian and Fedora rpm packages from jar files and samples is now officially supported. <br>
You can create a package by following the steps below. When creating a package, use the batch installation script (pkg_install _ ***. Sh) to install the necessary packages in advance.
 $ tar xvzf OpenRTM-aist-Java-1.2.1.tar.gz
 $ unzip OpenRTM-aist-Java-1.2.1-jar.zip
 $ cd OpenRTM-aist/1.2/
 $ cp -r ../../OpenRTM-aist-Java/packages.

 When creating a deb package
 $ cd packages/deb
 $ sh dpkg_build.sh

 When creating an rpm package
 $ cd packages/rpm
 $ sh rpm_build.sh

Packages are created in the pacakges directory.

<span style="color:red;">* Install tools such as "dpkg-dev build-essential debhelper devscripts" when creating deb packages on Ubuntu and Debian, and "rpm-build createrepo" before creating rpm packages on Fedora. Must be kept. </span>;
These can be installed by executing [batch installation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script) with the -c option.

## Release notes
- [1.2.1-RELEASE](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/tag/v1.2.1)

### Supported (build verified) OS
- Ubuntu 16.04 i386, amd64
- Ubuntu 18.04 amd64
- Raspbian Buster armhf
- Windows-10 (32 / 64bit)

