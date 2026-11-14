---
layout: page
title: "how to use the system environment variable setting tool"
---

<!-- Title: How to use the system environment variable setting tool -->
#contents

## VCVerChanger

### (G)Overview
<!-- *** 概要 -->

This tool is included in the installer of OpenRTM-aist version 1.2.0 or later and corresponds to the following cases.
- I want to change the version of Visual Studio used with OpenRTM-aist
- Both 32-bit version and 64-bit version of OpenRTM-aist are installed, but I want to use it by switching.
<!-- 本ツールは、OpenRTM-aist 1.2.0 版以降のインストーラーに含まれており、下記のケースに対応しています。 -->
<!-- - OpenRTM-aist で使用する Visual Studio のバージョンを変更したい -->
<!-- - OpenRTM-aist の32bit 版、64bit 版を両方インストールしているが、切り替えて使いたい。 -->

OpenRTM-aist uses the system environment of the same name for both 32-bit version and 64-bit version. Also added to PATH to pass through.
Therefore, installing both 32-bit version and 64-bit version or uninstalling one of them may require rewriting the system environment variables.
<!-- OpenRTM-aistは、32bit 版も64bit 版も同じ名前のシステム環境を利用しています。またパスを通すために PATH にも追加しています。 -->
<!-- このため、32bit 版、64bit 版の両方をインストールしたり、一方をアンインストールしたりすると、システム環境変数の書き換えが必要となる場合があります。 -->

In such a case, activate this tool and click the [Confirm] button to correct it to the correct system environment variable.
<!-- このような場合に本ツールを起動して [確認] ボタンをクリックすると、正しいシステム環境変数に修正します。 -->

(G)The log of this tool is output to the destination shown on the startup screen. Since it is overwriting every time, it can check just the last execution content.
<!-- 本ツールのログを、起動画面に示している先に出力しています。毎回上書きしているので直前の実行内容だけですが確認することができます。 -->
& br;

### (G)Installation and start-up
<!-- *** インストールおよび起動 -->

You can start it from the start menu after installation. You can also start by searching with VCVerChanger.
<!-- インストール後にスタートメニューから起動できます。VCVerChanger で検索しての起動もできます。 -->

<table class="table-alt">
<div align="center"><a href="VCVerChanger_01.png"><img src="VCVerChanger_01.png" width="70%;"></a></div>|
<div align="center"><a href="VCVerChanger_02.png"><img src="VCVerChanger_02.png" width="70%;"></a></div>|
<table class="table-alt">
  <tr>
    <th>CENTER: **From start to OpenRTM-aist xxx (since 1.2.0)**</th>
    <th>CENTER:**VCVerChanger**</th>
  </tr>
</table>
<!-- |CENTER:''スタートから OpenRTM-aist xxx（1.2.0以降）''|CENTER:''VCVerChanger''| -->

### (G)Visual Studio version update procedure
<!-- *** Visual Studio のバージョン更新手順 -->

Activate this tool and click the [Confirm] button. The image shown here is the result in an environment where only OpenRTM-aist 32-bit version is installed.
<!-- 本ツールを起動し、[確認] ボタンをクリックします。ここで示している画像は、OpenRTM-aist の 32bit 版だけをインストールしている環境での結果です。 -->
<br>
<br>

<div align="center"><a href="VCVerChanger_03.jpg"><img src="VCVerChanger_03.jpg" width="70%;"></a></div>
<br>
<br>

The current system environment variable setting is displayed. Make sure that the topmost Visual Studio version matches the version you have installed.
<!-- 現在のシステム環境変数の設定が表示されます。一番上の Visual Studio Version がインストールしているバージョンと一致しているか確認します。 -->
<br>
<br>

<div align="center"><a href="VCVerChanger_04.jpg"><img src="VCVerChanger_04.jpg" width="70%;"></a></div>
<br>
<br>

To change, select it from the list as shown below and click the [Update] button.
<!-- 変更する場合は、下記のようにリストから選択し、[更新] ボタンをクリックします。 -->
<br>
<br>

<div align="center"><a href="VCVerChanger_05.jpg"><img src="VCVerChanger_05.jpg" width="70%;"></a></div>
<br>
<br>

The changed setting will be displayed. Confirm that the value of the specified RTM_VC_VERSION is reflected in the path, and click the [Finish] button.
<!-- 変更後の設定が表示されますので、指定した RTM_VC_VERSION の値がパスに反映されていることを確認し、[終了] ボタンをクリックします。 -->
<br>
<br>

<div align="center"><a href="VCVerChanger_06.jpg"><img src="VCVerChanger_06.jpg" width="70%;"></a></div>
<br>
<br>

