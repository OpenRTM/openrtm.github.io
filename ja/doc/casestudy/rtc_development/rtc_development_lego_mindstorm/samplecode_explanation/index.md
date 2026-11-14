---
layout: page
title: サンプルコードの説明
---

<!-- Title: サンプルコードの説明 -->
#contents


### サンプルコードの説明
ここから、NXTRTC.py に先ほど作成した NXTBrick.py の機能を組み込んでいきます。

- NXTBrick.py のインポート
NXTBrick クラスを使用するために NXBrick.py をインポートします。
import の記述方法は、下記のように拡張子(.py)を除いたファイル名を指定します。
```
 import NXTBrick
```

- onInitialize(self) の実装
onInitialize()で、NXTBrick クラスのインスタンス化を行います。
NXTBrick クラスのインスタンス化過程にてエラーが発生した場合、RTC_ERROR が戻り
終了状態へ遷移します。
```
# create NXTBrick object
	try:
    	self._nxtbrick = NXTBrick.NXTBrick()
	except:
    	print "NXTBrick create failed."""
    	return RTC.RTC_ERROR
```

- onActivated(self, ec_id),onDeactivated(self, ec_id) の実装
onActivated(),onDeactivated()では、NXTBrickクラスのresetPosition() メソッドをコールします。
```
    self._nxtbrick.resetPosition() 
```

- onExecute(self, ec_id) の実装
onExecute() では、下記の処理を行ってます。


  - データ InPort からの速度の読み込み。
  - Configuration 機能を用い NXT のどのポートへ速度出力を行うかを決定。
  - NXTBrick の setMotors() メソッドにてモーターへ速度を出力。
  - NXTBrick の getSensors() にて NTX の超音波センサー値を取得し、データがあれば OutPort から出力。
  - NXTBrick の getMotors() にて NTX の回転角度[deg]を取得し、データがあれば OutPort から出力。

上記をまとめたサンプルコードを以下に示す。


```
 #!/usr/bin/env python
 # -*- coding:shift_jis -*-
 # -*- Python -*-
 
 import sys
 import time
 sys.path.append(".")
 
 # Import RTM module
 import OpenRTM
 import RTC
  
 # import NXTBrick class
 import NXTBrick
  
 # This module's spesification
 # <rtc-template block="module_spec">
 nxtrtc_spec = ["implementation_id", "NXTRTC", 
 		 "type_name",         "NXTRTC", 
 		 "description",       "NXT sample component", 
 		 "version",           "0.1", 
 		 "vendor",            "AIST", 
 		 "category",          "example", 
 		 "activity_type",     "DataFlowComponent", 
 		 "max_instance",      "10", 
 		 "language",          "Python", 
 		 "lang_type",         "SCRIPT",
 		 "conf.default.map", "A,B",
 		 ""]
 
 # </rtc-template>
 
 class NXTRTC(OpenRTM.DataFlowComponentBase):
 	def __init__(self, manager):
 		OpenRTM.DataFlowComponentBase.__init__(self, manager)
 
 		# DataPorts initialization
 		# <rtc-template block="data_ports">
 		self._d_vel = RTC.TimedFloatSeq(RTC.Time(0,0),[])
 		self._velIn = OpenRTM.InPort("vel", self._d_vel, OpenRTM.RingBuffer(8))
 		self.registerInPort("vel",self._velIn)
 		self._d_pos = RTC.TimedFloatSeq(RTC.Time(0,0),[])
 		self._posOut = OpenRTM.OutPort("pos", self._d_pos, OpenRTM.RingBuffer(8))
 		self.registerOutPort("pos",self._posOut)
 		self._d_sens = RTC.TimedFloatSeq(RTC.Time(0,0),[])
 		self._sensOut = OpenRTM.OutPort("sens", self._d_sens, OpenRTM.RingBuffer(8))
 		self.registerOutPort("sens",self._sensOut)
 
 		# initialize of configuration-data.
 		# <rtc-template block="configurations">
 		self._map = [['A', 'B']]
 		self._nxtbrick = None
 		self._mapping = {'A':0,'B':1,'C':2}
 		 
 	def onInitialize(self):
 		# Bind variables and configuration variable
 		# <rtc-template block="bind_config">
 		self.bindParameter("map", self._map, "A,B")
 
 		# create NXTBrick object
 		try:
 			print "Connecting to NXT brick ...."
 			self._nxtbrick = NXTBrick.NXTBrick()
 			print "Connection established."
 		except:
 			print "NXTBrick connection failed."
 			return RTC.RTC_ERROR
 
 		return RTC.RTC_OK
 
 	def onFinalize(self):
 		self._nxtbrick.close()
 
 	def onActivated(self, ec_id):
 		# reset NXTBrick's position.
 		self._nxtbrick.resetPosition()
 
 		return RTC.RTC_OK
 
 	def onDeactivated(self, ec_id):
 		# reset NXTBrick's position.
 		self._nxtbrick.resetPosition()
 
 		return RTC.RTC_OK
 
 	def onExecute(self, ec_id):
 		cnt = 0
 		# check new data.
 		if self._velIn.isNew():
 			# read velocity data from inport.
 			self._d_vel = self._velIn.read()
 			vel_ = [0,0,0]
 			vel_[self._mapping[self._map[0][0]]] = self._d_vel.data[0]
 			vel_[self._mapping[self._map[0][1]]] = self._d_vel.data[1]
 			# set velocity
 			self._nxtbrick.setMotors(vel_)
 
 		# get sensor data.
 		sensor_   = self._nxtbrick.getSensors()
 		if sensor_:
 			self._d_sens.data = sensor_
 			self._sensOut.write()
 
 		# get position data.
 		position_ = self._nxtbrick.getMotors()
 		if position_:
 			self._d_pos.data = \
 			    [position_[self._mapping[self._map[0][0]]][9], \
 				     position_[self._mapping[self._map[0][1]]][9]]
 		# write position data to outport.
 		self._posOut.write()
 
 		return RTC.RTC_OK
 
   def MyModuleInit(manager):
     profile = OpenRTM.Properties(defaults_str=nxtrtc_spec)
     manager.registerFactory(profile,
                             NXTRTC,
                             OpenRTM.Delete)
 
     # Create a component
     comp = manager.createComponent("NXTRTC")
 
  def main():
 	mgr = OpenRTM.Manager.init(len(sys.argv), sys.argv)
 	#mgr = OpenRTM.Manager.init(sys.argv)
 	mgr.setModuleInitProc(MyModuleInit)
 	mgr.activateManager()
 	mgr.runManager()
 
 if __name__ == "__main__":
 	main()
```

