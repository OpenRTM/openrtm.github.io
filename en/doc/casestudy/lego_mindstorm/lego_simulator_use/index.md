---
layout: page
title: using the simulator
---

<!-- Title: Using the Simulator -->
#contents

This page explains the specifications and usage of the simulator RTC for the modified Educator Vehicle.

<div align="center"><a href="ev32.png"><img src="ev32.png" width="60%;"></a></div>

# Specifications

<div align="center"><a href="simulator_ev3_1.png"><img src="simulator_ev3_1.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">EV3Simulator</th>
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
    <td>M motor angle</td>
  </tr>
  <tr>
    <td>pos_update</td>
    <td>RTC::TimedPose2D</td>
    <td>Current position update</td>
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
    <td>Current position</td>
  </tr>
  <tr>
    <td>current_vel</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Current velocity</td>
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
    <td>light_reflect</td>
    <td>RTC::TimedDouble</td>
    <td>Reflected light intensity measured by the color sensor</td>
  </tr>
  <tr>
    <td>touch</td>
    <td>RTC::TimedBooleanSeq</td>
    <td>Touch sensor on/off status. The right sensor is element 0, and the left sensor is element 1.</td>
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
    <td>medium_motor_speed</td>
    <td>1.6</td>
    <td>Speed of Motor M</td>
  </tr>
  <tr>
    <td>blocksConfigFile</td>
    <td>None</td>
    <td>Name of the obstacle placement configuration file</td>
  </tr>
  <tr>
    <td>touchSensorOnLength</td>
    <td>0.003</td>
    <td>Press distance required for the touch sensor to be judged as ON</td>
  </tr>
  <tr>
    <td>lightReflectThreshold</td>
    <td>0.1</td>
    <td>Outputs 255 when the distance from the color sensor to an object is less than or equal to this value</td>
  </tr>
  <tr>
    <td>plane_exist</td>
    <td>0</td>
    <td>Create a new ground plane when set to 1</td>
  </tr>
  <tr>
    <td>plane_x</td>
    <td>0</td>
    <td>Ground plane position (X)</td>
  </tr>
  <tr>
    <td>plane_y</td>
    <td>0</td>
    <td>Ground plane position (Y)</td>
  </tr>
  <tr>
    <td>plane_z</td>
    <td>0</td>
    <td>Ground plane position (Z)</td>
  </tr>
  <tr>
    <td>plane_lx</td>
    <td>1.0</td>
    <td>Ground plane length</td>
  </tr>
  <tr>
    <td>plane_ly</td>
    <td>1.0</td>
    <td>Ground plane width</td>
  </tr>
  <tr>
    <td>plane_lz</td>
    <td>1.0</td>
    <td>Ground plane height</td>
  </tr>
  <tr>
    <td>draw_time</td>
    <td>0.01</td>
    <td>Rendering period</td>
  </tr>
  <tr>
    <td>sampling_time</td>
    <td>-1</td>
    <td>Simulation time step. If set to a negative value, the execution context period is used.</td>
  </tr>
</table>

# Usage

The simulator can be downloaded from the following link.

- [ZIP File](https://github.com/Nobu19800/EV3SimulatorRTC/archive/master.zip)

The executable file (**EV3SimulatorComp.exe**) is located in the **EXE** folder of the extracted archive.

Running this executable starts the RTC.

## Configuration Parameters

### Obstacle Configuration File

You can specify a CSV file containing obstacle placement settings using the parameter **blocksConfigFile**.

A sample file named **test.csv** is included.

Describe the position, orientation, and size of each obstacle in the file.

<table class="table-alt">
  <tr>
    <td>Position (X)</td>
    <td>Position (Y)</td>
    <td>Position (Z)</td>
    <td>Length (L)</td>
    <td>Width (W)</td>
    <td>Height (H)</td>
    <td>Angle (θ)</td>
  </tr>
  <tr>
    <td>0.3</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.1</td>
    <td>1.0</td>
    <td>0.3</td>
    <td>0.0</td>
  </tr>
</table>

<div align="center"><a href="block1.png"><img src="block1.png" width="50%;"></a></div>

<div align="center"><a href="block2.png"><img src="block2.png" width="50%;"></a></div>

Any number of blocks can be configured.

### Ground Plane Configuration

The modified Educator Vehicle can detect the presence or absence of a traversable surface using its ultrasonic sensor and perform avoidance behavior.

To support simulation of this control behavior, configuration parameters are provided for creating a ground plane.

Set **plane_exist** to **1**, then configure the position and size of the ground plane.

