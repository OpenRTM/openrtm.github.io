---
layout: page
title: building from source (linux)
---

<!-- Title: ソースからのビルド (Linux編) -->
#contents

If you want to modify and use the OpenRTM-aist source code itself, you can obtain the OpenRTM-aist source code and build it.

## Building with Docker

This section introduces how to build OpenRTM-aist using a Dockerfile in an environment where only the minimum required libraries for building OpenRTM-aist are installed.<br>
The Docker image is created with the `docker build` command. Since the build is performed in a clean environment every time, this method is recommended.

If this is your first time using Docker, install it as follows. On an Ubuntu desktop environment, the `docker.io` package should be available.

```
 sudo apt install docker.io
```

<!-- - 参考：docker.io パッケージの提供が無い場合のインストール -->
<!-- -- 手動で、DockerのGPGキーを取得して、リポジトリ情報を書き込んで、docker-ceをインストールする流れになります -->
<!-- -- QEMU上にubuntu-20.04-server-cloudimg-arm64.imgで aarch64 環境を構築した時は、以下の手順でインストールしました -->
<!-- sudo apt install apt-transport-https ca-certificates curl software-properties-common -->
<!-- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - -->
<!-- sudo add-apt-repository "deb [arch=arm64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  -->
<!-- sudo apt update -->
<!-- sudo apt install docker-ce -->


## Building the C++ Source

The OpenRTM-aist 2.1 source tree includes Dockerfiles for Ubuntu 22.04 and 24.04.

```
 OpenRTM-aist/scripts/ubuntu_2204/Dockerfile
 OpenRTM-aist/scripts/ubuntu_2404/Dockerfile
```

The build procedure is shown below. This example builds for Ubuntu 24.04.<br>
Although the latest OpenRTM-aist source code is obtained from GitHub in this example, the same procedure can also be used to build modified source code.

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 sudo docker build -t test -f OpenRTM-aist/scripts/ubuntu_2404/Dockerfile .
```

If the build completes successfully, you can confirm that the Docker image named `test` specified with the `-t` option has been created.

```
 sudo docker images
 REPOSITORY       TAG           IMAGE ID          CREATED           SIZE
 test                    latest         0bc00f471b64   27 seconds ago   1.52GB
```

When repeatedly modifying the source and rebuilding until the build succeeds, many images named `<none>` are generated. Although they can be removed individually by specifying the IMAGE ID with `docker rmi`, the following command is convenient for removing them all at once.

```
 sudo docker rmi $(sudo docker images -f dangling=true -q)
```

### About the Docker Image "openrtm/devel-rtm"

The first line of the Dockerfiles used for the source build is as follows for Ubuntu 22.04 and 24.04, respectively. These Dockerfiles use the images with the following names uploaded to Docker Hub.

```
 FROM openrtm/devel-rtm:ubuntu22.04
        or
 FROM openrtm/devel-rtm:ubuntu24.04
```

These images are generated from the following `Dockerfile.devel-rtm`. They include fluent-bit and ROS2.

- For Ubuntu 22.04: humble
- For Ubuntu 24.04: jazzy

```
 OpenRTM-aist/scripts/ubuntu_2204/Dockerfile.devel-rtm
 OpenRTM-aist/scripts/ubuntu_2404/Dockerfile.devel-rtm
```

### Script for Building deb Packages with Docker

The script introduced here is used to create the release deb packages for OpenRTM-aist.<br>
If you want to install a modified version of OpenRTM-aist, you can easily test it by creating deb packages.

This script performs the entire process, from building the source code and generating deb packages in Docker to copying the resulting deb packages from the Docker container to the host system.

The procedure for creating deb packages for Ubuntu 24.04 is as follows.

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2404/
 sh build-cxx.sh
 ls -l
 drwxr-xr-x  2 root    root    4096 Jun 30 15:53 cxx-deb-pkgs/
```

The generated deb packages are output under `cxx-deb-pkgs`. Since the owner is `root`, it is recommended to change the ownership to the user who executed the script for easier access.<br>
Because the Docker image includes ROS, packages for ROS2 (`openrtm2-ros2-tp`) are also generated.
The SSM package (`openrtm2-ssm-tp`), introduced in Version 2.1, is also generated.

