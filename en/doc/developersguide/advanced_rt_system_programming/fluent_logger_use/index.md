---
layout: page
title: "log collection with fluent logger"
---

<!-- Title: Fluent Loggerによるログ収集 -->
#contents

Fluentd and Fluent Bit are open-source software libraries for processing and forwarding logs.

- [fluentd](https://www.fluentd.org/)
- [fluentbit](https://fluentbit.io/)

Fluentd and Fluent Bit can be configured with Input plugins that collect data and Output plugins that send data.
The overview diagram of Fluentd and Fluent Bit is as follows.

<div align="center"><a href="fluentbit2.png"><img src="fluentbit2.png" width="80%;"></a></div>

Input passes collected data to Output by receiving data from external processes, writing logs from inside processes, obtaining CPU usage, disk usage, and so on.
Output sends the received data to external processes, writes it to files, outputs it to standard output, and so on.
Input and Output are implemented as plugins, and by changing the plugins, the methods for collecting and sending data can be changed. Therefore, various data collection and transmission methods such as the following can be selected.

- [Inputs - Fluent Bit: Official Manual](https://docs.fluentbit.io/manual/pipeline/inputs)
- [Outputs - Fluent Bit: Official Manual](https://docs.fluentbit.io/manual/pipeline/outputs)

In addition, before data is passed from Input to Output, data conversion, addition, exclusion, and so on can be performed by Filter.

Tags can be set for Input, and matching rules can be set for Output and Filter.
Output and Filer can receive data with tags that match the matching rules.

This page explains how to use the Fluent Logger plugin of OpenRTM-aist.

## C++ Version

### Windows
#### Installing Fluent Bit

Bison/Flex is required to build Fluent Bit, so extract it to an appropriate location and set it in the PATH environment variable.

- https://sourceforge.net/projects/winflexbison/

set PATH=%WORKDIR%\win_flex_bison-2.5.24;%PATH%


Extract OpenSSL to an appropriate location.

- [How to Use SSLTransport]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ssltransport_use)


Extract the Fluent Bit source code modified for Windows to an appropriate location, and move to that folder in PowerShell.

- https://github.com/Nobu19800/fluent-bit

Run the following commands in PowerShell to build Fluent Bit.

```
 cmake -DFLB_RELEASE=On -DFLB_TRACE=Off -DFLB_SHARED_LIB=On -DFLB_EXAMPLES=Off  -DCMAKE_BUILD_TYPE=Release -DOPENSSL_ROOT_DIR=${OpenSSL_INSTALL_DIR} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=${FLUENTBIT_INSTALL_DIR}
 cmake --build . --config Release
 cmake --build . --target install --config Release
```


#### Installing Various Libraries
Copy the required header files with the following commands.

```
 $FLUENTBIT_BUILD_DIR = "${FLUENTBIT_SOURCE_DIR}\build"
```

```
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\monkey\include\monkey\mk_core\external -destination $FLUENTBIT_INSTALL_DIR\include\monkey\mk_core -recurs
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\monkey\mk_core\deps\libevent\include\event.h $FLUENTBIT_INSTALL_DIR\include
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\monkey\mk_core\deps\libevent\include\evutil.h $FLUENTBIT_INSTALL_DIR\include
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\monkey\mk_core\deps\libevent\include\event2 -destination $FLUENTBIT_INSTALL_DIR\include -recurs
 Copy-Item $FLUENTBIT_BUILD_DIR\lib\monkey\mk_core\deps\libevent\include\event2\event-config.h $FLUENTBIT_INSTALL_DIR\include\event2
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\msgpack-*\include\msgpack.h $FLUENTBIT_INSTALL_DIR\include
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\msgpack-*\include\msgpack -destination $FLUENTBIT_INSTALL_DIR\include -recurs
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\mbedtls-*\include\mbedtls -destination $FLUENTBIT_INSTALL_DIR\include -recurs
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\c-ares-*\include\*.h $FLUENTBIT_INSTALL_DIR\include
 Copy-Item $FLUENTBIT_BUILD_DIR\lib\c-ares-*\ares_build.h $FLUENTBIT_INSTALL_DIR\include
 Copy-Item $FLUENTBIT_BUILD_DIR\lib\c-ares-*\ares_config.h $FLUENTBIT_INSTALL_DIR\include
 Copy-Item $FLUENTBIT_BUILD_DIR\lib\c-ares-*\ares_config.h $FLUENTBIT_INSTALL_DIR\include
 New-Item $FLUENTBIT_INSTALL_DIR\lib\fluent-bit -ItemType Directory
 Copy-Item $FLUENTBIT_BUILD_DIR\library\Release\fluent-bit.lib $FLUENTBIT_INSTALL_DIR\lib\fluent-bit
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\cmetrics\include\cmetrics -destination $FLUENTBIT_INSTALL_DIR\include -recurs
 Copy-Item $FLUENTBIT_SOURCE_DIR\lib\cmetrics\include\prometheus_remote_write -destination $FLUENTBIT_INSTALL_DIR\include -recurs
```

#### Building OpenRTM-aist

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

When running CMake, set the **FLUENTBIT_ENABLE** and **FLUENTBIT_ROOT** options.

```
 cmake -DORB_ROOT=$ORB_ROOT -DFLUENTBIT_ENABLE=ON -DFLUENTBIT_ROOT=$FLUENTBIT_INSTALL_DIR -DCMAKE_INSTALL_PREFIX=$OPENRTM_INSTALL_DIR
```

The other steps are the same as the normal build procedure.

Install with the following command.

```
 cmake --build . --target install --config Release
```

#### Operation Check

td-agent or td-agent-bit must be installed and started.

- [Procedure for Installing and Starting Log Collection Software]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/fluent_logger_install)


##### Starting the RTC


Configure rtc.conf as follows. Change the tag name as needed.

```
 
 logger.plugins: C:\\Program Files\\OpenRTM-aist\\logger\\2.0.0\\FluentBit.dll
 logger.logstream.fluentd.output0.plugin: forward
 logger.logstream.fluentd.output0.conf.match:*
 
 logger.logstream.fluentd.input0.plugin: lib
 logger.logstream.fluentd.input0.conf.tag: test.simpleio
```

When the RTC is executed, logs are sent.

Alternatively, you can start it using **rtc.fluentbit_stream.conf** included with OpenRTM-aist.

```
 ${OPENRTM_INSTALL_DIR}\2.0.0\Components\C++\Examples\vc16\ConsoleOutComp.exe -f ${OPENRTM_INSTALL_DIR}\2.0.0\ext\logger\rtc.fluentbit_stream.conf
```

### Ubuntu
#### Installing Fluent Bit

```
 sudo apt install flex bison
 wget https://github.com/fluent/fluent-bit/archive/v1.8.9.tar.gz
 tar xf v1.8.9.tar.gz
 cd fluent-bit-1.8.9/
 sed  -i -e 's/jemalloc-5.2.1\/configure/jemalloc-5.2.1\/configure --disable-initial-exec-tls/g' CMakeLists.txt
 cd build
 cmake .. -DFLB_RELEASE=On -DFLB_TRACE=Off -DFLB_JEMALLOC=On -DFLB_TLS=On -DFLB_SHARED_LIB=On -DFLB_EXAMPLES=Off -DFLB_HTTP_SERVER=On -DFLB_IN_SYSTEMD=On -DFLB_OUT_KAFKA=Off
 cmake --build . --config Release -- -j$(nproc)
 sudo cmake --build . --target install
```

#### Installing Various Libraries
Copy the required header files with the following commands.

```
 export FLUENTBIT_SOURCE_DIR=${WORKSPACE}/fluent-bit-1.8.9
 export FLUENTBIT_BUILD_DIR = ${FLUENTBIT_SOURCE_DIR}/build
 export FLUENTBIT_INSTALL_DIR=/usr/local
```

```
 mkdir -p ${FLUENTBIT_INSTALL_DIR}/include/lib/flb_libco
 cp -r ${FLUENTBIT_SOURCE_DIR}/lib/flb_libco/libco.h ${FLUENTBIT_INSTALL_DIR}/include/lib/flb_libco
 cp -r ${FLUENTBIT_BUILD_DIR}/include/jemalloc ${FLUENTBIT_INSTALL_DIR}/include/
 cp -r ${FLUENTBIT_SOURCE_DIR}/lib/msgpack-*/include/* ${FLUENTBIT_INSTALL_DIR}/include/
 cp -r ${FLUENTBIT_SOURCE_DIR}/lib/monkey/include/monkey ${FLUENTBIT_INSTALL_DIR}/include/
 cp -r ${FLUENTBIT_SOURCE_DIR}/lib/mbedtls-*/include/mbedtls ${FLUENTBIT_INSTALL_DIR}/include/
 cp -r ${FLUENTBIT_SOURCE_DIR}/lib/c-ares-*/include/* ${FLUENTBIT_INSTALL_DIR}/include/
 cp -r ${FLUENTBIT_BUILD_DIR}/lib/c-ares-*/ares_build.h ${FLUENTBIT_INSTALL_DIR}/include/
 cp -r ${FLUENTBIT_BUILD_DIR}/lib/c-ares-*/ares_config.h ${FLUENTBIT_INSTALL_DIR}/include/
 cp -r ${FLUENTBIT_SOURCE_DIR}/lib/cmetrics/include/* ${FLUENTBIT_INSTALL_DIR}/include/
 cp ${FLUENTBIT_SOURCE_DIR}/lib/flb_libco/libco.h ${FLUENTBIT_INSTALL_DIR}/include/
```

#### Building OpenRTM-aist

- [OpenRTM-aist Build Procedure]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build)

When running CMake, set the **FLUENTBIT_ENABLE** and **FLUENTBIT_ROOT** options.

```
 cmake -DFLUENTBIT_ENABLE=ON -DFLUENTBIT_ROOT=${FLUENTBITINSTALLDIR} ..
```

The other steps are the same as the normal build procedure.

Install with the following command.

```
 cmake --build . --target install
```

#### Operation Check

td-agent or td-agent-bit must be installed and started.

- [Procedure for Installing and Starting Log Collection Software]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/fluent_logger_install)


