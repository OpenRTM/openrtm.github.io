---
layout: page
title: system settings for pirt-unit
---

<!-- Title: PiRT-Unitのためのシステム設定 -->
#contents

With the default settings of Raspberry Pi (raspbian armhf), SPI devices and other devices cannot be used.
Here, we configure the devices required to use PiRT-Unit and set up the programming environment.

## Setup Script

A script containing the following setup is available here.

- Setup script: [http://svn.openrtm.org/Embedded/trunk/RaspberryPi/tools/rpi.sh](http://svn.openrtm.org/Embedded/trunk/RaspberryPi/tools/rpi.sh)

Download it to an appropriate location in the image downloaded from the Raspberry Pi website and execute it as follows.

```
$ wget http://svn.openrtm.org/Embedded/trunk/RaspberryPi/tools/rpi.sh
$ chmod 755 rpi.sh
$ sudo rpi.sh rtunit0 --type rtunit
$ sudo rpi.sh rtunit0 --type rtunit_examples
```


This automatically performs the settings, package installation, and sample installation required to use PiRT-Unit as described below.
If errors occur due to version upgrades, changes in file locations, or other reasons, please notify us via the mailing list or similar means.

### rpi.sh Help


This automatically performs the settings, package installation, and sample installation required to use PiRT-Unit as described below.
If errors occur due to version upgrades, changes in file locations, or other reasons, please notify us via the mailing list or similar means.

### rpi.sh Help

```
Usage: rpi.sh hostname --type <TYPE>

TYPE are: basic kobuki kobuki_only rtunit rtunit_only
basic: Installing avahi, cmake, subversion/git and OpenRTM
kobuki: Installing basic + Kobuki RTC
kobuki_only: Installing Kobuki RTC only
rtunit: Installing basic + spi/i2c tools and modules
rtunit_only: Installing spi/i2c tools and modules only
rtunit_examples: Installing basic + PiRT-Unit examples

EXAMPLE:

Just change hostname
rpi.sh kobuki0
Basic setup: Installing OpenRTM-aist (C++/Python)
rpi.sh kobuki --type basic

"
3) Kobuki setup: Installing OpenRTM-aist (C++/Python) and Kobuki RTC

rpi.sh kobuki --type kobuki

```

## Changing System Configuration Files

The method for loading the spi and i2c device modules changed from kernel 3.18. It appears that Raspbian, the OS for Raspberry Pi, applies to this from the 2015 version onward, but check the kernel version to determine this.<br>
To use spi and i2c, enable them with raspi-config. See the [Initial Settings for Raspberry Pi]({{ site.baseurl }}/en/doc/installation/other/raspberrypi_casestudy/raspi_init_setting) page.

For versions older than this, configure the following files.

### Editing raspi-blacklist.conf

The following two lines are set in /etc/modprobe.d/raspi-blacklist.conf.

```
blacklist spi-bcm2708
blacklist i2c-bcm2708

```

Comment them out.


```
blacklist spi and i2c by default (many users don't need them)

#blacklist spi-bcm2708
#blacklist i2c-bcm2708

```

This allows the spi and i2c device modules to be loaded.

### Setting udev rules

Even if the spi and i2c device modules are loaded, by default they are configured with permissions that prevent access by general users.
Since this is somewhat inconvenient, configure them so that anyone can access them when the devices are created.
Create a new file named /etc/udev/rules.d/50-udev.rules and add the following line to it.


```
KERNEL=="spidev*", SUBSYSTEM=="spidev", GROUP="spi", MODE="0666"

```

This completes the preparation.


<!-- ============================================================ -->
## Installing Python Extension Modules

In PiRT-Unit, AD and DA are connected via SPI, and by installing a Python module for controlling SPI devices, AD and DA can be used easily from Python.

### Preparation

To use AD and DA via SPI from Python, install the following extension modules.

- WiringPi-Python:[https://github.com/WiringPi/WiringPi-Python.git](https://github.com/WiringPi/WiringPi-Python.git)
  - wiringPi: git[https://git.drogon.net/wiringPi](https://git.drogon.net/wiringPi)
- py-spidev:[https://raw.github.com/doceme/py-spidev](https://raw.github.com/doceme/py-spidev)

Install the following packages for preparation.

- python-dev
- git-core
- i2c-tools
- python-smbus
- python-setuptools


```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-dev git-core i2c-tools python-smbus
```

### Installing py-spidev

py-spidev is available on github at https://raw.github.com/doceme/py-spidev. Install it as follows.


```
$ cd ~ (or 適当なディレクトリー)
$ git clone git://github.com/doceme/py-spidev
$ cd py-spidev
$ chmod 755 setup.py
$ sudo ./setup.py install
```


This makes the Python module py-spidev available.
Try using the spidev module.

```
$ sudo python
sudo: unable to resolve host raspbian-armhf
Python 2.7.3 (default, Jan 13 2013, 11:20:46)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

 >>> import spidev
 >>> spi = spidev.SpiDev()
 >>> spi.open(0,0)
 >>> print spi.xfer2([0x00,0,0,0])

```

This reads and prints the value from the AD converter on CN2. The AD converter (ADC104S021) is a 10-bit single-ended type, and its maximum sampling rate is 200 kHz. (This does not guarantee a 200 kHz sampling rate on Linux.)
In practice, the voltage measured is the value output by "spi.xfer2([0x00],0,0,0])" divided by 1024 (bit) and multiplied by 5.0 (V).

```
 >>> r = spi.xfer2([0x00,0,0,0])
 >>> print r[0] * 5.0 / 1024.0, " [V]"
```

If you can execute everything up to this point without errors, the spidev module has been installed correctly.

### Installing WiringPi-Python

WiringPi-Python is a module for using WiringPi, a tool for controlling GPIO, from Python.
First, install WiringPi.

```
$ git clone git://git.drogon.net/wiringPi
$ cd cd wiringPi
$ git pull origin
$ ./build
```

Next, install WiringPi-Python itself as follows.

```
$ sudo apt-get install python-dev
$ git clone https://github.com/WiringPi/WiringPi-Python.git
$ cd WiringPi-Python
$ git submodule update --init
$ sudo python setup.py install
```

This completes the installation of the required modules.
