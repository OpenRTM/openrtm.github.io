---
layout: page
title: "installing jdk 8"
---

<!-- Title: Installing JDK 8 -->
#contents(5)

OpenRTM-aist-Java requires communication middleware called CORBA.

In Java, CORBA functionality was originally included as a standard feature. However, starting with Java 9, it was marked as deprecated (a feature scheduled for future removal), and it was completely removed in Java 11 and later.

Therefore, to use OpenRTM-aist-Java, it is necessary to use JDK 8, the Java 8 development environment package.

Although Oracle, the original distributor of JDK 8, has been gradually discontinuing its distribution and support, JDK 8 remains available from several vendors because many users still require Java 8.

This page introduces methods for obtaining and installing JDK 8.

## JDK 8 Distributions

Several JDK 8 distributions that we have identified are listed below.

Please note that this is only a selection of distributions we have found. The omission of any particular distribution is not intentional.

In addition, licensing and support terms vary among vendors. Some distributions may require payment for commercial use or support services. Please review the terms and conditions provided by each vendor before use.

### Oracle

As of November 2019, Oracle, the original developer and distributor of Java, still provides JDK 8 for download.

Oracle appears to provide a free license for personal and development use, while commercial use may require a paid subscription.

For accurate licensing information, please refer to the following links and Oracle's official announcements.

- [Oracle Java SE Subscription](https://www.oracle.com/technetwork/java/javaseproducts/overview/index.html)
  - [JDK 8 Download](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
  - This page may be removed if Oracle discontinues Java 8 distribution.

### OpenJDK

OpenJDK is Oracle's open-source Java implementation and is distributed under GPLv2 with the Classpath Exception.

Most JDK implementations are based on OpenJDK.

- [OpenJDK](http://openjdk.java.net/)

From the following page, locate the section for Java SE 8xxxx (u231 as of November 2019), click the **DOWNLOAD** button for the JDK, and obtain the package appropriate for your platform.

- [OpenJDK 8 Download](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

### AdoptOpenJDK

AdoptOpenJDK is a project sponsored by IBM and maintained by the community that provides OpenJDK builds.

Two JVM implementations are available:

- **HotSpot**, developed by the OpenJDK community
- **OpenJ9**, developed by the Eclipse community

From the link below:

1. Select **OpenJDK 8 (LTS)**.
2. Select either **HotSpot** or **OpenJ9**.
3. Click **Latest Release**.

The appropriate package for your platform should begin downloading automatically.

If you need a package for another platform, click **Other Platforms**.

Installation instructions are available via the **Installation** link.

- [AdoptOpenJDK](https://adoptopenjdk.net/)
  - [AdoptOpenJDK 8 Support](https://adoptopenjdk.net/support.html) (through May 2026)

### Amazon OpenJDK

Amazon Corretto is an OpenJDK distribution that includes long-term support from Amazon.

Visit the website below and click **Download Amazon Corretto 8**.

A list of platform-specific builds will be displayed. Download the installation package appropriate for your platform.

- [Amazon Corretto](https://aws.amazon.com/jp/corretto/)
  - [Amazon OpenJDK 8 Support](https://aws.amazon.com/jp/corretto/faqs/#support) (through June 2026)

## Installation on Linux

### Installing Packages from Repositories

Most major Linux distributions provide OpenJDK packages corresponding to JDK 8 through their standard package repositories.

#### Ubuntu / Debian / Raspberry Pi OS

On Ubuntu, Debian, and similar distributions, JDK 8 can be installed using:

```bash
$ sudo apt install openjdk-8-jdk
````

#### Fedora

On Fedora Linux, JDK 8 can be installed using:

```bash
$ sudo yum -y install java-1.8.0-openjdk
```

### Installing from Sources Other Than Repositories

JDK 8 can also be obtained from the third-party vendors listed above.

Follow the installation instructions provided by the vendor, or use the standard Java installation procedures.

As an example, the following procedure installs the Adoptium (formerly AdoptOpenJDK, now Temurin) package on Raspberry Pi OS Bookworm.

```bash
$ sudo apt install apt-transport-https
$ wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null
$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/trusted.gpg.d/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
$ sudo apt update
$ sudo apt install temurin-8-jdk
```

Verify the installed version:

```bash
$ java -version
openjdk version "1.8.0_402"
OpenJDK Runtime Environment (Temurin)(build 1.8.0_402-b06)
OpenJDK Client VM (Temurin)(build 25.402-b06, mixed mode)
```

### If Another JDK Version Is Already Installed

A version of Java other than JDK 8 may already be installed as the default Java environment.

Verify the current version:

```bash
$ java -version
```

Make sure the reported version begins with **1.8**, indicating JDK 8.

If another version is selected, use:

```bash
$ sudo update-alternatives --config java
```

to choose the JDK 8-based Java environment.

The following example shows the output on Ubuntu 18.04 after installing `openjdk-8-jdk`:

```text
$ sudo update-alternatives --config java

  Selection    Path                                          Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111     auto mode
  1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111     manual mode
  2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081     manual mode

Press <Enter> to keep the current choice [*], or type the selection number: 2

update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java to provide /usr/bin/java (java) in manual mode
```

## Installation on Windows

To install JDK 8 on Windows, download an MSI installer from one of the distribution sites listed above and run it.

For distributions that use installation formats other than MSI, follow the installation instructions provided by the vendor.

After installation, open a Command Prompt and verify the installation in the same way as on Linux:

```cmd
java -version
```

Confirm that the reported Java version corresponds to JDK 8.

