---
layout: page
title: initial setup
---

<!-- Title: Initial Setup -->
#contents

# Raspbian

Follow the instructions on [this page]({{ site.baseurl }}/en/doc/installation/other/raspberrypi_casestudy/prep_sdc) to write Raspbian to an SD card.

*If you are using the SD card included with the full kit, this step is not required.*

# Assembly

First, insert the SD card into the Raspberry Pi.

Once assembled, the SD card cannot be replaced unless the Raspberry Pi is removed.

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm2.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm2.png" width="70%;"></a></div>

Next, mount the Raspberry Pi onto the Raspberry Pi Mouse body.

Secure the Raspberry Pi to the spacers using the included screws.

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm0.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm0.png" width="70%;"></a></div>

Finally, connect the supplied board to the pin headers on both the Raspberry Pi and the Raspberry Pi Mouse body to complete the assembly.

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm1.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm1.png" width="70%;"></a></div>

# Starting Raspbian

The following procedures are performed after booting Raspbian.

First, connect a display, mouse, keyboard, and LAN cable to the Raspberry Pi.

The Raspberry Pi Mouse can be powered not only by the battery but also from an AC outlet using the included power cable. However, be careful about the orientation of the connector when connecting it to the Raspberry Pi Mouse.

The Raspberry Pi Mouse power switches are located as shown below.

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm8.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm8.png" width="70%;"></a></div>

The front switch controls the motor power, and the inner switch controls the Raspberry Pi power.

Turn the inner switch ON.

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm9.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm9.png" width="70%;"></a></div>

Once Raspbian has started, log in using:

- Username: `pi`
- Password: `raspberry`

After logging in, start X Window with the following command:

```bash
 startx
```

# Device Driver

After Raspbian starts, clone the repository using the following command:

```bash
 git clone https://github.com/rt-net/RaspberryPiMouse.git
```

*If git is not installed, install it first with the following command:*

```bash
 sudo apt-get install git
```

Next, check the kernel version with:

```bash
 uname -r
```

For example, if you are using a Raspberry Pi 2 Model B with kernel version `4.1.6-v7+`, load the kernel module using:

```bash
 cd RaspberryPiMouse/lib/Pi2B+/4.1.6-v7+/
 sudo insmod rtmouse.ko
```

If the SPI interface is not enabled, enable it using the following command or from:

```text
[Menu] > [Preferences] > [Raspberry Pi Configuration]
```

```bash
 sudo raspi-config
```

Use the arrow keys to select **Advanced Options** and press Enter.

Next, select **A5 SPI** using the same procedure.

Then select **Yes** using the left/right arrow keys and press Enter on **OK** to enable SPI.

After returning to the main screen, select **Finish** with the left/right arrow keys and exit.

For more details, refer to [this page](http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/).

*If you are using the SD card included with the full kit, this step is not required.*

# OpenRTM-aist

# C++ Version

To install the C++ version of OpenRTM-aist on Raspbian, run the following commands:

```bash
 wget http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_debian.sh
 sudo sh pkg_install_debian.sh
```

For more information, refer to [this page]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/install_rasbian_1_1).

*The host PC is assumed to be running Windows.*

For instructions on installing OpenRTM-aist on Windows, refer to [this page]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1).

Since the sample RT systems also use Python-based sample components, install the Python version as well.

In addition, the sample RT systems use `rtshell`, so install it by following the instructions on [this page]({{ site.baseurl }}/en/doc/old_documents/install_rtshell).

# Python Version

To install the Python version, first run the following commands:

```bash
 wget http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_debian.sh
 sudo sh pkg_install_python_debian.sh
```
