---
layout: page
title: "opencvcamera/cameraviewer and simple opencv samples"
---

<!-- Title: OpenCVCamera/CameraViewerとシンプルOpenCVサンプル -->
#contents

Please note that this sample is not included with the Python or Java editions of OpenRTM-aist. On Linux, build and install it according to [Building OpenCV Sample Code on Linux]({{ site.baseurl }}/en/doc/installation/sample_components/opencv_sample_build).

### Overview

By starting OpenCVCamera and CameraViewer, images captured from a USB camera can be displayed on a monitor. OpenCV image-processing sample RTC components can be connected between them to apply various effects.

### Startup Screens

<div align="center"><a href="new_00.png"><img src="new_00.png" width="80%;"></a></div>
<div align="center"><strong>OpenCVCamera Component and CameraViewer Component Execution Example</strong></div>

<div align="center"><a href="new_01.png"><img src="new_01.png" width="80%;"></a></div>
<div align="center"><strong>OpenCVCamera Execution Example (RTSystemEditor)</strong></div>

<div align="center"><a href="new_02.png"><img src="new_02.png" width="80%;"></a></div>
<div align="center"><strong>CameraViewer Execution Example (Monitor)</strong></div>

### Usage

OpenCVCamera is a sample component that acquires image data from a USB camera and displays it on a monitor through the CameraViewer component.

OpenCV RT sample components can also be inserted between them to apply image-processing effects.

- Procedure

  - Start RTSystemEditor and open a new SystemEditor. For details on using RTSystemEditor, refer to [RTSystemEditor]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_2_0).

  - Start both OpenCVCamera (openCVCamera.bat) and CameraViewer (CameraViewer.bat).

    - To use the sample OpenCV image-processing RT components, launch them after installation from:
      Start > OpenRTM-aist 1.2.1 x86_64 > C++_OpenCV-Examples
      (On a 32-bit environment:
      Start > OpenRTM-aist 1.2.1 x86 > C++_OpenCV-Examples)

  - These components will appear in the Name Service View of RTSystemEditor. Drag both of them onto the SystemEditor.

  - Connect the corresponding ports of the two components. (Refer to the RTSystemEditor execution example above.)

  - Right-click either component and select [Activate Systems].

### Using OpenCV Flip

  - Start the Flip component from:
    Start > OpenRTM-aist 1.2.1 x86_64 > C++_OpenCV-Examples
    (On a 32-bit environment:
    Start > OpenRTM-aist 1.2.1 x86 > C++_OpenCV-Examples)

  - Drag it onto the SystemEditor, connect it between OpenCVCamera and CameraViewer, and activate it. (Refer to the Flip execution example below.)

  - The Flip component can also modify its output by changing the value of the Configuration parameter "flip_mode." (Refer to the flip_mode example below.)

    - For detailed usage and explanations of Flip, see [here]({{ site.baseurl }}/en/doc/casestudy/opencv_comp_development/opencv_win81_vs2015).

<div align="center"><a href="new_05.png"><img src="new_05.png" width="60%;"></a></div>
<div align="center"><strong>Flip Execution Example (RTSystemEditor)</strong></div>

<div align="center"><a href="new_03_04.png"><img src="new_03_04.png" width="80%;"></a></div>
<div align="center"><strong>Changing flip_mode (RTSystemEditor and Monitor)</strong></div>

### Other OpenCV-Based Samples

<table class="table-alt">
  <tr>
    <th>Startup Command</th>
    <th>Function</th>
    <th>Configuration Parameters</th>
  </tr>
  <tr>
    <td>Affine.bat</td>
    <td>Performs affine transformation on the input image.</td>
    <td>Affine transformation matrix</td>
  </tr>
  <tr>
    <td>BackgroundSubtractionSimple.bat</td>
    <td>Outputs changes relative to the image captured when a key input is received.</td>
    <td>Parameters specifying the image change detection method</td>
  </tr>
  <tr>
    <td>Binarization.bat</td>
    <td>Converts the input image into a black-and-white binary image.</td>
    <td>Binarization threshold</td>
  </tr>
  <tr>
    <td>DialationErosion.bat</td>
    <td>Performs dilation/erosion processing.</td>
    <td>Binarization threshold</td>
  </tr>
  <tr>
    <td>Edge.bat</td>
    <td>Outputs first-derivative images in the X and Y directions and a Laplacian (second-derivative) image.</td>
    <td>Aperture size</td>
  </tr>
  <tr>
    <td>Findcontour.bat</td>
    <td>Extracts contours and displays them in the image.</td>
    <td>Pre-processing binarization threshold, hierarchy level, contour line size for display, contour approximation method</td>
  </tr>
  <tr>
    <td>Histgram.bat</td>
    <td>Displays histogram changes while adjusting image brightness and contrast.</td>
    <td>Brightness and contrast</td>
  </tr>
</table>


<table class="table-alt">
  <tr>
    <th>Startup Command</th>
    <th>Function</th>
    <th>Configuration Parameters</th>
  </tr>
  <tr>
    <td>Hough.bat</td>
    <td>Detects straight lines using the Hough Transform.</td>
    <td>Parameters for the Hough Transform and drawing parameters for detected lines.</td>
  </tr>
  <tr>
    <td>Perspective.bat</td>
    <td>Performs a perspective transformation on the image (as if viewed from below at an angle).</td>
    <td>None</td>
  </tr>
  <tr>
    <td>RockPaperScissors.bat</td>
    <td>Recognizes rock, paper, and scissors gestures from an image.</td>
    <td>Thresholds for gesture classification based on solidity and parameters for compensating missing regions through dilation/erosion processing.</td>
  </tr>
  <tr>
    <td>Rotate.bat</td>
    <td>Performs image rotation and scaling.</td>
    <td>Counterclockwise rotation angle and scaling factor.</td>
  </tr>
  <tr>
    <td>Scale.bat</td>
    <td>Performs image scaling.</td>
    <td>Scaling factors in the X and Y directions.</td>
  </tr>
  <tr>
    <td>Sepia.bat</td>
    <td>Applies a sepia-tone effect to the image.</td>
    <td>Sepia-tone color adjustment.</td>
  </tr>
  <tr>
    <td>Translate.bat</td>
    <td>Performs two-dimensional image translation.</td>
    <td>Translation direction.</td>
  </tr>
</table>

