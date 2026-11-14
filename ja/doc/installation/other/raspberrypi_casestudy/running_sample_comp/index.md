---
layout: page
title: サンプルコンポーネントの実行
---

<!-- Title: サンプルコンポーネントの実行 -->
<!-- * GPIOを利用したサンプル -->

#contents

以下の例では、GPIO を用いて、スイッチの ON/OFF の検出と、LED の点灯を行うコンポーネント (DigitalIn-RTC、DigitalOut-RTC) を作成して Raspberry Pi の特徴である GPIO の利用について理解を深めます。
サンプルコンポーネントのソースコードは以下からダウンロードできます。

- [サンプルコンポーネントソース](RaspberryPi_sample.zip)

## Raspberry Pi の GIOP

Raspberry Pi には GPIO端子があり、これを利用することで様々な外部デバイスを利用することができます。

Raspberry Pi 本体に付属している GPIO のピンアサインを以下に示します｡

<div align="center"><a href="raspberrypi_gpio_pinassign.png"><img src="raspberrypi_gpio_pinassign.png" width="80%;"></a></div>
<div align="center"><strong>Raspberry Pi GPIO のピンアサイン</strong></div>

GPIO を使用する場合には、各ピンの位置に注意してください｡特に5V 端子を使用する場合、配線を誤ると Raspberry Pi 本体および SD カードを破壊してしまう危険がありますので、十分に注意してください｡

## ブレッドボード配線例

LED を点灯させる回路と、スイッチの ON/OFF を検出する回路を作成します。
ブレッドボード等があれば簡単に回路を組めますが、ない場合でも部品点数が少ないのでリード線をはんだ付けするなどすれば比較的容易に回路を組むことができるでしょう。
以下に、必要な部品のリストを示します。

<table class="table-alt">
  <tr>
    <th colspan="2" style="text-align: center;">部品表</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">LED回路</td>
  </tr>
  <tr>
    <td>LED</td>
    <td>1個</td>
  </tr>
  <tr>
    <td>抵抗</td>
    <td>100Ω (茶黒茶金) ～330Ω (橙橙茶金)</td>
  </tr>
  <tr>
    <td>リード線</td>
    <td>若干</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">スイッチLED回路</td>
  </tr>
  <tr>
    <td>LED</td>
    <td>1個</td>
  </tr>
  <tr>
    <td>抵抗</td>
    <td>330Ω (橙橙茶金) ～1kΩ (茶黒赤金)</td>
  </tr>
  <tr>
    <td>リード線</td>
    <td>若干</td>
  </tr>
</table>

Raspberry Pi が1台の場合は、以下の LEDとスイッチ回路を同じ Raspberry Pi に接続します。
もし、Raspberry Pi が2台あるなら、それぞれの Raspberry Pi に LED とスイッチを取り付けると面白いかもしれません。

### DigitalIn-RTC 用配線例

DigitalIn-RTC は、データポートに入力された bool 値 (true/false) を指定された GPIO ポートに出力するコンポーネントです。GPIO ポートの出力値を観測するために、**Ground**ピンと**GPIO 18**ピンに LED と抵抗を接続し下図のような回路を作成します。

<div align="center"><a href="gpio_led_circuit.png"><img src="gpio_led_circuit.png" width="80%;"></a></div>
<div align="center"><strong>LED 接続回路図</strong></div>

ブレッドボードでこの回路を作成する場合はこのようになります。

<div align="center"><a href="3_rp2.png"><img src="3_rp2.png" width="80%;"></a></div>
<div align="center"><strong>ブレッドボードによる LED 回路配線例</strong></div>

### DigitalOut-RTC 用配線例

DigitalOut-RTC は、GPIO ポートに入力された bool 値 (true/false) をデータポートから出力するコンポーネントです｡
GPIO に値を入力するために、**Ground**, **3.3V Power**, **GPIO 17**に抵抗とスイッチを接続して下図のような回路を作成します。

<div align="center"><a href="gpio_stiwch_circuit.png"><img src="gpio_stiwch_circuit.png" width="80%;"></a></div>
<div align="center"><strong>タクトスイッチ接続回路図</strong></div>

ブレッドボードでこの回路を作成する場合はこのようになります。

<div align="center"><a href="3_rp3.png"><img src="3_rp3.png" width="80%;"></a></div>
<div align="center"><strong>ブレッドボードによりスイッチ回路配線例</strong></div>

## コンポーネントのコンパイル

ソースコードを以下から Raspberry Pi にダウンロードして、DigitalIn-RTC/DigitalOut-RTC コンポーネントをコンパイルします。

- [サンプルコンポーネントソース](RaspberryPi_sample.zip)

### DigitalIn-RTC のコンパイル

```
 $ unzip RaspberryPi_sample.zip
 $ cd RaspberryPi_sample/DigitalInRPI/
 $ vi CMakeLists.txt
```

ここで、CMakeLists.txt を書き換えて、ドキュメントの生成を抑制するよう設定します。

