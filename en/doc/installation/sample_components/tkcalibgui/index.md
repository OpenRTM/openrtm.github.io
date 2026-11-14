---
layout: page
title: "tkcalibgui"
---

<!-- Title: TkCalibGUI -->

#contents

## TkCalibGUI

Please note that this sample is not included with the Python or Java editions of OpenRTM-aist. On Linux, build and install it according to [Building OpenCV Sample Code on Linux]({{ site.baseurl }}/en/doc/installation/sample_components/opencv_sample_build).

### Overview

This is a sample RT Component with a GUI interface. The sample component can be started by running TkCalibGUI.bat.

It provides a GUI for the ImageCalibration component used for camera calibration.

When this component is launched and a camera component is selected from the available list, it automatically starts the ImageCalibrationComp component and automatically connects the ports between the components.

Using the GUI buttons, you can save camera images required for calibration and calculate camera parameters.

<br>

### Component Execution Requirements

If OpenRTM-aist C++ was installed using the Windows installer, simply running TkCalibGUI.bat is sufficient.

If OpenRTM-aist was built from source, the required runtime environment must be prepared. This component checks whether the required environment is available.

If the requirements are not met, a message dialog similar to the one below is displayed. Follow the instructions to install the missing components.

<div align="center"><a href="calib9.jpg"><img src="calib9.jpg" width="80%;"></a></div>
<div align="center"><strong>Message Displayed When Execution Requirements Are Not Met</strong></div>

#### For Windows Environments

<table class="table-alt">
  <tr>
    <td>Message</td>
    <td>Required Action</td>
  </tr>
  <tr>
    <td>OpenRTM-aist Python is not installed.</td>
    <td>You can download the Windows installer from the <a href="{{ site.baseurl }}/download/openrtm-aist-python/openrtm-aist-python_1_2_1_release">OpenRTM-aist Python Edition</a> page.<br>
    Select the installer version (32-bit or 64-bit) that matches your OpenRTM-aist C++ installation.</td>
  </tr>
  <tr>
    <td>Ttk is not installed.</td>
    <td>Install <a href="https://pypi.python.org/pypi/pyttk/0.3">pyttk</a>. It is included with Python 2.7, but must be installed separately for Python 2.6.</td>
  </tr>
  <tr>
    <td>PIL is not installed.</td>
    <td>Install <a href="http://www.pythonware.com/products/pil/">PIL</a>.</td>
  </tr>
  <tr>
    <td>NumPy is not installed.</td>
    <td>Install <a href="http://sourceforge.net/projects/numpy/files/NumPy/">NumPy</a>.</td>
  </tr>
  <tr>
    <td>rtctree is not installed.</td>
    <td>
      rtctree 3.0.1 or later is required.<br>
      An installer is planned, but until then, download the ZIP archive from the <a href="http://github.com/gbiggs/rtctree">GitHub page</a> using the "Download Zip" button, extract it, and install it by running setup.py:
      <br><code>python setup.py install</code><br>
      Add the path to <code>site-packages\rtctree\rtmidl</code> to the system environment variable PYTHONPATH.<br>
      Example:
      <code>C:\Python27\Lib\site-packages\rtctree\rtmidl</code>
    </td>
  </tr>
</table>

#### For Linux (Ubuntu) Environments

<table class="table-alt">
  <tr>
    <td>Message</td>
    <td>Required Action</td>
  </tr>
  <tr>
    <td>OpenRTM-aist Python is not installed.</td>
    <td>You can download the all-in-one installation script from the <a href="http://openrtm.org/openrtm/en/content/openrtm-aist-python-110-release">OpenRTM-aist Python Edition</a> page.</td>
  </tr>
  <tr>
    <td>Ttk is not installed.</td>
    <td><code>$ sudo apt-get install python-tk</code></td>
  </tr>
  <tr>
    <td>PIL is not installed.</td>
    <td><code>$ sudo apt-get install python-pil.imagetk</code></td>
  </tr>
  <tr>
    <td>NumPy is not installed.</td>
    <td><code>$ sudo apt-get install python-numpy</code></td>
  </tr>
  <tr>
    <td>rtctree is not installed.</td>
    <td>
      rtctree 3.0.1 or later is required.<br>
      Download it from GitHub and install it by running setup.py, as described for Windows.<br>
      Add PYTHONPATH to <code>~/.bashrc</code> or a similar shell configuration file:
      <br><code>export PYTHONPATH="/usr/local/lib/python2.7/dist-packages/rtctree/rtmidl"</code>
    </td>
  </tr>
