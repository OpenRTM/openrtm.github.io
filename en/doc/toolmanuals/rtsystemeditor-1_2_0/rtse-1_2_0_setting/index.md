---
layout: page
title: settings screen
---
<!-- Title: 設定画面 -->
#contents

<!-- **設定画面 -->
## RT System Editor
This section explains the settings screen of RT System Editor.
The RT System Editor settings screen can be displayed from the menu by selecting [window] > [preferences] > [RT System Editor].

&aname(cycle);
### Connection
In the connection settings, you configure the heartbeat settings for the state notification observer and the connection cycle settings.<br>
In middleware that supports the state notification observer (OpenRTM-aist 1.1 or later), RTC liveness is checked by sending heartbeats to the observer. The heartbeat setting items are as follows.

<div align="center"><strong>Heartbeat Setting Items</strong></div>
<table class="table-alt">
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Enable heartbeat</td>
    <td>Specifies whether to enable timeout detection by heartbeat.</td>
  </tr>
  <tr>
    <td>Heartbeat receive interval</td>
    <td>Specifies the heartbeat receive interval.<br>The unit is seconds, and the default is 1.0 second.</td>
  </tr>
  <tr>
    <td>Heartbeat receive count</td>
    <td>Specifies the number of heartbeat receptions for timeout detection.<br>Receive interval x receive count = timeout time [seconds]<br>The default is 3 times.</td>
  </tr>
</table>

The connection cycle is the cycle at which the System Editor collects system information and reflects it in the display in conventional middleware (OpenRTM-aist 1.0 or earlier).<br>
The unit is milliseconds. If 0 is specified, synchronization is not performed.
<br>

<div align="center"><a href="fig87ConnectionCycleSetScreen.png"><img src="fig87ConnectionCycleSetScreen.png" width="60%;"></a></div>
<div align="center"><strong>Connection Cycle Settings Screen</strong></div>
<br>


&aname(color);
### Display Color
On the display color settings screen, you can set the colors of the RTC and ExecutionContext states displayed in the System Editor.
For the meaning of each state, see [RTC Display in the System Editor]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_display#RTCcolor).
<br>

<div align="center"><a href="fig88DisplayColorSettingScreen.png"><img src="fig88DisplayColorSettingScreen.png" width="60%;"></a></div>
<div align="center"><strong>Display Color Settings Screen</strong></div>
<br>


&aname(icon);
### Icon
On the icon settings screen, you can set the icon image assigned to RTCs displayed in the System Editor and the display target pattern.
For the display target, set a pattern for the RTC type or category.
For an example of icon image display, see [RTC Display in the System Editor]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_display#RTCcolor).
<br>

<div align="center"><a href="fig89IconSettingScreen.png"><img src="fig89IconSettingScreen.png" width="60%;"></a></div>
<div align="center"><strong>Icon Image Settings Screen</strong></div>
<br>

Use the [Add], [Edit], and [Delete] buttons to add, edit, or delete icon image entries.
Clicking the [Add] or [Edit] button opens the icon image settings dialog, where you set the display target pattern and icon image file.
<br>

<div align="center"><a href="fig90IconSettingDialog.png"><img src="fig90IconSettingDialog.png" width="60%;"></a></div>
<div align="center"><strong>Icon Image Settings Screen</strong></div>
<br>

After setting the display pattern, click the [Apply] or [OK] button to apply the settings.<br>
Clicking the [Import] or [Export] button allows you to load the list of icon image settings from an XML file or save it to an XML file.
<br>


&aname(offline);
### Offline Editor
You can set the parameters that can be selected when connecting ports in the Offline Editor.<br>
The configurable items are [Interface Type], [Data Flow Type], and [Subscription Type]. When connecting ports, you can select values from the parameters set here.
For the meaning of each item, see data port connections.<br>
<br>

<div align="center"><a href="fig91OfflineEditor.png"><img src="fig91OfflineEditor.png" width="60%;"></a></div>
<div align="center"><strong>Offline Settings Screen</strong></div>
<br>


&aname(online);
### Online Editor
In the Online Editor, you can set whether to perform confirmation before executing RTC actions.
The default value is unchecked (confirmation is not performed).

<div align="center"><a href="fig92OnineEditor.png"><img src="fig92OnineEditor.png" width="60%;"></a></div>
<div align="center"><strong>Online Settings Screen</strong></div>
<br>


## RT Name Service View

&aname(ns-conn);
### Connection Cycle
The connection cycle is the cycle at which RT Name Service View collects system information and reflects it in the display.&br
There are two connection cycles: one for the Name Service View and one for the System Editor. The unit is milliseconds. If 0 is specified, synchronization is not performed.

<div align="center"><a href="figNS20ConnectCycle.png"><img src="figNS20ConnectCycle.png" width="60%;"></a></div>
<div align="center"><strong>Connection Cycle Settings Screen</strong></div>
<br>


&aname(ns-sync);
### Synchronization
The timeout wait time is the amount of time to wait when a connection to the system cannot be established while collecting system information (unit: milliseconds).

<div align="center"><a href="figNS21SyncCycle.png"><img src="figNS21SyncCycle.png" width="60%;"></a></div>
<div align="center"><strong>Connection Cycle Settings Screen</strong></div>
<br>

The relationship between the connection cycle and the synchronization timeout wait time is shown below.<br>
(Example: connection cycle is 1000 ms, synchronization timeout wait time is 100 ms)<br>

<div align="center"><a href="figNS22SyncCycleAndTimeOut.png"><img src="figNS22SyncCycleAndTimeOut.png" width="60%;"></a></div>
<div align="center"><strong>Relationship Between Connection Cycle and Synchronization Timeout Wait Time</strong></div>
<br>