##### Starting the RTC


Configure rtc.conf as follows. Change the tag name as needed.


```
 logger.plugins: /usr/local/lib/openrtm-2.0/logger/FluentBit.so
 logger.logstream.fluentd.output0.plugin: forward
 logger.logstream.fluentd.output0.conf.match:*
 
 logger.logstream.fluentd.input0.plugin: lib
 logger.logstream.fluentd.input0.tag: test.simpleio
```

When the RTC is executed, logs are sent.

If it does not work, remove broken links from /etc/ssl/certs.


Alternatively, you can start it using **rtc.fluentbit_stream.conf** included with OpenRTM-aist.

```
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/logger/rtc.fluentbit_stream.conf
```

## Python Version
The Python version of the Fluent Logger plugin supports only Forward Output.
It can be used by separately starting Fluentd or Fluent Bit that receives Forward communication, processing it, and sending it with another Output plugin.

### Installing fluent-logger-python
fluent-logger-python must be installed.

```
 pip install fluent-logger
```

<!-- - https://github.com/fluent/fluent-logger-python/releases -->

<!-- Extract fluent-logger-python-0.9.3.zip to an appropriate location and run the following command. -->

<!-- python setup.py install -->

For Ubuntu, run it with sudo.

### Operation Check
td-agent or td-agent-bit must be installed.

