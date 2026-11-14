---
layout: page
title: installation and startup
---
<!-- Title: インストールおよび起動 -->
#contents(4)
This section explains how to install and start RTCBuilder.
### Installing RTCBuilder
Since RTCBuilder is an Eclipse plugin, you must first install Eclipse itself and the other Eclipse plugins on which it depends.
<!-- [[動作環境:RTCBuilder]]を参照の上、これらをダウンロードします。 -->
<!-- Eclipse のインストールは解凍するだけです。また、 Eclipse のプラグインは解凍後、Eclipse フォルダ内に上書きするだけです。 -->
<!-- RTCBuilder のインストールは RTCBuilder のプラグイン jar ファイル（jp.go.aist.rtm.rtcbuilder_X.X.X.jar）を eclipse/plugins フォルダーに配置するだけで完了です。 -->
For installation, please refer to [Installing OpenRTM Eclipse tools]({{ site.baseurl }}/en/doc/installation/install_1_2/openrtp_1_2/)<!--/node/6655-->.
### Starting RTCBuilder
When you start Eclipse for the first time after installation, the following "Welcome" screen is displayed.
<br>

<div align="center"><a href="fig2InitialOfEclipseStart_1_ja.png"><img src="fig2InitialOfEclipseStart_1_ja.png" width="40%;"></a></div>
<div align="center"><strong>Screen when Eclipse is started for the first time</strong></div>
<br>
Click the "X" button at the upper left of this "Welcome" screen, and the following page will be displayed.
Click the [Open Perspective] button at the upper right, and select "Other" from the pull-down menu.
<br>

<div align="center"><a href="fig3PerspectiveSwitch_ja.png"><img src="fig3PerspectiveSwitch_ja.png" width="40%;"></a></div>
<div align="center"><strong>Switching Perspectives</strong></div>
<br>
Select "RTC Builder" and click the [OK] button.
<br>

<div align="center"><a href="fig2-3PerspectiveSelection_ja.png"><img src="fig2-3PerspectiveSelection_ja.png" width="50%;"></a></div>
<div align="center"><strong>Selecting a Perspective</strong></div>
<br>
RTCBuilder starts.
<br>

<div align="center"><a href="fig2-4RTCBuilderInit_ja.png"><img src="fig2-4RTCBuilderInit_ja.png" width="70%;"></a></div>
<div align="center"><strong>Initial screen when RTCBuilder starts</strong></div>
<br>

#### Starting the RTC Profile Editor
To open the RTC Profile Editor, click the [Open New RtcBuilder Editor] button on the toolbar, or select [File] > [Open New Builder Editor] from the menu bar.


<table class="table-alt">
  <tr>
    <td><div align="center"><a href="fig2-9ToolsBarOpenNewRtcBuilder_ja.png"><img src="fig2-9ToolsBarOpenNewRtcBuilder_ja.png" width="80%;"></a></div></td>
    <td><div align="center"><a href="fig2-10FileMenuOpenNewBuilder_ja.png"><img src="fig2-10FileMenuOpenNewBuilder_ja.png" width="60%;"></a></div></td>
  </tr>
  <tr>
    <td style="text-align: center;"><strong>Open New RtcBuilder Editor from the Toolbar</strong></td>
    <td style="text-align: center;"><strong>Open New Builder Editor from the File Menu</strong></td>
  </tr>
</table>

Enter a project name in the displayed new project creation dialog.
<div align="center"><a href="CreateProject2.png"><img src="CreateProject2.png" width="70%;"></a></div>
<div align="center"><strong>Creating a Project for RTCBuilder 1</strong></div>
<br>
The code generated using RTCBuilder, RTCProfile, and other files are saved under the project created here.
By default, the project is created under the workspace being used (inside the directory set in "Location").
If you want to create the project in any location, turn off the "Use default location" checkbox and specify the location in "Location".

<br>
A project with the specified name is generated and added to the Package Explorer.
<br>

<div align="center"><a href="fig2-8CreateProject4_ja.png"><img src="fig2-8CreateProject4_ja.png" width="70%;"></a></div>
<div align="center"><strong>Creating a Project for RTCBuilder 2</strong></div>
<br>
In the generated project, an RTC profile XML (RTC.xml) with default values is automatically generated.

