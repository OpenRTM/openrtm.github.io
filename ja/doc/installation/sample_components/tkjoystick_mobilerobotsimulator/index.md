---
layout: page
title: "tkjoystick/tkmobilerobotsimulator"
---

<!-- Title: TkJoyStick/TkMobileRobotSimulator -->
#contents
## TkJoyStick
このサンプルは、OpenRTM-aistのPython版に付属しています。 C++版、Java版には付属していませんのでご注意ください。

### 概要
GUI画面を持ったRTコンポーネントのサンプルです。TkJoyStickComp.batを実行することでサンプル・コンポーネントが起動されます。
GUI上のジョイスティックをドラッグで移動した位置に応じた値(x, y)を出力します。

### 起動画面
<div align="center"><a href="TkJoystick.png"><img src="TkJoystick.png" width="60%;"></a></div>
<div align="center"><strong>TkJoyStick実行例</strong></div>

### 使い方
- 画面中央に表示される小さい丸をドラッグすることで、丸の座標に応じた (x, y) の値を出力します。右上のScale Factorのスライダを調整することで、出力する座標値のスケールを調整できます。画面右下には、直角座標系の(x, y)の値と、極座標系の(r, theta)が表示されます。
- OutPortは2つあり、"pos"からは位置に応じた値が、"vel"からは反時計方向に座標を45度かたむけた値が、たとえば"pos"が(10,10)だとすると"vel"には(14.142, 0)が出力されます。

## TkMobileRobotSimulator
このサンプルは、OpenRTM-aistのPython版に付属しています。C++版、Java版には付属していませんのでご注意ください。

### 概要
GUI画面を持ったRTコンポーネントのサンプルです。TkMobileRobotSimulator.batを実行することでサンプル・コンポーネントが起動されます。

### 起動画面

<div align="center"><a href="TkMobileRobotSimulator.png"><img src="TkMobileRobotSimulator.png" width="60%;"></a></div>
<div align="center"><strong>TkMobileRobotSimulator実行例</strong></div>

### 使い方
実際にRTCとしてシステムが認識し、Name ServiceでRTCが見えるようにするためには、GUIの右側中央にある[Create]ボタンを押します。GUI上にモータで前後左右に動く物体を模した五角形のオブジェクトが表示されます。InPortへの入力値に応じて、画面上の5角形のオブジェクトが移動します。InPortへの入力はロボットを駆動する左側車輪用モータの回転速度と右側車輪のモータ回転速度になります。まっすぐ頂点方向に進むためには両方の車輪の速度が一緒である必要があります。

## システム構成
<div align="center"><a href="SysEdit.png"><img src="SysEdit.png" width="60%;"></a></div>
<div align="center"><strong>RTSystemEditor実行例</strong></div>

### 使い方
TkJoystick(入力デバイス)とTkMobileRobotSimulator接続し、GUI上でJoystickで移動速度を制御するくロボットのシミュレーションをします。

- 手順
  - RTSystemEditorを起動し、新規SystemEditorを開きます。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_2_0)を参照
  - TkJoyStickComp.py、TkMobileRobotSimulator.py、両コンポーネントを起動します。
  - TkMobileRobotSimulator.pyのGUIの[Create]ボタンを１回クリックします。
  - RTSystemEditorのName Service Viewに両コンポーネントが表示されるので、それらをSystemEditor上にドラッグします。
  - 両コンポーネントの対応ポート(どちらもvel)を結びます。(上図RTSystemEditor実行例を参照)
  - どちらかのコンポーネントを右クリックし、[Activate Systems]を選択します。
  - TkJoystickCompの画面上で中心点をドラッグすることにより、TkMobileRobotSimulator上の5角形のオブジェクト(ロボットを表しています)が動きます。Y方向(上下方向)にTkJoystickコンポーネントを動かすと進行方向への移動速度が変化し、X方向(左右方向)に動かすと、回転速度と回転方向が変化するように動きます。(TkJoyStickの"vel" OutPortを使う場合は、ジョイステックを上下方向に動かすと、ベクター値の2値が同じ値になります。また左右に動かした場合は、正負が逆の値になります。これをTkMobileRobotSimulatorに送ると、それぞれ左右のモータへの速度制御入力として動作するため、上下方向の移動は2つのモータを同じ方向で同じ速度で動かすような形で頂点方向への直進速度の制御ということになります。また左右方向のジョイステックの移動は"vel" OutPortからのベクターの2要素は正負が反転した値となり、それがTkMobileRobotSimulatorにとっては左右のモータの速度の制御値になるため、同じ絶対値速度で逆方向にモータを回すことになるので、ロボットはその場で回転するということになります。) 



