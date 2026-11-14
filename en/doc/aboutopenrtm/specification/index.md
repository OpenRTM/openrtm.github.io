---
layout: page
title: "openrtm-aist specifications"
---

<!-- Title: OpenRTM-aist Specifications -->
#contents

OpenRTM-aist consists of an RT Component Framework, RT Middleware, a collection of basic RT Components, libraries, basic services, and development tools.

The RT Component Framework provides the base classes required to create RT Components. All RT Components are implemented as subclasses of these base classes.

RT Middleware is responsible for loading RT Component modules created using the framework, managing their lifecycle (including instance creation and destruction), and registering components with the Naming Service.

OpenRTM-aist also includes libraries that improve usability, basic services such as RT Component registration and discovery (currently using the CORBA Naming Service), RTCBuilder for generating RT Component skeleton code, and tools such as RTSystemEditor for connecting and controlling RT Components.

Currently, OpenRTM-aist supports C++, Python, and Java, and can operate on Windows, UNIX-like operating systems, and μITRON-based operating systems (C++ edition only).

In addition, SEC Corporation provides OpenRTM .NET, an OpenRTM-aist-compatible middleware implementation that enables the creation and execution of RTCs in .NET environments, including C#.

RTCs developed in different programming languages and running on different operating systems can be interconnected and operate cooperatively.

## Interface Specifications

- Conforms to OMG Robotic Technology Component Specification 1.0
  - [OMG Specification formal/12-09-01](https://www.omg.org/spec/RTC/1.1/)
- Conforms to OMG Super Distributed Object Specification 1.1
  - [OMG Specification formal/08-10-01](http://www.omg.org/spec/SDO/1.1/)

### References

- [OMG (Object Management Group)](http://www.omg.org)
- [OMG Specifications](http://www.omg.org/technology/documents/spec_catalog.htm)

## Components

OpenRTM-aist consists of the following middleware libraries and development tools.

<div align="center"><strong>Components of OpenRTM-aist</strong></div>

<table class="table-alt">
  <tr>
    <td>Name</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>OpenRTM-aist (C++ Edition)</td>
    <td>Component framework, middleware libraries, and command-line tools for developing RT Components in C++.</td>
  </tr>
  <tr>
    <td>OpenRTM-aist (Python Edition)</td>
    <td>Component framework, middleware libraries, and command-line tools for developing RT Components in Python.</td>
  </tr>
  <tr>
    <td>OpenRTM-aist (Java Edition)</td>
    <td>Component framework, middleware libraries, and command-line tools for developing RT Components in Java.</td>
  </tr>
  <tr>
    <td>RTCBuilder</td>
    <td>An Eclipse plug-in for designing RT Components and generating source code.</td>
  </tr>
  <tr>
    <td>RTSystemEditor</td>
    <td>An Eclipse plug-in for operating RT Components and designing and managing RT systems.</td>
  </tr>
  <tr>
    <td>rtshell</td>
    <td>A set of command-line tools for operating RT Components and RT systems from a CUI environment.</td>
  </tr>
</table>

These software packages are distributed under a dual-license model consisting of EPL and separate commercial license agreements.

## System Requirements

### OpenRTM-aist (C++ Edition)

<table class="table-alt">
  <tr>
    <td>Compiler</td>
    <td>gcc 3.x or later, Visual C++ 2008, 2010, 2012, 2013, 2015, 2017, 2019</td>
  </tr>
  <tr>
    <td>Operating System</td>
    <td>Linux, FreeBSD, Windows, Mac OS X, TOPPERS ASP</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>i386, x86_64, ppc, arm</td>
  </tr>
  <tr>
    <td>Dependent Libraries</td>
    <td>omniORB 4.0 or later, libuuid (Linux)</td>
  </tr>
</table>

### OpenRTM-aist (Python Edition)

<table class="table-alt">
  <tr>
    <td>Python</td>
    <td>Python 2.7, Python 3.6, Python 3.7</td>
  </tr>
  <tr>
    <td>Dependent Libraries</td>
    <td>omniORBpy 2.3 or later</td>
  </tr>
</table>

### OpenRTM-aist (Java Edition)

<table class="table-alt">
  <tr>
    <td>Java</td>
    <td>JDK 5 or later</td>
  </tr>
  <tr>
    <td>Dependent Libraries</td>
    <td>Java IDL included with the JDK</td>
  </tr>
</table>

### RTCBuilder / RTSystemEditor

<table class="table-alt">
  <tr>
    <td>Eclipse</td>
    <td>Version 3.4 or later</td>
  </tr>
  <tr>
    <td>Java</td>
    <td>JDK 6 or later</td>
  </tr>
  <tr>
    <td>Dependent Libraries</td>
    <td>
      Eclipse EMF 2.2 or later (including SDO and XSD)<br>
      Eclipse GEF 3.2 or later (including Draw2D)
    </td>
  </tr>
</table>

### rtshell

<table class="table-alt">
  <tr>
    <td>Python</td>
    <td>Python 2.7, Python 3.6, Python 3.7</td>
  </tr>
  <tr>
    <td>Dependent Libraries</td>
    <td>omniORBpy 2.3 or later</td>
  </tr>
</table>
