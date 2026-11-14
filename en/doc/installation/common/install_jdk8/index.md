---
layout: page
title: installing jdk8
---

<!-- Title: JDK8のインストール -->
#contents(5)

Running OpenRTM-aist-Java requires communication middleware called CORBA. In Java, CORBA functionality was originally included as a standard feature. However, since Java 9 it has been treated as deprecated (a feature that is discouraged and scheduled for future removal), and it was completely removed in Java 11 and later. Therefore, to use OpenRTM-aist-Java, it is necessary to use JDK8, the Java 8 development environment package.

Although Oracle, the original distributor, has been discontinuing distribution and support for JDK8, many users still require Java 8. As a result, JDK8 remains available from several vendors for the time being. This document introduces how to obtain and install JDK8.

## JDK8 Distributors

Some JDK8 distributors that we have identified are listed below. Please note that this is simply a list of distributors we have found, and the absence of a distributor from this list does not imply any particular intention. In addition, distribution conditions vary by site, such as paid usage licenses or paid support services. Please review the terms on each site before use.

### Oracle

As of November 2019, JDK8 is still available for download from Oracle, the developer and distributor of Java. Personal and development use appear to be covered by a free license, while commercial use appears to require a paid license. For accurate license terms and conditions, please refer to the links below and Oracle's official announcements.

- [Oracle Java SE Subscription](https://www.oracle.com/technetwork/java/javaseproducts/overview/index.html)
  - [JDK8 Download](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
  - This page may be removed if Oracle stops distributing Java 8.

### OpenJDK

OpenJDK is Oracle's open-source implementation of Java and is distributed under GPLv2 with the Classpath Exception. Most JDK implementations are based on OpenJDK.

- [OpenJDK](http://openjdk.java.net/)

From the link below, locate Java SE 8xxxx (xxxx was u231 as of November 2019), then click the DOWNLOAD button for the JDK and obtain the package appropriate for your platform.

- [OpenJDK8 download](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

### Adopt Open JDK

AdoptOpenJDK is a project sponsored by IBM and maintained by the community that provides OpenJDK builds. Two JVM implementations are available: HotSpot, developed by the OpenJDK community, and OpenJ9, developed by the Eclipse community.

From the link below, select [OpenJDK8 (LTS)] and a JVM ([HotSpot] or [OpenJ9]), then click [Latest release]. A download appropriate for your platform should begin. If you need a build for a different platform, click [Other platforms] to obtain the required JDK. Installation instructions are available through the [Installation] link.

- [AdoptOpenJDK](https://adoptopenjdk.net/)
  - [Adopt Open JDK 8 Support](https://adoptopenjdk.net/support.html) (until May 2026)

### Amazon Open JDK

Amazon Corretto is an OpenJDK build that includes long-term support from Amazon. To obtain it, visit the website below and click the [Download Amazon Corretto 8] button. A list of builds for different platforms will be displayed. Obtain the installation file appropriate for your platform.

- [Amazon Corretto](https://aws.amazon.com/jp/corretto/)
  - [Amazon Open JDK 8 Support](https://aws.amazon.com/jp/corretto/faqs/#support) (until June 2026)

## Installation on Linux

### Obtaining Packages from Repositories

Major Linux distributions provide OpenJDK packages equivalent to JDK8 as standard packages.

#### Ubuntu/Debian/Raspbian

On Ubuntu Linux, Debian Linux, and similar distributions, installation can be performed with the following apt command.

```bash
$ sudo apt install openjdk-8-jdk
```


#### Fedora

On Fedora Linux, installation can be performed with the following yum command.

```bash
$ sudo yum -y install java-1.8.0-openjdk
```


### Methods Other Than Obtaining Packages from Repositories

You can also obtain JDKs from the third-party vendor websites listed above. For installation procedures, follow the instructions provided on those sites or use the standard Java installation methods.

As a reference, the following procedure shows how to install the Adoptium (formerly Temurin) package on a Raspberry Pi OS bookworm environment.


```bash
$ sudo apt install apt-transport-https
$ wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null
$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/trusted.gpg.d/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
$ sudo apt update
$ sudo apt install temurin-8-jdk
```

Verify the installed version.


```bash
$ java -version
openjdk version "1.8.0_402"
OpenJDK Runtime Environment (Temurin)(build 1.8.0_402-b06)
OpenJDK Client VM (Temurin)(build 25.402-b06, mixed mode)
```

### When a JDK Other Than JDK8 Is Already Installed

A JDK other than JDK8 may already be installed as the default Java environment.


```bash
$ java -version
```


Verify that the version starts with 1.8, which indicates JDK8.

If it does not, use the following command to select a JDK8-based Java environment.

```bash
$ sudo update-alternatives --config java
```

An example execution after installing openjdk-8-jdk on an Ubuntu 18.04 environment is shown below.

```bash
$ sudo update-alternatives --config java
Selection Path                                           Priority  Status 
0         /usr/lib/jvm/java-11-openjdk-amd64/bin/java    1111      auto mode
1         /usr/lib/jvm/java-11-openjdk-amd64/bin/java    1111      manual mode
2         /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java 1081      manual mode

Press <Enter> to keep the current choice [*], or type the selection number: 2
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java to provide /usr/bin/java (java) in manual mode

```

## Installation on Windows

To install JDK8 on Windows, obtain an MSI file from one of the websites listed above and run it, or, for files distributed in formats other than MSI, follow the installation instructions provided by the distributor.

After installation, as in the Linux case above, open a command prompt and enter:

```bash
java -version
```

to verify that the installation was successful.


```bash