### サンプルコードの説明(コールバックオブジェクトの使用例)
このサンプルでは上記のサンプルにコールバック OnWrite を追加し、InPort のバッファへデータが書き込まれた際にモーターへの速度出力を行うように拡張します。

- コールバッククラス~
下記のようにコールバッククラスを記述します。

```
 # @class CallBackClass
 # @brief callback class
 #
 # when data is written in the buffer of InPort,
 # it is called.
 class CallBackClass:
 	def __init__(self, nxtbrick_, map_):
 		self._nxtbrick = nxtbrick_
 		self._map = map_
 		self._mapping = {'A':0,'B':1,'C':2}
 
 	def __call__(self, pData):
 		vel_ = [0,0,0]
 		vel_[self._mapping[self._map[0][0]]] = pData.data[0]
 		vel_[self._mapping[self._map[0][1]]] = pData.data[1]
 		# set velocity
 		self._nxtbrick.setMotors(vel_)
```

このクラスでは、NTXBrick クラスのオブジェクトとコンフィギュレーション変数 map を引数にとります。

- コールバッククラスの登録~
下記のように、setOnWrite() メソッドにてコールバックオブジェクトを登録します。

```
   # set callback class
   self._velIn.setOnWrite(CallBackClass(self._ntxbrick,self._map))
```

setOnWrite() により、InPort へデータが書き込まれた際に、CallBackClassの<u>call</u>()
メソッドが呼ばれるようになります。

上記をまとめたサンプルコードを以下に示す。

