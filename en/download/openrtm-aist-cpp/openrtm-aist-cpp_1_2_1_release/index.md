---
layout: page
title: openrtm-aist c++ 1.2.1-release
---

<!-- Title: OpenRTM-aist C++ 1.2.1-RELEASE -->
<div align="right"><a href="cpp_logo.png"><img src="cpp_logo.png" width="10%;" align="right"></a></div>
#contents(4)

(G)Please refer to the following page for the installation procedure.

- [OpenRTM-aist (C ++ version) 1.2 Family installation]({{ site.baseurl }}/en/doc/installation/install_1_2/cpp_1_2)

## Package
### Windows Installer
The msi file is over 900MB in size. Use a high-speed line (50Mbps or more) to download in minutes.

#### For 64bit
<table class="table-alt">
  <tr>
    <td>Windows Installer <br> (including OpenRTM-aist, C ++, Python, <br> Java version and OpenRTP, <br> rtshell (4.2.2)) <br> (Visual Studio 2010, 2012, <br> 2013, 2015, 2017, 2019)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1-RELEASE_x86_64.msi">OpenRTM-aist-1.2.1-RELEASE_x86_64.msi</a> <br> MD5:be6b346d61768435d812cc032bc7a529</td>
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
<!-- - &color (red){* Please delete the old rtshell beforehand. However, if the OpenRTM-aist 1.1.2 version is installed using the msi file, no action is required. }; -->
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [doxygen](http://www.doxygen.nl/index.html) and download and install the latest "doxygen-X.X.X-setup.exe".


#### For 32bit
<table class="table-alt">
  <tr>
    <td>Installer for Windows<br> (OpenRTM-aist、C++、Python、<br>Java version, and OpenRTP、<br>including rtshell(4.2.2))<br>(Visual Studio 2010、2012、<br>2013、2015、2017、2019)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1-RELEASE_x86.msi">OpenRTM-aist-1.2.1-RELEASE_x86.msi</a> <br>MD5:a9186d409cafc039432a0e1c6e7e02ef</td>
    <td>2019/11/25</td>
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

- <span style="color:red;">※Please install one of the version of Python "3.7", "3.6" or "2.7".</span>;
- The above download link may be broken when the latest version of Doxygen is released. In that case, please go to the download page of [doxygen](http: //www.doxygen.nl/index.html) and download and install the latest "doxygen-X.X.X-setup.exe".


##### Confirm installation
It is recommended that you confirm that you can create a Visual C ++ project before the workshop.

First, start Visual Studio and click "File"-> "New"-> "Project". <br>
Select ** Visual C ++ ** for the template and select ** Empty project **.


#ref (vc2017.png, 70%, center)


After entering the project name and clicking OK, a Visual C ++ project is created.

If you cannot select ** Visual C ++ **, install "Desktop development with C ++" according to the procedure of [How to install Visual Studio Community 2019]({{ site.baseurl }}/en/doc/installation/install_1_2/cpp_1_2/install_windows_1_2/visual_studio_1_2/visual_studio_2022/).

Also, when using other than Visual Studio 2019, it is recommended to confirm that you can create a Visual C ++ project just in case.

#### How to use the old version runtime of C ++ version
The old version runtime is installed under the OpenRTM-aist directory as 1.0.0 (only for 32bit), 1.1.0, 1.1.1, 1.1.2, 1.2.0.
Use the system environment variable "RTM_BASE" through the path.

Example) The 1.1.1 version vc12 runtime path can be specified as "% RTM_BASE% \ 1.1.1 \ vc12 \ bin".

#### How to handle when OpenRTP / RTSystemEditor is reduced in high resolution (HiDPI) mode such as Windows10
If you use a high resolution mode such as Windows 10, Eclipse icons etc. may be displayed in a reduced size. The following FAQ explains the solution.
- [On Windows10, etc., in high resolution mode, icons are too small and hard to see](/ja/content/tool_trouble_shooting_ja # toc1)

### Linux package
We currently offer packages in the following distribution versions: <br>
You can use the installation script distributed below to install the required packages at once.

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
    <td>Raspbian Buster</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_raspbian.sh">pkg_install_raspbian.sh</a></td>
  </tr>
</table>

By specifying options, you can now install packages that meet your needs. Please refer to [Bulk installation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script) for installation method, options and package types.

If you have already installed 1.2.0-RELEASE, you can update it.

Ubuntu / Debian
 $ sudo apt-get update
 $ sudo apt-get dist-upgrade

Please see [OpenRTM-aist (C ++ version) 1.2 family installation]({{ site.baseurl }}/en/doc/installation/install_1_2/cpp_1_2) for download method and installation method.

&aname(src);
## Source code

<table class="table-alt">
  <tr>
    <td>C ++ version source code</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1. tar.bz2">OpenRTM-aist-1.2.1.tar.bz2</a> <br> MD5: 890ad85f3d6f6afd7d24d68c4aa6c290</td>
    <td>2019.11.25</td>
  </tr>
  <tr>
    <td>C ++ source code</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1. tar.gz">OpenRTM-aist-1.2.1.tar.gz</a> <br> MD5: dc7075480642017ea228d04c8bde6ca8</td>
    <td>2019.11.25</td>
  </tr>
  <tr>
    <td>C ++ version Windows only source</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.1/OpenRTM-aist-1.2.1 -win32.zip">OpenRTM-aist-1.2.1-win32.zip</a> <br> MD5: 5dd560c1ba2297b048a8a03c8db88632</td>
    <td>2019.11.25</td>
  </tr>
</table>

### Build from source

For details on how to build from source, see [Building from Source (Windows)]({{ site.baseurl }}/en/doc/installation/install_1_2/cpp_1_2/build_source_windows_1_2) or [Building from Source (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/cpp_1_2/build_source_linux_1_2) .

### Create deb / rpm package

From 1.1, the creation of deb packages for Ubuntu and Debian and rpm packages for Fedora from the above source code is officially supported.

You can create a package by following the steps below. When creating a package, use the bulk installation script (pkg_install _ ***. Sh) to install the necessary packages in advance.

 $ tar xvzf OpenRTM-aist-1.2.1-RELEASE.tar.gz
 $ cd OpenRTM-aist-1.2.1
 $ ./configure --prefix = /usr --enable-fluentd = yes --enable-observer = yes --enable-ssl = yes
 $ cd packages
 $ make

Packages are created in the pacakges directory.

<span style="color:red;">* Install tools such as "dpkg-dev build-essential debhelper devscripts" when creating deb packages on Ubuntu and Debian, and "rpm-build createrepo" before creating rpm packages on Fedora. Must be kept. </span>;
These can be installed by executing [Bulk installation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script) with the -c option.

## Release notes
OpenRTM-aist Official Website can use source code, Windows installer, Linux package, etc. in dual license system which can be selected from LGPL license or individual contract with AIST.
- [1.2.1-RELEASE](https://github.com/OpenRTM/OpenRTM-aist/releases/tag/v1.2.1)

### Supported (build verified) OS

- Ubuntu 16.04 i386, amd64
- Ubuntu 18.04 amd64
- Raspbian Buster armhf
- Windows-10 (32 / 64bit)

