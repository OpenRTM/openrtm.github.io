---
layout: page
title: "tao-related settings"
---

<!-- Title: TAO-Related Settings -->
#contents

This page describes how to create configuration files for using various communication protocols when TAO is used as the communication middleware in OpenRTM-aist.

TAO supports IIOP, DIOP, UIOP, HTIOP, SHMIOP, SSLIOP, SCIOP, MIOP, COIOP, and ZIOP communication.

However, protocols other than IIOP, SSLIOP, and ZIOP are proprietary protocols, so they are not compatible with other CORBA implementations.

## DIOP

DIOP (Datagram Inter-ORB Protocol) is an implementation of GIOP over UDP/IP. Compared with IIOP (TCP/IP), it is lightweight, but it is a communication protocol that does not guarantee delivery.

A major difference from IIOP communication is that CORBA service calls are one-way and cannot return values.

For example, when obtaining an RTC component profile from an external tool, DIOP communication cannot be used because the return value (component profile) cannot be obtained.

To use DIOP communication with OpenRTM-aist, the following method with the oneway attribute is defined for data port data transfer.

```
 module OpenRTM
 {
   interface InPortCdrUDP
   {
     oneway void put(in CdrData data);
   };
 };
```

When actually using it, as shown in the following figure, DIOP communication must be used for data transmission through data ports, while other connections must use another communication protocol such as IIOP.

<br>

<div align="center"><a href="diop.png"><img src="diop.png" width="70%;"></a></div>

<br>

The following shows an example configuration for rtc.conf.

Set the endpoints for IIOP and DIOP.

corba.args: -ORBEndpoint iiop://: -ORBEndpoint diop://: -ORBSvcConf svc.conf


svc.conf is a TAO configuration file.

If a file named svc.conf exists in the execution path, it is loaded automatically, but it can also be specified explicitly with the ORBSvcConf option.

In svc.conf, configure ORBProtocolFactory as follows.

```
 static Advanced_Resource_Factory "-ORBProtocolFactory DIOP_Factory -ORBProtocolFactory IIOP_Factory -ORBReactorType select_st"
```

You can also use rtc.diop.conf and svc.conf installed with OpenRTM-aist.

```
 %RTM_ROOT%Components\C++\Examples\%RTM_VC_VERSION%\ConsoleInComp.exe -f ext\tao_diop\rtc.diop.conf
 %RTM_ROOT%Components\C++\Examples\%RTM_VC_VERSION%\ConsoleOutComp.exe -f ext\tao_diop\rtc.diop.conf
```

When connecting ports, specify **corba_cdr_udp** for Interface Type to transfer data using DIOP communication.

In RT System Editor, set this in Connector Profile.

<br>

<div align="center"><a href="diop2.png"><img src="diop2.png" width="40%;"></a></div>

<br>

In rtc.conf, set **interface_type** to **corba_cdr_udp** to configure preconnection.

```
 manager.components.preconnect: ConsoleIn0.out?port=rtcname://localhost:2809/*/ConsoleOut0.in&interface_type=corba_cdr_udp
```

## HTIOP

HTIOP (HTTP Tunneling Inter-ORB Protocol) is a communication protocol that sends GIOP messages as HTTP packets.

The advantages of HTIOP communication include easier communication through firewalls and HTTP proxy servers, and easier reuse of existing mechanisms such as reverse proxies and load balancers.

First, start the Name Server, but the HTIOP endpoint must also be configured for the Name Server.

Create the configuration file **svc.names.htiop.conf** with the following contents.

```
 dynamic HTIOP_Factory Service_Object *
        TAO_HTIOP:_make_TAO_HTIOP_Protocol_Factory ()
        "-config ./HT_Config.conf"
 
 static Resource_Factory "-ORBProtocolFactory HTIOP_Factory"
```

Start **tao_cosnaming**, the Name Server included with TAO.

If OpenRTM-aist was built on Windows, it is copied to **${RTM_ROOT}/ACE/${RTM_VC_VERSION}/bin/tao_cosnaming.exe**. On Ubuntu, use the one located in ${OPENRTM_INSTALL_DIR}/bin when TAO is installed.

Start tao_cosnaming by specifying the created svc.names.htiop.conf as follows.

```
 ACE\vc16\bin\tao_cosnaming.exe -ORBEndpoint htiop://127.0.0.1:2809 -ORBSvcConf ext/svc.names.htiop.conf
```

