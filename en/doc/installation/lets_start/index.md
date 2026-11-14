---
layout: page
title: getting started with openrtm-aist in 10 minutes!
---

<!-- Title: OpenRTM-aistを10分で始めよう！ -->
#contents

The latest version, OpenRTM-aist-2.1.0-RELEASE, installs the C++ edition, Python edition, Java edition, OpenRTP, and rtshell.

# Preparation

## Installing Python

If Python is not installed, OpenRTM-aist cannot be installed.
Please install Python before installing OpenRTM-aist. Supported versions are
"3.14", "3.13", "3.12", "3.11", and "3.10".

For downloading Python, see [Installing OpenRTM-aist 2.1 on Windows](/en/doc/installation/install_2_1/install_windows_2_1/install_2_1).

The Python installation location supports the [Customize installation] option during installation.

Configure the search path automatically using the following method. This adds the directory containing python.exe and the Scripts directory to the Path.<br> (Example: Path=C:\Python313;C:\Python313\Scripts;...)

**[Installation Procedure]**

- Launch the Python installer. Version 3.13 is used as an example here.
- Check [add python *** to PATH] at the bottom of the first screen, then select [Customize installation].

<div align="center"><a href="py313_install_1.png"><img src="py313_install_1.png" width="70%;"></a></div>

- No changes are required on the [Optional Features] screen. Select [Next] to continue.

<div align="center"><a href="py313_install_2.png"><img src="py313_install_2.png" width="70%;"></a></div>

- On the [Advanced Options] screen, check [Install for all users], and specify the installation destination in [Customize install location]. (Example: Path=C:\Python313;C:\Python313\Scripts;...)

<div align="center"><a href="py313_install_3.png"><img src="py313_install_3.png" width="70%;"></a></div>

- Select [Install] to complete the installation.

## Downloading OpenRTM-aist

For downloading the installer, see [Download]({{ site.baseurl }}/en/download).

If you are using Microsoft Edge and cannot download because the following message appears, follow the procedure below.

<div align="center"><a href="edge-download-01.png"><img src="edge-download-01.png" width="70%;"></a></div>

- Click the "..." displayed when you hover the mouse cursor over the item.

<div align="center"><a href="edge-download-02.png"><img src="edge-download-02.png" width="70%;"></a></div>

- Click "Keep".

<div align="center"><a href="edge-download-03.png"><img src="edge-download-03.png" width="60%;"></a></div>

- Click the "✓" (check mark) next to "Delete", then click "Keep anyway" from the displayed menu.

<div align="center"><a href="edge-download-04.png"><img src="edge-download-04.png" width="50%;"></a></div>

- The download is now complete. Click "Open file" to start the installer.

## Installing OpenRTM-aist

**[Installation Procedure]**

1. Launch the installer and click [Next].
<div align="center"><a href="RTM210_msi_1.png"><img src="RTM210_msi_1.png" width="90%;"></a></div>
<br>

1. This is the license agreement page. Accept the software license terms and click [Next].
<div align="center"><a href="RTM210_msi_2.png"><img src="RTM210_msi_2.png" width="90%;"></a></div>
<br>

1. Select the installation type. Click [Next] with the default settings.
<div align="center"><a href="RTM210_msi_3.png"><img src="RTM210_msi_3.png" width="90%;"></a></div>
<br>

1. Select the setup type.
Click [Typical] to install all features.
<br>
<div align="center"><a href="RTM210_msi_4.png"><img src="RTM210_msi_4.png" width="90%;"></a></div>
<br>

1. Installation is complete. Click [Finish] to exit the installer.
<div align="center"><a href="RTM210_msi_5.png"><img src="RTM210_msi_5.png" width="90%;"></a></div>
<br>

<!-- ※使用しているVisual Studio のバージョンが2019(vc14)以外の場合は、以下のページを
参考に環境変数のRTM_VC_VERSIONを変更してください。&br; -->
<!-- [[RTM_VC_VERSIONの変更:/ja/node/6136/]] -->

