---
layout: page
title: 動作確認
---

<!-- Title: 動作確認 -->
#contents

Raspberry Pi にログイン後、コマンドからデバイスファイルを操作することで動作確認を行います。
各デバイスの位置などは [ラズパイマウスのマニュアル](http://resources.rt-net.jp/products/RPiM/raspberryPiMouseManual_2015_08_04.pdf) を参考にしてください。

# LED
以下のコマンドで LED が点灯、消灯しているかを確認してください。

```
 echo 1 > /dev/rtled0
 echo 0 > /dev/rtled0
```

```
 echo 1 > /dev/rtled1
 echo 0 > /dev/rtled1
```

```
 echo 1 > /dev/rtled2
 echo 0 > /dev/rtled2
```

```
 echo 1 > /dev/rtled3
 echo 0 > /dev/rtled3
```

# スイッチ
スイッチを押した状態、離した状態で以下のコマンドを入力してください。

```
 cat /dev/rtswitch0
 cat /dev/rtswitch1
 cat /dev/rtswitch2
 cat /dev/rtswitch3
```



# ブザー
以下のコマンドでブザーが鳴るかを確認してください。

```
 echo 440 > /dev/rtbuzzer0
 echo 0 > /dev/rtbuzzer0
```

## 距離センサー
距離センサーに物体を近づけた状態、離した状態で以下のコマンドを入力してください。

```
 cat /dev/rtlightsensor0
```

# モーター
最初にモーター電源スイッチを ON にしてください。
<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm10.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm10.png" width="60%;"></a></div>

以下のコマンドで車輪が回転するかを確認してください。

```
 echo 1 > /dev/rtmotoren0
 
 echo 400 > /dev/rtmotor_raw_l0
 echo -400 > /dev/rtmotor_raw_l0
 echo 0 > /dev/rtmotor_raw_l0
 
 echo 400 > /dev/rtmotor_raw_r0
 echo -400 > /dev/rtmotor_raw_r0
 echo 0 > /dev/rtmotor_raw_r0
 
 echo 0 > /dev/rtmotoren0
```

終わったらモーター電源スイッチを OFF にしてください。
