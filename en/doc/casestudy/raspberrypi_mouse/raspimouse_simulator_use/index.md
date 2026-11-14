---
layout: page
title: simulator usage
---

<!-- Title: Simulator Usage -->
#contents

This page describes the specifications and usage of the Raspberry Pi Mouse simulator RTC.

<div align="center"><a href="raspimouse2.png"><img src="raspimouse2.png" width="70%;"></a></div>

# Specifications

<div align="center"><a href="raspimouse.png"><img src="raspimouse.png" width="70%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">RaspberryPiMouseSimulator</th>
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
    <td>pose_update</td>
    <td>RTC::TimedPose2D</td>
    <td>Update current position</td>
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
    <td>current_velocity_out</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Current velocity</td>
  </tr>
  <tr>
    <td>current_pose_out</td>
    <td>RTC::TimedPose2D</td>
    <td>Current position</td>
  </tr>
  <tr>
    <td>ir_sensor_out</td>
    <td>RTC::TimedShortSeq</td>
    <td>Reproduced values corresponding to data acquired from the distance sensors</td>
  </tr>
  <tr>
    <td>ir_sensor_metre_out</td>
    <td>RTC::TimedDoubleSeq</td>
    <td>Distance measured by the distance sensors</td>
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
    <td>sampling_time</td>
    <td>-1</td>
    <td>Simulation time step. If set to a negative value, the execution context period is used.</td>
  </tr>
  <tr>
    <td>draw_time</td>
    <td>0.01</td>
    <td>Rendering interval</td>
  </tr>
  <tr>
    <td>sensor_param</td>
    <td>1394,792,525,373,299,260,222,181,135,100,81,36,17,16</td>
    <td>Parameters used to convert measured distances into raw sensor data. Values correspond to distances of 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.15, 0.20, 0.25, and 0.30 [m].</td>
  </tr>
  <tr>
    <td>blocksConfigFile</td>
    <td>None</td>
    <td>Name of the obstacle placement configuration file</td>
  </tr>
</table>

# Usage

You can download the simulator from the following link.

- [ZIP File](https://github.com/Nobu19800/RasPiMouseSimulatorRTC/archive/master.zip)

**The simulator used in RT Middleware workshops has different settings. Please download it from the workshop page instead.**

The executable file (**RaspberryPiMouseSimulatorComp.exe**) is located in the **EXE** folder of the extracted archive.

Running this executable starts the RTC.

## Data Ports

### Distance Sensor Data Output

There are two ports that output distance sensor data: **ir_sensor_out** and **ir_sensor_metre_out**.

Since **RaspberryPiMouseRTC** directly outputs distance sensor data, **ir_sensor_out** reproduces sensor values based on the distances measured in the simulator.

**ir_sensor_metre_out** outputs the measured distance values in meters.

## Configuration Parameters

### Obstacle Configuration File

The **blocksConfigFile** parameter can be used to specify a CSV file that defines obstacle placement.

A sample file named **test.csv** is included.

Specify the position, orientation, and size of each obstacle in the file.

<table class="table-alt">
  <tr>
    <th>Position (X)</th>
    <th>Position (Y)</th>
    <th>Position (Z)</th>
    <th>Length (L)</th>
    <th>Width (W)</th>
    <th>Height (H)</th>
    <th>Angle (θ)</th>
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

<div align="center"><a href="block1.png"><img src="block1.png" width="70%;"></a></div>

<div align="center"><a href="block2.png"><img src="block2.png" width="70%;"></a></div>

Any number of blocks can be configured.

