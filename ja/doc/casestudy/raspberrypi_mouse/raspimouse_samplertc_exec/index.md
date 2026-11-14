---
layout: page
title: サンプルの rtシステムの実行
---

<!-- Title: サンプルの RTシステムの実行 -->
#contents

## 事前準備
### Windows
#### RTC のインストール
サンプルの RTシステムの一部で以下のRTCを使用するためインストールしてください。

##### DirectInputRTC
ジョイスティックで操作するための RTC です。
以下のサイトからインストーラーをダウンロードして実行してください。

- http://ysuga.net/?p=130

##### JoystickToVelocity
DirectInputRTC のアウトポートからの出力(TimedLongSeq型)を TimedVelocity2D型に変換する RTC です。
以下のサイトからインストーラーをダウンロードして実行してください。

- http://ysuga.net/?p=130

#### ネームサーバー、RTシステムエディタの起動
##### Windows
まず最初に Windows でネームサーバー、RTシステムエディタを起動してください。
詳しい手順は [このページ]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/test_windows_1_1) を参考にしてください。

##### Raspbian
Raspbianの [一括インストールの項目]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_rtc_on_raspbian#toc4) でダウンロードしたファイルの中に rtc.conf があるので、rtc.conf の以下の ppp.pp.pp.ppp の部分を Windows側の IPアドレスに変更してください。

```
 corba.nameservers: ppp.pp.pp.ppp
```

これで起動したコンポーネントが Windows のネームサーバーに登録されるようになります。

Windows で IPアドレスを確認するには以下のコマンドを入力します。

```
 ipconfig
```


## RTC の起動
### Windows
Windows側のRTCは [スクリプトファイルの項目]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_rtc_on_windows#toc0) でダウンロードしたファイルの中に start_component.bat というバッチファイルがあるのでそれを実行すれば以下の RTC が起動します。


```
 DirectInput0
 JoystickToVelocity0
 RaspberryPiMouseGUI0
 TkJoyStick0
```


※64bit版 Windows、32bit版 OpenRTM-aist を対象にしています。32bit版 Windows の場合は start_component_32.bat、64bit版 OpenRTM-aist を利用する場合は start_component_64.bat を起動してください。
※Python のインストールしたディレクトリーにパスが通っていない場合、TkJoyStick は起動できません。お手数ですが [このページ]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/test_windows_python_1_1#toc7) の手順を参考にして手動で起動してください。

### Raspbian

[一括インストールの項目]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_rtc_on_raspbian#toc4) でダウンロードしたフォルダーの中の start_rtc.sh を実行することで起動できます。

```
 cd RaspberryPiMouseRTSystem_script_Raspbian
 sh start_rtc.sh
```

これで以下のコンポーネントが起動します。

```
 RaspberryPiMouseRTC0
 RaspberryPiMouseController_DistanceSensor0
 RaspberryPiMouseController_Joystick0
 NineAxisSensor_RT_USB0
```

## RTシステムの復元、開始
Windows側で [スクリプトファイルの項目]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_rtc_on_windows#toc0) でダウンロードしたファイルのSimpleControlRasPiMouse フォルダー内の SimpleControlRasPiMouse_resurrect.bat を実行してください。
これでデータポートの接続、コンフィギュレーションパラメーターの設定などが行われます。
次に SimpleControlRasPiMouse_activate.bat を実行すると RTC をアクティブ化します。
SimpleControlRasPiMouseはGUI からラズパイマウスを操作する RTシステムです。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/SimpleControlRasPiMouse/SimpleControlRasPiMouse.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/SimpleControlRasPiMouse/SimpleControlRasPiMouse.png" width="70%;"></a></div>

非アクティブにする際は SimpleControlRasPiMouse_stop.bat を起動してください。
SimpleControlRasPiMouse_teardown.bat を起動するとポートの接続を切断します。



## 各サンプルの詳細

SimpleControlRasPiMouse 以外のサンプルも****_resurrect.bat で RTシステム復元、****_activate.bat でアクティブ化、****_stop.bat で非アクティブ化、****_teardown.bat でポートの切断ができます。

