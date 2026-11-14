---
layout: page
title: building a development environment
---

<!-- Title: Building a Development Environment -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * Building a Development Environment -->
#contents

To develop components that run on EV3 and ev3dev, there are two approaches: developing directly on the EV3 or using a cross-development environment.

However, since the EV3 has only 64 MB of memory and a CPU clock speed of approximately 300 MHz, it is quite slow by today's development standards. As a result, development directly on the EV3 can be rather challenging.

Cross-development refers to creating executable files for a different architecture (such as ARM) on a general-purpose PC architecture such as Intel CPUs.

Although cross-development does not allow the compile-and-run workflow available on the target system itself, compilation is dramatically faster, resulting in higher overall development efficiency.

## Installing Ubuntu

The development environment uses Ubuntu (14.04 LTS), one of the Linux distributions.

- [Ubuntu 14.04 LTS](https://www.ubuntulinux.jp/News/ubuntu1404-ja-remix)

Download the ISO image from the above URL and install the operating system.

You may install it directly on your PC or use it within a virtual machine.

Common virtual machine environments include:

- VMware Player
  - As of August 2015: [https://my.vmware.com/jp/web/vmware/free#desktop_end_user_computing/vmware_player/7_0](https://my.vmware.com/jp/web/vmware/free#desktop_end_user_computing/vmware_player/7_0)
  - Or search for "VMware Player"
- VirtualBox
  - As of August 2015: [http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html?ssSourceSiteId=otnjp](http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html?ssSourceSiteId=otnjp)
  - Or search for "VirtualBox"
- Parallels (Mac)
  - As of August 2015: [http://www.parallels.com/jp/](http://www.parallels.com/jp/)
  - Or search for "Parallels"

For detailed usage instructions, please refer to each product's website or search for online tutorials.

## brickstrap

From this point onward, it is assumed that Ubuntu 14.04 has already been installed.

First, install a tool called **brickstrap**. Although brickstrap is primarily used to create ev3dev OS images, it can also be used as a cross-development tool.

## Installing brickstrap

brickstrap is developed on the following GitHub repository.

- [ev3dev](https://github.com/ev3dev/ev3dev)
  - [Cross-development using brickstrap](https://github.com/ev3dev/ev3dev/wiki/Using-brickstrap-to-cross-compile-and-debug)

First, install brickstrap. Since it is not available in the standard Debian repositories, the ev3dev.org package repository must be added.

```

$ sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 2B210565

<!-- $ sudo apt-add-repository http://ev3dev.org/debian -->

$ sudo apt-add-repository "deb http://archive.ev3dev.org/ubuntu trusty main"
$ sudo apt-get update
$ sudo apt-get install brickstrap

```

### Preparing for Image Creation

First, execute the following commands to create a supermin appliance.

```

$ sudo update-guestfs-appliance
$ sudo usermod -a -G kvm <username>
$ sudo chmod +r /boot/vmlinuz*

```

### Creating the Development Environment

Once the preparation is complete, create the development environment.

A simulated filesystem corresponding to the EV3 target system will be created in a specified directory. A suitable location is somewhere under your home directory. In this example, a directory named `work` is created under the home directory.

```

$ cd ~
$ mkdir work
$ cd work

```

Create the filesystem and image using the following command:

```

$ brickstrap -b ev3-ev3dev-jessie -d ev3-ev3dev-work all

```

This command takes approximately 10–20 minutes to complete.

What actually happens is that the commands, packages, and files required for the ev3dev Linux system are installed into a virtual root directory named `ev3-ev3dev-work`, and then assembled into an image file that can be written to an SD card.

When the process completes, you should find the files `ev3-ev3dev-work.tar` and `ev3-ev3dev-work.img`.

Writing the `.img` file to an SD card allows ev3dev to boot on the EV3.

### Replacing proot

On Ubuntu 14.04 x86_64, the version of `proot` used internally by brickstrap is outdated and cannot execute certain functions related to user IDs and group IDs, causing `apt-get` errors.

To avoid this issue, use `proot` version 4.0 or later.

- [http://proot.me/#downloads](http://proot.me/#downloads)

Download the x86_64 binary and copy it to your machine.

```

$ wget http://portable.proot.me/proot-x86_64
$ sudo mv /usr/bin/proot /usr/bin/proot_3.0.2
& sudo mv proot /usr/bin/
$ chmod 755 /usr/bin/proot

```

### Starting the Shell

The cross-development environment is now ready.

Next, OpenRTM-aist can be compiled and installed, and RT Components can be developed.

brickstrap provides a mode that behaves as though packages are being installed and source code is being compiled directly on the EV3.

Run the following command:

```

user@host:`/work$` brickstrap -b ev3-ev3dev-jessie -d ev3-ev3dev-work shell

```

The command prompt will change to **#**, indicating that you are now in the simulated EV3 environment.

## Compiling OpenRTM-aist

If you wish to compile and install OpenRTM-aist yourself, follow the steps below.

If you plan to use prebuilt packages instead, skip to the next section.

First, install the packages required to build OpenRTM-aist.

```

# apt-get update

# apt-get install libomniorb4-dev omniidl

# apt-get install gcc g++ make uuid-dev libboost-filesystem-dev

# apt-get install doxygen

# apt-get install build-essential debhelper devscripts

# apt-get install subversion texlive texlive-lang-cjk xdvik-ja python-yaml

# apt-get install wget

```

Next, download the OpenRTM-aist source code.

```

# cd /home

# wget http://tmp.openrtm.org/pub/OpenRTM-aist/cxx/x.y.z/OpenRTM-aist-x.y.z.tar.gz

# tar xvzf OpenRTM-aist-x.y.z.tar.gz

# cd OpenRTM-aist

# ./configure --prefix=/usr

# cd packages

# make

```

This generates OpenRTM-aist packages under the `packages` directory.

Install them as follows:

```

# dpkg -i openrtm-aist-*

```

Similarly, download and package OpenRTM-aist-Python.

```

# wget http://tmp.openrtm.org/pub/OpenRTM-aist/python/x.y.z/OpenRTM-aist-Python-x.y.z-RELEASE.zip

# cd OpenRTM-aist-Python

# cd packages

# make

```

Packages will be generated in the `packages` directory.

Install them as follows:

```

# dpkg -i openrtm-aist-python-*

```

## Installing OpenRTM-aist

Instead of compiling OpenRTM-aist from source as described above, you may install prebuilt packages.

The procedure is almost identical to installing OpenRTM-aist directly on ev3dev.

### Editing sources.list

Edit `/etc/apt/sources.list` to add openrtm.org as a package repository.

```

# vi /etc/apt/sources.list

```

Open the file and add the following line:

```

deb http://ftp.debian.org/debian jessie main contrib non-free
deb http://ev3dev.org/debian jessie main
deb http://openrtm.org/pub/Linux/debian jessie main ← Add this line

```

As shown above, add the OpenRTM repository at the end of the file.

Then update the package database:

```

# apt-get update

```

Since the EV3 is relatively slow, updating the package database may take a considerable amount of time.

### Installing OpenRTM-aist Packages

Once the OpenRTM package repository is available, install the packages as follows:

```

# apt-get install openrtm-aist openrtm-aist-dev openrtm-aist-example

# apt-get install openrtm-aist-python openrtm-aist-python-example

```
