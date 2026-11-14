---
layout: page
title: tutorial (slam exercise)
---

init
<!-- チュートリアル(SLAM実習) -->
#contents

## Introduction

This page explains how to perform navigation using SLAM with a Raspberry Pi Mouse equipped with a LiDAR.

<div align="center"><a href="https://rt-net.jp/mobility/wp-content/uploads/2019/12/23b47429c42d672e7f94ae0a3c9c9d6c.png"><img src="https://rt-net.jp/mobility/wp-content/uploads/2019/12/23b47429c42d672e7f94ae0a3c9c9d6c.png" width="70%;"></a></div>

SLAM stands for Simultaneous Localization and Mapping, which refers to performing environment map generation and self-localization simultaneously. In this tutorial, the [[RT Components for Mobile Robot Navigation:https://ogata-lab.jp/ja/technology_ja/mobile_nav_rtcs_ja.html]] are used.

The RT components for mobile robot navigation use a cross-platform library called [MRPT](https://www.mrpt.org/), which provides functions such as self-localization, environment map generation, and path planning.

## Preparation

### Installing the LiDAR

First, install the LiDAR on the Raspberry Pi Mouse.

There are two types of LiDAR mounts. Install the LiDAR on the Raspberry Pi Mouse by following the instructions for either (1) the dedicated LiDAR mount or (2) the multi-LiDAR mount described below.

#### Dedicated LiDAR Mount

If you are using a mount secured with two screws as shown in the image below, follow the procedure described here.

<div align="center"><a href="DSC04139.JPG"><img src="DSC04139.JPG" width="50%;"></a></div>

Prepare the Raspberry Pi Mouse, LiDAR, and tapping screws shown below.

<div align="center"><a href="slam29_2.png"><img src="slam29_2.png" width="50%;"></a></div>

Next, remove the screws from the bottom of the Raspberry Pi Mouse.

<div align="center"><a href="slam30.png"><img src="slam30.png" width="50%;"></a></div>

Slide the circuit board section together with the frame.

<div align="center"><a href="slam31.png"><img src="slam31.png" width="50%;"></a></div>

Next, remove the spacers by turning them by hand.

<div align="center"><a href="slam32.png"><img src="slam32.png" width="50%;"></a></div>

Remove the sensor board.

<div align="center"><a href="slam33.png"><img src="slam33.png" width="50%;"></a></div>
<div align="center"><a href="slam34.png"><img src="slam34.png" width="50%;"></a></div>

Place the LiDAR on top of the Raspberry Pi Mouse and secure it with screws.

<div align="center"><a href="slam35.png"><img src="slam35.png" width="50%;"></a></div>
<div align="center"><a href="slam36.png"><img src="slam36.png" width="50%;"></a></div>
<div align="center"><a href="slam37.png"><img src="slam37.png" width="50%;"></a></div>

Connect the Raspberry Pi Mouse and the LiDAR using a USB port.

<div align="center"><a href="slam38.png"><img src="slam38.png" width="50%;"></a></div>
<div align="center"><a href="slam39.png"><img src="slam39.png" width="50%;"></a></div>

Reassemble the removed parts to complete the installation.

#### Multi-LiDAR Mount

If you are using a mount with four hooks as shown in the image below, follow the procedure described here.

<div align="center"><a href="DSC04142.JPG"><img src="DSC04142.JPG" width="50%;"></a></div>

Hook the four tabs onto the Raspberry Pi Mouse as shown below.

First, attach the two front hooks.

<div align="center"><a href="DSC04145.JPG"><img src="DSC04145.JPG" width="50%;"></a></div>

Next, attach the rear hooks.

<div align="center"><a href="DSC04146.JPG"><img src="DSC04146.JPG" width="50%;"></a></div>

Then secure the front two locations of the multi-LiDAR mount with 3-8 pan-head tapping screws to complete the installation.

<div align="center"><a href="DSC04151.JPG"><img src="DSC04151.JPG" width="50%;"></a></div>

<div align="center"><a href="DSC04147.JPG"><img src="DSC04147.JPG" width="50%;"></a></div>

Connect the Raspberry Pi Mouse and the LiDAR using a USB port.

<div align="center"><a href="DSC04148.JPG"><img src="DSC04148.JPG" width="50%;"></a></div>

After completing the LiDAR installation, turn on the Raspberry Pi Mouse and connect to its access point.

## Navigation Map Generation System Using SLAM

In this section, you will try a system that generates an environment map while performing self-localization.

MRPT supports algorithms such as [ICP-SLAM and RBPF-SLAM](https://www.mrpt.org/List_of_SLAM_algorithms), but the RT components for mobile robot navigation use ICP-SLAM.

The ICP algorithm aligns two point cloud datasets (map data and the latest data acquired by the LRF) by repeatedly applying translation and rotation until the distances between corresponding points become minimal.

The current position is calculated by aligning the point cloud data of the map being generated with the data acquired by the LRF using the ICP algorithm.

### Starting the Mapper System (Raspberry Pi)

First, start the Mapper system from the web browser interface.

<div align="center"><a href="slam1.png"><img src="slam1.png" width="50%;"></a></div>

If the original page does not reappear, click **Back to the top page.**

<div align="center"><a href="slam2.png"><img src="slam2.png" width="50%;"></a></div>

### Starting NavigationManager (PC)

Next, start NavigationManager.

Execute the following batch file or shell script in the Navigation folder.

- NavigationManager.bat (Windows)
- NavigationManager.sh (Ubuntu)

The following GUI will start.

<div align="center"><a href="slam48.png"><img src="slam48.png" width="50%;"></a></div>

### Connecting Ports and Activating RTCs

The Name Service View in RTSystemEditor should be in the following state.

<div align="center"><a href="slam28.png"><img src="slam28.png" width="50%;"></a></div>

First, click the **Connect** button in the web browser interface.

This connects the RTC ports on the Raspberry Pi.

<div align="center"><a href="slam14.png"><img src="slam14.png" width="50%;"></a></div>

Connect the components in the system diagram as shown below.

<div align="center"><a href="slam46.png"><img src="slam46.png" width="50%;"></a></div>

Except for the NavigationManager-related connections, all other connections have already been established. Connect the following ports


<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th>Port Name</th>
    <th>Component Name</th>
    <th>Port Name</th>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>mapperService</td>
    <td>Mapper_MRPT0</td>
    <td>gridMapper</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>currentPose</td>
    <td>Mapper_MRPT0</td>
    <td>estimatedPose</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>targetVelocity</td>
    <td>RaspberryPiMouseRTC0</td>
    <td>target_velocity_in</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>range</td>
    <td>RPLiderRTC0(RobotisLDSensor0)</td>
    <td>range</td>
  </tr>
</table>

After connecting the ports, activate the RTCs.

<div align="center"><a href="slam5.png"><img src="slam5.png" width="50%;"></a></div>

### Creating a Map

Click the **Start Mapping** button in the NavigationManager GUI.

<div align="center"><a href="slam6.png"><img src="slam6.png" width="50%;"></a></div>

Next, when the RTCs are activated, the following joystick GUI starts.

Operate the yellow circle with the mouse.

This will move the Raspberry Pi Mouse.

<div align="center"><a href="slam8.png"><img src="slam8.png" width="50%;"></a></div>

After operating it for a while, an environment map similar to the following will be generated.

<div align="center"><a href="testMap.png"><img src="testMap.png" width="50%;"></a></div>

When map generation is complete, click the **Stop Mapping** button.

<div align="center"><a href="slam10.png"><img src="slam10.png" width="50%;"></a></div>

Next, save the map data.

Click the **Save Map** button.

<div align="center"><a href="slam11.png"><img src="slam11.png" width="50%;"></a></div>

Set the file name to **testMap** and save it in the Navigation folder.

<br>
※Clicking the **Open** button will save the file.

<div align="center"><a href="slam45.png"><img src="slam45.png" width="50%;"></a></div>

Finally, stop the Mapper system using the web browser interface.

<div align="center"><a href="slam13.png"><img src="slam13.png" width="50%;"></a></div>

## Running the Navigation (Path Planning) System

From here, you will use the generated environment map data to perform path planning with the Raspberry Pi Mouse.

### Starting the PathPlan System (Raspberry Pi)

Start the PathPlan system from the web browser interface.

<div align="center"><a href="slam15.png"><img src="slam15.png" width="50%;"></a></div>

If the original page does not reappear, click **Back to the top page.**

### Starting NavigationManager and MapServer (PC)

Next, start NavigationManager and MapServer.

If NavigationManager is already running, start only MapServer.

Run the following batch files or shell scripts in the Navigation folder.

- NavigationManager.bat (Windows), NavigationManager.sh (Ubuntu)
- MapServer.bat (Windows), MapServer.sh (Ubuntu)

### Connecting Ports and Activating RTCs

The Name Service View in RTSystemEditor should now look as follows.

<div align="center"><a href="slam18.png"><img src="slam18.png" width="50%;"></a></div>

First, click the **Connect** button in the web browser interface.

This will connect the RTC ports on the Raspberry Pi.

<div align="center"><a href="slam16.png"><img src="slam16.png" width="50%;"></a></div>

Connect the components on the system diagram as shown below.

<div align="center"><a href="slam19.png"><img src="slam19.png" width="50%;"></a></div>

<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th>Port Name</th>
    <th>Component Name</th>
    <th>Port Name</th>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>mapServer</td>
    <td>MapServer0</td>
    <td>mapServer</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>pathPlanner</td>
    <td>PathPlanner_MRPT0</td>
    <td>pathPlanner</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>pathFollower</td>
    <td>SimplePathFollower0</td>
    <td>PathFollower</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>currentPose</td>
    <td>Localization_MRPT0</td>
    <td>estimatedPose</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>range</td>
    <td>RPLiderRTC0(RobotisLDSensor0)</td>
    <td>range</td>
  </tr>
  <tr>
    <td>MapServer0</td>
    <td>mapServer</td>
    <td>Localization_MRPT</td>
    <td>mapServer</td>
  </tr>
</table>

After connecting the ports, activate the RTCs.

<div align="center"><a href="slam20.png"><img src="slam20.png" width="50%;"></a></div>

### Path Generation

First, set the target position and target orientation angle of the Raspberry Pi Mouse.

Click the desired target position on the map displayed in the NavigationManager GUI.

The white area on the map indicates regions where no obstacles were detected, so click somewhere within the white area.

<div align="center"><a href="slam21.png"><img src="slam21.png" width="50%;"></a></div>

The following dialog will be displayed, allowing you to set the target orientation angle.

<div align="center"><a href="slam22.png"><img src="slam22.png" width="50%;"></a></div>

Click any location in the dialog to change the angle of the red line extending from the center, and set an appropriate angle.

<div align="center"><a href="path23.png"><img src="path23.png" width="50%;"></a></div>

Click the **OK** button to display the target position on the map.

<div align="center"><a href="slam23.png"><img src="slam23.png" width="50%;"></a></div>

Next, click the **Plan Path** button.

<div align="center"><a href="slam24.png"><img src="slam24.png" width="50%;"></a></div>

The target path to the destination will then be calculated.

<div align="center"><a href="slam25.png"><img src="slam25.png" width="50%;"></a></div>

### Navigation Execution

Next, click the **Start Following** button.

<div align="center"><a href="slam26.png"><img src="slam26.png" width="50%;"></a></div>

The Raspberry Pi Mouse will begin moving toward the destination along the generated path.

<div align="center"><a href="slam27.png"><img src="slam27.png" width="50%;"></a></div>

When the Raspberry Pi Mouse reaches the destination, navigation is complete.

If you want to stop navigation during operation, click the **Stop Following** button.

## Summary

In this tutorial, you learned:

- How to install a LiDAR on a Raspberry Pi Mouse using either a dedicated LiDAR mount or a multi-LiDAR mount.
- How to connect the LiDAR to the Raspberry Pi Mouse and prepare the hardware for SLAM operation.
- How to start the Mapper system and NavigationManager.
- How to connect and activate the RTCs required for SLAM-based map generation.
- How to generate an environment map while performing self-localization using ICP-SLAM.
- How to save generated map data for later use.
- How to start the PathPlan system and MapServer for navigation.
- How to connect the RTCs required for path planning and localization.
- How to specify a target position and target orientation on a generated map.
- How to generate a navigation path and execute autonomous movement toward the destination.
- How to stop navigation when necessary.

By completing this tutorial, you have learned how to generate an environment map using SLAM, perform self-localization, create navigation paths, and execute autonomous navigation with a LiDAR-equipped Raspberry Pi Mouse.
