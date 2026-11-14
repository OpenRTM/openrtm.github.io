---
layout: page
title: building from source (c++ version)
---

<!-- Title: ソースからのビルド（C++版） -->

If you want to modify the OpenRTM-aist core and use it on Windows, you can obtain the OpenRTM-aist source code and build it yourself. Since OpenRTM-aist 2.0, CMake has been supported, so the procedure differs from that used up to version 1.2.

#contents

<!-- ------------------------------------------------------------ -->
## Required Software and Libraries

The following software is required. For details, see [Installing OpenRTM-aist 2.1 on Windows](/en/doc/installation/install_2_1/install_windows_2_1/install_2_1).

- Visual Studio
- Python
- CMake
- Doxygen & Graphviz (if you also want to build documentation)

In addition, the omniORB library is required.

- omniORB 4.3.4

Prebuilt binary packages provided by openrtm.org are available at the following link under names such as omniORB-4.3.4-x64-vc16-pyXX.zip.

Replace XX with the version of Python you have installed, download the appropriate package, and extract it to a suitable location (the examples below use `C:\workspace\omniORB`).

- [Binary Packages Provided by openrtm.org](https://openrtm.org/pub/omniORB/win32/omniORB-4.3.4/)

For information about building with other libraries, see [RT System Development (Advanced) - Building OpenRTM-aist (C++ Version) with CMake](/en/doc/installation/install_2_0/cpp_2_0/build_2_0/openrtm_cpp_cmake_build).

## Build and Installation Commands

Obtain the source code. If you want the latest source code of the OpenRTM-aist 2.1 series, use the master branch. If you want the OpenRTM-aist 2.1.0 release source, check out the v2.1.0 tag. <br>

```bash
git clone https://github.com/OpenRTM/OpenRTM-aist
cd OpenRTM-aist
git checkout -b v210-src refs/tags/v2.1.0
```

Run CMake with the following options.

- `-DORB_ROOT` : Path to the downloaded and extracted omniORB
- `-G` : Visual Studio version (e.g., "Visual Studio 18 2026", "Visual Studio 17 2022", "Visual Studio 16 2019")
- `-DCMAKE_INSTALL_PREFIX` : Installation destination path for the source build

```bash
mkdir build
cd build
cmake -DORB_ROOT=C:/workspace/omniORB-4.2.5-x64-vc16-py314 -G "Visual Studio 18 2026" -DCMAKE_INSTALL_PREFIX=C:/workspace/openrtminstall ..
```

Next, execute the following command. If the following message is displayed at the end, the build has succeeded.

```bash
cmake --build . --verbose --config Release
Build succeeded.
    0 Warning(s)
    0 Error(s)
```

After the build succeeds, complete the installation with the following command.

```bash
cmake --build . --config Release --target install
```

## Batch Processing with a Script

The following script (`OpenRTM-build-Windows.bat`) performs the entire process from downloading omniORB to building the source and installing OpenRTM-aist. It should be placed and executed in the cloned OpenRTM-aist directory.

```bat
cd OpenRTM-aist
copy scripts\OpenRTM-build-Windows.bat .
OpenRTM-build-Windows.bat > build.log
```

This `OpenRTM-build-Windows.bat` script is the same one used when building OpenRTM-aist for inclusion in the Windows MSI installer.

Please modify the CMake options as needed so that only the required components are built.
