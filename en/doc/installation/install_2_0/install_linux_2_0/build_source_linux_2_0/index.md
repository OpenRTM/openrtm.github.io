---
layout: page
title: building from source (linux)
---

<!-- Title: ソースからのビルド (Linux編) -->
#contents

If you want to modify and use the OpenRTM-aist source itself, you can obtain and build the OpenRTM-aist source code.

## Building with Docker

This section introduces a procedure for building using a Dockerfile in an environment where only the minimum required libraries for building OpenRTM-aist from source are installed. <br>
The Docker image is generated using the docker build command, and it is recommended because you can build in a completely clean environment every time.

If you are using Docker for the first time, install it as follows. If you are using the Ubuntu desktop environment, the docker.io package should be available.

```
 sudo apt install docker.io
```

- Reference: Installation when the docker.io package is not available
  - The process involves manually obtaining the Docker GPG key, writing repository information, and installing docker-ce
  - When building an aarch64 environment using ubuntu-20.04-server-cloudimg-arm64.img on QEMU, it was installed using the following procedure

```
 sudo apt install apt-transport-https ca-certificates curl software-properties-common
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
 sudo add-apt-repository "deb [arch=arm64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
 sudo apt update
 sudo apt install docker-ce
```

## Building C++ Source

The OpenRTM-aist 2.0 source includes Dockerfiles for Ubuntu 18.04, 20.04, and 22.04.

```
 OpenRTM-aist/scripts/ubuntu_1804/Dockerfile
 OpenRTM-aist/scripts/ubuntu_2004/Dockerfile
 OpenRTM-aist/scripts/ubuntu_2204/Dockerfile
```

The build procedure is as follows. This is a build example for Ubuntu 20.04. <br>
Although the latest OpenRTM-aist source is obtained from GitHub here, the same procedure can be used to build modified source code.

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 sudo docker build -t test -f OpenRTM-aist/scripts/ubuntu_2004/Dockerfile .
```

If the build completes without errors, you can confirm that a Docker image named test, specified by the -t option, has been generated.

```
 sudo docker images
 REPOSITORY       TAG           IMAGE ID          CREATED           SIZE
 test                    latest         0bc00f471b64   27 seconds ago   1.52GB
```

If you repeatedly modify the source and rebuild until it succeeds, many images named <none> will be generated. You can delete them by specifying the IMAGE ID with docker rmi, but if you want to delete them all at once, the following command is convenient.

```
 sudo docker rmi $(sudo docker images -f dangling=true -q)
```

### About the Docker Image "openrtm/devel-rtm"

The first line of the Dockerfiles used for source builds is as follows for Ubuntu 18.04, 20.04, and 22.04, and uses images with these names uploaded to Docker Hub.

```
 FROM openrtm/devel-rtm:ubuntu18.04
 FROM openrtm/devel-rtm:ubuntu20.04
 FROM openrtm/devel-rtm:ubuntu22.04
```

These images are generated from the following Dockerfile.devel-rtm files. fluent-bit, ROS, and ROS2 are installed.
- For Ubuntu 18.04: dashing, melodic
- For Ubuntu 20.04: foxy, noetic
- For Ubuntu 22.04: humble

```
 OpenRTM-aist/scripts/ubuntu_1804/Dockerfile.devel-rtm
 OpenRTM-aist/scripts/ubuntu_2004/Dockerfile.devel-rtm
 OpenRTM-aist/scripts/ubuntu_2204/Dockerfile.devel-rtm
```

### Script for Automatically Generating deb Packages with Docker

The script introduced here is used when creating release deb packages for OpenRTM-aist. <br>
If you want to modify and install OpenRTM-aist source code, you can easily test it using deb packages.

This script performs source builds and deb package generation in Docker, and also automatically copies the generated deb packages from the Docker container to the host.

The procedure for creating deb packages for Ubuntu 20.04 is as follows.

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2004/
 sh build-cxx.sh
 ls -l
 drwxr-xr-x  2 root    root    4096 Jun 30 15:53 cxx-deb-pkgs/
```

The generated deb packages are output under cxx-deb-pkgs. Since the owner is root, it is recommended to change ownership to the executing user for easier access. <br>
Because a Docker image with ROS installed is used, ROS-related packages (openrtm2-ros*-tp) are also generated.

```
 ls cxx-deb-pkgs/
 openrtm2-dev_2.0.0-0_amd64.deb         openrtm2-ros-tp_2.0.0-0_amd64.deb     openrtm2_2.0.0-0_amd64.buildinfo
 openrtm2-doc_2.0.0-0_all.deb                openrtm2-ros2-tp_2.0.0-0_amd64.deb   openrtm2_2.0.0-0_amd64.changes
 openrtm2-example_2.0.0-0_amd64.deb  openrtm2_2.0.0-0.dsc                            openrtm2_2.0.0-0_amd64.deb
 openrtm2-idl_2.0.0-0_amd64.deb           openrtm2_2.0.0-0.tar.gz
```