```
 #!/usr/bin/env python
 # -*- coding:shift_jis -*-
 # -*- Python -*-
 
 import sys
 import time
 sys.path.append(".")
 
 # Import RTM module
 import OpenRTM
 import RTC
  
 # import NXTBrick class
 import NXTBrick
 
  # This module's spesification
 # <rtc-template block="module_spec">
 nxtrtc_spec = ["implementation_id", "NXTRTC", 
 		 "type_name",         "NXTRTC", 
 		 "description",       "NXT sample component", 
 		 "version",           "0.1", 
 		 "vendor",            "AIST", 
 		 "category",          "example", 
 		 "activity_type",     "DataFlowComponent", 
 		 "max_instance",      "10", 
 		 "language",          "Python", 
 		 "lang_type",         "SCRIPT",
 		 "conf.default.map", "A,B",
 		 ""]
 
 # </rtc-template>
 
 # @class CallBackClass
 # @brief callback class
 #
 # when data is written in the buffer of InPort,
 # it is called.
 class CallBackClass:
 	def __init__(self, nxtbrick_, map_):
 		self._nxtbrick = nxtbrick_
 		self._map = map_
 		self._mapping = {'A':0,'B':1,'C':2}
 
 	def __call__(self, pData):
 		vel_ = [0,0,0]
 		vel_[self._mapping[self._map[0][0]]] = pData.data[0]
 		vel_[self._mapping[self._map[0][1]]] = pData.data[1]
 		# set velocity
 		self._nxtbrick.setMotors(vel_)
 
  class NXTRTC(OpenRTM.DataFlowComponentBase):
 	def __init__(self, manager):
 		OpenRTM.DataFlowComponentBase.__init__(self, manager)
 
 		# DataPorts initialization
 		# <rtc-template block="data_ports">
 		self._d_vel = RTC.TimedFloatSeq(RTC.Time(0,0),[])
 		self._velIn = OpenRTM.InPort("vel", self._d_vel, OpenRTM.RingBuffer(8))
 		self.registerInPort("vel",self._velIn)
 		self._d_pos = RTC.TimedFloatSeq(RTC.Time(0,0),[])
 		self._posOut = OpenRTM.OutPort("pos", self._d_pos, OpenRTM.RingBuffer(8))
 		self.registerOutPort("pos",self._posOut)
 		self._d_sens = RTC.TimedFloatSeq(RTC.Time(0,0),[])
 		self._sensOut = OpenRTM.OutPort("sens", self._d_sens, OpenRTM.RingBuffer(8))
 		self.registerOutPort("sens",self._sensOut)
 
 		# initialize of configuration-data.
 		# <rtc-template block="configurations">
 		self._map = [['A', 'B']]
 		self._nxtbrick = None
 		self._mapping = {'A':0,'B':1,'C':2}
 		 
 	def onInitialize(self):
 		# Bind variables and configuration variable
 		# <rtc-template block="bind_config">
 		self.bindParameter("map", self._map, "A,B")
 
 		# create NXTBrick object
 		try:
 			print "Connecting to NXT brick ...."
 			self._nxtbrick = NXTBrick.NXTBrick()
 			print "Connection established."
 		except:
 			print "NXTBrick connection failed."
 			return RTC.RTC_ERROR
 
 		# set callback class
 		self._velIn.setOnWrite(CallBackClass(self._ntxbrick,self._map))
 
 		return RTC.RTC_OK
 
 	def onFinalize(self):
 		self._nxtbrick.close()
 
 	def onActivated(self, ec_id):
 		# reset NXTBrick's position.
 		self._nxtbrick.resetPosition()
 
 		return RTC.RTC_OK
  
 	def onDeactivated(self, ec_id):
 		# reset NXTBrick's position.
 		self._nxtbrick.resetPosition()
 
 		return RTC.RTC_OK
  
 	def onExecute(self, ec_id):
 		# get sensor data.
 		sensor_   = self._nxtbrick.getSensors()
 		if sensor_:
 			self._d_sens.data = [sensor_[3]]
 			# write sensor data to outport.
 			self._sensOut.write()
 
 		# get position data.
 		position_ = self._nxtbrick.getMotors()
 		if position_:
 			self._d_pos.data = [position_[self._mapping[self._map[0][0]]][9],position_[self._mapping[self._map[0][1]]][9]]
 			# write position data to outport.
 			self._posOut.write()
 
 		return RTC.RTC_OK
  
 def MyModuleInit(manager):
     profile = OpenRTM.Properties(defaults_str=nxtrtc_spec)
     manager.registerFactory(profile,
                             NXTRTC,
                             OpenRTM.Delete)
 
     # Create a component
     comp = manager.createComponent("NXTRTC")
  
 def main():
 	mgr = OpenRTM.Manager.init(len(sys.argv), sys.argv)
 	#mgr = OpenRTM.Manager.init(sys.argv)
 	mgr.setModuleInitProc(MyModuleInit)
 	mgr.activateManager()
 	mgr.runManager()
 
 if __name__ == "__main__":
 	main()
```


はじめの例では、モーターへの出力、センサー値の読み込み、モーターエンコーダの読み込みをすべて同一ループで同期的に行っていましたが、コールバックを使用することで、データが来たらすぐにモーターへ値を出力できるようになります。



<!-- **NXTを自由に動かすコンポーネントを作ってみる -->
<!-- これで、NXTをRTコンポーネント化することができました。 -->
<!-- 次は、NXT RTCを自分独自のロジックで動かすためのコンポーネントを作ってみましょう。 -->
<!-- 上記のように、Pythonで作っても、もちろんC++やJavaで作っても構いません。 -->
<!-- どういった言語で作ったコンポーネントとも、このNXT RTCは接続することができます。 -->



