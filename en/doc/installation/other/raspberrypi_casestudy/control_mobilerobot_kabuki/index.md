---
layout: page
title: controlling the kobuki mobile robot
---

<!-- Title: Controlling the Kobuki Mobile Robot -->

#contents

Kobuki is a research mobile robot manufactured by Yujin Robotics.

It is approximately the same size as a Roomba robot vacuum and can be controlled from a PC via a USB serial connection.

Kobuki is equipped with I/O interfaces, serial communication ports, power connectors, buttons, LEDs, and other features, making it suitable as an experimental robot platform.

A script for installing the software required to run the Kobuki sample applications described below can be downloaded from:

- http://svn.openrtm.org/Embedded/trunk/RaspberryPi/tools/rpi.sh

```bash
$ wget http://svn.openrtm.org/Embedded/trunk/RaspberryPi/tools/rpi.sh
$ chmod 755 rpi.sh
$ sudo ./rpi.sh hostname --type kobuki
```

This script automatically performs the environment setup and compiles the Kobuki sample applications described in this guide.

## Connecting Raspberry Pi and Kobuki

The figure below shows the main panel of Kobuki.

<div align="center"><a href="kobuki_panel.png"><img src="kobuki_panel.png" width="70%;"></a></div>
<div align="center"><strong>Kobuki DC Output Connector</strong></div>

Use the 5V/1A DC output connector to power the Raspberry Pi, and use the USB connector for communication.

### Power Supply

Kobuki provides a DC output connector capable of supplying 5V at 1A, which can be used to power a Raspberry Pi.

The connector specifications are:

<table class="table-alt">
  <tr>
    <th colspan="2">Kobuki 5V/1A Connector</th>
  </tr>
  <tr>
    <td>Housing</td>
    <td>Molex PN: 43645-0200</td>
  </tr>
  <tr>
    <td>Terminal</td>
    <td>Molex PN: 43030-0001</td>
  </tr>
</table>

<div align="center"><a href="kobuki5v_connector.png"><img src="kobuki5v_connector.png" width="70%;"></a></div>
<div align="center"><strong>Kobuki DC 5V/1A Connector</strong></div>

These connectors can also be purchased from RT Robot Shop and similar suppliers.

- Kobuki Connector Set (¥450)
  http://www.rt-shop.jp/index.php?main_page=product_info&cPath=1001_1022&products_id=784

By creating a DC-to-USB power cable as shown below, power can be supplied to the Raspberry Pi.

<div align="center"><a href="kobuki_raspberry_dccable.png"><img src="kobuki_raspberry_dccable.png" width="70%;"></a></div>
<div align="center"><strong>DC Power Cable for Raspberry Pi</strong></div>

Nowadays, many portable batteries with USB outputs for smartphones are available and can also be used as power sources.

<div align="center"><a href="battery.png"><img src="battery.png" width="70%;"></a></div>
<div align="center"><strong>Portable Smartphone Battery</strong></div>

### USB Connection

Use the USB cable included with Kobuki to connect Kobuki and the Raspberry Pi.

On the Raspberry Pi, the device appears as:

```bash
$ ls /dev/ttyUSB*
/dev/ttyUSB0
```

### Hardware Setup

Mount the Raspberry Pi on the Kobuki platform and connect both power and USB cables.

If the Raspberry Pi is connected to a wireless LAN, Kobuki can be controlled remotely over Wi-Fi.

<div align="center"><a href="kobuki_and_raspi.png"><img src="kobuki_and_raspi.png" width="70%;"></a></div>
<div align="center"><strong>Kobuki Equipped with a Raspberry Pi</strong></div>

Since the Raspberry Pi may come loose while Kobuki is moving, securing it with hook-and-loop tape (Velcro) is recommended.

## Compiling the KobukiAIST RT Component

Although RT component compilation was covered previously, we review it here.

First, check out the KobukiAIST RT component from the repository below and build it.

- KobukiAIST RTC
  http://svn.openrtm.org/components/trunk/mobile_robots/kobuki

