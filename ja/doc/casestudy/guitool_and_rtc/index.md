---
layout: page
title: gui ツールキットとrtcの連携
---

<!-- Title: GUI ツールキットとRTCの連携 -->
#contents


## はじめに

Python のサンプルとして付属している GUIジョイスティック <br>
[TkJoyStickComp.py](http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/OpenRTM_aist/examples/TkJoyStick/TkJoyStickComp.py)

移動ロボットのシンプルなシミュレーターのサンプル <br>
[TkMobileRobotSimulator.py](http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/OpenRTM_aist/examples/MobileRobotCanvas/TkMobileRobotSimulator.py)

などが一例です。

## TkJoystickComp の例

TkJoystickComp のサンプルの main関数ですが、以下のようになっています。

```
 def main():
   tkJoyCanvas = tkjoystick.TkJoystick() # GUIオブジェクトを作成
   tkJoyCanvas.master.title("TkJoystick")
   mgr = OpenRTM_aist.Manager.init(sys.argv) # RTCマネージャを作成
   mgr.activateManager() #マネージャを活性化
 
   # コンポーネントの登録
   profile = OpenRTM_aist.Properties(defaults_str=tkjoystick_spec)
   mgr.registerFactory(profile,
                       TkJoyStick,
                       OpenRTM_aist.Delete)
   # コンポーネントの生成
   comp = mgr.createComponent("TkJoyStick")
 
   # このコンポーネントには set_pos というメンバ関数があり、
   # GUIジョイスティックの座標をコンポーネントに渡すために使用される。
   # TkJoystickのGUI の update イベントが呼ばれるときに、
   # こいつを呼ぶようにコールバックとしてセットする。
   tkJoyCanvas.set_on_update(comp.set_pos)
   mgr.runManager(True) # マネージャの runManager の引数に True を渡して non-block モードでマネージャを起動
   tkJoyCanvas.mainloop() # PythonのGUI のメインループに入る。
 
 if __name__ == "__main__":
   main()
```

## ポイント

### コンポーネントの中から GUI のメインループ関数を呼んだり、GUI オブジェクトを生成したりはしないほうが無難

GUI ツールキットの中には、mainスレッドから呼ばなければならないものや、　同一のスレッドから呼ばれることを前提としている関数などを持つものがある。RTC は onInitialize/onFinalize を呼ぶスレッドと、onExecute/onActivated/onDeactivated その他を呼ぶスレッドは異なります。また、onExecute 他の関数は複数のスレッドから同時に呼ばれる可能性すらあります。GUI スレッドと RTC とは別に扱ったほうがトラブルは少ないでしょう。

### GUI と RTC のデータのやり取りは、RTC にそのための関数を追加することで対応
  - 上記のような理由から、GUI とコンポーネントは切り離したほうがよいのですが、GUI と RTC とデータのやり取りをしなければならない時に困ります。通常 RTC にデータのやり取りをするためのインターフェースを別途継承させて、createComponent で取得したコンポーネントへのポインタを取得して GUI からデータを取得したり、データを与えたりします。

```
 class IMyInterface
 {
 public:
     virtual int getData() = 0;
     virtual void setData(double x, double y) = 0;
 };
 
 class MyComponent
  : public IMyInterface,
    public RTC::DataFlowComponentBase
 {
  : コンポーネントの定義
 public:
     virtual int getData()
     {
         coil::Guard guard(m_outdatalock);
         return m_outdata;
      }
    virtual void setData(double x, double y)
     {
         coil::Guard guard(m_indatalock);
         m_indata.x = x;
         m_indata.y = y;
     }
 };
```
このようにコンポーネントを実装しておいてから、
```
  RTObject_impl* rtobj = mgr.createComponent("MyComponent");
  IMyInterface* comp = dynamic_cast<IMyInterface*>(rtobj);
  if (comp == 0) { abort(); }
  mgr.runManager(true);
  gui.mainloop();
```
そして、GUIのコントロール内で
```
  std::cout << "out data: " << comp->getData() << std::endl; // データを取得
  comp->setData(1.0, 2.0); // データを入力
```
のようにRTCとデータのやり取りをします。

### RTC と GUI のコントロールやウィジェットを1対1対応にしておくとわかりやすい

ただし、GUI コントロールと RTC はそれぞれ生成方法が異なるので、別々に生成して、上述したように RTC に実装したデータ入出力関数を通じて GUI コントロールと結びつけたほうがよいでしょう。
 
移動ロボットのシンプルなシミュレーターのサンプルでは、移動ロボットオブジェクトとそれに対応する RTC を動的に増やしたり減らしたりしています。<br>
[TkMobileRobotSimulator.py](http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/OpenRTM_aist/examples/MobileRobotCanvas/TkMobileRobotSimulator.py)


