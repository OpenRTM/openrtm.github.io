---
layout: page
title: 画像処理コンポーネントの作成 (ubuntu 16.04、openrtm-aist-1.1.2-release、openrtp-1.1.2、cmake-3.5.1、code::blocks-16.01)
---

<!-- Title: 画像処理コンポーネントの作成 (Ubuntu 16.04、OpenRTM-aist-1.1.2-RELEASE、OpenRTP-1.1.2、CMake-3.5.1、Code::Blocks-16.01) -->
#contents

## はじめに

このケーススタディでは、簡単な画像処理をコンポーネント化する方法を紹介します。
既存のカメラコンポーネントと画像表示コンポーネントを利用し、カメラからの画像を左右(または上下)に反転させる処理部分をコンポーネントとして作成してカメラの画像を反転させ表示するシステムを作成します。

画像を反転する処理は簡単に実装することができますが、ここではより簡単に実装するために OpenCV ライブラリを利用し、より汎用性の高い RTコンポーネントを作成します。

### OpenCVとは

[OpenCV](http://opencv.jp/) (オープンシーブイ) とはかつてインテルが、現在は Itseez が開発・公開しているオープンソースのコンピュータービジョン向けライブラリです。

[Wikipedia](https://ja.wikipedia.org/wiki/OpenCV)より抜粋。

### 作成するRTコンポーネント

- Flip コンポーネント: OpenCV ライブラリが提供する様々な画像処理関数のうち、cv::flip() 関数を用いて画像の反転を行う RTコンポーネント。


## cv::flip関数のRTコンポーネント化

入力された画像を左右または上下に反転し出力する RTコンポーネントを、OpenCV ライブラリの cv::flip 関数を利用して作成します。作成および実行環境は Ubuntu上 の Code::Blocks (gccコンパイラ) を想定しています。
対象 OpenRTM-aist のバージョンは 1.1.2 です。


作成手順はおおよそ以下のようになります。

- 動作環境・開発環境についての確認
- OpenCVとcv::flip関数についての確認
- コンポーネントの仕様を決める
- RTCBuilder を用いたソースコードのひな形の作成
- アクティビティ処理の実装
- コンポーネントの動作確認


### cv::flip関数について

cv::flip 関数は、OpenCV で標準的に用いられている cv::Mat型の画像データを垂直軸 (左右反転)、水平軸 (上下反転)、または両軸 (上下左右反転)に対して反転させます。
関数プロトタイプと入出力の引数の意味は以下の通りです。

```
 void flip(const Mat& src, Mat& dst, int flipMode)
 
  
 src       入力配列
 dst       出力配列。もし dst=NULL であれば、src が上書きされます。
 flipMode 配列の反転方法の指定内容:
 　flipMode = 0: X軸周りでの反転(上下反転)
 　flipMode > 0: Y軸周りでの反転(左右反転)
 　flipMode < 0: 両軸周りでの反転(上下左右反転)
```


### コンポーネントの仕様

これから作成するコンポーネントを Flip コンポーネントと呼ぶことにします。

このコンポーネントは画像データ型の入力ポート (InPort) と、反転処理した画像を出力するための出力ポート (OutPort) を持ちます。
それぞれのポートの名前を 入力ポート(InPort)名: **originalImage**、出力ポート(OutPort)名: **flippedImage** とします。

OpenRTM-aist には、OpenCV を使用したビジョン関連のコンポーネントがサンプルとして付属しています。
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

この Flip コンポーネントではこれらのサンプルコンポーネントとデータのやり取りができるよう同じく CameraImage 型を InPort と OutPort に使用することにします。
CameraImage 型は InterfaceDataTypes.idl で定義されており、C++であれば、InterfaceDataTypesSkel.h をインクルードすると使えるようになります。

また、画像を反転させる方向は、左右反転、上下反転、上下左右反転の3通りがあります。これを実行時に指定できるように、RTコンポーネントのコンフィギュレーション機能を使用して指定できるようにします。
パラメーター名は **flipMode** という名前にします。

flipMode は cv::flip 関数の仕様に合わせて、型は int 型とし 上下反転、左右反転、上下左右反転それぞれに 0、1、-1 を割り当てることにします。

flipMode の各値での画像処理のイメージを下図に示します。

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
    <td>説明</td>
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
    <td>説明</td>
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
    <td>デフォルト値</td>
    <td>0</td>
  </tr>
  <tr>
    <td>制約</td>
    <td>(0,-1,1)</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>radio</td>
  </tr>
  <tr>
    <td>説明</td>
    <td><strong>反転モード</strong><br> 上下反転: 0 <br> 左右反転: 1 <br> 上下左右反転: -1</td>
  </tr>
</table>


### 動作環境・開発環境
Linux (ここでは Ubuntu 16.04 を仮定) 上に開発環境を構築します。


インストールスクリプトでインストールします。

```
 $ wget http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_ubuntu.sh
 $ sudo sh pkg_install_ubuntu.sh
```

#### OpenRTP のインストール

[こちらのURL]({{ site.baseurl }}/ja/download/tools/openrtp_1_1_2) からLinux版の OpenRTP(コンポーネント開発ツール、システム開発ツール統合環境) をダウンロード、インストールします。
OepnRTP の実行には Java も必要となりますので default-jre パッケージをインストールします。

```
 $ apt-get install default-jre
 $ wget http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-ja-linux-gtk-x86_64.tar.gz
 $ tar xvzf eclipse442-openrtp112v20160526-ja-linux-gtk-x86_64.tar.gz
```
<!-- $ cd eclipse -->
<!-- $ ./eclipse -->
<!-- $ ./openrtp -->

<span style="color:red;">Eclipse 起動後、RTSystemEditor でネームサーバーに接続できない場合があります。その場合、/etc/hosts の localhost の行に自ホスト名を追記してください。</span>;

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

#### CMake のインストール

```
 $ sudo apt-get install cmake cmake-gui
```

#### OpenCV および OpenCV コンポーネントのインストール

OpenCV および OpenCV のコンポーネントをインストールします。

まず、Ubuntu が提供している OpenCV のパッケージを下記のようにインストールします。

```
 $ sudo apt-get install libopencv-dev libcv2.4 libcvaux2.4 libhighgui2.4
```


リポジトリからソースコードをチェックアウトして、手動でコンパイルを行います。

```
 $ svn  co http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/opencv/
 $ cd opencv
 $ mkdir work
 $ cd work
 $ cmake ..
 $ make
 $ sudo make install
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

#### Code::Blocksのインストール
Code::Blocks は C/C++ に対応した統合開発環境です。
以下のコマンドでインストールできます。

```
 $ sudo apt-get install codeblocks
```

最新版を入手したい場合は以下のコマンドを入力します。

```
 $ sudo add-apt-repository ppa:damien-moore/codeblocks-stable
 $ sudo apt-get update
 $ sudo apt-get install codeblocks
```




### Flip コンポーネントの雛型の生成

Flip コンポーネントの雛型の生成は、RTCBuilder を用いて行います。

#### RTCBuilderの起動

Eclipse では、各種作業を行うフォルダーを「ワークスペース」(Work Space)とよび、原則としてすべての生成物はこのフォルダーの下に保存されます。
ワークスペースはアクセスできるフォルダーであれば、どこに作っても構いませんが、このチュートリアルでは以下のワークスペースを仮定します。

- /home/ユーザー名/workspace

まずは Eclipse を起動します。
OpenRTP を展開したディレクトリーに移動して以下のコマンドを入力します。

```
 $ ./openrtp
```

最初にワークスペースの場所を尋ねられますので、上記のワークスペースを指定してください。


<div align="center"><a href="workspace_ubuntu.png"><img src="workspace_ubuntu.png" width="80%;"></a></div>

<br>

すると、以下のような「ようこそ」画面が表示されます。<br>
「ようこそ」画面は必要ないので左上の [×] ボタンをクリックして閉じてください。
<br>


<div align="center"><a href="install41.png"><img src="install41.png" width="60%;"></a></div>
<div align="center"><strong>Eclipse の初期起動時の画面</strong></div>

右上の [Open Perspective] ボタンをクリックしてください。

<div align="center"><a href="install42.png"><img src="install42.png" width="60%;"></a></div>
<div align="center"><strong>パースペクティブの切り替え</strong></div>

「RTC Builder」を選択し、[OK] ボタンをクリックすることで、RTCBuilder が起動します。

<div align="center"><a href="SelectRTCBuilder.png"><img src="SelectRTCBuilder.png" width="30%;"></a></div>
<div align="center"><strong>パースペクティブの選択</strong></div>


#### 新規プロジェクトの作成

Flip コンポーネントを作成するために、RTCBuilder で新規プロジェクトを作成する必要があります。

左上の [Open New RTCBuilder Editor] のアイコンをクリックしてください。



<div align="center"><a href="CreateProject_0.png"><img src="CreateProject_0.png" width="60%;"></a></div>
<div align="center"><strong>RTC Builder 用プロジェクトの作成</strong></div>

｢プロジェクト名｣欄に作成するプロジェクト名 (ここでは **Flip**) を入力して [終了] をクリックします。

<div align="center"><a href="RT-Component-BuilderProject_0.png"><img src="RT-Component-BuilderProject_0.png" width="60%;"></a></div>


指定した名称のプロジェクトが生成され、パッケージエクスプローラ内に追加されます。


<div align="center"><a href="PackageExplolrer_0.png"><img src="PackageExplolrer_0.png" width="40%;"></a></div>

生成したプロジェクト内には、デフォルト値が設定された RTC プロファイル XML(RTC.xml) が自動的に生成されます。

#### RTC プロファイルエディタの起動

RTC.xml が生成された時点で、このプロジェクトに関連付けられているワークスペースとして RTCBuilder のエディタが開くはずです。
もし起動しない場合はパッケージエクスプローラーの RTC.xml をダブルクリックしてください。


<div align="center"><a href="Open_RTCBuilder_0.png"><img src="Open_RTCBuilder_0.png" width="60%;"></a></div>



#### プロファイル情報入力とコードの生成

まず、いちばん左の「基本」タブを選択し、基本情報を入力します。先ほど決めた Flip コンポーネントの仕様(名前)の他に、概要やバージョン等を入力してください。
ラベルが赤字の項目は必須項目です。その他はデフォルトで構いません。

- モジュール名: Flip
- モジュール概要: 任意(Flip image component)
- バージョン: 任意(1.0.0)
- ベンダ名: 任意
- モジュールカテゴリ: 任意(ImageProcessing)
- コンポーネント型: STATIC
- アクティビティ型: PERIODIC
- コンポーネント種類: DataFlowComponent
- 最大インスタンス数: 1
- 実行型: PeriodicExecutionContext
- 実行周期: 1000.0

<br>

<div align="center"><a href="Basic_0.png"><img src="Basic_0.png" width="50%;"></a></div>
<div align="center"><strong>基本情報の入力</strong></div>
<br>


次に、「アクティビティ」タブを選択し、使用するアクションコールバックを指定します。

Flip コンポーネントでは、onActivated()、onDeactivated()、onExecute() コールバックを使用します。下図のように①の onAtivated をクリック後に ②のラジオボタンにて [ON] にチェックを入れます。
onDeactivated、onExecute についても同様の操作を行います。

<br>

<div align="center"><a href="Activity_0.png"><img src="Activity_0.png" width="90%;"></a></div>
<div align="center"><strong>アクティビティコールバックの選択</strong></div>
<br>


さらに、「データポート」タブを選択し、データポートの情報を入力します。
先ほど決めた仕様を元に以下のように入力します。なお、変数名や表示位置はオプションなので変更しないで結構です。

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

<div align="center"><a href="DataPort_0.png"><img src="DataPort_0.png" width="50%;"></a></div>
<div align="center"><strong>データポート情報の入力</strong></div>
<br>

次に、「コンフィギュレーション」タブを選択し、先ほど決めた仕様を元に、Configuration の情報を入力します。制約条件および Widget とは、RTSystemEditor でコンポーネントのコンフィギュレーションパラメーターを表示する際に、スライダー、スピンボタン、ラジオボタンなど、GUIで値の変更を行うためのものです。

ここでは、flipMode が取りうる値は先ほど仕様を決めたときに、-1、0、1 の3つの値のみ取ることにしたので、ラジオボタンを使用することにします。

<br>
- flipMode
  - 名称: flipMode
  - データ型: int
  - デフォルト値: 0
  - 変数名: flipMode
  - 制約条件: (0, -1, 1) <span style="color:red;">※ (-1: 上下左右反転, 0: 上下反転, 1: 左右反転)</span>;
  - Widget: radio

<br>

<div align="center"><a href="Configuration_0.png"><img src="Configuration_0.png" width="50%;"></a></div>
<div align="center"><strong>コンフィグレーション情報の入力</strong></div>
<br>

次に、「言語・環境」タブを選択し、プログラミング言語を選択します。
ここでは、C++(言語)を選択します。なお、言語・環境はデフォルト等が設定されておらず、指定し忘れるとコード生成時にエラーになりますので、必ず言語の指定を行うようにしてください。

また、C++ の場合デフォルトでは CMake を利用してビルドすることになっていますが、旧式の VC のプロジェクトやソリューションを直接 RTCBuilder が生成する方法を利用したい場合は [Use old build environment] をチェックしてください。

<div align="center"><a href="Language_0.png"><img src="Language_0.png" width="50%;"></a></div>
<div align="center"><strong>プログラミング言語の選択</strong></div>
<br>

最後に、「基本」タブにある [コード生成] ボタンをクリックし、コンポーネントの雛型を生成します。

<br>

<div align="center"><a href="Generate_0.png"><img src="Generate_0.png" width="50%;"></a></div>
<div align="center"><strong>雛型の生成(Generate)</strong></div>
<br>

&color(red){※ 生成されるコード群は、Eclipse 起動時に指定したワークスペースフォルダーの中に生成されます。
現在のワークスペースは、[ファイル] > [ワークスペースの切り替え] で確認することができます。};


### CMake によるビルドに必要なファイルの生成

RTC Builder で生成したコードの中には CMake でビルドに必要な各種ファイルを生成するための CMakeLists.txt が含まれています。
CMake を利用することにより CMakeLists.txt から Visual Studio のプロジェクトファイル、ソリューションファイル、もしくは Makefile 等を自動生成できます。

#### CMakeList.txt の編集

src/CMakeLists.txt を gedit などで開いて編集します。
もしくは Eclipse 画面左のパッケージエクスプローラで src/CMakeLists.txt をダブルクリックもしくはエディタへドラッグアンドドロップしても編集できます。

<div align="center"><a href="EditCmakeLists_0.png"><img src="EditCmakeLists_0.png" width="70%;"></a></div>
<div align="center"><strong>CMakeLists.txtの編集</strong></div>

このコンポーネントでは OpenCV を利用していますので、OpenCV のヘッダのインクルードパス、ライブラリやライブラリサーチパスを与えてやる必要があります。
幸い OpenCV は CMake に対応しており、以下の2行を追加・変更するだけで OpenCV のライブラリがリンクされ使えるようになります。


- src/CMakeLists.txt を修正する
  - Eclipse のパッケージエクスプローラで src/CMakeLists.txt をダブルクリック
- find_package(OpenCV REQUIRED)を追加
- 最初のtarget_link_libraries に ${OpenCV_LIBS} を追加
  - target_link_libraries は2ヶ所あり、上が DLL、下が実行ファイルのライブラリ指定です

```
 set(comp_srcs Flip.cpp )
 set(standalone_srcs FlipComp.cpp)
 
 find_package(OpenCV REQUIRED) ←この行を追加
   ：中略
 add_dependencies(${PROJECT_NAME} ALL_IDL_TGT)
 target_link_libraries(${PROJECT_NAME} ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) ←　OepnCV_LIBSを追加
   ：中略
 add_executable(${PROJECT_NAME}Comp ${standalone_srcs}
   ${comp_srcs} ${comp_headers} ${ALL_IDL_SRCS})
 target_link_libraries(${PROJECT_NAME}Comp ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) ←　OepnCV_LIBSを追加
```


#### CMake(cmake-gui)の操作
CMake を利用してビルド環境の Configure を行います。
まずは CMake (cmake-gui) を起動してください。

```
 $ cmake-gui
```

<div align="center"><a href="CMakeGUI0_0_ubuntu.png"><img src="CMakeGUI0_0_ubuntu.png" width="80%;"></a></div>
<div align="center"><strong>CMake GUIの起動とディレクトリーの指定</strong></div>

画面上部に以下のようなテキストボックスがありますので、それぞれソースコードの場所 (CMakeList.txtがある場所) と、ビルドディレクトリーを指定します。

- **Where is the soruce code**
- **Where to build the binaries**

ソースコードの場所は Flip コンポーネントのソースが生成された場所で CMakeList.txt が存在するディレクトリーです。
デフォルトでは <ワークスペースディレクトリー>/Flip になります。


ビルドディレクトリとは、ビルドするためのプロジェクトファイルやオブジェクトファイル、バイナリを格納する場所のことです。
場所は任意ですが、この場合 <ワークスペースディレクトリー>/Flip/build のように分かりやすい名前をつけた Flip のサブディレクトリーを指定することをお勧めします。

<table class="table-alt">
  <tr>
    <td><strong>Where is the soruce code</strong></td>
    <td>/home/ユーザー名/workspace/Flip</td>
  </tr>
  <tr>
    <td><strong>Where to build the binaries</strong></td>
    <td>/home/ユーザー名/workspace/Flip/build</td>
  </tr>
</table>

指定したら、下のConfigureボタンを押します。すると下図のようなダイアログが表示されますので、生成したいプロジェクトの種類を指定します。
今回は CodeBlocks - Unix Makefiles を指定します。
Code::Blocks を使わない場合は Unix Makefiles を使ってください。

<div align="center"><a href="CMakeGUI1_0_ubuntu.png"><img src="CMakeGUI1_0_ubuntu.png" width="80%;"></a></div>
<div align="center"><strong>生成するプロジェクトの種類の指定</strong></div>

また cmake-gui を使用しない場合は以下のコマンドでファイルを生成できます。

```
 $ mkdir build
 $ cd build
 $ cmake .. -G "CodeBlocks - Unix Makefiles"
```




ダイアログで [Finish] をクリックすると Configure が始まります。問題がなければ下部のログウインドウに「Configuring done」と表示されますので、続けて [Generate] ボタンをクリックします。
「Generating done」と表示されればプロジェクトファイル(.cbp)・Makefile 等の出力が完了します。

なお、CMake は Configure の段階でキャッシュファイルを生成しますので、トラブルなどで設定を変更したり環境を変更した場合は [File] > [Delete Cache] でキャッシュを削除して Configure からやり直してください。



### ヘッダ、ソースの編集

次に先ほど指定した build ディレクトリーの中の Flip.cbp をダブルクリックして Code::Blocks を起動します。

ヘッダ (include/Flip/Flip.h) およびソースコード (src/Flip.cpp) をそれぞれ編集します。
Code::Blocks の Projects から Flip.h、Flip.cpp をダブルクリックすることで編集画面が開きます。


<div align="center"><a href="codeblocks0_0.png"><img src="codeblocks0_0.png" width="60%;"></a></div>


<span style="color:red;">64bitの環境の場合に Code::Blocks の動作が不安定になることがあります。その場合は code completion というプラグインを無効化すると動作することがあります。</span>;

「Plugins」>「Manage plugins...」を選択します。

<div align="center"><a href="codeblocks1_0.png"><img src="codeblocks1_0.png" width="80%;"></a></div>

「code completion」を選択して [Disable] をクリックします。

<div align="center"><a href="codeblocks2_0.png"><img src="codeblocks2_0.png" width="80%;"></a></div>

動作しないときはこの手順を試してください。


#### アクティビティ処理の実装

Flip コンポーネントでは、InPort から受け取った画像を画像保存用バッファに保存し、その保存した画像を OpenCVのcv::flip() 関数にて変換します。
その後、変換された画像を OutPort から送信します。

<br>
onActivated()、onExecute()、onDeactivated() での処理内容を下図に示します。
<br>

<div align="center"><a href="FlipRTC_State_0.png"><img src="FlipRTC_State_0.png" width="50%;"></a></div>
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
 #include <opencv2/opencv.hpp>
```



反転した画像の保存用にメンバー変数を追加します。

```
 private:
     // <rtc-template block="private_attribute">
  
     // </rtc-template>
 
     // <rtc-template block="private_operation">
  
     // </rtc-template>
 	    cv::Mat m_imageBuff;
 	    cv::Mat m_flipImageBuff;
```


#### ソースファイル (Flip.cpp) の編集

下記のように、onActivated()、onDeactivated()、onExecute() を実装します。

```
 RTC::ReturnCode_t Flip::onActivated(RTC::UniqueId ec_id)
 {
 
 	   // OutPortの画面サイズの初期化
 	   m_flippedImage.width = 0;
 	   m_flippedImage.height = 0;
 
 	   return RTC::RTC_OK;
 }
```



```
 RTC::ReturnCode_t Flip::onDeactivated(RTC::UniqueId ec_id)
 {
 	   if (!m_imageBuff.empty())
 	   {
 		   // 画像用メモリの解放
 		   m_imageBuff.release();
 		   m_flipImageBuff.release();
 	   }
 
 	   return RTC::RTC_OK;
 }
```


```
 RTC::ReturnCode_t Flip::onExecute(RTC::UniqueId ec_id)
 {
 	   // 新しいデータのチェック
 	   if (m_originalImageIn.isNew()) {
 		   // InPortデータの読み込み
 		   m_originalImageIn.read();
 
 		   // InPortとOutPortの画面サイズ処理およびイメージ用メモリの確保
 		   if (m_originalImage.width != m_flippedImage.width || m_originalImage.height != m_flippedImage.height)
 		   {
 			   m_flippedImage.width = m_originalImage.width;
 			   m_flippedImage.height = m_originalImage.height;
 
 			   m_imageBuff.create(cv::Size(m_originalImage.width, m_originalImage.height), CV_8UC3);
 			   m_flipImageBuff.create(cv::Size(m_originalImage.width, m_originalImage.height), CV_8UC3);
 
 			
 		   }
 
 		   // InPortの画像データをm_imageBuffにコピー
 		   memcpy(m_imageBuff.data, (void *)&(m_originalImage.pixels[0]), m_originalImage.pixels.length());
 
 		   // InPortからの画像データを反転する。 m_flipMode 0: X軸周り, 1: Y軸周り, -1: 両方の軸周り
 		   cv::flip(m_imageBuff, m_flipImageBuff, m_flipMode);
 
 		   // 画像データのサイズ取得
 		   int len = m_flipImageBuff.channels() * m_flipImageBuff.cols * m_flipImageBuff.rows;
 		   m_flippedImage.pixels.length(len);
 
 		   // 反転した画像データをOutPortにコピー
 		   memcpy((void *)&(m_flippedImage.pixels[0]), m_flipImageBuff.data, len);
 
 		   // 反転した画像データをOutPortから出力する。
 		   m_flippedImageOut.write();
 	   }
 
      return RTC::RTC_OK;
 }
```


### Code::Blocks によるビルド

#### ビルドの実行

Code::Blocksの [ビルド] ボタンをクリックしてビルドを行います。


<br>

<div align="center"><a href="codeblocks_build_0.png"><img src="codeblocks_build_0.png" width="70%;"></a></div>
<div align="center"><strong>ビルドの実行</strong></div>
<br>


### Flip コンポーネントの動作確認

ここでは、カメラコンポーネント (OpenCVCameraComp)とビューアコンポーネント (CameraViewerComp)を接続し動作確認を行います。

#### NameService の起動

コンポーネントの参照を登録するためのネームサービスを起動します。

<br>
```
 $ rtm-naming
```


#### rtc.conf の作成

RTコンポーネントでは、ネームサーバーのアドレスやネームサーバーへの登録フォーマットなどの情報を rtc.conf というファイルで指定する必要があります。

下記の内容を rtc.conf というファイル名で保存し、Flip\build\srcフォルダーに置いて下さい。

<span style="color:red;">※ Eclipse 起動時に workspace をデフォルトのままにしていた場合、Flip フォルダーのパスは、</span>;
<span style="color:red;">   C:\Documents and Settings\<ログインユーザー名>\workspace　となります。</span>;

```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```

#### Flip コンポーネントの起動

Flip コンポーネントを起動します。

先程 rtc.conf ファイルを置いたフォルダにある、FlipComp ファイルを実行してください。

```
 $ FlipComp -f rtc.conf
```

#### カメラコンポーネントとビューアコンポーネントの起動

USBカメラのキャプチャー画像を OutPort から出力する OpenCVCameraComp と InPort で受け取った画像を画面に表示する CameraViewerComp を起動します。

これら２つのコンポーネントは、下記のコマンドにて起動できます。

```
 $ /usr/local/share/openrtm-1.1/components/c++/opencv-rtcs/CameraViewerComp
 $ /usr/local/share/openrtm-1.1/components/c++/opencv-rtcs/OpenCVCameraComp
```




### コンポーネントの接続

下図のように、RTSystemEditor にて
OpenCVCameraComp と Flip、CameraviewerComp コンポーネントを接続します。

<div align="center"><a href="RTSE_Connect_0.png"><img src="RTSE_Connect_0.png" width="70%;"></a></div>
<div align="center"><strong>コンポーネントの接続</strong></div>

#### コンポーネントの Activate

RTSystemEditor の上部にあります [All Activate] というアイコンをクリックし、全てのコンポーネントをアクティブ化します。
正常にアクティベートされた場合、下図のように黄緑色でコンポーネントが表示されます。

<br>

<div align="center"><a href="RTSE_Activate_0.png"><img src="RTSE_Activate_0.png" width="70%;"></a></div>
<div align="center"><strong>コンポーネントのアクティブ化</strong></div>
<br>

#### 動作確認

下図のようにコンフィギュレーションビューにてコンフィギュレーションを変更することができます。

Flipコンポーネントのコンフィギュレーションパラメーター「flipMode」を「0」や「-1」などに変更し、画像の反転が行われるかを確認してください。

<br>

<div align="center"><a href="RTSE_Configuration_0.png"><img src="RTSE_Configuration_0.png" width="70%;"></a></div>
<div align="center"><strong>コンフィギュレーションパラメーターの変更</strong></div>
<br>



