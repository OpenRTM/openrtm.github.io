---
layout: page
title: system editor (basic operations)
---

<!-- Title: システムエディタ（基本操作編） -->
#contents

This section explains the overview and basic operations of the System Editor.


## Overview
In the System Editor, the state of RTCs is displayed in real time. You can also build systems and verify operation by connecting ports and changing the state of RTCs.
#clear

<table class="table-alt">
  <tr>
    <th><div align="center"><a href="SystemEditor_011.jpg"><img src="SystemEditor_011.jpg" width="45%;"></a></div></th>
    <th><div align="center"><a href="SystemEditor_012.jpg"><img src="SystemEditor_012.jpg" width="80%;"></a></div></th>
  </tr>
  <tr>
    <th style="text-align: center;">System Editor Location</th>
    <th style="text-align: center;">System Editor</th>
  </tr>
</table>
<br>


## Basic Operations
This section explains how to connect ports between RTCs and how to execute RTCs.

### Opening the System Editor
To open a new System Editor, click the [Open New System Editor] button on the toolbar, or select [File] > [Open New System Editor] from the menu bar.
<br>

<div align="center"><a href="SystemEditor_013.jpg"><img src="SystemEditor_013.jpg" width="70%;"></a></div>
<div align="center"><strong>Open New System Editor from the Toolbar</strong></div>
<br>

<div align="center"><a href="SystemEditor_014.jpg"><img src="SystemEditor_014.jpg" width="70%;"></a></div>
<div align="center"><strong>Open New System Editor from the File Menu</strong></div>
<br>


### Placing an RTC in the System Editor
To place an RTC in the System Editor, drag and drop the RTC from the Name Service View.
<br>

<div align="center"><a href="fig40EditorComponentDnD.png"><img src="fig40EditorComponentDnD.png" width="70%;"></a></div>
<div align="center"><strong>Placing an RTC in the System Editor</strong></div>
<br>

If you click RTCs in the name service while holding down the [Ctrl] key and select multiple RTCs, you can place them all together in the System Editor.
<br>

<div align="center"><a href="fig41EditorComponentMultiDnD.png"><img src="fig41EditorComponentMultiDnD.png" width="70%;"></a></div>
<div align="center"><strong>Placing Multiple RTCs Together in the System Editor</strong></div>
<br>

Note that RTCs that have already been placed in the System Editor, or parent RTCs and child RTCs of a composite RTC, cannot be added redundantly.
When placing multiple RTCs, duplicate RTCs are skipped, and when placing a single RTC, an error dialog is displayed.
<br>

<div align="center"><a href="fig42DeployComponentError.png"><img src="fig42DeployComponentError.png" width="70%;"></a></div>
<div align="center"><strong>Duplicate RTC Placement Error Dialog</strong></div>
<br>


### Changing the State of an RTC
This section explains how to change the state of an RTC.<br>
In the System Diagram, you can select an RTC and execute "Activate", "Deactivate", "Reset", "Finalize", "Exit", "Start", and "Stop".
You can also execute them in the same way from the Name Service View.
<br>

<table class="table-alt">
  <tr>
    <th><div align="center"><a href="fig51RTCStatusChangeNS.png"><img src="fig51RTCStatusChangeNS.png" width="85%;"></a></div></th>
    <th><div align="center"><a href="fig51RTCStatusChangeEditor.png"><img src="fig51RTCStatusChangeEditor.png" width="85%;"></a></div></th>
  </tr>
</table>
<div align="center"><strong>Changing the RTC State from the Name Service View (left) and the System Editor (right)</strong></div>
<br>

The meanings of these actions are as follows. Please pay attention to the execution target.
<br>

<div align="center"><strong>Actions for Changing the RTC State</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Action Name</th>
    <th>Execution Target</th>
    <th>Meaning</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Activate</td>
    <td>Executed for the selected RTC and its first ExecutionContext</td>
    <td>Requests Activate</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Deactivate</td>
    <td>〃</td>
    <td>Requests Deactivate</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Reset</td>
    <td>〃</td>
    <td>Requests Reset</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Exit</td>
    <td>Executed for the selected RTC</td>
    <td>Requests Exit</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Start</td>
    <td>Executed for the first ExecutionContext of the selected RTC</td>
    <td>Requests Start</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Stop</td>
    <td>〃</td>
    <td>Requests Activate</td>
  </tr>
</table>

If confirmation of action execution is enabled in the online editor item of "[Settings Screen]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_setting)", a confirmation dialog is displayed before the action is executed.

<div align="center"><a href="fig52RTCStatusChangeConfirm.png"><img src="fig52RTCStatusChangeConfirm.png" width="70%;"></a></div>
<div align="center"><strong>Action Execution Confirmation Dialog</strong></div>
<br>

By default, advance confirmation is disabled.<br>
Shortcut keys are assigned to Activate and Deactivate. By default, they are set as follows.<br>
・Activate → Ctrl + Alt + A <br>
・Deactivate → Ctrl + Alt + D <br>
To change the key bindings, use "General" → "Keys" in the standard Eclipse settings menu.
<br>

Also, as a function for easily operating the system, you can request Activate, Deactivate, Start, Stop, and changes for all RTCs included in the System Editor from the toolbar and context menu.
<br>

