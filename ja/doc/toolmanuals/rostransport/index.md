---
layout: page
title: rosトランスポート(rosport)
---

init
<!-- Title: ROSトランスポート(rosport) -->
Communicating with ROS nodes

This is the announcement for ROS support in OpenRTM-aist. This page will shortly be replaced with a tutorial on using the ports.

<br>

パッチのダウンロードは[こちら](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.0/ros_transport.patch-1.0.0.tar.gz)です。

サンプルコンポーネントは[こちら](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.0/examples.ros-1.0.0.tar.gz)でダウンロードができます。

<br>

Although I guess it's not a common thing yet, there have been murmurings
for quite a while now here in Japan about a desire to be able to use
OpenRTM-aist and ROS together. We would gain the huge range of
functional software and the persistent channel-based communications of
ROS, and keep the strong life-cycle and execution management of
OpenRTM-aist.

<br>

So here's a patch for OpenRTM-aist that does exactly that.

<br>

This patch adds a new transport type to OpenRTM-aist specifically for
communicating across ROS channels. No doubt someone will find the
ability to use a persistent channel for communication useful, but the
main benefit is that it gives nearly-seamless communications between
components written for OpenRTM-aist and nodes written for ROS. Your
network of distributed components/nodes no longer has to be in just one
framework.

<br>

There are no wrappers involved. It's all native communication using the
same ROS libraries as you would use in a pure-ROS system - no
translation layers means maximum efficiency. You create a port type for
the ROS transport, and off you go. If you already know ROS, you'll feel
right at home using the ports.

<br>

The one caveat is why I say nearly-seamless: we still don't have a
unified set of types (also, there are some issues with the typing system
in OpenRTM-aist that we're working to sort out). Fortunately, the types
issue is a hot topic amongst framework designers at the moment, so I
hope we will have solved that problem before too long.

<br>

I have attached both the patch, for OpenRTM-aist-1.0.0, and a set of
examples for each port type (publisher/subscriber/client/server). I hope
to get a web page up on the OpenRTM-aist site shortly with a more
detailed explanation of usage; for now, the examples and the doxygen
comments in the source will point you in the right direction - it's all
pretty simple.

<br>

Comments, suggestions, and improvements are welcome.

