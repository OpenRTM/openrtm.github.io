---
layout: page
title: 画像処理コンポーネントの作成(openrtm-aist-1.1、cmake、linux ubuntu 14.04) 
---

<!-- Title: 画像処理コンポーネントの作成(OpenRTM-aist-1.1、CMake、Linux Ubuntu 14.04) -->
#contents

## はじめに

このケーススタディでは、簡単な画像処理をコンポーネント化する方法を紹介します。既存のカメラコンポーネントと画像表示コンポーネントを利用し、カメラからの画像を左右 (または上下) に反転させる処理部分をコンポーネントとして作成してカメラの画像を反転させ表示するシステムを作成します。

画像を反転する処理は簡単に実装することができますが、ここではさらに簡単に実装するため OpenCV ライブラリを利用しより汎用性の高い RTコンポーネントを作成します。


### OpenCVとは

[OpenCV](http://opencv.jp/) とはかつてインテルが、現在は Willow Garage が開発・公開しているオープンソースのコンピュータービジョン向けライブラリです。

[Wikipedia](https://ja.wikipedia.org/wiki/OpenCV)より抜粋。

### 作成する RTコンポーネント

- Flip コンポーネント: OpenCV ライブラリが提供する様々な画像処理関数のうち、cvFlip() 関数を用いて画像の反転を行う RTコンポーネント。

## cvFlip 関数の RTコンポーネント化

入力された画像を左右または上下に反転し出力する RTコンポーネントを、OpenCV ライブラリの cvFlip 関数を利用して作成します。
作成および実行環境は Windows上の Visual C++ を想定しています。対象 OpenRTM-aist のバージョンは 1.1 です。


作成手順はおおよそ以下のようになります。

- 動作環境・開発環境についての確認
- OpenCV と cvFlip 関数についての確認
- コンポーネントの仕様を決める
- RTCBuilder を用いたソースコードのひな形の作成
- アクティビティ処理の実装
- コンポーネントの動作確認

### 動作環境の確認

Linux (ここでは Ubuntu 14.04 を仮定) 上に開発環境を構築します。

#### OpenRTM-aist のインストール

&color(red){Choreonoid を利用する場合、以下のように PPA から OpenRTM-aistを インストールしてください。
一括インストールスクリプトをすでに実行している場合、/etc/apt/sources.list の下の方に追記されている openrtm.org のリポジトリをコメントアウトした上で、 apt-get update してください。};

```
 $ sudo add-apt-repository ppa:hrg/daily
 $ sudo apt-get update
 $ sudo apt-get install openrtm-aist openrtm-aist-dev doxygen
```

#### OpenRTP のインストール

[こちらのURL]()（リンク切れです） から Linux版の OpenRTP (コンポーネント開発ツール、システム開発ツール統合環境) をダウンロード、インストールします。
OepnRTP の実行には Java も必要となりますので default-jre パッケージをインストールします。

```
 $ apt-get install default-jre
 $ wget http://openrtm.org/pub/openrtp/packages/1.1.0.rc5v20150317/eclipse381-openrtp110rc5v20150317-ja-linux-gtk-x86_64.tar.gz
 $ tar xvzf eclipse381-openrtp110rc5v20150317-ja-linux-gtk-x86_64.tar.gz
 $ cd eclipse
```
<!-- $ ./eclipse -->
```
 $ ./openrtp
```

<span style="color:red;">eclipse 起動後、RTSystemEditor でネームサーバーに接続できない場合があります。その場合、/etc/hosts の localhost の行に自ホスト名を追記してください。</span>;

```
 $ hostname
 ubuntu1404 ← ホスト名は ubuntu1404
 $ sudo vi /etc/hosts
```

```
 127.0.0.1       localhost
 を以下のように変更
 127.0.0.1       localhost ubuntu1404
```

#### OpenCV および OpenCV コンポーネントのインストール

OpenCV および OpenCV のコンポーネントをインストールします。

まず、Ubuntu が提供している OpenCV のパッケージを下記のようにインストールします。

```
 $ sudo apt-get install libopencv-dev libcv2.4 libcvaux2.4 libhighgui2.4
```

OpenCV RTC のパッケージは下記 URL にありますので、手動でダウンロードして、dpkg コマンドでインストールします。

```
 $ wget http://openrtm.org/pub/Linux/ubuntu/dists/trusty/main/binary-amd64/imageprocessing-1.1.0.deb
 $ sudo dpkg -i imageprocessing-1.1.0.deb
 $ ls /usr/share/openrtm-1.1/components/c++/opencv-rtcs/
 AffineComp                       FlipComp               RockPaperScissorsComp
 Affine.so                        Flip.so                RockPaperScissors.so
 BackGroundSubtractionSimpleComp  HistogramComp          RotateComp
 BackGroundSubtractionSimple.so   Histogram.so           Rotate.so
 BinarizationComp                 HoughComp              ScaleComp
 Binarization.so                  Hough.so               Scale.so
 CameraViewerComp                 ImageCalibrationComp   SepiaComp
 CameraViewer.so                  ImageCalibration.so    Sepia.so
 ChromakeyComp                    ImageSubstractionComp  SubStractCaptureImageComp
 Chromakey.so                     ImageSubstraction.so   SubStractCaptureImage.so
 DilationErosionComp              ObjectTrackingComp     TemplateComp
 DilationErosion.so               ObjectTracking.so      Template.so
 EdgeComp                         OpenCVCameraComp       TranslateComp
 Edge.so                          OpenCVCamera.so        Translate.so
 FindcontourComp                  PerspectiveComp
 Findcontour.so                   Perspective.so
```

### cvFlip 関数について

cvFlip 関数は、OpenCV で標準的に用いられている　IplImage型の画像データを垂直軸 (左右反転)、水平軸 (上下反転)、または両軸 (上下左右反転) に対して反転させます。関数プロトタイプと入出力の引数の意味は以下の通りです。

```
 void cvFlip(IplImage* src, IplImage* dst=NULL, int flipMode=0);
 #define cvMirror cvFlip
  
 src       入力配列
 dst       出力配列。もしdst=NULLであれば、srcが上書きされます。
 flipMode 配列の反転方法の指定内容:
 　flipMode = 0: X軸周りでの反転(上下反転)
 　flipMode > 0: Y軸周りでの反転(左右反転)
 　flipMode < 0: 両軸周りでの反転(上下左右反転)
```

### コンポーネントの仕様

これから作成するコンポーネントを Flip コンポーネントと呼ぶことにします。

このコンポーネントは画像データ型の入力ポート (InPort) と、反転処理した画像を出力するための出力ポート (OutPort) を持ちます。
それぞれのポートの名前を 入力ポート(InPort)名: **originalImage**, 出力ポート(OutPort)名: **flippedImage** とします。

OpenRTM-aist には OpenCV を使用したビジョン関連のコンポーネントがサンプルとして付属しています。
これらのコンポーネントのデータポートは画像の入出力に以下のような CameraImage 型を使用しています。

```
   struct CameraImage
     {
         /// Time stamp.
         Time tm;
         /// Image pixel width.
         unsigned short width;
         /// Image pixel height.
         unsigned short height;
         /// Bits per pixel.
         unsigned short bpp;
         /// Image format (e.g. bitmap, jpeg, etc.).
         string format;
         /// Scale factor for images, such as disparity maps,
         /// where the integer pixel value should be divided
         /// by this factor to get the real pixel value.
         double fDiv;
         /// Raw pixel data.
         sequence<octet> pixels;
     };
```

このFlipコンポーネントではこれらのサンプルコンポーネントとデータのやり取りができるよう同じく CameraImage型を InPort と OutPort に使用することにします。
CameraImage型は InterfaceDataTypes.idl で定義されており、C++であれば、InterfaceDataTypesSkel.h をインクルードすると使えるようになります。

また、画像を反転させる方向は、左右反転、上下反転、上下左右反転の3通りがあります。これを実行時に指定できるように、RTコンポーネントのコンフィギュレーション機能を使用して指定できるようにします。
パラメーター名は **flipMode** という名前にします。

flipMode は cvFlip 関数の仕様に合わせて、型は int 型とし 上下反転、左右反転、上下左右反転それぞれに 0、1、-1 を割り当てることにします。

flipModeの各値での画像処理のイメージを下図に示します。

<div align="center"><a href="cvFlip_and_FlipRTC.png"><img src="cvFlip_and_FlipRTC.png" width="60%;"></a></div>
<div align="center"><strong>Flip コンポーネントの flipMode 指定時の画像反転パターン</strong></div>

以上から Flip コンポーネントの仕様をまとめます。

<table class="table-alt">
  <tr>
    <th>コンポーネント名称</th>
    <th>Flip</th>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>originalImage</td>
  </tr>
  <tr>
    <td>型</td>
    <td>CameraImage</td>
  </tr>
  <tr>
    <td>意味</td>
    <td>入力画像</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>flippedImage</td>
  </tr>
  <tr>
    <td>型</td>
    <td>CameraImage</td>
  </tr>
  <tr>
    <td>意味</td>
    <td>反転された画像</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>flipMode</td>
  </tr>
  <tr>
    <td>型</td>
    <td>int</td>
  </tr>
  <tr>
    <td>意味</td>
    <td><strong>反転モード</strong> <br> 上下反転: 0 <br> 左右反転: 1 <br> 上下左右反転: -1</td>
  </tr>
</table>


### 動作環境・開発環境
ここで動作環境および開発環境を確認しておきます。

- OS: Windows XP SP3 (Vista, 7でも可能)
- コンパイラ: [Visual C++ 2010 Express Edition 日本語版](http://go.microsoft.com/fwlink/?LinkId=190491&clcid=0x411)

- [OpenRTM-aist-1.1.0-RC3 (C++版), Win32 VC2010]({{ site.baseurl }}/ja/download/openrtm-aist-content/110-rc3)

- RTSystemEditor 1.1
- RTCBuilder 1.1
  - [Eclipse3.4.2+RTSE+RTCB(1.1.0-RC2) Windows用全部入り]()（リンク切れです）

- [Doxygen](http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.11-setup.exe) ドキュメント生成に必要
- [CMake](https://cmake.org/files/v2.8/cmake-2.8.5-win32-x86.exe)

- [解凍ツール(Lhaplus)](http://www.forest.impress.co.jp/lib/arc/archive/archiver/lhaplus.html)

OpenRTM-aist-1.1 以降では、コンポーネントのビルドに CMake を使用します。また、RTC のひな形生成ツール RTCBuilder では、ドキュメントを入力してこれを Doxygen に処理させることで、コンポーネントのマニュアルも自動で生成することができるようになっています。
このため CMakeで Configure を行うときに Doxygen が要求されるため、予めインストールしておく必要があります。


### Flip コンポーネントの雛型の生成

Flip コンポーネントの雛型の生成は、RTCBuilder を用いて行います。

#### RTCBuilder の起動

Eclipse では、各種作業を行うフォルダーを「ワークスペース」(Work Space)とよび、原則としてすべての生成物はこのフォルダーの下に保存されます。
ワークスペースはアクセスできるフォルダーであれば、どこに作っても構いませんが、このチュートリアルでは以下のワークスペースを仮定します。

- `/workspace` (/home/<ユーザー名>/workspace を意味する。)


Eclipse を起動すると、ワークスペースの場所を尋ねられます。Eclipse を最初に起動したとき、または -clean オプション付きで起動した場合は、デフォルトで上記のディレクトリーが指定されますので、そのまま [OK] ボタンをクリックしてください。以下のような「ようこそ」画面が表示されます。
「ようこそ」画面はいまは必要ないので左上の「×」ボタンをクリックして閉じてください。


<div align="center"><a href="fig1-1EclipseInit.png"><img src="fig1-1EclipseInit.png" width="60%;"></a></div>
<div align="center"><strong>Eclipse の初期起動時の画面</strong></div>

右上の [Open Perspective] ボタンをクリックし、プルダウンの「Other…」を選択します。

<div align="center"><a href="fig2-2PerspectiveSwitch.png"><img src="fig2-2PerspectiveSwitch.png" width="60%;"></a></div>
<div align="center"><strong>パースペクティブの切り替え</strong></div>

「RTC Builder」を選択することで、RTCBuilder が起動します。メニューバーに「カナヅチとRT」の RTCBuilder のアイコンが表示されます。

<div align="center"><a href="fig2-3PerspectiveSelection.png"><img src="fig2-3PerspectiveSelection.png" width="30%;"></a></div>
<div align="center"><strong>パースペクティブの選択</strong></div>


#### 新規プロジェクトの作成

Flip コンポーネントを作成するために、RTCBuilder で新規プロジェクトを作成する必要があります。プロジェクトを作成する方法は2種類あります。

1. 画面上部のメニューから [ファイル] > [新規] > [プロジェクト] を選択 (Eclipse 共通)
  - ｢新規プロジェクト｣ 画面において，[その他] > [RTCビルダ] を選択し、[次へ] をクリックします。
1. メニューバーの [RTCBuilder] のアイコンをクリック


<div align="center"><a href="fig2-5CreateProject.png"><img src="fig2-5CreateProject.png" width="60%;"></a></div>
<div align="center"><strong>RTC Builder 用プロジェクトの作成　１ (「ファイル」メニューから)</strong></div>

<div align="center"><a href="fig2-6CreateProject2.png"><img src="fig2-6CreateProject2.png" width="30%;"></a></div>
<div align="center"><strong>RTC Builder 用プロジェクトの作成　２(「ファイル」メニューから)</strong></div>


どちらの方法でも、次ようなプロジェクト作成ウィザードが開始されます。
｢プロジェクト名｣欄に作成するプロジェクト名 (ここでは **Flip**) を入力して [完了] ボタンをクリックします。


<div align="center"><a href="RT-Component-BuilderProject.png"><img src="RT-Component-BuilderProject.png" width="30%;"></a></div>
<div align="center"><strong>RTC Builder 用プロジェクトの作成　３</strong></div>

指定した名称のプロジェクトが生成され、パッケージエクスプローラー内に追加されます。


<div align="center"><a href="PackageExplolrer.png"><img src="PackageExplolrer.png" width="30%;"></a></div>
<div align="center"><strong>RTC Builder 用プロジェクトの作成　４</strong></div>

生成したプロジェクト内には、デフォルト値が設定された RTC プロファイル XML(RTC.xml) が自動的に生成されます。

#### RTC プロファイルエディタの起動

RTC.xml が生成された時点で、このプロジェクトに関連付けられているワークスペースとして RTCBuilder のエディタが開くはずです。
もし開かない場合は、ツールバーの｢Open New RtcBuilder Editor｣ボタンをクリックするか、メニューバーの [ファイル] > [Open New Builder Editor] を選択します。


<div align="center"><a href="Open_RTCBuilder.png"><img src="Open_RTCBuilder.png" width="30%;"></a></div>
<div align="center"><strong>ツールバーから Open New RtcBuilder Editor</strong></div>

<div align="center"><a href="fig2-10FileMenuOpenNewBuilder.png"><img src="fig2-10FileMenuOpenNewBuilder.png" width="30%;"></a></div>
<div align="center"><strong>ファイルメニューから Open New Builder Editor</strong></div>


#### プロファイル情報入力とコードの生成

まず、いちばん左の「基本」タブを選択し、基本情報を入力します。先ほど決めた Flip コンポーネントの仕様(名前)の他に、概要やバージョン等を入力してください。
ラベルが赤字の項目は必須項目です。その他はデフォルトで構いません。

- モジュール名: Flip
- モジュール概要: Flip image component
- バージョン: 1.0.0
- ベンダ名: AIST
- モジュールカテゴリ: Category
- コンポーネント型: STATIC
- アクティビティ型: PERIODIC
- コンポーネント種類: DataFlowComponent
- 最大インスタンス数: 1
- 実行型: PeriodicExecutionContext
- 実行周期: 0.0 (<span style="color:RED;">下図では1.0となってますが 0.0 としてください.</span>;)

<br>

<div align="center"><a href="Basic.png"><img src="Basic.png" width="70%;"></a></div>
<div align="center"><strong>基本情報の入力</strong></div>
<br>

次に、「アクティビティ」タブを選択し、使用するアクションコールバックを指定します。

Flip コンポーネントでは、onActivated()、onDeactivated()、onExecute() コールバックを使用します。下図のように①の onAtivated をクリック後に ②のラジオボタンにて [ON] にチェックを入れます。
onDeactivated、onExecute についても同様の操作を行います。

<br>

<div align="center"><a href="Activity.png"><img src="Activity.png" width="70%;"></a></div>
<div align="center"><strong>アクティビティコールバックの選択</strong></div>
<br>

さらに、「データポート」タブを選択し、データポートの情報を入力します。
先ほど決めた仕様を元に以下のように入力します。なお、変数名や表示位置はオプションで、そのままで結構です。

<br>
- InPort Profile:
  - ポート名: originalImage
  - データ型: CameraImage
  - 変数名:  originalImage
  - 表示位置: left
<br>
- OutPort Profile:
  - ポート名: flippedImage
  - データ型: CameraImage
  - 変数名:  flippedImage
  - 表示位置: right

<br>

<div align="center"><a href="DataPort.png"><img src="DataPort.png" width="70%;"></a></div>
<div align="center"><strong>データポート情報の入力</strong></div>
<br>

次に、「コンフィギュレーション」タブを選択し、先ほど決めた仕様を元に、Configuration の情報を入力します。
制約条件および Widget とは、RTSystemEditor でコンポーネントのコンフィギュレーションパラメーターを表示する際に、スライダー、スピンボタン、ラジオボタンなど、GUI で値の変更を行うためのものです。

ここでは、flipMode が取りうる値は先ほど仕様を決めたときに、-1、0、1 の3つの値のみ取ることにしたので、ラジオボタンを使用することにします。

<br>
- flipMode
  - 名称: flipMode
  - データ型: int
  - デフォルト値: 1
  - 変数名: flipMode
  - 制約条件: (-1、0、1) <span style="color:RED;">※ (-1: 上下左右反転, 0: 上下反転, 1: 左右反転)</span>;
  - Widget: radio

<br>

<div align="center"><a href="Configuration.png"><img src="Configuration.png" width="70%;"></a></div>
<div align="center"><strong>コンフィグレーション情報の入力</strong></div>
<br>

次に、「言語・環境」タブを選択し、プログラミング言語を選択します。ここでは、C++(言語)を選択します。
なお、言語・環境はデフォルト等が設定されておらず、指定し忘れるとコード生成時にエラーになりますので、必ず言語の指定を行うようにしてください。

また、C++の場合デフォルトでは CMake を利用してビルドすることになっていますが、旧式の VC のプロジェクトやソリューションを直接 RTCBuilder が生成する方法を利用したい場合は [Use old build environment] をチェックしてください。

<div align="center"><a href="Language.png"><img src="Language.png" width="70%;"></a></div>
<div align="center"><strong>プログラミング言語の選択</strong></div>
<br>

最後に、「基本」タブにある [コード生成] ボタンをクリックし、コンポーネントの雛型を生成します。

<br>

<div align="center"><a href="Generate.png"><img src="Generate.png" width="70%;"></a></div>
<div align="center"><strong>雛型の生成(Generate)</strong></div>
<br>

&color(Red){※ 生成されるコード群は、Eclipse 起動時に指定したワークスペースフォルダーの中に生成されます。
現在のワークスペースは、[ファイル] > [ワークスペースの切り替え] で確認することができます。};


#### 仮ビルド

さて、ここまでで Flip コンポーネントのソースコードが生成されました。処理の中身は実装されていないので、InPort に画像を入力しても何も出力されませんが、生成直後のソースコードだけでもコンパイルおよび実行はできます。

※サービスポートとプロバイダを持つコンポーネントの場合、実装を行わないとビルドが通らないものもあります。

では、まず CMake を利用してビルド環境の Configure を行います。Linux であれば、Flip コンポーネントのソースが生成されたディレクトリーで

```
 $ cd workspace/Flip
 $ mkdir build
 $ cd build
 $ cmake ..
 $ make
```

とすれば、Configure およびビルドが完了するはずです。ビルド終了後、からの FlipComp を起動してみましょう。

```
 $ cd src
 $ ./FlipComp
```

起動後、RTSystemEditor などでアクセスしてみてください。Flip というコンポーネントが表示されているはずです。
カメラコンポーネント (OpenCVCameraComp) や表示コンポーネント (CameraViewerComp) などとも接続できますが、中で何も処理を行っていないでの、表示コンポーネントには何も表示されません。

次からは、コンポーネントのソースコードを作成し、中身を実装していきます。

### ヘッダ、ソースの編集

ヘッダ (include/Flip/Flip.h) およびソースコード (src/Flip.cpp) をそれぞれ編集します。
Eclipse 画面左のパッケージエクスプローラーでそれぞれのファイルをダブルクリックすると、通常は Visual C++ の編集画面が開きますので、そこで編集します。
Eclipse の中央のエディタにドラッグアンドドロップしても編集できます。

#### アクティビティ処理の実装

Flip コンポーネントでは、InPort から受け取った画像を画像保存用バッファに保存し、その保存した画像を OpenCV の cvFlip()関数にて変換します。
その後、変換された画像を OutPort から送信します。

<br>
onActivated()、onExecute()、onDeactivated() での処理内容を下図に示します。
<br>

<div align="center"><a href="FlipRTC_State.png"><img src="FlipRTC_State.png" width="50%;"></a></div>
<div align="center"><strong>アクティビティ処理の概要</strong></div>
<br>

onExecute() での処理を下図に示します。

<br>

<div align="center"><a href="FlipRTC.png"><img src="FlipRTC.png" width="50%;"></a></div>
<div align="center"><strong>onExucete() での処理内容</strong></div>
<br>


#### ヘッダファイル (Flip.h) の編集

OpenCV のライブラリを使用するため、OpenCV のインクルードファイルをインクルードします。

```
 //OpenCV用インクルードファイルのインクルード
 #include<cv.h>
 #include<cxcore.h>
 #include<highgui.h>
```

この cvFlip コンポーネントでは、画像領域の確保、Flip 処理、確保した画像領域の解放のそれぞれの処理を行います。
これらの処理は、それぞれ onActivated()、onDeactivated()、onExecute() のコールバック関数にて行います。

```
   /***
    *
    * The activated action (Active state entry action)
    * former rtc_active_entry()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
   virtual RTC::ReturnCode_t onActivated(RTC::UniqueId ec_id);
 
   /***
    *
    * The deactivated action (Active state exit action)
    * former rtc_active_exit()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
   virtual RTC::ReturnCode_t onDeactivated(RTC::UniqueId ec_id);
 
   /***
    *
    * The execution action that is invoked periodically
    * former rtc_active_do()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
   virtual RTC::ReturnCode_t onExecute(RTC::UniqueId ec_id);
```

反転した画像の保存用にメンバー変数を追加します。

```
   IplImage* m_imageBuff;
   IplImage* m_flipImageBuff;
```

#### ソースファイル (Flip.cpp) の編集

下記のように、onActivated()、onDeactivated()、onExecute()を実装します。

```
 RTC::ReturnCode_t Flip::onActivated(RTC::UniqueId ec_id)
 {
   // イメージ用メモリーの初期化
   m_imageBuff = NULL;
   m_flipImageBuff = NULL;
 
   // OutPortの画面サイズの初期化
   m_flippedImage.width = 0;
   m_flippedImage.height = 0;
  
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t Flip::onDeactivated(RTC::UniqueId ec_id)
 {
   if(m_imageBuff != NULL)
   {
     // イメージ用メモリーの解放
     cvReleaseImage(&m_imageBuff);
     cvReleaseImage(&m_flipImageBuff);
   }
 
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t Flip::onExecute(RTC::UniqueId ec_id)
 {
   // 新しいデータのチェック
   if (m_originalImageIn.isNew()) {
     // InPortデータの読み込み
     m_originalImageIn.read();
 
     // InPort と OutPort の画面サイズ処理およびイメージ用メモリーの確保
     if( m_originalImage.width != m_flippedImage.width || m_originalImage.height != m_flippedImage.height)
       {
 	m_flippedImage.width = m_originalImage.width;
 	m_flippedImage.height = m_originalImage.height;
 
 	// InPort のイメージサイズが変更された場合
 	if(m_imageBuff != NULL)
 	  {
 	    cvReleaseImage(&m_imageBuff);
 	    cvReleaseImage(&m_flipImageBuff);
 	  }
 
 	// イメージ用メモリーの確保
 	m_imageBuff = cvCreateImage(cvSize(m_originalImage.width, m_originalImage.height), IPL_DEPTH_8U, 3);
 	m_flipImageBuff = cvCreateImage(cvSize(m_originalImage.width, m_originalImage.height), IPL_DEPTH_8U, 3);
       }
 
     // InPort の画像データを IplImage の imageData にコピー
     memcpy(m_imageBuff->imageData,(void *)&(m_originalImage.pixels[0]),m_originalImage.pixels.length());
 
     // InPort からの画像データを反転する。 m_flipMode 0: X軸周り, 1: Y軸周り, -1: 両方の軸周り
     cvFlip(m_imageBuff, m_flipImageBuff, m_flipMode);
 
     // 画像データのサイズ取得
     int len = m_flipImageBuff->nChannels * m_flipImageBuff->width * m_flipImageBuff->height;
     m_flippedImage.pixels.length(len);
 
     // 反転した画像データを OutPort にコピー
     memcpy((void *)&(m_flippedImage.pixels[0]),m_flipImageBuff->imageData,len);
 
     // 反転した画像データを OutPort から出力する。
     m_flippedImageOut.write();
   }
 
   return RTC::RTC_OK;
 }
```

### CMake によるビルドに必要なファイルの生成


#### CMakeList.txt の編集

Eclipse 画面左のパッケージエクスプローラーで src/CMakeLists.txt をダブルクリックもしくはエディタへドラッグアンドドロップして編集します。

<div align="center"><a href="EditCmakeLists.png"><img src="EditCmakeLists.png" width="70%;"></a></div>
<div align="center"><strong>CMakeLists.txtの編集</strong></div>


このコンポーネントでは OpenCV を利用していますので、OpenCV のヘッダのインクルードパス、ライブラリやライブラリサーチパスを与えてやる必要があります。
幸い OpenCV は CMake に対応しており、以下の2行を追加・変更するだけで OpenCV のライブラリがリンクされ使えるようになります。

- src/CMakeLists.txt を修正する
  - Eclipse のパッケージエクスプローラーで src/CMakeLists.txt をダブルクリック
1. find_package (OpenCV REQUIRED) を追加
1. 最初の target_link_libraries に ${OpenCV_LIBS} を追加
  - target_link_libraries は2ヶ所あり、上が DLL、下が実行ファイルのライブラリ指定です

```
 set(comp_srcs Flip.cpp )
 set(standalone_srcs FlipComp.cpp)
 
 find_package(OpenCV REQUIRED) ← この行を追加
   ：中略
 add_dependencies(${PROJECT_NAME} ALL_IDL_TGT)
 target_link_libraries(${PROJECT_NAME} ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) ←　OepnCV_LIBSを追加
   ：中略
 add_executable(${PROJECT_NAME}Comp ${standalone_srcs}
   ${comp_srcs} ${comp_headers} ${ALL_IDL_SRCS})
 target_link_libraries(${PROJECT_NAME}Comp ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) ←　OepnCV_LIBSを追加
```

### ビルド

#### ビルドの実行

CMakeList.txt を編集したので、再度 CMake で Configure および Generate を行います。

```
 $ cd workspace/Flip (eclipse ワークスペース下の Flip ディレクトリーへ移動)
 $ rm -rf build (念のため仮ビルドで作成したディレクトリーは削除)
 $ mkdir build (再度 build ディレクトリーを作成)
 $ cd build
 $ cmake ..
 $ make
 
```
CMake の Generate が正常に終了した事を確認し、makeします。Configure で問題がある場合、先ほど編集した Flip/src/CMakeList.txt の編集にミスがある可能性があります。
make でエラーが出た場合は、ソースコードやヘッダの編集に間違いがある可能性があります。
エラーメッセージをよく見て、修正してください。

### Flip コンポーネントの動作確認

ここでは、OpenRTM-aist-1.1 以降で同梱されるようになったカメラコンポーネント (OpenCVCameraComp、または DirectShowCamComp)とビューアコンポーネント (CameraViewerComp)を接続し動作確認を行います。

#### NameService の起動

コンポーネントの参照を登録するためのネームサービスを起動します。

<br>
```
 $ rtm-naming
```

#### rtc.conf の作成

RTコンポーネントでは、ネームサーバーのアドレスやネームサーバーへの登録フォーマットなどの情報を rtc.conf というファイルで指定する必要があります。

下記の内容を rtc.conf というファイル名で保存し、workspace/Flip/build/src/ ディレクトリーに置いてください。

```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```

#### Flip コンポーネントの起動

Flip コンポーネントを起動します。

先程 rtc.conf ファイルを置いたフォルダーにある、FlipComp.exe ファイルを実行してください。

```
 $ cd workspace/Flip/build/src (もし現在 build/src 以外にいる場合）
 $ ./FlipComp
 
```
#### カメラコンポーネントとビューアコンポーネントの起動

USBカメラのキャプチャー画像を OutPort から出力する OpenCVCameraComp、InPort で受け取った画像を画面に表示する CameraViewerComp を起動します。

```
 $ /usr/share/openrtm-1.1/components/c++/opencv-rtcs/OpenCVCameraComp
 $ /usr/share/openrtm-1.1/components/c++/opencv-rtcs/CameraViewerComp
 
```
### コンポーネントの接続

下図のように、RTSystemEditor にて
OpenCVCameraComp (またはDirectShowcomp) と Flip、CameraviewerComp コンポーネントを接続します。

<div align="center"><a href="RTSE_Connect.png"><img src="RTSE_Connect.png" width="70%;"></a></div>
<div align="center"><strong>コンポーネントの接続</strong></div>

<span style="color:red;">Eclipse起動後、RTSystemEditor でネームサーバーに接続できない場合があります。その場合、/etc/hosts の localhost の行に自ホスト名を追記してください。</span>;

```
 $ hostname
 ubuntu1404 ← ホスト名は ubuntu1404
 $ sudo vi /etc/hosts
```

```
 127.0.0.1       localhost
 を以下のように変更
 127.0.0.1       localhost ubuntu1404
```

#### コンポーネントの Activate

RTSystemEditor の上部にあります「ALL」というアイコンをクリックし、全てのコンポーネントをアクティブ化します。正常にアクティベートされた場合、下図のように黄緑色でコンポーネントが表示されます。

<br>

<div align="center"><a href="RTSE_Activate.png"><img src="RTSE_Activate.png" width="70%;"></a></div>
<div align="center"><strong>コンポーネントのアクティブ化</strong></div>
<br>

#### 動作確認

下図のようにコンフィギュレーションビューにてコンフィギュレーションを変更することができます。

Flip コンポーネントのコンフィギュレーションパラメーター「flipMode」を「0」や「-1」などに変更し、画像の反転が行われるかを確認してください。

<br>

<div align="center"><a href="RTSE_Configuration.png"><img src="RTSE_Configuration.png" width="70%;"></a></div>
<div align="center"><strong>コンフィギュレーションパラメーターの変更</strong></div>
<br>

## Flip コンポーネントの全ソース

### Flip コンポーネントソースファイル (Flip.cpp)

```
 // -*- C++ -*-
 /*!
  * @file  Flip.cpp
  * @brief Flip image component
  * @date $Date$
  *
  * $Id$
  */
 
 #include "Flip.h"
 
 // Module specification
 static const char* flip_spec[] =
   {
     "implementation_id", "Flip",
     "type_name",         "Flip",
     "description",       "Flip image component",
     "version",           "1.0.0",
     "vendor",            "AIST",
     "category",          "Category",
     "activity_type",     "PERIODIC",
     "kind",              "DataFlowComponent",
     "max_instance",      "1",
     "language",          "C++",
     "lang_type",         "compile",
     // Configuration variables
     "conf.default.flipMode", "1",
     // Widget
     "conf.__widget__.flipMode", "radio",
     // Constraints
     "conf.__constraints__.flip_mode", "(-1,0,1)",
     ""
   };
 
 /*!
  * @brief constructor
  * @param manager Maneger Object
  */
 Flip::Flip(RTC::Manager* manager)
   : RTC::DataFlowComponentBase(manager),
     m_originalImageIn("originalImage", m_originalImage),
     m_flippedImageOut("flippedImage", m_flippedImage)
 {
 }
 
 /*!
  * @brief destructor
  */
 Flip::~Flip()
 {
 }
 
 
 RTC::ReturnCode_t Flip::onInitialize()
 {
   // Registration: InPort/OutPort/Service
   // Set InPort buffers
   addInPort("originalImage", m_originalImageIn);
   
   // Set OutPort buffer
   addOutPort("flippedImage", m_flippedImageOut);
   
   // Bind variables and configuration variable
   bindParameter("flipMode", m_flipMode, "1");
 
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t Flip::onActivated(RTC::UniqueId ec_id)
 {
   // イメージ用メモリーの初期化
   m_imageBuff = NULL;
   m_flipImageBuff = NULL;
 
   // OutPort の画面サイズの初期化
   m_flippedImage.width = 0;
   m_flippedImage.height = 0;
  
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t Flip::onDeactivated(RTC::UniqueId ec_id)
 {
   if(m_imageBuff != NULL)
   {
     // イメージ用メモリーの解放
     cvReleaseImage(&m_imageBuff);
     cvReleaseImage(&m_flipImageBuff);
   }
 
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t Flip::onExecute(RTC::UniqueId ec_id)
 {
   // 新しいデータのチェック
   if (m_originalImageIn.isNew()) {
     // InPort データの読み込み
     m_originalImageIn.read();
 
     // InPort と OutPort の画面サイズ処理およびイメージ用メモリーの確保
     if( m_originalImage.width != m_flippedImage.width || m_originalImage.height != m_flippedImage.height)
       {
 	m_flippedImage.width = m_originalImage.width;
 	m_flippedImage.height = m_originalImage.height;
 
 	// InPort のイメージサイズが変更された場合
 	if(m_imageBuff != NULL)
 	  {
 	    cvReleaseImage(&m_imageBuff);
 	    cvReleaseImage(&m_flipImageBuff);
 	  }
 
 	// イメージ用メモリーの確保
 	m_imageBuff = cvCreateImage(cvSize(m_originalImage.width, m_originalImage.height), IPL_DEPTH_8U, 3);
 	m_flipImageBuff = cvCreateImage(cvSize(m_originalImage.width, m_originalImage.height), IPL_DEPTH_8U, 3);
       }
 
     // InPort の画像データをIplImage の imageData にコピー
     memcpy(m_imageBuff->imageData,(void *)&(m_originalImage.pixels[0]),m_originalImage.pixels.length());
 
     // InPort からの画像データを反転する。 m_flipMode 0: X軸周り, 1: Y軸周り, -1: 両方の軸周り
     cvFlip(m_imageBuff, m_flipImageBuff, m_flipMode);
 
     // 画像データのサイズ取得
     int len = m_flipImageBuff->nChannels * m_flipImageBuff->width * m_flipImageBuff->height;
     m_flippedImage.pixels.length(len);
 
     // 反転した画像データを OutPort にコピー
     memcpy((void *)&(m_flippedImage.pixels[0]),m_flipImageBuff->imageData,len);
 
     // 反転した画像データを OutPort から出力する。
     m_flippedImageOut.write();
   }
 
   return RTC::RTC_OK;
 }
 
 
 extern "C"
 {
  
   void FlipInit(RTC::Manager* manager)
   {
     coil::Properties profile(flip_spec);
     manager->registerFactory(profile,
                              RTC::Create<Flip>,
                              RTC::Delete<Flip>);
   }
   
 };
```

### Flip コンポーネントのヘッダファイル (Flip.h)

```
 // -*- C++ -*-
 /*!
  * @file  Flip.h
  * @brief Flip image component
  * @date  $Date$
  *
  * $Id$
  */
 
 #ifndef FLIP_H
 #define FLIP_H
 
 #include <rtm/Manager.h>
 #include <rtm/DataFlowComponentBase.h>
 #include <rtm/CorbaPort.h>
 #include <rtm/DataInPort.h>
 #include <rtm/DataOutPort.h>
 #include <rtm/idl/BasicDataTypeSkel.h>
 #include <rtm/idl/ExtendedDataTypesSkel.h>
 #include <rtm/idl/InterfaceDataTypesSkel.h>
 
 //OpenCV 用インクルードファイルのインクルード
 #include<cv.h>
 #include<cxcore.h>
 #include<highgui.h>
 
 using namespace RTC;
 
 /*!
  * @class Flip
  * @brief Flip image component
  *
  */
 class Flip
   : public RTC::DataFlowComponentBase
 {
  public:
   /*!
    * @brief constructor
    * @param manager Maneger Object
    */
   Flip(RTC::Manager* manager);
 
   /*!
    * @brief destructor
    */
   ~Flip();
 
   /***
    *
    * The initialize action (on CREATED->ALIVE transition)
    * formaer rtc_init_entry() 
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
    virtual RTC::ReturnCode_t onInitialize();
 
   /***
    *
    * The activated action (Active state entry action)
    * former rtc_active_entry()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
    virtual RTC::ReturnCode_t onActivated(RTC::UniqueId ec_id);
 
   /***
    *
    * The deactivated action (Active state exit action)
    * former rtc_active_exit()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
    virtual RTC::ReturnCode_t onDeactivated(RTC::UniqueId ec_id);
 
   /***
    *
    * The execution action that is invoked periodically
    * former rtc_active_do()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
    virtual RTC::ReturnCode_t onExecute(RTC::UniqueId ec_id);
 
  protected:
   // Configuration variable declaration
   /*!
    * 
    * - Name:  flipMode
    * - DefaultValue: 1
    */
   int m_flipMode;
 
   // DataInPort declaration
   CameraImage m_originalImage;
 
   /*!
    */
   InPort<CameraImage> m_originalImageIn;
   
   // DataOutPort declaration
   CameraImage m_flippedImage;
 
   /*!
    */
   OutPort<CameraImage> m_flippedImageOut;
 
  private:
   // 処理画像用バッファ
   IplImage* m_imageBuff;
   IplImage* m_flipImageBuff;
 };
 
 
 extern "C"
 {
   DLL_EXPORT void FlipInit(RTC::Manager* manager);
 };
 
 #endif // FLIP_H
```

### Flip コンポーネントの全ソースコード

Flip コンポーネントの全ソースコードを以下に添付します。

[Flip.zip](Flip.zip)

