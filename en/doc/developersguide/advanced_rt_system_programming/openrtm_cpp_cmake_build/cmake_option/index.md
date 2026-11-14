---
layout: page
title: "cmake options"
---
<!-- Title: CMakeのオプション一覧 -->
#contents

## Option List

<table class="table-alt">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>CORBA</td>
    <td>Type of CORBA library to use (omniORB, TAO, ORBexpress)</td>
    <td>omniORB</td>
  </tr>
  <tr>
    <td>ORB_ROOT</td>
    <td>Directory where the CORBA library is installed</td>
    <td>If not specified, searched by FindPkgConfig for Ubuntu with omniORB. Otherwise, an error occurs.</td>
  </tr>
  <tr>
    <td>SSL_ENABLE</td>
    <td>Whether to generate the plugin for secure communication using SSL<br> ON: Generate<br> OFF: Do not generate</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>HTTP_ENABLE</td>
    <td>Whether to generate the plugin for HTTP communication<br> ON: Generate<br> OFF: Do not generate</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>OPENSSL_ROOT</td>
    <td>Directory containing the OpenSSL files. Required on Windows.</td>
    <td></td>
  </tr>
  <tr>
    <td>OBSERVER_ENABLE</td>
    <td>Whether to enable the Component Observer<br> ON: Enable<br> OFF: Disable</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>DOCUMENTS_ENABLE</td>
    <td>Whether to generate documentation with Doxygen<br> ON: Generate<br> OFF: Do not generate</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>ROS_ENABLE</td>
    <td>Whether to generate serializers and interfaces for ROS communication<br> ON: Generate<br> OFF: Do not generate</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>FASTRTPS_ENABLE</td>
    <td>Whether to generate interfaces for DDS (Fast-RTPS) communication<br> ON: Generate<br> OFF: Do not generate</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>ROS2_ENABLE</td>
    <td>Whether to generate serializers for ROS2 communication<br> ON: Generate<br> OFF: Do not generate</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>EXAMPLES_ENABLE</td>
    <td>Whether to build sample components<br> ON: Build<br> OFF: Do not build</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>UTILS_ENABLE</td>
    <td>Whether to build utility modules<br> ON: Build<br> OFF: Do not build</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>EXTLIB_ENABLE</td>
    <td>Whether to build external library modules<br> ON: Build<br> OFF: Do not build</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>FLUENTBIT_ENABLE</td>
    <td>Whether to build the Fluent Bit logger plugin<br> ON: Build<br> OFF: Do not build</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>FLUENTBIT_ROOT</td>
    <td>Directory of the Fluent Bit source code</td>
    <td></td>
  </tr>
  <tr>
    <td>OPENSPLICE_ENABLE</td>
    <td>Whether to generate interfaces for DDS (OpenSplice) communication<br> ON: Generate<br> OFF: Do not generate</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>OPENSPLICE_DIR</td>
    <td>Directory where OpenSplice is installed</td>
    <td></td>
  </tr>
  <tr>
    <td>RAPIDXML_DIR</td>
    <td>Directory where rapidxml is extracted</td>
    <td></td>
  </tr>
</table>

### omniORB Options

<table class="table-alt">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>OMNI_VERSION</td>
    <td>Major version of omniORB. Required when omniORB is built manually and installed in a custom location.</td>
    <td>If not specified, it is set automatically when omniORB is installed via pkg-config on Linux. Otherwise, an error occurs.</td>
  </tr>
  <tr>
    <td>OMNI_MINOR</td>
    <td>Minor version of omniORB. Required when omniORB is built manually and installed in a custom location.</td>
    <td>Same as above.</td>
  </tr>
  <tr>
    <td>OMNITHREAD_VERSION</td>
    <td>Version of omniThread. Required when omniORB is built manually and installed in a custom location.</td>
    <td>Same as above.</td>
  </tr>
</table>

### Dependencies of Buildable Modules

- OBSERVER_ENABLE
- DOCUMENTS_ENABLE
- EXAMPLES_ENABLE
- UTILS_ENABLE
- EXTLIB_ENABLE

These depend only on **libcoil** and **libRTC**.

- SSL_ENABLE
- ROS_ENABLE
- FASTRTPS_ENABLE

**EXTLIB_ENABLE** must be set to **ON**.

- ROS2_ENABLE

Since **FASTRTPS_ENABLE** must be set to **ON**, building **FastRTPSTransport** is required.

