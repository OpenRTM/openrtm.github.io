---
layout: page
title: faq on openrtm-aist (c++ version)
---

<!-- Title: OpenRTM-aist (C++版) に関する FAQ -->
#contents(3)

## Windows

### CMake fails

- Cause 1: The architecture may not match.

The architecture may not match.
For example, even though 32-bit OpenRTM is installed, the compiler may be specified as 64-bit in CMake, so the architecture may not match.
You need to match the architecture before running it.

<br>

- Cause 2: The CMake version may be old.
Install and run the versions of CMake and Visual Studio supported by OpenRTM.
<br>
<br>

### The name server console screen does not open
- Cause 1: omniORB is not installed

The msi installer provided by openrtm.org includes omniORB, but if you installed it manually, omniORB may not be installed, so check whether omniORB is installed.

<br>

- Cause 2: The environment variable OMNI_ROOT is not set
"Start Naming Service" starts the name server (omniNames.exe) from the batch file located at %RTM_ROOT%\bin\rtm-naming.bat. At this time, the environment variable OMNI_NAMES is used to refer to omniNames.exe. 
Normally, when OpenRTM-aist is installed with the installer, the OMNI_ROOT environment variable is automatically set, but for some reason the environment variable may become invalid, or if you installed manually, the environment variable may not be set.

Check that the environment variable OMNI_ROOT is set.<br>
Environment variables can be viewed and edited from:
- [Control Panel] > [System] > [Advanced] tab > [Environment Variables]
- Right-click [My Computer], then [Properties] > [Advanced] tab > [Environment Variables], etc.

Cause 3: If the user name contains double-byte characters, the folder for log output cannot be set properly and omniNames.exe fails to start
This may be improved by setting the environment variable TEMP to a location that does not contain double-byte characters.
Create an appropriate temporary folder (C:\temp in the following case), and set it at the beginning of rtm-naming.bat as follows so that the environment variable TEMP points to it.

```
 set cosnames="omninames"
 set orb="omniORB"
 set port=%1
 rem set OMNIORB_USEHOSTNAME=localhost
 set PATH=%PATH%;%OMNI_ROOT%\bin\x86_win32
 set TEMP=C:\temp
```

Also, in rare cases, it may not be possible to start due to problems with the host name or address settings.
In that case, you need to set the IP address of the PC you are using in omniNames.exe.
Set the environment variable OMNIORB_USEHOSTNAME as follows (the following is an example where the IP address of the local host is 192.168.0.11).

```
 set cosnames="omninames"
 set orb="omniORB"
 set port=%1
 set OMNIORB_USEHOSTNAME=192.168.0.11
 set PATH=%PATH%;%OMNI_ROOT%\bin\x86_win32
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

### When starting a sample component, it terminates with a runtime error
A runtime error may be displayed because libraries or other components are not installed or configured properly.
This may be improved by restarting the PC or uninstalling all of OpenRTM-aist and reinstalling it.
<br>
<br>

&aname(cmakecompilererrro);
### The compiler cannot be found when running CMake

The following error occurs when running CMake.

```
 No CMAKE_CXX_COMPILER could be found. 
```

First, check &lt;project directory&gt;/&lt;build directory&gt;/CMakeFiles/CMakeError.log.

:Cause 1: The wrong compiler was specified

When running (Configure) CMake, you specify the compiler. If you specify a compiler different from the installed Visual Studio, the compiler cannot be found and an error such as **No CMAKE_CXX_COMPILER could be found.** occurs.

Looking at CMakeError.log, an error occurs immediately after the compiler check starts, as shown below.

```
 Microsoft (R) Build Engine バージョン 4.6.1586.0
 [Microsoft .NET Framework、バージョン 4.0.30319.42000]
 Copyright (C) Microsoft Corporation. All rights reserved.
 
 2017/04/08 10:47:04 にビルドを開始しました。
 ノード 1 上のプロジェクト
 "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj"
 (既定のターゲット)。
 C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj(18,3): 
 error MSB4019: 
 インポートされたプロジェクト 
 "C:\Microsoft.Cpp.Default.props" が見つかりませんでした。<Import> 
 宣言のパスが正しいかどうか、およびファイルがディスクに存在しているかどうかを
 確認してください。
 プロジェクト
 "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj"
 (既定のターゲット) のビルドが終了しました -- 失敗。
 
 ビルドに失敗しました。
 
 "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj"
 (既定のターゲット) (1) ->
  C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj(18,3):
 error MSB4019: インポートされたプロジェクト 
 "C:\Microsoft.Cpp.Default.props" が見つかりませんでした。
 <Import> 宣言のパスが正しいかどうか、およびファイルがディスクに存在しているかどうかを
 確認してください。
  
     0 個の警告
     1 エラー
 
 経過時間 00:00:00.50
