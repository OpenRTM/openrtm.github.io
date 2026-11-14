---
layout: page
title: "using ssltransport"
---

<!-- Title: Using SSLTransport -->
#contents

## Overview

Some security features defined in the [CORBA Security Service](https://www.omg.org/spec/SEC/About-SEC/) specification are available for use.

The CORBA Security Service defines security policy models, authentication, access control, message protection, delegation, auditing, and non-repudiation. omniORB supports SSLIOP communication, which protects GIOP messages through SSL/TLS server/client authentication and encryption.

This page describes how to use omniORB's SSLIOP communication with OpenRTM-aist.

## C++

### Windows

#### Building and Installing OpenRTM-aist

First, extract the OpenSSL header files and libraries to an appropriate location.

- https://openrtm.org/pub/OpenSSL/

Build and install OpenRTM-aist + omniORB according to the following procedure.

- [Building OpenRTM-aist (C++ Version) with CMake]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build#windowsomniorb)

When running CMake, however, you must specify the **SSL_ENABLE** and **OPENSSL_ROOT_DIR** options.

<table class="table-alt">
  <tr>
    <th>Setting</th>
    <th>Description</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>SSL_ENABLE</td>
    <td>Whether to build the SSLTransport plugin</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>OPENSSL_ROOT_DIR</td>
    <td>Path where the OpenSSL files are located</td>
    <td>C:/work/OpenSSL/x64</td>
  </tr>
</table>

Also, specify the OpenRTM-aist installation directory when running CMake so that it is installed there.

```sh
set OPENRTM_INSTALL_DIR=C:/work/openrtm_install
set OMNIORB_SOURCE_DIR=C:/workspace/omniORB-4.2.5-x64-vc14-py310
set OPENSSL_ROOT_DIR=C:/work/OpenSSL/x64
cmake .. -DORB_ROOT=%OMNIORB_SOURCE_DIR% -DSSL_ENABLE=ON -DOPENSSL_ROOT_DIR=%OPENSSL_ROOT_DIR% -DCMAKE_INSTALL_PREFIX=%OPENRTM_INSTALL_DIR%
cmake --build . --config Release
cmake --build . --config Release --target install
```

### Ubuntu

#### Building and Installing OpenRTM-aist

Install the OpenSSL headers and libraries.

```sh
sudo apt install libssl-dev
```

Build and install OpenRTM-aist + omniORB according to the following procedure.

- [Building OpenRTM-aist (C++ Version) with CMake]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build#ubuntuomniorb)

However, you must specify the **SSL_ENABLE** option.

<table class="table-alt">
  <tr>
    <th>Setting</th>
    <th>Description</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>SSL_ENABLE</td>
    <td>Whether to build the SSLTransport plugin</td>
    <td>ON</td>
  </tr>
</table>

```sh
set OPENRTM_INSTALL_DIR=~/work/openrtm_install
cmake .. -DSSL_ENABLE=ON -DCMAKE_INSTALL_PREFIX=$OPENRTM_INSTALL_DIR
cmake --build . --config Release -- -j$(nproc)
cmake --build . --config Release --target install
```

## Python

### Building and Installing OpenRTM-aist

Install the Python version of OpenRTM-aist according to the following procedure.

- [Building and Verifying OpenRTM-aist]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/install_qnx_1_1/qnx_build_proc_1_2/openrtm_cpp_cmake_run#pythoninstall)

For the operation check, the Name Server included with the C++ version of OpenRTM-aist is used, so be sure to build the C++ version as well.

## Operation Check

### Starting the Name Server

To verify SSLTransport, the Name Server must support SSLIOP communication.

Start **openrtmNames**, which is included with OpenRTM-aist.

Run the following command. Adjust the path as necessary.

```sh
%OPENRTM_INSTALL_DIR%\2.0.0\bin\vc16\openrtmNames.exe -f %OPENRTM_INSTALL_DIR%\2.0.0\ext\rtc.names.ssl.conf
```

```sh
$OPENRTM_INSTALL_DIR/bin/openrtmNames -f $OPENRTM_INSTALL_DIR/etc/rtc.names.ssl.conf
```

Since **rtc.names.ssl.conf** uses the generated root certificate (**root.crt**) and the file **server.pem**, which contains the private key and server certificate, the RTCs used for the operation check also use these certificate files.

When developing an actual system, replace these certificates and private keys with your own.

### Starting the RTC

Create an rtc.conf file as shown below. Modify the OpenRTM-aist installation path as appropriate.

For C++, create the following file.

```text
manager.modules.load_path: C:/work/openrtm_install/2.0.0/ext/ssl
manager.preload.modules: SSLTransport.dll

corba.ssl.certificate_authority_file:C:/work/openrtm_install/2.0.0/ext/ssl/root.crt
corba.ssl.key_file:C:/work/openrtm_install/2.0.0/ext/ssl/server.pem
corba.ssl.key_file_password:password
corba.args:-ORBserverTransportRule "* ssl" -ORBclientTransportRule "* ssl" -ORBendPoint giop:ssl::
corba.nameservers: corbaloc:ssliop:localhost:2809
corba.master_manager: giop:ssl:localhost:2810
```

For Python, create the following file.

```text
manager.modules.load_path: C:/Python37/Lib/site-packages/OpenRTM_aist/ext/vc16/ssl
manager.preload.modules: SSLTransport.py

corba.ssl.certificate_authority_file:C:/Python37/Lib/site-packages/OpenRTM_aist/ext/ssl/root.crt
corba.ssl.key_file:C:/Python37/Lib/site-packages/OpenRTM_aist/ext/ssl/server.pem
corba.ssl.key_file_password:password
corba.args:-ORBserverTransportRule "* ssl" -ORBclientTransportRule "* ssl" -ORBendPoint giop:ssl::
corba.nameservers: corbaloc:ssliop:localhost:2809
corba.master_manager: giop:ssl:localhost:2810
```

The contents of each configuration item are as follows.

<table class="table-alt">
  <tr>
    <th>Item Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>corba.ssl.certificate_authority_file</td>
    <td>Root certificate</td>
  </tr>
  <tr>
    <td>corba.ssl.key_file</td>
    <td>Combined file containing the private key, server certificate, and client certificate</td>
  </tr>
  <tr>
    <td>corba.ssl.key_file_password</td>
    <td>Passphrase for the private key</td>
  </tr>
  <tr>
    <td>corba.args</td>
    <td>Arguments passed to the CORBA library initialization function. The endpoint for SSLIOP communication must be specified here.</td>
  </tr>
  <tr>
    <td>corba.nameservers</td>
    <td>Address of the Name Server. Configure this to connect to the Name Server using SSLIOP communication.</td>
  </tr>
  <tr>
    <td>corba.master_manager</td>
    <td>Endpoint of the Master Manager. For a Master Manager, specify its own endpoint. For a Slave Manager, specify the address of the Master Manager to connect to.</td>
  </tr>
</table>

Start the ConsoleIn and ConsoleOut RTCs using this rtc.conf.

```sh
%OPENRTM_INSTALL_DIR%\2.0.0\Components\C++\Examples\vc16\ConsoleInComp.exe -f rtc.conf
```

```sh
%OPENRTM_INSTALL_DIR%\2.0.0\Components\C++\Examples\vc16\ConsoleOutComp.exe -f rtc.conf
```

```sh
${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f rtc.conf
```

```sh
${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleInComp -f rtc.conf
```

```sh
python %OpenRTMPython_INSTALL_DIR%\Lib\site-packages\ConsoleIn.py -f rtc.conf
```

```sh
python %OpenRTMPython_INSTALL_DIR%\Lib\site-packages\ConsoleOut.py -f rtc.conf
```

```sh
python3 ${OpenRTMPython_INSTALL_DIR}/share/openrtm-2.0/components/python3/SimpleIO/ConsoleOut.py -f rtc.conf
```

```sh
python3 ${OpenRTMPython_INSTALL_DIR}/share/openrtm-2.0/components/python3/SimpleIO/ConsoleIn.py -f rtc.conf
```

The RTCs will now be registered with the Name Server. However, since RT System Editor does not support SSLIOP communication, you must use OpenRTM-aist functionality or rtshell to connect ports and activate RTCs.

## Connecting Ports and Activating RTCs at Manager Startup

By specifying rtcname or rtcloc format in [manager.components.preconnect]({{ site.baseurl }}/en/doc/developersguide/basic_rtc_programming/rtc_conf_reference#preconnect) and [manager.components.preactivation]({{ site.baseurl }}/en/doc/developersguide/basic_rtc_programming/rtc_conf_reference), you can connect ports and activate RTCs.

For SSLIOP communication, specify **ssliop** as the protocol as shown below.

```text
manager.components.preconnect: ConsoleIn0.out?port=rtcname.ssliop://localhost:2809/*/ConsoleOut0.in
manager.components.preactivation: ConsoleIn0, rtcname.ssliop://localhost:2809/*/ConsoleOut0
```

```text
naming.type: corba, manager
manager.components.preconnect: ConsoleIn0.out?port=rtcloc.ssliop://localhost:2810/*/ConsoleOut0.in
manager.components.preactivation: ConsoleIn0, rtcloc.ssliop://localhost:2810/*/ConsoleOut0
```

## Using rtshell

&aname(rtshell);

First, the currently distributed version of rtshell does not support this feature, so you need the latest versions of rtctree, rtshell, and rtsprofile.

- https://github.com/OpenRTM/rtctree
- https://github.com/OpenRTM/rtshell
- https://github.com/OpenRTM/rtsprofile

To use SSLIOP communication with rtshell, set the following environment variables.

<table class="table-alt">
  <tr>
    <th>Environment Variable</th>
    <th>Example Setting</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>RTCTREE_SSL_ENABLE</td>
    <td>YES</td>
    <td>YES: Enables SSLIOP communication in rtctree.</td>
  </tr>
  <tr>
    <td>RTCTREE_NAMESERVERS</td>
    <td>ssliop:localhost:2809</td>
    <td>Name Server to connect to</td>
  </tr>
  <tr>
    <td>ORBsslCAFile</td>
    <td>root.crt</td>
    <td>Root certificate</td>
  </tr>
  <tr>
    <td>ORBsslKeyFile</td>
    <td>server.pem</td>
    <td>Combined file containing the private key, server certificate, and client certificate</td>
  </tr>
  <tr>
    <td>ORBsslKeyPassword</td>
    <td>password</td>
    <td>Passphrase for the private key</td>
  </tr>
  <tr>
    <td>ORBserverTransportRule</td>
    <td>"* ssl"</td>
    <td>Communication protocol selection rule for the server side</td>
  </tr>
  <tr>
    <td>ORBclientTransportRule</td>
    <td>"* ssl"</td>
    <td>Communication protocol selection rule for the client side</td>
  </tr>
  <tr>
    <td>ORBendPoint</td>
    <td>giop:ssl::</td>
    <td>omniORB endpoint</td>
  </tr>
</table>

```sh
set RTCTREE_SSL_ENABLE=YES
set ORBsslCAFile=%RTM_ROOT%/ext/ssl/root.crt
set ORBsslKeyFile=%RTM_ROOT%/ext/ssl/server.pem
set ORBsslKeyPassword=password
set RTCTREE_NAMESERVERS=ssliop:localhost:2809
set ORBserverTransportRule=* ssl
set ORBclientTransportRule=* ssl
set ORBendPoint=giop:ssl::
```

By prefixing the Name Server address with **ssliop:** as shown below, you can connect to the Name Server using SSLIOP communication.

```sh
rtcon /ssliop:localhost:2809/test.host_cxt/ConsoleIn0.rtc:out /ssliop:localhost:2809/test.host_cxt/ConsoleOut0.rtc:in
rtact /ssliop:localhost:2809/test.host_cxt/ConsoleIn0.rtc /ssliop:localhost:2809/test.host_cxt/ConsoleOut0.rtc
rtdeact /ssliop:localhost:2809/test.host_cxt/ConsoleIn0.rtc /ssliop:localhost:2809/test.host_cxt/ConsoleOut0.rtc
rtexit /ssliop:localhost:2809/test.host_cxt/ConsoleOut0.rtc
rtcryo ssliop:localhost:2809 -o sys.rtsys
```

## Generating Private Keys and Certificates

First, you need to generate private keys and certificates.

There are four types of certificates: root certificates, intermediate certificates, server certificates, and client certificates.

The following figure provides an overview of server authentication using a server certificate.

<div align="center"><a href="ssl1.png"><img src="ssl1.png" width="80%;"></a></div>

In addition to the communicating server and client PCs, a Certificate Authority (CA) is required.

The Certificate Authority possesses the root certificate and its corresponding private key (Private Key 1).

After generating its private key, the server sends a Certificate Signing Request (CSR), which contains the public key information and website owner information, to the Certificate Authority using the generated private key (Private Key A).

The Certificate Authority issues a server certificate by signing the CSR with Private Key 1.

During the SSL/TLS handshake between the server and client, the server certificate is transmitted. Other processes, such as key exchange algorithms, are also performed at this stage, but they are omitted from this explanation.

The client verifies the signature of the server certificate using the public key in the root certificate obtained in advance. Once the certificate has been successfully verified, encrypted communication begins (encrypted with Private Key A and decrypted using the public key in the server certificate).

In some cases, an intermediate Certificate Authority obtains an intermediate certificate from the root Certificate Authority, and the intermediate Certificate Authority issues the server certificate.

The diagrams on the following page provide an easy-to-understand explanation and are recommended for reference.

- [Building a Private Certificate Authority with OpenSSL (Root CA, Intermediate CA)](https://qiita.com/bashaway/items/ac5ece9618a613f37ce5)

So far, the explanation has assumed that the client authenticates the server. However, there are cases where the server authenticates the client.

In omniORB, you can change the authentication method by specifying the following parameters with the `-ORBsslVerifyMode` argument or the `ORBsslVerifyMode` environment variable.

<table class="table-alt">
  <tr>
    <th>Parameter</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>none</td>
    <td>Continue the handshake even if server certificate verification fails. Client certificates are not requested.</td>
  </tr>
  <tr>
    <td>peer (default)</td>
    <td>The server requests a client certificate. The handshake is terminated if either server authentication or client authentication (when a client certificate is provided) fails.</td>
  </tr>
  <tr>
    <td>peer, fail</td>
    <td>Terminate the handshake if no client certificate is provided.</td>
  </tr>
  <tr>
    <td>peer, once</td>
    <td>Perform client authentication only during the initial handshake.</td>
  </tr>
  <tr>
    <td>peer, fail, once</td>
    <td>A combination of the above options.</td>
  </tr>
</table>

Since omniORB cannot specify separate root certificate files for server certificates and client certificates, specify both using the `corba.ssl.certificate_authority_file` option.

In summary, for SSL/TLS communication with OpenRTM-aist, the root certificate, server certificate, client certificate, intermediate certificate, and private key should be arranged as shown below.

<div align="center"><a href="ssl2.png"><img src="ssl2.png" width="80%;"></a></div>

The following example demonstrates how to create a self-signed Certificate Authority and self-signed certificates (commonly called "self-signed certificates") using OpenSSL commands.

The cnf file used here is the one provided on the website linked above.

First, create the **root**, **inter**, and **server** directories in a suitable working folder.

Create the private key and root certificate for the Root Certificate Authority.

```sh
mkdir root
cd root
mkdir newcerts
type nul > index.txt
echo 01 > serial
echo 00 > crlnumberl
openssl genrsa -out RootCA_key.pem -passout pass:rootpass 2048
openssl req -new -subj "/C=JP/ST=Tokyo/O=EXAMPLE/CN=EXAMPLE Root CA" -out RootCA_csr.pem -key RootCA_key.pem -passin pass:rootpass -config ../conf/openssl_sign.cnf
openssl ca -batch -extensions v3_ca -out RootCA_crt.pem -in RootCA_csr.pem -selfsign -keyfile RootCA_key.pem -passin pass:rootpass -config ../conf/openssl_sign.cnf
openssl x509 -in RootCA_crt.pem -out RootCA_crt.pem
cd ..
```

Next, create the private key for the Intermediate Certificate Authority and the CSR for the intermediate certificate.

```sh
mkdir inter
cd inter
mkdir newcerts
type nul > index.txt
echo 01 > serial
echo 00 > crlnumberl
openssl genrsa -out InterCA_key.pem -passout pass:interpass 2048
openssl req -new -subj "/C=JP/ST=Tokyo/O=EXAMPLE/CN=EXAMPLE Intermediate CA" -out InterCA_csr.pem -key InterCA_key.pem -passin pass:interpass -config ../conf/openssl_sign.cnf
cd ..
```

Issue the intermediate certificate using the Root Certificate Authority.

```sh
cd root
openssl ca -batch -extensions v3_ca -out ..\inter\InterCA_crt.pem -in ..\inter\InterCA_csr.pem -cert RootCA_crt.pem -keyfile RootCA_key.pem -passin pass:interpass -config ../conf/openssl_sign.cnf
cd ..
```

Next, create the server's private key and the CSR for the server certificate.

```sh
mkdir server
cd server
mkdir newcerts
type nul > index.txt
echo 01 > serial
echo 00 > crlnumberl
openssl genrsa -out Server_key.pem -passout pass:serverpass 2048
openssl req -new -subj "/C=JP/ST=Tokyo/O=EXAMPLE/CN=EXAMPLE Server" -out Server_csr.pem -key Server_key.pem -passin pass:serverpass -config ../conf/openssl_sign.cnf
cd ..
```

Issue the server certificate using the Intermediate Certificate Authority.

```sh
cd inter
openssl x509 -req -in ..\server\Server_csr.pem -sha256 -CA InterCA_crt.pem -CAkey InterCA_key.pem -set_serial 01 -days 730 -out ..\server\Server_crt.pem -passin pass:serverpass
cd ..
```

Concatenate the private key, server certificate, and intermediate certificate.

```sh
cd server
openssl x509 -in Server_crt.pem -out Server_crt.pem
openssl x509 -in ..\inter\InterCA_crt.pem -out InterCA_crt.pem
copy /b Server_key.pem + Server_crt.pem + InterCA_crt.pem server.pem
```

The files used in this example are the concatenated file (**server.pem**) and the root certificate (**RootCA_crt.pem**).

## Simple Operation Check

When OpenRTM-aist is built and installed, a configuration file for a simple operation check of SSLTransport is also installed.

### Windows

First, start the Name Server.

```sh
%RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
%RTM_ROOT%\bin\vc16\openrtmNames.exe -f %RTM_ROOT%\ext\rtc.names.ssl.conf
```

Next, start the RTC.

```sh
%RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
%RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\ssl\rtc.ssl.conf
```

### Ubuntu

First, configure the environment and start the Name Server.

```sh
source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
${OPENRTM_INSTALL_DIR}/bin/openrtmNames -f ${OPENRTM_INSTALL_DIR}/etc/rtc.names.ssl.conf
```

Next, start the RTC.

```sh
source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/ssl/rtc.ssl.conf
```

