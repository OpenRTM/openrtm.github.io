---
layout: page
title: installation
---

<!-- Title: インストール -->

<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="100;" align="right"></a></div>


OpenRTM-aist provides deb packages that can be used on Ubuntu and Debian GNU/Linux.
<!-- ２.０は現在、Debian、Ubuntu、Raspbian OSのディストリビューションに対応しています。 -->


#contents

Version 2.1 currently supports Ubuntu 22.04 and 24.04 (amd64 and arm64).
Please note that the supported versions of Ubuntu/Debian GNU/Linux and platform compatibility are subject to change without prior notice.

## Changes in Version 2.1

You can now install the new [SSM Communication Feature]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ssm_comm_use).<br>
Since the SSM library is statically linked, you do not need to install SSM separately. The following files are installed by the openrtm2-ssm-tp deb package.

```
 usr/
 ├── bin
 │   ├── killssm
 │   ├── lsssm
 │   ├── psssm
 │   ├── ssm-advance-player
 │   ├── ssm-coordinator
 │   ├── ssm-date
 │   ├── ssm-graph
 │   ├── ssm-logger
 │   ├── ssm-monitor
 │   ├── ssm-player
 │   ├── ssm-proxy
 │   ├── ssm-transporter
 │   └── topssm
 ├── etc
 │   └── transport
 │       └── rtc.ssm.conf
 └── share
     └── openrtm-2.1
         └── transport
             └── SSMTransport.so
```

This feature is **not** installed when the "Bulk Installation Script" described in the next section is executed without any options.<br>
It can be installed by specifying the option `-l c++ --ssm`. You can check the available options with `--help`.

## Bulk Installation Script

To install Version 2.0, paste and execute the following command at the shell prompt. It installs the C++ edition, Python edition, Java edition, OpenRTP (amd64 only), rtshell, and JDK 8. The script is not saved locally.<br>
*Even if multiple Java versions are installed by the script, the default Java version is automatically switched to Java 8.*

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

The following packages will be installed.

```
 $ dpkg -l | grep openrt
 ii  openrtm2:arm64                         2.1.0-0             arm64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:arm64                  2.1.0-0              arm64       OpenRTM-aist headers for development
 ii  openrtm2-doc                             2.1.0-0              all             Documentation for openrtm2
 ii  openrtm2-example:arm64            2.1.0-0             arm64       OpenRTM-aist examples
 ii  openrtm2-idl:arm64                     2.1.0-0             arm64       OpenRTM-aist idls for development
 ii  openrtm2-java:arm64                  2.1.0-0             arm64       OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-example:arm64     2.1.0-0            arm64        OpenRTM-aist-Java examples
 ii  openrtm2-naming:arm64              2.1.0-0            arm64        OpenRTM-aist name server launcher
 ii  openrtm2-python3                       2.1.0-0            arm64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-example          2.1.0-0            arm64        OpenRTM-aist-Python examples
```

The installation of rtshell fails when using the default pip version.<br>
Follow the yellow message displayed by the installation script and add the following lines to `/etc/pip.conf` (create the file if it does not exist).

```
 $ vi /etc/pip.conf
 [global]
 break-system-packages = true
```

After applying the above setting, run the installation script again to install rtshell.

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python        2.1.0
 rtctree-aist                       4.2.5
 rtshell-aist                       4.2.10
 rtsprofile-aist                    4.1.6
```

By specifying options, you can install packages that match your requirements. The available options can be checked with the following command.

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) --help
```

For detailed information about the installed packages, see "[Details of OpenRTM-aist-2.1 deb Packages]({{ site.baseurl }}/en/doc/installation/install_2_1/install_linux_2_1/install_debpackages_workcontent_2_1)".

## Installing ROS Packages

In Version 2.1, packages for the ROS communication feature (for ROS2) can be installed.<br>
This section describes how to install the packages in an environment where ROS2 has already been installed.

As described in the help message, the ROS package installation options are as follows.<br>

'''
[-e ros2|all] [--ros2]
'''

If you have already executed the installation script without any options and want to install the ROS2 packages afterward, use the `-l c++ --ros2` option.

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l c++ --ros2
```

If you want to install all packages including the ROS2 packages from the beginning, use the `-l all --ros2` option.

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l all --ros2
```

Verify the installed packages.

```
 $ dpkg -l | grep openrt
 ii  openrtm2:amd64                          2.1.0-0       amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:amd64                    2.1.0-0       amd64        OpenRTM-aist headers for development
 ii  openrtm2-doc                               2.1.0-0       all               Documentation for openrtm2
 ii  openrtm2-example:amd64             2.1.0-0       amd64        OpenRTM-aist examples
 ii  openrtm2-idl:amd64                      2.1.0-0       amd64        OpenRTM-aist idls for development
 ii  openrtm2-java:amd64                   2.1.0-0       amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-example:amd64      2.1.0-0      amd64        OpenRTM-aist-Java examples
 ii  openrtm2-naming:arm64               2.1.0-0      arm64        OpenRTM-aist name server launcher
 ii  openrtm2-python3                         2.1.0-0      amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-example            2.1.0-0      amd64        OpenRTM-aist-Python examples
 ii  openrtm2-ros2-tp:amd64               2.1.0-0      amd64        OpenRTM-aist extension ROS2 package
 ii  openrtp2:amd64                            2.1.0-0      amd64        OpenRTP, Open RT Platform distributed by AIST
```
