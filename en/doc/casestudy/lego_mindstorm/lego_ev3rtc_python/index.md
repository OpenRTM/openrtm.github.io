---
layout: page
title: creating rtcs for ev3 (python edition)
---

init
<!-- Title: Creating RTCs for EV3 (Python Edition) -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * Creating RTCs for EV3 (Python Edition) -->
#contents

## Assembling the Mobile Robot

When you purchase the standard EV3 kit, it should include a manual describing how to build a mobile robot (Educator Vehicle).

If you do not have the manual, you can download it from the following URL. In this tutorial, we will use this mobile robot as an example to create a mobile robot RTC.

- [Educator Vehicle](http://robotsquare.com/wp-content/uploads/2013/10/45544_educator.pdf)

First, assemble the mobile robot (Educator Vehicle) according to the manual.

Connect the motors and sensors as follows:

<table class="table-alt">
  <tr>
    <td>Right Motor</td>
    <td>Port C</td>
  </tr>
  <tr>
    <td>Left Motor</td>
    <td>Port B</td>
  </tr>
  <tr>
    <td>Motor (M)</td>
    <td>Port A</td>
  </tr>
  <tr>
    <td>Right Touch Sensor</td>
    <td>Port 3</td>
  </tr>
  <tr>
    <td>Left Touch Sensor</td>
    <td>Port 1</td>
  </tr>
  <tr>
    <td>Ultrasonic Sensor</td>
    <td>Port 4</td>
  </tr>
  <tr>
    <td>Gyro Sensor</td>
    <td>Port 2</td>
  </tr>
</table>

## Mobile Robot Kinematics

The component described above receives a two-dimensional velocity command as input. However, to actually control the motors, motor angular velocity commands must be calculated and sent to the motors.

For an introduction to mobile robot kinematics, the following page by Professor Kumagai of Tohoku Gakuin University is helpful:

- [http://www.mech.tohoku-gakuin.ac.jp/rde/contents/course/robotics/wheelrobot.html](http://www.mech.tohoku-gakuin.ac.jp/rde/contents/course/robotics/wheelrobot.html)

Following the Common Interface Specification for Autonomous Mobile Functions,

- [http://openrtm.org/openrtm/ja/project/Recommendation_CommonIF](http://openrtm.org/openrtm/ja/project/Recommendation_CommonIF)(No corresponding English project page available.)

we assume a right-handed coordinate system with the robot's forward direction as the X-axis.

Velocity commands are represented as `(v_x, v_y, v_a)` according to this coordinate system. Since this is a differential-drive mobile robot, `v_y` is always 0, so only `v_x` and `v_a` need to be specified.

Let the angular velocities of the right and left wheels be <a href="math16.png"><img src="math16.png" width="2%;"></a> and <a href="math17.png"><img src="math17.png" width="2%;"></a>, respectively, and let the wheel radius be `r`. The linear velocities at the wheel-ground contact points, `v_r` and `v_l`, are:

<br>
<div align="center"><a href="math3.png"><img src="math3.png" width="10%;"></a></div>
<div align="center"><a href="math4.png"><img src="math4.png" width="10%;"></a></div>
<br>

Let `ρ` be the distance from the center of rotation to the center of the robot. Then:

<br>
<div align="center"><a href="math5.png"><img src="math5.png" width="10%;"></a></div>
<br>

On the other hand, if `d` is half the distance between the wheels (half the tread width), then:

<br>
<div align="center"><a href="math0.png"><img src="math0.png" width="10%;"></a></div>
<div align="center"><a href="math1.png"><img src="math1.png" width="10%;"></a></div>
<br>

From these equations, the angular velocities that should be applied to the left and right motors for a velocity command `(v_x, v_y, v_a)` are:

<br>
<div align="center"><a href="math6.png"><img src="math6.png" width="10%;"></a></div>
<div align="center"><a href="math7.png"><img src="math7.png" width="10%;"></a></div>
<br>

For the Educator Vehicle, the wheel diameter `(2r)` and tread width `(2d)` are:

<table class="table-alt">
  <tr>
    <td>Wheel Diameter (2r)</td>
    <td>56 mm (0.056 m)</td>
  </tr>
  <tr>
    <td>Wheel Radius (r)</td>
    <td>28 mm (0.028 m)</td>
  </tr>
  <tr>
    <td>Tread Width (2d)</td>
    <td>118.5 mm (0.1185 m)</td>
  </tr>
  <tr>
    <td>Half Tread Width (d)</td>
    <td>59.25 mm (0.05925 m)</td>
  </tr>
  <tr>
    <td>Wheel Width</td>
    <td>28.5 mm (0.0285 m)</td>
  </tr>
</table>

Therefore:

<br>
<div align="center"><a href="math8.png"><img src="math8.png" width="10%;"></a></div>
<div align="center"><a href="math9.png"><img src="math9.png" width="10%;"></a></div>
<br>

## Self-Localization (Odometry)

Next, let us consider how to estimate the robot's position.

By integrating the robot's linear and angular velocities, the position and orientation at any time can be obtained. Let the linear velocity be `v_x` and the angular velocity be `v_a`. Using a linear approximation, the relationship between the infinitesimal displacement `(x, y, θ)` and `(v_x, v_a)` is:

<br>
<div align="center"><a href="math10.png"><img src="math10.png" width="10%;"></a></div>
<div align="center"><a href="math11.png"><img src="math11.png" width="10%;"></a></div>
<div align="center"><a href="math12.png"><img src="math12.png" width="10%;"></a></div>
<br>

(A more accurate method would use arc approximation, but for simplicity we use linear approximation here.)

When implementing this on a computer with a sampling period `Δt [s]`, the equations become:

<div align="center"><a href="math13.png"><img src="math13.png" width="100;"></a></div>
<div align="center"><a href="math14.png"><img src="math14.png" width="100;"></a></div>
<div align="center"><a href="math15.png"><img src="math15.png" width="100;"></a></div>

## Creating an RTC Skeleton

## Designing the RTC

Now we design the RTC to be created.

The specifications of the RTC are shown below. Enter the required information in RTCBuilder and generate the skeleton code.

<table class="table-alt">
  <tr>
    <td colspan="3" style="text-align: center;"><strong>Basic Tab</strong></td>
  </tr>
  <tr>
    <td style="text-align: center;"><strong>Profile Item</strong></td>
    <td colspan="2" style="text-align: center;"><strong>Name / Setting</strong></td>
  </tr>
  <tr>
    <td>Module Name</td>
    <td colspan="2" style="text-align: center;">EducatorVehicle</td>
  </tr>
  <tr>
    <td>Version</td>
    <td colspan="2" style="text-align: center;">Any</td>
  </tr>
  <tr>
    <td>Vendor</td>
    <td colspan="2" style="text-align: center;">Any</td>
  </tr>
  <tr>
    <td>Category</td>
    <td colspan="2" style="text-align: center;">Mobilerobot</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;"><strong>Activity</strong></td>
  </tr>
  <tr>
    <td>Enabled Actions</td>
    <td colspan="2" style="text-align; ">onInitialize, onActivated, onDeactivated, onExecute</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;"><strong>Data Ports (InPort)</strong></td>
  </tr>
  <tr>
    <td><strong>Port Name</strong></td>
    <td><strong>Type</strong></td>
    <td><strong>Description</strong></td>
  </tr>
  <tr>
    <td>velocity2D</td>
    <td>RTC::TimedVelocity2D</td>
    <td>Velocity command (v_x, v_y, v_θ) [m/s, m/s, rad/s]</td>
  </tr>
  <tr>
    <td>angle</td>
    <td>RTC::TimedDouble</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;"><strong>Data Ports (OutPort)</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>Type</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>odometry</td>
    <td>RTC::TimedPose2D</td>
    <td>Current position and orientation (x, y, θ) [m, m, rad]</td>
  </tr>
  <tr>
    <td>ultrasonic</td>
    <td>RTC::RangeData</td>
    <td>Stores the ultrasonic sensor measurement as range sensor distance data in element 1</td>
  </tr>
  <tr>
    <td>gyro</td>
    <td>RTC::TimedDouble</td>
    <td>Outputs gyro sensor values as TimedDouble [rad]</td>
  </tr>
  <tr>
    <td>color</td>
    <td>RTC::TimedString</td>
    <td>Outputs color sensor values as color names (none, black, white, blue, green, red, yellow, brown)</td>
  </tr>
  <tr>
    <td>touch</td>
    <td>RTC::TimedBooleanSeq</td>
    <td>Outputs touch sensor values as Boolean[2]</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;"><strong>Configuration</strong></td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>Type</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>wheelRadius</td>
    <td>double</td>
    <td>Wheel radius [m]</td>
  </tr>
  <tr>
    <td>wheelDistance</td>
    <td>double</td>
    <td>Half the distance between the wheels [m]</td>
  </tr>
</table>