## Checking System Environment Variables

We have confirmed cases where nested environment variables are not expanded recursively, but this can be resolved using the VerChanger tool. For details, see the following page.

- [Checking System Environment Variables](/en/doc/installation/install_2_1/install_win_2_1/install_2_1#toc9)

## Running Sample Components

This section explains how to verify the connection operation between two RTCs using the RTSystemEditor feature of OpenRTP.

&aname(openrtp_start);

### Starting OpenRTP

- Launch it by clicking the desktop shortcut.

<div align="center"><a href="OpenRTP210-001.png"><img src="OpenRTP210-001.png" width="70%;"></a></div>
<div align="center"><strong>Starting OpenRTP</strong></div>

- Specify any appropriate location for the workspace.

<div align="center"><a href="OpenRTP122-001.png"><img src="OpenRTP122-001.png" width="70%;"></a></div>
<div align="center"><strong>Selecting a Workspace</strong></div>
<br>

- The "Welcome" screen is not needed, so click the [×] button on the [Welcome] tab in the upper-left corner to close the screen.

<div align="center"><a href="OpenRTP122-002.png"><img src="OpenRTP122-002.png" width="70%;"></a></div>
<div align="center"><strong>Screen at Initial Startup</strong></div>
<br>

### Using RTSystemEditor

- Click [Open Perspective] in the upper-right corner of the screen. In the dialog that appears, select [RT System Editor] and click [Open] to start RTSystemEditor.

<div align="center"><div align="center"><a href="OpenRTP122-003.png"><img src="OpenRTP122-003.png" width="70%;"></a></div>;  <div align="center"><a href="OpenRTP122-004.png"><img src="OpenRTP122-004.png" width="70%;"></a></div>;</div>
<div align="center"><strong>Switching Perspectives</strong></div>
<br>

- Only during the first startup, a dialog saying "Failed to start the toolbar." will be displayed. Follow the instructions to exit OpenRTP and start it again.

<div align="center"><a href="OpenRTP210-002.png"><img src="OpenRTP210-002.png" width="70%;"></a></div>
<div align="center"><strong>Restart OpenRTP</strong></div>

- Press the Name Service startup button to start the localhost name server.

<div align="center"><div align="center"><a href="OpenRTP210-003.png"><img src="OpenRTP210-003.png" width="70%;"></a></div>;  <div align="center"><a href="OpenRTP210-004.png"><img src="OpenRTP210-004.png" width="70%;"></a></div>;</div>

### Starting C++ ConsoleIn and ConsoleOut

- Enter "c++_e" in lowercase in the Windows search box. When the C++_Examples candidate appears, click it.

<div align="center"><a href="menu-c++RTC_001.png"><img src="menu-c++RTC_001.png" width="70%;"></a></div>
<div align="center"><strong>Select C++_Examples</strong></div>

- A list of C++ sample RTCs will be displayed. Double-click ConsoleIn and ConsoleOut to start them.

<div align="center"><a href="menu-c++RTC_002.png"><img src="menu-c++RTC_002.png" width="20%;"></a></div>
<div align="center"><strong>Start ConsoleIn and ConsoleOut</strong></div>

<br>

- After startup, console windows similar to the following will be displayed.

<!-- CENTER:&ref(ConsoleIn001.png,center,90%);&ref(ConsoleOut001.png,center,90%); -->

<div align="center"><div align="center"><a href="ConsoleInOut122-001.png"><img src="ConsoleInOut122-001.png" width="90%;"></a></div>;</div>
<div align="center"><strong>ConsoleIn.bat and ConsoleOut.bat</strong></div>
<br>

- Click [Open New System Editor] from the toolbar to display the [System Diagram].

<div align="center"><a href="OpenRTP122-008.png"><img src="OpenRTP122-008.png" width="70%;"></a></div>
<div align="center"><strong>Display the System Diagram</strong></div>
<br>

- Drag and drop the ConsoleIn and ConsoleOut components from [NameServiceView] onto the [System Diagram]. They will be displayed as shown below.

<div align="center"><a href="OpenRTP122-009.png"><img src="OpenRTP122-009.png" width="70%;"></a></div>
<div align="center"><strong>Drag and Drop Components</strong></div>
<br>

- Connect the components by dragging and dropping between the data ports. After that, a dialog prompting for the information required for the connection will appear. Click [OK].

<div align="center"><div align="center"><a href="OpenRTP122-010.png"><img src="OpenRTP122-010.png" width="70%;"></a></div>;  <div align="center"><a href="OpenRTP122-011.png"><img src="OpenRTP122-011.png" width="70%;"></a></div>;</div>
<div align="center"><strong>Connecting Components</strong></div>
<br>

- The components will be connected as shown in the image below.

<div align="center"><a href="OpenRTP122-012.png"><img src="OpenRTP122-012.png" width="70%;"></a></div>
<div align="center"><strong>Connection Complete</strong></div>
<br>

- Change the component state to Active. Click [All Activate]. If the component color changes from blue to light green, the operation is successful. Components can also be activated individually by selecting them and right-clicking. (If [All Activate] is not displayed, try restarting OpenRTP. Alternatively, you may activate the components individually.)

<div align="center"><a href="OpenRTP122-013.png"><img src="OpenRTP122-013.png" width="70%;"></a></div>
<br>

<div align="center"><a href="OpenRTP122-014.png"><img src="OpenRTP122-014.png" width="70%;"></a></div>
<div align="center"><strong>Activation Complete</strong></div>
<br>


### Verifying Operation in the Component Console Windows

- Next, verify operation in the console windows. After connecting the components in RTSystemEditor, "Please input number:" is displayed in the ConsoleIn window.

<div align="center"><a href="Console122-001.png"><img src="Console122-001.png" width="70%;"></a></div>
<div align="center"><strong>"Please input number:" Displayed</strong></div>
<br>

- Enter any numeric value in the ConsoleIn window and press [Enter]. The value is displayed in the ConsoleOut window.

<div align="center"><div align="center"><a href="Console122-002.png"><img src="Console122-002.png" width="90%;"></a></div>;</div>
<div align="center"><strong>Operation Verification</strong></div>
<br>

  - Entering non-numeric values or excessively large values may cause abnormal behavior. In that case, stop the batch file using the Ctrl-C key and restart from launching the batch files again.

- To terminate the components, click [All Deactivate] from the toolbar. Then right-click the components and select [Exit].

  - If deactivation takes a long time, ConsoleIn is waiting for numeric input. In that case, enter any numeric value.

<div align="center"><a href="Console122-004.png"><img src="Console122-004.png" width="70%;"></a></div>
<div align="center"><strong>Deactivating Components</strong></div>
<br>

<div align="center"><a href="Console122-005.png"><img src="Console122-005.png" width="70%;"></a></div>
<div align="center"><strong>Terminating Components</strong></div>
<br>

- This completes the operation verification using ConsoleIn and ConsoleOut.

## Using rtshell

rtshell is installed by default with OpenRTM-aist.

By using rtshell, you can activate, deactivate, and terminate RTCs from the command line.<br>

See [Installing and Verifying rtshell Operation (Windows Edition)](/en/doc/installation/install_rtshell/check_windows).

## Next...

Please refer to the links below.

- **Try running more samples　　　&t;：　**[Sample Components]({{ site.baseurl }}/en/doc/installation/sample_components)
- **Try creating a component　　　&t;：　**[Case Study]({{ site.baseurl }}/en/doc/casestudy)
- **Learn OpenRTM from the basics　&t;：　**[Developer's Guide]({{ site.baseurl }}/en/doc/developersguide)
- **Join the community　　　　　&t;：　**[Community]({{ site.baseurl }}/en/community)
- **Browse published components　&t;：　**[Projects](/ja/node/123)(No corresponding English project page available.)
