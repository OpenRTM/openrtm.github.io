---
layout: page
title: 画像処理コンポーネントの作成 (windows 10、openrtm-aist-2.0.0、openrtp-2.0.0、cmake-3.19.8、vs2019)
---

<!-- Title: 画像処理コンポーネントの作成 (Windows 10、OpenRTM-aist-2.0.0、OpenRTP-2.0.0、CMake-3.19.8、VS2019) -->
#contents

## はじめに

このケーススタディでは、簡単な画像処理をコンポーネント化する方法を紹介します。既存のカメラコンポーネントと画像表示コンポーネントを利用し、カメラからの画像を左右(または上下)に反転させる処理部分をコンポーネントとして作成してカメラの画像を反転させ表示するシステムを作成します。

画像を反転する処理は簡単に実装することができますが、ここではより簡単に実装するために OpenCV ライブラリを利用し、汎用性の高い RTコンポーネントを作成します。

### OpenCVとは

[OpenCV](http://opencv.jp/) (オープンシーブイ) とはかつてインテルが、現在はItseezが開発・公開しているオープンソースのコンピュータービジョン向けライブラリです。

[Wikipedia](https://ja.wikipedia.org/wiki/OpenCV)より抜粋。

### 作成する RTコンポーネント

- Flip コンポーネント: OpenCV ライブラリが提供する様々な画像処理関数のうち、cv::flip() 関数を用いて画像の反転を行う RTコンポーネント。


## cv::flip 関数の RTコンポーネント化

入力された画像を左右または上下に反転し出力する RTコンポーネントを、OpenCV ライブラリの cv::flip 関数を利用して作成します。作成および実行環境は Windows上 の Visual Studio を想定しています。対象 OpenRTM-aist のバージョンは 1.1.2 です。


作成手順はおおよそ以下のようになります。

- 動作環境・開発環境についての確認
- OpenCV と cv::flip 関数についての確認
- コンポーネントの仕様を決める
- RTCBuilder を用いたソースコードのひな形の作成
- アクティビティ処理の実装
- コンポーネントの動作確認


### cv::flip関数について

cv::flip 関数は、OpenCV で標準的に用いられている cv::Mat 型の画像データを垂直軸 (左右反転)、水平軸 (上下反転)、または両軸 (上下左右反転)に対して反転させます。関数プロトタイプと入出力の引数の意味は以下の通りです。

```
 void flip(const Mat& src, Mat& dst, int flipMode)
```


<table class="table-alt">
  <tr>
    <td>src</td>
    <td>入力配列</td>
  </tr>
  <tr>
    <td>dst</td>
    <td>出力配</td>
  </tr>
  <tr>
    <td>flipMode</td>
    <td>配列の反転方法の指定内容:<br>　flipMode = 0: X軸周りでの反転(上下反転)<br>　flipMode > 0: Y軸周りでの反転(左右反転)<br>　flipMode < 0: 両軸周りでの反転(上下左右反転)</td>
  </tr>
</table>


### コンポーネントの仕様 &aname(flip_info);

これから作成するコンポーネントを Flip コンポーネントと呼ぶことにします。

このコンポーネントは画像データ型の入力ポート (InPort) と、反転処理した画像を出力するための出力ポート (OutPort) を持ちます。それぞれのポートの名前を 入力ポート(InPort)名: **originalImage**、出力ポート(OutPort)名: **flippedImage** とします。

OpenRTM-aist には OpenCV を使用したビジョン関連のコンポーネントがサンプルとして付属しています。これらのコンポーネントのデータポートは画像の入出力に以下のような CameraImage 型を使用しています。

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

このFlipコンポーネントではこれらのサンプルコンポーネントとデータのやり取りができるよう同じく CameraImage型 を InPort と OutPort に使用することにします。

CameraImage型 は InterfaceDataTypes.idl で定義されており、C++であれば、InterfaceDataTypesSkel.h をインクルードすると使えるようになります。

また、画像を反転させる方向は、左右反転、上下反転、上下左右反転の3通りがあります。これを実行時に指定できるように、RTコンポーネントのコンフィギュレーション機能を使用して指定できるようにします。パラメーター名は **flipMode** という名前にします。

flipMode は cv::flip 関数の仕様に合わせて、型は int 型とし 上下反転、左右反転、上下左右反転それぞれに 0、1、-1 を割り当てることにします。

flipMode の各値での画像処理のイメージを下図に示します。

<div align="center"><a href="cvFlip_and_FlipRTC.png"><img src="cvFlip_and_FlipRTC.png" width="70%;"></a></div>
<div align="center"><strong>Flipコンポーネントの flipMode 指定時の画像反転パターン</strong></div>

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
    <td>RTC::CameraImage</td>
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
    <td>RTC::CameraImage</td>
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
    <td>(0,-1, 1)</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>radio</td>
  </tr>
  <tr>
    <td>説明</td>
    <td><strong>反転モード</strong> <br> 上下反転: 0 <br> 左右反転: 1 <br> 上下左右反転: -1</td>
  </tr>
</table>


### 動作環境・開発環境
ここで動作環境および開発環境を確認しておきます。

- OS: Windows 10(11、8.1 でも可能)
- コンパイラ: [Visual Studio 2019 Community]({{ site.baseurl }}/ja/doc/installation/install_1_2/cpp_1_2/install_windows_1_2/visual_studio_1_2/visual_studio_2022)
- [OpenRTM-aist-2.0.0-RC220404_x86_64]()（リンク切れです）
- [CMake](https://github.com/Kitware/CMake/releases/download/v3.23.1/cmake-3.23.1-windows-x86_64.msi)


OpenRTM-aist-1.1 以降では、コンポーネントのビルドに CMake を使用します。

### Flipコンポーネントの雛型の生成

Flipコンポーネントの雛型の生成は、RTCBuilder を用いて行います。

#### RTCBuilderの起動

Eclipse では、各種作業を行うフォルダーを「ワークスペース」(Work Space)とよび、原則としてすべての生成物はこのフォルダの下に保存されます。
ワークスペースはアクセスできるフォルダーであれば、どこに作っても構いませんが、このチュートリアルでは以下のワークスペースを仮定します。

- C:\workspace

まずは Eclipse を起動します。
Windows 10の場合はデスクトップの以下のショートカットをダブルクリックして起動します。

<div align="center"><a href="flip1.png"><img src="flip1.png" width="15%;"></a></div>

最初にワークスペースの場所を尋ねられますので、上記のワークスペースを指定して [OK] をクリックしてください。


<div align="center"><a href="flip2.png"><img src="flip2.png" width="60%;"></a></div>

すると、以下のようなWelcomeページが表示されます。<br>
Welcomeページは必要ないので左上の [×] ボタンをクリックして閉じてください。
<br>


<div align="center"><a href="flip3.png"><img src="flip3.png" width="60%;"></a></div>
<div align="center"><strong>Eclipseの初期起動時の画面</strong></div>

右上の [Open Perspective] ボタンをクリックしてください。

<div align="center"><a href="flip4.png"><img src="flip4.png" width="60%;"></a></div>
<div align="center"><strong>パースペクティブの切り替え</strong></div>

「RTC Builder」を選択し、[OK] ボタンをクリックします。<br>
RTCBuilderが起動します。

<div align="center"><a href="flip5.png"><img src="flip5.png" width="60%;"></a></div>
<div align="center"><strong>パースペクティブの選択</strong></div>

#### 新規プロジェクトの作成

Flipコンポーネントを作成するために、RTCBuilder で新規プロジェクトを作成する必要があります。

左上の [Open New RTCBuilder Editor] のアイコンをクリックしてください。



<div align="center"><a href="flip6.png"><img src="flip6.png" width="60%;"></a></div>
<div align="center"><strong>RTC Builder 用プロジェクトの作成</strong></div>

｢プロジェクト名｣欄に作成するプロジェクト名 (ここでは **Flip**) を入力して [終了] をクリックします。

<div align="center"><a href="flip7.png"><img src="flip7.png" width="60%;"></a></div>


指定した名称のプロジェクトが生成され、パッケージエクスプローラ内に追加されます。


<div align="center"><a href="flip8.png"><img src="flip8.png" width="60%;"></a></div>

生成したプロジェクト内には、デフォルト値が設定された RTC プロファイル XML(RTC.xml) が自動的に生成されます。

#### RTC プロファイルエディタの起動

RTC.xmlが生成された時点で、このプロジェクトに関連付けられているワークスペースとして RTCBuilder のエディタが開くはずです。



#### プロファイル情報入力とコードの生成

まず、いちばん左の「基本」タブを選択し、基本情報を入力します。先ほど決めた Flip コンポーネントの仕様(名前)の他に、概要やバージョン等を入力してください。ラベルが赤字の項目は必須項目です。その他はデフォルトで構いません。

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

<div align="center"><a href="flip9.png"><img src="flip9.png" width="60%;"></a></div>
<div align="center"><strong>基本情報の入力</strong></div>
<br>


次に、「アクティビティ」タブを選択し、使用するアクションコールバックを指定します。

Flipコンポーネントでは、onActivated()、onDeactivated()、onExecute()コールバックを使用します。下図のように①の onAtivated をクリック後に ②のラジオボタンにて [ON] にチェックを入れます。onDeactivated、onExecute についても同様の操作を行います。

<br>

<div align="center"><a href="flip10.png"><img src="flip10.png" width="60%;"></a></div>
<div align="center"><strong>アクティビティコールバックの選択</strong></div>
<br>


さらに、「データポート」タブを選択し、データポートの情報を入力します。
先ほど決めた仕様を元に以下のように入力します。なお、変数名や表示位置はオプションなので、変更しなくて結構です。

<br>

- InPort Profile:
  - ポート名: originalImage
  - データ型: RTC::CameraImage
  - 変数名:  originalImage
  - 表示位置: left

<br>

- OutPort Profile:
  - ポート名: flippedImage
  - データ型: RTC::CameraImage
  - 変数名:  flippedImage
  - 表示位置: right

<br>

<div align="center"><a href="flip11.png"><img src="flip11.png" width="60%;"></a></div>
<div align="center"><strong>データポート情報の入力</strong></div>
<br>

次に、「コンフィギュレーション」タブを選択し、先ほど決めた仕様を元に、Configuration の情報を入力します。制約条件および Widget とは、RTSystemEditor でコンポーネントのコンフィギュレーションパラメーターを表示する際に、スライダー、スピンボタン、ラジオボタンなど、GUIで値の変更を行うためのものです。

ここでは、flipMode が取りうる値は先ほど仕様を決めたときに、-1、0、1 の3つの値のみ取ることにしたので、ラジオボタンを使用することにします。

<br>

- flipMode
  - 名称: flipMode
  - データ型: int
  - デフォルト値: 0
  - 制約条件: (0, -1, 1)
    - <span style="color:red;">※ (-1: 上下左右反転、 0: 上下反転、 1: 左右反転)</span>;
  - Widget: radio

<br>

<div align="center"><a href="flip12.png"><img src="flip12.png" width="60%;"></a></div>
<div align="center"><strong>コンフィグレーション情報の入力</strong></div>
<br>

次にプログラミング言語の選択とコードの生成を行いますが、<span style="color:red;">OpenRTM-aist 2.0と1.2でツールの仕様が変わっています。</span>;

まずは1.2.2以前のバージョンの手順について説明します。


「言語・環境」タブを選択し、プログラミング言語を選択します。ここでは、C++(言語)を選択します。なお、言語・環境はデフォルト等が設定されておらず、指定し忘れるとコード生成時にエラーになりますので、必ず言語の指定を行うようにしてください。


<div align="center"><a href="Language_0.png"><img src="Language_0.png" width="50%;"></a></div>
<div align="center"><strong>プログラミング言語の選択</strong></div>
<br>

最後に、「基本」タブにある"コード生成"ボタンをクリックし、コンポーネントの雛型を生成します。

<br>

<div align="center"><a href="Generate_0.png"><img src="Generate_0.png" width="50%;"></a></div>
<div align="center"><strong>雛型の生成(Generate)</strong></div>
<br>


次に2.0以降のバージョンの手順について説明します。

「基本」タブを選択して、下にスクロールすると見える「言語」の項目でC++を選択します。

<div align="center"><a href="flip13.png"><img src="flip13.png" width="60%;"></a></div>

最後に**コード生成**ボタンをクリックし、コンポーネントの雛型を生成します。


コード生成が完了したら、以下のようにFlipプロジェクトを右クリックして、「表示方法」->「システム・エクスプローラー」をクリックすることで、エクスプローラーでワークスペースのフォルダを開いてください。
Flipフォルダに各種ファイルが生成されているか確認してください。

<div align="center"><a href="flip14.png"><img src="flip14.png" width="60%;"></a></div>


### CMakeによるビルドに必要なファイルの生成

RTC Builder で生成したコードの中には CMake でビルドに必要な各種ファイルを生成するための CMakeLists.txt が含まれています。
CMake を利用することにより CMakeLists.txt から Visual Studio のプロジェクトファイル、ソリューションファイル、もしくは Makefile 等を自動生成できます。

#### CMakeList.txt の編集

Flipフォルダのsrc/CMakeLists.txtをメモ帳などで開いて編集します。

<div align="center"><a href="flip15.png"><img src="flip15.png" width="60%;"></a></div>
<div align="center"><strong>CMakeLists.txtの編集</strong></div>

このコンポーネントでは OpenCV を利用していますので、OpenCV のヘッダのインクルードパス、ライブラリやライブラリサーチパスを設定する必要があります。OpenCV は CMake に対応しており、以下の2行を追加・変更するだけで OpenCV のライブラリがリンクされ使えるようになります。


- src/CMakeLists.txt を修正する
  - エクスプローラで src/CMakeLists.txt をダブルクリックしてメモ帳で開く
1. find_package(OpenCV REQUIRED)を追加
1. 最初のtarget_link_libraries に ${OpenCV_LIBS} を追加
  - target_link_libraries は2ヶ所あり、上がDLL、下が実行ファイルのライブラリ指定です

```
 set(comp_srcs Flip.cpp )
 set(standalone_srcs FlipComp.cpp)
 
 find_package(OpenCV REQUIRED) # <- この行を追加
   ：中略
 add_dependencies(${PROJECT_NAME} ALL_IDL_TGT)
 target_link_libraries(${PROJECT_NAME} ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) # <- OepnCV_LIBSを追加
   ：中略
 add_executable(${PROJECT_NAME}Comp ${standalone_srcs}
   ${comp_srcs} ${comp_headers} ${ALL_IDL_SRCS})
 add_dependencies(${PROJECT_NAME}Comp ALL_IDL_TGT)
 target_link_libraries(${PROJECT_NAME}Comp ${OPENRTM_LIBRARIES} ${OpenCV_LIBS})  # <- OepnCV_LIBSを追加
```


#### CMake(cmake-gui)の操作
CMakeを利用してビルド環境のConfigureを行います。
まずはCMake(cmake-gui)を起動してください。Windows 10の場合は画面左下の「ここに入力して検索」にCMakeと入力して検索してください。

<div align="center"><a href="flip16.png"><img src="flip16.png" width="60%;"></a></div>

<div align="center"><a href="flip17.png"><img src="flip17.png" width="60%;"></a></div>
<div align="center"><strong>CMake GUIの起動とディレクトリーの指定</strong></div>

画面上部に以下のようなテキストボックスがありますので、それぞれソースコードの場所( CMakeList.txt がある場所) と、ビルドディレクトリーを指定します。

- **Where is the soruce code**
- **Where to build the binaries**

ソースコードの場所は Flip コンポーネントのソースが生成された場所で CMakeList.txt が存在するディレクトリーです。デフォルトでは <ワークスペースディレクトリー>/Flip になります。

FlipフォルダのCMakeLists.txtをcmake-guiにドラッグアンドドロップすると、Flipフォルダのパスが自動的に入力されます。

<div align="center"><a href="flipzu1.png"><img src="flipzu1.png" width="60%;"></a></div>

ビルドディレクトリーとは、ビルドするためのプロジェクトファイルやオブジェクトファイル、バイナリを格納する場所のことです。場所は任意ですが、この場合 <ワークスペースディレクトリー>/Flip/build のように分かりやすい名前をつけたFlipのサブディレクトリーを指定することをお勧めします。

<table class="table-alt">
  <tr>
    <th>**Where is the soruce code**</th>
    <th>C:\workspace\Flip</th>
  </tr>
  <tr>
    <td>**Where to build the binaries**</td>
    <td>C:\workspace\Flip\build</td>
  </tr>
</table>

指定したら、下のConfigureボタンを押します。Create Directoryの画面が出たらYESをクリックしてください。

<div align="center"><a href="flip20.png"><img src="flip20.png" width="60%;"></a></div>


すると下図のようなダイアログが表示されますので、生成したいプロジェクトの種類を指定します。
今回は Visual Studio 16 2019 とします。VS2017やVS2022 を利用している方はそれぞれ読み替えてください。項目にVisual Studio 2022が無い場合は、cmake-guiのバージョンが古いため最新のバージョンをインストールし直してください。


<div align="center"><a href="flip21.png"><img src="flip21.png" width="60%;"></a></div>
<div align="center"><strong>生成するプロジェクトの種類の指定</strong></div>

ダイアログで [Finish] をクリックすると Configure が始まります。問題がなければ下部のログウインドウに「Configuring done」と表示されますので、続けて [Generate] ボタンをクリックします。「Generating done」と表示されればプロジェクトファイル・ソリューションファイル等の出力が完了します。

<div align="center"><a href="flip22.png"><img src="flip22.png" width="60%;"></a></div>

「Open Project」ボタンを押すと、Visual Studio 2019が起動して先ほど指定した build ディレクトリーの中の Flip.sln を 開きます。

<div align="center"><a href="flip23.png"><img src="flip23.png" width="60%;"></a></div>

なお、CMake は Configure の段階でキャッシュファイルを生成しますので、トラブルなどで設定を変更したり環境を変更した場合は [File] > [Delete Cache] でキャッシュを削除して Configure からやり直してください。



### ヘッダ、ソースの編集



ヘッダ (include/Flip/Flip.h) およびソースコード (src/Flip.cpp) をそれぞれ編集します。
Visual Studio のソリューションエクスプローラから Flip.h、Flip.cpp をクリックすることで編集画面が開きます。


<div align="center"><a href="flip25.png"><img src="flip25.png" width="60%;"></a></div>



#### アクティビティ処理の実装

Flip コンポーネントでは、InPort から受け取った画像を画像保存用バッファに保存し、その保存した画像を OpenCVのcv::flip() 関数にて変換します。その後、変換された画像を OutPort から送信します。

<br>
onActivated()、onExecute()、onDeactivated()での処理内容を下図に示します。
<br>

<div align="center"><a href="FlipRTC_State_0.png"><img src="FlipRTC_State_0.png" width="50%;"></a></div>
<div align="center"><strong>アクティビティ処理の概要</strong></div>
<br>

onExecute() での処理を下図に示します。

<br>

<div align="center"><a href="FlipRTC.png"><img src="FlipRTC.png" width="60%;"></a></div>
<div align="center"><strong>onExucete()での処理内容</strong></div>
<br>

#### ヘッダファイル (Flip.h) の編集

OpenCV のライブラリを使用するため、OpenCV のインクルードファイルをインクルードします。

```
 #include <rtm/DataInPort.h>
 #include <rtm/DataOutPort.h>
 
 #include <opencv2/opencv.hpp> #この行を追加
 
 
 // <rtc-template block="component_description">
```


反転した画像の保存用にメンバー変数を追加します。

```
 private:
   // <rtc-template block="private_attribute">
  
   // </rtc-template>
  
   // <rtc-template block="private_operation">
  
   // </rtc-template>
  cv::Mat m_imageBuff; #この行を追加
  cv::Mat m_flipImageBuff; #この行を追加
```


#### ソースファイル (Flip.cpp) の編集

下記のように、onActivated()、onDeactivated()、onExecute() を実装します。

```
 RTC::ReturnCode_t Flip::onActivated(RTC::UniqueId ec_id)
 {
 
 	   // OutPortの画面サイズを0に設定
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
 
 		   // InPortからの画像データを反転する。 m_flipMode 0: X軸周り、1: Y軸周り、-1: 両方の軸周り
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


### Visual Studioによるビルド

#### ビルドの実行

Visual Studioの「ビルド」→「ソリューションのビルド」を選択してビルドを行います。


<br>

<div align="center"><a href="flip27.png"><img src="flip27.png" width="60%;"></a></div>
<div align="center"><strong>ビルドの実行</strong></div>
<br>


### Flipコンポーネントの動作確認

ここでは、OpenRTM-aist-1.1 以降で同梱されるようになったカメラコンポーネント (OpenCVCameraComp)とビューアコンポーネント (CameraViewerComp)を接続し動作確認を行います。

まずはRTSystemEditorを起動します。
OpenRTPのパースペクティブを開く画面からRTSystemEditorを選択して開いてください。

<div align="center"><a href="flip4.png"><img src="flip4.png" width="60%;"></a></div>

<div align="center"><a href="flip28.png"><img src="flip28.png" width="60%;"></a></div>

#### NameServiceの起動

コンポーネントの参照を登録するためのネームサービスを起動します。

<br>
RTSystemEditorのネームサービスビュー上部のネームサービス起動ボタンを押してください。

<div align="center"><a href="flip29.png"><img src="flip29.png" width="60%;"></a></div>

#### Flipコンポーネントの起動

Flip コンポーネントを起動します。

build/src/Debug (もしくはbuild/src/Release)フォルダの FlipComp.exe ファイルを実行して下さい。

<div align="center"><a href="flip30.png"><img src="flip30.png" width="60%;"></a></div>

#### カメラコンポーネントとビューアコンポーネントの起動

USBカメラのキャプチャ画像を OutPort から出力する OpenCVCameraComp と、InPort で受け取った画像を画面に表示する CameraViewerComp を起動します。

これら２つのコンポーネントは、下記の手順にて起動できます。


- Windows 10の場合は画面左下の「ここに入力して検索」に「C++_OpenCV-Examples」と入力して検索してください。

<div align="center"><a href="flip31.png"><img src="flip31.png" width="60%;"></a></div>


- エクスプローラーが立ち上がるので、「OpenCVCameraComp.bat」と「CameraViewerComp.bat」をそれぞれクリックして実行します。


<div align="center"><a href="flip32.png"><img src="flip32.png" width="60%;"></a></div>


### コンポーネントの接続

コンポーネントが起動すると、以下のようにネームサービスビューにFlip、CameraViewer、OpenCVCameraコンポーネントが表示されるため、左上の「Open New System Editor」ボタン (ONのボタン) をクリックしてエディタを起動後に、エディタにコンポーネントをドラッグアンドドロップします。

<div align="center"><a href="flipzu2.png"><img src="flipzu2.png" width="60%;"></a></div>

下図のように、RTSystemEditorにて OpenCVCameraComp と Flip、CameraviewerComp コンポーネントを接続します。

<div align="center"><a href="flip35.png"><img src="flip35.png" width="60%;"></a></div>
<div align="center"><strong>コンポーネントの接続</strong></div>

ポートの接続は、片側のポートからもう片側のポートにドラッグアンドドロップすることでコネクタが生成されます。

<div align="center"><a href="flip39.png"><img src="flip39.png" width="60%;"></a></div>

#### コンポーネントのActivate

RTSystemEditor の上部にあります「All Activate」というアイコンをクリックし、全てのコンポーネントをアクティブ化します。正常にアクティベートされた場合、下図のように黄緑色でコンポーネントが表示されます。

<br>

<div align="center"><a href="flip36.png"><img src="flip36.png" width="60%;"></a></div>
<div align="center"><strong>コンポーネントのアクティブ化</strong></div>
<br>

#### 動作確認

下図のようにコンフィギュレーションビューにてコンフィギュレーションを変更することができます。

<div align="center"><a href="flip40.png"><img src="flip40.png" width="60%;"></a></div>

エディタ上のFlipコンポーネントをクリックして編集ボタンを押してください。

Flip コンポーネントのコンフィギュレーションパラメーター「flipMode」を「0」や「-1」などに変更し、画像の反転が行われるかを確認してください。

<br>

<div align="center"><a href="flip37.png"><img src="flip37.png" width="60%;"></a></div>
<div align="center"><strong>コンフィギュレーションパラメーターの変更</strong></div>
<br>

コンポーネントを終了する場合は、「All Exit」ボタンを押すとエディタ上のコンポーネントが全て終了します。

<div align="center"><a href="flip38.png"><img src="flip38.png" width="60%;"></a></div>

