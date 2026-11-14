---
layout: page
title: views (manager control view)
---
<!-- Title: ビュー（マネージャコントロールビュー編） -->
<!-- #contents -->

This section explains the Manager Control View.
<br>

<div align="center"><a href="fig12ManagerControlView.png"><img src="fig12ManagerControlView.png" width="70%;"></a></div>
<div align="center"><strong>Location of the Manager Control View</strong></div>
<br>

When a manager is selected in the Name Service View, the Manager Control View becomes active, and the selected manager can be controlled.
<br>

<div align="center"><a href="fig13ManagerControlView.png"><img src="fig13ManagerControlView.png" width="100%;"></a></div>
<div align="center"><strong>Manager Control View</strong></div>
<br>

<div align="center"><strong>Screen Layout of the Manager Control View</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>①</td>
    <td>Button for displaying the list of loadable modules.</td>
  </tr>
  <tr>
    <td>②</td>
    <td>Button for displaying the list of loaded modules.</td>
  </tr>
  <tr>
    <td>③</td>
    <td>Button for displaying the component list.</td>
  </tr>
  <tr>
    <td>④</td>
    <td>Component creation button.<br>Opens the component creation dialog and creates a new component. The created component is displayed in the component list display in ③.</td>
  </tr>
  <tr>
    <td>⑤</td>
    <td>Manager duplication button. Starts a new manager. * Currently unavailable because the specification has not yet been determined.</td>
  </tr>
  <tr>
    <td>⑥</td>
    <td>Manager termination button. Terminates the selected manager. * Currently unavailable because the specification has not yet been determined.</td>
  </tr>
  <tr>
    <td>⑦</td>
    <td>Table that displays lists of modules and components.</td>
  </tr>
  <tr>
    <td>⑧</td>
    <td>Specifies the URL when loading a module by specifying a URL.</td>
  </tr>
  <tr>
    <td>⑨</td>
    <td>Module load and unload buttons.<br>Loads or unloads the module selected in the table in ⑦, or the module specified by URL.</td>
  </tr>
</table>

To load a module into the manager, click the [Loadable Modules] button. When you select a displayed loadable module, the [Load] button becomes enabled, and clicking it loads the module.<br>
You can also add a module by specifying a URL by entering the module URL in the "URL:" text box and clicking the [Load] button.
<br>

<div align="center"><a href="fig14LoadModule.png"><img src="fig14LoadModule.png" width="100%;"></a></div>
<div align="center"><strong>Loading a Module</strong></div>
<br>

To unload a module, click the [Loaded Modules] button. When you select a displayed loaded module, the [Unload] button becomes enabled, and clicking it unloads the module.
<br>

<div align="center"><a href="fig15UnLoadModule.png"><img src="fig15UnLoadModule.png" width="100%;"></a></div>
<div align="center"><strong>Unloading a Module</strong></div>
<br>

To create a new component, click the [Create] button to open the component creation dialog, select the type of component to create, and click [OK]. The component is then created.<br>
The created component is registered with the name service by the manager and appears in the component list displayed by the [Active Components] button.
<br>

<div align="center"><a href="fig16ComponentDialog.png"><img src="fig16ComponentDialog.png" width="60%;"></a></div>
<div align="center"><strong>Component Creation Dialog</strong></div>
<br>

The component type is selected from the components defined in modules already loaded into the manager.<br>
In Parameter, component creation parameters can be specified in the format "param1=value1&param2=value2". The following common parameters can be set for all components.
<br>

<div align="center"><strong>Common Parameters for Component Creation</strong></div>
<table class="table-alt">
  <tr>
    <th>Parameter Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>instance_name</td>
    <td>Instance name of the component.<br>If not specified, a serial number is appended to the component type (type_name).</td>
  </tr>
  <tr>
    <td>type_name</td>
    <td>Component type</td>
  </tr>
  <tr>
    <td>description</td>
    <td>Component description</td>
  </tr>
  <tr>
    <td>version</td>
    <td>Component version</td>
  </tr>
  <tr>
    <td>vendor</td>
    <td>Component provider</td>
  </tr>
  <tr>
    <td>category</td>
    <td>Component category</td>
  </tr>
</table>

<br>
You can also specify ConfigurationSet values using component creation parameters.<br>
ConfigurationSet parameters are specified in the format "conf.NNNN.PPPP=VVVV", where NNNN is the ConfigurationSet name, PPPP is the parameter name, and VVVV is the setting value.<br>
For example, to create a ConsoleIn component, create a ConfigurationSet named mode1, and specify the parameters input_mode and input_cycle, the settings are as follows.
<br>

<div align="center"><a href="fig17ConfigurationSet.png"><img src="fig17ConfigurationSet.png" width="100%;"></a></div>
<div align="center"><strong>Specifying ConfigurationSet Parameters When Creating a Component</strong></div>
<br>

In addition, arbitrary parameters can be specified depending on the component.
<br>
