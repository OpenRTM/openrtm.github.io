---
layout: page
title: installing rtcs for the educator vehicle (ev3)
---

<!-- Installing RTCs for the Educator Vehicle (EV3) -->
#contents

This page explains how to install the various RTCs used to control the Educator Vehicle.

## EducatorVehicle

EducatorVehicle is a component for controlling the driving speed of the EV3 and outputting sensor data.

- [https://github.com/Nobu19800/EducatorVehicle](https://github.com/Nobu19800/EducatorVehicle)

Enter the following commands in the cross-development environment.

```

git clone https://github.com/Nobu19800/EducatorVehicle
cd EducatorVehicle
cmake .
make

```

Transfer the generated `src/EducatorVehicleComp` to the EV3.

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">EducatorVehicle</th>
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
    <td>velocity2D</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Target velocity</td>
  </tr>
  <tr>
    <td>angle</td>
    <td>RTC::TimedDouble</td>
    <td>Motor M angle</td>
  </tr>
  <tr>
    <td>lcd</td>
    <td>RTC::CameraImage</td>
    <td>Image data to be displayed on the LCD</td>
  </tr>
  <tr>
    <td>sound</td>
    <td>RTC::TimedString</td>
    <td>Audio output</td>
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
    <td>odometry</td>
    <td>RTC::TimedPose2D</td>
    <td>Current position and orientation</td>
  </tr>
  <tr>
    <td>current_vel</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Current velocity and angular velocity</td>
  </tr>
  <tr>
    <td>ultrasonic</td>
    <td>RTC::RangeData</td>
    <td>Distance measured by the ultrasonic sensor</td>
  </tr>
  <tr>
    <td>gyro</td>
    <td>RTC::TimedDouble</td>
    <td>Angle measured by the gyro sensor</td>
  </tr>
  <tr>
    <td>color</td>
    <td>RTC::TimedString</td>
    <td>Color measured by the color sensor</td>
  </tr>
  <tr>
    <td>light_reflect</td>
    <td>RTC::TimedDouble</td>
    <td>Reflected light intensity measured by the color sensor</td>
  </tr>
  <tr>
    <td>touch</td>
    <td>RTC::TimedBoolean</td>
    <td>Touch sensor ON/OFF state. The right sensor corresponds to element 0, and the left sensor corresponds to element 1.</td>
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
    <td>wheelRadius</td>
    <td>0.028</td>
    <td>Wheel radius</td>
  </tr>
  <tr>
    <td>wheelDistance</td>
    <td>0.054</td>
    <td>Half the distance between the wheels</td>
  </tr>
  <tr>
    <td>medium_motor_speed</td>
    <td>1.6</td>
    <td>Speed of Motor M</td>
  </tr>
</table>

<div align="center"><a href="simulator_ev3_2.png"><img src="simulator_ev3_2.png" width="50%;"></a></div>

### Touch Sensor Output

For the data received through `touch`, element 0 corresponds to the right touch sensor (Port 3), and element 1 corresponds to the left touch sensor (Port 1).

### Audio Output

The following commands can be used as input to the `sound` port.

- beep
  - Entering `beep` produces a beep sound.

- tone
  - Enter `tone`, followed by a frequency and duration, as shown below, to play a tone at the specified frequency for the specified number of milliseconds.

```

tone,100,1000

```

- Other strings
  - Any other string will be spoken using text-to-speech.

### Images Displayed on the LCD

Image files can be converted by dragging and dropping them onto `saveBinaryImage.exe`.

The image data displayed on the LCD can be supplied after conversion using the following component.

When using Windows, start it using `ImageConversionLCDComp.exe` in the release folder.

- [https://github.com/Nobu19800/ImageConversionLCD](https://github.com/Nobu19800/ImageConversionLCD)

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">ImageConversionLCD</th>
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
    <td>out</td>
    <td>RTC::CameraImage</td>
    <td>Image data before conversion</td>
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
    <td>RTC::CameraImage</td>
    <td>Converted image data</td>
  </tr>
</table>

<div align="center"><a href="ImageConversionLCD.png"><img src="ImageConversionLCD.png" width="70%;"></a></div>

For example, by connecting it to the OpenRTM-aist sample component **OpenCVCamera**, camera images can be displayed on the EV3 LCD.

<div align="center"><a href="system_lcd.png"><img src="system_lcd.png" width="60%;"></a></div>

<div align="center"><a href="s_DSC00796.JPG"><img src="s_DSC00796.JPG" width="50%;"></a></div>

Alternatively, a specific image can be displayed.

<div align="center"><a href="s_DSC00797.JPG"><img src="s_DSC00797.JPG" width="50%;"></a></div>
<br>

<div align="center"><a href="s_DSC00798.JPG"><img src="s_DSC00798.JPG" width="50%;"></a></div>

## ControlEducatorVehicle

ControlEducatorVehicle can be used to control the following mobile robot (modified Educator Vehicle). Refer to [this page]({{ site.baseurl }}/en/doc/casestudy/lego_mindstorm/lego_howtobuild) for assembly instructions.

- [https://github.com/Nobu19800/ControlEducatorVehicle](https://github.com/Nobu19800/ControlEducatorVehicle)

<div align="center"><a href="s_DSC00443.JPG"><img src="s_DSC00443.JPG" width="50%;"></a></div>
<br>
<div align="center"><a href="s_DSC00440.JPG"><img src="s_DSC00440.JPG" width="50%;"></a></div>

Features:

- Avoids obstacles when a touch sensor is pressed.
- Stops when the reflected light intensity measured by the color sensor falls below a specified threshold.
- Measures the distance to the ground using the ultrasonic sensor, stops when the measured value exceeds a threshold, rotates the ultrasonic sensor, and searches for drivable ground.

If the ultrasonic sensor is not used, it can also be used to control a standard Educator Vehicle.

Enter the following commands in the cross-development environment.

```

git clone https://github.com/Nobu19800/ControlEducatorVehicle
cd ControlEducatorVehicle
cmake .
make

```

Transfer the generated `src/ControlEducatorVehicleComp` to the EV3.

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">ControlEducatorVehicle</th>
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
    <td>Target velocity</td>
  </tr>
  <tr>
    <td>current_pose</td>
    <td>RTC::TimedPose2D</td>
    <td>Current position and orientation</td>
  </tr>
  <tr>
    <td>ultrasonic</td>
    <td>RTC::TimedRangeData</td>
    <td>Distance measured by the ultrasonic sensor</td>
  </tr>
  <tr>
    <td>light_reflect</td>
    <td>RTC::TimedDouble</td>
    <td>Reflected light intensity measured by the color sensor</td>
  </tr>
  <tr>
    <td>touch</td>
    <td>TimedBoolean</td>
    <td>Touch sensor ON/OFF state</td>
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
    <td>Corrected target velocity</td>
  </tr>
  <tr>
    <td>angle</td>
    <td>RTC::TimedDouble</td>
    <td>Motor M angle</td>
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
    <td>sensor_height</td>
    <td>0.2</td>
    <td>Ultrasonic sensor threshold used to determine whether drivable ground exists</td>
  </tr>
  <tr>
    <td>back_speed</td>
    <td>0.1</td>
    <td>Reverse movement speed</td>
  </tr>
  <tr>
    <td>back_time</td>
    <td>1.0</td>
    <td>Duration of reverse movement</td>
  </tr>
  <tr>
    <td>rotate_speed</td>
    <td>0.8</td>
    <td>Rotation speed</td>
  </tr>
  <tr>
    <td>rotate_time</td>
    <td>2.0</td>
    <td>Rotation duration</td>
  </tr>
  <tr>
    <td>medium_motor_range</td>
    <td>1.6</td>
    <td>Operating range of Motor M</td>
  </tr>
</table>

<div align="center"><a href="ControlEducatorVehicle.png"><img src="ControlEducatorVehicle.png" width="60%;"></a></div>

### Obstacle Avoidance Using Touch Sensor Input

<div align="center"><a href="ev3_4.png"><img src="ev3_4.png" width="60%;"></a></div>

When a touch sensor is activated, the robot first moves backward at the speed specified by `back_speed` for the duration specified by `back_time`, as shown in step ③.

It then rotates at the angular velocity specified by `rotate_speed` for the duration specified by `rotate_time`, as shown in step ④.

The direction of rotation is opposite to the side on which the activated touch sensor is located.

### Measuring the Distance to the Ground Using the Ultrasonic Sensor

To perform the operation of measuring the distance to the ground, stopping, and rotating the ultrasonic sensor to search for drivable ground, the EV3 Education Vehicle must be assembled with the ultrasonic sensor mounted on a rotating mechanism.

The operation sequence is as follows.

<div align="center"><a href="ev3_sensor.png"><img src="ev3_sensor.png" width="60%;"></a></div>

Suppose the robot is driving on a desk and reaches the edge as shown in step ②.

If the distance measured by the ultrasonic sensor exceeds `sensor_height`, the robot stops.

Then, as shown in step ③, the ultrasonic sensor rotates 90 degrees to the right and checks whether the distance to the ground is less than `sensor_height`.

If the measured value is still greater than `sensor_height`, the sensor rotates 180 degrees to the left as shown in step ④ and checks again.

If a direction is found where the measured distance is less than `sensor_height`, the Education Vehicle rotates toward that direction.

## Batch Installation

To install all of the RTCs described above at once, enter the following commands.

```

git clone https://github.com/Nobu19800/EducatorVehicle_script_ev3dev
cd EducatorVehicle_script_ev3dev
sh Component/install_rtc.sh

```