```bash
$ svn co http://svn.openrtm.org/components/trunk/mobile_robots/kobuki
$ cd kobuki
$ mkdir build
$ cd build
$ cmake -DCMAKE_INSTALL_PREFIX=/usr ..
$ make
$ cd src
$ sudo make install
```

After installation, the executable should be installed at:

```text
/usr/lib/openrtm-1.1/rtc/KobukiAISTComp
```

To test it:

```bash
$ rtm-naming
$ sudo /usr/lib/openrtm-1.1/rtc/KobukiAISTComp
```

Root privileges are required because access to `/dev/ttyUSB0` is necessary.

Start RTSystemEditor and connect to the Raspberry Pi using its hostname or IP address.

You should see a component named **KobukiAIST0**.

Open its Configuration dialog.

You can control LEDs such as LED1 and LED2 by selecting RED, GREEN, and other options using the radio buttons. The LEDs should illuminate accordingly.

## Automatically Starting the KobukiAIST Component

To automatically start the KobukiAIST component when Raspberry Pi boots, create the following script as:

```bash
/etc/kobuki.sh
```

Create the file:

```bash
$ sudo vi /etc/kobuki.sh
```

Contents:

```sh
#!/bin/sh
#
# KobukiAIST RTC launch script
#

ns=/usr/bin/rtm-naming
kobukiRTC=/usr/lib/openrtm-1.1/rtc/KobukiAISTComp
workdir=/tmp/kobuki

$ns
sleep 5

if test -d $workdir ; then
        echo ""
else
        mkdir $workdir
fi

cd $workdir

while :
do
    rm -f $workdir/*.log
    $kobukiRTC
    sleep 5
done
```

Make it executable:

```bash
$ sudo chmod 755 /etc/kobuki.sh
```

Then insert the following line into `/etc/rc.local`, just before `exit 0`:

```bash
/etc/kobuki.sh 2>&1 | perl -p -e 's/\n/\r\n/g' 1>&2 &
exit 0
```

Now, whenever Raspberry Pi boots, the KobukiAIST component will automatically start.

Even if the component exits, it will automatically restart after 5 seconds.

As long as Kobuki remains powered on, the component will continue running.

## Operating the Kobuki Component

### Using TkJoystick

TkJoystick is a sample component included with OpenRTM-aist-Python.

However, it outputs only joystick X-Y values and differential wheel speeds, and does not provide a 2D velocity vector (`TimedVelocity2D`) output.

Try modifying TkJoystick to output a `TimedVelocity2D` and connect it to Kobuki.

Original TkJoystick RTC:

- http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/OpenRTM_aist/examples/TkJoyStick/

Windows installation locations:

```text
C:\Program Files (x86)\OpenRTM-aist\x.y\examples\Python\TkJoyStick
C:\Program Files\OpenRTM-aist\x.y\examples\Python\TkJoyStick
```

### Hint

Inside `TkJoystick.py`, the left and right wheel speeds are already calculated.

Using mobile robot kinematics, you can derive:

- Linear velocity (v)
- Angular velocity (ω)

Refer to:

- Mathematics of Wheeled Mobile Robots
  http://www.mech.tohoku-gakuin.ac.jp/rde/contents/course/robotics/wheelrobot.html

The `TimedVelocity2D` data structure is:

```cpp
struct Velocity2D
{
  double va; // angular velocity [rad/s]
  double vx; // forward velocity [m/s]
  double vy; // lateral velocity [m/s]
};

struct TimedVelocity2D
{
  Time tm;
  Velocity2D data;
};
```

(Translation continues into autonomous movement control, sensor mapping, and the KobukiAutoMove example.)


### Autonomous Navigation

Next, let's make Kobuki move autonomously using its sensors.

Kobuki is equipped with:

- Bumper sensors
- Proximity sensors (near/far)
- Cliff sensors

In this example, we will implement a simple Roomba-like behavior:

1. Move forward continuously.
2. When a wall or obstacle is detected:
   - Move backward slightly.
   - Rotate.
   - Resume moving forward.

