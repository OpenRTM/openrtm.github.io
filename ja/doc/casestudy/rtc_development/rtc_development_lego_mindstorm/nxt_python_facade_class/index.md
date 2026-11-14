---
layout: page
title: nxt python facade クラス
---

<!-- Title: NXT Python Facade クラス -->
## NXT Python Facade クラス
NXT Python 自体は NXTインテリジェントブロックのほとんどすべての機能を使用することができますが、それらの機能すべてを直接使用するのは煩雑になるため、利用したい機能のみをインターフェースする Facade クラスを作ります。

NXT の主な機能を列挙します。

- 入力
  - モーター速度値を与える
  - サウンドの音程値を与える
  - 液晶表示に出力するメッセージを与える
- 出力
  - モーターエンコーダ値を読む
  - センサー値(サウンド、超音波、タッチ、光)の値を読む
  - システム情報を読む
- その他
  - NXT の検索
  - NXT への接続
  - NXT のファイルの読み書き
  - ファームウエアの読み書き

これらすべてを一度にサポートするクラスを作るのでは Façade クラスを作る意味がなくなってしまいます。
必要な機能が出てきたらそのつど Façade クラスを更新すればよいのです。
したがって、ここで作成する Façade クラスでは、今回作成するロボットに合わせて、以下の機能のみをサポートすることにします。

- 入力
  - モーター速度値を与える: setMotors()
- 出力
  - モーターエンコーダ値を読む: getMotors()
  - センサー値 (サウンド、超音波、タッチ、光) の値を読む: getSensors()

関数名はおおよそのイメージです。
この考え方で作成したクラス (NXTBrick.py) を以下に示します。

```
 #!/usr/bin/env python
 # @file NXTBrick.py
 # -*- coding:shift_jis -*-
 import nxt.locator
 from nxt.sensor import *
 from nxt.motor import *
 class NXTBrick:
     def __init__(self, bsock=None):
         コンストラクタ
         NXT ブロックへのコネクションを行い、モーターや、センサーオブジェクトを
         作成する。モーターのエンコーダのリセットを行う。
         """
         if bsock:
             self.sock = bsock
         else:
             self.sock = nxt.locator.find_one_brick().connect()
         self.motors = [Motor(self.sock, PORT_A),
                        Motor(self.sock, PORT_B),
                        Motor(self.sock, PORT_C)]
             
         self.sensors = [TouchSensor(self.sock, PORT_1),
                         SoundSensor(self.sock, PORT_2),
                         LightSensor(self.sock, PORT_3),
                         UltrasonicSensor(self.sock, PORT_4)]
         self.resetPosition()
 
     def close(self):
         """
         NXT ブロックとの接続を終了する
         """
         self.sock.close()
 
     def resetPosition(self, relative = 0):
         """
         NXT のモーターのエンコーダをリセットする
         """
         for m in self.motors:
             m.reset_position(relative)
 
     def setMotors(self, vels):
         """
         配列を受け取り、モーターのパワーとしてセットする。
         vels の数とモーターの数が一致しない場合、両者の要素数のうち小さい方でループを回す。
         """
         for i, v in enumerate(vels[:min(len(vels),len(self.motors))]):
             self.motors[i].power = max(min(v,127),-127)
             self.motors[i].mode = MODE_MOTOR_ON | MODE_REGULATED
             self.motors[i].regulation_mode = REGULATION_MOTOR_SYNC
             self.motors[i].run_state = RUN_STATE_RUNNING
             self.motors[i].tacho_limit = 0
             self.motors[i].set_output_state()
 
     def getMotors(self):
         """
         モーターの位置(角度)を取得する
         
         """
         state = []
         for m in self.motors:
             state.append(m.get_output_state())
         return state
 
     def getSensors(self):
         """
         センサの値を取得する。得られたデータは配列で返される。
         """
         state = []
         for s in self.sensors:
             state.append(s.get_sample())
         return state
 
 
 """
 テストプログラム
 モーターに適当な出力を与え、角度を読み表示する。
 センサから値を読み込み表示する。
 """
 if __name__ == "__main__":
     import time
     nxt = NXTBrick()
     print "connected"
     
     # モーターのテスト
     for i in range(100):
         nxt.setMotors([80,-80,80])
         print "Motor: "
         mstat = nxt.getMotors()
         for i, m in enumerate(mstat):
             print "(" , i, "): ", m
         time.sleep(0.1)
     nxt.setMotors([0,0,0])
 
     # センサーのテスト
     for i in range(100):
         sensors = ["Touch", "Sound", "Light", "USonic"]
         sval = nxt.getSensors()
         for s in sensors:
             print s + ": " + sval
             print ""
             time.speel(0.1)
```


最後の **if <u>name</u> == "<u>main</u>":**から始まる部分はテストプログラムです。このモジュールを単体で動かしたときに実行されます。
まずは、このモジュールが完全に動くまでテストをすることが重要です。

以上で、NXT の Façade クラスができました。
非常に簡単なクラスですが、モーターに速度を与え、ポジションを読み、センサーの値を読むことのできるクラスができました。
はじめから何でもできるようにしようとすると、結局何をするためのクラスなのかよくわからないクラスができてしまいます。
バージョンアップはいつでもできるので、まずは最低限の機能でもちゃんと動くクラスを作ることが重要です。



