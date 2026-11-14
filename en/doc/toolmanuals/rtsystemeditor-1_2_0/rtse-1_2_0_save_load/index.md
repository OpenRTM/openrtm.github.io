---
layout: page
title: system editor (save)
---
<!-- Title: システムエディタ（セーブ編） -->
#contents

This section explains how to save and open the System Editor.

### Saving the System Editor
The System Editor can be saved. To save it, select [File] from the menu or right-click the editor and select "Save". ("Save As..." allows you to freely select the file to save.)
<br>

<table class="table-alt">
  <tr>
<td><div align="center"><a href="SystemEditor_1401.jpg"><img src="SystemEditor_1401.jpg" width="90%;"></a></div></td>
<td><div align="center"><a href="SystemEditor_1402.jpg"><img src="SystemEditor_1402.jpg" width="90%;"></a></div></td>
  </tr>
  <tr>
    <td style="text-align: center;"><strong>System Editor Save Menu</strong></td>
    <td style="text-align: center;"><strong>Context Menu</strong></td>
  </tr>
</table>
<br>

When you select system save, the profile information dialog opens. Set the required items and click the [OK] button to save the system information to a file.<br>
<br>

<div align="center"><a href="SystemEditor_1403.jpg"><img src="SystemEditor_1403.jpg" width="70%;"></a></div>
<div align="center"><strong>Profile Information Dialog</strong></div>
<br>

<div align="center"><strong>Profile Information Items</strong></div>
<table class="table-alt">
  <tr>
    <th>Name</th>
    <th>Shape</th>
  </tr>
  <tr>
    <td>Vendor</td>
    <td>Vendor name. An element that makes up the RT system identifier.<br>Required item.</td>
  </tr>
  <tr>
    <td>System Name</td>
    <td>System name. An element that makes up the RT system identifier.<br>Required item.</td>
  </tr>
  <tr>
    <td>Version</td>
    <td>System version. An element that makes up the RT system identifier.<br>Required item.</td>
  </tr>
  <tr>
    <td>Path</td>
    <td>File name used to save the system.<br>Required item.</td>
  </tr>
  <tr>
    <td>Update Log</td>
    <td>Describes supplementary information such as version notes.</td>
  </tr>
  <tr>
    <td>Required</td>
    <td>Check the RTCs required to operate the RT system.</td>
  </tr>
</table>


### Opening a Saved System Editor
To open a saved System Editor, right-click the editor and select "Open".
<br>

<div align="center"><a href="SystemEditor_1404.jpg"><img src="SystemEditor_1404.jpg" width="60%;"></a></div>
<div align="center"><strong>Opening the System Editor</strong></div>
<br>

After opening, RT System Editor treats the remote system as the correct source and updates it with the latest information. To restore the saved contents to the system, use "Open and Restore...", described in the next section.
<br>


### Opening and Restoring a Saved System
To open and restore a saved System Editor, right-click the editor and select "Open and Restore..." or "Open and Quick Restore...".
<br>

<div align="center"><a href="SystemEditor_1405.jpg"><img src="SystemEditor_1405.jpg" width="60%;"></a></div>
<div align="center"><strong>Opening and Restoring the System Editor</strong></div>
<br>

The following contents are restored to the system.
- Connections between ports (when the connector from the time of saving does not exist)
- Configuration information~
During restoration, the name service is searched using the component path ID to obtain the remote component.<br>
When "Quick Restore" is selected, before accessing the name service, it attempts to obtain the remote component using the IOR saved in the profile. If it cannot be obtained, the name service is searched.<br>
If restoration fails, the error details are displayed.
<br>

<div align="center"><a href="fig85ErrorMessageOfRestorationFailure.png"><img src="fig85ErrorMessageOfRestorationFailure.png" width="60%;"></a></div>
<div align="center"><strong>Error Message for Restoration Failure</strong></div>
<br>

RT System Editor also attempts to restore as much as possible even when an error occurs.
<br>
<br>

