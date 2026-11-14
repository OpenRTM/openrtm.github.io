---
layout: page
title: "tkmotorcomp/slidercomp"
---

<!-- Title: TkMotorComp/SliderComp -->

#contents

## TkMotorComp

This sample is included with the Python edition of OpenRTM-aist.

Please note that it is not included with the C++ or Java editions.

### Overview

This is a sample RT Component with a GUI interface. The sample component can be started by running:

```text
TkMotorComp.bat
```

### Startup Screen

<div align="center"><a href="TkMotorComp.png"><img src="TkMotorComp.png" width="70%;"></a></div>
<div align="center"><strong>TkMotorComp Execution Example</strong></div>

---

## SliderComp

This sample is included with the Python edition of OpenRTM-aist.

Please note that it is not included with the C++ or Java editions.

### Overview

This is a sample RT Component with a GUI interface. The sample component can be started by running:

```text
SliderComp.bat
```

(The screen shown below is from a Windows environment.)

### Startup Screen

<div align="center"><a href="SliderComp.png"><img src="SliderComp.png" width="70%;"></a></div>
<div align="center"><strong>SliderComp Execution Example</strong></div>

---

## System Configuration

<div align="center"><a href="RTSE_Slider_Motor.png"><img src="RTSE_Slider_Motor.png" width="70%;"></a></div>
<div align="center"><strong>SliderComp and TkMotorComp in RTSystemEditor</strong></div>

### Usage

SliderComp and TkMotorComp together provide a GUI-based simulation environment in which slider controls are used to control motor rotation.

- Procedure

  - Start RTSystemEditor and open a new SystemEditor.

    For details on using RTSystemEditor, refer to:

    [RTSystemEditor]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_2_0)

  - Start both components:

    ```text
    SliderComp.bat
    TkMotorComp.bat
    ```

  - Both components will appear in the Name Service View of RTSystemEditor. Drag them onto the SystemEditor.

  - Connect the corresponding ports of the two components. (Refer to the RTSystemEditor example shown above.)

  - Right-click either component and select:

    ```text
    [Activate Systems]
    ```

  - In the TkMotorComp GUI, a set of rotating disks representing motor-driven actuators will be displayed.

  - Verify that the rotation of these disks can be controlled using the vertical slider knobs in the SliderComp GUI.

  - The six slider knobs correspond to six simulated motor rotations.

