---
layout: page
title: "imagesubtraction"
---

<!-- Title: ImageSubtraction -->

#contents

OpenRTM-aistのPython版、Java版には付属していませんのでご注意ください。また、Linux上では、[LinuxにおけるOpenCVサンプルコードのビルド手順]({{ site.baseurl }}/ja/doc/installation/opencvcamera/sample_components/opencv_sample_build)に従ってビルドしてインストールしてください。

### 概要
ImageSubtractionを起動することによって入力画像から背景画像を取り出し、前景画像部を判定し、それを取り出すマスク画像を、背景画像を出力します。
OpenCVCamera、CameraViewerといっしょに使用します。（なおWindows環境では現状このコンポーネントは再ビルドしないと現在正常に動作しないようなので、Ubuntu 18.04環境での使用を推奨いたします。)

### 起動画面

<div align="center"><a href="ImageSubtract_exe.png"><img src="ImageSubtract_exe.png" width="60%;"></a></div>
<div align="center"><strong>ImageSubtractionコンポーネンの実行例</strong></div>

### 使い方
ImageSubtractionは、入力画像から背景画像を取り出すためのコンポーネントです。ここではUSB Cameraから画像を取り込むためのOpenCVCameraと、処理した画像を表示するためのCameraViewerコンポーネントと使用します。

- 手順 (以下はUbuntu 18.04での手順です。)
  - ターミナルを起動します。
  - 上記の[LinuxにおけるOpenCVサンプルコードのビルド手順]({{ site.baseurl }}/doc/installation/sample_components/opencvcamera/opencv_sample_build/)に従いサンプルコードのインストールをします。
  - [OpenRTP]({{ site.baseurl }}/ja/doc/installation/install_1_2/start_openrtp_linux_1_2)に従いOpenRTPを起動しRTSystemEditorを起動し、Name Service ViewにRTCが表示されるようにします。新規SystemEditorを開きます。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_2_0)を参照してください。
  - 新規にターミナル画面を開きます。
  - 以下のコマンドを実行して、rtc.confを編集します。
```
 $ cd ImageProcessing/opencv/bin
 $ sudo vi rtc.conf
```
  - 最終行に以下の行を付け加えます。
```
 manager.components.naming_policy: ns_unique
```
  - 新規にターミナルを起動して
```
 $ cd ImageProcessing/opencv/bin
 $ ./CameraViewerComp
```
ターミナルを起動後の上記コマンドをさらに3回くり返し、4つのCameraViewerコンポーネントを起動します。
  - 新規にターミナルを起動します。
```
 $ cd ImageProcessing/opencv/bin
 $ ./OpenCVCameraComp
```
としてOpenCVCameraCompを起動します。
  - さらにもう一度ターミナルを起動して
```
 $ cd ImageProcessing/opencv/bin
 $ ./ImageSubtractionComp
```
と入力してImageSubtractionコンポーネントを起動します。
  - RTSystemEditorの画面のName Service viewのところの[>]をクリックして、起動したコンポーネントCameraView0, CameraViewer1, CameraViewer2, CameraViewe3, OpenCVCamera0, ImageSubtraction0のコンポーネントが表示されているのを確認します。
  - RTSystemEditorで上部の[Open New System Editor]ボタン<a href="icon_open_editor_ja.png"><img src="icon_open_editor_ja.png" width="4%;"></a> をクリックし、新規System Editorを開き、[System Dialgram]を新たに表示させます。
  - 上記の5つのコンポーネントをSystem Diagram上にドラッグ&ドロップします。
  - 下記の画面のように各コンポーネントのポートを接続します。

<div align="center"><a href="RTSystemEditor_ImageSubtraction.png"><img src="RTSystemEditor_ImageSubtraction.png" width="100%;"></a></div>
<div align="center"><strong>ImageSubtractionコンポーネンの実行例</strong></div>

  - どれかのコンポーネントを右クリックし、[Activate Systems]を選択します。
  - 画面のウィンドウを動かしながら4つのCameraViewerの画面を表示させます。
<div align="center"><a href="compexec.png"><img src="compexec.png" width="100%;"></a></div>
<div align="center"><strong>ImageSubtraction出力画像</strong></div>
  - マウスをcapture_imageのウィンドウから外に移動するとそのタイミングで背景画面が取り込まれ、それがback_imageに表示されます。他の画面もどうなるか確認してください。

なお、コンフィギュレーション・パラメータとして以下のようなものが設定可能です。
<table class="table-alt">
  <tr>
    <th>パラメータ名</th>
    <th>意味</th>
  </tr>
  <tr>
    <td>control_mode</td>
    <td>bとmが選択でき、bの時はkeyイベントに伴いバックグラウンドイメージの取り込みが行われ、mの時は画素ごとに閾値を決めるDYNAMIC_MODEと画面全体で一つの閾値を使うCONSTANT_MODEが切り替わります。</td>
  </tr>
  <tr>
    <td>image_height</td>
    <td>縦方向の画素数を指定しますが、このサンプルでは機能しません。</td>
  </tr>
  <tr>
    <td>image_width</td>
    <td>横方向の画素数を指定しますが、このサンプルでは機能しません。</td>
  </tr>
  <tr>
    <td>threshold_coefficient</td>
    <td>DYNAMIC_MODEで使う係数</td>
  </tr>
  <tr>
    <td>constant_threshold</td>
    <td>CONSTANT_MODEで使う閾値</td>
  </tr>
</table>

