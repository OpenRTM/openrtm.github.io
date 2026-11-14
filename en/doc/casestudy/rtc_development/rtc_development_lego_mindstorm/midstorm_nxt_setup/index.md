---
layout: page
title: mindstorm nxt setup
---
<!-- Title: Mindstorm NXT 設定 -->
#contents

Before turning NXT into an RTC, first configure NXT and the PC.
The PC and NXT can be connected via USB or Bluetooth, but since NXT runs on batteries, we do not want to use it tethered, so we will connect it via Bluetooth.


## Assembling the Block
Here, we will use the configuration shown in the photo as an example and turn NXT into an RTC.

<!-- div align="center"><a href="TribotBase.png"><img src="TribotBase.png" width="100;"></a></div-->

TribotBase.png

This is a simple configuration in which an ultrasonic sensor that looks like eyes is attached to the front of the mobile base part of a configuration called Tribot.
The assembly method for the mobile base is described in detail in the small booklet inside the box labeled "Start Here" included in the Mindstorm NXT package, so refer to it.
Add several LEGO blocks to the mobile base explained in this booklet and attach the ultrasonic sensor to complete it.


## Installing the Bluetooth Device
The NXT intelligent block has Bluetooth built in from the beginning.
On the other hand, if a Bluetooth device is not built into the PC, you can communicate with NXT by attaching a Bluetooth device like the one in the photo to the PC.

First, attach these devices and, if necessary, install the device drivers so that they can be used.
On Windows XP and similar systems, most commercially available Bluetooth devices seem to work with the default driver without installing a separate driver.

<!-- div align="center"><a href="BluetoothDevices.png"><img src="BluetoothDevices.png" width="100;"></a></div-->
BluetoothDevices.png

If Bluetooth is installed properly, a Bluetooth icon will appear in the Control Panel.
Clicking this displays the Bluetooth settings dialog shown in the figure.

<!-- div align="center"><a href="BthDialogOption.png"><img src="BthDialogOption.png" width="100;"></a></div -->
BluetoothDevices.png

Open "Options" and check the following:
- "Turn discovery on"
- "Show the Bluetooth icon in the notification area"

Next, since NXT and the PC will be connected, leave this dialog open for now.


## Connecting the PC and NXT
The procedure for connecting the PC and NXT via Bluetooth is roughly as follows.

1. Turn on NXT
1. Put NXT in Bluetooth search mode and search
1. Select your PC
1. Select the channel
1. Start the connection wizard from the PC Bluetooth settings dialog
1. Set the passkey
1. Press the connection button on both the PC and NXT
1. Restart NXT after connection


### Starting NXT
Press the orange button in the center of the NXT intelligent block to turn it on.
When it turns on, a "pirolirori♪" sound plays and the block starts up. (No sound is produced if the volume setting is 0.)
When it is turned on, it enters the "My files" mode screen shown in the figure.

<!-- div align="center"><a href="NXTBoot.png"><img src="NXTBoot.png" width="100;"></a></div-->
NXTBoot.png

If this screen does not appear, you can switch to "My files" mode by pressing the square button below the orange button several times.

### Searching for Bluetooth Devices
In "My files" mode, press the gray triangular buttons on the left and right of the orange button to move the cursor to "Bluetooth" mode, then press the orange button.

<!-- div align="center"><a href="NXTBluetooth.png"><img src="NXTBluetooth.png" width="100;"></a></div-->
NXTBluetooth.png

Next, press the left and right triangular buttons to move the cursor to "Search" mode.

<!-- div align="center"><a href="NXTBthSearch.png"><img src="NXTBthSearch.png" width="100;"></a></div-->
NXTBthSearch.png

In this state, press the orange button to actually search for connection targets.
The search screen is shown below.
<!-- div align="center"><a href="NXTBthSearching.png"><img src="NXTBthSearching.png" width="100;"></a></div-->
NXTBthSearching.png


### Connecting the Device
If Bluetooth on the PC is enabled and the PC is visible from NXT, the PC name should appear as shown in the figure.
Here, the PC name means the "Computer name" in Windows.

<!-- div align="center"><a href="NXTBthPCfound.png"><img src="NXTBthPCfound.png" width="100;"></a></div-->
NXTBthPCfound.png

If there are Bluetooth-equipped PCs nearby, several PCs may be visible.
Press the triangular buttons to move the cursor to your PC, then press the orange confirmation button.

Next, the Bluetooth channel selection screen appears, so press the orange confirmation button as it is.
After "Connecting" is displayed, the passkey input screen appears, so press the orange button as it is.
<!--div align="center"><a href="NXTBthPasskey.png"><img src="NXTBthPasskey.png" width="100;"></a></div-->
NXTBthPasskey.png

A balloon like the one shown in the figure appears on the PC side, so click this balloon.

<!-- div align="center"><a href="PCballoon.png"><img src="PCballoon.png" width="100;"></a></div-->
PCballoon.png

You will be asked to enter the passkey, so enter the passkey that was displayed on NXT earlier.
When the connection is complete, a dialog like the one shown in the figure appears.
To avoid recognizing other devices, check "Turn discovery off" and press "Finish" to exit.

<!-- div align="center"><a href="PCConnectComp.png"><img src="PCConnectComp.png" width="100;"></a></div-->
PCConnectComp.png

### Confirming the Connection
If you look at the "Devices" tab in the Bluetooth settings dialog, you can confirm that NXT is connected as shown in the figure.

<!-- div align="center"><a href="PCDevlistNXT.png"><img src="PCDevlistNXT.png" width="100;"></a></div-->
PCDevlistNXT.png