Start the CosoleIn and ConsoleOut components with rtc.conf containing the following contents.

```
 corba.args: -ORBEndpoint htiop:// -ORBSvcConf ext/tao_htiop/svc.htiop.conf
 
 corba.nameservers: corbaloc:htiop:localhost:2809
 corba.master_manager: htiop://127.0.0.1:2810
 
 manager.components.preactivation: ConsoleIn0, rtcname.htiop://localhost:2809/*/ConsoleOut0
 manager.components.preconnect: ConsoleIn0.out?port=rtcname.htiop://localhost:2809/*/ConsoleOut0.in
```

The **corba.args** option specifies arguments to TAO's ORB_init function.

It configures the HTIOP endpoint and the TAO configuration file (ext/svc.htiop.conf).


Create the configuration file **svc.htiop.conf** with the following contents.

```
 dynamic HTIOP_Factory Service_Object *
        TAO_HTIOP:_make_TAO_HTIOP_Protocol_Factory ()
        "-config ext/tao_htiop/HT_Config.conf"
 
 static Advanced_Resource_Factory "-ORBProtocolFactory HTIOP_Factory"
```

Also configure the Name Server to connect to.

Specify the HTIOP endpoint (**htiop:localhost:2809**) for the Name Server.

When using HTIOP communication, RTCs cannot be operated from RT System Editor or rtshell.

Currently, you must either create your own application or configure preconnection (**preconnect**) and preactivation (**preactivation**) when starting the manager.

You can configure the proxy server in **HT_Config.conf**.

```
 [htbp]
 
 proxy_port=3128
 proxy_host=localhost
```

The following shows an example of HTTP packets used in HTIOP communication.

After executing the GET method, the POST method is executed. The GIOP message is stored in the body of the POST request and sent.

```
 GET http://127.0.0.1:2809//1/request1647425846.html HTTP/1.1
```

```
 POST http://127.0.0.1:2809//1/request1647418153.html HTTP/1.1
 Content-Type: application/octet-stream
 Content-Length: 123
 
 
 GIOP\x01\x00\x01\x00o\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x0c\x00\x00\x00\x01\xc0N\r\x01\x00\x01\x00\t\x01\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x0b\x00\x00\x00NameService\x00\x06\x00\x00\x00_is_a\x00\x00\x00\x00\x00\x00\x00+\x00\x00\x00IDL:omg.org/CosNaming/NamingContextExt:1.0\x00
```

## SSLIOP

SSLIOP (Secure Sockets Layer (SSL) Inter-ORB Protocol) is a communication protocol that applies SSL/TLS server/client authentication and encrypted communication to GIOP, enabling secure communication.

First, when building OpenRTM-aist, enable the **SSL_ENABLE** option when running CMake.

```
 cmake .. -DSSL_ENABLE=ON
```

After building and installing OpenRTM-aist, start the Name Server.

Since the Name Server requires an SSLIOP endpoint, create the configuration file **svc.names.ssliop.conf** with the following contents.

```
 dynamic SSLIOP_Factory Service_Object *
        TAO_SSLIOP:_make_TAO_SSLIOP_Protocol_Factory()
        "-SSLAuthenticate SERVER_AND_CLIENT -SSLPrivateKey PEM:./etc/ssl/server.pem -SSLCertificate PEM:./etc/ssl/root.crt -SSLPassword passward -SSLCAfile PEM:./etc/ssl/root.crt"
 static Resource_Factory "-ORBProtocolFactory SSLIOP_Factory"
```

The **SSLPrivateKey** option specifies the private key, **SSLCertificate** specifies the server certificate, and **SSLCAfile** specifies the root certificate.

Start **tao_cosnaming**, the Name Server included with TAO.

Start tao_cosnaming by specifying the created **svc.names.ssliop.conf** as follows.

```
 tao_cosnaming -ORBEndpoint iiop://localhost:/ssl_port=2809 -ORBSvcConf etc/svc.names.ssliop.conf
```

Start the CosoleIn and ConsoleOut components using an rtc.conf file with the following contents.

