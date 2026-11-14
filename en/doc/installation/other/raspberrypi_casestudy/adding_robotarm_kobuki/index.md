---
layout: page
title: procedure for mounting a robot arm on kobuki
---

<!-- Title: Procedure for Mounting a Robot Arm on Kobuki -->

#contents

## Academic SCARA Robot

The Academic SCARA Robot is a horizontally articulated robotic arm sold by Vstone for learning robot control.

- https://www.vstone.co.jp/products/scara_robot/

For information about RTCs for controlling the Academic SCARA Robot, refer to:

- [Robot Education Tool Using a Portable RTM Environment Installed on a USB Memory Device]({{ site.baseurl }}/ja/node/5943)(No corresponding English project page available.)

This section explains how to mount the Academic SCARA Robot onto the Kobuki platform.

<br>

<div align="left"><a href="s_DSC00494.JPG"><img src="s_DSC00494.JPG" width="50%;"></a></div>

<br>

The following items are required:

<table class="table-alt">
  <tr>
    <th>Item</th>
    <th>Quantity</th>
  </tr>
  <tr>
    <td>Kobuki</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Plate</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Support posts (5 cm)</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Academic SCARA Robot</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Wood screws (2 cm or longer)</td>
    <td>4</td>
  </tr>
</table>

### Robot Specifications

<table class="table-alt">
  <tr>
    <th colspan="2">Academic SCARA Robot Specifications</th>
  </tr>
  <tr>
    <td>Degrees of Freedom</td>
    <td>4 DOF + Gripper</td>
  </tr>
  <tr>
    <td>Servo Motor</td>
    <td>RS304MD</td>
  </tr>
  <tr>
    <td>Communication Method</td>
    <td>HID USB–UART Bridge</td>
  </tr>
</table>

### Mounting the SCARA Robot Directly to the Plate

This section describes how to mount the SCARA robot directly onto the plate.

First, drill pilot holes in the plate using an awl or similar tool.

Create holes at the positions marked by the red dots below.

<br>

<div align="left"><a href="plate.jpg"><img src="plate.jpg" width="50%;"></a></div>

<br>

Then secure the base of the SCARA robot to the plate using wood screws.

<br>

<div align="left"><a href="s_DSC00511.JPG"><img src="s_DSC00511.JPG" width="50%;"></a></div>

<br>

### Mounting Using the Base

This section explains how to attach the SCARA robot to its base and then mount the base onto the plate.

#### Modifying the Base

To secure the base to the Kobuki plate, drill holes in the robot base.

Drill holes at the locations indicated in red in the figure below. The hole size should match the wood screws you intend to use.

<br>

<div align="left"><a href="s_DSC00493.JPG"><img src="s_DSC00493.JPG" width="70%;"></a></div>

<br>

#### Attaching the Base

First, mount the SCARA robot onto its base.

Install it facing the opposite direction as shown in the figure, and secure it using the thumb screws.

<br>

<div align="left"><a href="s_DSC00492.JPG"><img src="s_DSC00492.JPG" width="70%;"></a></div>

<br>

#### Mounting the Robot

Prepare pilot holes in the plate beforehand using an awl or drill.

Insert wood screws through the holes made in the base and fasten the base to the plate.

<br>

<div align="left"><a href="s_DSC00508.JPG"><img src="s_DSC00508.JPG" width="70%;"></a></div>

<br>

### Installing the Plate

First, attach four support posts to the Kobuki platform.

The laser range sensor and Raspberry Pi should be attached to Kobuki using double-sided tape or a similar method.

<br>

<div align="left"><a href="s_DSC00499.JPG"><img src="s_DSC00499.JPG" width="70%;"></a></div>

<br>

Use support posts created by connecting two 5 cm posts together.

<br>

<div align="left"><a href="s_DSC00496.JPG"><img src="s_DSC00496.JPG" width="70%;"></a></div>

<br>

Finally, place the plate on top and secure it with screws.

<br>

<div align="left"><a href="s_DSC00503.JPG"><img src="s_DSC00503.JPG" width="70%;"></a></div>

<br>

## SainSmart 4-DOF Robot Arm

This section describes how to mount the 4-DOF robot arm sold by SainSmart onto Kobuki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-ky9icPtKZM" frameborder="0" allowfullscreen></iframe>

- http://www.sainsmart.com/diy-4-axis-servos-control-palletizing-robot-arm-model-for-arduino-uno-mega2560.html

For information on RTCs for controlling the 4-DOF robot arm, refer to:

- [RT Components for Educational Robot Arm Control Using RT Middleware]({{ site.baseurl }}/ja/node/5933)(No corresponding English project page available.)

The following items are required:

<table class="table-alt">
  <tr>
    <th>Item</th>
    <th>Quantity</th>
  </tr>
  <tr>
    <td>Kobuki</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Plate</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Support posts (5 cm)</td>
    <td>8</td>
  </tr>
  <tr>
    <td>4-DOF Robot Arm</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Arduino Uno*</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Jumper wires</td>
    <td>15 or more</td>
  </tr>
  <tr>
    <td>Breadboard</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Battery holder (for four AA batteries)</td>
    <td>1</td>
  </tr>
  <tr>
    <td>AA batteries</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Wood screws (2 cm or longer)</td>
    <td>4</td>
  </tr>
</table>

* When controlling from an Intel Edison or Raspberry Pi, a PCA9685-based servo driver may be used instead.

### Robot Specifications

<table class="table-alt">
  <tr>
    <th colspan="2">4-DOF Robot Arm Specifications</th>
  </tr>
  <tr>
    <td>Degrees of Freedom</td>
    <td>4 DOF</td>
  </tr>
  <tr>
    <td>Servo Motors</td>
    <td>MG995, SG90 9G</td>
  </tr>
</table>

### Mounting the Robot

The 4-DOF robot arm already includes mounting holes, so no modification is necessary.

<br>

<div align="center"><a href="arm_4axis.jpg"><img src="arm_4axis.jpg" width="70%;"></a></div>

<br>

Insert wood screws through the mounting holes in the base and fasten the robot arm to the plate.

### Installing the Plate

The procedure is the same as described in the section:

[Academic SCARA Robot Installation Procedure](#土台の取り付け)

