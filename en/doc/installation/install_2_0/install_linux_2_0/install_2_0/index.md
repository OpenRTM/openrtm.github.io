---
layout: page
title: install
---
<!-- Title: インストール -->

<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="100;" align="right"></a></div>


OpenRTM-aist provides deb packages that can be used on Ubuntu and Debian GNU Linux.
<!-- ２.０は現在、Debian、Ubuntu、Raspbian OSのディストリビューションに対応しています。 -->


#contents

2.0 currently supports Ubuntu 18.04 and 20.04 (amd64 and arm64 for each).
Please note that supported versions for Ubuntu/Debian GNU Linux and availability of support may change without notice.

## Changes in the 2.0 Series

C++ and OpenRTP can now coexist between the 1.2 series and the 2.0 series. With this support, the following installation-related items have changed.

- The deb package names for the 2.0 series have been changed
- Python and Java cannot coexist between the 1.2 series and the 2.0 series
  - If you use the batch installation script, installed different versions are automatically uninstalled
- The batch installation scripts for the 1.2 series and the 2.0 series have been separated
  - Installation of the 1.2 series: pkg_install_ubuntu.sh
  - Installation of the 2.0 series: openrtm2_install_ubuntu.sh

In addition, the installation scripts (for both the 1.2 series and the 2.0 series) now support batch processing from download to installation.

## Batch Installation Script

To install the 2.0 series, paste the following into the shell prompt and execute it. The C++ version, Python version, Java version, OpenRTP (amd64 only), rtshell, and JDK8 will be installed. The script is not saved locally.<br>
* Even if multiple versions of Java are installed by running the script, it is switched to use Java 8

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

By executing this, the following deb packages and rtshell via pip are installed.

```
 $ dpkg -l | grep openrt
 ii  openrtm2:amd64                          2.0.0-0                  amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:amd64                    2.0.0-0                  amd64        OpenRTM-aist headers for development
 ii  openrtm2-doc                               2.0.0-0                  all               Documentation for openrtm2
 ii  openrtm2-example:amd64             2.0.0-0                  amd64        OpenRTM-aist examples
 ii  openrtm2-idl:amd64                      2.0.0-0                  amd64        OpenRTM-aist idls for development
 ii  openrtm2-java:amd64                   2.0.0-0                  amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-doc                        2.0.0-0                  all               Documentation for openrtm2-java
 ii  openrtm2-java-example:amd64      2.0.0-0                  amd64        OpenRTM-aist-Java examples
 ii  openrtm2-python3                         2.0.0-0                  amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-doc                   2.0.0-0                  all               Documentation for openrtm2-python3
 ii  openrtm2-python3-example            2.0.0-0                  amd64        OpenRTM-aist-Python examples
 ii  openrtp2:amd64                            2.0.0-0                  amd64        OpenRTP, Open RT Platform distributed by AIST
```

&color(fuchsia){On Ubuntu 24.04, rtshell installation fails when using the default pip version. Follow the yellow message displayed by the installation script, add the following to /etc/pip.conf (create it if it does not exist), and then run the installation script again to install it.};

```
 $ vi /etc/pip.conf
 [global]
 break-system-packages = true
```

By specifying options, you can install packages according to your purpose. help can be checked as follows.

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) --help
```

The detailed contents of the installed packages can be checked in "[Detailed Contents of the OpenRTM-aist-2.0 deb Packages]({{ site.baseurl }}/en/doc/installation/install_2_0/install_linux_2_0/install_debpackages_workcontent_2_0)".

## Installing Packages for ROS

In the 2.0 series, packages for ROS communication functions can be installed. (For ROS and ROS2) <br>
This section explains how to install packages in an environment where both ROS and ROS2 are installed.

As described in help, the ROS package installation options are supported as follows.<br>
[-e ros|ros2|all] [--ros|--ros2]

If you have already run the installation script without options and want to additionally install packages for ROS and ROS2, this can be done with "-l c++ -e all".<br>
<span style="color:fuchsia;">In environments of Ubuntu 22.04 or later where only ROS2 is supported, only packages for ROS2 are installed with -e all.</span>;


```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l c++ -e all
```

If you want to install everything including packages for ROS and ROS2 from the beginning, this can be done with "-l all -e all".
```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l all -e all
```

Check the installed packages.

```
 $ dpkg -l | grep openrt
 ii  openrtm2:amd64                          2.0.0-0       amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:amd64                    2.0.0-0       amd64        OpenRTM-aist headers for development
 ii  openrtm2-doc                               2.0.0-0       all               Documentation for openrtm2
 ii  openrtm2-example:amd64             2.0.0-0       amd64        OpenRTM-aist examples
 ii  openrtm2-idl:amd64                      2.0.0-0       amd64        OpenRTM-aist idls for development
 ii  openrtm2-java:amd64                   2.0.0-0       amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-doc                        2.0.0-0       all               Documentation for openrtm2-java
 ii  openrtm2-java-example:amd64      2.0.0-0      amd64        OpenRTM-aist-Java examples
 ii  openrtm2-python3                         2.0.0-0      amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-doc                   2.0.0-0      all               Documentation for openrtm2-python3
 ii  openrtm2-python3-example            2.0.0-0      amd64        OpenRTM-aist-Python examples
 ii  openrtm2-ros-tp:amd64                 2.0.0-0      amd64        OpenRTM-aist extension ROS package
 ii  openrtm2-ros2-tp:amd64               2.0.0-0      amd64        OpenRTM-aist extension ROS2 package
 ii  openrtp2:amd64                            2.0.0-0      amd64        OpenRTP, Open RT Platform distributed by AIST
