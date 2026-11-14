---
layout: page
title: "subtractcaptureimage"
---

<!-- Title: SubtractCaptureImage -->

#contents

OpenRTM-aistのPython版、Java版には付属していませんのでご注意ください。また、Linux上では、[LinuxにおけるOpenCVサンプルコードのビルド手順]({{ site.baseurl }}/ja/doc/installation/sample_components/opencvcamera/opencv_sample_build)に従ってビルドしてインストールしてください。

### 概要
SubtractCaptureImageは入力画像から、変化のない部分を背景と判断して、前景(移動物)を取り出すマスク画像を出力するコンポーネントで、動的な背景差分法でリアルタイムな背景更新をするコンポーネントのサンプルです。OpenCVCamera、CameraViewerコンポーネントと共に使用します。

### 使い方
SubtractCaptureImageは入力画像で動きがないものを背景とみなして背景とするのと、画面上に新たに追加された物も動きがなくしばらくおいておかれると、それの部分も背景の一部と判定し、背景画像にとりこみます。出力には、入力画像、前景(移動物を示す)のマスク画像、移動物でも背景でもないものを示すマスク画像、背景画像、静止物体の背景化を表示する画像が出力されます。
このコンポーネントを使ってみるためにはCameraViewerを複数起動して複数の出力画像を同時に見るか、CameraViewerとの接続を変えながら、それぞれの出力画像を見ていってください。また入力画像としてOpenCVCameraコンポーネントを使用してみると良いでしょう。

- 手順 (Windows環境)
- [OpenRTPの起動手順(1.2系、Windows)]({{ site.baseurl }}/ja/doc/installation/install_1_2/start_openrtp_proc_windows_1_2)に従いOpenRTPを起動しRTSystemEditorを起動し、Name Service ViewにRTCが表示されるようにします。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_2_0)を参照してください。
- 管理者権限でコマンドプロンプトを開きCameraViewerコンポーネントを複数実行できるようにします。
- rtc.confを編集します。例えば、以下のようなコマンドを入力し編集を行います。

```
 cd "\Program Files\OpenRTM-aist\1.2.1\Components\C++\OpenCV\vc14"
 notepad rtc.conf
```
とし、以下の行を付け加えます。
```
 manager.components.naming_policy: ns_unique
```

- コマンドプロンプトを閉じます。
- エクスプローラーで\Program Files\OpenRTM-aist\1.2.1\Components\C++\OpenCVとたどります。
- CameraViewer.batをダブルクリックします。
- CameraViewer.batさらにダブルクリックし、全部で5つのCameraVieweerコンポーネントを起動します。
- OpenCVCamera.batをダブルクリックします。
- SubtractCaptureImage.batをダブルクリックします。
- RTSystemEditorの画面のName Service viewのところの[>]をクリックして、起動したコンポーネントCameraViewer0、CameraViewer1、CameraViewer2、CameraViewer3、CameraViewer4、SubtractCaputreImage0、OpenCVCamera0のコンポーネントが表示されているのを確認します。
  - RTSystemEditorで上部の[Open New System Editor]ボタン<a href="icon_open_editor_ja.png"><img src="icon_open_editor_ja.png" width="4%;"></a>; をクリックし、新規System Editorを開き、[System Dialgram]を新たに表示させます。
- 上記の7つのコンポーネントをSystem Diagram上にドラッグ&ドロップします。
- 下記の画面のように各コンポーネントのポートを接続します。

<div align="center"><a href="RTSE_SubtractCaptureImage.png"><img src="RTSE_SubtractCaptureImage.png" width="75%;"></a></div>
<div align="center"><strong>SubtractCaptureImageコンポーネントの接続</strong></div>

- どれかのコンポーネントを右クリックし、[Activate Systems]を選択します。
- 画面のウィンドウを動かしながらCameraViewerの画面を表示させます。
- まずはbackGraoundImg が接続されているCameraViewer3の画面と入力画面と同じ画面であるoutput_imageに接続されているCameraViewer0の画面を見てみます。どちらにも何らかの画像が表示されているのを確認します。
- ここでforeMaskImgが接続されているCameraView1の画面を見てみると、最初は白い部分があったのが、徐々に真っ黒な画面になっていくというのが分かります。この画面は黒い部分が背景と見なされている部分、白い部分が前景と見なされている部分ということを示しています。前景と見なされるのは変化している部分、つまり動いている物です。そこで、真っ黒になった時に、なにか動くものを撮影してみると、その動いた物体の部分が白く表示されるのが分かります。またStillImgであるCameraView3の出力には動いているものが静止しはじめると、徐々にその物体がはっきりするようになってくるというのが分かります。下記のその例の画像を示します。
<div align="center"><a href="SubtractCaptureImageOut1.png"><img src="SubtractCaptureImageOut1.png" width="75%;"></a></div>
<div align="center">''それぞれの出力ポートの画像 － 前景検出’’</div>

- 上記の画像は、撮影してしばらくおいて、foreMaskImgが真っ黒になった後に、指を横からゆっくりと動かして画面にいれた例です。foreMaskImgを見るとと動いている指の部分が前景(移動物)として見なされているのと、動きがゆっくりなのでstillImgのところで指が一部静止物と見なされてきている様子見られます。
- 次の画像は、ラズパイマウスというRaspberry Piでコントロールする小型ロボットがある画面を、しばらく撮影し、ある時点で、そのラズパイマウスの上に猫の置物をおいた時の画像で、猫の置物が静止物と見なされ、徐々に背景と判定されていく過程の画像です。
<div align="center"><a href="SubtractCaptureImageOut2.png"><img src="SubtractCaptureImageOut2.png" width="75%;"></a></div>
<div align="center"><strong>それぞれの出力ポートの画像 － 静止物検出、背景更新</strong></div>
- StillImgの画像は、猫の置物をほぼ静止物と見なしているのを示しています。このアルゴリズムでは、静止物を背景と見なすのには、さらに時間を必要とし、その部分を徐々に背景と見なします。backGroundImgの画像では猫の置物の一部が表示され、その部分が背景と見なされているのがわかります。この後backGroundImgはStillImgとほぼ同じ画像になるように変化していきます。一方foreMaskImgは、白いところがあり、この部分は、まだ前景(移動物の画像)だと見なされています。
- stillMaskImgについては静止画として表現するのは難しいので、ここではサンプル画像は白いままのものしか提示しません。この画像に関しては、実際に画像を表示させて確認してください。なお、この出力は定常的には全体が白い画像が出力され、背景とも前景(移動物)とも見なされない部分、つまり背景と判定される直前に静止物が取り除かれたようなケースだけその部分を黒くした画像が出力されます。




