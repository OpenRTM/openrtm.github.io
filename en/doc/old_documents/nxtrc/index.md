---
layout: page
title: 
---
<br>
<a>No English version available.
</a>

<!-- Title: NXTRTC -->

#contents

このサンプルは、OpenRTM-aistのPython版に付属しています。
C++版、Java版には付属していませんのでご注意ください。

### 概要
NXTRTC.pyは、LEGO Mindstorm NXTのモーター制御や、センサーデータを出力するコンポーネントです。

- 参考
  - [RTコンポーネント作成(LEGO Mindstorm編)]({{ site.baseurl }}/en/doc/casestudy/rtc_development/rtc_development_lego_mindstorm)

### 起動画面

<div align="center"><a href="NXTRTC.png"><img src="NXTRTC.png" width="70%;"></a></div>
<div align="center"><strong>NXTRTC実行例(NXTRTC)</strong></div>

<div align="center"><a href="TkMotor.png"><img src="TkMotor.png" width="100;"></a></div>
<div align="center"><strong>TkMotorComp実行例(TkMotorComp)</strong></div>

<div align="center"><a href="NXTRTC_example_rtse_ja.png"><img src="NXTRTC_example_rtse_ja.png" width="80%;"></a></div>
<div align="center"><strong>NXTRTC 実行例(RTSystemEditor)</strong></div>


<br>
#### 使い方
GUIをもったTkJoystick(入力デバイス)と、TkMotor(出力デバイス)に接続し、LEGOのモータ制御と値の確認をします。

※詳細は[RTコンポーネント作成(LEGO Mindstorm編)]({{ site.baseurl }}/en/doc/casestudy/rtc_development/rtc_development_lego_mindstorm)マニュアルでごご覧ください。

<br>


- 手順
  - RTSystemEditorを起動し、新規SystemEditorを開きます。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_2_0)を参照
  - [こちら]({{ site.baseurl }}/en/doc/casestudy/rtc_development/rtc_development_lego_mindstorm/midstorm_nxt_setup)を参考にPCとLEGO MindstormをBluetooth、又はUSB接続してください。
  - NXTRTC.py、入力デバイスTkJoyStickComp.py、TkMotorComp、各コンポーネントを起動します。
  - RTSystemEditorのName Service Viewにコンポーネントが表示されるので、それらをSystemEditor上にドラッグします。
  - 両コンポーネントの対応ポートを結びます。(上図SystemEditor実行例を参照)
  - どちらかのコンポーネントを右クリックし、[Activate Systems]を選択します。


