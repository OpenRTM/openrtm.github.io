---
layout: page
title: "openrtm integration plugin for choreonoid, python version (notes)"
---
#contents

### About the Choreonoid OpenRTM Integration Plugin
The OpenRTM integration plugin included standard with Choreonoid does not have the following functions.

- Configuration parameter setting function
- Data type identification function when connecting connectors

It seems that these functions are planned to be added soon, but at present, configure configuration parameters externally using RTShell or similar tools.

Care is required because connections are made even when the data types differ during connector connection.


### Known Bugs

There seem to be environments where Python modules cannot be loaded with RTCEditor.
The cause is under investigation.


### Unimplemented Functions

The function for executing RTCs started with the ComponentList item by simulator ticks is currently unimplemented.



### Libraries Used

The libraries used are as follows.

- Choreonoid
- boost-1.6.1
- Eigen
- omniORB-4.2.2
- OpenRTM-aist-1.2.0
- pybind11
- Python-2.7.13
- Qt 5.8
- yaml-0.1.7


The following libraries are also used in the sample components.

- ODE-0.13
- PySDL2
- SDL2

### Notes on Choreonoid
- The order of items may differ depending on the environment
- To localize a plugin into Japanese, prepare the language file **ja.po** inside the **po** folder.
```
 Plugin root directory
```
<table class="table-alt">
  <tr>
    <th>-po</th>
  </tr>
  <tr>
    <td>-ja.po</td>
  </tr>
</table>

In ja.po, list the text before and after translation as follows.

```
 msgid "RTC directory"
 msgstr "RTC directory"
```

This should automatically compile the PO file into an MO file, but since Choreonoid loads the file corresponding to the plugin name, the plugin name must be set correctly.

