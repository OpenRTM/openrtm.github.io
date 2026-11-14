---
layout: page
title: installing rtcs for raspberry pi mouse (raspbian)
---

<!-- Title: Installing RTCs for Raspberry Pi Mouse (Raspbian) -->
#contents

# RaspberryPiMouseRTC

RaspberryPiMouseRTC is an RT-Component for controlling Raspberry Pi Mouse, developed by the Robot System Design Laboratory at Meijo University.

It can be installed using the following commands:

```bash
 git clone https://github.com/rsdlab/RaspberryPiMouseRTC.git
 cd RaspberryPiMouseRTC
 cmake .
 make
```

Install the following RTCs as needed.

# RaspberryPiMouseController_DistanceSensor

This RTC generates obstacle-avoidance behavior by rotating the Raspberry Pi Mouse when its distance sensors detect an obstacle.

It can be installed using the following commands:

```bash
 git clone https://github.com/Nobu19800/RaspberryPiMouseController_DistanceSensor
 cd RaspberryPiMouseController_DistanceSensor
 cmake .
 make
```

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseController_DistanceSensor_comp.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseController_DistanceSensor_comp.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">RaspberryPiMouseController_DistanceSensor</th>
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
    <td>target_velocity_in</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Target velocity before correction</td>
  </tr>
  <tr>
    <td>distance_sensor</td>
    <td>RTC::TimedShortSeq</td>
    <td>Distance sensor measurements</td>
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
    <td>target_velocity_out</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Target velocity after correction</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">Configuration Parameters</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>Default Value</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>sensor_limit</td>
    <td>10</td>
    <td>Distance sensor threshold that triggers avoidance behavior</td>
  </tr>
  <tr>
    <td>rotational_speed</td>
    <td>1.6</td>
    <td>Speed of avoidance rotation</td>
  </tr>
  <tr>
    <td>stop_velocity</td>
    <td>0.01</td>
    <td>Forward velocity threshold used to determine whether the robot is stopped</td>
  </tr>
</table>

# RaspberryPiMouseController_Joystick

This RTC controls the Raspberry Pi Mouse in a specified direction using a joystick.

*This RTC requires an orientation-sensing RTC such as NineAxisSensor_RT_USB described below.*

It can be installed using the following commands:

```bash
 git clone https://github.com/Nobu19800/RaspberryPiMouseController_Joystick
 cd RaspberryPiMouseController_Joystick
 cmake .
 make
```

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseController_Joystick_comp.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseController_Joystick_comp.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">RaspberryPiMouseController_Joystick</th>
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
    <td>joystick_float</td>
    <td>RTC::TimedFloatSeq</td>
    <td>Joystick input</td>
  </tr>
  <tr>
    <td>joystick_long</td>
    <td>RTC::TimedFloatSeq</td>
    <td>Joystick input</td>
  </tr>
  <tr>
    <td>orientation</td>
    <td>RTC::TimedOrientation3D</td>
    <td>Orientation measured by sensors</td>
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
    <td>out</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Target velocity</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">Configuration Parameters</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>Default Value</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>forward_factor</td>
    <td>0.01</td>
    <td>Forward velocity scaling factor applied to joystick input</td>
  </tr>
  <tr>
    <td>tangential_factor</td>
    <td>1.0</td>
    <td>Rotational velocity scaling factor applied to joystick input</td>
  </tr>
  <tr>
    <td>x_reverse</td>
    <td>0</td>
    <td>Reverse the joystick X coordinate when set to 1</td>
  </tr>
  <tr>
    <td>m_y_reverse</td>
    <td>0</td>
    <td>Reverse the joystick Y coordinate when set to 1</td>
  </tr>
</table>

# NineAxisSensor_RT_USB

This RTC outputs measurement data from the [USB 9-Axis IMU Sensor Module](http://www.rt-shop.jp/blog/archives/7238) sold by RT Corporation.

It can be installed using the following commands:

```bash
 git clone https://github.com/Nobu19800/NineAxisSensor_RT_USB
 cd NineAxisSensor_RT_USB
 cmake .
 make
```

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/NineAxisSensor_RT_USB_comp.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/NineAxisSensor_RT_USB_comp.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">NineAxisSensor_RT_USB</th>
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
    <td>acc</td>
    <td>RTC::TimedAcceleration3D</td>
    <td>Accelerometer measurements</td>
  </tr>
  <tr>
    <td>magn</td>
    <td>RTC::TimedDoubleSeq</td>
    <td>Geomagnetic sensor measurements</td>
  </tr>
  <tr>
    <td>gyro</td>
    <td>RTC::TimedAngularVelocity3D</td>
    <td>Gyroscope measurements</td>
  </tr>
  <tr>
    <td>temp</td>
    <td>RTC::TimedDouble</td>
    <td>Temperature sensor measurements</td>
  </tr>
  <tr>
    <td>rot</td>
    <td>RTC::TimedOrientation3D</td>
    <td>Orientation</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">Configuration Parameters</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>Default Value</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>rotOffset</td>
    <td>0</td>
    <td>Orientation offset (adjust when 0 [rad] should represent a direction other than north)</td>
  </tr>
  <tr>
    <td>magnOffsetX</td>
    <td>-65</td>
    <td>Geomagnetic sensor offset (X-axis)</td>
  </tr>
  <tr>
    <td>magnOffsetY</td>
    <td>-60</td>
    <td>Geomagnetic sensor offset (Y-axis)</td>
  </tr>
  <tr>
    <td>magnOffsetZ</td>
    <td>-5</td>
    <td>Geomagnetic sensor offset (Z-axis)</td>
  </tr>
  <tr>
    <td>serial_port</td>
    <td>COM3 (Windows), /dev/ttyACM0 (Linux)</td>
    <td>Device file name</td>
  </tr>
</table>

Calibration software for the geomagnetic sensor can be installed using the following commands:

```bash
 git clone https://github.com/Nobu19800/CalibrationUSBNineAxisSensor
 cd CalibrationUSBNineAxisSensor
 cmake .
 make
```

When executed, the software starts a 10-second countdown.

During this time, rotate the sensor through various orientations.

If possible, perform a figure-eight motion similar to the compass calibration procedure used on smartphones.

At the end of the process, calibration values for the X, Y, and Z geomagnetic sensor axes will be displayed.

Multiply each value by -1 and apply the results to the corresponding configuration parameters of `NineAxisSensor_RT_USB`.

If the sensor is later mounted on a robot or its installation conditions change, perform calibration again.

# Batch Installation

The RTCs listed above can be installed all at once.

Run the following commands:

```bash
 git clone https://github.com/Nobu19800/RaspberryPiMouseRTSystem_script_Raspbian
 cd RaspberryPiMouseRTSystem_script_Raspbian
 sh Component/install_rtc.sh
```

This installs each RTC into the `Component` directory of `RaspberryPiMouseRTSystem_script_Raspbian`.

*The calibration software is not installed automatically and must be installed manually.*


