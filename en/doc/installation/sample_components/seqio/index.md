---
layout: page
title: "seqio"
---

<!-- **SeqIO -->
#contents

This sample is included with the C++, Python, and Java editions of OpenRTM-aist.

### Overview

This sample demonstrates how to use InPorts and OutPorts. When the SeqIn and SeqOut components are started, a GUI or console window is displayed.

Both SeqIn and SeqOut provide the following DataPort types:

TimedShort, TimedLong, TimedFloat, TimedDouble, TimedShortSeq, TimedLongSeq, TimedFloatSeq, and TimedDoubleSeq.

The output of each port is determined by random values. When corresponding ports are connected, the output values on the SeqOut side and the input values on the SeqIn side are displayed in their respective GUI or console windows. (Use RTSystemEditor to connect the ports.)

### Startup Screens

<div align="center"><a href="SeqIO_example_rtse_ja.png"><img src="SeqIO_example_rtse_ja.png" width="60%;"></a></div>
<div align="center"><strong>SeqIO Execution Example (RTSystemEditor Connection Screen)</strong></div>

<div align="center"><a href="SeqIO_example_cpp.png"><img src="SeqIO_example_cpp.png" width="60%;"></a></div>
<div align="center"><strong>SeqIn and SeqOut Component Execution Example (C++ Edition)</strong></div>

<div align="center"><a href="SeqIO_example_python.png"><img src="SeqIO_example_python.png" width="60%;"></a></div>
<div align="center"><strong>SeqIn and SeqOut Component Execution Example (Python Edition)</strong></div>

<div align="center"><a href="SeqIO_example_java.png"><img src="SeqIO_example_java.png" width="60%;"></a></div>
<div align="center"><strong>SeqIn and SeqOut Component Execution Example (Java Edition)</strong></div>

### Usage

The SeqIO sample continuously outputs numeric data from SeqOut, sends it to SeqIn through data ports, and displays it in a GUI or console window.

Connect the corresponding ports of SeqOut and SeqIn in RTSystemEditor. When both components are activated, not only the values output by SeqOut but also the values received by SeqIn change continuously, allowing observation of data port input and output.

- Procedure

  - Start RTSystemEditor and prepare a SystemEditor. For details on using RTSystemEditor, refer to [RTSystemEditor]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_2_0).

  - Start both the SeqOut and SeqIn components. The startup method depends on the operating system and the OpenRTM-aist language edition. Refer to the table below.

<table class="table-alt">
  <tr>
    <th></th>
    <th colspan="2">Windows</th>
    <th colspan="2">Linux</th>
  </tr>
  <tr>
    <td></td>
    <td>SeqIn Component</td>
    <td>SeqOut Component</td>
    <td>SeqIn Component</td>
    <td>SeqOut Component</td>
  </tr>
  <tr>
    <td>C++ Edition</td>
    <td>SeqIn.bat</td>
    <td>SeqOut.bat</td>
    <td>SeqInComp</td>
    <td>SeqOutComp</td>
  </tr>
  <tr>
    <td>Python Edition</td>
    <td>SeqIn.bat</td>
    <td>SeqOut.bat</td>
    <td>SeqIn.py</td>
    <td>SeqOut.py</td>
  </tr>
  <tr>
    <td>Java Edition</td>
    <td>SeqIn.bat</td>
    <td>SeqOut.bat</td>
    <td>SeqIn.sh</td>
    <td>SeqOut.sh</td>
  </tr>
</table>

  - Both components will appear in the NameServiceView of RTSystemEditor. Drag them onto the SystemEditor.

  - Connect the corresponding ports of the two components. (Refer to the SeqIO execution example above.)

  - Right-click either component and select [Activate System].

