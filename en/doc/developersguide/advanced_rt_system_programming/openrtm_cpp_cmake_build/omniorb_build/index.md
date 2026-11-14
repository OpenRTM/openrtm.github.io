---
layout: page
title: "building omniorb"
---
<!-- Title: omniORBのビルド -->
#contents

## Windows

### Building omniORB

&aname(windows);

Python and Cygwin must be installed before building.

- [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
- [https://www.cygwin.com/](https://www.cygwin.com/)

If you want to use the **sslTp** and **httpTp** features, OpenSSL must also be built.

- [https://github.com/openssl/openssl/tags](https://github.com/openssl/openssl/tags)

Install Strawberry Perl and execute the following commands.

```sh
set OPENSSL_INSTALL_DIR=C:/work/openssl_install
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
perl Configure VC-WIN64A --prefix=%OPENSSL_INSTALL_DIR% no-asm shared
nmake install
```

Obtain the omniORB source code.

- [https://sourceforge.net/projects/omniorb/files/omniORB/](https://sourceforge.net/projects/omniorb/files/omniORB/)

Set the Python and OpenSSL paths in **mk/platforms/x86_win32_vs_16.mk**.
Even if **OPEN_SSL_ROOT** is not specified, omniORB can still be built, but the **sslTp** and **httpTp** features cannot be used.

```make
PYTHON = /cygdrive/c/Python310/python
```

```make
OPEN_SSL_ROOT = /cygdrive/c/work/openssl_install
```

Specify the build environment in **config/config.mk**.

```make
platform = x86_win32_vs_16
```

Move to the extracted omniORB directory and execute the following commands.

```sh
set PATH=C:\cygwin64\bin;%PATH%;
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
cd src
make export
```

Next, build **omniORBpy**.
First, obtain the omniORBpy source code.

- [https://sourceforge.net/projects/omniorb/files/omniORBpy/](https://sourceforge.net/projects/omniorb/files/omniORBpy/)

Copy **omniORBpy** into the **src/lib** directory of omniORB.

```text
omniORB-4.x.y
   |--src
   |  |--lib
   |    |--omniORBpy
   |--mk
   |  |--platforms
   |    |--x86_win32_vs_16
   |--config
     |--config.mk
```

Move to the **omniORBpy** directory and execute the **make** command.

```sh
cd lib\omniORBpy
make export
```

### Setting Environment Variables

&aname(windows_env);

To verify the operation of **omniORB** and **omniORBpy**, you must configure the **PATH** and **PYTHONPATH** environment variables.

```sh
set omniORB_DIR=C:/workspace/omniORB-4.3.0
set PATH=%omniORB_DIR%\bin\x86_win32;%PATH%
set PYTHONPATH=%omniORB_DIR%\lib\x86_win32;%omniORB_DIR%\lib\python;%PYTHONPATH%
```

## Ubuntu

### Building omniORB

&aname(ubuntu);

If you want to use the **sslTp** and **httpTp** features, OpenSSL must be installed.

```sh
sudo apt install libssl-dev
```

Next, obtain the omniORB source code and build it.

```sh
export PYTHON=/usr/bin/python3
export OMNIORB_INSTALL_DIR=~/work/omniorb_install
wget https://jaist.dl.sourceforge.net/project/omniorb/omniORB/omniORB-4.3.0/omniORB-4.3.0.tar.bz2
tar xf omniORB-4.3.0.tar.bz2
cd omniORB-4.3.0
./configure --prefix=${OMNIORB_INSTALL_DIR} --with-openssl
make
make install
```

Build **omniORBpy**.

```sh
export PYTHON=/usr/bin/python3
wget https://jaist.dl.sourceforge.net/project/omniorb/omniORBpy/omniORBpy-4.3.0/omniORBpy-4.3.0.tar.bz2
tar xf omniORBpy-4.3.0.tar.bz2
cd omniORBpy-4.3.0
./configure --with-omniorb=${OMNIORB_INSTALL_DIR} --prefix=${OMNIORB_INSTALL_DIR} --with-openssl
make
make install
```

### Setting Environment Variables

&aname(ubuntu_env);

To verify the operation of **omniORB** and **omniORBpy**, you must configure the **PATH**, **LD_LIBRARY_PATH**, and **PYTHONPATH** environment variables.

```sh
export PATH=${OMNIORB_INSTALL_DIR}/bin:$PATH
export LD_LIBRARY_PATH=${OMNIORB_INSTALL_DIR}/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=${OMNIORB_INSTALL_DIR}/lib/python3.6/site-packages:$PYTHONPATH
```

To allow **pkg-config** to detect omniORB, set the **PKG_CONFIG_PATH** environment variable as follows.

```sh
export PKG_CONFIG_PATH=${OMNIORB_INSTALL_DIR}/lib/pkgconfig:$PKG_CONFIG_PATH
```
