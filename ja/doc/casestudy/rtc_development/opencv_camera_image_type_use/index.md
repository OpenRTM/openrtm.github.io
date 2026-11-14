---
layout: page
title: rtコンポーネント作成(opencv編 cameraimage型の使用)
---

<!-- Title: RTコンポーネント作成(OpenCV編 CameraImage型の使用) -->
#contents

# はじめに
ここでは、OpenCV ライブラリを VC９ にて RTコンポーネント化する手順を紹介します。

## OpenCV とは

[OpenCV](http://opencv.jp/) とはインテルが開発・公開しているオープンソースのコンピュータービジョン向けライブラリです。

[Wikipedia](http://ja.wikipedia.org/wiki/OpenCV) より抜粋。

## 作成する RTコンポーネント

- Flip コンポーネント: OpenCV ライブラリのうち、cvFlip() 関数を用いて画像の反転を行う RTコンポーネント。

# OpenCV ライブリの RTコンポーネント化 (Flipコンポーネント)

ここでは、OpenCV ライブラリのうち、画像の反転を行う cvFlip() を VC９ にて RTコンポーネント化します。

以下は、作業の流れです。

- cvFlip 関数について
- コンポーネントの概要
- 動作環境・開発環境
- Flip コンポーネントの雛型の生成
- アクティビティ処理の実装
- コンポーネントの動作確認

## cvFlip 関数について

cvFlip 関数は、2次元配列を垂直、水平、または両軸で反転します。

```
 void cvFlip(IplImage* src, IplImage* dst=NULL, int flip_mode=0);
 #define cvMirror cvFlip
  
 src       入力配列
 dst       出力配列。もし dst = NULL であれば、src が上書きされます。
 flip_mode 配列の反転方法の指定内容:
 　flip_mode = 0: X軸周りでの反転(上下反転)
 　flip_mode > 0: Y軸周りでの反転(左右反転)
 　flip_mode < 0: 両軸周りでの反転(上下左右反転)
```

## コンポーネントの概要

InPort からの入力画像を反転し OutPort から出力するコンポーネント。

<br>
反転の対象軸は、RTC のコンフィギュレーション機能を使用して flipMode という名前のパラメーターで指定します。

flipMode は、反転したい方向に応じて下記のように指定してください。

- 上下反転したい場合、0

- 左右反転したい場合、1

- 上下左右反転したい場合、-1

<br>

作成する RTC の仕様は以下のとおりです。

- InPort
  - キャプチャーされた画像データ (CameraImage)

- OutPort
  - 反転した画像データ (CameraImage)

- Configuration
  - 反転方法の指定 (int)

※ CameraImage型は、OpenRTM-aist の InterfaceDataTypes.idl にて下記のように定義されているデータ型です。

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


<br>
図1は、それぞれの flipMode での画像処理のイメージ図です。

<br>

<div align="center"><a href="cvFlip_and_FlipRTC.png"><img src="cvFlip_and_FlipRTC.png" width="70%;"></a></div>
<div align="center"><strong>図1. Flip コンポーネントの flipMode の指定パターン</strong></div>
<br>

## 動作環境・開発環境
- OS: Windows XP SP3
- コンパイラ: [Visual C++ 2008 Express Edition 日本語版](http://www.microsoft.com/japan/msdn/vstudio/express/default.aspx)

- [OpenCV2.1(VC2008用)](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.1/OpenCV-2.1.0-win32-vs2008.exe/download)
- [OpenRTM-aist-1.0.0-RELEASE(C++版), Win32 VC2008](http://www.openrtm.org/pub/Windows/OpenRTM-aist/cxx/OpenRTM-aist-1.0.0-RELEASE_vc9_100212.msi)

- [OpenCV用RTC群(Win32用インストーラ)](http://www.openrtm.org/pub/OpenRTM-aist/components/OpenCV/OpenCV-RTC-0.0.1.msi)
- [OpenCV用RTC群(ソースコード)](http://www.openrtm.org/pub/OpenRTM-aist/components/OpenCV/OpenCV_RTC_0.0.1.tar.gz)

- RTSystemEditor 1.0
- RTCBuilder 1.0
  - [Eclipse3.4.2+RTSE(1.0.0-RELEASE)+RTCB(1.0.0-RELEASE)Windows用全部入り]()（リンク切れです）

- [解凍ツール(Lhaplus)](http://www.forest.impress.co.jp/lib/arc/archive/archiver/lhaplus.html)

## Flip コンポーネントの雛型の生成

Flip コンポーネントの雛型の生成は、RTCBuilder を用いて行います。

### RTCBuilder の起動

新規ワークスペースを指定して Eclipse を起動すると、以下のような「ようこそ」画面が表示されます。
<br>

<div align="center"><a href="fig1-1EclipseInit.png"><img src="fig1-1EclipseInit.png" width="70%;"></a></div>
<!-- CENTER:''図 1-1 Eclipseの初期起動時の画面'' -->
<div align="center"><strong>図2. Eclipseの初期起動時の画面</strong></div>
<br>
この「ようこそ」画面左上の「X」をクリックして画面を閉じると、以下の画面が表示されます。
右上の [Open Perspective] ボタンをクリックし、プルダウンの「Other…」を選択します。
<br>

<div align="center"><a href="fig2-2PerspectiveSwitch.png"><img src="fig2-2PerspectiveSwitch.png" width="70%;"></a></div>
<!-- CENTER:''図 2-2 パースペクティブの切り替え'' -->
<div align="center"><strong>図3. パースペクティブの切り替え</strong></div>
<br>
「RTC Builder」を選択し、[OK] ボタンをクリックします。
<br>

<div align="center"><a href="fig2-3PerspectiveSelection.png"><img src="fig2-3PerspectiveSelection.png" width="50%;"></a></div>
<!-- CENTER:''図 2-3　パースペクティブの選択'' -->
<div align="center"><strong>図4. パースペクティブの選択</strong></div>
<br>
RTCBuilder が起動します。
<br>

<div align="center"><a href="NewRTCBEditor.png"><img src="NewRTCBEditor.png" width="70%;"></a></div>
<!-- CENTER:''図 2-4 RTC Builderの初期起動時画面'' -->
<div align="center"><strong>図5. RTC Builderの初期起動時画面</strong></div>
<br>

### RTCBuilder用 プロジェクトの作成
まず最初に，RT コンポーネントを作成するための Eclipse プロジェクトを作成します。
画面上部のメニューから [ファイル] > [新規] > [プロジェクト] を選択します。
<br>

<div align="center"><a href="fig2-5CreateProject.png"><img src="fig2-5CreateProject.png" width="70%;"></a></div>
<!-- CENTER:''図 2-5 RTC Builder 用プロジェクトの作成　１'' -->
<div align="center"><strong>図6. RTC Builder 用プロジェクトの作成　１</strong></div>
<br>
表示された｢新規プロジェクト｣画面において、[その他] > [RTC ビルダ] を選択し、[次へ] をクリックします。
<br>

<div align="center"><a href="fig2-6CreateProject2.png"><img src="fig2-6CreateProject2.png" width="50%;"></a></div>
<!-- CENTER:''図 2-6 RTC Builder 用プロジェクトの作成　２'' -->
<div align="center"><strong>図7. RTC Builder 用プロジェクトの作成　２</strong></div>
<br>
｢プロジェクト名｣欄に作成するプロジェクト名を入力して [完了] をクリックします。
<br>

<div align="center"><a href="RT-Component-BuilderProject.png"><img src="RT-Component-BuilderProject.png" width="50%;"></a></div>
<!-- CENTER:''図 2-7 RTC Builder 用プロジェクトの作成　３'' -->
<div align="center"><strong>図8. RTC Builder 用プロジェクトの作成　３</strong></div>
<br>
指定した名称のプロジェクトが生成され、パッケージエクスプローラー内に追加されます。
<br>

<div align="center"><a href="PackageExplolrer.png"><img src="PackageExplolrer.png" width="50%;"></a></div>
<!-- CENTER:''図 2-8 RTC Builder 用プロジェクトの作成　４'' -->
<div align="center"><strong>図9. RTC Builder 用プロジェクトの作成　４</strong></div>
<br>
生成したプロジェクト内には、デフォルト値が設定された RTC プロファイル XML(RTC.xml) が自動的に生成されます。

### RTC プロファイルエディタの起動
RTC プロファイルエディタを開くには、ツールバーの｢ [Open New RtcBuilder Editor] ボタンをクリックするか、メニューから [ファイル] > [Open New Builder Editor] を選択します。
<br>

<div align="center"><a href="Open_RTCBuilder.png"><img src="Open_RTCBuilder.png" width="50%;"></a></div>
<!-- CENTER:''図 2-9 ツールバーから Open New RtcBuilder Editor'' -->
<div align="center"><strong>図10. ツールバーから Open New RtcBuilder Editor</strong></div>
<br>
<br>

<div align="center"><a href="fig2-10FileMenuOpenNewBuilder.png"><img src="fig2-10FileMenuOpenNewBuilder.png" width="30%;"></a></div>
<!-- CENTER:''図 2-10 File メニューから Open New Builder Editor'' -->
<div align="center"><strong>図11. File メニューから Open New Builder Editor</strong></div>
<br>

### コンポーネントのプロファイル情報入力とコードの生成

1. 「基本」タブを選択し、基本情報を入力します。

<br>
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
- 実行周期: 0.0 (<span style="color:RED;">図13では1.0となってますが,0.0として下さい.</span>;)
<br>
- Output Project: Flip


<br>

<div align="center"><a href="Basic.png"><img src="Basic.png" width="70%;"></a></div>
<div align="center"><strong>図13. 基本情報の入力</strong></div>
<br>

2. 「アクティビティ」タブを選択し、使用するアクションコールバックを指定します。

Flip コンポーネントでは、onActivated()、onDeactivated()、onExecute()コ ールバックを使用します。
図14のように①の onAtivated をクリック後に ②のラジオボタンの [ON] にチェックを入れます。onDeactivated、onExecute についても同様の操作を行います。

<br>

<div align="center"><a href="Activity.png"><img src="Activity.png" width="70%;"></a></div>
<div align="center"><strong>図14. アクティビティコールバックの選択</strong></div>
<br>

3. 「データポート」タブを選択し、データポートの情報を入力します。

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

4.　「コンフィギュレーション」タブを選択し、Configuration の情報を入力します。

ラジオボタンでコンフィギュレーションの変更を行います。

<br>
- flipMode
  - 名称: flipMode
  - データ型: int
  - デフォルト値: 1
  - 変数名: flipMode
  - 制約条件: (-1, 0, 1) <span style="color:RED;">※ (-1: 上下左右反転, 0: 上下反転, 1: 左右反転)</span>;
  - Widget: radio

<br>

<div align="center"><a href="Configuration.png"><img src="Configuration.png" width="70%;"></a></div>
<div align="center"><strong>図16. コンフィグレーション情報の入力</strong></div>
<br>

5.　「言語・環境」タブを選択し、プログラミング言語を選択します。

今回は、C++(言語)を選択します。

<br>

<div align="center"><a href="Language.png"><img src="Language.png" width="70%;"></a></div>
<div align="center"><strong>図17. プログラミング言語の選択</strong></div>
<br>

6.　「基本」タブにある [コード生成] ボタンをクリックし、コンポーネントの雛型を生成します。

<br>

<div align="center"><a href="Generate.png"><img src="Generate.png" width="70%;"></a></div>
<div align="center"><strong>図18. 雛型の生成(Generate)</strong></div>
<br>

<span style="color:Red;">※ 生成されるコード群は、Eclipse 起動時に指定したワークスペースフォルダーの中に生成されます。現在のワークスペースは、[ファイル] > [ワークスペースの切り替え] で確認することができます。</span>;

## アクティビティ処理の実装

Flip コンポーネントでは、InPort から受け取った画像を画像保存用バッファに保存し、その保存した画像を OpenCV の cvFlip() 関数にて変換します。その後、変換された画像を OutPort から送信します。
<br>

<br>
onActivated()、onExecute()、onDeactivated() での処理内容を図19に示します。
<br>

<div align="center"><a href="FlipRTC_State.png"><img src="FlipRTC_State.png" width="50%;"></a></div>
<div align="center"><strong>図19. アクティビティ処理の概要</strong></div>
<br>

onExecute() での処理を図20に示します。

<br>

<div align="center"><a href="FlipRTC.png"><img src="FlipRTC.png" width="50%;"></a></div>
<div align="center"><strong>図20. onExucete()での処理内容</strong></div>
<br>


### OpenCV用 ユーザープロパティシートのコピー
プロパティシートとは、コンパイルに必要な種々のオプション（インクルードパス、ライブラリロードバス、ライブラリ）やマクロを記述した VC の設定ファイルの一種です。
RTCBuilder や rtc-template で生成した VC用のプロジェクトでは、VC のプロパティシートを使用して各種オプションを与えています。また、ユーザーが追加でオプションを追加できるように、ユーザー定義のプロパティシートもインクルードするようになっています。
- rtm_config.vsprop：OpenRTM に関する情報を含むプロパティシート。インストールされている OpenRTM-aist に依存するファイルであるため、copyprops.bat を使用して OpenRTM のシステムディレクトリーからカレントのプロジェクトへコピーします。
- user_config.vsprops：ユーザー定義のプロパティシート。デフォルトは空です。使い方は、ソースコード：OpenRTM-aist/win32/OpenRTM-aist/example/USBCamera の中に入っているuser_config.vsprops (OpenCV用の設定)を参考にしてください。

以下の内容を user_config.vsprops というファイル名で保存し、Flip フォルダーにコピーしてください。

もしくは、下記より vsprops ファイルをダウンロードし、Flip フォルダーに保存してください。

<br>
[user_config.vsprops]()（リンク切れです）

※　既に Flip フォルダーには user_config.vsprops ファイルが存在していますが、上書きして構いません。

<br>
```
 <?xml version="1.0" encoding="shift_jis"?>
 <VisualStudioPropertySheet
 	ProjectType="Visual C++"
 	Version="8.00"
 	Name="OpenCV21"
 	>
 	<Tool
 		Name="VCCLCompilerTool"
 		AdditionalIncludeDirectories="$(cv_includes)"
 	/>
 	<Tool
 		Name="VCLinkerTool"
 		AdditionalLibraryDirectories="$(cv_libdir)"
 	/>
 	<UserMacro
 		Name="user_lib"
 		Value="$(cv_lib)"
 	/>
 	<UserMacro
 		Name="user_libd"
 		Value="$(cv_libd)"
 	/>
 	<UserMacro
 		Name="cv_root"
 		Value="C:\OpenCV2.1"
 	/>
 	<UserMacro
 		Name="cv_includes"
 		Value="&quot;$(cv_root)\include\opencv&quot;"
 	/>
 	<UserMacro
 		Name="cv_libdir"
 		Value="&quot;$(cv_root)\lib&quot;"
 	/>
 	<UserMacro
 		Name="cv_bin"
 		Value="$(cv_root)\bin"
 	/>
 	<UserMacro
 		Name="cv_lib"
 		Value="cv210.lib cvaux210.lib highgui210.lib cxcore210.lib"
 	/>
 	<UserMacro
 		Name="cv_libd"
 		Value="cv210d.lib cvaux210d.lib highgui210d.lib cxcore210d.lib"
 	/>
 </VisualStudioPropertySheet>
```

### copyprops.bat の実行

copyprops.batというファイルを実行することで、rtm_config.vspropsというファイルがコピーされます。

rtm_config.vspropsファイルは、RTコンポーネントをVC++でビルドするために必要なインクルードパスやリンクするライブラリ等が記述されたファイルです。

### ヘッダファイルの編集

- OpenCV のライブラリを使用するため、OpenCV のインクルードファイルをインクルードします。

```
 //OpenCV 用インクルードファイルのインクルード
 #include<cv.h>
 #include<cxcore.h>
 #include<highgui.h>
```

- この cvFlip コンポーネントでは、画像領域の確保、Flip 処理、確保した画像領域の解放のそれぞれの処理を行います。これらの処理は、それぞれ onActivated()、onDeactivated()、onExecute() のコールバック関数にて行います。

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

- 反転した画像の保存用にメンバー変数を追加します。

```
   IplImage* m_imageBuff;
   IplImage* m_flipImageBuff;
```

### ソースファイルの編集

下記のように、onActivated()、onDeactivated()、onExecute() を実装します。

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

### ビルドの実行

Flip_vc9.sln ファイルをダブルクリックし、Visual C++ 2008 を起動します。

Visual C++ 2008 の起動後、図21のようにし、コンポーネントのビルドを行います。

<br>

<div align="center"><a href="VC++_build.png"><img src="VC++_build.png" width="70%;"></a></div>
<div align="center"><strong>図21. ビルドの実行</strong></div>
<br>

## Flip コンポーネントの動作確認

ここでは、「OpenCV用RTC群 (Win32用インストーラ)」にてインストールした USBCameraAqcuireComp コンポーネントと、USBCameraMonitorCom コンポーネント、それと、今回作成した Flip コンポーネントを接続し動作確認を行います。

### NameService の起動

omniORB のネームサービスを起動します。

<br>
[スタート] > [すべてのプログラム] > [OpenRTM-aist] > [C++] > [tools] の順に辿り、「Start Naming Service」をクリックしてください。

&color(RED){※ 「Star Naming Service」をクリックしても omniNames が起動されない場合は、フルコンピューター名が14文字以内に設定されているかを確認してください。

### rtc.confの作成

RTコンポーネントでは、ネームサーバーのアドレスやネームサーバーへの登録フォーマットなどの情報を rtc.conf というファイルで指定する必要があります。

下記の内容を rtc.conf というファイル名で保存し、Flip\FlipComp\Debug(もしくは、Release)フォルダーに置いて下さい。

<span style="color:RED;">※ Eclipse 起動時に workspace をデフォルトのままにしていた場合、Flip フォルダーのパスは、</span>;

<span style="color:RED;">   C:\Documents and Settings\<ログインユーザー名>\workspace　となります。</span>;

```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```

### Flip コンポーネントの起動

Flip コンポーネントを起動します。

先程 rtc.conf ファイルを置いたフォルダーにある、FlipComp.exe ファイルを実行して下さい。

### USBCameraAqcuire、USBCameraMonitor コンポーネントの起動

USB カメラのキャプチャ画像を OutPort から出力する USBCameraAqcuireComp コンポーネントと、InPort で受け取った画像を画面に表示する USBCameraMonitorComp コンポーネントを起動します。

これら２つのコンポーネントは、下記の手順にて起動できます。


[スタート] > [すべてのプログラム] > [OpenRTM-aist] > [components] > [C++] > [OpenCV] を選択し、「USBCameraAqcuireComp」と「USBCameraMonitorComp」をそれぞれクリックして実行します。

### コンポーネントの接続

図22のように、RTSystemEditor にて USBCameraAqcuireComp、Flip、USBCameraMonitorComp コンポーネントを接続します。

<br>

<div align="center"><a href="RTSE_Connect.png"><img src="RTSE_Connect.png" width="70%;"></a></div>
<div align="center"><strong>図22. コンポーネントの接続</strong></div>
<br>

### コンポーネントの Activate

RTSystemEditor の上部にあります「ALL」というアイコンをクリックし、全てのコンポーネントをアクティベートします。

正常にアクティベートされた場合、図23のように黄緑色でコンポーネントが表示されます。

<br>

<div align="center"><a href="RTSE_Activate.png"><img src="RTSE_Activate.png" width="70%;"></a></div>
<div align="center"><strong>図23. コンポーネントのアクティベート</strong></div>
<br>

### 動作確認

図24のようにコンフィギュレーションビューにてコンフィギュレーションを変更することができます。

Flip コンポーネントのコンフィギュレーションパラメーター「flipMode」を「0」や「-1」などに変更し、画像の反転が行われるかを確認してください。

<br>

<div align="center"><a href="RTSE_Configuration.png"><img src="RTSE_Configuration.png" width="70%;"></a></div>
<div align="center"><strong>図24. コンフィギュレーションパラメーターの変更</strong></div>
<br>

## Flip コンポーネントのソースファイル

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
 
     // InPort の画像データを IplImage の imageData にコピー
     memcpy(m_imageBuff->imageData,(void *)&(m_originalImage.pixels[0]),m_originalImage.pixels.length());
 
     // InPort からの画像データを反転する。 m_flipMode 0: X軸周り, 1: Y軸周り, -1: 両方の軸周り
     cvFlip(m_imageBuff, m_flipImageBuff, m_flipMode);
 
     // 画像データのサイズ取得
     int len = m_flipImageBuff->nChannels * m_flipImageBuff->width * m_flipImageBuff->height;
     m_flippedImage.pixels.length(len);
 
     // 反転した画像データを OutPortにコピー
     memcpy((void *)&(m_flippedImage.pixels[0]),m_flipImageBuff->imageData,len);
 
     // 反転した画像データを OutPortから出力する。
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

## Flip コンポーネントのヘッダファイル

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

## Flip コンポーネントのビルド済みパッケージ

ビルド済みパッケージを下記からダウンロードできます。

拡張子を"zip_"としてますので、"zip"にリネームしてから解凍してください。


- [ビルド済みパッケージ]()（リンク切れです）