```

- Solution: Specify the correct compiler.

1. Check the installed OpenRTM
  - → Is it 32-bit or 64-bit? 
1. Check the installed Visual Studio
  - → Visual Studio 2008 (VC9), 2010 (VC10), 2012 (VC11), 2013 (VC12), 2015 (VC14), 2017 (VC15)
1. Delete the CMake cache
  - When changing the compiler specification, you must always delete the cache.
1. Specify the correct compiler in CMake Configure
  - Match 32-bit/64-bit to the installed OpenRTM
    - 32-bit is without suffix (example: Visual Studio 10 2010)
    - 64-bit is Win64 (example: Visual Studio 10 2010 Win64)

<br>

- Cause 2: Visual C++ is not installed
When installing Visual Studio, Visual C++, including the C++ compiler, may not have been installed.

- Solution: Install Visual C++
Start the installer again (download it first if you do not have it on hand), and perform installation from [Change].
Select Customize installation and confirm that Visual C++ is included in the items to be installed before installing.

In this case as well, the output content of CMakeError.log is the same as (Cause 1).


- Cause 3: rc.exe cannot be executed
In rare cases, even though the installed compiler is correctly specified when running CMake, an error such as **No CMAKE_CXX_COMPILER could be found.** may occur.
One possible cause is that when multiple versions of Visual Studio have been installed and uninstalled, inconsistencies may rarely occur in the toolchain settings, resulting in an error such as **rc.exe cannot be executed** as shown below.

```
 C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\CL.exe
 /c /nologo /W0 /WX- /Od /D _MBCS /Gm- /EHsc /RTC1
 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc140.pdb"
 /Gd /TC /errorReport:queue CMakeCCompilerId.c
   CMakeCCompilerId.c
 Link:
 C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe
 /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO
 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib
 shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST
 /MANIFESTUAC:"level='asInvoker' uiAccess='false'"
 /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE /TLBID:1
 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib"
 /MACHINE:X64 Debug\CMakeCCompilerId.obj
 LINK : fatal error LNK1158: 'rc.exe' を実行できません。
 [C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj]
 プロジェクト "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj"
 (既定のターゲット) のビルドが終了しました -- 失敗。
 
 ビルドに失敗しました。
