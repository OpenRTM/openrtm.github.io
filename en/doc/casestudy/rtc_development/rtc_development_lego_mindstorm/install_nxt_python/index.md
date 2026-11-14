---
layout: page
title: installing nxt python
---

<!-- Title: NXT Python のインストール -->
#contents


# Installing NXT Python


Before creating the NXT RTC, install PyBlues, a module for using Bluetooth from Python, and NXT Python, a module for controlling NXT.
- [PyBlues](http://code.google.com/p/pybluez/)
  - [PyBluez-0.18.win32-py2.4](http://pybluez.googlecode.com/files/PyBluez-0.18.win32-py2.4.exe)
  - [PyBluez-0.18.win32-py2.5](http://pybluez.googlecode.com/files/PyBluez-0.18.win32-py2.5.exe)
  - [PyBluez-0.18.win32-py2.6](http://pybluez.googlecode.com/files/PyBluez-0.18.win32-py2.6.exe)
  - [PyBluez-0.18.tar](http://pybluez.googlecode.com/files/PyBluez-0.18.tar.gz)
- [NXT Python](http://home.comcast.net/`dplau/nxt_python/)`
  - [nxt_python-0.7.zip](http://home.comcast.net/`dplau/nxt_python/download/nxt_python-0.7.zip)`
  - [nxt_python-0.7.tar.gz](http://home.comcast.net/`dplau/nxt_python/download/nxt_python-0.7.tar.gz)`


## Installing PyBlues
Download the Windows installer from the link above.
Run the downloaded executable file to complete the installation.

## Installing NXT Python
Download the zip file from the link above.
NXT Python is installed using the setup.py script.
- If .py files are associated:

setup.py install

- If they are not associated:

c:\Python24\python setup.py install

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\tmp\nxt_python-0.7>setup.py install
running install
running build
running build_py
...
copying build\scripts-2.4\nxt_filer -> c:\python24\Scripts
copying build\scripts-2.4\nxt_push -> c:\python24\Scripts
copying build\scripts-2.4\nxt_test -> c:\python24\Scripts

C:\tmp\nxt_python-0.7>


## Testing NXT Python
With NXT turned ON and connected to the PC, run the samples under example and check whether NXT can be controlled from NXT Python.

The example directory contains the following samples.

- latency.py: Measures the latency of sensor reading.
- mary.py: Plays "Mary Had a Little Lamb" using the NXT sound function.
- message_test.py: Displays a message on the LCD screen of the intelligent block.
- spin.py: Moves the motors on PortB and PortC to make it spin.
- test_sensors.py: Displays the values of all sensors.

When running these tests, they must be executed with the motors, sensors, and other devices used by each sample connected. &aname(miyamoto);
