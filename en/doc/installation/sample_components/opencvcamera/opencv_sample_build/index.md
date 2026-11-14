---
layout: page
title: Building OpenCV Samples on Linux
---

<!-- Title: Building OpenCV Samples on Linux -->

On Linux, the OpenCV sample code is **not** installed when you run the all-in-one installation script. To install the sample code, you must obtain the source code from the GitHub repository and build it manually.

The procedure is as follows.

- Install OpenRTM-aist using the [all-in-one installation script]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script). (The following procedure requires the C++ and Python editions. In most cases, OpenRTP is also required to run the samples. Specify the appropriate options as needed.) For example:

```sh
$ sudo sh pkg_install_ubuntu.sh -l all --yes
```

- Install OpenCV 3.4 or later. (Currently, only OpenCV 3.4.5 has been tested. Depending on your environment, you may need to build OpenCV from source.)

- Obtain the source code and build it using the following procedure.

```sh
$ sudo apt-get install git
$ git clone https://github.com/OpenRTM/ImageProcessing.git
$ cd ImageProcessing/opencv
$ mkdir build
$ cd build
$ cmake ..
$ make
$ ./build_linux_package.sh
$ sudo dpkg -i imageprocessing_1.2.1_amd64.deb
```
