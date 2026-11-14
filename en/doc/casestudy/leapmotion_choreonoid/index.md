---
layout: page
title: "controlling choreonoid with leap motion"
---

<!-- Title: Controlling Choreonoid with Leap Motion -->
#contents

In this case study, a Leap Motion sensor is used to control a GRobo robot running in the Choreonoid simulator.

First, you will verify operation using the provided components (demo system and sample components). Then, you will create your own component to control the robot in the simulator.

<!--break-->

## Resources and Prerequisites

Download and extract the following archive:

[robomec2015_openrtm_tutorial_part3.zip]()(No corresponding page available.) <span style="color:red;">Updated: 2015/05/20</span>

The main contents of the archive are:

- **Demo/**: Components and Choreonoid for the demo system
  - **rtc_handle.bat**: Batch file for launching the demo system
- **src/**: Source code of the provided components
  - **LeapMotion_RobotControl_Sample**: Source code of the sample component
- **LeapMotionGRoboControlSampleComp.exe**: Binary of the sample component (x64, Visual Studio 2013)
- **online_tutorial/**: This web page

<span style="color:red;">[Required]</span> Download and install the Leap Motion driver by clicking **"Windows Download"** from the following page:

https://www.leapmotion.com/setup/windows

## Verifying the Demo System

In this section, you will start the demo system and verify its operation.

Follow the steps below:

1. Start the Name Server using **"Start Naming Service"** from the Start Menu (refer to the [OpenRTM documentation]()(No corresponding page available.)).
2. Launch **RTSystemEditorRCP** or **OpenRTP 1.1.1** from the Start Menu.
3. Run **Demo/rtc_handle.bat** to start the demo launcher.
4. In RtcHandle, click the following buttons to launch the components:
   1. CNoid_G
   2. RobotDemo
   3. LeapRTC
   4. LeapMotion
5. Click **"getRtcList"**.
6. Click **"Load"** and select **"LeapDemo.data"**.
7. Click **"ConnectAll"** to connect all components automatically.
8. Click **"ActivateAll"** to activate all components and start the system.
9. **While the LeapRTCComp window is selected**, move your hands above the Leap Motion sensor. Data will appear in the LeapMotion window, and the robot in the simulator will move according to the generated commands.

## Verifying the Sample Component

In this section, the sample component is used instead of the **GRobotDemo** component to control the robot in the simulator.

Before proceeding, start the demo system using the steps described above.

### Compiling LeapMotionGRoboControlSampleComp

1. Start CMake.
2. Specify **src/LeapMotion_RobotControl_Sample** as the source directory.
3. Specify the **build** directory inside the source directory as the build directory.
4. Click **Configure**.
5. Select an appropriate Generator.
   - The example shown uses Visual Studio 2013 x64.
   - Select the Generator corresponding to your installed OpenRTM version.
6. Click **Generate** to create the project.
7. Open **LeapMotionGRoboControlSample.sln** in Visual Studio and build **ALL_BUILD**.
8. Confirm that the component binary has been generated.

### Running LeapMotionGRoboControlSampleComp

1. Execute **LeapMotionGRoboControlSampleComp.exe**.
2. In RTSystemEditor, delete the connections of the **GRobotDemo** component.
3. Connect **LeapMotionGRoboControlSampleComp** as follows and activate it:
   - Connect `LeapMotion.eSEAT0.hands_out` to `LeapMotionGRoboControlSample0.hand_positions`
   - Connect `LeapMotionGRoboControlSample0.hand_positions` to `RobotMotion0.targetAngle`
4. **While the LeapRTCComp window is selected**, move your hands above the Leap Motion sensor. The robot's hands in the simulator will follow your hand movements.

## Creating Your Own Component

This section explains how to create a robot control component.

First, generate a source-code skeleton using RTCBuilder. Then, edit the source code freely to implement your own algorithm for controlling the robot using Leap Motion data.

### Creating the RTC

1. Start RTCBuilder.
2. Create a new RTCBuilder project (choose any project name and component name).
3. Select the following activities:
   - **onActivated**
   - **onDeactivated**
   - **onExecute**
4. Create the following data ports:

| Type | Port Name | Data Type |
|--------|--------|--------|
| InPort | hand_positions | RTC::TimedFloatSeq |
| OutPort | command | RTC::TimedString |
| OutPort | target_angles | RTC::TimedShortSeq |

5. Skip the Service Port tab (none required).
6. Skip the Configuration tab (none required).
7. Set the programming language to **C++**.
8. Generate the component source skeleton.

### Editing the Source Code

After generation, edit and compile the component using CMake and Visual Studio.

#### Add the following private variables to the class definition in the header file:

```cpp
bool m_rightUp;
bool m_leftUp;
````

#### Add the following function near line 12 of the .cpp file:

```cpp
double minmax(double a, double max, double min)
{
  if (a > max)
  {
    return max;
  }
  else if (min > a)
  {
    return min;
  }
  return a;
}
```

#### Add the following lines to the constructor:

```cpp
m_rightUp = false;
m_leftUp = false;
```

#### Replace the contents of `onExecute()` with the provided source code.

(The original code block should be kept exactly as provided.)

Compile the component using the same procedure as for the sample component.

The compiled component can be used in the same way as **LeapMotionGRoboControlSample0**.

After confirming that it behaves the same as the sample component, modify the source code while referring to the following input/output data formats.

### Input Data Format

The data received through `eSEAT0.hands_out` and supplied to the component's `hand_positions` input port has the following format:

```text
[right hand x, right hand y, right hand z,
 left hand x,  left hand y,  left hand z]
```

### Command Output Port

The `command` output port controls the robot's posture by outputting one of the following commands:

* b_step
* balance
* bothdown
* bothup
* bow
* bye
* f01
* f1
* f_step
* go_ahead
* go_back
* gymnastics
* init
* kick
* l1
* left_step
* leftdown1
* leftdown2
* leftup1
* leftup2
* look_left
* look_right
* motion
* muri
* r1
* rest
* right_step
* rightdown1
* rightdown2
* rightup1
* rightup2
* turn_l
* turn_r

### Target Angle Output Port

The `target_angles` output port specifies joint positions using the format:

```text
[joint number, position, joint number, position, ...]
```

For example:

```text
[14, <position>, 15, <position>, 16, <position>,
 17, <position>, 18, <position>, 19, <position>]
```

## Using Components on Another Computer

Components running on another computer can also be used.

This section explains how to connect components across a network.

<span style="color:red;">Before proceeding, be sure to disable Windows Firewall.</span>

### Verifying Name Server Connectivity

First, verify that the computers can communicate and that the remote Name Server is visible.

1. Determine the IP address of the remote computer.
2. In RTSystemEditor, click **Add Name Server** and enter the remote computer's IP address.
3. If successful, the remote Name Server will appear in the Name Server list.

### Verifying Component Connectivity

After confirming Name Server visibility:

1. On the local computer, start **ConsoleInComp.exe**.
2. On the remote computer, start **ConsoleOutComp.exe**.
3. In RTSystemEditor, place:

   * ConsoleIn0 (local Name Server)
   * ConsoleOut0 (remote Name Server)
4. Connect their ports.
5. If successful, numbers entered in ConsoleInComp.exe will be displayed by ConsoleOutComp.exe.

If remote components cannot be controlled:

1. Open `rtc.conf`.
2. Add the following line:

```text
corba.endpoint: <IP address>
```

3. Use the local computer's IP address on the local machine and the remote computer's IP address on the remote machine.
4. Restart all components.

### Using a Remote Leap Motion Component

Once connectivity has been verified, the remote **LeapRTC0** component can be used from the local RTSystemEditor.

Place the remote LeapRTC0 component in the System Diagram and connect its ports. It will behave as if the Leap Motion sensor were directly connected to the local computer.

If RTSystemEditor still cannot control the component, follow the `rtc.conf` procedure described above.

For this tutorial package, the relevant `rtc.conf` files are located in:

* `robomec2015_openrtm_tutorial_part3/Demo/LeapMotion`
* `robomec2015_openrtm_tutorial_part3/Demo/eSEAT`

