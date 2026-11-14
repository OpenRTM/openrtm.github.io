---
layout: page
title: raspberry pi mouse use cases
---

<!-- Title: Raspberry Pi Mouse Use Cases -->
<!-- #contents -->

Raspberry Pi Mouse (hereafter referred to as "RasPiMouse") is a two-wheeled mobile robot sold by RT Corporation.

Since it is equipped with a Raspberry Pi, development can be performed using Linux (Raspbian) and other environments.

<div align="center"><a href="s_DSC00444.JPG"><img src="s_DSC00444.JPG" width="50%;"></a></div>

This document introduces how to use OpenRTM-aist with RasPiMouse and related topics.

## Specifications

<table class="table-alt">
  <tr>
    <th colspan="2" style="text-align: center;">Raspberry Pi Mouse Specifications</th>
  </tr>
  <tr>
    <td>CPU</td>
    <td>Raspberry Pi 2 Model B</td>
  </tr>
  <tr>
    <td>Motor</td>
    <td>Two ST-42BYG020 stepping motors</td>
  </tr>
  <tr>
    <td>Motor Driver</td>
    <td>Two SLA7070MRPT motor drivers</td>
  </tr>
  <tr>
    <td>Distance Sensor</td>
    <td>Four red LEDs + phototransistors (ST-1K3)</td>
  </tr>
  <tr>
    <td>Red LEDs for Monitoring</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Buzzer</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Switch</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Battery</td>
    <td>One LiPo 3-cell (11.1V) 1000mAh battery</td>
  </tr>
</table>

<hr>

- [Tutorial (Raspberry Pi Mouse)](./raspimouse_tutorial)
- [Tutorial (Raspberry Pi Mouse, RTM Seminar)](./raspimouse_tutorial_rtm_seminar)
- [Tutorial (Raspberry Pi Mouse, Bootcamp Edition)](./raspimouse_tutorial_bootcamp)
- [Initial Setup](./raspimouse_init)
- [Operation Check](./raspimouse_test)
- [Installing RTCs for Raspberry Pi Mouse (Raspbian)](./raspimouse_rtc_on_raspbian)
- [Installing RTCs for Raspberry Pi Mouse (Windows)](./raspimouse_rtc_on_windows)
- [Running Sample RT Systems]({{ site.baseurl }}/en/content/sample_system_raspimouse)
- [Control Using Custom RTCs]({{ site.baseurl }}/en/content/rtc_create_raspimouse)
- [Supplementary Information](./raspimouse_appendix)
- [Using the Simulator](./raspimouse_simulator_use)
- [Compilation Method (Ubuntu, CMake, Using Code::Blocks)]({{ site.baseurl }}/en/content/build_ubuntu_codeblocks)


