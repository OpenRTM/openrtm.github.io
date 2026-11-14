---
layout: page
title: sample code explanation
---

<!-- Title: サンプルコードの説明 -->
#contents


### Sample Code Explanation
From here, we will incorporate the functionality of NXTBrick.py created earlier into NXTRTC.py.

- Importing NXTBrick.py
To use the NXTBrick class, import NXBrick.py.
Specify the file name without the extension (.py) as shown below for the import statement.
```
 import NXTBrick
```

- Implementing onInitialize(self)
In onInitialize(), instantiate the NXTBrick class.
If an error occurs during the instantiation process of the NXTBrick class, RTC_ERROR is returned and the state transitions to the exit state.
```
# create NXTBrick object
	try:
    	self._nxtbrick = NXTBrick.NXTBrick()
	except:
    	print "NXTBrick create failed."""
    	return RTC.RTC_ERROR
```

- Implementing onActivated(self, ec_id), onDeactivated(self, ec_id)
In onActivated() and onDeactivated(), call the resetPosition() method of the NXTBrick class.
```
    self._nxtbrick.resetPosition() 
```

- Implementing onExecute(self, ec_id)
In onExecute(), the following processing is performed.


  - Read velocity from the data InPort.
  - Use the Configuration function to determine which NXT port to output velocity to.
  - Output velocity to the motors using the setMotors() method of NXTBrick.
  - Obtain the ultrasonic sensor value of NXT using getSensors() of NXTBrick, and output it from the OutPort if data is available.
  - Obtain the rotation angle [deg] of NXT using getMotors() of NXTBrick, and output it from the OutPort if data is available.

The sample code summarizing the above is shown below.


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

### Sample Code Explanation (Example of Using a Callback Object)
In this sample, the callback OnWrite is added to the above sample and extended so that velocity is output to the motors when data is written to the InPort buffer.

- Callback class~
Write the callback class as follows.

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

This class takes an NTXBrick class object and the configuration variable map as arguments.

- Registering the callback class~
Register the callback object with the setOnWrite() method as shown below.

```
   # set callback class
   self._velIn.setOnWrite(CallBackClass(self._ntxbrick,self._map))
```

With setOnWrite(), the <u>call</u>()
method of CallBackClass will be called when data is written to the InPort.

The sample code summarizing the above is shown below.

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


In the first example, output to the motors, reading sensor values, and reading motor encoders were all performed synchronously in the same loop, but by using a callback, values can be output to the motors immediately when data arrives.



<!-- **NXTを自由に動かすコンポーネントを作ってみる -->
<!-- これで、NXTをRTコンポーネント化することができました。 -->
<!-- 次は、NXT RTCを自分独自のロジックで動かすためのコンポーネントを作ってみましょう。 -->
<!-- 上記のように、Pythonで作っても、もちろんC++やJavaで作っても構いません。 -->
<!-- どういった言語で作ったコンポーネントとも、このNXT RTCは接続することができます。 -->

