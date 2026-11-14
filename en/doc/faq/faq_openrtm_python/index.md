---
layout: page
title: faq on openrtm-aist (python version)
---

<!-- Title: OpenRTM-aist (Python版) に関する FAQ -->
#contents(3)

## Windows

### The name server console screen does not open
- Cause 1: omniORBpy is not installed
The msi installer provided by openrtm.org includes omniORBpy, but if you installed it manually, omniORBpy may not be installed, so check whether omniORBpy is installed.

<br>

- Cause 2: The association of py files is different
The file that starts the name server is C:\Program Files (x86)\OpenRTM-aist\1.1\bin\rtm-naming.py. (When installed with the 32-bit version msi)<br>
If you open a console screen in this directory and execute python rtm-naming.py, the name server starts, but if it cannot be started by double-clicking rtm-naming.py, check the installed python.<br>
If both the 32-bit and 64-bit versions of Python are installed, it seems that the one installed first is associated with py files, so installing Python with the same architecture as the OpenRTM-aist-Python installer first may solve the problem.

<br>

- Cause 3: It cannot be started due to a problem with the host name or address settings
You need to set the IP address of the PC you are using in omniNames.exe.
Set the environment variable OMNIORB_USEHOSTNAME as follows (the following is an example where the IP address of the local host is 192.168.0.11).

```
 変数名(N): OMNIORB_USEHOSTNAME
 変数値(V): 192.168.0.11
```

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

&aname(pythonusage);
### When rtm-naming.py is executed, omniNames displays "usage:"  
**Symptom: When rtm-naming.py is executed from a directory containing spaces, such as "C**: \Documents and Settings\Hoge\My Documents", omniNames displays "usage:" and exits.

:Solution: If the above symptom occurs, use one of the following methods to deal with it.

**Solution 1:** Create an appropriate folder such as "RTMNaming" directly under C:\ (or in a location where the path name does not contain spaces), and execute rtm-naming.py.

**Solution 2:** Edit line 48 of rtm-naming.py in C:\Python<version>\Lib\site-packages\OpenRTM\rtm-naming as follows.~

```
 rtm-naming.py 48行目
  cmd = "omniNames -start "+str(port)+" -logdir \""+str(currdir)+"\" &"
```
<br>
<br>

&aname(pythonexe);
### python.exe does not start  
Add the Python installation folder to the environment variable Path (such as C:\Python26).
<br>
<br>
&aname(python);
### In an environment where Cygwin is installed, multiple python.exe files may exist 
In an environment where Cygwin is installed, python.exe may also exist on Cygwin. In that case, the search path to python.exe on Cygwin is usually set to take precedence, so even if the environment variable Path is set properly, a version of python.exe different from the Python that should have been installed this time (that is, the one on Cygwin) may start. In this case, problems due to differences in Python versions will occur. A characteristic of this problem is that it is very difficult to identify the cause. When using the Python version of OpenRTM-aist in an environment where Cygwin or similar software is installed, make sure that python.exe is being started from the Python installation folder of the relevant version.

**Example confirmation methods:** Check the version with "python -V"; in an environment with Cygwin, check which python.exe is being executed with which python; etc.

**Action when this problem is found:** It can be solved by adding the Python installation folder (such as C:\Python26) to the **beginning** of the **system environment variable Path** (not the *user environment variable Path*).
<br>
<br>

&aname(MSVCerror);
### It exits with the error "MSVCP71.dll was not found, ..." 
This error occurs because msvcp71.dll is not in the WINDOWS\system32 folder. Obtain msvcp71.dll from [here ](http://www.vector.co.jp/soft/win95/util/se435079.html).
<br>
<br>

&aname(rtc.conf);
### "Can't open file: ./rtc.conf" or similar is displayed
:Symptom: rtc.conf cannot be found in the startup folder of the RT component (or on the search path), so it cannot be started.
In this case, the following is displayed.
```
 Can't open file: ./rtc.conf
 Can't open file: /etc/rtc.conf
 Can't open file: /etc/rtc/rtc.conf
 Can't open file: /usr/local/etc/rtc.conf
 Can't open file: /usr/local/etc/rtc/rtc.conf
```
This is because the search path for rtc.conf is in the default state, and it was searched in the order above but could not be found, so this display appears.

:Solution:
To avoid this, create a file named rtc.conf with content such as the following:~
```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```
and place it on the above search path (usually the current folder, that is, the same folder as the component).
<br>
<br>

### The component is not registered with the name service
:Cause: The line break code of rtc.conf may be CRLF.
Check rtc.conf with the following command, and if the string CRLF is displayed, create rtc.conf again.
```
 $ file rtc.conf
```
<br>
