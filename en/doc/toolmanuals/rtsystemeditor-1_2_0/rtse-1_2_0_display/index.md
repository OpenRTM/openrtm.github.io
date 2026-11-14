---
layout: page
title: system editor (rtc display / drawing editing)
---
<!-- Title: システムエディタ（RTC の表示 / 描画編集 編） -->
#contents

This section explains operations for displaying RTCs and editing RTC drawings.

&aname(RTCcolor);
### RTC Display
RTCs placed in the System Editor are displayed as rectangles, and ports are displayed around those rectangles. Each state is also represented by color.
<br>

<div align="center"><a href="fig43RTCDisplayExample.png"><img src="fig43RTCDisplayExample.png" width="60%;"></a></div>
<div align="center"><strong>Example of RTC Display</strong></div>
<br>

The list of icons and state colors is as follows.
<br>

<div align="center"><strong>Component and Port Icons</strong></div>

<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Name</th>
    <th>Shape</th>
    <th colspan="2">State</th>
    <th>Default Color (*)</th>
  </tr>
  <tr>
    <td rowspan="5">1</td>
    <td rowspan="5">RTC</td>
    <td rowspan="5"><div align="center"><a href="IconShape.png"><img src="IconShape.png" width="50;"></a></div></td>
    <td>CREATED</td>
    <td><div align="center"><a href="IconWhite.png"><img src="IconWhite.png" width="100;"></a></div></td>
    <td>White</td>
  </tr>
  <tr>
    <td>INACTIVE</td>
    <td><div align="center"><a href="IconBlue.png"><img src="IconBlue.png" width="100;"></a></div></td>
    <td>Blue</td>
  </tr>
  <tr>
    <td>ACTIVE</td>
    <td><div align="center"><a href="IconLightGreen.png"><img src="IconLightGreen.png" width="100;"></a></div></td>
    <td>Light Green</td>
  </tr>
  <tr>
    <td>ERROR</td>
    <td><div align="center"><a href="IconRed.png"><img src="IconRed.png" width="100;"></a></div></td><td>Red</td>
  </tr>
  <tr>
    <td>UNKNOWN</td>
    <td><div align="center"><a href="IconBlack.png"><img src="IconBlack.png" width="100;"></a></div></td>
    <td>lack</td>
  </tr>
  <tr>
    <td rowspan="2">2</td>
    <td rowspan="2">Execution Context <br>(first one only)</td>
    <td rowspan="2">(outer border line of the RTC rectangle)</td>
    <td>RUNNING</td>
    <td><div align="center"><a href="IconGray.png"><img src="IconGray.png" width="100;"></a></div></td>
    <td>Gray</td>
  </tr>
  <tr>
    <td>STOPPED</td>
    <td><div align="center"><a href="IconBlack.png"><img src="IconBlack.png" width="100;"></a></div></td><td>Black</td>
  </tr>
  <tr>
    <td rowspan="2">3</td>
    <td rowspan="2">InPort</td>
    <td rowspan="2"><div align="center"><a href="IconInPort.png"><img src="IconInPort.png" width="50;"></a></div></td>
    <td>Not connected</td>
    <td><div align="center"><a href="IconBlue.png"><img src="IconBlue.png" width="100;"></a></div></td>
    <td>Blue</td>
  </tr>
  <tr>
    <td>Connected (one or more)</td>
    <td><div align="center"><a href="IconLightGreen.png"><img src="IconLightGreen.png" width="100;"></a></div></td>
    <td>Light Green</td>
  </tr>
  <tr>
    <td rowspan="2">4</td>
    <td rowspan="2">OutPort</td>
    <td rowspan="2"><div align="center"><a href="IconOutPort.png"><img src="IconOutPort.png" width="50;"></a></div></td>
    <td>Not connected</td>
    <td><div align="center"><a href="IconBlue.png"><img src="IconBlue.png" width="100;"></a></div></td>
    <td>Blue</td>
  </tr>
  <tr>
    <td>Connected (one or more)</td>
    <td><div align="center"><a href="IconLightGreen.png"><img src="IconLightGreen.png" width="100;"></a></div></td>
    <td>Light Green</td>
  </tr>
  <tr>
    <td rowspan="2">5</td>
    <td rowspan="2">ServicePort</td>
    <td rowspan="2"><div align="center"><a href="IconServicePort.png"><img src="IconServicePort.png" width="50;"></a></div></td>
    <td>Not connected</td>
    <td><div align="center"><a href="IconLightBlue.png"><img src="IconLightBlue.png" width="100;"></a></div></td>
    <td>light Blue</td>
  </tr>

  <tr>
    <td>Connected (one or more)</td>
    <td><div align="center"><a href="IconCyan.png"><img src="IconCyan.png" width="100;"></a></div></td>
    <td>Cyan</td>
  </tr>
