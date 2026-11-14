---
layout: page
title: various settings
---

<!-- Title: 各種設定 -->
#contents

This section explains the various settings of RTCBuilder.
The RTCBuilder settings screen is displayed by selecting "RTCBuilder" from the "Preferences" screen, which is displayed by selecting [Window] > [Preferences...] from the menu at the top of the screen.
<br>

<div align="center"><a href="fig7-1SettingRTCBuilder2_ja.png"><img src="fig7-1SettingRTCBuilder2_ja.png" width="50%;"></a></div>

## Data Type
You can set the location of the IDL files that define the data types configured for Data Port and Configuration parameters.
To add a new IDL storage directory, click the [New] button. You can also delete the selected IDL storage directory by clicking the [Remove] button.
Select the actual location of the IDL storage directory in the directory selection screen that appears when you click inside the "IDL File Directories" field.

<div align="center"><a href="fig7-1SettingRTCBuilder1_ja.png"><img src="fig7-1SettingRTCBuilder1_ja.png" width="50%;"></a></div>
<div align="center"><strong>RTCBuilder Settings Screen</strong></div>

<br>


## Code Generation
You can set the default contents that are configured when a new editor is displayed or a new item is added on the Basic Profile input page and Configuration Profile input page of the RTC Profile Editor.
<br>

<div align="center"><a href="fig7-2SettingGenerateCode_ja.png"><img src="fig7-2SettingGenerateCode_ja.png" width="40%;"></a></div>
<div align="center"><strong>Code Generation Settings Screen</strong></div>
<br>
The default settings on this settings screen (the contents set when the [Restore Defaults] button is clicked) are as follows.
<div align="center"><strong>Code Generation Settings Screen Default Values</strong></div>
<table class="table-alt">
  <tr>
    <th>Item</th>
    <th>Default Value</th>
  </tr>
  <tr>
    <td>></td>
    <td>Basic</td>
  </tr>
  <tr>
    <td>Component name</td>
    <td>ModuleName</td>
  </tr>
  <tr>
    <td>Description</td>
    <td>ModuleDescription</td>
  </tr>
  <tr>
    <td>Version</td>
    <td>1.0.0</td>
  </tr>
  <tr>
    <td>Vendor</td>
    <td>VendorName</td>
  </tr>
  <tr>
    <td>Category</td>
    <td>Category</td>
  </tr>
  <tr>
    <td>Component Type</td>
    <td>STATIC</td>
  </tr>
  <tr>
    <td>Component’s activity type</td>
    <td>PERIODIC</td>
  </tr>
  <tr>
    <td>Max. Instances</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Component kind</td>
    <td>DataFlowComponent</td>
  </tr>
  <tr>
    <td>Execution type</td>
    <td>PeriodicExecutionContext</td>
  </tr>
  <tr>
    <td>Execution rate</td>
    <td>1.0</td>
  </tr>
  <tr>
    <td>></td>
    <td>Configuration</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>conf_name</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>conf_type</td>
  </tr>
  <tr>
    <td>Variable Name</td>
    <td>conf_varname</td>
  </tr>
  <tr>
    <td>Default Value</td>
    <td>conf_default</td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td>conf_constraint</td>
  </tr>
  <tr>
    <td>Unit</td>
  </tr>
</table>
<br>

## Port
You can set the default contents that are configured when a new item is added on the Data Port Profile input page and Service Port Profile input page of the RTC Profile Editor.
<br>

<div align="center"><a href="fig7-3SettingPort_ja.png"><img src="fig7-3SettingPort_ja.png" width="40%;"></a></div>
<div align="center"><strong>Port Settings Screen</strong></div>
<br>
The default settings on this settings screen (the contents set when the [Restore Defaults] button is clicked) are as follows.
<div align="center"><strong>Port Settings Screen Default Values</strong></div>
<table class="table-alt">
  <tr>
    <th>Item</th>
    <th>Default Value</th>
  </tr>
  <tr>
    <td colspan="2">Data Port</td>
  </tr>
  <tr>
    <td>DataPort Name</td>
    <td>dp_name</td>
  </tr>
  <tr>
    <td>DataPort Type</td>
    <td>dp_type</td>
  </tr>
  <tr>
    <td>DataPort Variable Name</td>
    <td>dp_vname</td>
  </tr>
  <tr>
    <td>DataPort Constraint</td>
    <td>dp_constraint</td>
  </tr>
  <tr>
    <td >DataPort Unit</td>
    <td ></td>
  </tr>
  <tr>
    <td colspan="2">Service Port</td>
  </tr>
  <tr>
    <td>ServicePort Name</td>
    <td>sv_name</td>
  </tr>
  <tr>
    <td colspan="2">Service Interface</td>
  </tr>
  <tr>
    <td>Interface Name</td>
    <td>if_name</td>
  </tr>
  <tr>
    <td>Instance Name</td>
    <td>if_instance</td>
  </tr>
  <tr>
    <td>Variable Name</td>
    <td>if_varname</td>
  </tr>
</table>
<br>

## Configuration
You can set the items displayed in the system configuration information on the Configuration Profile input page of the RTC Profile Editor.
<br>