(Actual Roomba robots use more sophisticated algorithms.)

The sensor outputs of the KobukiAIST RTC are shown below.

Note that the IR sensors are intended to receive infrared signals from the docking station and cannot be used for obstacle detection.

Therefore, only the bumper and cliff sensors should be used for obstacle and cliff detection.

<table class="table-alt">
<tr><th>No.</th><th>Enum</th><th>Description</th></tr>
<tr><td>0</td><td>RIGHT_BUMPER</td><td>Right bumper</td></tr>
<tr><td>1</td><td>CENTER_BUMPER</td><td>Center bumper</td></tr>
<tr><td>2</td><td>LEFT_BUMPER</td><td>Left bumper</td></tr>
<tr><td>3</td><td>RIGHT_WHEEL_DROP</td><td>Right wheel drop</td></tr>
<tr><td>4</td><td>LEFT_WHEEL_DROP</td><td>Left wheel drop</td></tr>
<tr><td>5</td><td>RIGHT_CLIFF</td><td>Right cliff sensor</td></tr>
<tr><td>6</td><td>CENTER_CLIFF</td><td>Center cliff sensor</td></tr>
<tr><td>7</td><td>LEFT_CLIFF</td><td>Left cliff sensor</td></tr>
<tr><td>8</td><td>RIGHT_IRFAR_RIGHT</td><td>Right IR / Dock Right Far</td></tr>
<tr><td>9</td><td>RIGHT_IRFAR_CENTER</td><td>Right IR / Dock Center Far</td></tr>
<tr><td>10</td><td>RIGHT_IRFAR_LEFT</td><td>Right IR / Dock Left Far</td></tr>
<tr><td>11</td><td>RIGHT_IRNEAR_RIGHT</td><td>Right IR / Dock Right Near</td></tr>
<tr><td>12</td><td>RIGHT_IRNEAR_CENTER</td><td>Right IR / Dock Center Near</td></tr>
<tr><td>13</td><td>RIGHT_IRNEAR_LEFT</td><td>Right IR / Dock Left Near</td></tr>
<tr><td>14</td><td>CENTER_IRFAR_RIGHT</td><td>Center IR / Dock Right Far</td></tr>
<tr><td>15</td><td>CENTER_IRFAR_CENTER</td><td>Center IR / Dock Center Far</td></tr>
<tr><td>16</td><td>CENTER_IRFAR_LEFT</td><td>Center IR / Dock Left Far</td></tr>
<tr><td>17</td><td>CENTER_IRNEAR_RIGHT</td><td>Center IR / Dock Right Near</td></tr>
<tr><td>18</td><td>CENTER_IRNEAR_CENTER</td><td>Center IR / Dock Center Near</td></tr>
<tr><td>19</td><td>CENTER_IRNEAR_LEFT</td><td>Center IR / Dock Left Near</td></tr>
<tr><td>20</td><td>LEFT_IRFAR_RIGHT</td><td>Left IR / Dock Right Far</td></tr>
<tr><td>21</td><td>LEFT_IRFAR_CENTER</td><td>Left IR / Dock Center Far</td></tr>
<tr><td>22</td><td>LEFT_IRFAR_LEFT</td><td>Left IR / Dock Left Far</td></tr>
<tr><td>23</td><td>LEFT_IRNEAR_RIGHT</td><td>Left IR / Dock Right Near</td></tr>
<tr><td>24</td><td>LEFT_IRNEAR_CENTER</td><td>Left IR / Dock Center Near</td></tr>
<tr><td>25</td><td>LEFT_IRNEAR_LEFT</td><td>Left IR / Dock Left Near</td></tr>
<tr><td>26</td><td>KOBUKI_DOCKED</td><td>Docking completed</td></tr>
</table>

To receive these sensor outputs, you will need:

- One InPort of type `RTC::TimedBooleanSeq`
- One OutPort of type `TimedVelocity2D` for sending velocity commands to Kobuki

