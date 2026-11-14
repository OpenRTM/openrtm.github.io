---
layout: page
title: "openrtm integration plugin for choreonoid, python version tutorial (tankjoystick)"
---

This page explains the procedure for operating the Tank model with a gamepad using the Choreonoid OpenRTM integration plugin Python version.
The model used and the RTC to be created are almost the same as those in the [tutorial on the official Choreonoid page](https://choreonoid.org/ja/manuals/1.7/openrtm/tank-joystick-project.html).


<br>

<div align="center"><a href="choreonoid-openrtm-py60.png"><img src="choreonoid-openrtm-py60.png" width="50%;"></a></div>
<br>


#contents

## Creating the RTC

This chapter explains the procedure for developing an RTC that performs input and output for actuators, sensors, and similar elements on the simulator.

### Starting RTC Builder

First, create a source code template with RTC Builder.
Install OpenRTM-aist in order to use RTC Builder.

- [OpenRTM-aist.2.0.1-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-cpp/openrtm-aist-cpp_1_1_2_release)


After installation is complete, start RTC Builder and create the template.
On Windows 8.1, you can start it by clicking "Start" > "Apps view (lower-right arrow)" > "OpenRTM-aist 2.0.1" > "OpenRTP".


The following can be used as a reference for the creation procedure.

- [RTCBuilder-1.1.0]({{ site.baseurl }}/ja/doc/toolmanuals/rtcbuilder-1_1_0/)


### Creating the RTC Template

The specification of the RTC to be created is as follows. Select **Python** as the language.

<br>

<div align="center"><a href="https://cloud.githubusercontent.com/assets/6216077/25479366/8b893cd4-2b7f-11e7-958c-8ba2052c448d.png"><img src="https://cloud.githubusercontent.com/assets/6216077/25479366/8b893cd4-2b7f-11e7-958c-8ba2052c448d.png" width="50%;"></a></div>
<br>

<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th><strong>TankIoRTC_Py</strong></th>
  </tr>
  <tr>
    <td colspan="2">CENTER: <strong>InPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>velocities</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVelocity2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Target velocity of the vehicle body</td>
  </tr>
  <tr>
    <td colspan="2"> <strong>InPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>torques</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedDoubleSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Joint torque of the turret section</td>
  </tr>
  <tr>
    <td colspan="2"><strong>InPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>lightSwitch</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedBooleanSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Light on/off</td>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>angles</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>PanTiltAngles</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Joint angles of the turret section</td>
  </tr>
  <tr>
    <td colspan="2"> <strong>Language</strong></td>
  </tr>
  <tr>
    <td colspan="2">Python</td>
  </tr>
</table>


### Editing the Source Code

The generated source code contains a class with the RTC module name (for TankIoRTC_Py, class TankIoRTC_Py), so add the following functions to that class.

<table class="table-alt">
  <tr>
    <th>Function Name</th>
    <th>Argument</th>
    <th>Content</th>
  </tr>
  <tr>
    <td>setBody</td>
    <td>body</td>
    <td>Function for setting the Body object</td>
  </tr>
  <tr>
    <td>inputFromSimulator</td>
    <td></td>
    <td>Function for writing processing such as outputting sensor measurement values from an outport. Executed after the simulation step</td>
  </tr>
  <tr>
    <td>outputToSimulator</td>
    <td></td>
    <td>Function for writing processing such as inputting actuator torques from an inport. Executed before the simulation step</td>
  </tr>
</table>


Specifically, write the following source code.



```
 class TankIoRTC_Py(OpenRTM_aist.DataFlowComponentBase):
 	(省略)
 
 	#ボディオブジェクト設定関数
 	def setBody(self, body):
 		
 		self.ioBody = body
 		
 		#Linkオブジェクト取得
 		self.cannonY = self.ioBody.link("CANNON_Y")
 		self.cannonP = self.ioBody.link("CANNON_P")
 		self.crawlerL = self.ioBody.link("CRAWLER_TRACK_L")
 		self.crawlerR = self.ioBody.link("CRAWLER_TRACK_R")
 		
 		#Lightオブジェクト取得
 		self.light = self.ioBody.getLight("MainLight")
 		
 		
 	#センサの計測値などをアウトポートから出力する処理等を記述する関数
 	#シミュレーションステップ後に実行される
 	def inputFromSimulator(self):
 		if self.ioBody:
 			#砲台の角度取得、格納
 			self._d_angles.pan = self.cannonY.q
 			self._d_angles.tilt = self.cannonP.q
 
 			#砲台の角度出力
 			OpenRTM_aist.setTimestamp(self._d_angles)
 			self._anglesOut.write()
 
 
 	#アクチュエータのトルクなどをインポートから入力する処理等を記述する関数
 	#シミュレーションステップ前に実行される
 	def outputToSimulator(self):
 		if self.ioBody:
 			#砲台のトルク入力
 			if self._torquesIn.isNew():
 				data = self._torquesIn.read()
 				self.cannonY.u = data.data[0]
 				self.cannonP.u = data.data[1]
 			#車体の速度入力
 			if self._velocitiesIn.isNew():
 				data = self._velocitiesIn.read()
 				vx = data.data.vx
 				va = data.data.va
 				
 				rms = (vx + va*self._wheel_distance[0])/self._wheel_radius[0]
 				lms = (vx - va*self._wheel_distance[0])/self._wheel_radius[0]
 				
 				#クローラーの速度入力
 				self.crawlerL.dq = lms
 				self.crawlerR.dq = rms
 			#ライトのオンオフ入力
 			if self._lightSwitchIn.isNew():
 				data = self._lightSwitchIn.read()
 				
 				self.light.on(data.data[0])
 				self.light.notifyStateChange()
 
 
```

First, in the setBody function, the Link objects and Light object to be controlled are obtained.
Link and Light objects can be obtained by name.

You can check Link names by selecting the item corresponding to the model and then displaying the "Link" tab from the lower-left view.


<br>

<div align="center"><a href="choreonoid-openrtm-py33.png"><img src="choreonoid-openrtm-py33.png" width="50%;"></a></div>
<br>


I do not know how to check Light names, so please check the official Choreonoid website.



```
 	def setBody(self, body):
 		self.ioBody = body
 
 		self.cannonY = self.ioBody.link("CANNON_Y")
 		
 		(省略)
 		
 		self.light = self.ioBody.getLight("MainLight")
```




Joint angles can be obtained using the **q** variable.

```
 self._d_angles.pan = self.cannonY.q
```



Joint velocity input can be reflected in the simulator by storing values in the **dq** variable, and torque input by storing values in the **u** variable.

```
 self.crawlerL.dq = lms
```

```
 self.cannonY.u = data.data[0]
```



For turning the light on and off, store a bool variable in the **on** variable.

```
 self.light.on =  data.data[0]
```




## Creating the RT System

### Starting Choreonoid

#### Windows

On Windows, double-click **bin/chorenoid.exe** in the folder where Choreonoid was extracted.

#### Ubuntu

On Ubuntu, enter **choreonoid** from the command line.



### Adding Items

#### World and Simulator

First, add a world item and a simulator item. From File > New, select and add **World** and **AIST Simulator**.
* The order of displayed items may change, so the screen may differ from this image.

<br>

<div align="center"><a href="choreonoid-openrtm-py31.png"><img src="choreonoid-openrtm-py31.png" width="50%;"></a></div>
<br>



At this point, the item tree is as follows.

```
 World(World item)
    |-AISTSimulator(AIST Simulator)
```

For an overview of the item tree and how to move items, refer to the following page.

- [Projects and Items — Choreonoid Development Version Documentation](https://choreonoid.org/ja/documents/latest/basics/item.html#basics-item-tree)


#### Model


Next, add the environment and Tank models.

From File > Import, select **OpenHRP Model File**, and then load the following files.

- {Choreonoid installation directory}/share/model/tank/tank.wrl
- {Choreonoid installation directory}/share/model/Labo1/Labo1.wrl


<br>

<div align="center"><a href="https://cloud.githubusercontent.com/assets/6216077/25477833/cf26b56c-2b79-11e7-9cb9-7c3844c4508b.png"><img src="https://cloud.githubusercontent.com/assets/6216077/25477833/cf26b56c-2b79-11e7-9cb9-7c3844c4508b.png" width="50%;"></a></div>
<br>


At this point, the item tree is as follows.

```
 World(World item)
    |-AISTSimulator(AIST Simulator)
    |-Tank(model/tank/tank.wrl)
    |-Labo1(model/Labo1/Labo1.wrl)
```


#### RT Components

Add RT Components. From File > New, select and add **PyRTC**.

<br>

<div align="center"><a href="choreonoid-openrtm-py32.png"><img src="choreonoid-openrtm-py32.png" width="50%;"></a></div>
<br>



Add three items under the Tank item, and name them **TankIO**, **Controller**, and **Joystick**.

At this point, the item tree is as follows.

```
 World(World item)
    |-AISTSimulator(AIST Simulator)
    |-Tank(model/tank/tank.wrl)
      |-TankIO(PyRTC)
      |-Controller(PyRTC)
      |-Joystick(PyRTC)
    |-Labo1(model/Labo1/Labo1.wrl)
```

#### Setting the Python Files

Set the item named **RTC module** from the properties of **TankIO**, **Controller**, and **Joystick**.


<br>

<div align="center"><a href="https://cloud.githubusercontent.com/assets/6216077/25478203/2c301ca2-2b7b-11e7-8ca8-25a7a17a73c1.png"><img src="https://cloud.githubusercontent.com/assets/6216077/25478203/2c301ca2-2b7b-11e7-8ca8-25a7a17a73c1.png" width="50%;"></a></div>
<br>



Set the following files for each item.

<table class="table-alt">
  <tr>
    <th>Item Name</th>
    <th>File Name</th>
  </tr>
  <tr>
    <td>TankIO</td>
    <td>TankIoRTC_Py.py</td>
  </tr>
  <tr>
    <td>Controller</td>
    <td>TankJoystickControllerRTC_Py.py</td>
  </tr>
  <tr>
    <td>Joystick</td>
    <td>JoystickPySDL2.py</td>
  </tr>
</table>


When a Python file is set, the RTC starts.
* In this plugin, there is no distinction such as ControllerRTC, BodyIoRTC, and RTC like in the C++ version of the OpenRTM plugin included with Choreonoid. If processing such as controlling the robot on the simulator and obtaining sensor values is written in the RTC source code, it can operate in the same way as BodyIoRTC.


#### Building the RT System

Add an RT System. From File > New, select and add **RT System**.

<br>

<div align="center"><a href="cnoid-rtm-py6.png"><img src="cnoid-rtm-py6.png" width="50%;"></a></div>
<br>

From View > Show View, display the **RTC Diagram**.


If **'RTC List** is not displayed, display it in the same way.


<br>

<div align="center"><a href="cnoid-rtm-py7.png"><img src="cnoid-rtm-py7.png" width="50%;"></a></div>
<br>


After displaying the RTC Diagram, you can display RTCs on the RTC Diagram by dragging and dropping them from the RTC List in the lower-left.


<br>

<div align="center"><a href="cnoid-rtm-py8.png"><img src="cnoid-rtm-py8.png" width="50%;"></a></div>
<br>



Connect them on the RTC Diagram as follows.

<br>

<div align="center"><a href="https://cloud.githubusercontent.com/assets/6216077/25478523/5d02cf18-2b7c-11e7-8221-3e60171d65fd.png"><img src="https://cloud.githubusercontent.com/assets/6216077/25478523/5d02cf18-2b7c-11e7-8221-3e60171d65fd.png" width="50%;"></a></div>
<br>


#### Running the Simulation

Before starting the simulation, set the time resolution to 1000 fps. When you start the simulation with this setting, you will be able to operate the crawler and arm on the simulator using the joystick of the gamepad, and turn the light on and off using buttons.

### RTC Specifications

The basics are the same as the samples of the OpenRTM plugin included with Choreonoid, but some data types have been changed and configuration parameters have been added.

#### TankJoystickControllerRTC_Py

This is an RTC for controlling the Tank robot.

<br>

<div align="center"><a href="https://cloud.githubusercontent.com/assets/6216077/25479368/8e0862be-2b7f-11e7-9a44-b553218fe3c9.png"><img src="https://cloud.githubusercontent.com/assets/6216077/25479368/8e0862be-2b7f-11e7-9a44-b553218fe3c9.png" width="50%;"></a></div>
<br>



<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th><strong>TankJoystickControllerRTC_Py</strong></th>
  </tr>
  <tr>
    <td colspan="2"><strong>InPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>angles</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>PanTiltAngles</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Joint angles of the turret section</td>
  </tr>
  <tr>
    <td colspan="2"><strong>InPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>axes_1</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVector2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Status of the right analog stick. When tilted, it outputs a value in the range from 0.0 to 1.0. Depending on the direction tilted, right is positive, left is negative, down is positive, and up is negative.</td>
  </tr>
  <tr>
    <td colspan="2"><strong>InPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>axes_2</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVector2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Status of the left analog stick</td>
  </tr>
  <tr>
    <td colspan="2"><strong>InPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>buttons</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedBooleanSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Button on/off</td>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>velocities</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVelocity2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Target velocity of the vehicle body</td>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>torques</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedDoubleSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Joint torque of the turret section</td>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>lightSwitch</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedBooleanSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Light on/off</td>
  </tr>
  <tr>
    <td colspan="2"><strong>Configuration</strong></td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>timeStep</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0.001</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Simulation step time</td>
  </tr>
  <tr>
    <td colspan="2">CENTER: <strong>Configuration</strong></td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>KP</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>200.0</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Proportional gain</td>
  </tr>
  <tr>
    <td colspan="2"><strong>Configuration</strong></td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>KD</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>double</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>50.0</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Derivative gain</td>
  </tr>
</table>

#### JoystickPySDL2

This is an RTC that outputs the status of the gamepad's analog sticks, buttons, and so on.

<br>

<div align="center"><a href="https://cloud.githubusercontent.com/assets/6216077/25479372/8fa43300-2b7f-11e7-9fed-0deb4988cfdd.png"><img src="https://cloud.githubusercontent.com/assets/6216077/25479372/8fa43300-2b7f-11e7-9fed-0deb4988cfdd.png" width="50%;"></a></div>
<br>



<table class="table-alt">
  <tr>
    <th>Component Name</th>
    <th><strong>TankJoystickControllerRTC_Py</strong></th>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>axes_1</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVector2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Status of the right analog stick. When tilted, it outputs a value in the range from 0.0 to 1.0. Depending on the direction tilted, right is positive, left is negative, down is positive, and up is negative.</td>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>axes_2</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVector2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Status of the left analog stick</td>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>buttons</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedBooleanSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Button on/off</td>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>hats</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedBooleanSeq</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>D-pad status</td>
  </tr>
  <tr>
    <td colspan="2"><strong>OutPort</strong></td>
  </tr>
  <tr>
    <td>Port Name</td>
    <td>balls</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>TimedVector2D</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Movement amount of the joy ball</td>
  </tr>
  <tr>
    <td colspan="2"><strong>Configuration</strong></td>
  </tr>
  <tr>
    <td>Parameter Name</td>
    <td>index</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>int</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>Gamepad ID</td>
  </tr>
</table>