```

## Installing the 2.0 Series in an Environment Where the 1.2 Series Is Installed

The installation script for the 1.2 series can also be executed by specifying a URL. Install all packages by running the script without options.

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh)
```

Check the installed packages.

```
 $ dpkg -l | grep openrt
 ii  openrtm-aist:amd64                         1.2.2-0
 ii  openrtm-aist-dev:amd64                   1.2.2-0
 ii  openrtm-aist-doc                              1.2.2-0
 ii  openrtm-aist-example:amd64            1.2.2-0
 ii  openrtm-aist-idl:amd64                     1.2.2-0
 ii  openrtm-aist-java:amd64                  1.2.2-0
 ii  openrtm-aist-java-doc                       1.2.2-0
 ii  openrtm-aist-java-example:amd64     1.2.2-0
 ii  openrtm-aist-python3                        1.2.2-0
 ii  openrtm-aist-python3-doc                  1.2.2-0
 ii  openrtm-aist-python3-example           1.2.2-0
 ii  openrtp:amd64                                  1.2.2-4
```

If you then install the 2.0 series, c++ and openrtp from the 1.2 series and the 2.0 series coexist, but only the 2.0 series is installed for java and python.

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

During script execution, you will be asked "Do you want to continue? [Y/n]" regarding the uninstallation of the 1.2 series java and python packages, so press the Enter key. <br>
Check the installed packages.

```
 $ dpkg -l | grep openrt
 ii  openrtm-aist:amd64                         1.2.2-0
 ii  openrtm-aist-dev:amd64                   1.2.2-0
 ii  openrtm-aist-doc                              1.2.2-0
 ii  openrtm-aist-example:amd64            1.2.2-0
 ii  openrtm-aist-idl:amd64                     1.2.2-0
 ii  openrtm2:amd64                              2.0.0-0
 ii  openrtm2-dev:amd64                        2.0.0-0
 ii  openrtm2-doc                                   2.0.0-0
 ii  openrtm2-example:amd64                 2.0.0-0
 ii  openrtm2-idl:amd64                          2.0.0-0
 ii  openrtm2-java:amd64                        2.0.0-0
 ii  openrtm2-java-doc                             2.0.0-0
 ii  openrtm2-java-example:amd64           2.0.0-0
 ii  openrtm2-python3                              2.0.0-0
 ii  openrtm2-python3-doc                       2.0.0-0
 ii  openrtm2-python3-example                2.0.0-0
 ii  openrtp:amd64                                  1.2.2-4
 ii  openrtp2:amd64                                2.0.0-0
```

Along with this, rtshell is also reinstalled.

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python    2.0.0
 rtctree-aist           4.2.3
 rtshell-aist           4.2.9
 rtsprofile-aist        4.1.5
```

## Installing the 1.2 Series in an Environment Where the 2.0 Series Is Installed

c++ and openrtp from the 1.2 series and the 2.0 series coexist, but only the 1.2 series is installed for java and python. 

```
 $ dpkg -l | grep openrt
 ii  openrtm-aist:amd64                        1.2.2-0
 ii  openrtm-aist-dev:amd64                 1.2.2-0
 ii  openrtm-aist-doc                             1.2.2-0
 ii  openrtm-aist-example:amd64           1.2.2-0
 ii  openrtm-aist-idl:amd64                    1.2.2-0
 ii  openrtm-aist-java:amd64                 1.2.2-0
 ii  openrtm-aist-java-doc                      1.2.2-0
 ii  openrtm-aist-java-example:amd64    1.2.2-0
 ii  openrtm-aist-python3                       1.2.2-0
 ii  openrtm-aist-python3-doc                 1.2.2-0
 ii  openrtm-aist-python3-example          1.2.2-0
 ii  openrtm2:amd64                             2.0.0-0
 ii  openrtm2-dev:amd64                       2.0.0-0
 ii  openrtm2-doc                                  2.0.0-0
 ii  openrtm2-example:amd64                2.0.0-0
 ii  openrtm2-idl:amd64                         2.0.0-0
 ii  openrtp:amd64                                1.2.2-4
 ii  openrtp2:amd64                             2.0.0-0
```

rtshell is also reinstalled for OpenRTM-aist-Python 1.2.2.

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python    1.2.2
 rtctree-aist           4.2.3
 rtshell-aist           4.2.9
 rtsprofile-aist        4.1.5
```
