---
layout: page
title: nxt python facade class
---

<!-- Title: NXT Python Facade クラス -->
## NXT Python Facade Class
NXT Python itself can use almost all functions of the NXT intelligent block, but using all of those functions directly becomes complicated, so we will create a Facade class that interfaces only with the functions we want to use.

The main functions of NXT are listed below.

- Input
  - Provide motor speed values
  - Provide sound pitch values
  - Provide messages to output to the LCD display
- Output
  - Read motor encoder values
  - Read sensor values (sound, ultrasonic, touch, light)
  - Read system information
- Others
  - Search for NXT
  - Connect to NXT
  - Read and write files on NXT
  - Read and write firmware

Creating a class that supports all of these at once would defeat the purpose of creating a Façade class.
You can update the Façade class each time a required function comes up.
Therefore, the Façade class created here will support only the following functions according to the robot being created this time.

- Input
  - Provide motor speed values: setMotors()
- Output
  - Read motor encoder values: getMotors()
  - Read sensor values (sound, ultrasonic, touch, light): getSensors()

The function names are rough examples.
The class (NXTBrick.py) created based on this idea is shown below.

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


The final part starting with **if <u>name</u> == "<u>main</u>":** is the test program. It is executed when this module is run by itself.
First, it is important to test this module until it works completely.

This completes the NXT Façade class.
Although it is a very simple class, we now have a class that can give speed values to the motors, read positions, and read sensor values.
If you try to make it do everything from the beginning, you will end up with a class whose purpose is unclear.
Since version upgrades can be done at any time, it is important to first create a class that works properly even with the minimum required functions.

