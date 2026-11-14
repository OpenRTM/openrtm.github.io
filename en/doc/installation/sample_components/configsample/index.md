---
layout: page
title: "configsample"
---

<!-- Title: ConfigSample -->
#contents

This sample is included with the C++, Python, and Java editions of OpenRTM-aist.

### Overview

This sample demonstrates how to use configuration sets in RT Components.

Start the ConfigSample component. When the component starts successfully, configuration sets are already configured in advance.

Use RTSystemEditor to inspect the configuration sets.

If an error message such as "The specified path could not be found." occurs when starting the component, modify the value of "example.ConfigSample.config_file" in the rtc.conf file located in the RTMExamples/ConfigSample directory as follows.

- Replace it with the path shown below.

```text
.\\RTMExamples\\ConfigSample\\configsample.conf
(Use '\\' instead of '\' between directory names and file names.)
```

- Alternatively, replace it with the full path to "configsample.conf". In this case as well, use '\\' between directory names and file names as described above.

### Startup Screen

<div align="center"><a href="ConfigSample_example_rtse_ja.png"><img src="ConfigSample_example_rtse_ja.png" width="60%;"></a></div>
<div align="center"><strong>ConfigSample Execution Example</strong></div>

### Usage

The dataset corresponding to the ConfigurationSet selected and configured in the ConfigurationView of RTSystemEditor is displayed on the prompt and continuously updated.

- Procedure

  - Start RTSystemEditor and prepare a SystemEditor. For details on using RTSystemEditor, refer to [RTSystemEditor]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_2_0).

  - Start the ConfigSample component. The startup method depends on the operating system and OpenRTM-aist language edition. Refer to the table below.

<table class="table-alt">
  <tr>
    <th></th>
    <th>Windows</th>
    <th>Linux</th>
  </tr>
  <tr>
    <td>C++ Edition</td>
    <td>ConfigSample.bat</td>
    <td>ConfigSampleComp</td>
  </tr>
  <tr>
    <td>Python Edition</td>
    <td>ConfigSample.bat</td>
    <td>ConfigSample.py</td>
  </tr>
  <tr>
    <td>Java Edition</td>
    <td>ConfigSample.bat</td>
    <td>ConfigSample.sh</td>
  </tr>
</table>

  - The component will appear in the Name Service View of RTSystemEditor. Drag it onto the SystemEditor.

  - Select an appropriate ConfigurationSet (default, mode0, or mode1) from the Configuration View of RTSystemEditor.

  - Modify the values as necessary.

  - Click the [Apply] button.

