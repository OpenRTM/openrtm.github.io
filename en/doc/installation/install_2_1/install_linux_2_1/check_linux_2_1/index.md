---
layout: page
title: operation check (linux)
---

<!-- Titile: 動作確認(Linux編) -->

#contents

## Running the Sample Components

After the installation has completed successfully, you can verify the operation using the included sample components. The sample components are installed in the following locations.

```
 /usr/share/openrtm-2.1/components/c++/examples
 /usr/share/openrtm-2.1/components/python3/
 /usr/share/openrtm-2.1/components/java
```

Start OpenRTP, the tool used to operate RTCs and build RT systems.

- For OpenRTM-aist 2.x, start it with the `openrtp2` command.

```
 $ openrtp2
```

<!-- OpenRTM-aist 1.2系では openrtp コマンドで起動します。コマンド名は異なりますが、起動手順、使い方は 1.2系と変更ありませんので、詳細は以下のページをご覧ください。 -->
<!-- - [[OpenRTPの起動手順(1.2系、Linux):/node/6654]] -->
<!--  -->
<!-- ※OpenRTPは1.2系と2.0系の共存が可能です。このため、openrtp と openrtp2 の両方を実行することは可能です。  -->

The Windows version of the included sample components is listed on the following page. There is no difference in the behavior of the components between the Windows and Linux versions.

- [List of Sample Components]({{ site.baseurl }}/en/doc/installation/install_2_0/install_windows_2_0/check_windows_2_0#toc1)

If you would like more detailed instructions on how to run the sample components in a Linux environment, please refer to the following pages for Version 1.2. The execution procedure is the same for Version 2.x; simply replace the component paths accordingly.

- [OpenRTM-aist (C++ Edition) 1.2 - Operation Check (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/cpp_1_2/check_linux_1_2)
- [OpenRTM-aist (Python Edition) 1.2 - Operation Check (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/python_1_2/check_python_linux_1_2)
- [OpenRTM-aist (Java Edition) 1.2 - Operation Check (Linux)]({{ site.baseurl }}/en/doc/installation/install_1_2/java_1_2/check_linux_java_1_2)

## Installing the OpenCV Sample Components

A deb package is not provided for the OpenCV C++ sample components. Instead, a script is provided to generate the deb package from the source code. Please build and install it.

### Example: Installing OpenCV 4.5.4

The following example builds and installs OpenCV Version 4.5.4 together with the OpenCV extra modules (opencv_contrib).

- First, uncomment the following `deb-src` line in `/etc/apt/sources.list`.

```
 $ sudo vi /etc/apt/sources.list
      :
 deb-src http://jp.archive.ubuntu.com/ubuntu/ *** universe
    or
 deb-src http://us.archive.ubuntu.com/ubuntu/ *** universe
```

- Run the following commands to install OpenCV.

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

### Building the OpenCV Sample Components

Obtain the ImageProcessing source code, build it, and generate the deb package.

```
 git clone https://github.com/OpenRTM/ImageProcessing
 cd ImageProcessing/opencv
 mkdir build
 cd build
 cmake ..
 ./build_linux_package.sh
```

This generates `imageprocessing_2.x.x_amd64.deb`. Install it as follows.

```
 sudo dpkg -i imageprocessing_2.x.x_amd64.deb
 ls /usr/share/openrtm-2.0/components/c++/opencv-rtcs/
 Affine                       CameraViewer     Edge         Histogram         ImageSubtraction  Perspective        Scale                 Template
 BackGroundSubtractionSimple  Chromakey        Findcontour  Hough             ObjectTracking    RockPaperScissors  Sepia                 Translate
 Binarization                 DilationErosion  Flip         ImageCalibration  OpenCVCamera      Rotate             SubtractCaptureImage  rtc.conf
```

Executable files (`***Comp`) are installed in each sample directory. Try running them.
```