<table class="table-alt">
<tr><th colspan="2" style="text-align:center;">Basic Profile</th></tr>
<tr><td>Component Name</td><td>KobukiAutoMove</td></tr>
<tr><td>Module Description</td><td>Kobuki auto move component</td></tr>
<tr><td>Version</td><td>1.0.0</td></tr>
<tr><td>Vendor</td><td>AIST</td></tr>

<tr><th colspan="2" style="text-align:center;">Activities</th></tr>
<tr><td colspan="2">onInitialize, onFinalize, onActivated, onDeactivated, onExecute</td></tr>

<tr><th colspan="2" style="text-align:center;">Data Ports</th></tr>

<tr><td colspan="2">[in] bumper</td></tr>
<tr><td>Description</td><td>Sensor information (true: obstacle detected; false: no obstacle)</td></tr>
<tr><td>Data Type</td><td>TimedBooleanSeq</td></tr>
<tr><td>Details</td><td>data[0]: Right bumper, data[1]: Center bumper, ... data[7]: Left cliff sensor</td></tr>

<tr><td colspan="2">[out] targetVelocity</td></tr>
<tr><td>Description</td><td>Mobile robot velocity vector</td></tr>
<tr><td>Data Type</td><td>TimedVelocity2D</td></tr>
<tr><td>Details</td><td>vx: linear velocity, vy: 0.0, va: angular velocity</td></tr>
<tr><td>Units</td><td>vx [m/s], va [rad/s]</td></tr>
</table>

Using the information above, try creating a simple RTC that enables Kobuki to move autonomously.

If you encounter problems connecting components, refer to the Troubleshooting section.

#### Hint

As shown earlier, Kobuki velocity commands use the `TimedVelocity2D` type:

```cpp
struct Velocity2D
{
  double va; // angular velocity [rad/s]
  double vx; // forward velocity [m/s]
  double vy; // lateral velocity [m/s]
};

struct TimedVelocity2D
{
  Time tm;
  Velocity2D data;
};
```

For a differential-drive robot:

```cpp
vy = 0.0
```

Moving forward:

```cpp
va = 0.0;
vx = 0.2;
vy = 0.0;
```

Moving backward:

```cpp
va = 0.0;
vx = -0.2;
vy = 0.0;
```

Rotating in place:

```cpp
va = 1.0;
vx = 0.0;
vy = 0.0;
```

<div align="center"><a href="timed_velocity_2d.png"><img src="timed_velocity_2d.png" width="60%;"></a></div>
<div align="center"><strong>Mobile Robot Coordinate System and TimedVelocity2D</strong></div>

When data arrives at the InPort, read the bumper information.

The bumper status is stored in the `.data` array of the `TimedBooleanSeq` object.

From the table above:

- data[0] = Right bumper
- data[1] = Center bumper
- data[2] = Left bumper

If any of these values becomes `true`, a collision has been detected.

The robot should then:

1. Move backward.
2. Rotate.
3. Move forward again.

Set the appropriate values in the `TimedVelocity2D` structure and write them to the OutPort to send velocity commands to Kobuki.

The control algorithm is illustrated below.

<div align="center"><a href="kobuki_auto.png"><img src="kobuki_auto.png" width="50%;"></a></div>
<div align="center"><strong>Flowchart</strong></div>

Ideally, the robot would measure how far it has moved backward or rotated and use feedback control.

For simplicity, however, you may use sleep functions.

On Linux:

```cpp
coil::sleep(coil::TimeValue(0.01)); // wait 10 ms
```

On Windows, the accuracy of `coil::sleep()` is poor, so the standard `Sleep()` function is recommended.

Using these hints, try implementing a control component that enables Kobuki to move autonomously.

## Reference Solutions

Reference implementations of the modified TkJoyStick component and the autonomous navigation component are provided below:

- [GUI Joystick:TkJoyStick.zip](TkJoyStick.zip)

- [Kobuki Autonomous Controller:KobukiAutoMove.zip](KobukiAutoMove.zip)
