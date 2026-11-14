---
layout: page
Title: 動作確認 (Windows編) 

---

<!-- Title: 動作確認 (Windows編) -->

#contents


## サンプルコンポーネントを実行する

インストールが正常に終了したら、付属のサンプルコンポーネントで動作を確認できます。
batファイルを用意していますので、それをダブルクリックすれば起動できます。

batファイルは、スタートメニューの [OpenRTM-aist 2.0.* x86_64] からスタートメニューフォルダーを開くとアクセスしやすいです。<br>
「C++_Examples」「C++_OpenCV-Examples」「Python_Examples」「Java_Examples」の各フォルダ下にbatファイルがあります。
詳細は、10分で始めようページの解説をご覧ください。 <br>

- [OpenRTM-aistを10分で始めよう！・サンプルコンポーネントを実行する]({{ site.baseurl }}/ja/doc/installation/lets_start#toc5) 

<br>
<div align="center"><a href="start-menu-folder.png"><img src="start-menu-folder.png" width="50%;"></a></div><br>
<div align="center"><strong>スタートメニューフォルダー</strong></div>
<br>


サンプルコンポーネントのインストール先は以下です。

```
 C:\Program Files\OpenRTM-aist\2.0.x\Components\C++\Examples
 C:\Program Files\OpenRTM-aist\2.0.x\Components\Python
 C:\Program Files\OpenRTM-aist\2.0.x\Components\Java
 C:\Program Files\OpenRTM-aist\2.0.x\Components\C++\OpenCV
```


## サンプルコンポーネント一覧

付属しているサンプルコンポーネントの簡単な説明と、使い方を解説しているページへのリンクを以下に示します。

### C++版、Python版、Java版に付属

<table class="table-alt">
  <tr>
    <td>batファイル名</td>
    <td>サンプルコンポーネントの簡単な説明</td>
    <td>使い方解説ページ</td>
  </tr>
  <tr>
    <td>ConsoleIn.bat <br>ConsoleOut.bat</td>
    <td>**ConsoleIn.bat** : コンソールから入力された数値をOutPortから出力する<span style="color:default;">ConsoleInコンポーネント</span>; を起動します。<br> **ConsoleOut.bat** : InPortに入力された数値をコンソールに表示する<span style="color:default;">ConsoleOutコンポーネント</span>;  を起動します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/simpleio">SimpleIO</a></td>
  </tr>
  <tr>
    <td>SeqIn.bat <br> SeqOut.bat</td>
    <td>**SeqIn.bat** : ランダムな数値(Short、Long、Float、Doubleとそのシーケンス型)を出力する<span style="color:default;">SeqInコンポーネント</span>;を起動します。<br> **SeqOut.bat** : InPortに入力される数値(Short、Long、Float、Doubleとそのシーケンス型)を表示する<span style="color:default;">SeqOut</span>;を起動します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/seqio">SeqIO</a></td>
  </tr>
  <tr>
    <td>MyServiceProvider.bat <br>MyServiceConsumer.bat</td>
    <td>**MyServiceProvider.bat** : MyService型のサービスを提供する<span style="color:default;">MyServiceProviderコンポーネント</span>; を起動します。<br> **MyServiceConsumer.bat** : MyService型のサービスを提供する<span style="color:default;">MyServiceConsumerコンポーネント</span>; を起動します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/simpleservice">SimpleService</a></td>
  </tr>
  <tr>
    <td>ConfigSample.bat</td>
    <td>Configuration機能の使用例のサンプル<span style="color:default;">ConfigSampleコンポーネント</span>; を起動します。RtcLinkからConfigurationを変更してConfigurationの挙動を理解するためのサンプルです。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/configsample">ConfigSample</a></td>
  </tr>
  <tr>
    <td>Composite.bat</td>
    <td>複合コンポーネント作成サンプル<span style="color:default;">PeriodicECSharedComponentコンポーネント</span>; を起動します。Sensor、Controller、Motorの3つサブ・コンポネントを複合しています。 ConsoleInなどのコンポーネント接続して使ってみると良いでしょう。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/composite">Composite</a></td>
  </tr>
</table>

### Python版のみに付属

<table class="table-alt">
  <tr>
    <td>batファイル名</td>
    <td>サンプルコンポーネントの簡単な説明</td>
    <td>使い方解説ページ</td>
  </tr>
  <tr>
    <td>TkJoystickComp.bat</td>
    <td>Tcl/Tkを用いたGUIコンポーネントのサンプル。簡易ジョイスティックコンポーネント。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/tkjoystick_mobilerobotsimulator#toc0">TkJoyStick</a></td>
  </tr>
  <tr>
    <td>TkMobileRobotSimulator.bat</td>
    <td>モバイルロボットの簡易シミュレーター。ロボットの速度をInPortで受け、移動後の位置をOutPortから出力する。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/tkjoystick_mobilerobotsimulator#toc4">TkMobileRobotSimulator</a></td>
  </tr>
  <tr>
    <td>TkMotorComp.bat</td>
    <td>Tcl/Tkを用いたGUIコンポーネントのサンプル。InPortで受け取った値の速度で回転する様子をGUIで表示する。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/tkmotorcomp_slidercomp#toc0">TkMotorComp</a></td>
  </tr>
  <tr>
    <td>SliderComp.bat</td>
    <td>Tcl/Tkを用いたGUIコンポーネントのサンプル。Sliderで指定した値をOutPortから出力する。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/tkmotorcomp_slidercomp#toc3">SliderComp</a></td>
  </tr>
  <tr>
    <td>TkMotorPosComp.bat</td>
    <td>Tcl/TKを用いたGUIコンポーネントのサンプル。InPortで受け取った値を回転角として動く様子をGUIで表示する。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/tkmotorposcomp_slidercomp">TkMotorPosComp</a></td>
  </tr>
  <tr>
    <td>TkLRFViewer.bat</td>
    <td>Tcl/Tkを用いたGUIコンポーネントのサンプル。レーザーレンジセンサーなどから出力されるデータを表示する。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/tklrfviewer">tkLRFViewer</a></td>
  </tr>
  <tr>
    <td>AutoControl.bat</td>
    <td>モバイルロボット用のコンポーネントで速度を出力する。測位センサーのデータをInPortで受け、ロボットの速度を計算してOutPortから出力する。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/autocontrol">Autocontrol</a></td>
  </tr>
</table>

### Python版、Java版に付属

<table class="table-alt">
  <tr>
    <td>batファイル名</td>
    <td>サンプルコンポーネントの簡単な説明</td>
    <td>使い方解説ページ</td>
  </tr>
  <tr>
    <td>ExtConsoleIn.bat <br> ExtConsoleOut.bat <br> ExtConnector.bat</td>
    <td>**ExtConsoleIn.bat** : 外部からのトリガで制御されるコンソール入力された数値をOutportから出力するコンポーネントを起動します。<br> **ExtConsoleOut.bat** : 外部からのトリガで制御されるInportに入力された数値をコンソールに出力するコンポーネントを起動します。<br> **ExtConnector.bat** : ExtTrigger/ConsoleInComp.class or .pyとExtTrigger/ConsoleOutComp.class or .pyへの外部トリガー送るプログラムを起動します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/exttrigger">ExtTrigger</a></td>
  </tr>
</table>

### Java版のみに付属

<table class="table-alt">
  <tr>
    <td>batファイル名</td>
    <td>サンプルコンポーネントの簡単な説明</td>
    <td>使い方解説ページ</td>
  </tr>
  <tr>
    <td>GUIIn.bat</td>
    <td>スライダーの位置をOutportから出力するGUIのサンプルを起動します。ConsoleOutComp.classと接続することもできます。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/guiin">GUIIn</a></td>
  </tr>
</table>

### OpenCV C++版

<table class="table-alt">
  <tr>
    <td>batファイル名</td>
    <td>サンプルコンポーネントの簡単な説明</td>
    <td>使い方解説ページ</td>
  </tr>
  <tr>
    <td>Affine.bat</td>
    <td>入力画像のアフィン変換をします。</td>
  </tr>
  <tr>
    <td>BackgroundSubtractionSimple.bat</td>
    <td>入力画像においてKey入力があった時点の画像から変化分を出力します。</td>
  </tr>
  <tr>
    <td>Binarization.bat</td>
    <td>入力画像を二値化した白黒画像に変換します。</td>
  </tr>
  <tr>
    <td>CameraViewer.bat</td>
    <td>InPort で受け取った画像を画面に表示します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/opencvcamera">CameraViewer</a></td>
  </tr>
  <tr>
    <td>Chromakey.bat</td>
    <td>画像から特定の色を除去し物体を抽出します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/chromakey">Chromakey</a></td>
  </tr>
  <tr>
    <td>DialationErosion.bat</td>
    <td>ダイアレーション/エロージョン処理を行います。</td>
  </tr>
  <tr>
    <td>Edge.bat</td>
    <td>X方向一次微分画像、Y方向一次微分画像、ラプラシアン画像(二次微分画像)を出力します</td>
  </tr>
  <tr>
    <td>Findcontour.bat</td>
    <td>輪郭抽出をして、輪郭を画像中に表示します。</td>
  </tr>
  <tr>
    <td>Flip</td>
    <td>画像の反転を行います。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/opencvcamera">Flip使用例</a></td>
  </tr>
  <tr>
    <td>Histgram.bat</td>
    <td>白黒化した画像の明度/コントラストの変更処理をしながら、ヒストグラムの変化を表示します。</td>
  </tr>
  <tr>
    <td>Hough.bat</td>
    <td>ハフ変換による直線抽出</td>
  </tr>
  <tr>
    <td>ImageCalibration.bat</td>
    <td>カメラキャリブレーションを行います。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/tkcalibgui">TkCalibGUIから自動起動</a></td>
  </tr>
  <tr>
    <td>ImageSubtraction.bat</td>
    <td>入力画像から背景画像を取り出し、前景画像部を判定し、それを取り出すマスク画像を、背景画像を出力します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/imagesubtraction">ImageSubtraction</a></td>
  </tr>
  <tr>
    <td>ObjectTracking.bat</td>
    <td>画面上から選択したオブジェクトを追跡して、その位置を赤い楕円形で囲んで示します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/objecttracking">ObjectTracking</a></td>
  </tr>
  <tr>
    <td>OpenCVCamera.bat</td>
    <td>USBカメラのキャプチャ画像を OutPort から出力します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/opencvcamera">OpenCVCamera</a></td>
  </tr>
  <tr>
    <td>Perspective.bat</td>
    <td>画像のパースペクティブ変換(斜め下から見たように変換します。</td>
  </tr>
  <tr>
    <td>RockPaperScissors.bat</td>
    <td>画像でグーチョキパーを判定します。</td>
  </tr>
  <tr>
    <td>Rotate.bat</td>
    <td>画像を回転と縮小拡大処理をします。</td>
  </tr>
  <tr>
    <td>Scale.bat</td>
    <td>画像の縮小拡大処理をします。</td>
  </tr>
  <tr>
    <td>Sepia.bat</td>
    <td>画像のセピア化を行います。</td>
  </tr>
  <tr>
    <td>SubtractCaptureImage.bat</td>
    <td>入力画像から変化のない部分を背景と判断して、前景(移動物)を取り出すマスク画像を出力します。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/substractcaptureimage">SubtractCaptureImage</a></td>
  </tr>
  <tr>
    <td>Template.bat</td>
    <td>テンプレートマッチング</td>
  </tr>
  <tr>
    <td>TkCalibGUI.bat</td>
    <td>カメラキャリブレーションを行う ImageCalibrationコンポーネント用のGUIです。</td>
    <td><a href="{{ site.baseurl }}/ja/doc/installation/sample_components/tkcalibgui">TkCalibGUI</a></td>
  </tr>
  <tr>
    <td>Translate.bat</td>
    <td>画像の2次元移動処理をします。</td>
  </tr>
</table>


