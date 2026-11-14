---
layout: page
title: ラズパイマウス用 rtc のインストール(raspbian)
---

<!-- Title: ラズパイマウス用 RTC のインストール(Raspbian) -->
#contents


# RaspberryPiMouseRTC
RaspberryPiMouseRTC は名城大学のロボットシステムデザイン研究室で開発されているラズパイマウス制御用の RTコンポーネントです。

以下のコマンドでインストールできます。

```
 git clone https://github.com/rsdlab/RaspberryPiMouseRTC.git
 cd RaspberryPiMouseRTC
 cmake .
 make
```

以下の RTC は必要に応じてインストールしてください。

# RaspberryPiMouseController_DistanceSensor
ラズパイマウスの距離センサーが障害物を感知した際に回転して回避する運動を生成する RTC です。

以下のコマンドでインストールできます。

```
 git clone https://github.com/Nobu19800/RaspberryPiMouseController_DistanceSensor
 cd RaspberryPiMouseController_DistanceSensor
 cmake .
 make
```

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseController_DistanceSensor_comp.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseController_DistanceSensor_comp.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">RaspberryPiMouseController_DistanceSensor</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>target_velocity_in</td>
    <td>RTC::TimedVelocity2D</td>
    <td>補正前の目標速度</td>
  </tr>
  <tr>
    <td>distance_sensor</td>
    <td>RTC::TimedShortSeq</td>
    <td>距離センサーの計測値</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>target_velocity_out</td>
    <td>RTC::TimedVelocity2D</td>
    <td>補正後の目標速度</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">コンフィギュレーションパラメーター</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>デフォルト値</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>sensor_limit</td>
    <td>10</td>
    <td>回避運動を開始する距離センサーの計測値</td>
  </tr>
  <tr>
    <td>rotational_speed</td>
    <td>1.6</td>
    <td>回避運動の速さ</td>
  </tr>
  <tr>
    <td>stop_velocity</td>
    <td>0.01</td>
    <td>停止していると判定する直進速度</td>
  </tr>
</table>


# RaspberryPiMouseController_Joystick
ジョイスティックでラズパイマウスを指定の方角へ制御するための RTC です。
※この RTC の動作には以下の NineAxisSensor_RT_USB等の方角が計測できる RTC が必須です。

以下のコマンドでインストールできます。

```
 git clone https://github.com/Nobu19800/RaspberryPiMouseController_Joystick
 cd RaspberryPiMouseController_Joystick
 cmake .
 make
```

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseController_Joystick_comp.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseController_Joystick_comp.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">RaspberryPiMouseController_Joystick</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>joystick_float</td>
    <td>RTC::TimedFloatSeq</td>
    <td>ジョイスティックの入力</td>
  </tr>
  <tr>
    <td>joystick_long</td>
    <td>RTC::TimedFloatSeq</td>
    <td>ジョイスティックの入力</td>
  </tr>
  <tr>
    <td>orientation</td>
    <td>RTC::TimedOrientation3D</td>
    <td>センサーなど計測した姿勢</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>out</td>
    <td>RTC::TimedVelocity2D</td>
    <td>目標速度</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">コンフィギュレーションパラメーター</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>デフォルト値</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>forward_factor</td>
    <td>0.01</td>
    <td>入力に対する直進速度の大きさ</td>
  </tr>
  <tr>
    <td>tangential_factor</td>
    <td>1.0</td>
    <td>入力に対する回転速度の大きさ</td>
  </tr>
  <tr>
    <td>x_reverse</td>
    <td>0</td>
    <td>1の時はジョイスティックのX座標を反転する</td>
  </tr>
  <tr>
    <td>m_y_reverse</td>
    <td>0</td>
    <td>1の時はジョイスティックのY座標を反転する</td>
  </tr>
</table>

# NineAxisSensor_RT_USB
アールティが販売している [USB出力9軸 IMUセンサーモジュール](http://www.rt-shop.jp/blog/archives/7238) の計測値を出力する RTC です。

以下のコマンドでインストールできます。

```
 git clone https://github.com/Nobu19800/NineAxisSensor_RT_USB
 cd NineAxisSensor_RT_USB
 cmake .
 make
```

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/NineAxisSensor_RT_USB_comp.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/NineAxisSensor_RT_USB_comp.png" width="60%;"></a></div>


<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">NineAxisSensor_RT_USB</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>acc</td>
    <td>RTC::TimedAcceleration3D</td>
    <td>加速度センサーの計測値</td>
  </tr>
  <tr>
    <td>magn</td>
    <td>RTC::TimedDoubleSeq</td>
    <td>地磁気センサーの計測値</td>
  </tr>
  <tr>
    <td>gyro</td>
    <td>RTC::TimedAngularVelocity3D</td>
    <td>ジャイロセンサーの計測値</td>
  </tr>
  <tr>
    <td>temp</td>
    <td>RTC::TimedDouble</td>
    <td>温度センサーの計測値</td>
  </tr>
  <tr>
    <td>rot</td>
    <td>RTC::TimedOrientation3D</td>
    <td>姿勢</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">コンフィギュレーションパラメーター</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>デフォルト値</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>rotOffset</td>
    <td>0</td>
    <td>姿勢のオフセット(0[rad]を北以外の方角にしたい場合に調整)</td>
  </tr>
  <tr>
    <td>magnOffsetX</td>
    <td>-65</td>
    <td>地磁気センサーのオフセット(X軸)</td>
  </tr>
  <tr>
    <td>magnOffsetY</td>
    <td>-60</td>
    <td>地磁気センサーのオフセット(Y軸)</td>
  </tr>
  <tr>
    <td>magnOffsetZ</td>
    <td>-5</td>
    <td>地磁気センサーのオフセット(Z軸)</td>
  </tr>
  <tr>
    <td>serial_port</td>
    <td>COM3(Windows)、/dev/ttyACM0(Linux)</td>
    <td>デバイスファイル名</td>
  </tr>
</table>

地磁気センサーのキャリブレーション用のソフトウェアは以下のコマンドでインストールできます。

```
 git clone https://github.com/Nobu19800/CalibrationUSBNineAxisSensor
 cd CalibrationUSBNineAxisSensor
 cmake .
 make
```


実行すると10秒カウントを始めるので、センサーをいろんな姿勢になるように回転させてください。
可能ならばスマートフォンの8の字調整の動きを行ってください。

そして最後にX・Y・Z軸の地磁気センサの補正値が表示されるので、その値に-1掛けた数値を NineAxisSensor_RT_USB のコンフィギュレーションパラメーターに反映させてください。

ロボットにセンサーを取り付ける等した場合は再度キャリブレーションを行ってください。


# 一括インストール
上記の RTC を一括でインストールします。
以下のコマンドを入力してください。

```
 git clone https://github.com/Nobu19800/RaspberryPiMouseRTSystem_script_Raspbian
 cd RaspberryPiMouseRTSystem_script_Raspbian
 sh Component/install_rtc.sh
```

これで RaspberryPiMouseRTSystem_script_Raspbian の Component フォルダー内に各 RTC がインストールされます。
※キャリブレーション用ソフトウェアはインストールされないので、手動でインストールしてください。

