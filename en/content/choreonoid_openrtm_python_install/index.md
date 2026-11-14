---
layout: page
title: "installation procedure for the openrtm integration plugin for choreonoid, python version"
---

#contents

## Operating Environment
The operating environments are as follows.

- Windows 8.1
- Windows 10
- Ubuntu 14.04
- Ubuntu 16.04

For Windows, prebuilt binaries are distributed.


## Installation Procedure (Windows)

### Python

Install Python 2.7 (**64-bit**).

- [Python 2.7.14](https://www.python.org/downloads/release/python-2714/)

### Choreonoid

The prebuilt Choreonoid + OpenRTM integration plugin can be downloaded from the following.

- [Choreonoid+OpenRTM-Python-Plugin.zip](https://drive.google.com/a/nobu777.net/uc?authuser=0&id=1EA9LEduA1mVAoPbyL4IFQ5k8L61TxQux&export=download)


Installation is complete by extracting this file to an appropriate location using [Lhaplus](https://forest.watch.impress.co.jp/library/software/lhaplus/) or a similar tool.

### When Building from Source Code
If, for some reason, you must build from source code, build it according to the procedure on the following page.

- [Installation Procedure (Windows, Build from Source)](https://github.com/Nobu19800/OpenRTMPythonPlugin/wiki/%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%89%8B%E9%A0%86(Windows))

## Installation Procedure (Ubuntu)

### Download

The Choreonoid installation procedure seems to be described in detail on the [Choreonoid website](http://choreonoid.org/ja/manuals/latest/install/build-ubuntu.html), but it is also explained here just in case.

The Choreonoid source code has been independently modified for the following reasons.


- Changes to add a function that opens a dedicated Python editor when double-clicking an RTC in the RT system editor of the OpenRTM integration plugin
- Some changes because it did not work on Windows as of July 2017
- Addition of functions for operating lights from Python


For this reason, clone the forked version instead of the original Choreonoid.

```
 git clone https://github.com/Nobu19800/choreonoid.git
```

If git is not installed, enter the following command.

```
 sudo apt-get install git
```


### Installation
#### Dependent Libraries
Choreonoid appears to include a script for installing required libraries, so start this script.

```
 cd choreonoid
 sh misc/script/install-requisites-ubuntu-14.04.sh
```

#### OpenRTM-aist

```
 wget http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-aist/build/pkg_install_ubuntu.sh
```
sudo sh pkg_install_ubuntu.sh

#### OpenRTM-aist-Python

Enter the following commands.

```
 wget http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_2/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh
 sudo sh pkg_install_python_ubuntu.sh
```


#### Choreonoid

```
 cd sample
 git clone https://github.com/Nobu19800/OpenRTMPythonPlugin.git
 cd ..
 mkdir build
 cd build
 cmake .. -DENABLE_PYTHON=ON -DBUILD_PYTHON_PLUGIN=ON -DBUILD_OPENRTM_PYTHON_PLUGIN=ON
 make
 sudo make install
```

Build with the cmake command options changed as follows.

```
 cmake .. -DENABLE_PYTHON=ON -DBUILD_PYTHON_PLUGIN=ON -DBUILD_OPENRTM_PYTHON_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_OPENRTM_PLUGIN=ON
```


### Installing Software Required for Operation Check

A gamepad RTC is used for the operation check, and PySDL2 must be installed for this RTC to operate.

It is only required for the RTC used for operation check, so if you do not perform the operation check on the next page, you do not need to install it.

Enter the following commands.

```
 wget https://bitbucket.org/marcusva/py-sdl2/downloads/PySDL2-0.9.5.tar.gz
 tar xf PySDL2-0.9.5.tar.gz
 cd PySDL2-0.9.5
 sudo python setup.py install
```

SDL2 also needs to be installed, so install it with the following command.

```
 sudo apt-get install libsdl2-2.0-0 libsdl2-image-2.0-0
```

This completes the preparation.

### Additional Note
The source code of OpenRTMPythonPlugin must be placed in the sample folder of choreonoid.

```
 cd sample
 git clone https://github.com/Nobu19800/OpenRTMPythonPlugin.git
```
