---
layout: page
title: offline system editor
---
<!-- Title: オフラインシステムエディタ -->
#contents
<!-- オフラインシステムエディタ -->


### Overview
This section explains the overview of the Offline System Editor.
<br>

<div align="center"><a href="fig86OfflineSysetmEditor.png"><img src="fig86OfflineSysetmEditor.png" width="70%;"></a></div>
<div align="center"><strong>Location of the Offline System Editor</strong></div>
<br>

In the Offline System Editor, you edit an RT system by adding components from the Repository View to the diagram by drag and drop. The basic operations are the same as those of the online System Editor, but you cannot change the state of RTCs. Also, RTC states are not changed or updated in real time.
<br>


### Basic Functions

#### Opening the Offline System Editor
To open a new Offline System Editor, click the "Open New Offline System Editor" button on the toolbar, or select [File] > [Open New Offline System Editor] from the menu bar.
<br>


<div align="center"><a href="fig87OpenNewOfflineSystemEditorFromToolbar.png"><img src="fig87OpenNewOfflineSystemEditorFromToolbar.png" width="60%;"></a></div>
<div align="center"><strong>Open New Offline System Editor from the Toolbar</strong></div>
<br>

<div align="center"><a href="fig88FileOpenNewOfflineEditor.png"><img src="fig88FileOpenNewOfflineEditor.png" width="50%;"></a></div>
<div align="center"><strong>Open New Offline System Editor from the File Menu</strong></div>
<br>


#### Placing Component Specifications in the Offline System Editor
To place component specifications in the Offline System Editor, drag and drop the component specifications from the Repository View.
<br>

<div align="center"><a href="fig89OfflineEditorComponentDnD.png"><img src="fig89OfflineEditorComponentDnD.png" width="70%;"></a></div>
<div align="center"><strong>Placing Component Specifications in the Offline System Editor</strong></div>
<br>

If you click component specifications in the Repository View while holding down the Ctrl key and select multiple component specifications, you can place them all together in the Offline System Editor.
<br>

<div align="center"><a href="fig90OfflineEditorComponentMultiDnD.png"><img src="fig90OfflineEditorComponentMultiDnD.png" width="70%;"></a></div>
<div align="center"><strong>Placing Multiple Component Specifications Together in the Offline System Editor</strong></div>
<br>


#### Editing Component Specifications in the Offline System Editor
In the Offline System Editor, you can perform most of the operations available in the System Editor, except for those related to the operation of runtime components, using the same operations as in the System Editor.
<br>


### Deployment Function

This section explains the overview of the deployment function using the Offline System Editor.
<br>

By using the deployment function, you can build an actual system from an offline profile created in the Offline System Editor.

#### Setting Deployment Information
Right-click a component placed in the Offline Editor and select "Set Deploy Info." from the displayed menu. The deployment information settings screen is displayed.
<br>

<div align="center"><a href="fig91DeploySetting.png"><img src="fig91DeploySetting.png" width="60%;"></a></div>
<div align="center"><strong>Setting Deployment Information</strong></div>
<br>

<table class="table-alt">
  <tr>
    <td><div align="center"><a href="fig92DeployComp.png"><img src="fig92DeployComp.png" width="60%;"></a></div></td>
    <td><div align="center"><a href="fig92DeployManager.png"><img src="fig92DeployManager.png" width="60%;"></a></div></td>
  </tr>
  <tr>
    <td style="text-align: center;"><strong>Running RTCs</strong></td>
    <td style="text-align: center;"><strong>Running Managers</strong></td>
  </tr>
</table>

<div align="center"><strong>Deployment Information Settings Screen</strong></div>
<br>

The deployment information settings screen displays a list of currently running RTCs and Managers. Select the element to use when deploying the target RTC.
<br>

* The contents of the deployment information settings screen use the items displayed in NameServiceView. If information about running elements is not displayed, check the display contents of NameServiceView and refresh it as necessary.
<br>

* If a composite RTC is selected, only the Manager information list is displayed. Select the Manager to use during deployment.
<br>


#### Saving and Loading Deployment Information
The configured deployment information can be saved and loaded separately from the RtsProfile. Right-click the Offline Editor and select "Save Deploy Info." or "Load Deploy Info." from the displayed menu.
<br>

<div align="center"><a href="fig93DeploySave.png"><img src="fig93DeploySave.png" width="80%;"></a></div>
<div align="center"><strong>Saving and Loading Deployment Information</strong></div>
<br>

* When loading deployment information, the corresponding RTC is searched for using the component ID (vendor name, category name, component name, and version number) as the key.
<br>


#### Executing Deployment
To build (deploy) an actual system based on the configured deployment information, right-click the Offline Editor and select "Deploy System" from the displayed menu.
<br>

<div align="center"><a href="fig94Deploy.png"><img src="fig94Deploy.png" width="80%;"></a></div>
<div align="center"><strong>Deployment</strong></div>
<br>

When deployment is executed, the actual system is built (deployed) based on the configured deployment information. Then, a new online editor is opened and the deployment result is displayed.
<br>

If there is a component in the target offline system for which deployment information has not been configured, or if the configured deployment target is not running at the time of deployment, a warning screen like the following is displayed.
<br>

<div align="center"><a href="fig95DeployWarning.png"><img src="fig95DeployWarning.png" width="70%;"></a></div>
<div align="center"><strong>Warning Screen During Deployment</strong></div>
<br>

If "Cancel" is selected on the warning screen, the deployment process is aborted. If [OK] is selected, the system is built (deployed) as much as possible using the running deployment targets.