```


- Solution: Copy rc.exe and rcdll.dll
A workaround for this is to copy rc.exe and rcdll.dll to the tool directory of the target compiler.

1. Find rc.exe and rcdll.dll
  - Open Explorer, open **C:\Program Files** (or **C:\Program Files (x86)**), and search for rc.exe. rcdll.dll should be in the same directory, so you only need to search for rc.exe.
  - Normally, several rc.exe files are found under **C:\Program Files (x86)\Windows Kits**, but the one under the x86 directory is the target.
  - In the search results, right-click the target rc.exe and select **"Open file location"**
1. Open the compiler tool directory
  - Open another Explorer window and open the tool's bin directory
  - In the example log above, from **C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe**, you can see that the tool directory is **C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin** (the bin directory is the target; x86?amd64 can be ignored).
1. Copy rc.exe and rcdll.dll
  - Copy rc.exe and rcdll.dll from the Explorer window opened in step 1 to the tool directory opened in step 2
<br>
<br>

<br>

### An error saying xxx.dll does not exist is displayed when running OpenRTP
- Cause 1:
  - This may be a phenomenon that occurs only on Windows 10.
  - RTM_VC_VERSION may not be correctly set in the environment variables.

- Solution:
After installing OpenRTM, restart the PC and check whether RTM_VC_VERSION is correctly set in the environment variables.
<br>
<br>

&aname(errorapplication);
### "This application has failed to start because the application configuration is incorrect. ..." is displayed
When trying to start a sample RT component or similar by executing xxxComp.exe, an error like the above may appear.
This error occurs because the VC++ library runtime components are not present in the execution environment.
OpenRTM-aist (C++ version) cannot run in an environment where VC++-related development environments (Microsoft Visual Studio, Visual C++ Express, etc.) are not installed, so be sure to install a VC++-related development environment.~
<br>
<br>

&aname(errorinit);
### The application error "The application failed to initialize properly. ..." is displayed
When trying to start the name server by executing rtm-naming.bat, an error like the above may appear.
This error occurs because the VC++ library runtime components are not present in the execution environment.
OpenRTM-aist (C++ version) cannot run in an environment where VC++-related development environments (Microsoft Visual Studio, Visual C++ Express, etc.) are not installed, so be sure to install a VC++-related development environment.
<br>
<br>

#### VC++-related libraries are not installed
Install an application such as Visual Studio.
<br>
<br>

### An application error occurs when executing rtm-naming.bat
VC++-related libraries may not be installed, so install them.
<br>
<br>

### rtm-naming cannot be executed
Even if rtm-naming.bat is executed, a black window (Command Prompt screen) opens for a moment and then closes.

- Cause 1: omniORB is not installed
  - Solution: Download and install omniORB from the download page.<br>
Normally, rtm-naming.bat executes the omniORB name server **omniNames.exe**.~
If omniORB is not installed, **omniNames.exe** is not installed either, so the name server cannot be executed.~
<br>
- Cause 2: The log directory path contains double-byte characters
  - Solution: Normally, rtm-naming.bat executes the omniORB name server **omniNames.exe** as follows.~
```
 omniNames.exe -start 2809 -logdir %TEMP%
```

Normally, the environment variable %TEMP% points to the user's temporary directory:
```
 C:\Documents and Settings\ユーザー名\Local Settings\Temp
```

Here, if the **user name** is Japanese, omniNames cannot correctly create the log file, so it terminates without running.~
The following three countermeasures are possible.
- Do not use a Japanese user name
  - Create a new user that does not use Japanese and run it in that environment.
- Rewrite rtm-naming.bat
  - Rewrite the following part in rtm-naming.bat under **C**:\Program Files\OpenRTM-aist\[version number]\bin** ~

```
 %cosnames% -start %port% -logdir %TEMP%\ 
```
as follows:~
```
 %cosnames% -start %port% -logdir [log directory whose path does not contain Japanese]
```
~
The **log directory whose path does not contain Japanese** should be a safe directory where you have write permission. For example, C:\tmp.

- Use the Java version of orbd
  - When you install the Java version of OpenRTM-aist and the JDK, **start-orbd.vbs** appears in the examples of the Java version in the Start menu. This is a script that starts the CORBA name server included with the JDK.~
This name server does not have the Japanese path problem that omniNames has, so by using it, the name server can be started even if the user name is Japanese.
<br>

## UNIX
### configure was executed, but it exits with an error
Most configure errors occur when required packages cannot be found. If an error occurs, check whether the required packages are installed and whether the headers and libraries are installed in directories that autoconf can find.
<br>
<br>

### The build does not complete even after running make, or an error is displayed when running make 
The package installation or the build of OpenRTM-aist (C++ version) may be incomplete. Start the automatic package installer again and redo the process from package installation.
If any error message is displayed on the processing screen during package installation, manually install only the relevant package and then run configure.
After confirming that no error message is displayed when running configure, run make again to complete the build.
<br>
<br>

### The run.sh script for executing the sample program SimpleIO cannot be executed
The execute bit may not be set on run.sh. Set the execute bit and run it as shown below, or pass it directly to the shell and execute it.~
```
 > ls -al run.sh
 -rw-r--r--  1 n-ando  n-ando  1146  4 27 15:12 run.sh
 > chmod 755 run.sh
 > ./run.sh
```
or
```
 > sh run.sh
```
<br>
<br>

### The sample program SimpleIO was started, but it does not work properly
The SimpleIO execution script run.sh assumes that the terminal window is one of kterm, xterm, or gnome-terminal.
Therefore, if you are using a terminal window other than these, edit run.sh as appropriate before running it.~
<br>
