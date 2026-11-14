---
layout: page
title: views (execution context view) 
---

<!-- Title: ビュー（実行コンテキストビュー編） -->
<!-- #contents -->

This section explains the Execution Context View.
<br>

<div align="center"><a href="fig23ECView.jpg"><img src="fig23ECView.jpg" width="85%;"></a></div>
<div align="center"><strong>Location of the Execution Context View</strong></div>
<br>

In the Execution Context View, you can display a list of execution contexts (ECs) to which the selected RTC belongs, start/stop ECs, execute RTC actions, and attach/detach RTCs to/from ECs. You can also set the execution cycle of ECs.
<br>

<div align="center"><a href="fig24ECView.png"><img src="fig24ECView.png" width="100%;"></a></div>
<div align="center"><strong>Execution Context View</strong></div>
<br>

<div align="center"><strong>Screen Layout of the Execution Context View</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>①</td>
    <td>Instance name of the RTC.</td>
  </tr>
  <tr>
    <td>②</td>
    <td>Displays a list of ECs to which the RTC belongs.<br> ECs owned by the RTC are displayed as "owned*", and ECs in which the RTC only participates are displayed as "participate*".</td>
  </tr>
  <tr>
    <td>③</td>
    <td>Execution rate of the EC selected in ②.</td>
  </tr>
  <tr>
    <td>④<br>⑤</td>
    <td>Displays the properties of the selected EC as a list of Name and Value.<br>　id: EC ID. In online mode, context_handle is displayed as the ID.<br>　kind: EC type (PERIODIC/EVENT_DRIVEN/OTHER)<br>　state: EC state (RUNNING/STOPPING)<br>　component_state: State of the selected RTC on the EC (ACTIVE/INACTIVE/ERROR)<br>　owner: Instance name of the owner RTC of this EC<br>　participants: Number of RTCs participating in this EC<br>Other arbitrary properties set for the EC are also displayed.</td>
  </tr>
  <tr>
    <td>⑥</td>
    <td>Applies the entered execution rate to the EC.</td>
  </tr>
  <tr>
    <td>⑦</td>
    <td>Starts the selected EC. (Not available offline)</td>
  </tr>
  <tr>
    <td>⑧</td>
    <td>Stops the selected EC. (Not available offline)</td>
  </tr>
  <tr>
    <td>⑨</td>
    <td>Activates the state of the selected RTC on the selected EC. (Not available offline)</td>
  </tr>
  <tr>
    <td>⑩</td>
    <td>Deactivates the state of the selected RTC on the selected EC. (Not available offline)</td>
  </tr>
  <tr>
    <td>⑪</td>
    <td>Resets the state of the selected RTC on the selected EC. (Not available offline)</td>
  </tr>
  <tr>
    <td>⑫</td>
    <td>Detaches the selected RTC from the selected EC.<br>However, if the RTC itself is the owner of the EC, it cannot be detached.</td>
  </tr>
  <tr>
    <td>⑬</td>
    <td>Opens the RTC selection dialog on the System Editor and attaches the selected RTC to the EC.</td>
  </tr>
</table>

The value being edited for the execution rate is not applied until the [Apply] button in ⑥ is clicked. Information being modified (not yet applied) is displayed in light red. If the input value is invalid, it is displayed in red.
<br>

<div align="center"><a href="fig25EditRate.png"><img src="fig25EditRate.png" width="70%;"></a></div>
<div align="center"><strong>Editing the Execution Rate</strong></div>
<br>

<div align="center"><a href="fig26EditRateError.png"><img src="fig26EditRateError.png" width="70%;"></a></div>
<div align="center"><strong>When the Execution Rate Setting Value Is Invalid</strong></div>
<br>

In the online editor, you can operate ECs and change the state of RTCs on those ECs.<br>
Click the [Start] button to start the EC, and the state property becomes "RUNNING". Click the [Stop] button to stop the EC, and state becomes "STOPPING".<br>
To change the state of an RTC on an EC, click the [Activate] or [Deactivate] button. When activated, the component_state property becomes "ACTIVE", and when deactivated, component_state becomes "INACTIVE".<br>
If an RTC enters the "ERROR" state for some reason, click the [Reset] button to recover it.
<br>

<div align="center"><a href="fig27ActionAndStatus.png"><img src="fig27ActionAndStatus.png" width="70%;"></a></div>
<div align="center"><strong>EC Operations and RTC State Changes</strong></div>
<br>

An RTC can be attached to multiple ECs.<br>
Select the EC to which you want to add the RTC, and click the [Attach] button. The RTC selection dialog opens. The selection dialog displays a list of RTCs in the System Editor.
<br>

<div align="center"><a href="fig28SelectDialog.png"><img src="fig28SelectDialog.png" width="70%;"></a></div>
<div align="center"><strong>RTC Selection Dialog</strong></div>
<br>

When you select an RTC and click [OK], the RTC is added to the EC, and the newly added EC is added to the list of participate ECs for the added RTC.
<br>

<div align="center"><a href="fig29AttachContext.png"><img src="fig29AttachContext.png" width="100%;"></a></div>
<div align="center"><strong>Attaching an RTC to an EC</strong></div>
<br>

To detach an EC, select the participate EC and click the [Detach] button.
<br>

<div align="center"><a href="fig30DetachContext.png"><img src="fig30DetachContext.png" width="100%;"></a></div>
<div align="center"><strong>Detaching an RTC from an EC</strong></div>
<br>
