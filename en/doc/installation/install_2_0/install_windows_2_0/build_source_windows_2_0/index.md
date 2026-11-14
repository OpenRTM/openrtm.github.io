---
layout: page
title: building from source (c++ version)
---

<!-- Title: Building from Source (C++ Version) -->


If you want to modify the OpenRTM-aist core and use it on Windows, you can obtain the OpenRTM-aist source code and build it yourself. Since OpenRTM-aist 2.0, CMake is supported, so the procedure differs from that used for versions up to 1.2.

#contents


<!-- ------------------------------------------------------------ -->

## Required Software and Libraries

The following software is required. For details, see [Installing OpenRTM-aist 2.0 on Windows]({{ site.baseurl }}/en/doc/installation/install_2_0/install_windows_2_0/install_2_0).

- Visual Studio
- Python
- CMake
- Doxygen & Graphviz (if you also want to build documentation)

The omniORB library is also required.

- omniORB 4.2.5 (as of June 2022)

Prebuilt binary packages provided by openrtm.org are available at the link below under names such as omniORB-4.2.5-x64-vc14-pyXX.zip.

Replace XX with the version of Python you have installed, download the appropriate package, and extract it to a suitable location (C:\workspace\omniORB is used in the examples below).

- [Binary Packages Provided by openrtm.org](https://openrtm.org/pub/omniORB/win32/omniORB-4.2.5/)

For information on building with other libraries, see [RT System Development (Advanced) - Building OpenRTM-aist (C++ Version) with CMake]({{ site.baseurl }}/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build).

## Build and Installation Commands

Obtain the source code. For the latest OpenRTM-aist 2.0 source, use the master branch. For the OpenRTM-aist 2.0.0 release source, check out the v2.0.0 tag.

```bash
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist
 git checkout -b v200-src refs/tags/v2.0.0
```

Run CMake with the following options:

- `-DORB_ROOT` : Path to the downloaded and extracted omniORB
- `-G` : Visual Studio version (e.g., "Visual Studio 17 2022", "Visual Studio 16 2019")
- `-DCMAKE_INSTALL_PREFIX` : Installation destination path

```bash
 mkdir build
 cd build
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.5-x64-vc14-py310 -G "Visual Studio 17 2022" -DCMAKE_INSTALL_PREFIX=C:/workspace/openrtminstall ..
```

Next, execute the following command. If the message below is displayed at the end, the build was successful.

```bash
 cmake --build . --verbose --config Release

 Build succeeded.
     0 Warning(s)
     0 Error(s)
```

After a successful build, complete the installation with the following command:

```bash
 cmake --build . --config Release --target install
```

## Batch Processing Using a Script

The following script (`cxx_src_build.bat`) performs the entire process from downloading omniORB to building and installing OpenRTM-aist from source. Place it under the cloned OpenRTM-aist directory and execute it.

```bash
 cd OpenRTM-aist
 cxx_src_build.bat > 1.log
```

Before running the script, modify the following three settings to match your environment:

```bat
 set CMAKE_GENERATOR="Visual Studio 16 2019"
 set PY_VERSION=39    ... Specify one of 37, 38, 39, or 310
 set INSTALL_PREFIX=C:\localRTM-test
```

### cxx_src_build.bat

```bat
 @echo off
 @rem
 @rem ---------- Environment-specific settings (begin) -------
 set CMAKE_GENERATOR="Visual Studio 16 2019"
 set PY_VERSION=39
 set INSTALL_PREFIX=C:\localRTM-test
 @rem ---------- Environment-specific settings (end) -------
 set OMNI_VERSION=4.2.5
 set VC_VERSION=vc14
 if exist %INSTALL_PREFIX% rmdir /s/q %INSTALL_PREFIX%
 @rem
 @rem Convert "\" in paths to "/"
 set current_dir=%~dp0
 set RTM_ROOT=%current_dir:\=/%
 set INSTALL_PREFIX=%INSTALL_PREFIX:\=/%
 @rem
 @rem omniORB download
 set base_omni_url="https://openrtm.org/pub/omniORB/win32/omniORB-%OMNI_VERSION%/"
 set OMNIORB_DIR=omniORB-%OMNI_VERSION%-x64-%VC_VERSION%-py%PY_VERSION%
 set OMNIORB_ZIP=%OMNIORB_DIR%.zip
 set OMNIORB_URL=%base_omni_url%/%OMNIORB_ZIP%
 if not exist %OMNIORB_ZIP% (
   powershell wget -O %OMNIORB_ZIP% %OMNIORB_URL%
 )
 if exist %OMNIORB_DIR% rmdir /s/q %OMNIORB_DIR%
 powershell Expand-Archive .\%OMNIORB_ZIP% -DestinationPath .\\

 set OMNIORB_ROOT=%RTM_ROOT%/%OMNIORB_DIR%
 @rem
 @rem set cmake parameter
 set CMAKE_OPT=-DORB_ROOT=%OMNIORB_ROOT% ^
```

```bat
   -DCMAKE_INSTALL_PREFIX=%INSTALL_PREFIX% ^
   -G %CMAKE_GENERATOR% ^
   -A x64 ..
```

```bat
 call :CMAKE_Release
 exit /b
 @rem
```

```bat
 :CMAKE_Release
```

```bat
 if exist build-release rmdir /s/q build-release
 mkdir build-release
 cd build-release
 cmake %CMAKE_OPT%
 cmake --build . --verbose --config Release
 cmake --install .
 cd ..
 exit /b
```

## Reference: Build Script for MSI Generation

The following build script is used to create MSM files (for VC2019 and VC2022) to be included in MSI installers.

The following libraries are used:

- Boost Library 1.78.0
- OpenSSL 3.0.1
- Fluent Bit v1.8.9 (built from source)

OpenRTM-aist is built in both Release and Debug configurations. Although omniORB binaries built with VC14 work correctly, VC16-specific binaries are prepared and used.

```bat
 @echo off
 @rem
 set CMAKE_GENERATOR="Visual Studio 16 2019"
 set VC_VERSION=vc16
 set SSL_VC_VERSION=vc14
 set PY_VERSION=39
 set INSTALL_PREFIX=C:\localRTM
 set OMNI_VERSION=4.2.5
 set SSL_VERSION=3.0.1
 set BOOST_PATH=C:\local\boost_1_78_0
 set FLB_ROOT=C:\localFLB
 @rem
 if exist %INSTALL_PREFIX% rmdir /s/q %INSTALL_PREFIX%
 @rem ------------
 @rem Convert "\" in paths to "/"
 set current_dir=%~dp0
 set RTM_ROOT=%current_dir:\=/%
 set BOOST_PATH=%BOOST_PATH:\=/%
 set INSTALL_PREFIX=%INSTALL_PREFIX:\=/%
 set FLB_ROOT=%FLB_ROOT:\=/%
 @rem ------------
 @rem omniORB download
 set base_omni_url="https://openrtm.org/pub/omniORB/win32/omniORB-%OMNI_VERSION%/"
 set OMNIORB_DIR=omniORB-%OMNI_VERSION%-x64-%VC_VERSION%-py%PY_VERSION%
 set OMNIORB_ZIP=%OMNIORB_DIR%.zip
 set OMNIORB_URL=%base_omni_url%/%OMNIORB_ZIP%
 if not exist %OMNIORB_ZIP% (
   powershell wget -O %OMNIORB_ZIP% %OMNIORB_URL%
 )
 if exist %OMNIORB_DIR% rmdir /s/q %OMNIORB_DIR%
 powershell Expand-Archive .\%OMNIORB_ZIP% -DestinationPath .\\
```

```bat
 set OMNIORB_ROOT=%RTM_ROOT%/%OMNIORB_DIR%
 @rem ------------
 @rem OpenSSL download
 set base_ssl_url="https://openrtm.org/pub/OpenSSL/%SSL_VERSION%"
 set OPENSSL_ZIP=openssl-%SSL_VERSION%-win64-%SSL_VC_VERSION%.zip
 set OPENSSL_URL=%base_ssl_url%/%OPENSSL_ZIP%
 if not exist %OPENSSL_ZIP% (
   powershell wget -O %OPENSSL_ZIP% %OPENSSL_URL%
 )
 if exist OpenSSL rmdir /s/q OpenSSL
 powershell Expand-Archive .\%OPENSSL_ZIP% -DestinationPath .\\
```

```bat
 set SSL_ROOT=%RTM_ROOT%OpenSSL/build
 @rem ------------
 @rem set cmake parameter
 set CMAKE_OPT=-DRTM_VC_VER=%VC_VERSION% ^
```

```bat
   -DORB_ROOT=%OMNIORB_ROOT% ^
   -DCORBA=omniORB ^
   -DSSL_ENABLE=ON ^
   -DOPENSSL_ROOT=%SSL_ROOT% ^
   -DCMAKE_INSTALL_PREFIX=%INSTALL_PREFIX% ^
   -DWINDOWS_MSM_BUILD=ON ^
   -DBOOST_ROOT=%BOOST_PATH% ^
   -DFLUENTBIT_ENABLE=ON ^
   -DFLUENTBIT_ROOT=%FLB_ROOT% ^
   -G %CMAKE_GENERATOR% ^
   -A x64 ..
```

```bat
 call :CMAKE_Debug
 call :CMAKE_Release
 exit /b
 @rem ------------
```

```bat
 :CMAKE_Release
```

```bat
 if exist build-release rmdir /s/q build-release
 mkdir build-release
 cd build-release
 cmake %CMAKE_OPT%
 cmake --build . --verbose --config Release
 cmake --install .
 cd ..
 exit /b
 @rem ------------
```

```bat
 :CMAKE_Debug
```

```bat
 if exist build-debug rmdir /s/q build-debug
 mkdir build-debug
 cd build-debug
 cmake %CMAKE_OPT%
 cmake --build . --verbose --config Debug
 cmake --install . --config Debug
 cd ..
 exit /b
```

