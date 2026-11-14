---
layout: page
title: faq on openrtm-aist (java version) 
---

<!-- Title: OpenRTM-aist (Java版) に関する FAQ -->
#contents(3)

## Common to All OSes

### Data transfer takes time with Java version components
When sending and receiving especially large data (often seen with data of 100 kB or more) between Java version RT components and components in other languages such as C++, the speed may drop drastically. This is known to be a problem on the Java CORBA side, and it can be avoided by setting the timeout appropriately.~
Set the Java CORBA timeout by writing the following in the rtc.conf loaded by the Java version RTC.~
```
 corba.args: -ORBTCPReadTimeouts 1:60000:300:1
```
In Java (JDK 1.5 or later), the default is **100:3000:300:20**, and this means changing it to **1:60000:300:1**. Each item means the following, from left to right:
- The time (ms) for which the Read Thread is suspended when 0 bytes are read while reading CORBA data
- The maximum cumulative time (ms) that the Read Thread waits when reading CORBA data
- The timeout (ms) when reading the GIOP header
- The rate (%) at which the next suspension time is increased when the Read Thread is suspended while reading CORBA data

Therefore, **1:60000:300:1** means:
- When reading returns 0 bytes, suspend the Read Thread for 1 ms
- The maximum cumulative time that the Read Thread waits is 6000 ms
- The timeout when reading the GIOP header is 300 ms
- Increase the Read Thread suspension time by 1% at a time

For large data, the data cannot be read completely in a single read, so reads are normally performed several times.~
Since the next data does not arrive immediately, read returns with the number of read bytes as 0 bytes, but normally the next data arrives within 1 ms. With the default setting, the Read Thread waits 100 ms, but there is no need to wait that long; waiting about 1 ms allows the next data to be read immediately.~
With the default setting, after waiting 100 ms, another read returns 0, so it waits an additional 100 ms + 20%, or 120 ms. If the data is too large, repeating this 12 times reaches the maximum cumulative time of 3000 ms and causes a timeout, and even if the data is small, it takes the number of data fragments × 100 ms, making it extremely slow.~
Since Java CORBA splits data at 100 kB, when exchanging data larger than this, it is recommended to make the above setting in rtc.conf.
<br>
<br>

## Windows

### The name server console screen does not open
"Start Java Naming Service" starts the name server (omniNames.exe) from the batch file located at %RTM_ROOT%\bin\rtm-naming.bat.
At this time, the environment variable OMNI_NAMES is used to refer to omniNames.exe.
Normally, when OpenRTM-aist is installed with the installer, the OMNI_ROOT environment variable is automatically set. However, for some reason the environment variable may become invalid, or if you installed manually, the environment variable may not be set.
<br>
<br>

### Sample components do not start
There is a problem with the rtc.conf settings. Reset the rtc.conf settings as follows and check again.
```
 corba.nameservers: localhost
```
For example, if settings such as corba.endpoint/corba.endpoints do not match the host address of the PC currently running, CORBA will terminate abnormally.
<br>
<br>

### When starting a sample component, it terminates with a runtime error
A runtime error may be displayed because libraries or other components are not installed or configured properly.
This may be improved by restarting the PC or uninstalling all of OpenRTM-aist and reinstalling it.
<br>
<br>

## UNIX

&aname(fedoraNS);
### An error is displayed in the NameService View of RTSystemEditor on FedoraCore
If the OS is FedoraCore, installing Java with yum may install GCJ (The GNU Compiler for Java), and if that GCJ is used, an error may be displayed in the NameService View of RTSystemEditor.~
If an error is displayed, first check whether Oracle Java is being used.~
If you want to use Oracle Java only with Eclipse, download jdk-xxx-linux-i586.bin, execute it, and copy the generated jre directory to the Eclipse installation directory before use.~
```
 $ sh jdk-6u4-linux-i586.bin
 $ cp -r jdk1.6.0_04/jre eclipse/
```
- (It also seems possible to select the Java to use by using JPackage and alternatives.)
<br>
<br>

&aname(javafedora);
### Handling Java installation on FedoraCore 
If the OS is FedoraCore, installing Java with yum may install GCJ (The GNU Compiler for Java), and using that GCJ may cause several problems.~
If problems occur, first check whether Oracle Java is being used.

- References 
  - [Hints for JDK installation]({{ site.baseurl }}/en/doc/installation/install_1_1/java_1_1/tips_jdk#fedora)
  - [A simple method for applying Oracle Java to Eclipse in UNIX-like environments]({{ site.baseurl }}/en/doc/faq/faq_rtp_tools#rtclinksunjava)

