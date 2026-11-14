---
layout: page
title: creating an msi with cpack (windows)
---
<!-- Title: CPack で msi 作成（Windows） -->
#contents(4)

## Introduction

The msi installer is created by building with Visual Studio.<br>

## Creation Procedure When Not Including doxygen Documentation
* By default, the documentation build is OFF, so it is not generated.

From Solution Explorer in Visual Studio, right-click "PACKAGE", select "Build", and execute it.
<br>
<div align="center"><a href="doxygenoff1-1.png"><img src="doxygenoff1-1.png" width="50%;"></a></div>

<br>

## Creation Procedure When Including doxygen Documentation
Change the following line in CMakeLists.txt directly under the project folder from OFF to ON.<br>
For a C++ RTC, this is around line 86, and for a Python RTC, around line 77.

```
 option(BUILD_DOCUMENTATION "Build the documentation" ON) ※この行の OFF を ON に書き換えます。(デフォルトは OFF)
```

1. From Solution Explorer in Visual Studio, right-click "doc", select "Build", and execute it.<br>
<br>
<div align="center"><a href="doxygenon1-1.png"><img src="doxygenon1-1.png" width="50%;"></a></div>
<br>
1. After the build of "doc" is complete, right-click "PACKAGE" and select "Build".<br>
<br>

<div align="center"><a href="doxygenon1-2.png"><img src="doxygenon1-2.png" width="50%;"></a></div>
<br>

[Notes]
- Confirm that "BUILD_DOCUMENTATION" is checked in CMake configure.
- Build "doc" first, and then build "PACKAGE". If you build "PACKAGE" without building "doc", an error will occur.

## msi Installer Storage Location and File Name
If it is created successfully, it will be saved in [build] under the project directory.<br>
The file name will be "RTC project name + RTC version number_OpenRTM-aist version number_architecture".<br><br>
(Example) Flip100_rtm120_win64.msi<br>
* The architecture will be [win32] or [win64].<br>
　The version number is in a format with dots removed; [1.0.0] becomes [100].

## Installing and Uninstalling an msi
### Installation
1. Double-click the created msi installer.<br>
<br>
1. Click [Next].<br>
<br>
<div align="center"><a href="msi_install1-1.png"><img src="msi_install1-1.png" width="50%;"></a></div>
<br>
1. Check [I accept the license agreement] and click [Next].<br>
<br>
<div align="center"><a href="msi_install2-1.png"><img src="msi_install2-1.png" width="50%;"></a></div>
<br>
1. Click [Next].<br>
The default installation path is as follows.<br>
(Example) C:\Program Files\OpenRTM-aist\1.2.0\Components\c++\ImageProcessing\<br>
* ImageProcessing is the name specified in "Module Category" in RTCBuilder.<br>
<br>
<div align="center"><a href="msi_install3-1.png"><img src="msi_install3-1.png" width="50%;"></a></div>
<br>
1. Click [Install] to start the installation.<br>
<br>
<div align="center"><a href="msi_install4-1.png"><img src="msi_install4-1.png" width="50%;"></a></div>
<br>
<div align="center"><a href="msi_install4-2.png"><img src="msi_install4-2.png" width="50%;"></a></div>
<br>
1. Click [Finish] to exit the installer. After installation, it will be registered in the Start menu.<br>
<br>
<div align="center"><a href="msi_install5-1.png"><img src="msi_install5-1.png" width="50%;"></a></div>
<br>

### GUID Settings for Upgrades
When upgrading, it is necessary to set a GUID in order to check the version that is already installed.
Because the GUID is not set by default, a new GUID is assigned every time PACKAGE is built in Visual Studio.
By setting the GUID in advance, it is possible to determine whether it is an upgrade or a new installation.<br>
The procedure for setting the GUID is shown below.<br><br>
1. From Solution Explorer in Visual Studio, right-click "PACKAGE", select "Build", and execute it.<br>
<br>
<div align="center"><a href="msi_upgrade1-1.png.png"><img src="msi_upgrade1-1.png" width="50%;"></a></div>
<br>
1. When the build is complete, the GUID will be displayed in the output screen below. Select it and copy it.<br>
<br>
<div align="center"><a href="msi_upgrade2-1.png"><img src="msi_upgrade2-1.png" width="50%;"></a></div>
<br>
1. From Solution Explorer, expand "ALL_BILD" and click CMakeLists.txt.<br>
<br>
<div align="center"><a href="msi_upgrade3-1.png"><img src="msi_upgrade3-1.png" width="50%;"></a></div>
<br>
1. Paste the GUID copied in step 2 as shown in the following screen, and overwrite-save CMakeLists.txt.<br>
<br>
<div align="center"><a href="msi_upgrade4-1.png"><img src="msi_upgrade4-1.png" width="50%;"></a></div>
<br>
1. Again, from Solution Explorer, right-click "PACKAGE", select "Build", and execute it.<br>
<br>
<div align="center"><a href="msi_upgrade5-1.png"><img src="msi_upgrade5-1.png" width="50%;"></a></div>
<br>