(*Note*) Running this script on an amd64 environment generates deb packages for amd64, while running it on an aarch64 environment generates deb packages for arm64.

If you want to modify and install OpenRTM-aist source code, comment out the following sections of build-cxx.sh, place the OpenRTM-aist source in the same directory as build-cxx.sh, and execute it.

```
 #----- OpenRTM-aist
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #rm -rf OpenRTM-aist    <-- Comment out
 #git clone https://github.com/OpenRTM/OpenRTM-aist    <-- Comment out
```

## Building Python Source

The OpenRTM-aist-Python source does not include a Dockerfile. The following Dockerfiles are used when creating release deb packages for OpenRTM-aist-Python.
- [ubuntu_1804/Dockerfile-python-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_1804/Dockerfile-python-deb)
- [ubuntu_2004/Dockerfile-python-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2004/Dockerfile-python-deb)
- [ubuntu_2204/Dockerfile-python-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2204/Dockerfile-python-deb)

As with the C++ source build, this section introduces a script that performs source builds and deb package generation in Docker, and automatically copies the generated deb packages from the Docker container to the host.

The procedure for creating deb packages for Ubuntu 20.04 is as follows.

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2004/
 sh build-python.sh
```

The generated deb packages are output under python-deb-pkgs, and the source packages are output under python-src-pkgs.

```
 ls python-deb-pkgs/
 openrtm2-python3-doc_2.0.0-0_all.deb 
 openrtm2-python3-example_2.0.0-0_amd64.deb  openrtm2-python3_2.0.0-0_amd64.changes
 openrtm2-python3_2.0.0-0.dsc                           openrtm2-python3_2.0.0-0_amd64.deb
```

```
 ls python-src-pkgs/
 OpenRTM-aist-Python-2.0.0.tar.gz  OpenRTM-aist-Python-2.0.0.zip  
```

If you want to modify and install OpenRTM-aist-Python source code, comment out the following sections of build-python.sh, place the OpenRTM-aist-Python source in the same directory as build-python.sh and Dockerfile-python-deb, and execute it.

```
 #----- OpenRTM-aist-Python
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #-------- Comment out from here
 #rm -rf OpenRTM-aist-Python
 #git clone https://github.com/OpenRTM/OpenRTM-aist-Python
 #cd OpenRTM-aist-Python
 #git checkout ${BRANCH}
 #cd -
 #-------- Comment out to here
```

## Building Java Source

The OpenRTM-aist-Java source does not include a Dockerfile. The following Dockerfiles are used when creating release deb packages for OpenRTM-aist-Java.
- [ubuntu_1804/Dockerfile-java-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_1804/Dockerfile-java-deb)
- [ubuntu_2004/Dockerfile-java-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2004/Dockerfile-java-deb)
- [ubuntu_2204/Dockerfile-java-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2204/Dockerfile-java-deb)

As with the C++ source build, this section introduces a script that performs source builds and deb package generation in Docker, and automatically copies the generated deb packages from the Docker container to the host.

The procedure for creating deb packages for Ubuntu 20.04 is as follows.

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2004/
 sh build-java.sh
```

The generated deb packages are output under java-deb-pkgs, and the source packages are output under java-src-pkgs.

```
 ls java-deb-pkgs/
 openrtm2-java-doc_2.0.0-0_all.deb        openrtm2-java_2.0.0-0_amd64.buildinfo
 openrtm2-java-example_2.0.0-0_amd64.deb  openrtm2-java_2.0.0-0_amd64.changes
 openrtm2-java_2.0.0-0.dsc                openrtm2-java_2.0.0-0_amd64.deb
```

```
 ls java-src-pkgs/
 OpenRTM-aist-Java-2.0.0-jar.zip  OpenRTM-aist-Java-2.0.0.zip
 OpenRTM-aist-Java-2.0.0.tar.gz  
```

If you want to modify and install OpenRTM-aist-Java source code, comment out the following sections of build-java.sh, place the OpenRTM-aist-Java source in the same directory as build-java.sh and Dockerfile-java-deb, and execute it.

```
 #----- OpenRTM-aist-Java
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #-------- Comment out from here
 #rm -rf OpenRTM-aist-Java
 #git clone https://github.com/OpenRTM/OpenRTM-aist-Java
 #cd OpenRTM-aist-Java
 #git checkout ${BRANCH}
 #cd -
 #-------- Comment out to here
```
