---
layout: page
title: configuring the vxworks simulator
---

<!-- Title: VxWorksシミュレータの設定 -->
#contents

This page explains how to configure the VxWorks simulator that runs on Wind River Workbench.

## Adding a Simulator
The default simulator in Workbench is the linux_diab simulator.
Because OpenRTM-aist uses the GNU compiler, you need to use the linux_gnu simulator.

Click the Define a connection to remote system button to add a simulator.



<br>

<div align="center"><a href="sim1.png"><img src="sim1.png" width="60%;" align="center"></a></div>

<br>


In Select Remote System Type in the New Connection window, select ""Wind River VxWorks 6.x Simulator Connection"" and proceed to the next step.

<br>

<div align="center"><a href="sim2.png"><img src="sim2.png" width="60%;" align="center"></a></div>

<br>




In VxWorks Boot parameters, specify the linux_gnu simulator for Custom simulator.

- Example: /home/openrtm/WindRiver/vxworks-6.9/target/proj/linux_gnu/default/vxWorks

<br>

<div align="center"><a href="sim3.png"><img src="sim3.png" width="60%;" align="center"></a></div>

<br>


When you reach Network Options, set the network to Full Network and configure the IP address.
Click the Finish button to create the simulator.


<br>

<div align="center"><a href="sim4.png"><img src="sim4.png" width="60%;" align="center"></a></div>

<br>


## Starting the Network Interface
Start the network interface for the simulator.
Execute the following command.

```
sudo ${WIND_BASE}/host/${WIND_HOST_TYPE}/bin/vxsimnetd
```


A network interface named **tap0** is added.

If you want to use the Naming Service started on Ubuntu, restart the Naming Service with the following command.


```
sudo rtm-naming
```
