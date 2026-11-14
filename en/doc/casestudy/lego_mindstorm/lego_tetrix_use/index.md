---
layout: page
title: how to use tetrix
---

<!-- Title: How to Use TETRIX -->
#contents

## Overview

TETRIX is an expansion product for LEGO Mindstorms sold by Pitsco Education.

It includes aluminum frames, high-torque motors, and other components, making it possible to build full-scale robots.

- [http://www.afrel.co.jp/lineup/tetrix](http://www.afrel.co.jp/lineup/tetrix)

## Specifications

- DC Motor

<table class="table-alt">
  <tr>
    <th>Voltage</th>
    <th>12V</th>
  </tr>
  <tr>
    <td>Stall Torque</td>
    <td>2.1 N·m</td>
  </tr>
  <tr>
    <td>Rotation Speed</td>
    <td>152 rpm</td>
  </tr>
</table>

- RC Servo

<table class="table-alt">
  <tr>
    <th>Name</th>
    <th>HS-485HB (HITEC)</th>
  </tr>
  <tr>
    <td>Voltage</td>
    <td>6V</td>
  </tr>
  <tr>
    <td>Stall Torque</td>
    <td>0.59 N·m</td>
  </tr>
  <tr>
    <td>Rotation Speed</td>
    <td>56 rpm</td>
  </tr>
</table>

## Motor Drivers

The TETRIX Base Set includes a DC motor driver (DC Motor Controller for TETRIX) and an RC servo driver (Servo Controller for TETRIX).

By connecting these motor drivers to the EV3, it becomes possible to control DC motors and RC servos.

## Connection Method

Connect the devices as shown below.

<div align="center"><a href="s_DSC00776.JPG"><img src="s_DSC00776.JPG" width="70%;"></a></div>

After making the connection and turning on the motor driver power, power on the EV3.

## Operation

Communication between the EV3 and the motor drivers is performed via I2C.

If the connection is successful, one of the device files `i2c-3`, `i2c-4`, `i2c-5`, or `i2c-6` should appear under `/dev`.

The number corresponds to the port number plus 2. For example, if connected to Port 1, the device file will be `i2c-3`.

The following sections describe how to control the motor drivers from C++ and Python on ev3dev.

First, include the files required for I2C communication.

- C++

```cpp
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>
```

- Python

```python
import smbus
```

Start I2C communication.

- C++

```cpp
int fd; = open("/dev/i2c-3", O_RDWR);
```

- Python

```python
sm = smbus.SMBus(3)
```

The motor driver's default address is `0x01`. When connected in a daisy chain, addresses `0x02` through `0x08` are assigned.

In the example connection above, the DC motor driver should be set to `0x01`, and the RC servo driver should be set to `0x02`.

First, let's control the DC motor driver.

### DC Motor Driver

Set the control mode.

The control mode can be configured by writing the following values to register `0x44` for Motor 1 or `0x47` for Motor 2.

*Note:* Encoders are not included in the TETRIX Base Set. If you want to use speed control or position control modes, you must purchase encoders separately.

<table class="table-alt">
  <tr>
    <th>Input Value</th>
    <th>Control Mode</th>
  </tr>
  <tr>
    <td>0b00</td>
    <td>PWM</td>
  </tr>
  <tr>
    <td>0b01</td>
    <td>Speed Control</td>
  </tr>
  <tr>
    <td>0b10</td>
    <td>Position Control</td>
  </tr>
  <tr>
    <td>0b11</td>
    <td>Encoder Reset</td>
  </tr>
</table>

<br>

Set PWM mode.

- C++

```cpp
ioctl(fd, I2C_SLAVE, 0x01)
unsigned char buf[2] = {0x44, 0x00};
write(fd, buf, 2);
```

- Python

```python
sm.write_i2c_block_data(0x01, 0x44, [0x00])
```

Finally, set the PWM width.

This can be configured by writing to register `0x45` for Motor 1 or `0x46` for Motor 2.

PWM values:
- `1` to `127`: Forward rotation
- `-127` to `-1`: Reverse rotation
- `0`: Float stop mode
- `128`: Brake stop mode

- C++

```cpp
unsigned char buf[2] = {0x45, 0x30};
write(fd, buf, 2);
```

- Python

```python
sm.write_i2c_block_data(0x01, 0x45, [0x30])
```

### RC Servo Driver

The RC servo driver can control up to six RC servos.

Control is performed by writing the target angle to registers `0x42` through `0x47`.

Pulse widths can be set between 0.75 ms and 2.25 ms.

- C++

```cpp
ioctl(fd, I2C_SLAVE, 0x02)
unsigned char buf[2] = {0x42, 0x60};
write(fd, buf, 2);
```

- Python

```python
sm.write_i2c_block_data(0x02, 0x42, [0x60])
```

## Example Application

The following is an example of a vehicle built using DC motors.

<div align="center"><a href="s_DSC00777.JPG"><img src="s_DSC00777.JPG" width="60%;"></a></div>

Two L motors are attached to the handle section, allowing the vehicle to be controlled by rotating the motors.

<div align="center"><a href="tetrix_device.png"><img src="tetrix_device.png" width="60%;"></a></div>

The RTCs used are described below.

### TetrixVehicle

A component for controlling the vehicle shown above.

- https://github.com/Nobu19800/TetrixVehicle

<div align="center"><a href="TetrixVehicle.png"><img src="TetrixVehicle.png" width="80%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">TetrixVehicle</th>
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
    <td>target_velocity</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Target velocity</td>
  </tr>
  <tr>
    <td>update_position</td>
    <td>RTC::TimedPose2D</td>
    <td>Reset position</td>
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
    <td>position</td>
    <td>RTC::TimedPose2D</td>
    <td>Current position</td>
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
    <td>0.04</td>
    <td>Wheel radius</td>
  </tr>
  <tr>
    <td>wheelDistance</td>
    <td>0.34</td>
    <td>Distance between wheels</td>
  </tr>
  <tr>
    <td>portNum</td>
    <td>1</td>
    <td>Port number</td>
  </tr>
  <tr>
    <td>rot_dir_left_motor</td>
    <td>1</td>
    <td>Left wheel rotation direction</td>
  </tr>
  <tr>
    <td>rot_dir_righteft_motor</td>
    <td>-1</td>
    <td>Right wheel rotation direction</td>
  </tr>
  <tr>
    <td>GearRatio</td>
    <td>3.0</td>
    <td>Gear ratio</td>
  </tr>
</table>

### VehicleController

A component that outputs the target vehicle velocity based on the angles of the L motors.

- [https://github.com/Nobu19800/VehicleController](https://github.com/Nobu19800/VehicleController)

<div align="center"><a href="VehicleController.png"><img src="VehicleController.png" width="80%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">VehicleController</th>
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
    <td>rotation_by_angle</td>
    <td>-0.6</td>
    <td>Amount of target angular velocity change based on the base motor angle</td>
  </tr>
  <tr>
    <td>velocity_by_angle</td>
    <td>-0.1</td>
    <td>Amount of target velocity change based on the tip motor angle</td>
  </tr>
</table>