```
 corba.args: -ORBEndpoint htiop:// -ORBSvcConf ./etc/tao_htiop/svc.ssliop.conf
 
 corba.nameservers: corbaloc:ssliop:127.0.0.1:2809
 corba.master_manager: ssliop://127.0.0.1:2810
 
 manager.components.preactivation: ConsoleIn0, rtcname.ssliop://localhost:2809/*/ConsoleOut0
 manager.components.preconnect: ConsoleIn0.out?port=rtcname.ssliop://localhost:2809/*/ConsoleOut0.in
```

The **corba.args** option specifies the arguments passed to TAO's ORB_init function.

It configures the SSLIOP endpoint and the TAO configuration file (ext/svc.ssliop.conf).

Create **svc.ssliop.conf** with the following contents.

```
 dynamic SSLIOP_Factory Service_Object *
        TAO_SSLIOP:_make_TAO_SSLIOP_Protocol_Factory()
        "-SSLAuthenticate SERVER_AND_CLIENT -SSLPrivateKey PEM:./etc/ssl/server.pem -SSLCertificate PEM:./etc/ssl/root.crt -SSLPassword passward -SSLCAfile PEM:./etc/ssl/root.crt"
 static Advanced_Resource_Factory "-ORBProtocolFactory SSLIOP_Factory"
```

Also configure the Name Server to connect to.

Specify the SSLIOP endpoint (**ssliop:127.0.0.1:2809**) for the Name Server.

Since SSLIOP communication conforms to the OMG CORBA Security Service specification, it can communicate with other CORBA implementations such as omniORB and OiL.

Therefore, rtshell can be used to connect ports and activate RTCs. For information on using SSLIOP communication with rtshell, refer to the following page.

- [Using SSLTransport]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/ssltransport_use#rtshell)

As shown in rtc.conf, you can also configure preconnection (**preconnect**) and preactivation (**preactivation**) when the manager starts.


## SHMIOP

SHMIOP (Shared Memory Inter-ORB Protocol) is a communication protocol for exchanging GIOP messages through shared memory.

Since data is transferred by reading from and writing to shared memory, improved performance can be expected compared with transfer over TCP/IP communication.

However, although the data transfer uses shared memory, TCP/IP communication is used to notify data writes.

```
 corba.args: -ORBListenEndpoints shmiop:// -ORBSvcConf /home/nobu/testlib/etc/tao_shmiop/svc.shmiop.conf -ORBDebugLevel 5
 
 
 corba.nameservers: corbaloc:shmiop:1.0@2809
 corba.master_manager: shmiop://1.0@hostname:2810
```

```
 static Advanced_Resource_Factory "-ORBProtocolFactory SHMIOP_Factory -ORBProtocolFactory IIOP_Factory -ORBReactorType select_st"
```

## Simple Operation Check

When OpenRTM-aist is built and installed, configuration files for a simple operation check of the above communication protocols are installed.

### DIOP

```
 %RTM_ROOT%\ext\environment-setup.tao.vc16.bat
 %RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\tao_diop\rtc.diop.conf
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/tao_diop/rtc.diop.conf
```

### HTIOP

```
 %RTM_ROOT%\ext\environment-setup.tao.vc16.bat
 %RTM_ROOT%\ACE\vc16\bin\tao_cosnaming.exe  -ORBEndpoint htiop://127.0.0.1:2809 -ORBSvcConf %RTM_ROOT%\ext\svc.names.htiop.conf
```

```
 %RTM_ROOT%\ext\environment-setup.tao.vc16.bat
 %RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\tao_htiop\rtc.htiop.conf
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/bin/openrtmNames -ORBEndpoint htiop://127.0.0.1:2809 -ORBSvcConf  ${OPENRTM_INSTALL_DIR}/etc/svc.names.htiop.conf
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/tao_htiop/rtc.htiop.conf
```
### SSLIOP

```
 %RTM_ROOT%\ext\environment-setup.tao.vc16.bat
 %RTM_ROOT%\ACE\vc16\bin\tao_cosnaming.exe -ORBEndpoint iiop://localhost:/ssl_port=2809 -ORBSvcConf %RTM_ROOT%\ext\svc.names.ssliop.conf
```

```
 %RTM_ROOT%\ext\environment-setup.tao.vc16.bat
 %RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\tao_ssliop\rtc.ssliop.conf
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/bin/openrtmNames -ORBEndpoint iiop://localhost:/ssl_port=2809 -ORBSvcConf  ${OPENRTM_INSTALL_DIR}/etc/svc.names.ssliop.conf
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/tao_ssliop/rtc.ssliop.conf
```
