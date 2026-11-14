---
layout: page
title: faq on installation
---

<!-- Title:  インストールに関する FAQ -->
#contents
#clear

## Windows

### The version number is not displayed even after installing Python on Windows
Even if you install a Python version supported by OpenRTM-aist and add the Python path at that time, the version number may not be displayed when you check it from the Command Prompt.

```
 >python --version
 Python
```

**Cause:**
- A version downloaded from the Microsoft Store or similar may already be installed
- Check the installation location with the where python command
```
 >where python
```

**Solution:**
- Check Python's app execution aliases, and if they are turned on, turn them off and restart Windows
- In Windows Settings → Apps & features → App execution aliases, turn off "pytnon.exe" and "python3.exe"


After restarting, confirm that the Python version number is displayed in the Command Prompt.
For the procedure for adding the path when installing Python, see the explanation on the following page. <br>
[Let's Start OpenRTM-aist in 10 Minutes!・Installing Python](/en/doc/installation/lets_start#toc1) 


<br>
<br>

### A warning appears from Windows Defender
When trying to start the name server or sample components, the Windows Defender Firewall may display the [Windows Security Alert] dialog.
<br>
<br>
**Solution:**
Check [Private networks (home or work networks) (R)], uncheck [Public networks (airports, coffee shops, etc.) (not recommended) (U)], and click [Allow access (A)].
<br>
<br>

### OpenRTM-aist 1.1.2 was installed on Windows 10, but it was not added to PATH
**Cause:**
- This may be a phenomenon that occurs only on Windows 10.
- If the PATH setting is long, it may be truncated due to the length limit.


**Solution:**
Restart the PC after installation.
<br>
<br>

### The omniORB PATH setting is not expanded on Windows 10

When checking the set command on Windows 10, the variable part %OMNI_ROOT% of the omniORB PATH setting was not expanded.
<br>
<br>
**Cause:**
- This may be a phenomenon that occurs only on Windows 10.
- The PATH may not have been expanded.


**Solution:**
Restart the PC after installation.
<br>
<br>

### Eclipse cannot be started
JRE may not be installed, so install the supported version of JRE.
<br>
<br>


## UNIX

### A download error is displayed during automatic package installation 
The automatic installer included with OpenRTM-aist checks for the presence and version of packages, and if an appropriate package is not installed, it downloads and processes each package from its download site.
For this reason, when installing with the automatic installer, be sure to connect the computer to the Internet.~
If a download error occurs even though the network connection is normal, the download may have failed due to line congestion or similar reasons, or the file location or name may have changed on the download site side.
In the former case, try running the automatic installer again at a different time of day. In the latter case, find the relevant package and download and install it manually, or correct the download source address in the automatic installer and then start it again.~
<br>
<br>

&aname(openrtminstfault);
### OpenRTM-aist installation fails 
If an old version of OpenRTM-aist has not been completely uninstalled, a new version cannot be installed. Uninstall the old version once, and then perform the installation again.
#### Common to Fedora, Ubuntu, and Debian:
Uninstall using pkg_install_XXXX.sh.~

```
 >su
 #pkg_install_XXXX.sh -u
```

You will be asked for permission to uninstall, so complete the process while entering **"y"**.
Alternatively, follow the steps below.

#### Fedora:
Uninstall using the yum command. Perform the uninstall using the following procedure.~

```
 >su

 #yum remove OpenRTM-aist-example
 #yum remove OpenRTM-aist-dev
 #yum remove OpenRTM-aist-doc
 #yum remove OpenRTM-aist
```
#### Ubuntu / Debian:
Uninstall using the apt-get command. Perform the uninstall using the following procedure.~
```
 >su

 #apt-get remove OpenRTM-aist-example
 #apt-get remove OpenRTM-aist-dev
 #apt-get remove OpenRTM-aist-doc
 #apt-get remove OpenRTM-aist
```
<br>
<br>

&aname(notusecd);
### A CD is requested when performing installation using apt-get or similar 
In distributions such as Ubuntu and Debian, when performing installation using apt-get, pkg_install_ubuntu.sh, or pkg_install_debian.sh, you may be asked for a CD as follows.
Media change:~
```
 　　'Ubuntu 7.10 _Gutsy Gibbon_ Japanese Remix - Release i386 (20071018)'
```

Please insert the disk labeled as above into the drive '/cdrom/' and press Enter.~
Of course, preparing the CD is one solution, but the following describes what to do if you cannot prepare it for various reasons.~
In this case, first enter **C-c** (Ctrl+c) to interrupt the installation process, and then redo the installation process using the following procedure.

:1. Edit **/etc/apt/sources.list**

At the beginning of **/etc/apt/sources.list**, there is a line such as~
```
 deb cdrom:[Ubuntu 7.10 _Gutsy Gibbon_ Japanese Remix - Release i386 (20071018)]/ gutsy main restricted
```

or~
```
 deb cdrom:[Debian GNU/Linux 4.0 r3 _Etch_ - Official i386 NETINST Binary-1 20080218-14:15]/ etch contrib main
```

Insert the **#** character at the beginning of the corresponding line and comment it out.~
```
 #deb cdrom:[Ubuntu 7.10 _Gutsy Gibbon_ Japanese Remix - Release i386 (20071018)]/ gutsy main restricted
```

or~
```
 #deb cdrom:[Debian GNU/Linux 4.0 r3 _Etch_ - Official i386 NETINST Binary-1 20080218-14:15]/ etch contrib main
```

:2. Redo the installation process
Redo the installation process that was interrupted earlier from the beginning.
<br>

