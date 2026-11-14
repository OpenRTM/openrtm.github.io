---
layout: page
title: system editor (composite components)

---

<!-- Title: システムエディタ（複合コンポーネント編） -->
#contents

This section explains how to operate composite components.

### Creating a Composite Component
You can combine multiple components into a composite component.<br>
Select the components you want to make into a composite component, right-click them, and select "Create Composite Component". The composite component creation dialog will be displayed.
<br>

<div align="center"><a href="fig66CreateCompositeComponent.png"><img src="fig66CreateCompositeComponent.png" width="50%;"></a></div>
<div align="center"><strong>Creating a Composite Component</strong></div>
<br>

<div align="center"><a href="SystemEditor_1302.jpg"><img src="SystemEditor_1302.jpg" width="60%;"></a></div>
<div align="center"><strong>Composite Component Creation Dialog</strong></div>
<br>

The items in the dialog are as follows.<br>

<div align="center"><strong>Dialog Items and Requirements for Creating a Composite Component</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Dialog Description</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>①</td>
    <td>Manager</td>
    <td>Select a manager from the list of managers displayed in the Name Service View. The manager selected here creates the composite component.</td>
  </tr>
  <tr>
    <td>②</td>
    <td>Name</td>
    <td>Specifies the instance name of the composite component.</td>
  </tr>
  <tr>
    <td>③</td>
    <td>Type</td>
    <td>Specifies the type of composite component. The available types are as follows.<br>[PeriodicECShared]<br>Each RTC operates by sharing only the ExecutionContext. Since the state of each RTC is independent, multiple states may exist within the composite component.<br>[PeriodicStateShared]<br>Each RTC operates by sharing the same ExecutionContext as well as the same state.<br>[Grouping]<br>A composite component in which each RTC shares nothing, and each RTC maintains its own ExecutionContext and state.</td>
  </tr>
  <tr>
    <td>④</td>
    <td>Path</td>
    <td>Specifies the path to be set for the composite component.</td>
  </tr>
  <tr>
    <td>⑤</td>
    <td>Port</td>
    <td>Selects the ports to be displayed on the composite component from the list of ports of the child components.<br>Proxy ports are created on the composite component for the ports selected here.<br></td>
  </tr>
  <tr>
    <td>⑥</td>
    <td>-</td>
    <td>Buttons for selecting all ports and clearing all port selections</td>
  </tr>
</table>

When a composite component is created, the components that were selected as child components disappear from the System Editor, and the new composite component is drawn.<br>
Double-click the composite component diagram, or right-click it and select "Open in Editor". A new System Diagram opens and the inside of the composite component is displayed.<br>
<br>

<div align="center"><a href="fig68CompositeOpenWithSE.png"><img src="fig68CompositeOpenWithSE.png" width="60%;"></a></div>
<div align="center"><strong>Opening a Composite Component in the System Editor</strong></div>

<br>

<div align="center"><a href="fig69ViewCompositeComponent.png"><img src="fig69ViewCompositeComponent.png" width="60%;"></a></div>
<div align="center"><strong>System Editor Displaying the Inside of a Composite Component</strong></div>
<br>

* However, when saving the system configuration, drawing information for a component can be saved only once for each component, so drawing information changed in the System Diagram that displays the inside of the composite component is not saved.
<br>


### Adding a Child to a Composite Component
Open the System Editor that displays the inside of the composite component, and drag and drop an RTC from the Name Service View. This adds the RTC as a child of the composite component. All ports of the added child RTC are set to private.
<br>

<div align="center"><a href="fig70CompositeComponentAddRTC.png"><img src="fig70CompositeComponentAddRTC.png" width="70%;"></a></div>
<div align="center"><strong>Adding a Child RTC</strong></div>
<br>


### Deleting a Child from a Composite Component
Open the System Editor that displays the inside of the composite component, and delete the child component there. This deletes the child from the composite component.<br>
The deleted child component disappears from inside the composite component and is displayed in the original System Diagram (the diagram in which the composite component itself is displayed).
<br>