```
 option(BUILD_DOCUMENTATION "Build the documentation" OFF)
  ↓
 option(BUILD_DOCUMENTATION "Build the documentation" ON)
 
 $ mkdir build
 $ cd build
 $ cmake ..
 -- The C compiler identification is GNU 4.6.3
 -- The CXX compiler identification is GNU 4.6.3
   : 中略
 -- Configuring done
 -- Generating done
 -- Build files have been written to: /home/pi/RaspberryPi_sample/DigitalInRPI/build
```

OpenRTM-aist が正しくインストールされていれば、問題なく configure が終了します。
もし、OpenRTM や coil が無いなどでエラーが出た場合、OpenRTM-aist (C++版) が正しくインストールされていることを確認 (dpkg -l |grep openrtm 等) してください。

```
 $ make
  : 中略
 Scanning dependencies of target DigitalInComp
 [ 66%] Building CXX object src/CMakeFiles/DigitalInComp.dir/DigitalInComp.cpp.o
 [100%] Building CXX object src/CMakeFiles/DigitalInComp.dir/DigitalIn.cpp.o
 Linking CXX executable DigitalInComp
 [100%] Built target DigitalInComp
 $
```

コンパイルされたコンポーネント DigitalInComp は src の下にあります。

```
 $ ls src/
 CMakeFiles  cmake_install.cmake  DigitalInComp  DigitalIn.so  Makefile
```

### DigitalOut-RTC のコンパイル

DigitalIn-RTC と同様にコンパイルします。

```
 $ cd RaspberryPi_sample/DigitalOutRPI/
 $ mkdir build
 $ vi CMakeLists.txt
```

ここで、CMakeLists.txt を書き換えて、ドキュメントの生成を抑制するよう設定します。

```
 option(BUILD_DOCUMENTATION "Build the documentation" OFF)
  ↓
 option(BUILD_DOCUMENTATION "Build the documentation" ON)
 
 $ mkdir build
 $ cd build
 $ cmake ..
 -- The C compiler identification is GNU 4.6.3
 -- The CXX compiler identification is GNU 4.6.3
   : 中略
 -- Configuring done
 -- Generating done
 -- Build files have been written to: /home/pi/RaspberryPi_sample/DigitalOutRPI/build
```
続いて make します。

```
 $ make
 -- OpenRTMConfig.cmake found.
 -- Configrued by configuration mode.
  : 中略
 Scanning dependencies of target DigitalOutComp
 [ 66%] Building CXX object src/CMakeFiles/DigitalOutComp.dir/DigitalOutComp.cpp.o
 [100%] Building CXX object src/CMakeFiles/DigitalOutComp.dir/DigitalOut.cpp.o
 Linking CXX executable DigitalOutComp
 [100%] Built target DigitalOutComp
 $
```

コンパイルされたコンポーネント DigitalOutComp は src の下にあります。

```
 $ ls src/
 CMakeFiles  cmake_install.cmake  DigitalOutComp  DigitalOut.so  Makefile
```

## コンポーネントの実行

各RTC が正常にコンパイルできたら、NameServer を起動後、各RTC を起動します｡

```
 $ rtm-naming
 $ sudo  /home/pi/RaspberryPi_sample/DigitalOutRPI/build/src/DigitalOutComp &
 $ sudo  /home/pi/RaspberryPi_sample/DigitalInRPI/build/src/DigitalInComp &
```

**<span style="color:red;">サンプルコンポーネントは GPIO を利用するので root 権限で実行する必要があります｡</span>**

PC上で RTSystemEditor を起動し、Raspberry Pi上の NameServewr に接続します｡
各RTC を配置し、ポート間の接続を行った後、活性化(Activate)します｡

<div align="center"><a href="3_rp4.png"><img src="3_rp4.png" width="80%;"></a></div>
<div align="center"><strong>サンプル RTC の実行</strong></div>

各RTC が正常に起動すると、タクトスイッチの状態に応じて、LED が点灯/消灯するようになります｡


<hr>
# コメント

### naming serverの設定について

パーマリンク Submitted by SUZUKAWA yuichi on 火, 2013-04-23 00:53.

<table class="table-alt">
 <tr>
<td>
早速、この方法で試してみたのですが、Naming Serverが立ち上がったのに、Eclips上に表示されなくて悩みました。

力技で、Raspberry pi 側の naming serverのHost server名を192.168.0.X:100などのように設定して無理やりポート開きました。 通常だと、ローカルホストになるので「Raspberry pi：ポートナンバー」の様に表示されて、入れないです。

</td>
 </tr>
 </table>

### Raspberry pi UART通信コンポーネントの作成について

パーマリンク Submitted by SUZUKAWA yuichi on 火, 2013-04-23 01:02.

<table class="table-alt">
 <tr>
<td>
追加ですが、簡単なUART通信のループバックコンポーネントを作ったらうまくいきました。

プログラムは以下のサイト様を参考にさせて頂きました。

ほぼ移植で動きます。

参考サイト ・Chick Lab様 Raspberry Pi でシリアル通信 http://chicklab.blog84.fc2.com/blog-entry-46.html ・工作と小物のがらくた部屋様 http://junkroom2cyberrobotics.blogspot.jp/2013/03/raspberry-pi-uart.html

</td>
 </tr>
 </table>
