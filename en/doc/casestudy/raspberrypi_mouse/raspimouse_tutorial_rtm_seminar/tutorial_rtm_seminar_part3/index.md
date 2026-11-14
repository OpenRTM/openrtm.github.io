---
layout: page
title: tutorial (rtm workshop, part 3)
---

<!-- Title: チュートリアル(RTM講習会、第3部) -->
#contents

On this page, you will build an RT system that integrates the Raspberry Pi Mouse and LEGO Mindstorms EV3.

Use the Raspberry Pi Mouse as an access point, and connect both the laptop PC and EV3 to the access point.

*Please make sure to use the EV3 with the same number as the Raspberry Pi Mouse.*

<br>

<div align="center"><a href="robomech2018_8.jpg"><img src="robomech2018_8.jpg" width="70%;"></a></div>
<br>


## EV3 Devices
The following devices are included with the EV3.

<table class="table-alt">
  <tr>
    <td><strong>Gyro Sensor</strong><br> <div align="center"><a href="https://afrel.co.jp/pages-assets/images/technology/ev3/technology-ev3-img7.jpg"><img src="https://afrel.co.jp/pages-assets/images/technology/ev3/technology-ev3-img7.jpg" width="30%;"></a></div></td>
    <td>Angle Mode: Accuracy +/- 3°<br> Angular Velocity Mode: Up to 440 deg/sec <br> Sampling Rate: 1,000 Hz</td>
  </tr>
  <tr>
    <td><strong>Color Sensor</strong> <br> <div align="center"><a href="https://afrel.co.jp/pages-assets/images/technology/ev3/technology-ev3-img5.jpg"><img src="https://afrel.co.jp/pages-assets/images/technology/ev3/technology-ev3-img5.jpg" width="30%;"></a></div></td>
    <td>Measurement: Reflected red light, ambient brightness, color <br> Number of detectable colors: 8 (none, black, blue, green, yellow, red, white, brown)<br> Sampling Rate: 1,000 Hz <br> Distance: Approximately 1 mm to 18 mm (Afrel measured value)</td>
  </tr>
  <tr>
    <td><strong>Touch Sensor</strong><br> <div align="center"><a href="https://afrel.co.jp/pages-assets/images/technology/ev3/technology-ev3-img6.jpg"><img src="https://afrel.co.jp/pages-assets/images/technology/ev3/technology-ev3-img6.jpg" width="30%;"></a></div></td>
    <td>On (1), Off (0) <br> Switch travel distance: Approximately 4 mm</td>
  </tr>
  <tr>
    <td><strong>Ultrasonic Sensor</strong><br> <div align="center"><a href="https://afrel.co.jp/pages-assets/images/technology/ev3/technology-ev3-img8.jpg"><img src="https://afrel.co.jp/pages-assets/images/technology/ev3/technology-ev3-img8.jpg" width="30%;"></a></div></td>
    <td>Distance measurement range: 3 cm to 250 cm <br> Distance measurement accuracy: +/- 1 cm <br> Front LED indicator: Lit = ultrasonic transmission, Blinking = ultrasonic observation</td>
  </tr>
  <tr>
    <td><strong>EV3 L Motor</strong><br> <div align="center"><a href="https://afrel.co.jp/images/2013/04/45502_LargeMotor.jpg"><img src="https://afrel.co.jp/images/2013/04/45502_LargeMotor.jpg" width="30%;"></a></div></td>
    <td>Feedback: 1° increments <br> Rotation Speed: 160 to 170 RPM <br> Rated Torque: 0.21 N・m (30oz*in) <br> Stall Torque: 0.42 N・m (60oz*in) <br> Weight: 76 g</td>
  </tr>
  <tr>
    <td><strong>EV3 M Motor</strong> <br> <div align="center"><a href="https://afrel.co.jp/images/2013/04/45503_MediumMotor.jpg"><img src="https://afrel.co.jp/images/2013/04/45503_MediumMotor.jpg" width="30%;"></a></div></td>
    <td>Feedback: 1° increments <br> Rotation Speed: 240 to 250 RPM <br> Rated Torque: 0.08 N・m (11oz*in) <br> Stall Torque: 0.12 N・m (17oz*in) <br> Weight: 36 g</td>
  </tr>
</table>


## Assembling the EV3
First, mount the EV3 main unit onto the base.

<br>

<div align="center"><a href="robomech2018_12.jpg"><img src="robomech2018_12.jpg" width="70%;"></a></div>
<br>

Next, connect the EV3 and the left/right L motors using 25 cm cables.

<br>