</table>

<hr>


**'* The colors of each state can be changed from [Display Color]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_setting#color) on the settings screen.**'

You can also attach icon images according to the RTC type and category.
<br>

<div align="center"><a href="fig44RTCDisplayIconExample.png"><img src="fig44RTCDisplayIconExample.png" width="50%;"></a></div>
<div align="center"><strong>Example of RTC Icon Image Display</strong></div>
<br>

**'* Icon images can be changed from [Icon]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_setting#icon) on the settings screen.**'


### RTC Synchronization
The state of RTCs placed in the System Editor is monitored, and the display is updated in real time.<br>
The monitoring methods include the state notification observer method (OpenRTM-aist 1.1 or later) and periodic checking by polling. Monitoring parameters can be changed in the connection settings screen.<br>
When placing an RTC in the System Editor, the middleware version is checked, and if observers are supported, an observer is registered with the RTC. If observers are not supported, the state is queried periodically.
<br>

<div align="center"><a href="fig45StatusObserver.png"><img src="fig45StatusObserver.png" width="100%;"></a></div>
<div align="center"><strong>State Notification Observer</strong></div>
<br>

When an RTC is deleted from the System Editor, the observer is also unregistered.<br>
The contents notified by the state notification observer are as follows.
<br>

<div align="center"><strong>Notification Contents of the State Notification Observer</strong></div>
<table class="table-alt">
  <tr>
    <td>Notification</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>COMPONENT_PROFILE</td>
    <td>Notifies when there is a change in the component profile of the RTC</td>
  </tr>
  <tr>
    <td>RTC_STATUS</td>
    <td>RTC state<br>Notifies the new state and the ID of the target EC</td>
  </tr>
  <tr>
    <td>EC_STATUS</td>
    <td>Execution context state<br>Notifies execution rate changes, EC start/stop, and RTC attach/detach</td>
  </tr>
  <tr>
    <td>PORT_PROFILE</td>
    <td>Port state<br>Notifies port addition/deletion and connection/disconnection of connections</td>
  </tr>
  <tr>
    <td>CONFIGURATION</td>
    <td>Configuration state<br>Notifies configuration addition/change/deletion and switching of the active configuration</td>
  </tr>
</table>

<br>

In addition, a heartbeat is notified at regular intervals to confirm that the RTC is alive.<br>
If the heartbeat is not notified a certain number of times, the RTC is regarded as having terminated abnormally and is removed from the System Editor.
<br>


### RTC Drawing Editing
This section explains RTC drawing editing. (The term "drawing editing" is intentionally used instead of "editing" because the work described here edits the drawing and has no effect on the system.)

- Changing the size and moving an RTC (no effect on the system)~
To move an RTC, select the RTC and drag it. To change the size of an RTC, drag the handles that are displayed when the RTC is selected.
<br>

<div align="center"><a href="fig46RTCMoveResize.png"><img src="fig46RTCMoveResize.png" width="50%;"></a></div>
<div align="center"><strong>Moving an RTC (left) and changing the size of an RTC (right)</strong></div>
<br>

The position and size of the selected RTC are also displayed in the status bar.
<br>

<div align="center"><a href="fig47StatusBar.png"><img src="fig47StatusBar.png" width="50%;"></a></div>
<div align="center"><strong>Status Bar</strong></div>
<br>

- Rotating an RTC (no effect on the system)~
Select the target component and click the right mouse button while holding down the Ctrl key to rotate it to a horizontal orientation. Click the right mouse button while holding down the Shift key to rotate it to a vertical orientation. By repeating the same operations, you can change it to the opposite horizontal orientation or the opposite vertical orientation, allowing operation in the up, down, left, and right directions.
<br>

<div align="center"><a href="fig48RTCRotate.png"><img src="fig48RTCRotate.png" width="50%;"></a></div>
<div align="center"><strong>Rotated RTC</strong></div>
<br>


- Deleting an RTC (no effect on the system)~
To delete an RTC, select the RTC and click the [Delete] button, or select [Delete] from the context menu.
<br>

<div align="center"><a href="fig49DeleteComponent.png"><img src="fig49DeleteComponent.png" width="50%;"></a></div>
<div align="center"><strong>Deleting an RTC</strong></div>
<br>


- Moving a connection line between ports (no effect on the system)~
To move a connection line, select the connection line and move the displayed handler. Vertical lines can be moved left and right, and horizontal lines can be moved up and down.
<br>

<div align="center"><a href="fig50MoveConnection.png"><img src="fig50MoveConnection.png" width="70%;"></a></div>
<div align="center"><strong>Moving connection lines: vertical line (left) and horizontal line (right)</strong></div>
<br>

