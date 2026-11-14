---
layout: page
title: 画像処理コンポーネントの作成(openrtm-aist-1.1、cmake、vc2010)
---

<!-- Title: 画像処理コンポーネントの作成(OpenRTM-aist-1.1、CMake、VC2010) -->
#contents

## はじめに

このケーススタディでは、簡単な画像処理をコンポーネント化する方法を紹介します。
既存のカメラコンポーネントと画像表示コンポーネントを利用し、カメラからの画像を左右(または上下)に反転させる処理部分をコンポーネントとして作成してカメラの画像を反転させ表示するシステムを作成します。

画像を反転する処理は簡単に実装することができますが、ここでは、より簡単に実装するのため OpenCV ライブラリを利用して汎用性の高い RTコンポーネントを作成します。

### OpenCV とは

[OpenCV](http://opencv.jp/) (オープンシーブイ) とはかつてインテルが、現在は Willow Garage が開発・公開しているオープンソースのコンピュータービジョン向けライブラリです。

[Wikipedia](https://ja.wikipedia.org/wiki/OpenCV)より抜粋。

### 作成する RTコンポーネント

- Flipコンポーネント: OpenCV ライブラリーが提供する様々な画像処理関数のうち、cvFlip() 関数を用いて画像の反転を行う RTコンポーネント。

## cvFlip 関数の RTコンポーネント化

入力された画像を左右または上下に反転し出力する RTコンポーネントを、OpenCV ライブラリの cvFlip 関数を利用して作成します。
作成および実行環境は Windows 上の Visual C++ を想定しています。対象 OpenRTM-aist のバージョンは 1.1.0 です。


作成手順はおおよそ以下のようになります。

- 動作環境・開発環境についての確認
- OpenCV と cvFlip 関数についての確認
- コンポーネントの仕様を決める
- RTCBuilder を用いたソースコードのひな形の作成
- アクティビティ処理の実装
- コンポーネントの動作確認

### cvFlip 関数について

cvFlip 関数は、OpenCV で標準的に用いられている IplImage 型の画像データを垂直軸 (左右反転)、水平軸 (上下反転)、または両軸 (上下左右反転)に対して反転させます。
関数プロトタイプと入出力の引数の意味は以下のとおりです。

```
 void cvFlip(IplImage* src, IplImage* dst=NULL, int flipMode=0);
 #define cvMirror cvFlip
  
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

OpenRTM-aist には OpenCVを使用したビジョン関連のコンポーネントがサンプルとして付属しています。
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

flipMode は cvFlip 関数の仕様に合わせて、型は int 型とし、上下反転、左右反転、上下左右反転それぞれに 0、1、-1 を割り当てることにします。

flipMode の各値での画像処理のイメージを図1に示します。

<div align="center"><a href="cvFlip_and_FlipRTC.png"><img src="cvFlip_and_FlipRTC.png" width="60%;"></a></div>
<div align="center"><strong>図1. Flip コンポーネントの flipMode 指定時の画像反転パターン</strong></div>

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
    <td><strong>>反転モード</strong> <br> 上下反転: 0 <br> 左右反転: 1 <br> 上下左右反転: -1</td>
  </tr>
</table>


### 動作環境・開発環境
ここで動作環境および開発環境を確認しておきます。

- OS: Windows XP SP3 (Vista、7でも可能)
- コンパイラ: [Visual C++ 2010 Express Edition 日本語版](http://go.microsoft.com/fwlink/?LinkId=190491&clcid=0x411)

- [OpenRTM-aist-1.1.0-RC3 (C++版), Win32 VC2010]({{ site.baseurl }}/ja/download/openrtm-aist-content/110-rc3)

- RTSystemEditor 1.1
- RTCBuilder 1.1
  - [Eclipse3.4.2+RTSE+RTCB(1.1.0-RC2) Windows用全部入り]()（リンク切れです）

- [Doxygen](http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.11-setup.exe) ドキュメント生成に必要
- [CMake](https://cmake.org/files/v3.5/cmake-3.5.2-win32-x86.msi)


- [解凍ツール(Lhaplus)](http://www.forest.impress.co.jp/lib/arc/archive/archiver/lhaplus.html)

OpenRTM-aist-1.1 以降では、コンポーネントのビルドに CMake を使用します。
また、RTC のひな形生成ツール RTCBuilder では、ドキュメントを入力して Doxygen に処理させることで、コンポーネントのマニュアルも自動で生成することができるようになっています。
このため CMake で Configure を行うときに Doxygen が要求されるので予めインストールしておく必要があります。


### Flip コンポーネントの雛型の生成

Flip コンポーネントの雛型の生成は、RTCBuilder を用いて行います。

#### RTCBuilder の起動

新規ワークスペースを指定して Eclipse を起動すると、以下のような「ようこそ」画面が表示されます。<br>
「ようこそ」画面は必要ないので左上の [×] ボタンをクリックして閉じてください。


<div align="center"><a href="fig1-1EclipseInit.png"><img src="fig1-1EclipseInit.png" width="60%;"></a></div>1
<div align="center"><strong>図2. Eclipseの初期起動時の画面</strong></div>

右上の [Open Perspective] ボタンをクリックし、プルダウンの「Other…」を選択します。


<div align="center"><a href="fig2-2PerspectiveSwitch.png"><img src="fig2-2PerspectiveSwitch.png" width="60%;"></a></div>
<div align="center"><strong>図3. パースペクティブの切り替え</strong></div>

「RTC Builder」を選択し、[OK] ボタンをクリックします。


<div align="center"><a href="fig2-3PerspectiveSelection.png"><img src="fig2-3PerspectiveSelection.png" width="60%;"></a></div>
<div align="center"><strong>図4. パースペクティブの選択</strong></div>

RTCBuilder が起動します。
<br>

<div align="center"><a href="NewRTCBEditor.png"><img src="NewRTCBEditor.png" width="70%;"></a></div>
<div align="center"><strong>図5. RTC Builder の初期起動時画面</strong></div>
<br>

#### 新規プロジェクトの作成

Flip コンポーネントを作成するために、RTCBuilder で新規プロジェクトを作成する必要があります。メニューから [ファイル] > [新規] > [プロジェクト] を選択します。


<div align="center"><a href="fig2-5CreateProject.png"><img src="fig2-5CreateProject.png" width="60%;"></a></div>
<div align="center"><strong>図6. RTC Builder 用プロジェクトの作成　１</strong></div>

表示された ｢新規プロジェクト｣ 画面において，[その他] > [RTCビルダ] を選択し、[次へ] をクリックします。
<br>


<div align="center"><a href="fig2-6CreateProject2.png"><img src="fig2-6CreateProject2.png" width="60%;"></a></div>
<div align="center"><strong>図7. RTC Builder 用プロジェクトの作成　２</strong></div>

｢プロジェクト名｣欄に作成するプロジェクト名 (ここでは **Flip**) を入力して [完了] をクリックします。


<div align="center"><a href="RT-Component-BuilderProject.png"><img src="RT-Component-BuilderProject.png" width="60%;"></a></div>
<div align="center"><strong>図8. RTC Builder 用プロジェクトの作成　３</strong></div>

指定した名称のプロジェクトが生成され、パッケージエクスプローラー内に追加されます。
<br>


<div align="center"><a href="PackageExplolrer.png"><img src="PackageExplolrer.png" width="30%;"></a></div>
<div align="center"><strong>図9. RTC Builder 用プロジェクトの作成　４</strong></div>

生成したプロジェクト内には、デフォルト値が設定された RTC プロファイル XML(RTC.xml) が自動的に生成されます。


#### RTC プロファイルエディタの起動
RTC.xml が生成された時点で、このプロジェクトに関連付けられているワークスペースとして RTCBuilder のエディタが開くはずです。
もし開かない場合は、ツールバーの [Open New RtcBuilder Editor] ボタンをクリックするか、メニューから [ファイル] > [Open New Builder Editor] を選択します。


<div align="center"><a href="Open_RTCBuilder.png"><img src="Open_RTCBuilder.png" width="30%;"></a></div>
<div align="center"><strong>図10. ツールバーから Open New RtcBuilder Editor</strong></div>

<div align="center"><a href="fig2-10FileMenuOpenNewBuilder.png"><img src="fig2-10FileMenuOpenNewBuilder.png" width="30%;"></a></div>
<div align="center"><strong>図11. ファイルメニューから Open New Builder Editor</strong></div>


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
- 実行周期: 0.0 (<span style="color:RED;">図13では1.0となってますが 0.0 としてください.</span>;)
<br>
- Output Project: Flip


<br>

<div align="center"><a href="Basic.png"><img src="Basic.png" width="70%;"></a></div>
<div align="center"><strong>図13. 基本情報の入力</strong></div>
<br>

次に、「アクティビティ」タブを選択し、使用するアクションコールバックを指定します。

Flipコンポーネントでは、onActivated()、onDeactivated()、onExecute()コールバックを使用します。
図14のように①の onAtivated をクリック後に ②のラジオボタンにて [ON] にチェックを入れます。onDeactivated、onExecute についても同様の操作を行います。

<br>

<div align="center"><a href="Activity.png"><img src="Activity.png" width="70%;"></a></div>
<div align="center"><strong>図14. アクティビティコールバックの選択</strong></div>
<br>

次に、「データポート」タブを選択し、データポートの情報を入力します。先ほど決めた仕様を元に以下のように入力します。
なお、変数名や表示位置はオプションのため、変更しないで結構です。

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
<div align="center"><strong>図15. データポート情報の入力</strong></div>
<br>

次に、「コンフィギュレーション」タブを選択し、先ほど決めた仕様を元に、Configuration の情報を入力します。
制約条件および Widget とは、RTSystemEditor でコンポーネントのコンフィギュレーションパラメーターを表示する際に、スライダー、スピンボタン、ラジオボタンなど、GUIで値の変更を行うためのものです。

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
<div align="center"><strong>図16. コンフィグレーション情報の入力</strong></div>
<br>

次に、「言語・環境」タブを選択し、プログラミング言語を選択します。ここでは、C++(言語)を選択します。
なお、言語・環境はデフォルト等が設定されておらず、指定し忘れるとコード生成時にエラーになりますので、必ず言語の指定を行うようにしてください。

また、C++ の場合デフォルトでは CMake を利用してビルドすることになっていますが、旧式の VC のプロジェクトやソリューションを直接 RTCBuilder が生成する方法を利用したい場合は **Use old build environment** をチェックしてください。

<div align="center"><a href="Language.png"><img src="Language.png" width="70%;"></a></div>
<div align="center"><strong>図17. プログラミング言語の選択</strong></div>
<br>

最後に、「基本」タブにある [コード生成] ボタンをクリックし、コンポーネントの雛型を生成します。

<br>

<div align="center"><a href="Generate.png"><img src="Generate.png" width="70%;"></a></div>
<div align="center"><strong>図18. 雛型の生成(Generate)</strong></div>
<br>

&color(Red){※ 生成されるコード群は、Eclipse 起動時に指定したワークスペースフォルダーの中に生成されます。
現在のワークスペースは、[ファイル] > [ワークスペースの切り替え] で確認することができます。};


#### 仮ビルド

さて、ここまでで Flip コンポーネントのソースコードが生成されました。
処理の中身は実装されていないので、InPort に画像を入力しても何も出力されませんが、生成直後のソースコードだけでもコンパイルおよび実行はできます。

※サービスポートとプロバイダーを持つコンポーネントの場合、実装を行わないとビルドが通らないものもあります。

では、まず CMake を利用してビルド環境の Configure を行います。Linux であれば、Flip コンポーネントのソースが生成されたディレクトリーで

```
 $ cmake .
 $ make
```

とすれば、Configure およびビルドが完了するはずです。

Windows の場合は GUI を利用して Configure してみます。
スタートメニューなどから **CMake (cmake-gui)** を起動します。

<div align="center"><a href="CMakeGUI0.png"><img src="CMakeGUI0.png" width="50%;"></a></div>
<div align="center"><strong>図19. CMake GUI の起動とディレクトリーの指定</strong></div>

画面上部に以下のようなテキストボックスがありますので、それぞれソースコードの場所(CMakeList.txtがある場所) と、ビルドディレクトリーを指定します。

- Where is the soruce code
^ Where to build the binaries

ソースコードの場所は Flip コンポーネントのソースが生成された場所で、CMakeList.txt が存在するディレクトリーです。
デフォルトでは <ワークスペースディレクトリー>/Flip になります。

また、ビルドディレクトリーとは、ビルドするためのプロジェクトファイルやオブジェクトファイル、バイナリを格納する場所のことです。
場所は任意ですが、この場合 <ワークスペースディレクトリー>/Flip/build のように分かりやすい名前をつけた Flip のサブディレクトリーを指定することをお勧めします。

指定したら、[Configure] ボタンをクリックします。すると図20のようなダイアログが表示されますので、生成したいプロジェクトの種類を指定します。
今回は Visual Studio 10 とします。VS8 や VS9 を利用している方はそれぞれ読み替えてください。

<div align="center"><a href="CMakeGUI1.png"><img src="CMakeGUI1.png" width="50%;"></a></div>
<div align="center"><strong>図20. 生成するプロジェクトの種類の指定</strong></div>

ダイアログで [Finish] をクリックすると Configure が始まります。問題がなければ下部のログウインドウに「Configuring done」と出力されますので、続けて [Generate] ボタンをクリックします。
「Generating done」と出ればプロジェクトファイル・ソリューションファイル等の出力が完了します。

なお、CMake は Configure の段階でキャッシュファイルを生成しますので、トラブルなどで設定を変更したり環境を変更した場合は [File] > [Delete Cache] でキャッシュを削除して Configure からやり直してください。

次に先ほど指定したbuild ディレクトリーの中の Flip.sln をダブルクリックして Visual Studio 2010 を起動します。

起動後、ソリューションエクスプローラーの「ALL_BUILD」を右クリックし「ビルド」を選択します。特に問題がなければ、正常にビルドが終了します。

<div align="center"><a href="VCbuild0.png"><img src="VCbuild0.png" width="50%;"></a></div>
<div align="center"><strong>図21. ビルド画面</strong></div>

### ヘッダ、ソースの編集

#### アクティビティ処理の実装

Flip コンポーネントでは、InPort から受け取った画像を画像保存用バッファに保存し、その保存した画像を OpenCV の cvFlip() 関数にて変換します。
その後、変換された画像を OutPort から送信します。

<br>
onActivated()、onExecute()、onDeactivated() での処理内容を図22に示します。
<br>

<div align="center"><a href="FlipRTC_State.png"><img src="FlipRTC_State.png" width="50%;"></a></div>
<div align="center"><strong>図22. アクティビティ処理の概要</strong></div>
<br>

onExecute() での処理を図23に示します。

<br>

<div align="center"><a href="FlipRTC.png"><img src="FlipRTC.png" width="50%;"></a></div>
<div align="center"><strong>図23. onExucete() での処理内容</strong></div>
<br>


#### ヘッダファイル (Flip.h) の編集

OpenCV のライブラリを使用するため、OpenCV のインクルードファイルをインクルードします。

```
 //OpenCV用インクルードファイルのインクルード
 #include<cv.h>
 #include<cxcore.h>
 #include<highgui.h>
```

この cvFlip コンポーネントでは、画像領域の確保、Flip 処理、確保した画像領域の解放のそれぞれの処理を行います。これらの処理は、それぞれ onActivated()、onDeactivated()、onExecute() のコールバック関数にて行います。

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
 
     // InPort の画像データを IplImageの imageData にコピー
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

このコンポーネントでは OpenCV を利用していますので、OpenCV のヘッダのインクルードパス、ライブラリーやライブラリサーチパスを与えてやる必要があります。幸い OpenCV は CMake に対応しており、以下の4行を追加するだけで OpenCV のライブラリーがリンクされ使えるようになります。


```
 # check doxygen installed
 find_package(Doxygen)
 if(DOXYGEN_FOUND STREQUAL "NO")
     message(FATAL_ERROR "Doxygen not found.")
 endif()
```

```
 # 以下の5行をCMakeList.txt に加える
 cmake_policy(SET CMP0015 NEW)
 find_package(OpenCV REQUIRED)
 list(APPEND INCLUDE_DIRS ${OpenCV_INCLUDE_DIRS})
 list(APPEND LIBRARY_DIRS ${OpenCV_LIB_DIR})
 list(APPEND LIBRARIES ${OpenCV_LIBS})
```

### VC++ によるビルド

#### ビルドの実行

CMakeList.txt を編集したので、再度 CMake GUI で ConfigureおよびGenerate を行います。
CMakeのGenerate が正常に終了した事を確認し、Flip.sln ファイルをダブルクリックし、Visual C++ 2010 を起動します。

Visual C++ 2010 の起動後、図24のようにし、コンポーネントのビルドを行います。

<br>

<div align="center"><a href="VC++_build.png"><img src="VC++_build.png" width="70%;"></a></div>
<div align="center"><strong>図24. ビルドの実行</strong></div>
<br>

### Flip コンポーネントの動作確認

ここでは、OpenRTM-aist-1.1 以降で同梱されるようになったカメラコンポーネント (OpenCVCameraComp、または DirectShowCamComp)とビューアコンポーネント (CameraViewerComp)を接続し動作確認を行います。

#### NameServiceの起動

コンポーネントの参照を登録するためのネームサービスを起動します。

<br>
[スタート] > [すべてのプログラム] > [OpenRTM-aist] > [C++] > [tools] を選択し、「Start Naming Service」をクリックしてください。

&color(RED){※ 「Star Naming Service」をクリックしても omniNames が起動しない場合は、フルコンピューター名が14文字以内に設定されているかを確認してください。

#### rtc.conf の作成

RTコンポーネントでは、ネームサーバーのアドレスやネームサーバーへの登録フォーマットなどの情報を rtc.conf というファイルで指定する必要があります。

下記の内容を rtc.conf というファイル名で保存し、Flip\FlipComp\Debug(もしくは、Release)フォルダーに置いてください。

<span style="color:RED;">※ Eclipse 起動時に workspace をデフォルトのままにしていた場合、Flip フォルダーのパスは、</span>;

<span style="color:RED;">   C:\Documents and Settings\<ログインユーザー名>\workspace　となります。</span>;

```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```

#### Flip コンポーネントの起動

Flip コンポーネントを起動します。

先程 rtc.conf ファイルを置いたフォルダーにある、FlipComp.exe ファイルを実行してください。
FlipComp.exe 画面が表示されます。

#### カメラコンポーネントとビューアコンポーネントの起動

USB カメラのキャプチャー画像を OutPort から出力する OpenCVCameraComp または DirectShowCamComp コンポーネントと、InPort で受け取った画像を画面に表示する CameraViewerComp を起動します。

これら２つのコンポーネントは、下記の手順にて起動できます。


[スタート] > [すべてのプログラム] > [OpenRTM-aist] > [components] > [C++] > [examples] > [opencv-rtcs] を選択し、「OpenCVCameraComp」と「CameraViewerComp」をそれぞれクリックして実行します。
「OpenCVCameraComp」と「CameraViewerComp」画面が表示されます。

OpenCVCameraComp ではうまくカメラを認識しない場合があります。その場合は DirectShowCamComp を使用してみてください。



### コンポーネントの接続

図25のように、RTSystemEditor にて USBCameraAqcuireComp、Flip、USBCameraMonitorComp コンポーネントを接続します。

<div align="center"><a href="RTSE_Connect.png"><img src="RTSE_Connect.png" width="70%;"></a></div>
<div align="center"><strong>図25. コンポーネントの接続</strong></div>



#### コンポーネントの Activate

RTSystemEditor の上部にあります「ALL」というアイコンをクリックし、全てのコンポーネントをアクティブ化します。正常にアクティベートされた場合、図26のように黄緑色でコンポーネントが表示されます。

<br>

<div align="center"><a href="RTSE_Activate.png"><img src="RTSE_Activate.png" width="70%;"></a></div>
<div align="center"><strong>図26. コンポーネントのアクティブ化</strong></div>
<br>

#### 動作確認

図27のようにコンフィギュレーションビューにてコンフィギュレーションを変更することができます。

Flip コンポーネントのコンフィギュレーションパラメーター「flipMode」を「0」や「-1」などに変更し、画像の反転が行われるかを確認してください。

<br>

<div align="center"><a href="RTSE_Configuration.png"><img src="RTSE_Configuration.png" width="70%;"></a></div>
<div align="center"><strong>図27. コンフィギュレーションパラメーターの変更</strong></div>
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
 
     // InPortの画像データを IplImage の imageData にコピー
     memcpy(m_imageBuff->imageData,(void *)&(m_originalImage.pixels[0]),m_originalImage.pixels.length());
 
     // InPort からの画像データを反転する。 m_flipMode 0: X軸周り, 1: Y軸周り, -1: 両方の軸周り
     cvFlip(m_imageBuff, m_flipImageBuff, m_flipMode);
 
     // 画像データのサイズ取得
     int len = m_flipImageBuff->nChannels * m_flipImageBuff->width * m_flipImageBuff->height;
     m_flippedImage.pixels.length(len);
 
     // 反転した画像データをOutPortにコピー
     memcpy((void *)&(m_flippedImage.pixels[0]),m_flipImageBuff->imageData,len);
 
     // 反転した画像データをOutPortから出力する。
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
 
 //OpenCV用インクルードファイルのインクルード
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