<div align="center"><a href="fig71DeleteChildComponent.png"><img src="fig71DeleteChildComponent.png" width="70%;"></a></div>
<div align="center"><strong>Deleting a Child Component from Inside a Composite Component</strong></div>
<br>

<div align="center"><a href="fig72ChildComponent.png"><img src="fig72ChildComponent.png" width="70%;"></a></div>
<div align="center"><strong>Displaying a Child Component on the System Editor Where the Composite Component Is Displayed</strong></div>
<br>


### Deleting a Composite Component
Right-click the composite component and select "Delete". The composite component is deleted from the diagram.<br>
If the composite component is open in another System Diagram when it is deleted, a dialog confirming that the editor should be closed is displayed.
<br>

<div align="center"><a href="fig73DeleteCompositeComponent.png"><img src="fig73DeleteCompositeComponent.png" width="70%;"></a></div>
<div align="center"><strong>Deleting a Composite Component</strong></div>
<br>

<div align="center"><a href="fig74CloseCompositeComponentDialog.png"><img src="fig74CloseCompositeComponentDialog.png" width="50%;"></a></div>
<div align="center"><strong>Dialog Confirming Closure of the Editor Displaying the Composite Component</strong></div>
<br>


### Decomposing a Composite Component
Right-click the composite component and select "Decompose Composite Component". This sends exist() to the composite component and terminates the component itself.<br>
If the composite component is open in another System Diagram when it is decomposed, a dialog confirming that the editor should be closed is displayed.<br>
When the composite component is decomposed, the child components are displayed in the original System Diagram (the diagram where the composite component was displayed).
<br>

<div align="center"><a href="fig75DecomposeCompositeComponent.png"><img src="fig75DecomposeCompositeComponent.png" width="50%;"></a></div>
<div align="center"><strong>Decomposing a Composite Component</strong></div>
<br>

<div align="center"><a href="fig76CloseCompositeComponentDialog.png"><img src="fig76CloseCompositeComponentDialog.png" width="70%;"></a></div>
<div align="center"><strong>Dialog Confirming Closure of the Editor Displaying the Composite Component</strong></div>
<br>


### Switching Ports Between Public and Private
If the ports of a component in the System Editor that displays the inside of the composite component are exposed on the composite component, they are displayed with different icons as shown below.
<br>

<div align="center"><strong>Icons for Public Ports of Child RTCs</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Name</th>
    <th>Shape</th>
  </tr>
  <tr>
    <td>1</td>
    <td>InPort</td>
    <td><div align="center"><a href="IconExportedInPort.png"><img src="IconExportedInPort.png" width="100;"></a></div></td>
  </tr>
  <tr>
    <td>2</td>
    <td>OutPort</td>
    <td><div align="center"><a href="IconExportedOutPort.png"><img src="IconExportedOutPort.png" width="100;"></a></div></td>
  </tr>
  <tr>
    <td>3</td>
    <td>ServicePort</td>
    <td><div align="center"><a href="IconExportedServicePort.png"><img src="IconExportedServicePort.png" width="100;"></a></div></td>
  </tr>
</table>

Right-click a public port and select "Unexport" to change the port to a non-public state. Also, right-click a non-public port and select "Export" to change the port to a public state.
<br>

<table class="table-alt">
  <tr>
    <th><div align="center"><a href="fig77ExportPort.png"><img src="fig77ExportPort.png" width="100%;"></a></div></th>
    <th><div align="center"><a href="fig77UnexportPort.png"><img src="fig77UnexportPort.png" width="100%;"></a></div></th>
  </tr>
</table>

<div align="center"><strong>Public/Private Port Setting</strong></div>
<br>

However, if the port is connected to a port of another component, it cannot be set to "Unexport".
<br>

<div align="center"><a href="fig78CantUnexport.png"><img src="fig78CantUnexport.png" width="70%;"></a></div>
<div align="center"><strong>When There Is a Port Connection</strong></div>
<br>
