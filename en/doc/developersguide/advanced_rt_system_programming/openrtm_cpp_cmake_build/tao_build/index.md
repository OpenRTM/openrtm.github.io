---
layout: page
title: "building tao"
---
<!-- Title: TAOのビルド -->
#contents

## Windows

&aname(windows);

### Building ACE+TAO

Download **ACE+TAO.zip** from one of the following locations.

- [http://download.dre.vanderbilt.edu](http://download.dre.vanderbilt.edu)
- [https://github.com/DOCGroup/ACE_TAO/releases](https://github.com/DOCGroup/ACE_TAO/releases)

Build ACE and TAO using Visual Studio.

Rename **ace/config-win32.h** to **ace/config.h** in the extracted **ACE+TAO.zip** directory.

Open **ACE_vs2019.sln** (or **ACE_vs2017.sln**) in Visual Studio and build it.
For 64-bit builds, change the solution platform from **Win32** to **x64**.

Next, set the following environment variable, then open **TAO_vs2019.sln** (or **TAO_vs2017.sln**) in Visual Studio and build it.

<table class="table-alt">
  <tr>
    <th>Environment Variable</th>
    <th>Description</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>ACE_ROOT</td>
    <td>Path to the extracted <strong>ACE_wrappers</strong> directory</td>
    <td>C:/work/ACE_wrappers</td>
  </tr>
</table>

```sh
cd TAO
set ACE_ROOT=C:/work/ACE_wrappers
TAO_vs2019.sln
```

## Ubuntu

&aname(ubuntu);

### Building ACE+TAO

Obtain **ACE+TAO.tar.gz** and build it using the following commands.

```sh
export ACE_INSTALL_DIR=~/work/ace_install
sudo apt-get install gperf
export ACE_ROOT=${PWD}/ACE_wrappers/build/linux
export TAO_ROOT=${ACE_ROOT}/TAO
export LD_LIBRARY_PATH=$ACE_ROOT/ace:$ACE_ROOT/lib
export INSTALL_PREFIX=$ACE_INSTALL_DIR
wget https://github.com/DOCGroup/ACE_TAO/releases/download/ACE%2BTAO-7_0_6/ACE+TAO-7.0.6.tar.gz
tar xf ACE+TAO-7.0.6.tar.gz
cd ACE_wrappers
mkdir -p build/linux
./bin/create_ace_build build/linux
echo '#include "ace/config-linux.h"' > build/linux/ace/config.h
echo 'include $(ACE_ROOT)/include/makeinclude/platform_linux.GNU' > build/linux/include/makeinclude/platform_macros.GNU
cd build/linux
make
make install
cd TAO
make
make install
```

To enable **SSLIOP**, you must enable the **ssl** option and build **SSLIOP** as shown below.

```sh
cd build/linux
make ssl=1
make install ssl=1
cd TAO
make SSLIOP ssl=1
make install ssl=1
```

### Setting Environment Variables

&aname(ubuntu_env);

To allow **pkg-config** to detect ACE+TAO, set the **PKG_CONFIG_PATH** environment variable as follows.

```sh
export PKG_CONFIG_PATH=${ACE_INSTALL_DIR}/lib/pkgconfig:$PKG_CONFIG_PATH
```

## Starting the Name Server (SSLIOP)

To start the Name Server with SSLIOP communication enabled, execute the following command.

```sh
${ACE_INSTALL_DIR}bin/tao_cosnaming -ORBSvcConf server.conf -ORBEndpoint iiop://localhost:/ssl_port=2809
```

If the endpoint is specified as **ssliop://localhost:2809**, access using the **corbaloc** format will not work correctly.
Therefore, specify the endpoint as **iiop://localhost:/ssl_port=2809**, as shown above.

For example, prepare **server.conf** as follows.

```conf
dynamic SSLIOP_Factory Service_Object *
        TAO_SSLIOP:_make_TAO_SSLIOP_Protocol_Factory()
        "-SSLAuthenticate SERVER_AND_CLIENT -SSLPrivateKey PEM:server_key.pem -SSLCertificate PEM:server_cert.pem -SSLCAfile PEM:cacert.pem"
static Resource_Factory "-ORBProtocolFactory SSLIOP_Factory"
```

