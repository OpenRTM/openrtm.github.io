---
layout: page
title: installing rtcs for raspberry pi mouse (windows)
---

<!-- Title: Installing RTCs for Raspberry Pi Mouse (Windows) -->
#contents

# Script Files

These are script files for automating RTC startup and RT system restoration.

Download them from [here](https://github.com/Nobu19800/RaspberryPiMouseRTSystem_script/archive/master.zip).

# RaspberryPiMouseGUI

This is a GUI for operating Raspberry Pi Mouse.

It is included in the file downloaded in the Script Files section.

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseGUI/RaspberryPiMouseGUI.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseGUI/RaspberryPiMouseGUI.png" width="60%;"></a></div>

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseGUI_comp.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseGUI_comp.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">RaspberryPiMouseGUI</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>Data Type</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>current_velocity</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Current velocity</td>
  </tr>
  <tr>
    <td>current_pose</td>
    <td>RTC::TimedPose2D</td>
    <td>Current position and orientation</td>
  </tr>
  <tr>
    <td>distance_sensor</td>
    <td>RTC::TimedShortSeq</td>
    <td>Distance sensor measurements</td>
  </tr>
  <tr>
    <td>orientation</td>
    <td>RTC::TimedOrientation3D</td>
    <td>Current orientation</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>Data Type</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>target_velocity</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Target velocity</td>
  </tr>
  <tr>
    <td>target_position</td>
    <td>RTC::TimedPoint2D</td>
    <td>Target position (unused)</td>
  </tr>
  <tr>
    <td>update_pose</td>
    <td>RTC::TimedPose2D</td>
    <td>Position reset</td>
  </tr>
</table>