<table class="table-alt">
  <tr>
    <td>Right L Motor</td>
    <td>Port C</td>
    <td>25 cm Cable</td>
  </tr>
  <tr>
    <td>Left L Motor</td>
    <td>Port B</td>
    <td>25 cm Cable</td>
  </tr>
</table>

<br>

<div align="center"><a href="robomech2018_13.jpg"><img src="robomech2018_13.jpg" width="70%;"></a></div>
<br>

The port numbers and device names to connect the cables are labeled.

If you want to attach other devices, refer to [Tutorial (EV3)]({{ site.baseurl }}/en/doc/casestudy/lego_mindstorm/lego_rtm_seminar/tutorial_ev3_win#toc30).

## Connecting to the EV3
### Connecting the Laptop PC and Raspberry Pi
Complete the procedure in [Part 2]({{ site.baseurl }}/en/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_ubuntu_part2) up to verifying operation on the actual hardware.
At this point, the laptop PC and the Raspberry Pi access point should already be connected.

<br>

<div align="center"><a href="robomech2018_9.jpg"><img src="robomech2018_9.jpg" width="50%;"></a></div>
<br>


## Turning the EV3 Power On/Off

### Turning the Power On

Press the center button to power on the EV3.

<br>

<div align="center"><a href="ev3_on.jpg"><img src="ev3_on.jpg" width="50%;"></a></div>
<br>

### Turning the Power Off

To turn off the EV3, press the Back button at the upper-left of the EV3 unit on the initial screen and select "Power Off".

<br>

<div align="center"><a href="ev3_off.jpg"><img src="ev3_off.jpg" width="50%;"></a></div>
<br>

<br>

<div align="center"><a href="s_DSC01033.JPG"><img src="s_DSC01033.JPG" width="50%;"></a></div>
<br>

### Reboot

To reboot the EV3, press the Back button at the upper-left of the EV3 unit on the initial screen and select "Reboot".

### Reset

If ev3dev stops during startup, press and hold the Center button, Back button (upper-left), and Left button simultaneously. When the screen turns off, release the Back button to reboot.

<br>

<div align="center"><a href="ev3_reset.jpg"><img src="ev3_reset.jpg" width="50%;"></a></div>
<br>


### Connecting Raspberry Pi and EV3

Turn on the EV3.

After startup, it automatically connects to the Raspberry Pi.
If the connection is successful, the IP address is displayed in the upper-left corner of the EV3 screen.
The displayed IP address will be 192.168.11.yyy.

<br>

<div align="center"><a href="tutorial_ev3_irex25.png"><img src="tutorial_ev3_irex25.png" width="50%;"></a></div>
<br>


#### Starting the Name Server and RTC
Start the Name Server and RTC using the EV3 on-screen interface.

From the EV3 operation screen, select "File Browser" → "scripts".

The Name Server and RTC are started by executing the **start_rtcs.sh** script.

```
 ------------------------------
 192.168.11.yyy
 ------------------------------
         File Browser
 ------------------------------
 /home/robot/scripts
 ------------------------------
 ../
 Component/
 ・・
 [start_rtcs.sh                 ]
 ------------------------------
```

<br>

<div align="center"><a href="tutorial_ev3_irex32.png"><img src="tutorial_ev3_irex32.png" width="70%;"></a></div>
<br>


### Adding the Name Server
From RTSystemEditor, connect to the Name Server at 192.168.11.yyy.

<br>

<div align="center"><div align="center"><a href="tutorial_raspimouse0.png"><img src="tutorial_raspimouse0.png" width="50%;"></a></div>;  <div align="center"><a href="tutorial_ev3_irex22.png"><img src="tutorial_ev3_irex22.png" width="50%;"></a></div>;</div>
<br>
<br>

At this point, the Name Service View in RTSystemEditor contains the Name Servers for localhost, 192.168.11.1, and 192.168.11.yyy.

The RTC registered in the Name Server at 192.168.11.yyy is named **EducatorVehicle1**.

<br>

<div align="center"><a href="robomech2018_10.jpg"><img src="robomech2018_10.jpg" width="70%;"></a></div>
<br>

- localhost
  - RobotController0
- 192.168.11.1
  - RaspberryPiMouseRTC0
  - OpenCVCamera0
  - artp0
- 192.168.11.yyy
  - EducatorVehicle1

## Summary

In this tutorial, you learned:

- How to configure a network in which the Raspberry Pi Mouse acts as an access point and both a laptop PC and EV3 connect to it.
- The specifications and functions of the sensors and motors included with the EV3.
- How to assemble the EV3 and connect the left and right motors to the designated ports.
- How to power on, power off, reboot, and reset the EV3.
- How to connect the EV3 to the Raspberry Pi and verify the assigned IP address.
- How to start the Name Server and RTC on the EV3 using the start_rtcs.sh script.
- How to add the EV3 Name Server to RTSystemEditor and confirm the registered RTCs.

By completing this tutorial, you have learned how to assemble and connect the EV3, establish communication with the Raspberry Pi, start the required RT components, and integrate the EV3 into the RT system environment.


## Operation Check

Connect RaspberryPiMouseRTC0 (192.168.11.1) and EducatorVehicle1 (192.168.11.yyy) on the system diagram.

By connecting the current velocity output of EducatorVehicle0 to the target velocity input of RaspberryPiMouseRTC0, the Raspberry Pi Mouse will follow the movement of the EV3.

<br>

<div align="center"><a href="robomech2018_14.jpg"><img src="robomech2018_14.jpg" width="70%;"></a></div>
<br>

Activate the RTC and rotate the wheels of the Educator Vehicle. The Raspberry Pi Mouse will move accordingly.

<br>

<div align="center"><a href="robomech2018_11.jpg"><img src="robomech2018_11.jpg" width="70%;"></a></div>
<br>

## Optional Exercises

This completes the main practical training. If you have extra time, try the following exercises.

### Controlling the Raspberry Pi Mouse Using the EV3 Touch Sensors

Create an RT system that moves the Raspberry Pi Mouse forward and backward using the on/off state of the EV3 touch sensors.

<br>

<!-- div align="center"><a href="https://afrel.co.jp/cms/wp-content/uploads/2013/04/45507_TouchSensor.jpg"><img src="https://afrel.co.jp/cms/wp-content/uploads/2013/04/45507_TouchSensor.jpg" width="70%;"></a></div-->
<div align="center"><strong>Touch Sensor</strong></div>
<br>

#### Connecting the Touch Sensors

Connect the EV3 and the touch sensors using 35 cm cables.

<table class="table-alt">
  <tr>
    <th>Right Touch Sensor</th>
    <th>Port 3</th>
    <th>35 cm Cable</th>
  </tr>
  <tr>
    <td>Left Touch Sensor</td>
    <td>Port 1</td>
    <td>35 cm Cable</td>
  </tr>
</table>

#### Creating the RTC

Create an RTC with the following specifications.

<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th>SampleTouchSensor</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>touch</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedBooleanSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Touch sensor on/off state</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>target_velocity</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVelocity2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Target velocity</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>speed</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0.2</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Straight-line speed when the touch sensor is on</td>
  </tr>
</table>

Enable onExecute in the Activity settings.

Implement the onExecute function of SampleTouchSensor as follows.

```cpp
 RTC::ReturnCode_t SampleTouchSensor::onExecute(RTC::UniqueId ec_id)
 {
 	//新規データの確認
 	if (m_touchIn.isNew())
 	{
 		//データの読み込み
 		m_touchIn.read();
 		//配列の要素数が1以上かを確認
 		if (m_touch.data.length() == 2)
 		{
 			//0番目のデータがオンの場合は直進する指令を出力
 			//0番目のデータは右側のタッチセンサに対応
 			if (m_touch.data[0])
 			{
 				//目標速度を格納
 				m_target_velocity.data.vx = m_speed;
 				m_target_velocity.data.vy = 0;
 				m_target_velocity.data.va = 0;
 				setTimestamp(m_target_velocity);
 				//データ出力
 				m_target_velocityOut.write();
 			}
 			//1番目のデータがオンの場合は後退する指令を出力
 			//1番目のデータは左側のタッチセンサに対応
 			else if (m_touch.data[1])
 			{
 				//目標速度を格納
 				m_target_velocity.data.vx = -m_speed;
 				m_target_velocity.data.vy = 0;
 				m_target_velocity.data.va = 0;
 				setTimestamp(m_target_velocity);
 				//データ出力
 				m_target_velocityOut.write();
 			}
 			//オフの場合は停止する
 			else
 			{
 				//目標速度を格納
 				m_target_velocity.data.vx = 0;
 				m_target_velocity.data.vy = 0;
 				m_target_velocity.data.va = 0;
 				setTimestamp(m_target_velocity);
 				//データ出力
 				m_target_velocityOut.write();
 			}
 		}
 	}
   return RTC::RTC_OK;
 }
```

#### Creating the RT System

After connecting the data ports as shown below, turning the touch sensors on and off will move the Raspberry Pi forward and backward.

<br>

<div align="center"><a href="robomech2018_15.jpg"><img src="robomech2018_15.jpg" width="70%;"></a></div>
<br>

### Operating Two Robots Simultaneously with a Joystick Component

Create an RT system that controls both the Raspberry Pi Mouse and EV3 using the GUI joystick shown below.

<br>

<div align="center"><a href="robomech2018_18.jpg"><img src="robomech2018_18.jpg" width="50%;"></a></div>
<br>

#### Starting the Joystick Component

The joystick component is included in the OpenRTM-aist Python sample programs (**TkJoyStickComp.py**).

For Windows 8.1, start the joystick component by selecting "Start" > "Apps View (lower-right arrow)" > "OpenRTM-aist 1.2.0" > "Python_Examples", then double-clicking "TkJoyStickComp.bat" in Explorer.

#### Creating the RTC

Since the OutPort data type of TkJoyStickComp.py is **TimedFloatSeq**, you need to create an RTC that converts it to **TimedVelocity2D**.

Create an RTC with the following specifications.

<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th>FloatSeqToVelocity</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>in</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedFloatSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Data before conversion</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>out</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVelocity2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Data after conversion</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>rotation_by_position</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>-0.02</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Angular velocity change per joystick X-coordinate position</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>velocity_by_position</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0.002</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Velocity change per joystick Y-coordinate position</td>
  </tr>
</table>

Enable onExecute in the Activity settings.

Edit the onExecute function as follows.

```cpp
 RTC::ReturnCode_t FloatSeqToVelocity::onExecute(RTC::UniqueId ec_id)
 {
 	//新規データの確認
 	if (m_inIn.isNew())
 	{
 		//データの読み込み
 		m_inIn.read();
 		//配列のデータ数確認
 		if (m_in.data.length() >= 2)
 		{
 			//目標速度格納
 			m_out.data.vx = m_in.data[1] * m_velocity_by_position;
 			m_out.data.vy = 0;
 			m_out.data.va = m_in.data[0] * m_rotation_by_position;
 			setTimestamp(m_out);
 			//目標速度出力
 			m_outOut.write();
 		}
 	}
   return RTC::RTC_OK;
 }
```

#### Creating the RT System

Connect the data ports as shown below.

<br>

<div align="center"><a href="robomech2018_16.jpg"><img src="robomech2018_16.jpg" width="70%;"></a></div>
<br>

### Making the EV3 Speak

If a string (TimedString type) is input to the port named **sound** of EducatorVehicleRTC, the EV3 will speak the text.

#### Creating the RTC

Create an RTC with the following specifications.

<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th>SpeechSample</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>out</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedString</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>String to be spoken</td>
  </tr>
</table>

Enable onExecute in the Activity settings.

Edit the onExecute function as follows.

```cpp
 RTC::ReturnCode_t SpeechSample::onExecute(RTC::UniqueId ec_id)
 {
 	std::cout << "Please input: ";
 	std::string ret;
 	//文字入力
 	std::cin >> ret;
 	//データに格納
 	m_out.data = CORBA::string_dup(ret.c_str());
 	setTimestamp(m_out);
 	//データ出力
 	m_outOut.write();
 
   return RTC::RTC_OK;
 }
```

When outputting a string (`const char*`) through a data port, you must copy the string using the **CORBA::string_dup function**.

```cpp
 m_out.data= CORBA::string_dup("abc");
```

#### Creating the RT System

Connect the data ports as shown below.

<br>

<div align="center"><a href="robomech2018_17.jpg"><img src="robomech2018_17.jpg" width="70%;"></a></div>
<br>

### Marker Following

When the Raspberry Pi Mouse starts, the OpenCVCamera component and the artp component are also started.

The OpenCVCamera component acquires images, and the artp component calculates and outputs the marker position and orientation from the image data.

<br>

<div align="center"><a href="robomech2018_19.jpg"><img src="robomech2018_19.jpg" width="70%;"></a></div>
<br>

Create an RT system in which the Raspberry Pi Mouse follows a marker.

#### Mounting the Camera

First, mount the camera on the Raspberry Pi Mouse.

Attach the following base parts to the Raspberry Pi Mouse.

<br>

<div align="center"><a href="robomech2018_23.jpg"><img src="robomech2018_23.jpg" width="70%;"></a></div>
<br>

Attach Part ① to the top of the Raspberry Pi Mouse.

Install it by pushing it in from the left side.

<br>

<div align="center"><a href="s_DSC09198.JPG"><img src="s_DSC09198.JPG" width="70%;"></a></div>
<br>

<br>

At this time, attach it so that the protrusion on the left side grips the plate.

<br>

<div align="center"><a href="robomech2018_22.jpg"><img src="robomech2018_22.jpg" width="70%;"></a></div>
<br>

Insert Part ② into the left side of Part ① from above.

<br>

<div align="center"><a href="s_DSC09201.JPG"><img src="s_DSC09201.JPG" width="70%;"></a></div>
<br>

<br>

<br>

<div align="center"><a href="robomech2018_25.jpg"><img src="robomech2018_25.jpg" width="70%;"></a></div>
<br>

Insert Part ③ into Part ② from the left side.

<br>

<div align="center"><a href="robomech2018_24.jpg"><img src="robomech2018_24.jpg" width="70%;"></a></div>
<br>

Finally, mount the camera and connect the USB cable to the Raspberry Pi to complete the assembly.

<br>

<div align="center"><a href="s_DSC01096.JPG"><img src="s_DSC01096.JPG" width="70%;"></a></div>
<br>

<br>

<br>

<div align="center"><a href="s_DSC01098.JPG"><img src="s_DSC01098.JPG" width="70%;"></a></div>
<br>

<br>


#### Creating the RTC

Create an RTC with the following specifications.

<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th>testARToolKit</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>marker_pos</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedPose3D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Marker position</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>target_vel</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVelocity2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Target velocity of the robot</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>x_distance</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0.5</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Target distance to the marker (X axis)</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>y_distance</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Target distance to the marker (Y axis)</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>x_speed</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0.1</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Movement speed in the X-axis direction</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>r_speed</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0.2</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Movement speed in the rotational direction</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>error_range_x</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0.1</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Allowable range for the target distance in the X-axis direction</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>error_range_y</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0.05</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Allowable range for the target distance in the Y-axis direction</td>
  </tr>
</table>

Set onExecute to ON in the Activity settings.

Edit onExecute as follows.

```cpp
 RTC::ReturnCode_t testARToolKit::onExecute(RTC::UniqueId ec_id)
 {
 	//新規データの確認
 	if (m_marker_posIn.isNew())
 	{
 		m_target_vel.data.vx = 0;
 		m_target_vel.data.vy = 0;
 		m_target_vel.data.va = 0;
 
 		//データの読み込み
 		m_marker_posIn.read();
 		//マーカーの位置(X軸)が目標距離(X軸)よりも大きい場合
 		if (m_marker_pos.data.position.x > m_x_distance + m_error_range_x/2.0)
 		{
 			m_target_vel.data.vx = m_x_speed;
 		}
 		//マーカーの位置(X軸)が目標距離(X軸)よりも小さい場合
 		else if (m_marker_pos.data.position.x < m_x_distance - m_error_range_x/2.0)
 		{
 			m_target_vel.data.vx = -m_x_speed;
 		}
 		//マーカーの位置(Y軸)が目標距離(Y軸)よりも大きい場合
 		else if (m_marker_pos.data.position.y > m_y_distance + m_error_range_y/2.0)
 		{
 			m_target_vel.data.va = m_r_speed;
 		}
 		//マーカーの位置(Y軸)が目標距離(Y軸)よりも小さい場合
 		else if (m_marker_pos.data.position.y < m_y_distance - m_error_range_y/2.0)
 		{
 			m_target_vel.data.va = -m_r_speed;
 		}
 		setTimestamp(m_target_vel);
 		//データ書き込み
 		m_target_velOut.write();
 	}
   return RTC::RTC_OK;
 }
```

#### Creating the RT System

Connect the data ports as shown below.

<br>

<div align="center"><a href="robomech2018_20.jpg"><img src="robomech2018_20.jpg" width="70%;"></a></div>
<br>

Activate the RTC, move the marker in front of the camera, and check whether the Raspberry Pi Mouse moves.

## Summary

In this tutorial, you learned:

- How to build an RT system that links the Raspberry Pi Mouse and LEGO Mindstorms EV3.
- How to connect the laptop PC, Raspberry Pi Mouse, and EV3 through the Raspberry Pi Mouse access point.
- How to assemble the EV3 and connect its motors and sensors.
- How to start the Name Server and RTCs on the EV3.
- How to connect RTCs in RTSystemEditor and verify coordinated operation between the EV3 and Raspberry Pi Mouse.
- How to create RTCs for touch sensor control, joystick-based control, EV3 speech output, and marker following.
- How to mount a camera on the Raspberry Pi Mouse and use marker position data to control robot movement.

By completing this tutorial, you have learned how to construct and operate RT systems that integrate the Raspberry Pi Mouse, EV3, sensors, joystick input, speech output, and camera-based marker following.
