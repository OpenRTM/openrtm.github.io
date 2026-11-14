---
layout: page
title: ministickコンポーネントの作成
---

<!-- Title: Ministickコンポーネントの作成 -->
<!-- * Ministickコンポーネントの作成 -->

#contents

## Ministickコンポーネントの作成

Phidgets は Phidgets Inc. から発売されている、IO拡張ボードとセンサ群製品です。
日本では、ぷらっとほーむなどで購入することができます。

- Phidgets Inc.: http://www.phidgets.com/
- ぷらっとほーむ: http://online.plathome.co.jp/

PCにUSB接続の拡張IOボードを接続し、様々なセンサ、アクチュエータユニットを追加して、プログラム等から計測・制御することができるキットです。

PCと接続する場合は、Interface Kitが必要ですが、PiRT-Unitでのみ使用する場合は、Sensor Kitのみでよいでしょう。

- [Phidget Interface Kit #1](http://online.plathome.co.jp/item/detail/41595459/Phidgets/Phidget-Interface-Kit-Package--1/2005_1)
- [Phidget Interface Kit #2](http://online.plathome.co.jp/item/detail/41595460/Phidgets/Phidget-Interface-Kit-Package--2/2006_1)
- [Phidget Sensor Kit #1](http://online.plathome.co.jp/item/detail/41595256/Phidgets/Phidget-Sensor-Kit--1/42000_1)
- [Phidget Sensor Kit #2](http://online.plathome.co.jp/item/detail/41595257/Phidgets/Phidget-Sensor-Kit--2/42001_0)

PIRT-UnitのADピンは、Phidgetのセンサが接続可能なピンアサインとなっており、Phidgetデバイスを接続することで、容易に拡張することができるようになっています。

ここでは、Phidget の Ministick sensorを利用して、移動ロボットを制御してみます。
Ministick sensor は Phidget Sensor Kit #2 に含まれています。

## Ministick sensorとPiRT-Unitの接続

Ministick sensorの出力ピンとPiRT-Unitを以下のように接続します。

- X軸方向: CN2
- Y軸方向: CN3

<div align="center"><a href="ministick_connection.png"><img src="ministick_connection.png" width="80%;"></a></div>
<div align="center"><strong>Ministick sensorとPiRT-Unitの接続</strong></div>

X軸方向 (横向き) がADのCH0に、Y軸方向 (縦向き) がADのCH1に対応します。

このデータを読むプログラムをPythonで書いてみます。

### サンプルプログラム

```
 #!/usr/bin/env python
 # -*- coding: euc-jp -*- 
 import sys
 import time
 import spidev
 
 class ADC:
   def __init__(self):
     self.spi = spidev.SpiDev()
     self.spi.open(0, 0)
 
   def get_value(self, channel):
     sned_ch = [0x00,0x08,0x10,0x18]
     if ((channel > 3) or (channel < 0)):
       return -1
     r = self.spi.xfer2([sned_ch[channel],0,0,0])
     ret = ((r[2] << 6 ) & 0x300) |  ((r[2] << 6) & 0xc0) | ((r[3] >> 2) & 0x3f)
     return ret     
 
   def get_voltage(self, channel):
     ret = self.get_value(channel) * 5.0 / 1024
     return ret     
 
 def main():
   adc = ADC()
   while 1:
     adc1 = adc.get_value(0)
     msg1 = "%1.5fV(%04x)" % ((float(adc1)*5/1024),adc1)
     print msg1,
 
     adc1 = adc.get_value(1)
     msg1 = "%1.5fV(%04x)" % ((float(adc1)*5/1024),adc1)
     print msg1,
 
     adc2 = adc.get_value(2)
     msg2 = "%1.5fV(%04x)" % ((float(adc2)*5/1024),adc2)
     print msg2,
 
     adc3 = adc.get_value(3)
     msg3 = "%1.5fV(%04x)" % ((float(adc3)*5/1024),adc3)
     print msg3,
 
     sys.stdout.write("\n")
     time.sleep(0.5)
 
 if __name__ == '__main__':
   main()
```

このようなプログラムを作成します。TeraTermなどでRaspberry Piにログインして、サンプルプログラムを作成、テストします。

```
 Linux raspbian-armhf 3.2.27+ #307 PREEMPT Mon Nov 26 23:22:29 GMT 2012 armv6l
 
 The programs included with the Debian GNU/Linux system are free software;
 the exact distribution terms for each program are described in the
 individual files in /usr/share/doc/*/copyright.
 
 Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
 permitted by applicable law.
 Last login: Tue May 14 07:07:04 2013 from dhcpe2078.a02.aist.go.jp
 pi@raspbian-armhf ~ $ vi adc_test.py
 pi@raspbian-armhf ~ $ chmod 755 adc_test.py
 pi@raspbian-armhf ~ $ ./adc_test.py
```

サンプルプログラムを実行すると以下のような画面になります。ジョイスティックを倒してみると、Ch0,Ch1のデータが変化します。

<div align="center"><a href="ministick_teraterm.png"><img src="ministick_teraterm.png" width="50%;"></a></div>
<div align="center"><strong>ministick sensorの座標軸</strong></div>

それぞれ、X軸は左に倒すと、Y軸は上に倒すと電圧値が上がり、逆に倒すと電圧値が下がることがわかります。
ministick sensorの座標の関係を図に表わすと以下のようになります。

<div align="center"><a href="ministick_axis_ja.png"><img src="ministick_axis_ja.png" width="50%;"></a></div>
<div align="center"><strong>ministick sensorの座標軸</strong></div>

これは、一般的な座標系とはX軸が逆向きになっていますので、センサ値を処理する際には注意が必要です。

また、中心位置では、それぞれ5.0Vの半分、2.5V程度を指していることもわかると思います。
ただし、この値はぴったり2.5Vではなく、状況によっても変化するので、使用する前にキャリブレーションが必要なこともわかります。

## ジョイスティックコンポーネントの仕様

ministick sensorを利用したジョイスティックコンポーネントを作成します。
仕様としては、以下のようにします。

<table class="table-alt">
  <tr>
    <th colspan="2" style="text-align: center;">基本プロファイル</th>
  </tr>
  <tr>
    <td>コンポーネント名</td>
    <td>Ministick</td>
  </tr>
  <tr>
    <td>モジュール概要</td>
    <td>Phidget ministick sensor component</td>
  </tr>
  <tr>
    <td>バージョン</td>
    <td>1.0.0</td>
  </tr>
  <tr>
    <td>ベンダ名</td>
    <td>AIST</td>
  </tr>
  <tr>
    <td>モジュールカテゴリ</td>
    <td>Input Device</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">アクティビティ</td>
  </tr>
  <tr>
    <td colspan="2" >
    onInitialize, onFinalize, onActivated, onDeactivated, onExecute</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">データポート</td>
  </tr>
  <tr>
    <td colspan="2" >[out] pos</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>ジョイスティックのX-Y位置データ</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>TimedFloatSeq</td>
  </tr>
  <tr>
    <td>詳細</td>
    <td>data[0]: x位置, data[1]: y位置</td>
  </tr>
  <tr>
    <td>単位</td>
    <td>無し</td>
  </tr>
  <tr>
    <td colspan="2" >[out] vel</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>移動ロボットの速度ベクトル</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>TimedVelocity2D</td>
  </tr>
  <tr>
    <td>詳細</td>
    <td>vx: 並進速度, vy: 0.0, va: 角速度</td>
  </tr>
  <tr>
    <td>単位</td>
    <td>vx [m/s], va [rad/s]</td>
  </tr>
  <tr>
    <td colspan="2" >[out] wheel_vel</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>車輪速度</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>TimedFloatSeq</td>
  </tr>
  <tr>
    <td>詳細</td>
    <td>data[0]: 左車輪角速度, data[1]: 右車輪角速度</td>
  </tr>
  <tr>
    <td>単位</td>
    <td>[rad/s]</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">コンフィギュレーション</td>
  </tr>
  <tr>
    <td colspan="2" >scaling</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>スケーリングファクタ</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>double</td>
  </tr>
  <tr>
    <td>GUIコントロール</td>
    <td>slider.0.1</td>
  </tr>
  <tr>
    <td>制約条件</td>
    <td>0.0<=x<=10.0</td>
  </tr>
  <tr>
    <td colspan="2" >tread</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>移動ロボットのトレッド幅</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>double</td>
  </tr>
  <tr>
    <td>GUIコントロール</td>
    <td>slider.0.01</td>
  </tr>
  <tr>
    <td>制約条件</td>
    <td>0.0<=x<=1.0</td>
  </tr>
  <tr>
    <td colspan="2" >print_xy</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>XYデータプリントのデバッグフラグ</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>string</td>
  </tr>
  <tr>
    <td>GUIコントロール</td>
    <td>radio</td>
  </tr>
  <tr>
    <td>制約条件</td>
    <td>(YES,NO)</td>
  </tr>
  <tr>
    <td colspan="2" >print_vel</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>velデータのデバッグプリントフラグ</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>string</td>
  </tr>
  <tr>
    <td>GUIコントロール</td>
    <td>radio</td>
  </tr>
  <tr>
    <td>制約条件</td>
    <td>(YES,NO)</td>
  </tr>
  <tr>
    <td colspan="2" >print_wvel</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>wheel_velデータのデバッグプリントフラグ</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>string</td>
  </tr>
  <tr>
    <td>GUIコントロール</td>
    <td>radio</td>
  </tr>
  <tr>
    <td>制約条件</td>
    <td>(YES,NO)</td>
  </tr>
</table>

この仕様に従い、RTCBuilderでPythonのテンプレートコードを生成します。

<div align="center"><a href="ministick_builder_basic.png"><img src="ministick_builder_basic.png" width="30%;"></a>
<a href="ministick_builder_activity.png"><img src="ministick_builder_activity.png" width="30%;"></a>
<a href="ministick_builder_dataport.png"><img src="ministick_builder_dataport.png" width="30%;"></a></div>;<br>
<div align="center"><a href="ministick_builder_configuration.png"><img src="ministick_builder_configuration.png" width="30%;"></a>
<a href="ministick_builder_documentation.png"><img src="ministick_builder_documentation.png" width="30%;"></a>
<a href="ministick_builder_lang.png"><img src="ministick_builder_lang.png" width="30%;"></a></div>;
<div align="center"><strong>RTCBuilderの設定画面(クリックすると拡大します)</strong></div>


## 実装

コンポーネントにADCの読み込みなどの機能を追加していきます。

### SPIモジュールの初期化


まず、コンポーネントのコンストラクタでSPIオブジェクトを生成し初期化します。

他の import 文の近くに、spidevをimportする一文を追加します。計算などで使用するのでmathモジュールもインポートします。


```
 # Import RTM module
 import RTC
 import OpenRTM_aist
 
 import math
 import spidev
```

さらに、コンストラクタで、必要な変数を初期化子、SPIオブジェクトを生成します。

```
 class Ministick(OpenRTM_aist.DataFlowComponentBase):
   def __init__(self, manager):
     OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
 
     self._scaling = [1.0]
     self._tread = [0.2]
     self._print_xy = ["NO"]
     self._print_vel = ["NO"]
     self._print_wvel = ["NO"]
     self.x = 0.0
     self.y = 0.0
     self.spi = spidev.SpiDev()
     self.spi.open(0, 0)
```

### get_adc 関数の追加

AD変換器からデータを読む関数を Ministickクラスに追加します。
<u>init</u>() 関数の次あたりに、以下の関数を追記します。

```
  def get_adc(self, channel):
    sned_ch = [0x00,0x08,0x10,0x18]
    if ((channel > 3) or (channel < 0)):
      return -1
    r = self.spi.xfer2([sned_ch[channel],0,0,0])
    ret = ((r[2] << 6 ) & 0x300) |  ((r[2] << 6) & 0xc0) | ((r[3] >> 2) & 0x3f)
    return ret
```

### X-Yの位置→車輪速度変換関数

X-Yの位置から車輪の速度へ変換する関数をMinistickクラスに追加します。

```
 dev xy_to_wvel(self, x, y):
   th = math.atan2(y, x)
   v = math.hypot(x, y)
   vl = v * math.cos(th - (math.pi/4.0))
   vr = v * math.sin(th - (math.pi/4.0))
   return (vl, vr)
```


### 車輪速度→速度ベクトル変換関数

車輪速度から速度ベクトルへ変換する関数をMinistickクラスに追加します。

```
 def wvel_to_vel2d(self, vl, vr):
   v = (vr + vl) / 2.0
   if v < 0.0:
     w = - (vr - vl) / self._tread[0]
   else:
     w = (vr - vl) / self._tread[0]
   return RTC.Velocity2D(v, 0.0, w)
```

### キャリブレーション

コンポーネント初期化時に、ジョイスティックのニュートラル位置をキャリブレーションします。
AD変換器からデータを100回程度読み込み平均し、オフセットデータとして保存します。

```
 def onInitialize(self):
```
     : 中略
```
    self.x_offset_v = 0.0
    self.y_offset_v = 0.0
    for i in range(1, 100):
      self.x_offset_v += self.get_adc(0)
      self.y_offset_v += self.get_adc(1)
    self.x_offset_v = self.x_offset_v / 100.0
    self.y_offset_v = self.y_offset_v / 100.0
 
    return RTC.RTC_OK
```

### onExecuteの実装

最後に、onExecute関数を実装します。

```
 def onExecute(self, ec_id):
    self.x = - (self.get_adc(0) - self.x_offset_v) * self._scaling[0] / 1000.0
    self.y = (self.get_adc(1) - self.y_offset_v) * self._scaling[0] / 1000.0
    if self._print_xy[0] != "NO":
      print "(x, y) = ", self.x, self.y
    self._d_pos.data = [self.x, self.y]
    
    self._d_wvel.data = self.xy_to_wvel(self.x, self.y)
    if self._print_wvel[0] != "NO":
      print "(vl, vr) = ", self._d_wvel.data[0], self._d_wvel.data[1]
    self._d_vel.data = self.wvel_to_vel2d(self._d_wvel.data[0],
                                          self._d_wvel.data[1])
    if self._print_vel[0] != "NO":
      print "(vx, va) = ", self._d_vel.data.vx, self._d_vel.data.va
 
    self._posOut.write()
    self._velOut.write()
    self._wvelOut.write()
 
    return RTC.RTC_OK
```


<!-- ============================================================ -->
## テスト

Ministickコンポーネントと、いろいろなものを接続してテストしてみます。

### OpenRTM-aist-Pythonに付属のサンプルと接続

TkMobileRobotCanvasと接続してみます。

Windows上のインストールされているOpenRTM-aist-Pythonのサンプルから TkMobileRobotCanvasを起動します。
同時に、ネームサービスとRTSystemEditorも起動してください。

<div align="center"><a href="tkmobilerobotcanvas.png"><img src="tkmobilerobotcanvas.png" width="80%;"></a></div>
<div align="center"><strong>Tk Mobile Robot Simulator 画面</strong></div>

Createボタンを押し、移動ロボットを一つ生成します。
ネームサーバにコンポーネントが一つ現れるので、SystemEditor上にドラッグアンドドロップします。

次に、Raspberry Pi上でネームサーバとMinistickコンポーネントを起動します。

```
 $ rtm-naming
 $ ./Ministick.py
 
```

RTSystemEditorから、RaspberryPiのネームサーバに接続すると、Ministickコンポーネントが見えますので、SystemEditor上にドラッグアンドドロップします。

Ministick の wvel データポートから先ほど生成した移動ロボットコンポーネントへポートを接続します。

<div align="center"><a href="ministick_and_mobilerobot.png"><img src="ministick_and_mobilerobot.png" width="80%;"></a></div>
<div align="center"><strong>Ministickと移動ロボットコンポーネントの接続</strong></div>

アクティベートすると、両方のコンポーネントが緑色になり操作可能になります。

### Kobukiと接続

前述のKobukiの制御、の節に従ってKobukiコンポーネントをRaspberryPi上で起動します。

<!-- - [移動ロボットKobukiの制御]({{ site.baseurl }}/ja/content/raspberrypi_kobuki_control)-->
- [移動ロボットKobukiの制御]({{ site.baseurl }}/ja/doc/installation/other/raspberrypi_casestudy/control_mobilerobot_kobuki)

Ministickコンポーネントを別のRaspberry Pi上で起動します。

それぞれのコンポーネントはローカルのネームサーバ(デフォルト)に参照を登録させて、別のPCからこれら2つのネームサーバにRTSystemEditorで接続します。
Name Service Viewに2つのコンポーネントが見えるはずですので、これら (Ministick の vel と KobukiAIST の targetVelocity) を接続します。(下図参照)

<div align="center"><a href="ministick_and_kobuki.png"><img src="ministick_and_kobuki.png" width="80%;"></a></div>
<div align="center"><strong>Ministick RTCとKobukiAIST RTCの接続</strong></div>

RTSystemEditorのメニューバーの緑色の再生ボタン(全活性化)を押すと、システムが動き出しMinistickでKobukiを操作できます。

## トラブルシューティング

### Ministickがニュートラル状態でもロボットが動く

Ministickがニュートラル状態でも、TkMobileRobotのロボットやKobukiが少しずつ動く場合があります。これは、ニュートラル状態のキャリブレーションが十分ではないためです。
Ministickコンポーネントを工夫して、使いやすいコンポーネントにしてみましょう。

例えば、キャリブレーションをonActivatedで行うようにすれば、一旦Deactivateして再度Activateすれば零点をリセットできます。
また、onDeactivatedの時には速度0を出力するようにすれば、JyoistickのDeactivateによりロボットが安全に停止します。
あるいは、零点付近に不感帯を設けることで、多少キャリブレーションがずれても、ニュートラル状態で必ず0が出力されるようにできます。

### Permission deniedエラー

以下のようなパーミッション関係のエラーが出ることがあります。
上述のudevの設定が正しく行われていない可能性がありますので、見直してください。

```
 pi@raspbian-armhf ~ $ ./adc_text.py
 Traceback (most recent call last):
   File "./adc_text.py", line 47, in <module>
     main()
   File "./adc_text.py", line 25, in main
     adc = ADC()
   File "./adc_text.py", line 10, in __init__
     self.spi.open(0, 0)
 IOError: [Errno 13] Permission denied
```

また、sudo を利用しても実行可能です。

