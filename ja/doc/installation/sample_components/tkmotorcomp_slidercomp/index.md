---
layout: page
title: "tkmotorcomp/slidercomp"
---

<!-- Title: TkMotorComp/SliderComp -->

#contents

## TkMotorComp
このサンプルは、OpenRTM-aistのPython版に付属しています。
C++版、Java版には付属していませんのでご注意ください。

### 概要
GUI画面を持ったRTコンポーネントのサンプルです。TkMotorComp.batを実行することでサンプル・コンポーネントが起動します。

### 起動画面

<div align="center"><a href="TkMotorComp.png"><img src="TkMotorComp.png" width="70%;"></a></div>
<div align="center"><strong>TkMotorComp実行例</strong></div>

## SliderComp
このサンプルは、OpenRTM-aistのPython版に付属しています。
C++版、Java版には付属していませんのでご注意ください。

### 概要
GUI画面を持ったRTコンポーネントのサンプルです。SliderComp.batを実行することでサンプル・コンポーネントが起動します。（以下の画面は、Windowsで動作させた場合のものです。）

### 起動画面

<div align="center"><a href="SliderComp.png"><img src="SliderComp.png" width="70%;"></a></div>
<div align="center"><strong>SliderComp実行例</strong></div>

## システム構築
<div align="center"><a href="RTSE_Slider_Motor.png"><img src="RTSE_Slider_Motor.png" width="70%;"></a></div>
<div align="center"><strong>RTSystemEditor上のSliderCompとTkMotorComp</strong></div>

### 使い方
SliderCompとTkMotorCompでスライドノブでモータの回転の制御をする環境をGUI上でシミュレーションします。

- 手順
  - RTSystemEditorを起動し、新規SystemEditorを開きます。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_2_0)を参照
  - SliderComp.bat、TkMotorComp.bat、両コンポーネントを起動します。
  - RTSystemEditorのName Service Viewに両コンポーネントが表示されるので、それらをSystemEditor上にドラッグします。
  - 両コンポーネントの対応ポートを結びます。(上図RTSystemEditor実行例を参照)
  - どちらかのコンポーネントを右クリックし、[Activate Systems]を選択します。
  - TkMotorCompのGUI上でモータで駆動される円盤を模したものが表示され、その回転が、SliderCompのGUI上の上下スライドノブで制御できるのを確認してください。それぞれ6つのノブと6つのモータの回転を模しています。


