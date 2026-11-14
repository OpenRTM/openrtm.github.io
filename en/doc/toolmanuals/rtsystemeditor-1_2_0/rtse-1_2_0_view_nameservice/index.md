---
layout: page
title: views (name service view)
---
<!-- Title: ビュー（ネームサービスビュー編 -->
#contents

This section explains the Name Service View.
<br>

In OpenRTM-aist, a name service is used to manage and publish RTCs, and the Name Service View allows you to display and edit this information.
<br>


### Function Overview
The Name Service View provides functions for graphically operating RTCs in real time. The list of provided functions is as follows.
#clear

<div align="center"><strong>Function Overview List</strong></div>
<table class="table-alt">
  <tr>
    <td>No.</td>
    <td>Function Name</td>
    <td>Function Overview</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Name Server Connection/Edit Function</td>
    <td>Connects to a name server and displays the registered components in the Name Service View in a tree format.</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Component Profile Display Function</td>
    <td>Displays the profile information of the selected component in the Property View.</td>
  </tr>
</table>


### Starting the Name Service View
Select [Window] > [Show View] > [Name Service View] from the menu to display the Name Service View.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0301.jpg"><img src="RTCBuilder1.1.2_0301.jpg" width="70%;"></a></div>
<div align="center"><strong>Show View</strong></div>
<br>

<div align="center"><a href="RTCBuilder1.1.2_0302.jpg"><img src="RTCBuilder1.1.2_0302.jpg" width="60%;"></a></div>
<div align="center"><strong>Initial Startup Screen of the Name Service View</strong></div>
<br>


### Connecting to a Name Server
To connect to a name server, click the [Add Name Server] button at the top of the Name Service View, or select [Add Name Server] from the context menu.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0303.jpg"><img src="RTCBuilder1.1.2_0303.jpg" width="60%;"></a></div>
<div align="center"><strong>Connecting to a Name Server</strong></div>
<br>

In the name server connection dialog, enter the IP address and port number. (If the port number is omitted, the port number configured on the settings screen is used. The default port number is port 2809.)
<br>

<div align="center"><a href="RTCBuilder1.1.2_0304.jpg"><img src="RTCBuilder1.1.2_0304.jpg" width="60%;"></a></div>
<div align="center"><strong>Name Server Connection Dialog</strong></div>
<br>

**Note:** When Eclipse is started or restarted, it automatically connects to the last connected address. If none exists, it attempts to connect to port 2809 on localhost.


### Removing a Name Server from the Screen
To remove a connected name server from the screen, right-click the name server and select [Remove from View].
<br>

<div align="center"><a href="RTCBuilder1.1.2_0305.jpg"><img src="RTCBuilder1.1.2_0305.jpg" width="60%;"></a></div>
<div align="center"><strong>Removing a Name Server from the Screen</strong></div>
<br>

### Displaying the Contents of a Name Server
If components are registered in the connected name server, the registered contents are displayed in a tree format as shown below.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0306.jpg"><img src="RTCBuilder1.1.2_0306.jpg" width="60%;"></a></div><br>
<div align="center"><strong>Name Service View</strong></div>
<br>

The meanings of the icons are as follows.

<div align="center"><strong>List of Name Server Icons</strong></div>


<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Icon</th> 
    <th>Type (KIND)</th> 
    <th>Name</th>
  </tr>
  <tr>
    <td>1</td>
    <td><div align="center"><a href="IconHostCxt.png"><img src="IconHostCxt.png" width="13%;"></a></div></td>
    <td>host_cxt</td>
    <td>Host context</td>
  </tr>
  <tr>
    <td>2</td>
    <td><div align="center"><a href="IconMgrCxt.png"><img src="IconMgrCxt.png" width="13%;"></a></div></td>
    <td>mgr_cxt</td>
    <td>Manager context</td>
  </tr>
  <tr>
    <td>3</td>
    <td><div align="center"><a href="IconCateCxt.png"><img src="IconCateCxt.png" width="13%;"></a></div></td>
    <td>cate_cxt</td>
    <td>Category context</td>
  </tr>
  <tr>
    <td>4</td>
    <td><div align="center"><a href="IconModCxt.png"><img src="IconModCxt.png" width="13%;"></a></div></td>
    <td>mod_cxt</td>
    <td>Module context</td>
  </tr>
  <tr>
    <td>5</td>
    <td><div align="center"><a href="IconElse.png"><img src="IconElse.png" width="13%;"></a></div></td>
    <td>Other than the above</td>
    <td>Folder (contexts other than the above)</td>
  </tr>
  <tr>
    <td>6</td>
    <td><div align="center"><a href="IconRTC.png"><img src="IconRTC.png" width="13%;"></a></div></td>
    <td>None</td>
    <td>RTC</td>
  </tr>
  <tr>
    <td>7</td>
    <td><div align="center"><a href="IconMgr.png"><img src="IconMgr.png" width="13%;"></a></div></td>
    <td>None</td>
    <td>Manager</td>
  </tr>
  <tr>
    <td>8</td>
    <td><div align="center"><a href="IconObj.png"><img src="IconObj.png" width="13%;"></a></div></td>
    <td>None</td>
    <td>Object (object other than RTC)</td>
  </tr>
  <tr>
    <td>9</td>
    <td><div align="center"><a href="IconZombi.png"><img src="IconZombi.png" width="13%;"></a></div></td>
    <td>None</td>
    <td>Zombie object that is registered in the name server but whose actual object cannot be accessed</td>
  </tr>