[Supplement]<br>
In addition to the above, there is also a method of creating a new GUID.<br>
From the Visual Studio menu, select [Tools] > [Create GUID] to display the "Create GUID" dialog.<br>
<br>
1. In [GUID format], select [4. Registry Format...].<br>
1. Click the [New GUID] button.<br>
1. Click the [Copy] button.<br>
1. Click the [Exit] button to close the dialog.<br>
<br>
<div align="center"><a href="msi_upgrade6-1.png"><img src="msi_upgrade6-1.png" width="50%;"></a></div>
<br>
1. Paste it into CMakeLists.txt as shown in the following screen and overwrite-save it. * Paste only the numbers.<br>
<br>
<div align="center"><a href="msi_upgrade4-1.png"><img src="msi_upgrade4-1.png" width="50%;"></a></div>
<br>

### Uninstallation
The uninstallation procedure is as follows.
#### How to Remove from Control Panel
1. Open [Control Panel] and click [Uninstall a program].<br>
<br>
<div align="center"><a href="msi_uninstall0-1.png"><img src="msi_uninstall0-1.png" width="50%;"></a></div>
<br>
1. Select the installed package name and click [Uninstall].<br>
<br>
<div align="center"><a href="msi_uninstall0-2.png"><img src="msi_uninstall0-2.png" width="50%;"></a></div>
<br>
1. If the display has disappeared from the list in Control Panel, uninstallation is complete.<br><br>
#### How to Remove from the Installer
1. Double-click the created msi installer.<br><br>
1. Click [Remove].<br>
<br>
<div align="center"><a href="msi_uninstall1-1.png"><img src="msi_uninstall1-1.png" width="50%;"></a></div>
<br>
1. Click [Remove].<br>
<br>
<div align="center"><a href="msi_uninstall2-1.png"><img src="msi_uninstall2-1.png" width="50%;"></a></div>
<br>
<div align="center"><a href="msi_uninstall2-2.png"><img src="msi_uninstall2-2.png" width="50%;"></a></div>
<br>
1. Click [Finish] to exit the installer.<br>
<br>
<div align="center"><a href="msi_uninstall3-1.png"><img src="msi_uninstall3-1.png" width="50%;"></a></div>
<br>

## IDL Compilation Processing for Python RTCs with Service Ports
Python RTCs with service ports execute IDL compilation when the package is installed.
This behavior is implemented by idlcompile.bat and delete.bat in the project folder during IDL compilation execution, so be careful not to delete these files, as the function will stop working.<br>
By uninstalling from Control Panel, files generated after IDL compilation execution will also be deleted.

The following is a list of files installed by the msi installer. Files marked with ★ are generated by IDL compilation.

```
 tree /f インストールディレクトリー\OpenRTM-aist\1.2.0\Components\Python\Category\FlipGUI
 C:\インストールディレクトリー\OpenRTM-aist\1.2.0\Components\Python\Category\FlipGUI
 │  BasicDataType_idl.py ★
 │  CalibrationService_idl.py ★
 │  delete.bat
 │  ExtendedDataTypes_idl.py ★
 │  idlcompile.bat
 │  InterfaceDataTypes_idl.py ★
 │  RTC.xml
 │  rtutil.py
 │  setup.py
 │  flipgui.py
 │  FlipGUIComp.py
 │
 ├─idl
 │   BasicDataType.idl
 │   CalibrationService.idl
 │   CMakeLists.txt
 │   ExtendedDataTypes.idl
 │   InterfaceDataTypes.idl
 │
 ├─ImageCalibService ★
 │   __init__.py ★
 │
 ├─ImageCalibService__POA ★
 │   __init__.py ★
 │
 ├─RTC ★
 │   __init__.py ★
 │
 └─RTC__POA ★
       __init__.py ★
```
