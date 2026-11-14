---
layout: page
title: generating the nxtrtc template
---

<!-- Title: NXTRTC の雛形を生成 -->
### Generating the NXTRTC Template
Create the template with RtcTemplate.
There are two ways to create the template: using the command-line version rtc-template, or using the Eclipse version RtcTemplate.

To execute rtc-template, create the following batch file.


```
 python "C:\Program Files\OpenRTM-aist\0.4\utils\rtc-template\rtc-template.py" -bpython^
  --module-name=NXTRTC --module-desc="NXT sample component"^
  --module-version=0.1 --module-vendor=AIST --module-category=example^
  --module-comp-type=DataFlowComponent --module-act-type=SPORADIC^
  --module-max-inst=10^
  --inport=vel:TimedFloatSeq^
  --outport=pos:TimedFloatSeq --outport=sens:TimedFloatSeq^
  --config="map:string:A,B"
```


In the Eclipse version RtcTemplate, the settings are as follows.
- Programing language selection: Python
- Module definition
  - Module name: NXTRTC
  - Module decription: NXT sample component
  - Module version: 0.1
  - Module vender: AIST
  - Module category: example
  - Component type: DataFlowComponent
  - Component's activity type: SPORADIC
  - Number of maximum instance: 10
- InPort definition
  - Ports: Name:vel Type:TimedFloatSeq
- OutPort definition
  - Ports: Name:pos, Type:TimedFloatSeq
  - Ports: Name:sens, Type:TimedFloatSeq
- ConfigurationSet definition
  - Cfg Sets: Name:map, Type:string, Default Value: A,B

Executing rtc-template (gen.bat)

```
 > gen.bat
  python "C:\Program Files\OpenRTM-aist\0.4\utils\rtc-template\rtc-template.py"
  -bpython --module-name=NXTRTC --module-desc="NXT sample component" 
  --module-version=0.1 --module-vendor=AIST --module-category=example 
  --module-comp-type=DataFlowComponent --module-act-type=SPORADIC 
  --module-max-inst=10 --inport=vel:TimedFloatSeq 
  --outport=pos:TimedFloatSeq --outport=sens:TimedFloatSeq
  --config="map:string:A,B"
 
   File "NXTRTC.py" was generated.
   File "README.NXTRTC" was generated.
   File "NXTRTC.yaml" was generated.
```

As shown above, template files such as NXTRTC.py have been created.