</table>



The Name Service View constantly monitors each connected name server and synchronizes and updates the display. (The monitoring cycle can be changed in [[Connection Cycle:]] on the settings screen.)
Also, when you want to explicitly reacquire the contents of a name server, perform an update. To perform an update, click the [Refresh] button at the top of the Name Service View, or select [Refresh] from the context menu.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0307.jpg"><img src="RTCBuilder1.1.2_0307.jpg" width="60%;"></a></div>
<div align="center"><strong>Refresh</strong></div>
<br>


### Changing the Display Range of the Name Service View
The Name Service View has a function for moving the display root position to prevent the operation range from becoming complicated as the number of RTCs increases.<br>
To move the display root, select the destination, then click the [Jump Next] button at the top of the Name Service View, or select [Jump Next] from the context menu.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0308.jpg"><img src="RTCBuilder1.1.2_0308.jpg" width="60%;"></a></div>
<div align="center"><strong>Changing the Display Root</strong></div>
<br>

<div align="center"><a href="RTCBuilder1.1.2_0309.jpg"><img src="RTCBuilder1.1.2_0309.jpg" width="60%;"></a></div>
<div align="center"><strong>Example of Changing the Display Root</strong></div>
<br>

After moving, you can return one level up with [Back]. You can also return to the top-level hierarchy with [Back to Home].


### Filtering the Display Contents of the Name Service View
As another way to prevent the operation range from becoming complicated as the number of RTCs increases, the Name Service View has a filter function that limits the types of entries displayed.<br>
To set a filter, click the [Set Filter] button at the top of the Name Service View.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0310.jpg"><img src="RTCBuilder1.1.2_0310.jpg" width="60%;"></a></div>
<div align="center"><strong>Filter Instruction</strong></div>
<br>

In the "Set Filter" dialog, select the types of entries to hide from the "Select elements to exclude from the view" field.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0311.jpg"><img src="RTCBuilder1.1.2_0311.jpg" width="60%;"></a></div>
<div align="center"><strong>Name Service Filter Dialog</strong></div>
<br>

If you check the elements you want to exclude from the Name Service View display, they will no longer be displayed in the Name Service View.<br>
When "Naming Object Name" is enabled, objects that match the object name condition are hidden.<br>
For the object name condition, prefix match and partial match can be selected.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0312.jpg"><img src="RTCBuilder1.1.2_0312.jpg" width="60%;"></a></div>
<div align="center"><strong>Filtering by Object Name</strong></div>
<br>


### Deleting an Entry from the Name Service
In the Name Service View, you can delete naming object entries from the name service. To delete a naming object, click [Delete from Name Service] in the context menu.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0313.jpg"><img src="RTCBuilder1.1.2_0313.jpg" width="60%;"></a></div>
<div align="center"><strong>Deleting from the Name Service</strong></div>
<br>


### Registering an Object in the Name Service
In the Name Service View, you can register an object entry in the name service.<br>
To register an object, select [Add Object] from the context menu of the context or object under which you want to add the object.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0314.jpg"><img src="RTCBuilder1.1.2_0314.jpg" width="60%;"></a></div>
<div align="center"><strong>Adding an Object</strong></div>
<br>

<div align="center"><a href="RTCBuilder1.1.2_0315.jpg"><img src="RTCBuilder1.1.2_0315.jpg" width="60%;"></a></div>
<div align="center"><strong>Add Object Dialog</strong></div>
<br>

In the "Add Object" dialog, specify the object name (Name), type (Kind), and IOR.


### Registering a Context in the Name Service
In the Name Service View, you can register a context entry in the name service.<br>
To register a context, select [Add Context] from the context menu of the context under which you want to add the context.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0316.jpg"><img src="RTCBuilder1.1.2_0316.jpg" width="60%;"></a></div>
<div align="center"><strong>Adding a Context</strong></div>
<br>

<div align="center"><a href="RTCBuilder1.1.2_0317.jpg"><img src="RTCBuilder1.1.2_0317.jpg" width="60%;"></a></div>
<div align="center"><strong>Add Context Dialog</strong></div>
<br>

In the "Add Context" dialog, specify the context name (Name) and type (Kind).<br>
For type (Kind), select one of the following values.

<div align="center"><strong>List of Context Types (kind)</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Type (Kind)</th>
    <th>Name</th>
  </tr>
  <tr>
    <td>1</td>
    <td>host_cxt</td>
    <td>Host context</td>
  </tr>
  <tr>
    <td>2</td>
    <td>mgr_cxt</td>
    <td>Manager context</td>
  </tr>
  <tr>
    <td>3</td>
    <td>cate_cxt</td>
    <td>Category context</td>
  </tr>
  <tr>
    <td>4</td>
    <td>mod_cxt</td>
    <td>Module context</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Enter something other than the above</td>
    <td>Folder (contexts other than the above)</td>
  </tr>
</table>


### Deleting Zombie Objects
The Name Service View has a function for deleting zombie objects all at once. To delete all zombie objects, click the [Clear Zombies] button at the top of the Name Service View.
<br>

<div align="center"><a href="RTCBuilder1.1.2_0318.jpg"><img src="RTCBuilder1.1.2_0318.jpg" width="60%;"></a></div>
<div align="center"><strong>Clear Zombies</strong></div>
<br>