</table>

### Startup Screen

<div align="center"><a href="calib1.jpg"><img src="calib1.jpg" width="60%;"></a></div>

First, select the camera component to use from the list. This list displays the camera components available in the current environment.

In a Windows 10 environment using VC2019, OpenCVCameraComp and MFCameraComp are available. Both provide similar functionality, but OpenCVCameraComp is newer and generally less dependent on the execution environment.

The executable launched by tkCalibGUI.bat also starts the ImageCalibration component. Although the ImageCalibration component can be launched independently using ImageCalibration.bat, no sample component is provided for standalone operation. Therefore, if you want to use ImageCalibration without TkCalibGUI, you must create your own component to connect to it.

<div align="center"><a href="calib2.jpg"><img src="calib2.jpg" width="60%;"></a></div>

Click the [All Activate] button to display the camera image.

At this point, the component connections are as shown below. All components except TkCalibGUI are started automatically, and their ports are connected automatically.

<div align="center"><a href="calib10.jpg"><img src="calib10.jpg" width="60%;"></a></div>

### Usage

Prepare a checkerboard pattern (calibration pattern). In this example, the following pattern is used:

<div align="center"><a href="checkerboard.pdf"><img src="checkerboard.pdf" width="100;"></a></div>

The number of checkerboard corners must be specified in the Configuration settings of ImageCalibration.

The values:

- checker_h
- checker_w

represent the number of shared vertices between black and white squares (that is, the number of squares minus one in each direction).

The number of images to capture (`image_num`) can also be changed in the Configuration settings.

To capture calibration images, photograph the checkerboard from various angles while covering as much of the image area as possible. Save the specified number of images.

You can verify each captured image using the [Confirm] button.

If you click the [Delete] button, the image is removed and should be captured again.

<div align="center"><a href="calib3.jpg"><img src="calib3.jpg" width="50%;"></a><a href="calib4.jpg"><img src="calib4.jpg" width="50%;"></a></div>
<div align="center"><a href="calib5.jpg"><img src="calib5.jpg" width="50%;"></a><a href="calib6.jpg"><img src="calib6.jpg" width="50%;"></a></div>

Once the required number of images has been saved, the [Show Results] button becomes available.

Clicking it displays the calculated camera parameter values.

<div align="center"><a href="calib8.jpg"><img src="calib8.jpg" width="60%;"></a></div>

The camera parameters are written to a file named `camera.yml` in the same directory as the component executable.

```yaml
%YAML:1.0
calibration_time: "Thu May 22 16:38:06 2014\n"
image_width: 640
image_height: 480
board_width: 13
board_height: 9
cameraMatrix: !!opencv-matrix
   rows: 3
   cols: 3
   dt: d
   data: [ 5.8272934483011682e+002, 0., 3.3703801084645710e+002, 0.,
       5.8023846162074653e+002, 2.2824562602176763e+002, 0., 0., 1. ]
distCoeffs: !!opencv-matrix
   rows: 1
   cols: 5
   dt: d
   data: [ -1.4659954975042236e-001, 5.7825601645508595e-001,
       -3.3745642103035984e-003, 1.2569676956708463e-003,
       -9.8011775330916773e-001 ]
```

### Image Output (Reference)

For reference, when the [Save] button is clicked, image files are written to the directory specified by the system environment variable TEMP or TMP.

- File names:
  `capture0.jpg` – `capture4.jpg`
  (when five images are saved; grayscale images)

<div align="center"><a href="capture0.jpg"><img src="capture0.jpg" width="70%;"></a></div>

Using the generated camera parameters, distortion-corrected versions of the images are also written to the same directory.

- File names:
  `undistorted0.jpg` – `undistorted4.jpg`
  (the numbering corresponds to the matching `capture*.jpg` files)

<div align="center"><a href="undistorted0.jpg"><img src="undistorted0.jpg" width="70%;"></a></div>