```
 ls cxx-deb-pkgs/
 openrtm2_2.1.0-0_amd64.buildinfo  openrtm2-dev_2.1.0-0_amd64.deb      openrtm2-naming_2.1.0-0_amd64.deb
 openrtm2_2.1.0-0_amd64.changes    openrtm2-doc_2.1.0-0_all.deb        openrtm2-ros2-tp_2.1.0-0_amd64.deb
 openrtm2_2.1.0-0_amd64.deb        openrtm2-example_2.1.0-0_amd64.deb  openrtm2-ssm-tp_2.1.0-0_amd64.deb
 openrtm2_2.1.0-0.dsc              openrtm2-idl_2.1.0-0_amd64.deb      openrtm2-ssm-tp-dbgsym_2.1.0-0_amd64.ddeb
```

(*Note*) Running this script on an amd64 environment generates deb packages for amd64, while running it on an aarch64 environment generates deb packages for arm64.

If you want to install a modified version of OpenRTM-aist, comment out the following lines in `build-cxx.sh`, place the OpenRTM-aist source code in the same directory as `build-cxx.sh`, and then run the script.

```
 #----- OpenRTM-aist
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #rm -rf OpenRTM-aist    <-- Comment out
 #git clone https://github.com/OpenRTM/OpenRTM-aist    <-- Comment out
```

## Building the Python Source

The OpenRTM-aist-Python source package does not include a Dockerfile. The following Dockerfiles are used when creating the release deb packages for OpenRTM-aist-Python.

- [ubuntu_2204/Dockerfile-python-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2204/Dockerfile-python-deb)
- [ubuntu_2404/Dockerfile-python-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2404/Dockerfile-python-deb)

As with the C++ source build, the following script performs the entire process, from building the source code and generating deb packages in Docker to copying the generated deb packages from the Docker container to the host system.

The procedure for creating deb packages for Ubuntu 24.04 is as follows.

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2404/
 sh build-python.sh
```

The generated deb packages are output under `python-deb-pkgs`.

```
 ls python-deb-pkgs/
 openrtm2-python3_2.1.0-0_amd64.changes  openrtm2-python3_2.1.0-0.dsc
 openrtm2-python3_2.1.0-0_amd64.deb      openrtm2-python3-example_2.1.0-0_amd64.deb
```

If you want to install a modified version of OpenRTM-aist-Python, comment out the following section in `build-python.sh`, place the OpenRTM-aist-Python source code in the same directory as `build-python.sh` and `Dockerfile-python-deb`, and then run the script.

```
 #----- OpenRTM-aist-Python
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #--------　Comment out from here
 #rm -rf OpenRTM-aist-Python
 #git clone https://github.com/OpenRTM/OpenRTM-aist-Python
 #cd OpenRTM-aist-Python
 #git checkout ${BRANCH}
 #cd -
 #--------　Comment out to here
```

## Building the Java Source

The OpenRTM-aist-Java source package does not include a Dockerfile. The following Dockerfiles are used when creating the release deb packages for OpenRTM-aist-Java.

- [ubuntu_2204/Dockerfile-java-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2204/Dockerfile-java-deb)
- [ubuntu_2404/Dockerfile-java-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2404/Dockerfile-java-deb)

As with the C++ source build, the following script performs the entire process, from building the source code and generating deb packages in Docker to copying the generated deb packages from the Docker container to the host system.

The procedure for creating deb packages for Ubuntu 24.04 is as follows.

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2404/
 sh build-java.sh
```

The generated deb packages are output under `java-deb-pkgs`, and the source packages are output under `java-src-pkgs`.

```
 ls java-deb-pkgs/
 openrtm2-java_2.1.0-0_amd64.buildinfo  openrtm2-java_2.1.0-0_amd64.deb  openrtm2-java-doc_2.1.0-0_all.deb
 openrtm2-java_2.1.0-0_amd64.changes    openrtm2-java_2.1.0-0.dsc        openrtm2-java-example_2.1.0-0_amd64.deb
```

```
 ls java-src-pkgs/
 OpenRTM-aist-Java-2.1.0-jar.zip  OpenRTM-aist-Java-2.1.0.tar.gz  OpenRTM-aist-Java-2.1.0.zip
```

If you want to install a modified version of OpenRTM-aist-Java, comment out the following section in `build-java.sh`, place the OpenRTM-aist-Java source code in the same directory as `build-java.sh` and `Dockerfile-java-deb`, and then run the script.

```
 #----- OpenRTM-aist-Java
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #--------　Comment out from here
 #rm -rf OpenRTM-aist-Java
 #git clone https://github.com/OpenRTM/OpenRTM-aist-Java
 #cd OpenRTM-aist-Java
 #git checkout ${BRANCH}
 #cd -
 #--------　Comment out to here
```

