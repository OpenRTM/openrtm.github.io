---
layout: page
title: operation check (windows)
---

<!-- Title: 動作確認 (Windows編) -->

#contents

## Running Sample Components

After installation has completed successfully, you can verify operation using the included sample components.
Batch files are provided, so you can start them simply by double-clicking.

The batch files are easy to access by opening the Start Menu folder from [OpenRTM-aist 2.1.* x86_64] in the Start Menu.<br>

Batch files are located under the folders "C++_Examples", "C++_OpenCV-Examples", "Python_Examples", and "Java_Examples".

For details, refer to the explanation on the Getting Started in 10 Minutes page. <br>

- [Getting Started with OpenRTM-aist in 10 Minutes! - Running Sample Components]({{ site.baseurl }}/en/doc/installation/lets_start#toc5)
<br>

<div align="center"><a href="start-menu-folder.png"><img src="start-menu-folder.png" width="70%;"></a></div><br>
<div align="center"><strong>Start Menu Folder</strong></div>
<br>

The sample components are installed in the following locations.

```
 C:\Program Files\OpenRTM-aist\2.1.x\Components\C++\Examples
 C:\Program Files\OpenRTM-aist\2.1.x\Components\Python
 C:\Program Files\OpenRTM-aist\2.1.x\Components\Java
 C:\Program Files\OpenRTM-aist\2.1.x\Components\C++\OpenCV
```

## Sample Component List

The following table provides brief descriptions of the included sample components and links to pages explaining how to use them.

### Included with C++, Python, and Java Versions

<table class="table-alt">
  <tr>
    <td>Batch File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Guide Page</td>
  </tr>
  <tr>
    <td>ConsoleIn.bat <br>ConsoleOut.bat</td>
    <td><strong>ConsoleIn.bat</strong>: Starts the <span style="color:default;">ConsoleIn component</span>, which outputs numeric values entered from the console through an OutPort.<br><strong>ConsoleOut.bat</strong>: Starts the <span style="color:default;">ConsoleOut component</span>, which displays numeric values received through an InPort on the console.</td>
    <td><a href="/ja/doc/installation/sample_components/simpleio">SimpleIO</a></td>
  </tr>
  <tr>
    <td>SeqIn.bat <br> SeqOut.bat</td>
    <td><strong>SeqIn.bat</strong>: Starts the <span style="color:default;">SeqIn component</span>, which outputs random numeric values (Short, Long, Float, Double, and their sequence types).<br><strong>SeqOut.bat</strong>: Starts the <span style="color:default;">SeqOut component</span>, which displays numeric values (Short, Long, Float, Double, and their sequence types) received through an InPort.</td>
    <td><a href="/ja/doc/installation/sample_components/seqio">SeqIO</a></td>
  </tr>
  <tr>
    <td>MyServiceProvider.bat <br>MyServiceConsumer.bat</td>
    <td><strong>MyServiceProvider.bat</strong>: Starts the <span style="color:default;">MyServiceProvider component</span>, which provides a service of type MyService.<br><strong>MyServiceConsumer.bat</strong>: Starts the <span style="color:default;">MyServiceConsumer component</span>, which provides a service of type MyService.</td>
    <td><a href="/ja/doc/installation/sample_components/simpleservice">SimpleService</a></td>
  </tr>
  <tr>
    <td>ConfigSample.bat</td>
    <td>Starts the <span style="color:default;">ConfigSample component</span>, a sample demonstrating the use of the Configuration feature. This sample helps you understand Configuration behavior by modifying Configuration settings from RtcLink.</td>
    <td><a href="/ja/doc/installation/sample_components/configsample">ConfigSample</a></td>
  </tr>
  <tr>
    <td>Composite.bat</td>
    <td>Starts the <span style="color:default;">PeriodicECSharedComponent component</span>, a sample for creating composite components. It combines three subcomponents: Sensor, Controller, and Motor. Try connecting it with components such as ConsoleIn.</td>
    <td><a href="/ja/doc/installation/sample_components/composite">Composite</a></td>
  </tr>
</table>

### Included Only with the Python Version

<table class="table-alt">
  <tr>
    <td>Batch File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Guide Page</td>
  </tr>
  <tr>
    <td>TkJoystickComp.bat</td>
    <td>A sample GUI component using Tcl/Tk. A simple joystick component.</td>
    <td><a href="/ja/doc/installation/sample_components/tkjoystick_mobilerobotsimulator#toc0">TkJoyStick</a></td>
  </tr>
  <tr>
    <td>TkMobileRobotSimulator.bat</td>
    <td>A simple mobile robot simulator. Receives robot velocity through an InPort and outputs the resulting position through an OutPort.</td>
    <td><a href="/ja/doc/installation/sample_components/tkjoystick_mobilerobotsimulator#toc4">TkMobileRobotSimulator</a></td>
  </tr>
  <tr>
    <td>TkMotorComp.bat</td>
    <td>A sample GUI component using Tcl/Tk. Displays rotation at a speed corresponding to values received through an InPort.</td>
    <td><a href="/ja/doc/installation/sample_components/tkmotorcomp_slidercomp#toc0">TkMotorComp</a></td>
  </tr>
  <tr>
    <td>SliderComp.bat</td>
    <td>A sample GUI component using Tcl/Tk. Outputs values specified with a slider through an OutPort.</td>
    <td><a href="/ja/doc/installation/sample_components/tkmotorcomp_slidercomp#toc3">SliderComp</a></td>
  </tr>
  <tr>
    <td>TkMotorPosComp.bat</td>
    <td>A sample GUI component using Tcl/Tk. Displays motion corresponding to values received through an InPort as rotation angles.</td>
    <td><a href="/ja/doc/installation/sample_components/tkmotorposcomp_slidercomp">TkMotorPosComp</a></td>
  </tr>
  <tr>
    <td>TkLRFViewer.bat</td>
    <td>A sample GUI component using Tcl/Tk. Displays data output from laser range sensors and similar devices.</td>
    <td><a href="/ja/doc/installation/sample_components/tklrfviewer">tkLRFViewer</a></td>
  </tr>
  <tr>
    <td>AutoControl.bat</td>
    <td>A component for mobile robots that outputs velocity. It receives positioning sensor data through an InPort, calculates robot velocity, and outputs it through an OutPort.</td>
    <td><a href="/ja/doc/installation/sample_components/autocontrol">Autocontrol</a></td>
  </tr>
</table>

### Included with Python and Java Versions

<table class="table-alt">
  <tr>
    <td>Batch File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Guide Page</td>
  </tr>
  <tr>
    <td>ExtConsoleIn.bat <br> ExtConsoleOut.bat <br> ExtConnector.bat</td>
    <td><strong>ExtConsoleIn.bat</strong>: Starts a component that outputs numeric values entered through the console via an OutPort, controlled by external triggers.<br><strong>ExtConsoleOut.bat</strong>: Starts a component that outputs numeric values received through an InPort to the console, controlled by external triggers.<br><strong>ExtConnector.bat</strong>: Starts a program that sends external triggers to ExtTrigger/ConsoleInComp.class or .py and ExtTrigger/ConsoleOutComp.class or .py.</td>
    <td><a href="/ja/doc/installation/sample_components/exttrigger">ExtTrigger</a></td>
  </tr>
</table>

### Included Only with the Java Version

<table class="table-alt">
  <tr>
    <td>Batch File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Guide Page</td>
  </tr>
  <tr>
    <td>GUIIn.bat</td>
    <td>Starts a GUI sample that outputs slider positions through an OutPort. It can also be connected to ConsoleOutComp.class.</td>
    <td><a href="/ja/doc/installation/sample_components/guiin">GUIIn</a></td>
  </tr>
</table>

### OpenCV C++ Version

<table class="table-alt">
  <tr>
    <td>Batch File Name</td>
    <td>Brief Description of the Sample Component</td>
    <td>Usage Guide Page</td>
  </tr>
  <tr>
    <td>Affine.bat</td>
    <td>Performs affine transformation on the input image.</td>
  </tr>
  <tr>
    <td>BackgroundSubtractionSimple.bat</td>
    <td>Outputs changes from the image at the moment a key input is received.</td>
  </tr>
  <tr>
    <td>Binarization.bat</td>
    <td>Converts the input image into a binary black-and-white image.</td>
  </tr>
  <tr>
    <td>CameraViewer.bat</td>
    <td>Displays images received through an InPort.</td>
    <td><a href="/ja/doc/installation/sample_components/opencvcamera">CameraViewer</a></td>
  </tr>
  <tr>
    <td>Chromakey.bat</td>
    <td>Removes a specified color from an image and extracts objects.</td>
    <td><a href="/ja/doc/installation/sample_components/chromakey">Chromakey</a></td>
  </tr>
  <tr>
    <td>DialationErosion.bat</td>
    <td>Performs dilation and erosion processing.</td>
  </tr>
  <tr>
    <td>Edge.bat</td>
    <td>Outputs first-derivative images in the X and Y directions and a Laplacian image (second-derivative image).</td>
  </tr>
  <tr>
    <td>Findcontour.bat</td>
    <td>Extracts contours and displays them in the image.</td>
  </tr>
  <tr>
    <td>Flip</td>
    <td>Flips the image.</td>
    <td><a href="/ja/doc/installation/sample_components/opencvcamera">Flip Usage Example</a></td>
  </tr>
  <tr>
    <td>Histgram.bat</td>
    <td>Displays histogram changes while modifying brightness and contrast of a grayscale image.</td>
  </tr>
  <tr>
    <td>Hough.bat</td>
    <td>Line extraction using the Hough transform.</td>
  </tr>
  <tr>
    <td>ImageCalibration.bat</td>
    <td>Performs camera calibration.</td>
    <td><a href="/ja/doc/installation/sample_components/tkcalibgui">Automatically Started from TkCalibGUI</a></td>
  </tr>
  <tr>
    <td>ImageSubtraction.bat</td>
    <td>Extracts the background image from the input image, detects foreground regions, and outputs a mask image and background image.</td>
    <td><a href="/ja/doc/installation/sample_components/imagesubtraction">ImageSubtraction</a></td>
  </tr>
  <tr>
    <td>ObjectTracking.bat</td>
    <td>Tracks an object selected on the screen and indicates its position with a red ellipse.</td>
    <td><a href="/ja/doc/installation/sample_components/objecttracking">ObjectTracking</a></td>
  </tr>
  <tr>
    <td>OpenCVCamera.bat</td>
    <td>Outputs captured images from a USB camera through an OutPort.</td>
    <td><a href="/ja/doc/installation/sample_components/opencvcamera">OpenCVCamera</a></td>
  </tr>
  <tr>
    <td>Perspective.bat</td>
    <td>Performs perspective transformation on images (as if viewed from below at an angle).</td>
  </tr>
  <tr>
    <td>RockPaperScissors.bat</td>
    <td>Determines rock-paper-scissors gestures from images.</td>
  </tr>
  <tr>
    <td>Rotate.bat</td>
    <td>Performs image rotation and scaling.</td>
  </tr>
  <tr>
    <td>Scale.bat</td>
    <td>Performs image scaling.</td>
  </tr>
  <tr>
    <td>Sepia.bat</td>
    <td>Applies a sepia effect to images.</td>
  </tr>
  <tr>
    <td>SubtractCaptureImage.bat</td>
    <td>Determines unchanged regions in the input image as background and outputs a mask image that extracts the foreground (moving objects).</td>
    <td><a href="/ja/doc/installation/sample_components/substractcaptureimage">SubtractCaptureImage</a></td>
  </tr>
  <tr>
    <td>Template.bat</td>
    <td>Template matching.</td>
  </tr>
  <tr>
    <td>TkCalibGUI.bat</td>
    <td>A GUI for the ImageCalibration component used for camera calibration.</td>
    <td><a href="/ja/doc/installation/sample_components/tkcalibgui">TkCalibGUI</a></td>
  </tr>
  <tr>
    <td>Translate.bat</td>
    <td>Performs two-dimensional image translation.</td>
  </tr>
</table>

