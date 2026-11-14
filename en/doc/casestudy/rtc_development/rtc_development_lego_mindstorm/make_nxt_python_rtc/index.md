---
layout: page
title: nxt python facade class
---

<!-- Title: NXT Python RTC 化 -->
With this, you are now ready to control NXT from a PC using Python.

You may now want to use RtcTemplate or similar tools to generate a template for an NXT component and start coding.
NXT Python is a well-organized Python module, but please wait before writing NXT Python code directly into the RTC template.

As you can see from the samples, NXT Python consists of multiple modules such as locators, motors, and sensors, and because it can control detailed functions for motors and sensors, the access methods are also somewhat complicated.

Here, we will create a class for grouping the multiple NXT Python modules together and accessing them through a single interface.
In terms of software patterns, this is the Façade pattern.

The Façade pattern, or Facade pattern, is one of the computer software design patterns defined by the GoF (Gang of Four). 
Facade means "front desk" or "interface." Its purpose is to eliminate redundancy in programs by consolidating the procedures for using a group of related classes into a single class that serves as the interface. (Source: Free encyclopedia "Wikipedia", Facade pattern)

Creating this kind of convenience class has the following advantages.

- The created class can be used for purposes other than RTCs
- Debugging becomes easier
  - It is easier to debug the Façade class by itself
  - If it is turned directly into an RTC, in this example it becomes difficult to distinguish whether the problem is with how NXT Python is used or how the RTC is used
- Changes become easier
  - Even if the Façade class is changed, the RTC-side code does not need to be changed as long as the interface is not changed
  - For example, if you want to add limiters to the input and output of functions such as get_xxx() and set_xxx(), only the Façade class needs to be changed
- Switching to devices other than NXT becomes easier
  - For example, if the next version of the NXT block is released, it will be easier to support it as long as the interface is the same.

This applies generally when creating RTCs.
By properly turning the target robot, device, or similar object into a class, you can respond flexibly to device changes and changes or version upgrades of the RTC itself, and create software that is robust against changes.

Never make primitive function calls such as the following in onExecute() or similar functions.


ioctl(xxxx, xxxx); // UNIX デバイスへの直アクセス
inb(xxx);          // I/O への直アクセス
outb(xxx);         // I/O への直アクセス

Ideally, it should be "high-level abstraction" code consisting only of calls to a function that "reads a value from an InPort and processes it" and a function that "obtains a value through some processing and outputs it from an OutPort," as shown below.

```
 onExecute(ec_id)
 { //　擬似コード
      if (m_inport.isNew())
     {
        retval = m_myrobot.set_actuator(m_inport.read());
        if (retval == fatal_error) return RTC::RTC_ERROR;
     }
     if (myrobot.get_sensor(sensor_data) == true)
     {
         m_outport.wrtie(sensor_data);
     } 
     else
     {// リードエラーの場合の処理
         if (fatal_error) return RTC::RTC_ERROR;
     }
     return RTC::RTC_OK;
 }
```
<br>
