---
layout: page
title: "procedure for implementing a custom interface type for data ports"
---

<!-- Title: データポートの独自インターフェース型の実装手順 -->
#contents

OpenRTM-aist data ports basically transfer data through CORBA method calls, but by adding communication interface plugins, various communication protocols can be selected.

<br>

<div align="center"><a href="if1.png"><img src="if1.png" width="100%;"></a></div>

<br>

This page explains how to add a custom communication interface.
Please also refer to the following procedure for creating a custom serializer.

- [Procedure for Implementing a Custom Serializer]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/implement_original_serializer)

OpenRTM-aist has Push-type and Pull-type communication as data flow types, as well as a duplex type for bidirectional communication, although it is still under implementation.
Push-type communication consists of **InPortConsumer** and **InPortProvider**, while Pull-type communication consists of **OutPortConsumer** and **OutPortProvider**.

In Push-type communication, the Publisher on the OutPort side calls the **put** function of InPortConsumer, and data is transferred to InPortProvider inside the put function.
InPortProvider calls the write function of the InPortConnector object to add data.

<br>

<div align="center"><a href="if2.png"><img src="if2.png" width="70%;"></a></div>

<br>

In Pull-type communication, the InPort side calls the **get** function of OutPortConsumer, and data is obtained from OutPortProvider inside the get function.
On the OutPort side, OutPortProvider calls the read function of OutPortConnector, obtains the data, and passes it to OutPortConsumer.

<br>

<div align="center"><a href="if3.png"><img src="if3.png" width="70%;"></a></div>

<br>


Therefore, a custom communication interface can be implemented by implementing InPortConsumer and InPortProvider for Push-type communication, or OutPortConsumer and OutPortProvider for Pull-type communication.



The implementation procedures for custom interface types are shown below.

- [Procedure for Implementing a Custom Interface Type (C++)]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/implement_dataport_interface_type/cpp/)
- [Procedure for Implementing a Custom Interface Type (Python)]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/implement_dataport_interface_type/python/)
- [Procedure for Implementing a Custom Interface Type (Java)]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/implement_dataport_interface_type/java/)

