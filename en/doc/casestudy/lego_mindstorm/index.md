---
layout: page
title: lego mindstorms ev3 use cases
---

<!-- Title: LEGO Mindstorms EV3 Use Cases -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * LEGO Mindstorms EV3 Use Cases -->
#contents

LEGO Mindstorms EV3 is a new package in the LEGO Mindstorms series. The main controller of the EV3 comes with Linux preinstalled, enabling robot development in a variety of programming languages.

In the NXT, wireless communication with external devices was basically limited to Bluetooth. The EV3, however, is equipped with a USB interface, allowing communication with external devices over wireless LAN and other networks by connecting a USB Wi-Fi adapter.

With Linux as its operating system, the EV3 enables more flexible and advanced robot development than ever before.

This document introduces how to install OpenRTM-aist on LEGO Mindstorms EV3, use it for robot control, and develop RT Components.

### Specifications

The appearance of the EV3 is shown below.

<div align="center"><a href="ev3.png"><img src="ev3.png" width="60%;"></a></div>
<div align="center"><strong>LEGO Mindstorms EV3</strong></div>

The EV3 computer has the following specifications.

- [Afrel Web Page](http://www.afrel.co.jp/archives/850)

<table class="table-alt">
  <tr>
    <td colspan="2" style="text-align: center;"><strong>LEGO Mindstorms EV3 Specifications</strong></td>
  </tr>
  <tr>
    <td>Processor</td>
    <td>ARM9 300MHz</td>
  </tr>
  <tr>
    <td>Memory (ROM)</td>
    <td>16MB Flash</td>
  </tr>
  <tr>
    <td>Memory (RAM)</td>
    <td>64MB RAM</td>
  </tr>
  <tr>
    <td>OS</td>
    <td>Linux-based</td>
  </tr>
  <tr>
    <td>Display</td>
    <td>178 x 128 pixels</td>
  </tr>
  <tr>
    <td>Output Ports</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Input Ports</td>
    <td>4 <br> Analog <br> Digital 460.8kbit/s</td>
  </tr>
  <tr>
    <td>USB Communication Speed</td>
    <td>High Speed (480Mbps)</td>
  </tr>
  <tr>
    <td>USB Interface</td>
    <td>Supports daisy-chaining EV3 units (up to 4) <br> Supports Wi-Fi communication dongles</td>
  </tr>
  <tr>
    <td>SD Card Slot</td>
    <td>Supports Micro SD cards up to 32GB</td>
  </tr>
  <tr>
    <td>Smart Device Connectivity</td>
    <td>iOS, Android, Windows</td>
  </tr>
  <tr>
    <td>User Interface</td>
    <td>6 buttons, illumination function</td>
  </tr>
  <tr>
    <td>Program Size (Line Tracing Example)</td>
    <td>0.950KB</td>
  </tr>
  <tr>
    <td>Sensor Communication Performance</td>
    <td>1000 times/sec, 1ms</td>
  </tr>
  <tr>
    <td>Data Logging</td>
    <td>Up to 1,000 samples/sec</td>
  </tr>
  <tr>
    <td>Bluetooth Communication</td>
    <td>Can connect to up to 7 slave devices</td>
  </tr>
  <tr>
    <td>Power Supply</td>
    <td>Rechargeable battery pack or six AA batteries</td>
  </tr>
</table>

The EV3 includes a rechargeable battery pack. Its specifications are as follows.

<table class="table-alt">
  <tr>
    <th>Battery Type</th>
    <th>Lithium-ion</th>
  </tr>
  <tr>
    <td>Capacity</td>
    <td>2050mAh</td>
  </tr>
  <tr>
    <td>Compatibility with NXT DC Battery</td>
    <td>No</td>
  </tr>
  <tr>
    <td>Charging with NXT DC Adapter</td>
    <td>Supported</td>
  </tr>
  <tr>
    <td>Comparison with AA Batteries</td>
    <td>The rechargeable DC battery lasts longer than using AA batteries.</td>
  </tr>
  <tr>
    <td>Charging Time</td>
    <td>4 hours (full charge)</td>
  </tr>
</table>

### Overview of This Book

This book explains how to build an environment for developing and running RT Components with OpenRTM-aist, useful techniques for practical use, methods for controlling mobile robots, and how to use I/O devices.

<br>
<hr>

- [Tutorial (EV3)](./lego_tutorial_ev3)
- [Preparing an SD Card](./lego_sdcard_prep)
- [Initial Setup of EV3 and ev3dev](./lego_setup_ev3_ev3dev)
- [Running Sample Components](./lego_samplec_exec)
- [Setting Up the Development Environment](./lego_devenv_make)
- [Using EV3 Devices](./lego_ev3_device_use)
- [Using python-ev3dev](./lego_python-ev3dev_use)
- [Using the EV3 Device C++ Bindings](./lego_ev3dev_cpp_binding)
- [Creating RTCs for EV3 (Python Edition)](./lego_ev3rtc_python)
- [Operating EV3 Devices](./lego_ev3_dev_operation)
- [Installing RTCs for the Educator Vehicle (EV3)](./lego_ev3_rtc_install)
- [Running Sample RT Systems](./lego_sample_rts_exec)
- [Controlling with Your Own RTC](./lego_original_rtc_use)
- [Configuring EV3 as a Wireless LAN Access Point](./lego_ev3_wifi_ap)
- [Using TETRIX](./lego_tetrix_use)
- [Using the Simulator](./lego_simulator_use)
- [Tutorial (RTM Training Course)](./lego_rtm_seminar)
- [Assembly Instructions](./lego_howtobuild)