- [Procedure for Installing and Starting Log Collection Software]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/fluent_logger_install)

#### Starting the RTC
When you write the following in rtc.conf and start the RTC, logs are sent to fluentd.

```
 manager.modules.load_path: C:\\Python37\\Lib\\site-packages\\OpenRTM_aist\\ext\\logger\\fluentlogger
 logger.plugins: FluentLogger.py
 logger.logstream.fluentd.output0.tag: test.simpleio
```

Change **manager.modules.load_path** as needed according to the Python path where OpenRTM-aist is installed.
For Ubuntu, it becomes something like **/usr/local/lib/python2.7/dist-packages/OpenRTM_aist/ext/logger/fluentlogger**.

Logs are displayed in fluentd as follows.

```
 2018-12-26 09:06:18.000000000 +0900 test.simpleio: {"message":"exit","time":"2018-12-26 09:06:18,841","name":"fluent.ec_worker","level":"TRACE"}
```

The message contents, name, time when the log was sent, and log level are sent.


## Simple Operation Check
When OpenRTM-aist is built and installed, a configuration file for a simple operation check of the Fluent Logger plugin is installed.

```
 %RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
 %RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\logger\rtc.fluentbit_stream.conf
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/logger/rtc.fluentbit_stream.conf
```

## Log Visualization with Kibana+Elasticsearch

