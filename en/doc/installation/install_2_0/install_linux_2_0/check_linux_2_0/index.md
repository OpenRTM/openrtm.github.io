---
layout: page
title: operation check (linux)
---

<hr>

<!-- Titile: 動作確認(Linux編) -->

#contents

## Running Sample Components

After installation has completed successfully, you can check the operation using the included sample components. The sample components are installed in the following locations.

```
 /usr/share/openrtm-2.0/components/c++/examples
 /usr/share/openrtm-2.0/components/python3/
 /usr/share/openrtm-2.0/components/java
```

Start OpenRTP, a tool for operating RTCs and building RT systems.

- OpenRTM-aist 2.0 series is started with the openrtp2 command

```
 $ openrtp2
```

OpenRTM-aist 1.2 series is started with the openrtp command. Although the command name is different, the startup procedure and usage are the same as in the 1.2 series, so please refer to the following page for details.
- [OpenRTP Startup Procedure (1.2 Series, Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/start_openrtp_linux_1_2)

* OpenRTP can coexist between the 1.2 series and the 2.0 series. Therefore, it is possible to run both openrtp and openrtp2. 

For the included sample components, a list for the Windows version is provided on the following page. There is no difference in component operation between the Windows version and the Linux version.
- [Sample Component List]({{ site.baseurl }}/en/doc/installation/install_2_0/install_windows_2_0/check_windows_2_0#toc1)

If you would like to know a little more about the procedure for running sample components in a Linux environment, please refer to the following explanation pages for the 1.2 series. If you replace the component paths accordingly, the execution procedure is the same for the 2.0 series.
- [OpenRTM-aist (C++ Version) 1.2 Series: Operation Check (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/cpp_1_2/check_linux_1_2)
- [OpenRTM-aist (Python Version) 1.2 Series: Operation Check (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2/check_python_linux_1_2)
- [OpenRTM-aist (Java Version) 1.2 Series: Operation Check (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/java_1_2/check_linux_java_1_2)

## Installing OpenCV Sample Components

Deb packages for installing the OpenCV C++ sample components are not provided. A script for generating deb packages from source is provided, so please build and install them.

### OpenCV 4.5.4 Installation Example

This is an example of building and installing version 4.5.4 of OpenCV itself together with the extension module set (opencv_contrib).

- First, uncomment the following deb-src line in /etc/apt/sources.list.

```
 $ sudo vi /etc/apt/sources.list
      :
 deb-src http://jp.archive.ubuntu.com/ubuntu/ *** universe
    or
 deb-src http://us.archive.ubuntu.com/ubuntu/ *** universe
```

- OpenCV installation is completed by executing the following commands.

```
 sudo apt build-dep opencv
 wget https://github.com/opencv/opencv/archive/refs/tags/4.5.4.tar.gz -O opencv-4.5.4.tar.gz
 tar xvzf opencv-4.5.4.tar.gz
 wget https://github.com/opencv/opencv_contrib/archive/refs/tags/4.5.4.tar.gz -O opencv_contrib-4.5.4.tar.gz
 tar xvzf opencv_contrib-4.5.4.tar.gz
 cd opencv-4.5.4
 mkdir build
 cd build
 cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.5.4/modules -DBUILD_opencv_java=OFF ..
 make -j$(nproc)
 sudo make install
 sudo ldconfig
```

### Procedure for Building OpenCV Sample Components

Obtain and build the ImageProcessing source, then generate the deb package.

```
 git clone https://github.com/OpenRTM/ImageProcessing
 cd ImageProcessing/opencv
 mkdir build
 cd build
 cmake ..
 ./build_linux_package.sh
```

This generates imageprocessing_2.x.x_amd64.deb, so install it.

```
 sudo dpkg -i imageprocessing_2.x.x_amd64.deb
 ls /usr/share/openrtm-2.0/components/c++/opencv-rtcs/
 Affine                       CameraViewer     Edge         Histogram         ImageSubtraction  Perspective        Scale                 Template
 BackGroundSubtractionSimple  Chromakey        Findcontour  Hough             ObjectTracking    RockPaperScissors  Sepia                 Translate
 Binarization                 DilationErosion  Flip         ImageCalibration  OpenCVCamera      Rotate             SubtractCaptureImage  rtc.conf
```

Executable files (***Comp) are installed under each sample directory, so please try running them. 

## Notes on CMake in an Environment Where the 1.2 Series and 2.0 Series Coexist

The C++ sample components have generally been regenerated so that they can be built with CMake. <br>
Here, ConsoleIn is used as an example.

In an environment where the 1.2 series and 2.0 series coexist, OpenRTMConfig.cmake is installed in the following two locations. Therefore, the OpenRTMConfig.cmake found first is used.

```
 /usr/lib/x86_64-linux-gnu/openrtm-2.0/cmake/OpenRTMConfig.cmake
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/cmake/OpenRTMConfig.cmake
```

In this environment, try running cmake for ConsoleIn.

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist/examples/ConsoleIn/
 mkdir build
 cd build
 cmake ..
      :
 -- OpenRTMConfig.cmake 2.0.0 found.
```

In the 2.0 series OpenRTMConfig.cmake, the version number is output. In the 1.2 series, the version number is not output.<br>
If you want to build with the 1.2 series, specify OpenRTM_DIR as follows using the cmake option.

```
 cmake -DOpenRTM_DIR=/usr/lib/x86_64-linux-gnu/openrtm-1.2/cmake ..
    :
 -- OpenRTMConfig.cmake found.

```
