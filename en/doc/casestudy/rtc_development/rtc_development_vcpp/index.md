---
layout: page
title: creating rt components (vc++ edition)
---

<!-- Title: RTコンポーネント作成(VC++編) -->
#contents

# Component with Data Ports

Here, we create a component (MRCConvertor) with two data ports using VC8.

## Component Overview 

A component that converts data from an input device into the speeds of two wheels and outputs them from an OutPort.

It can be used when operating a mobile robot (two front wheels, one rear wheel, only the front wheels are driven) with an input device such as a joystick.


The specifications of the RTC to be created are as follows.

- InPort
  - Velocity for the mobile robot (TimedFloatSeq)

- OutPort
  - Wheel velocities of the mobile robot (TimedFloatSeq)

## Generating the MRCConvertor Template 

Generate the template with RtcTemplate.

### Creating a Working Folder 
Create a working folder in an appropriate location.

This time, use the same folder name as the component name (MRCConvertor).

1. Double-click "My Computer"
1. Move to the folder where you want to create the working folder
1. Right-click and create a folder from [New] > [Folder]

### CUI Version rtc-template Edition (gen.bat)

To make it easy to execute rtc-template, create a batch file like the following in the working folder created earlier.

```
 rtc-template.py -bcxx^
  --module-name=MRCConvertor --module-desc="Convertor component for MobileRobot component"^
  --module-version=1.0.0 --module-vendor=AIST --module-category=Category^
  --module-comp-type=DataFlowComponent --module-act-type=PERIODIC^
  --module-max-inst=1^
  --inport=velFromInput:TimedFloatSeq^
  --outport=velToWheel:TimedFloatSeq
```

### Executing rtc-template (gen.bat)

Execute the gen.bat file as shown below.

```
 >gen.bat
  rtc-template.py -bcxx
  --module-name=MRCConvertor
  --module-desc="Convertor component for MobileRobot component"
  --module-version=1.0.0 --module-vendor=AIST
  --module-category=Category
  --module-comp-type=DataFlowComponent --module-act-type=PERIODIC
  --module-max-inst=1
  --inport=velFromInput:TimedFloatSeq --outport=velToWheel:TimedFloatSeq

   File "MRCConvertor.h" was generated.
   File "MRCConvertor.cpp" was generated.
   File "MRCConvertorComp.cpp" was generated.
   File "Makefile.MRCConvertor" was generated.
   File "MRCConvertorComp_vc8.vcproj" was generated.
   File "MRCConvertor_vc8.vcproj" was generated.
   File "MRCConvertorComp_vc9.vcproj" was generated.
   File "MRCConvertor_vc9.vcproj" was generated.
   File "MRCConvertor_vc8.sln" was generated.
   File "MRCConvertor_vc9.sln" was generated.
   File "copyprops.bat" was generated.
   File "user_config.vsprops" was generated.
   File "README.MRCConvertor" was generated.
   File "MRCConvertor.yaml" was generated.
```

### Eclipse Version RtcTemplate Edition 

The settings in the Eclipse version RtcTemplate are as follows.

- Programing language selection: C++
- Module definition
  - Module name: MRCConvertor
  - Module decription: Convertor component for MobileRobot component
  - Module version: 1.0.0
  - Module vender: AIST
  - Module category: Category
  - Component type: DataFlowComponent
  - Component's activity type: PERIODIC
  - Number of maximum instance: 1
- InPort definition
  - Ports: Name:velFromInput Type:TimedFloatSeq
- OutPort definition
  - Ports: Name:velToWheel, Type:TimedFloatSeq


### Running copyprops.bat 

By executing RtcTemplate, the copyprops.bat file is generated in the working folder.

Using this copyprops.bat file, copy rtm_config.vsprops, which is required to build the component, to the working folder.

Double-click the copyprops.bat file.


## Implementing MRCConvertor 

### Starting Visual Studio 

Double-click MRCConvertorComp_vc8.vcproj to start Visual Studio.

### Editing the Header File

In the Visual Studio Solution Explorer, click MRCConvertorComp > Header Files in this order, then double-click MRCConvertor.h.

#### Including Header Files
This time, we will use std::vector and the math library, so include the two header files.

```
 #include <vector>
 // VC8 にて Math::M_PI を使用するため
 #define _USE_MATH_DEFINES
 #include <math.h>
```


- Uncomment the "virtual RTC::ReturnCode_t onExecute(RTC::UniqueId ec_id);" function.

- Declaring member variables and methods~
This time, declare the convert() method for converting the movement vector of MobileRobot (two front wheels, one rear wheel, only the front wheels are driven) into wheel velocities, and the coefficient m_k required for the conversion.


```
 private:  float m_k;
 
  /*!
   * @brief InPortからのデータ(X、Y) をMobileRobot用の車輪速度データに変換する。
   *        m_velFromInput.data[0]とm_velFromInput.data[1]だけを使用する。
   */
  std::vector<float> convert(float x, float y) {
	float th = atan2(y,x);
	float v  = m_k * hypot(x,y);
	std::vector<float> ret_val;
	ret_val.push_back(v * cos(th - (M_PI/4.0))); // left vel
	ret_val.push_back(v * sin(th - (M_PI/4.0))); // right vel
	return ret_val;
  }
```

### Editing the Source File 

In the Visual Studio Solution Explorer, click MRCConvertorComp > Source Files in this order, then double-click MRCConvertor.cpp.


#### Implementing onExecute()
Uncomment onExecute() and implement it as follows.


```
 /*!
  * @brief InPort からのデータ (X、Y) を MobileRobot用の車輪速度データに変換し、
  *        OutPort から出力する。
  */

 RTC::ReturnCode_t MRCConvertor::onExecute(RTC::UniqueId ec_id)
 {
   if (m_velFromInputIn.isNew()) {
 	m_velFromInputIn.read();
 	if (m_velFromInput.data.length() > 2) {
 	  std::vector<float>  con_val = this->convert(m_velFromInput.data[0],m_velFromInput.data[1]);
 	  for (int i = 0; i < 2; i++)
 		m_velToWheel.data[i] = con_val[i];
 	  m_velToWheelOut.write();
 	}
   }
   return RTC::RTC_OK;
 }
```

The processing performed here is as follows:

1. Check whether data has arrived at the InPort with m_velFromInputIn.isNew().
1. If new data has arrived, read the data into the variable with m_velFromInputIn.read().
1. Convert the read data into wheel velocities with convert().
1. Set the converted data in the OutPort variable and write it to the OutPort buffer.


## Build

From the Visual Studio menu, click [Build] > [Build Solution] to build the component.


## Creating rtc.conf 

In an editor, write the following content and save it with the file name rtc.conf in the Debug or Release folder.

```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```

## Execution

If there were no errors in the build, create rtc.conf in the Debug or Release folder and run MRCConvertorComp.exe.

Start NamingService before running MRCConvertorComp.exe.
### Starting the Name Server

Double-click <OpenRTM-aist installation folder>\bin\rtm-naming.bat to start the CORBA name server.


### Running MRCConvertorComp.exe

Move to the Debug or Release folder and run MRCConvertorComp.exe.
