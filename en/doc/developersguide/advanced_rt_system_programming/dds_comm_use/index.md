---
layout: page
title: "using dds communication functions"
---

<!-- Title: DDS通信機能の利用 -->
#contents

DDS (Data Distribution Service) is a communication middleware specification based on the publish-subscribe model defined by OMG.
Within a domain, Domain Participants communicate with other Domain Participants through DDS Publishers that distribute data and DDS Subscribers that receive data.
A Publisher can distribute data for a specified topic, and a Subscriber can receive data for a specified topic.


<div align="center"><a href="dds1.png"><img src="dds1.png" width="80%;"></a></div>

The conceptual diagram of DDS is shown in the figure above, but internally, communication is performed using multicast communication and unicast communication over UDP/IP.

<div align="center"><a href="dds2.png"><img src="dds2.png" width="80%;"></a></div>

Participants detect each other using PDP (Participant Discovery Protocol). At this time, messages such as unicast addresses are sent by multicast communication.
Next, SEDP (Endpoint Discovery Protocol) shares DataWriter and DataReader information using unicast communication. If the topic and data type match, the endpoints are determined to match, and data transmission and reception are started.

In addition, DDS has a function for controlling communication QoS (Quality of Service).

## Available Implementations
Currently, the following DDS implementations are supported.

- [Fast DDS]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/dds_comm_use/fast-rtps)
- [OpenSplice]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/dds_comm_use/opensplice)


