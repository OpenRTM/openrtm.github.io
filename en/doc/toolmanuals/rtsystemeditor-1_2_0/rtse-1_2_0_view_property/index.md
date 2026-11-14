---
layout: page
title: views (property view)
---
<!-- Title: ビュー（プロパティビュー編） -->
<!-- #contents -->

This section explains the Property View.
<br>

<div align="center"><a href="SystemEditor_Property_01.jpg"><img src="SystemEditor_Property_01.jpg" width="85%;"></a></div>
<div align="center"><strong>Location of the Property View</strong></div>
<br>

The Property View displays profile information of RTCs and connectors selected in the System Dialog in real time. (Even while an RTC is selected, if a change is detected, it is reflected immediately.)
<br>

<table class="table-alt">
  <tr>
    <td style="text-align: center;">For RTC</td>
    <td style="text-align: center;">For Composite RTC</td>
    <td style="text-align: center;">For Manager</td>
  </tr>
  <tr>
    <td><div align="center"><a href="fig353TypePropertyView1.png"><img src="fig353TypePropertyView1.png" width="80%;"></a></div></td>
    <td><div align="center"><a href="fig353TypePropertyView2.png"><img src="fig353TypePropertyView2.png" width="80%;"></a></div></td>
    <td><div align="center"><a href="fig353TypePropertyView3.png"><img src="fig353TypePropertyView3.png" width="80%;"></a></div></td>
  </tr>
</table>
<div align="center"><strong>Property View</strong></div>
<br>

The meanings of the displayed icons are as follows.
<br>

<div align="center"><strong>List of Property Icons</strong></div>
<table class="table-alt">
  <tr>
    <td>No.</td>
    <td>Icon</td>
    <td>Name</td>
    <td>Display Contents</td>
  </tr>
  <tr>
    <td>1</td>
    <td><div align="center"><a href="IconRTC2.png"><img src="IconRTC2.png" width="50%;"></a></div></td>
    <td>RTC</td>
    <td>InstanceName, TypeName, Description, Vender, Category, State (*displayed based on the LifeCycleState of the first ExecutionContext)</td>
  </tr>
  <tr>
    <td>2</td>
    <td><div align="center"><a href="IconExecContext.png"><img src="IconExecContext.png" width="50%;"></a></div></td>
    <td>ExecutionContext</td>
    <td>State, Kind, Rate</td>
  </tr>
  <tr>
    <td>3</td>
    <td><div align="center"><a href="IconServicePort.png"><img src="IconServicePort.png" width="50
%;"></a></div></td>
    <td>ServicePort</td>
    <td>Name, list of property information</td>
  </tr>
  <tr>
    <td>4</td>
    <td><div align="center"><a href="IconOutPort.png"><img src="IconOutPort.png" width="50%;"></a></div></td>
    <td>Outport</td>
    <td>Name, list of property information</td>
  </tr>
  <tr>
    <td>5</td>
    <td><div align="center"><a href="IconInPort.png"><img src="IconInPort.png" width="50%;"></a></div></td>
    <td>Inport</td>
    <td>Name, list of property information</td>
  </tr>
  <tr>
    <td>6</td>
    <td><div align="center"><a href="IconPIP.png"><img src="IconPIP.png" width="50%;"></a></div></td>
    <td>PortInterfaceProfile</td>
    <td>InterfaceName, TypeName, PortInterfacePolarity</td>
  </tr>
  <tr>
    <td>7</td>
    <td><div align="center"><a href="IconMgr.png"><img src="IconMgr.png" width="50%;"></a></div></td>
    <td>Manager</td>
    <td>Components (list of created component names)<br>Loadable Modules (list of loadable module names)<br>Loaded Modules (list of loaded module names)</td>
  </tr>
</table>



According to the RTC specification, an RTC's LifeCycleState exists for each ExecutionContext. Therefore, multiple states exist, but RT System Editor displays STATE using only the first ExecutionContext.
<br>
<br>