<div align="center"><a href="fig7-4SettingConfig_ja.png"><img src="fig7-4SettingConfig_ja.png" width="40%;"></a></div>
<div align="center"><strong>Configuration Settings Screen</strong></div>
<br>
The default settings on this settings screen (the contents set when the [Restore Defaults] button is clicked) are as follows.
<div align="center"><strong>Configuration Settings Screen Default Values</strong></div>
<!-- |項目|デフォルト値||項目|デフォルト値| -->

<table class="table-alt">
  <tr>
    <th>Item</th>
    <th>Default Value</th>
  </tr>
  <tr>
    <td>exec_cxt.periodic.type</td>
    <td>PeriodicExecutionContext</td>
  </tr>
  <tr>
    <td>exec_cxt.periodic.rate</td>
    <td>1000</td>
  </tr>
  <tr>
    <td>exec_cxt.evdriven.type</td>
    <td>EventDrivenExecutionContext</td>
  </tr>
</table>

<br>

## Export
You can set the files to be included in each archive format of the RT component packaging function.
<br>

<div align="center"><a href="fig7-4SettingExport_ja.png"><img src="fig7-4SettingExport_ja.png" width="40%;"></a></div>
<div align="center"><strong>Export Settings Screen</strong></div>
<br>
The settings screen is divided into sections for each archive format (Source Export, Binary Export, Source+Binary Export). Each section consists of an extension specification area and a file name specification area.
<br>


<div align="center"><a href="fig7-5SettingExport_ja.png"><img src="fig7-5SettingExport_ja.png" width="70%;"></a></div>
<div align="center"><strong>Export Settings Screen (Section)</strong></div>
<br>
In the extension specification area, you can set the extensions of files to be included in each archive format. When you click the [Select Types] button, a type selection screen like the following is displayed. Select the file types you want to include in the archive.
<br>
<br>
<table class="table-alt">
  <tr>
    <!-- th>BGCOLOR(white):</th-->
    <td><div align="left"><a href="fig7-6Select_ja.png"><img src="fig7-6Select_ja.png" width="70%;" align="left"></a></div></td>
    <td>* Only registered extensions are displayed in the file extension list. If you want to select files that do not exist in the list, enter the corresponding extensions in the "Other extensions" field at the bottom of the screen, separated by ",".</td>
  </tr>
</table>

<div align="center"><strong>Extension Selection Screen</strong></div>
<br>
In the file setting area, you can set the file names to be included in the archive. When you click the [Add] button at the bottom of the "File name" list, a new row is added, so directly enter the file name you want to include in the archive. You can also delete the selected row by clicking the [Delete] button.
In the example shown in <strong>Export Settings Screen (Section)</strong> above, when "Source+Binary" is selected as the archive method, files with the extensions "cpp" and "h" and files with the names "Makefile" and "README" are included in the archive.
The default settings on this settings screen (the contents set when the [Restore Defaults] button is clicked) are as follows.
<div align="center"><strong>Export Settings Screen Default Values</strong></div>
<table class="table-alt">
  <tr>
    <th>Item</th>
    <th>Default Value</th>
  </tr>
  <tr>
    <td colspan="2">Source Export</td>
  </tr>
  <tr>
    <td>Extension</td>
    <td>conf, cpp, h, vcproj, java, xml, py</td>
  </tr>
  <tr>
    <td>File Name</td>
    <td>Makefile, README</td>
  </tr>
  <tr>
    <td colspan="2">Binary Export</td>
  </tr>
  <tr>
    <td>Extension</td>
    <td>conf, exe, class, py</td>
  </tr>
  <tr>
    <td>File Name</td>
    <td>README</td>
  </tr>
  <tr>
    <td colspan="2">Source+Binary Export</td>
  </tr>
  <tr>
    <td>Extension</td>
    <td>conf, cpp, h, vcproj, java, xml, py, exe, class</td>
  </tr>
  <tr>
    <td>File Name</td>
    <td>Makefile, README</td>
  </tr>
</table>
<br>

## Build View 
You can set the color information of the icons displayed in the Build View.
<br>

<div align="center"><a href="fig7-7SettingBuildView_ja.png"><img src="fig7-7SettingBuildView_ja.png" width="40%;"></a></div>
<div align="center"><strong>Build View Settings Screen</strong></div>
<br>
Each color setting button allows you to change the color settings for the component body, DataInPort, DataOutPort, ServicePort, and ServiceInterface.
<br>

<!-- *Data Type -->
<!-- Data Port および Configuration パラメーターで設定するデータ型を定義した IDL ファイルの位置を設定することができます。 -->
<!-- #br -->
<!--  -->
<!-- #ref(fig7-6Datatype.png,nolink,center) -->
<!-- CENTER:''Data Type設定画面'' -->
<!--  -->
<!-- IDL格納ディレクトリを新規に追加する場合は、｢Add｣ボタンをクリックしてください。また、「Delete」ボタンをクリックすると、選択中のIDL格納ディレクトリを削除することができます。 -->
<!-- #br -->
<!-- IDL格納ディレクトリの実際の位置は、｢IDL File Directories｣欄内をクリックして表示されるディレクトリ選択画面にて選択してください。 -->
<!-- #br -->

## Document
<!-- 各アクティビティの概要を説明するドキュメントの入力を設定することができます。 -->
You can set the enabled/disabled attributes (ON/OFF) for each activity.
<div align="center"><a href="fig7-8SettingDocument_ja.png"><img src="fig7-8SettingDocument_ja.png" width="40%;"></a></div>
<div align="center"><strong>Document Settings Screen</strong></div>