### (G)Procedure for switching OpenRTM-aist 32bit, 64bit pass
<!-- *** OpenRTM-aist の 32bit、64bit パスの切替手順 -->

When installing 32 bit version and 64 bit version in succession, start this tool and click the [Confirmation] button.
The setting of the current system environment variable is displayed and you can confirm that both settings are mixed and added to PATH.
<!-- 32bit 版と 64bit 版を続けてインストールした場合、本ツールを起動して [確認] ボタンをクリックします。 -->
<!-- 現在のシステム環境変数の設定が表示され、PATH に両方の設定が混ざって追加されていることを確認できます。 -->
<br>
<br>

<div align="center"><a href="VCVerChanger_07.jpg"><img src="VCVerChanger_07.jpg" width="70%;"></a></div>
<br>
<br>

Select either 32 bit or 64 bit, and click the [Switch] button.
<!-- 32bit、64bit のどちらかを選択し、[切替] ボタンをクリックします。 -->
<br>
<br>

<div align="center"><a href="VCVerChanger_08.jpg"><img src="VCVerChanger_08.jpg" width="70%;"></a></div>
<br>
<br>

Since the setting after switching is displayed, confirm the path and click the [End] button.
<!-- 切り替え後の設定が表示されますので、パスを確認し [終了] ボタンをクリックします。 -->
<br>
<br>

<div align="center"><a href="VCVerChanger_09.jpg"><img src="VCVerChanger_09.jpg" width="70%;"></a></div>
<br>
<br>

## Tool for OpenRTM-aist 1.1.2 version OpenRTMEnvTool
<!-- ** OpenRTM-aist 1.1.2版用のツール OpenRTMEnvTool -->

### (G)Download
<!-- *** ダウンロード -->

To run this tool, mfc dll is required. To execute the tool without installing this dll separately, two kinds of executable files are prepared.
Please download it according to your version of Visual Studio.
<!-- 本ツールの実行には、mfc の dll が必要です。この dll を別途インストールせずともツールを実行するために、2種類の実行ファイルを用意しています。 -->
<!-- ご使用の Visual Studio のバージョンに合わせてダウンロードしてください。 -->

<table class="table-alt">
  <tr>
    <th>LEFT:200</th>
    <th>LEFT:200</th>
    <th>c</th>
  </tr>
  <tr>
    <td>Visual Studio 2008, 2010, 2012</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/tools/OpenRTMEnvTool_vc10.exe">OpenRTMEnvTool_vc10.exe</a></td>
  </tr>
  <tr>
    <td>Visual Studio 2013, 2015</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/tools/OpenRTMEnvTool_vc12.exe">OpenRTMEnvTool_vc12.exe</a></td>
  </tr>
</table>

### (G)How to use
<!-- *** 使い方 -->
When executing the downloaded exe file, the following screen is displayed, so click the [Confirmation] button.
<!-- ダウンロードした exe ファイルを実行すると以下の画面が表示されるので、[確認] ボタンをクリックします。 -->
<br>
<br>

<div align="center"><a href="RTMEnvTool_01.jpg"><img src="RTMEnvTool_01.jpg" width="70%;"></a></div>
<br>
<br>

Since the setting of the current system environment variable is displayed, make sure that the setting of "RTM_VC_VERSION" at the top matches the version of Visual Studio you are installing.
<!-- 現在のシステム環境変数の設定が表示されるので、一番上の「RTM_VC_VERSION」の設定がインストールしている Visual Studio のバージョンと一致しているか確認します。 -->
<br>
<br>

<div align="center"><a href="RTMEnvTool_02.jpg"><img src="RTMEnvTool_02.jpg" width="70%;"></a></div>
<br>
<br>

To change the setting of "RTM_VC_VERSION" to vc 14 (for vc 2015), specify it as shown below and click the "Update" button.
<!-- 「RTM_VC_VERSION」の設定を vc14 (vc2015用）に変更する場合は、下記のように指定し、[更新] ボタンをクリックします。 -->
<br>
<br>

<div align="center"><a href="RTMEnvTool_03.jpg"><img src="RTMEnvTool_03.jpg" width="70%;"></a></div>
<br>
<br>

The changed setting will be displayed. Confirm that the value of the specified RTM_VC_VERSION is reflected in the path, and click the [Finish] button.
<!-- 変更後の設定が表示されますので、指定した RTM_VC_VERSION の値がパスに反映されていることを確認し、[終了] ボタンをクリックします。 -->
<br>
<br>

<div align="center"><a href="RTMEnvTool_04.jpg"><img src="RTMEnvTool_04.jpg" width="70%;"></a></div>
<br>
<br>


