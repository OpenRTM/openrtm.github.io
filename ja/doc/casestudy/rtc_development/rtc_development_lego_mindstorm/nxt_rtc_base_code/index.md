---
layout: page
title: nxtrtc の雛形を生成
---

<!-- Title: NXTRTC の雛形を生成 -->
### NXTRTC の雛形を生成
RtcTemplateで雛形を作成します。
雛型を作成する方法には、コマンドライン版の rtc-template を使う方法と、Eclipse版の RtcTemplate を使う方法があります。

rtc-template を実行するために、以下のようなバッチファイルを作成します。


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


Eclipse版 RtcTemplate では下記のようになります。
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

rtc-template(gen.bat)の実行

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

以上のように、NXTRTC.py などのひな型ファイルができました。



