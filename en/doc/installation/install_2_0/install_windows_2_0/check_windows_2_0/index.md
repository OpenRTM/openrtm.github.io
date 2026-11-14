---
layout: page
title: operation check (windows edition)
---

<!-- Title: 動作確認 (Windows編) -->

#contents


## Running Sample Components

If the installation has completed successfully, you can verify operation using the included sample components.
bat files are provided, so you can start them by double-clicking them.

The bat files are easy to access by opening the Start Menu folder from [OpenRTM-aist 2.0.* x86_64] in the Start menu.<br>
The bat files are located under the folders "C++_Examples", "C++_OpenCV-Examples", "Python_Examples", and "Java_Examples".
For details, refer to the explanation on the Get Started in 10 Minutes page. <br>
- [Get Started with OpenRTM-aist in 10 Minutes! - Running Sample Components]({{ site.baseurl }}/en/doc/installation/lets_start#toc5) 

<br>
<div align="center"><a href="start-menu-folder.png"><img src="start-menu-folder.png" width="50%;"></a></div><br>
<div align="center"><strong>Start Menu Folder</strong></div>
<br>


The installation locations of the sample components are as follows.

```
 C:\Program Files\OpenRTM-aist\2.0.x\Components\C++\Examples
 C:\Program Files\OpenRTM-aist\2.0.x\Components\Python
 C:\Program Files\OpenRTM-aist\2.0.x\Components\Java
 C:\Program Files\OpenRTM-aist\2.0.x\Components\C++\OpenCV
```


## List of Sample Components

Brief descriptions of the included sample components and links to pages explaining how to use them are shown below.

### Included with the C++, Python, and Java Versions

<table class="table-alt">
  <tr>
    <td>bat File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Explanation Page</td>
  </tr>
  <tr>
    <td>ConsoleIn.bat <br>ConsoleOut.bat</td>
    <td><strong>ConsoleIn.bat</strong> : Starts the <span style="color:default;">ConsoleIn component</span>; which outputs numerical values entered from the console from an OutPort.<br> <strong>ConsoleOut.bat</strong> : Starts the <span style="color:default;">ConsoleOut component</span>; which displays numerical values input to an InPort on the console.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/simpleio">SimpleIO</a></td>
  </tr>
  <tr>
    <td>SeqIn.bat <br> SeqOut.bat</td>
    <td><strong>SeqIn.bat</strong> : Starts the <span style="color:default;">SeqIn component</span>; which outputs random numerical values (Short, Long, Float, Double, and their sequence types).<br> <strong>SeqOut.bat</strong> : Starts <span style="color:default;">SeqOut</span>; which displays numerical values input to an InPort (Short, Long, Float, Double, and their sequence types).</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/seqio">SeqIO</a></td>
  </tr>
  <tr>
    <td>MyServiceProvider.bat <br>MyServiceConsumer.bat</td>
    <td><strong>MyServiceProvider.bat</strong> : Starts the <span style="color:default;">MyServiceProvider component</span>; which provides a service of the MyService type.<br> <strong>MyServiceConsumer.bat</strong> : Starts the <span style="color:default;">MyServiceConsumer component</span>; which provides a service of the MyService type.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/simpleservice">SimpleService</a></td>
  </tr>
  <tr>
    <td>ConfigSample.bat</td>
    <td>Starts the <span style="color:default;">ConfigSample component</span>; which is a sample showing how to use the Configuration feature. This sample is used to understand the behavior of Configuration by changing Configuration from RtcLink.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/configsample">ConfigSample</a></td>
  </tr>
  <tr>
    <td>Composite.bat</td>
    <td>Starts the <span style="color:default;">PeriodicECSharedComponent component</span>; which is a sample for creating composite components. It combines three sub-components: Sensor, Controller, and Motor. You may want to try using it by connecting components such as ConsoleIn.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/composite">Composite</a></td>
  </tr>
</table>

### Included Only with the Python Version

<table class="table-alt">
  <tr>
    <td>bat File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Explanation Page</td>
  </tr>
  <tr>
    <td>TkJoystickComp.bat</td>
    <td>A sample GUI component using Tcl/Tk. A simple joystick component.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/tkjoystick_mobilerobotsimulator#toc0">TkJoyStick</a></td>
  </tr>
  <tr>
    <td>TkMobileRobotSimulator.bat</td>
    <td>A simple simulator for mobile robots. It receives robot velocity through an InPort and outputs the position after movement from an OutPort.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/tkjoystick_mobilerobotsimulator#toc4">TkMobileRobotSimulator</a></td>
  </tr>
  <tr>
    <td>TkMotorComp.bat</td>
    <td>A sample GUI component using Tcl/Tk. It displays in a GUI how the motor rotates at the speed corresponding to the value received through an InPort.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/tkmotorcomp_slidercomp#toc0">TkMotorComp</a></td>
  </tr>
  <tr>
    <td>SliderComp.bat</td>
    <td>A sample GUI component using Tcl/Tk. It outputs the value specified by a slider from an OutPort.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/tkmotorcomp_slidercomp#toc3">SliderComp</a></td>
  </tr>
  <tr>
    <td>TkMotorPosComp.bat</td>
    <td>A sample GUI component using Tcl/TK. It displays in a GUI how the motor moves using the value received through an InPort as the rotation angle.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/tkmotorposcomp_slidercomp">TkMotorPosComp</a></td>
  </tr>
  <tr>
    <td>TkLRFViewer.bat</td>
    <td>A sample GUI component using Tcl/Tk. It displays data output from devices such as laser range sensors.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/tklrfviewer">tkLRFViewer</a></td>
  </tr>
  <tr>
    <td>AutoControl.bat</td>
    <td>A component for mobile robots that outputs velocity. It receives positioning sensor data through an InPort, calculates the robot velocity, and outputs it from an OutPort.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/autocontrol">Autocontrol</a></td>
  </tr>
</table>

### Included with the Python and Java Versions

<table class="table-alt">
  <tr>
    <td>bat File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Explanation Page</td>
  </tr>
  <tr>
    <td>ExtConsoleIn.bat <br> ExtConsoleOut.bat <br> ExtConnector.bat</td>
    <td><strong>ExtConsoleIn.bat</strong> : Starts a component controlled by an external trigger that outputs numerical values entered from the console from an Outport.<br> <strong>ExtConsoleOut.bat</strong> : Starts a component controlled by an external trigger that outputs numerical values input to an Inport to the console.<br> <strong>ExtConnector.bat</strong> : Starts a program that sends an external trigger to ExtTrigger/ConsoleInComp.class or .py and ExtTrigger/ConsoleOutComp.class or .py.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/exttrigger">ExtTrigger</a></td>
  </tr>
</table>

### Included Only with the Java Version

<table class="table-alt">
  <tr>
    <td>bat File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Explanation Page</td>
  </tr>
  <tr>
    <td>GUIIn.bat</td>
    <td>Starts a sample GUI that outputs the slider position from an Outport. It can also be connected to ConsoleOutComp.class.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/guiin">GUIIn</a></td>
  </tr>
</table>

### OpenCV C++ Version

<table class="table-alt">
  <tr>
    <td>bat File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Explanation Page</td>
  </tr>
  <tr>
    <td>Affine.bat</td>
    <td>Performs affine transformation on the input image.</td>
  </tr>
  <tr>
    <td>BackgroundSubtractionSimple.bat</td>
    <td>Outputs the difference from the image at the time of key input in the input image.</td>
  </tr>
  <tr>
    <td>Binarization.bat</td>
    <td>Converts the input image into a binarized black-and-white image.</td>
  </tr>
  <tr>
    <td>CameraViewer.bat</td>
    <td>Displays the image received through an InPort on the screen.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/opencvcamera">CameraViewer</a></td>
  </tr>
  <tr>
    <td>Chromakey.bat</td>
    <td>Removes a specific color from the image and extracts the object.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/chromakey">Chromakey</a></td>
  </tr>
  <tr>
    <td>DialationErosion.bat</td>
    <td>Performs dilation/erosion processing.</td>
  </tr>
  <tr>
    <td>Edge.bat</td>
    <td>Outputs a first derivative image in the X direction, a first derivative image in the Y direction, and a Laplacian image (second derivative image).</td>
  </tr>
  <tr>
    <td>Findcontour.bat</td>
    <td>Extracts contours and displays the contours in the image.</td>
  </tr>
  <tr>
    <td>Flip</td>
    <td>Flips the image.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/opencvcamera">Flip Usage Example</a></td>
  </tr>
  <tr>
    <td>Histgram.bat</td>
    <td>Displays changes in the histogram while modifying the brightness/contrast of the grayscale image.</td>
  </tr>
  <tr>
    <td>Hough.bat</td>
    <td>Line extraction using the Hough transform</td>
  </tr>
  <tr>
    <td>ImageCalibration.bat</td>
    <td>Performs camera calibration.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/tkcalibgui">Automatically Started from TkCalibGUI</a></td>
  </tr>
  <tr>
    <td>ImageSubtraction.bat</td>
    <td>Extracts a background image from the input image, determines the foreground image region, and outputs a mask image that extracts it and the background image.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/imagesubtraction">ImageSubtraction</a></td>
  </tr>
  <tr>
    <td>ObjectTracking.bat</td>
    <td>Tracks an object selected on the screen and indicates its position by surrounding it with a red ellipse.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/objecttracking">ObjectTracking</a></td>
  </tr>
  <tr>
    <td>OpenCVCamera.bat</td>
    <td>Outputs captured images from a USB camera through an OutPort.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/opencvcamera">OpenCVCamera</a></td>
  </tr>
  <tr>
    <td>Perspective.bat</td>
    <td>Performs perspective transformation on the image (transforms it as if viewed from diagonally below).</td>
  </tr>
  <tr>
    <td>RockPaperScissors.bat</td>
    <td>Determines rock, paper, or scissors from an image.</td>
  </tr>
  <tr>
    <td>Rotate.bat</td>
    <td>Rotates and scales the image.</td>
  </tr>
  <tr>
    <td>Scale.bat</td>
    <td>Scales the image up or down.</td>
  </tr>
  <tr>
    <td>Sepia.bat</td>
    <td>Applies a sepia tone to the image.</td>
  </tr>
  <tr>
    <td>SubtractCaptureImage.bat</td>
    <td>Determines unchanged parts of the input image as the background and outputs a mask image that extracts the foreground (moving object).</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/substractcaptureimage">SubtractCaptureImage</a></td>
  </tr>
  <tr>
    <td>Template.bat</td>
    <td>Template matching</td>
  </tr>
  <tr>
    <td>TkCalibGUI.bat</td>
    <td>A GUI for the ImageCalibration component that performs camera calibration.</td>
    <td><a href="{{ site.baseurl }}/en/doc/installation/sample_components/tkcalibgui">TkCalibGUI</a></td>
  </tr>
  <tr>
    <td>Translate.bat</td>
    <td>Performs two-dimensional translation of the image.</td>
  </tr>
</table>
