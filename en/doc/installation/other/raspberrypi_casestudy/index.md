---
layout: page
title: openrtm-aist use cases on raspberry pi
---

<!-- Title: OpenRTM-aist Use Cases on Raspberry Pi -->

<div align="right"><a href="Raspberry_Pi_Logo.svg_.png"><img src="Raspberry_Pi_Logo.svg_.png" width="5%; margin:10px;" align="right"></a></div>

## Introduction

Raspberry Pi is a single-board computer developed by the Raspberry Pi Foundation in the United Kingdom and is based on ARM processors.

Despite its compact embedded-board form factor, Raspberry Pi can run standard ARM versions of Linux distributions (Debian, Fedora, Arch Linux) as well as FreeBSD. Since it supports native compilation directly on the board, it is very easy to use.

Storage is provided via inexpensive, high-capacity SD cards, and the board itself is also very affordable, costing around 3,000 yen.

In addition, Raspberry Pi provides a variety of basic I/O interfaces and can connect to numerous external devices, making it suitable for applications such as robot control, sensor measurement, and many other embedded and robotics projects.

### Specifications

The appearance of a Raspberry Pi is shown below.

<div align="center"><a href="raspberrypi.png"><img src="raspberrypi.png" width="50%;"></a></div>
<div align="center"><strong>Raspberry Pi</strong></div>

Raspberry Pi is available in three primary categories (Model A, Model B, and Model Zero), with multiple variations within each category. For details, refer to the Wikipedia page below.

- Wikipedia: http://ja.wikipedia.org/wiki/Raspberry_Pi

Representative model specifications are shown below.

<table class="table-alt">
  <tr>
    <td colspan="4" style="text-align: center;">Specifications</td>
  </tr>
  <tr>
    <td></td>
    <td>3 Model B</td>
    <td>3 Model B+</td>
    <td>4 Model B (4 GB)</td>
  </tr>
  <tr>
    <td>Target Price</td>
    <td>$35</td>
    <td>$35</td>
    <td>$55</td>
  </tr>
  <tr>
    <td>SoC</td>
    <td>Broadcom BCM2837</td>
    <td>Broadcom BCM2837B0</td>
    <td>Broadcom BCM2711</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>ARM Cortex-A53 1.2 GHz</td>
    <td>ARM Cortex-A53 1.4 GHz</td>
    <td>ARM Cortex-A72 1.5 GHz</td>
  </tr>
  <tr>
    <td>GPU</td>
    <td colspan="2" style="text-align: center;">Broadcom VideoCore IV</td>
    <td>Broadcom VideoCore VI</td>
  </tr>
  <tr>
    <td>Memory (SDRAM)</td>
    <td colspan="2" style="text-align: center;">1 GB (shared with GPU)</td>
    <td>4 GB (shared with GPU)</td>
  </tr>
  <tr>
    <td>USB 2.0 Ports</td>
    <td>4 (integrated USB hub)</td>
    <td>4</td>
    <td>2</td>
  </tr>
  <tr>
    <td>USB 3.0 Ports</td>
    <td colspan="2" style="text-align: center;">-</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Video Output</td>
    <td colspan="2" style="text-align: center;">Composite RCA (PAL & NTSC), HDMI (rev 1.3 & 1.4), MIPI DSI</td>
    <td>Composite RCA (PAL/NTSC), dual micro-HDMI 2.0 (up to 4Kp60), MIPI DSI</td>
  </tr>
  <tr>
    <td>Audio Output</td>
    <td colspan="2" style="text-align: center;">3.5 mm jack, I2S, HDMI</td>
    <td>3.5 mm jack, I2S, micro HDMI</td>
  </tr>
  <tr>
    <td>Storage</td>
    <td colspan="3" style="text-align: center;">SD Memory Card / MMC / SDIO card slot</td>
  </tr>
  <tr>
    <td>Networking</td>
    <td>10/100 Mbps Ethernet (RJ45)</td>
    <td>Gigabit Ethernet over USB 2.0 (maximum throughput 300 Mbps) (RJ45)</td>
    <td>Gigabit Ethernet (RJ45)</td>
  </tr>
  <tr>
    <td>Low-Level Peripherals</td>
    <td colspan="3" style="text-align: center;">8 × GPIO, UART, I2C, SPI with two chip selects, +3.3V, +5V, Ground</td>
  </tr>
  <tr>
    <td>Power</td>
    <td colspan="2" style="text-align: center;">2.5 A (12.5 W)</td>
    <td>3 A (15 W)</td>
  </tr>
  <tr>
    <td>Power Source</td>
    <td colspan="2" style="text-align: center;">5 V via microUSB or GPIO</td>
    <td>5 V via USB Type-C or GPIO</td>
  </tr>
  <tr>
    <td>Dimensions</td>
    <td>85.0 mm × 56.5 mm</td>
    <td colspan="2" style="text-align: center;">85.0 mm × 56.0 mm</td>
  </tr>
</table>

For more detailed specifications, please refer to the Wiki page and other related resources.

### Overview of This Book

Using the PiRT-Unit I/O expansion board developed by AIST, I/O devices can be utilized relatively easily.

<div align="center"><a href="pirt-unit.png"><img src="pirt-unit.png" width="70%;"></a></div>
<div align="center"><strong>PiRT-Unit</strong></div>

OpenRTM-aist (C++, Python, and Java editions) can be compiled and executed directly on Raspberry Pi. As a result, despite being an embedded platform, it can be used in much the same way as a standard Linux PC development environment.

This guide explains:

- How to build a development environment for OpenRTM-aist
- Useful tips and operational know-how
- Methods for controlling mobile robots
- Techniques for utilizing I/O devices
- Development and execution of RT Components

<div align="center"><a href="pirt-unit_app.png"><img src="pirt-unit_app.png" width="70%;"></a></div>
<div align="center"><strong>Applications Using Raspberry Pi and PiRT-Unit</strong></div>

<hr>

- [Preparing an SD Card](./prep_sdc)
- [Initial Raspberry Pi Configuration](./raspi_init_setting)
- [Using xfinder](./howtouse_xfinder)
- [Installing the Development Environment](./install_development_env)
- [Running Sample Components](./running_sample_comp)
- [I/O Programming with PiRT-Unit](./io_programming_pirt-unit)
- [Controlling the Kobuki Mobile Robot](./control_mobilerobot_kabuki)
- [Adding a Robot Arm to Kobuki](./adding_robotarm_kobuki)
- [Appendix](./appendix)

