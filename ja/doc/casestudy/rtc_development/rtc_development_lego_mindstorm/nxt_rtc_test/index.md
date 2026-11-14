---
layout: page
title: nxt rtc 動作確認
---

<!-- Title: NXT RTC 動作確認 -->
#contents


# NXT RTC 動作確認
では、作成した NXTRTC を実際に動作させてみます。

## ネームサーバーの起動
ネームサーバーを起動します。
Windows用の OpenRTM-aist(C++版) をインストールしている場合は、スタートメニューの「OpenRTM-aist」>「C++」>「tools」>「Start Naming Service」から起動できます。

## rtc.conf の作成
rtc.conf を作成します。

```
 corba.nameservers: localhost
 naming.formats: %n.rtc
 manager.shutdown_auto: NO
```

corna.nameservers の項目は使用したいネームサーバーのアドレスに合わせて設定します。
ここでは、ローカルのネームサーバーを使用しますので、**localhost**とします。

起動したいコンポーネントが入っているそれぞれのディレクトリーにコピーしておきます。
今回作成した NXTRTC のほかに
- TkJoystickComp
- TkMotorPosComp
- TkSliderMonitorComp
を起動することにします。


## RTSystemEditor の起動
RTSystemEditor を起動します。
RTSystemEditor を起動後、ネームサーバー(ここでは localhost)に接続します。
また、SystemDiagram エディタを開くために、ツールバーの SystemDiagram アイコンをクリックします。


## コンポーネントの起動
以下のコンポーネントを起動します。
- NXTRTC
- TkJoystickComp
- TkMotorPosComp
- TkSliderMonitorComp
起動すると、RTSystemEditorのNameServcie ビュー上にコンポーネントが表示されます。

### TkJoystickComp
TkJoyStickComp は GUI上でジョイスティックを模擬するためのコンポーネントです。
図に示すような GUI があらわれ、中央の丸をドラッグすることでジョイスティックのように、X-Yの値を OutPort(上) から出力するコンポーネントです。
TkJoyStickComp にはもうひとつ OutPort(下) が付いていて、こちらは作動駆動型移動ロボットを操作するのに便利な左右の車輪の速度を出力するためのデータポートです。
NXTRTC の入力ポートに直接接続すれば、Tribot を制御することができます。

<div align="center"><a href="TkJoystick.png"><img src="TkJoystick.png" width="70%;"></a></div>

### TkMotorComp
TkMotorComp は GUI上で車輪に見立てた丸いアイコンが、InPort へ入力されたデータ(角度)に従って回転する、車輪の回転の様子をモニタリングするためのコンポーネントです。
NXTRTC の車輪の角度を出力する OutPort に接続することで、NXT の車輪の回転の様子を見ることができます。
NXT の車輪を手で回しても、その様子をモニタすることができます。
<div align="center"><a href="TkMotor.png"><img src="TkMotor.png" width="70%;"></a></div>

### TkSliderMonitorComp
TkSliderMonitorComp は、InPort へ入力されたデータの値をGUIのスライダで表示するためのコンポーネントです。
NXTRTC のセンサー出力ポートに接続することで、NXT のセンサーデータのモニタリングをすることができます。


## コンポーネントの接続
すべてのコンポーネントが起動したら、コンポーネントを接続します。
NameService ビューから SystemDiagram エディタへ各コンポーネントをドラッグアンドドロップします。
接続したいポートからポートへドラッグアンドドロップすることでポートを接続することができます。
下に、幾つかのコンポーネントを接続した例を示します。

<span style="color:red;">NXTに超音波センサーが取り付けられていない場合、NXTRTC の Activate 後にエラー状態(赤色)になります。</span>;

RtcLink.png
<!-- div align="center"><a href="RtcLink.png"><img src="RtcLink.png" width="70%;"></a></div-->

これらのコンポーネントを使って、NXTRTC が正しく動いているかどうかを確認しましょう。

<!-- **NXTを自由に動かすコンポーネントを作ってみる -->
<!-- これで、NXTをRTコンポーネント化することができました。 -->
<!-- 次は、NXT RTCを自分独自のロジックで動かすためのコンポーネントを作ってみましょう。 -->
<!-- 上記のように、Pythonで作っても、もちろんC++やJavaで作っても構いません。 -->
<!-- どういった言語で作ったコンポーネントとも、このNXT RTCは接続することができます。 -->

