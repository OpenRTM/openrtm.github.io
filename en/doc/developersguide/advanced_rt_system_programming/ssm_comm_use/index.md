---
layout: page
title: "using the ssm communication feature"
---

<!-- Title: Using the SSM Communication Feature -->

#contents

This page describes how to install the communication plugin for [SSM (Streaming-data-Sharing-Manager)](https://github.com/sitRyo/Distributed-Streaming-data-Sharing-Manager).

The following procedures assume an Ubuntu 18.04 environment.

## Installing SSM

Install SSM using the following commands.

```sh
git clone https://github.com/sitRyo/Distributed-Streaming-data-Sharing-Manager -b 32-64bit
cd Distributed-Streaming-data-Sharing-Manager/
./configure --prefix=${OPENRTM_INSTALL_DIR}
sudo autoreconf -i -f
make
make install
```

## Building and Installing OpenRTM-aist

Turn ON the **SSM_ENABLE** option when running CMake. If you want to specify the SSM installation directory, set **SSM_ROOT**.

```sh
cmake -DSSM_ENABLE=ON -DSSM_ROOT=${OPENRTM_INSTALL_DIR} ..
```

The remaining steps are the same as the standard build procedure.

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

After building, install OpenRTM-aist.

```sh
cmake --build . --config Release --target install
```

#### Operation Check

Create the following rtc.conf.

```text
manager.modules.load_path: /usr/local/lib/openrtm-2.0/transport/
manager.modules.preload: SSMTransport.so
manager.components.preconnect: ConsoleOut0.in?interface_type=ssm&ssm.stream_name=test_stream&dataflow_type=pull, ConsoleIn0.out?interface_type=ssm&ssm.stream_name=test_stream
manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

Start **ssm-coordinator** before launching the RTCs.

```sh
ssm-coordinator
```

Launch **ConsoleInComp** and **ConsoleOutComp** from separate terminals to verify that data is transferred correctly.

### Connection Options

The following options can be configured in the connector profile when connecting data ports.

<table class="table-alt">
  <tr>
    <th>Option Name</th>
    <th>Default Value</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>ssm.stream_name</td>
    <td>sensor_test</td>
    <td></td>
  </tr>
  <tr>
    <td>ssm.stream_size</td>
    <td>0</td>
    <td></td>
  </tr>
  <tr>
    <td>ssm.life_ssm_time</td>
    <td>5.0</td>
    <td></td>
  </tr>
  <tr>
    <td>ssm.cycle_ssm_time</td>
    <td>0.05</td>
    <td></td>
  </tr>
  <tr>
    <td>ssm.stream_id</td>
    <td>0</td>
    <td></td>
  </tr>
</table>

## Simple Operation Check

When OpenRTM-aist is built and installed, a configuration file for a simple operation check of **SSMTransport** is installed.

```sh
${SSM_INSTALL_DIR}/bin/ssm-coordinator
```

```sh
source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/transport/rtc.ssm.conf
```
