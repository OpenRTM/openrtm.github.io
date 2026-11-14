---
layout: page
title: about rt middleware / openrtm-aist
---

<!-- Title: RTミドルウェア / OpenRTM-aist について -->
#contents
#clear


## What is RT Middleware? 
Not only individual robots, but also various available robot functional elements are called RT (Robot Technology/Robotic Technology).
RT Middleware is a platform for modularizing these various functional elements and integrating them as software.
The purpose of RT Middleware is to establish an open-architecture platform whose specifications are open and in which various implementations can interconnect with each other.
Therefore, RT Middleware is a term that refers to this overall platform.

## What is an RT Component?
In RT Middleware, robot functional elements are modularized as software components called RT Components, and robots are realized by combining RT Components on RT Middleware.
RT Components have data ports and service ports for communication and interaction with other components, and by standardizing these interface specifications, various components can be easily connected to each other.
In addition, RT Components have common internal states and state transitions, allowing upper-level application programs to handle many components in a unified manner.
Furthermore, because they have a standard interface that allows internal parameter settings to be operated externally, they can be reused for various purposes without recompilation.

## What is OpenRTM-aist?
OpenRTM-aist is one implementation of RT Middleware implemented and distributed by AIST.
It consists of an RT Component framework for creating RT Components, RT Middleware for managing and operating the lifecycle of RT Components, RTCBuilder for creating component template code, and RTSystemEditor, a GUI tool for operating and connecting RT Components.
Currently, AIST provides implementations for C++, Python, and Java.~
<!-- このほかに、この OpenRTM-aist を他の言語へ移植したバージョンも開発されており、現在 Version0.2.0 互換の実装としては、Java版および .NET版の OpenRTM 互換ミドルウエアが存在します。 -->
<!--  -->
<!-- **OpenRTM-aist の現在のバージョンは？ -->
<!-- OpenRTM-aist の現在のバージョンは1.0.0です。 -->
<!--  -->
## What languages are supported?
OpenRTM-aist provides a framework for developing RT Components in C++, Python, and Java.

## What OSes are supported?
OpenRTM-aist is currently verified to run on FreeBSD, Linux, and Windows.
<!-- 動作する FreeBSD のバージョン、Linux ディストリビューション 及び Windows は以下の通りです。 -->
<!-- -FreeBSD (5.2, 6.0, 6.2) -->
<!-- -Vine Linux (3.2, 4.0)  -->
<!-- -Fedora Core (4, 5, 6) -->
<!-- -Debian3.1(Sarge)  -->
<!-- -Ubuntu Linux 7 -->

## What is the license?
OpenRTM-aist is provided under a dual licensing system consisting of the LGPL (GNU Lesser General Public License) and a license individually contracted with AIST.
The individual license is a license that allows distribution with the source kept closed when you want to modify the source code of OpenRTM-aist and use it commercially.
In particular, for uses such as embedded systems, source modifications are usually required, so this kind of license is provided to promote use by companies and other organizations.

## What is the license of components I create?
Components can be created and distributed as dynamically linkable libraries (called Shared Objects on UNIX and DLLs (Dynamic Link Libraries) on Windows), so components that are dynamically linked with and use the OpenRTM-aist core library are not subject to any particular restrictions under the LGPL license.
The creator can set an individual license.
However, if you agree with our aim of promoting component reuse, we would appreciate it if you made the components you create open at the source code level.