<table class="table-alt">
  <tr>
    <th>ファイル名</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>****_resurrect.bat</td>
    <td>RTシステム復元</td>
  </tr>
  <tr>
    <td>****_activate.bat</td>
    <td>アクティブ化</td>
  </tr>
  <tr>
    <td>****_stop.bat</td>
    <td>非アクティブ化</td>
  </tr>
  <tr>
    <td>****_teardown.bat</td>
    <td>ポートの切断</td>
  </tr>
</table>

### LightSensorControlRasPiMouse
このサンプルは GUI によるラズパイマウスの操作に加え、距離センサが物体を検知すると回転して回避を行う RTシステムです。
試しに RaspberryPiMouseController_DistanceSensor0 のコンフィギュレーションパラメーター sensor_limit の値を変更してみると動きが変わると思います。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/LightSensorControlRasPiMouse/LightSensorControlRasPiMouse.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/LightSensorControlRasPiMouse/LightSensorControlRasPiMouse.png" width="70%;"></a></div>

### JoystickControlRasPiMouse
このサンプルは OpenRTM-aist-Python のサンプルコンポーネント TkJoyStick で傾けた方角にラズパイマウスを操作するRTシステムです。
このサンプルの動作には USB出力9軸 IMUセンサモジュールを Raspberry Pi に接続しておく必要があります。
[センサのキャリブレーション]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_rtc_on_raspbian#toc3) はラズパイマウスに装着した状態で行ってください。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/JoystickControlRasPiMouse/JoystickControlRasPiMouse.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/JoystickControlRasPiMouse/JoystickControlRasPiMouse.png" width="70%;"></a></div>

### JoystickLightSensorControlRasPiMouse
このサンプルは TkJoyStick による走行する方角の操作ができることに加えて、距離センサーが物体を検知した際に回避運動を行う RTシステムです。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/JoystickLightSensorControlRasPiMouse/JoystickLightSensorControlRasPiMouse.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/JoystickLightSensorControlRasPiMouse/JoystickLightSensorControlRasPiMouse.png" width="70%;"></a></div>


### GamePadSimpleControlRasPiMouse
このサンプルはゲームパッドのアナログスティックで傾けた方向にラズパイマウスを操作する RTシステムです。
Windows側の PC にゲームパッドを接続してから起動してください。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/GamePadSimpleControlRasPiMouse/GamePadSimpleControlRasPiMouse.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/GamePadSimpleControlRasPiMouse/GamePadSimpleControlRasPiMouse.png" width="70%;"></a></div>

### GamePadLightSensorSimpleControlRasPiMouse
このサンプルはゲームパッドによる走行する方向の操作ができることに加えて、距離センサーが物体を検知した際に回避を行う RTシステムです。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/GamePadLightSensorSimpleControlRasPiMouse/GamePadLightSensorSimpleControlRasPiMouse.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/GamePadLightSensorSimpleControlRasPiMouse/GamePadLightSensorSimpleControlRasPiMouse.png" width="70%;"></a></div>

### GamePadControlRasPiMouse
このサンプルはゲームパッドのアナログスティックで傾けた方角にラズパイマウスを操作する RTシステムです。
9軸センサにより現在の姿勢を計算して、アナログスティックの傾けた方角に進むように制御を行います。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/GamePadControlRasPiMouse/GamePadControlRasPiMouse.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/GamePadControlRasPiMouse/GamePadControlRasPiMouse.png" width="70%;"></a></div>

### GamePadLightSensorControlRasPiMouse
このサンプルはゲームパッドによる走行する方角の操作ができることに加えて、距離センサーが物体を検知した際に回避を行う RTシステムです。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/GamePadLightSensorControlRasPiMouse/GamePadLightSensorControlRasPiMouse.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/GamePadLightSensorControlRasPiMouse/GamePadLightSensorControlRasPiMouse.png" width="70%;"></a></div>