[Kibana](https://www.elastic.co/jp/kibana/) is a data visualization tool developed by Elastic.
By working together with the analysis engine [ElasticSearch](https://www.elastic.co/jp/elasticsearch/), it enables data visualization such as graphs in a web browser.

This section explains the procedure for sending logs from the OpenRTM-aist Fluent Bit plugin to ElasticSearch and visualizing the data with Kibana.

### Installing Elasticsearch
Install Elasticsearch in an Ubuntu 18.04 environment with the following commands.
Depending on the Elasticsearch version, it may not work on Ubuntu 18.04, so install version 7.8.0, whose operation has been verified here.

```
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 add-apt-repository "deb https://artifacts.elastic.co/packages/7.x/apt stable main"
 sudo apt update
 sudo apt install elasticsearch=7.8.0
 sudo systemctl daemon-reload
 sudo systemctl enable elasticsearch.service
```

Edit **/etc/elasticsearch/elasticsearch.yml**.

```
 network.bind_host: 0
 discovery.seed_hosts: ["127.0.0.1", "[::1]"]
```


Restart the service after editing.

```
 sudo systemctl restart elasticsearch.service
```

If it cannot start due to insufficient memory, edit **/etc/elasticesearch/jvm.options** and adjust it.

 -Xms1g
 -Xmx1g


### Installing Kibana
Install Kibana with the following command. Specify the same version as Elasticsearch.

```
 sudo apt install kibana=7.8.0
 sudo systemctl daemon-reload
 sudo systemctl enable kibana.service
```

Also, add the following lines to **/etc/kibana/kibana.yml**.

```
 server.port: 5601
 server.host: "0.0.0.0"
```

Specify the IP address set for the NIC in **server.host**.

```
 server.host: "192.168.11.2"
```


Restart the service.

```
 sudo systemctl restart kibana.service
```

### Operation Check

Create the following rtc.conf.

```
 logger.enable: YES
 logger.log_level: INFO
 
 
 logger.plugins: ${OPNRTM_INSTALL_DIR}/lib/openrtm-2.0/logger/FluentBit.so
 
 logger.logstream.fluentd.input.plugin: lib
 logger.logstream.fluentd.input.conf.tag: myRTCs_log
 
 logger.logstream.fluentd.output0.plugin: es
 logger.logstream.fluentd.output0.conf.match: *
 logger.logstream.fluentd.output0.conf.host: 127.0.0.1
 logger.logstream.fluentd.output0.conf.port: 9200
 logger.logstream.fluentd.output0.conf.Index: fluentbit
```

Replace ${OPNRTM_INSTALL_DIR} with the path where OpenRTM-aist is installed.
Specify the Elasticsearch address and port number in **host** and **port**.
Set any strings for **Index** and **tag**.

Start the RTC by specifying this rtc.conf.

```
 ./share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f rtc.conf
```


Next, access Kibana from a web browser and check the logs.
Access **http://127.0.0.1:5601**. If accessing from another terminal, change the IP address.


<div align="center"><a href="kibana1.png"><img src="kibana1.png" width="50%;"></a></div>

Set the index pattern for the data to visualize. In this example, **fluentbit** was specified for Index in rtc.conf.
When the page opens, click the upper left, and then click **Stack Management** under Managment from the displayed menu.

<div align="center"><a href="kibana2.png"><img src="kibana2.png" width="60%;"></a></div>

Click **Index Patterns** on the left side of the Stack Management page.

<div align="center"><a href="kibana3.png"><img src="kibana3.png" width="60%;"></a></div>

On the Index patterns page, press the **Create Index pattern** button.

<div align="center"><a href="kibana4.png"><img src="kibana4.png" width="60%;"></a></div>

On the Create index pattern page, specify **fluentbit*** for Index pattern and press the Next step button.

<div align="center"><a href="kibana5.png"><img src="kibana5.png" width="60%;"></a></div>

In Step 2, leave Time Filter field name as **@timestamp** and press the Create index pattern button.

<div align="center"><a href="kibana6.png"><img src="kibana6.png" width="60%;"></a></div>

From here, check the data.
Click the upper left of the page, and then click Kibana **Discover** from the menu.

<div align="center"><a href="kibana7.png"><img src="kibana7.png" width="60%;"></a></div>

On the Discover screen, the index pattern is displayed on the left, so click the index pattern and switch to the previously configured **fluentbit***.

<div align="center"><a href="kibana8.png"><img src="kibana8.png" width="60%;"></a></div>

You can now check the list of logs. For procedures for using graphs and so on, refer to the Kibana manual and other resources.

<div align="center"><a href="kibana9.png"><img src="kibana9.png" width="50%;"></a></div>


### Operation Check with Python
When checking operation with the Python version of OpenRTM-aist, use the Elasticsearch Logger plugin.
First, install the Python library for Elasticsearch and the ECS formatter. Pay attention to the Elasticsearch version.

```
 pip install elasticsearch==7.8.0
 pip install ecs-logging
```

Prepare an rtc.conf like the following and load **ESLogger.py**.

```
 logger.enable: YES
 logger.log_level: PARANOID
 
 logger.plugins: C:\\Python37\\Lib\\site-packages\\OpenRTM_aist\\ext\\logger\\eslogger\\ESLogger.py
 
 logger.logstream.elasticsearch.output0.host: 127.0.0.1
 logger.logstream.elasticsearch.output0.port: 9200
 logger.logstream.elasticsearch.output0.index: fluentbit
```

Specify the address and port number of the destination Elasticsearch server, and the index where the data will be registered.

Start the RTC by specifying this rtc.conf.

```
 ConsoleOut.py -f rtc.conf
```