<div align="center"><a href="fig53AllExec.png"><img src="fig53AllExec.png" width="85%;"></a></div>
<div align="center"><strong>All Execution (Toolbar, from left: All Activate, All Deactivate, All Start, All Stop)</strong></div>
<br>

All-type actions are also performed for ExecutionContexts other than the first one. Please note that the results differ from activating or starting each RTC on the screen one by one.


### Connecting Ports
In the System Editor, you can connect RTC ports to each other.<br>
To connect ports, drag and drop one port to another port.
<br>

<div align="center"><a href="fig54ConnectPort.png"><img src="fig54ConnectPort.png" width="70%;"></a></div>
<div align="center"><strong>Port Connection</strong></div>
<br>

After the drag and drop is completed, a dialog prompting you to enter the information required for connection is displayed.
<br>

<div align="center"><a href="SystemEditor_015.jpg"><img src="SystemEditor_015.jpg" width="70%;"></a></div>
<div align="center"><strong>Example of the ConnectorProfile Dialog</strong></div>
<br>

In this dialog, a ConnectorProfile is created. The ConnectorProfile must be created so that the conditions required by each port are satisfied. This dialog prompts you with pull-down menus so that only values satisfying the required conditions can be entered.
For a connection that cannot satisfy the required conditions, a prohibited mark is displayed during the drag-and-drop connection, and drag and drop cannot be performed.
<br>

<div align="center"><a href="fig56ConnectedProhibitionMark.png"><img src="fig56ConnectedProhibitionMark.png" width="50%;"></a></div>
<div align="center"><strong>Connection Prohibited Mark</strong></div>
<br>

Port connections are broadly divided into data port connections and service port connections. For details, please refer to "[System Editor (Connecting Ports)]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_setting)".


### Disconnecting a Port Connection
To disconnect a port connection, select the connection and click the [Delete] button, or click [Delete] displayed in the context menu.
<br>

<div align="center"><a href="fig61Disconnect.png"><img src="fig61Disconnect.png" width="70%;"></a></div>
<div align="center"><strong>Deleting a Connection</strong></div>
<br>


### Disconnecting All Port Connections
To disconnect all port connections, select a port, right-click it, and execute "All Disconnect".
<br>

<div align="center"><a href="fig62AllDisconnect.png"><img src="fig62AllDisconnect.png" width="70%;"></a></div>
<div align="center"><strong>Disconnecting All Connections</strong></div>
<br>


### Setting a Single Port Connection
You can set a ConnectorProfile for a single port connection.<br>
Right-click a port and select "Connect" from the context menu. The ConnectorProfile settings dialog opens in the same way as for a port-to-port connection.
<br>

<div align="center"><a href="fig63ConnectSinglePort.png"><img src="fig63ConnectSinglePort.png" width="70%;"></a></div>
<div align="center"><strong>Single Port Connection</strong></div>
<br>

To delete a single port connection, similarly select "Disconnect" from the right-click context menu and operate from the port disconnection dialog.
Delete the target from the list of ConnectorProfiles displayed in the dialog, and click the [OK] button to perform the disconnection process.
<br>

<div align="center"><a href="fig64DisconnectPort.png"><img src="fig64DisconnectPort.png" width="70%;"></a></div>
<div align="center"><strong>Port Disconnection</strong></div>
<br>

<div align="center"><a href="fig65DisconnectPortDialog.png"><img src="fig65DisconnectPortDialog.png" width="70%;"></a></div>
<div align="center"><strong>Port Disconnection Dialog</strong></div>
<br>

The port disconnection dialog displays a list of all ConnectorProfiles for single port connections and normal port-to-port connections, so it can also be used to check single port connections that are not drawn in the diagram.
<br>


### Collecting Logs
With the log notification observer, RTC log messages can be collected by the tool. (OpenRTM-aist 1.1 or later)<br>
Right-click an RTC on the diagram and select "Start Logging" from the context menu to start log collection.
For an RTC that has already started log collection, the menu display changes to "Stop Logging", and log collection is stopped.<br>
For an RTC that does not support observers, the menu is disabled.
<br>

<table class="table-alt">
  <tr>
    <td style="text-align: center;">Starting Log Collection</td>
    <td style="text-align: center;">Stopping Log Collection</td>
  </tr>
  <tr>
<td><div align="center"><a href="fig79LoggingStart.png"><img src="fig79LoggingStart.png" width="50%;"></a></div></td>
<td><div align="center"><a href="fig79LoggingStop.png"><img src="fig79LoggingStop.png" width="50%;"></a></div></td>
  </tr>
</table>
<div align="center"><strong>Starting/Stopping Log Collection</strong></div>

For log collection, as with the state notification observer, a reference to the log notification observer is registered with the RTC and notifications are received.
The observer is registered when log collection is started from the context menu, and the observer is unregistered when log collection is stopped.
Also, as with the state notification observer, the observer is unregistered when an RTC is removed from the diagram.<br>
In log notification, a data structure including the time and log level (log record) is sent from the RTC, and the tool accumulates the log data.
The accumulated logs can be viewed using the Log View.
<br>

<div align="center"><a href="fig80LogObserver.png"><img src="fig80LogObserver.png" width="70%;"></a></div>
<div align="center"><strong>Log Notification Observer</strong></div>
<br>

