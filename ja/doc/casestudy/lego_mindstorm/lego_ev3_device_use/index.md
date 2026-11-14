---
layout: page
title: ev3 デバイスの利用
---

<!-- -*- pukiwiki-edit -*- -->
<!-- * EV3 デバイスの利用 -->
#contents

## LEGO Mindstorms のセンサーとモーター

LEGO Mindstorms EV3 には標準で、以下のようなモーター・センサーが付属しています。

- ジャイロセンサー x1
- カラーセンサー x1
- タッチセンサー x2
- 超音波距離センサー x1
- モーター（L）x2
- モーター（M）x1

センサー類は、プッシュスイッチは ON/OFF 値を取得可能で、超音波センサー、ジャイロセンサーは連続値を出力可能、カラーセンサーはいくつかの色を認識することもできます。
モーターは2種類（L、M)あり、それぞれ PWM（トルク）制御、速度制御、位置制御が可能で、これらの制御のゲイン等も変更できます。
以下に、EV3 のセンサーとモーターの使用を表示します。

<table class="table-alt">
  <tr>
    <td><strong>ジャイロセンサー</strong>
    </td>
    <td>確度モード: 精度 +/- 3°<br> 角速度モード: 最大 440 deg/sec <br> サンプリングレート 1,000 Hz</td>
  </tr>
  <tr>
    <td><strong>カラーセンサー</strong></td>
    <td>計測: 赤色光の反射光、周囲の明るさ、色 <br> 検出カラー数: 8色 （無色、黒、青、緑、黄、赤、白、茶）<br> サンプリングレート 1,000 Hz <br> 距離 約1mm～18mm（アフレル調査値）</td>
  </tr>
  <tr>
    <td><strong>タッチセンサー</strong></td>
    <td>オン (1)、オフ (0) <br> スイッチ可動域: 約4mm</td>
  </tr>
  <tr>
    <td><strong>超音波センサー</strong></td>
    <td>距離計測可能範囲: 3cmから250cm <br> 距離計測精度: +/- 1 cm <br> 前面電飾: 点灯：超音波発信中、点滅：超音波観測中</td>
  </tr>
  </tr>
  <tr>
  </tr>
  <tr>
  </tr>
  <tr>
    <td><strong>EV3 Lモーター</strong></td>
    <td>フィードバック: 1°単位 <br> 回転数: 160から170RPM <br> 定格トルク: 0.21 N・m (30oz*in) <br> 停動トルク: 0.42 N・m (60oz*in) <br> 重さ: 76 g</td>
  </tr>
  <tr>
    <td><strong>EV3 Mモーター</strong></td>
    <td>フィードバック 1°単位 <br> 回転数: 240から250RPM <br> 定格トルク: 0.08 N・m (11oz*in) <br> 停動トルク: 0.12 N・m (17oz*in) <br> 重さ: 36 g</td>
  </tr>
</table>


## sysfs 経由でのアクセス
ev3dev からこれらのデバイスにアクセスするには、sysfs という仕組みを経由してアクセスします。
sysfs は /sys 以下にある疑似的なファイルシステムで、ここに存在するファイルに値を書き込んだり読み込んだりすることで、モーターの制御やセンサーデータへのアクセスが可能になります。

sysfs 経由でのデバイスのアクセス方法に関しては、以下の ev3dev のドキュメントに詳細が記載されています。

- 様々なデバイスへのアクセス [http://www.ev3dev.org/docs/drivers/](http://www.ev3dev.org/docs/drivers/)
  - モーターリファレンス [http://www.ev3dev.org/docs/drivers/tacho-motor-class/](http://www.ev3dev.org/docs/drivers/tacho-motor-class/)
    - モーター制御チュートリアル: [http://www.ev3dev.org/docs/tutorials/tacho-motors/](http://www.ev3dev.org/docs/tutorials/tacho-motors/)
  - センサーリファレンス : [http://www.ev3dev.org/docs/drivers/lego-sensor-class/](http://www.ev3dev.org/docs/drivers/lego-sensor-class/)

具体的には、以下のようにアクセスします。

### モーターの制御例

モーターを連続回転するには、ポートAにモーター(L/Mどちらでもよい)をコマンドラインから以下のように入力します。

```
 # echo 50 > /sys/class/tacho-motor/motor0/duty_cycle_sp
 # echo run-forever > /sys/class/tacho-motor/motor0/command
```

現在の位置を表示させるにはこのように入力します。止めるには Ctrl+C 

```
 # while true; do echo -en "\033[0G$(cat /sys/class/tacho-motor/motor0/speed)   "; done
```
回転を止めるには、以下のように入力します。

```
 # echo stop > /sys/class/tacho-motor/motor0/command
```

### センサーの例

センサーなども同様のアクセス法で利用できます。
カラーセンサーをポート1に接続します。カラーセンサーの先1cm位のところに赤いものを置いてください。
以下のようなコマンドを入力すると、**5**と表示されます。

```
 # echo "COL-COLOR" > /sys/class/lego-sensor/sensor1/mode
 # cat /sys/class/lego-sensor/sensor1/value1
 5
```

カラーセンサーには、いくつかのモードがあり、上ではカラー検出モードを使用しました。このモードでは、以下の8つの色 (ただし、0は何もないことを意味する) を認識します。
<table class="table-alt">
  <tr>
    <td>色</td>
    <td>無</td>
    <td>黒</td>
    <td>青</td>
    <td>緑</td>
    <td>黄</td>
    <td>赤</td>
    <td>白</td>
    <td>茶</td>
  </tr>
  <tr>
    <td>番号</td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
  </tr>
</table>

コマンドラインからは以上のようにアクセスできますが、プログラムからこれらの操作をしようとすると非常に面倒な手続きが必要になります。

プログラムからデバイスにアクセスためのアクセスライブラリがありますので、これを利用します。


