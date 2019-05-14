このページは首都大学東京大学院のユビキタスロボティクス特論(2019年5月15日)で行うOpenRTM-aist 1.2.0のインストール、Flipコンポーネント作成の手順を記したページです。
本来は[openrtm.org](https://openrtm.org/openrtm/)のページに記載してあるのですが、授業当日にopenrtm.orgを閉じるらしいので臨時ページを作成しました。

既にRTミドルウェアについては説明済みだと聞いていますが、分からない点は以下の用語集を参考にしてください。

- [用語集](https://nobu19800.github.io/RTM-Lua/docs/glossary.html)

## OpenRTM-aist 1.2.1のインストール
### Windowsの場合
以下のソフトウェアをインストールしてください。

* [Visual Studio 2017(2008、2012、2013、2015、2019でも可)](vs_install.md)
  * **Visual C++がインストールされているかは必ず確認してください。**
* [Python 2.7](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi)
  * Python 3.6、3.7がインストールされている場合はそのままで問題ありません
* [CMake](https://github.com/Kitware/CMake/releases/download/v3.14.1/cmake-3.14.1-win64-x64.msi)
* [Doxygen](http://doxygen.nl/files/doxygen-1.8.14-setup.exe)
* [OpenRTM-aist-1.2.1-RC1](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86_64.msi)

**OpenRTM-aist 1.1.2以前をインストールしている場合**
OpenRTM-aist 1.1.2以前をインストールしている場合はアンインストールしてください。

**Visual Studioをインストールすることが困難な場合について**

Visual Studioは大量のファイルをダウンロードする必要があるため環境によってはダウンロードに数時間かかる可能性があります。


### Ubuntuの場合

* g++

```shell
$ sudo apt-get install gcc g++
```
* omniORB

```shell
$ sudo apt-get install libomniorb4-dev omniidl omniorb-nameserver
$ sudo apt-get install python-omniorb-omg omniidl-python
```
* CMake

```shell
$ sudo apt-get install cmake
```
* Doxygen

```shell
$ sudo apt-get install doxygen
```

* JDK

```shell
# Ubuntu 18.04、18.10の場合
$ sudo apt-get install openjdk-8-jdk
# Ubuntu 16.04の場合
$ sudo apt-get install default-jdk
```

Ubuntu 18.04、18.10の場合は以下のコマンドでjava8に切り替えます。

```shell
$ sudo update-alternatives --config java
```

* OpenRTM-aist

```shell
ubuntu 18.04 (64bit) の場合

C++版のインストール
wget https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz
tar xf OpenRTM-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz
cd OpenRTM-aist_1.2.0_ubuntu18.04_amd64_package
sudo sh install-openrtm-deb-packages.sh
cd ..

Python版のインストール
wget https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python_1.2.0_ubuntu18.04_amd64_package.tar.gz
tar xf OpenRTM-aist-Python_1.2.0_ubuntu18.04_amd64_package.tar.gz
cd OpenRTM-aist-Python_1.2.0_ubuntu18.04_amd64_package
sudo sh install-openrtm-deb-packages.sh
cd ..


RTSystemEditor/RTCBuilderのインストール
wget https://github.com/OpenRTM/OpenRTP-aist/releases/download/v1.2.0/OpenRTP-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz
tar xf OpenRTP-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz
cd OpenRTP-aist_1.2.0_ubuntu18.04_amd64_package
sudo sh install-openrtm-deb-packages.sh
cd ..
```

## Flipコンポーネント作成手順
以下のようにInPortで受信した画像を左右上下に反転させてOutPortから出力するRTコンポーネント(RTC)を作成します。

![image](https://user-images.githubusercontent.com/6216077/57673335-7f81f880-7656-11e9-8be9-283cf3b0b314.png)

作成手順は以下のようになっています。

1. RTCの仕様を決める
2. RTC BuilderでRTCのひな形コードを生成する
3. 内部の処理を実装する
4. RT System EditorでRTシステムを作成、動作確認をする

### RTCの仕様を決める
RTCのモジュール名等の基本的な情報、RTCにどのようなデータポート、サービスポート、コンフィギュレーションパラメータなどが使えるのか等の仕様をまず決める必要があります。
今回は以下のような仕様に設定します。

RTCは状態遷移を行い、状態によりonActivated、onDeactivated、onExecute等のコールバック関数を呼び出します。
これらのコールバック関数で画像反転処理、リソースの解放処理などを実行します。RTCの主たる機能を実行する部分をアクティビティと言います。

今回は以下のコールバック関数を有効にします。

|関数名|意味|
|onActivated|RTCがアクティブ状態に遷移したときに呼び出されるコールバック関数。初期化などを実行する。|
|onDeactivated|RTCが非アクティブ状態に遷移したときに呼び出されるコールバック関数。終了処理などを実行する。|
|onExecute|RTCがアクティブ状態の時に周期的に呼び出されるコールバック関数。メインの処理を実行する。|


FlipコンポーネントはInPortで他のRTCから受信した画像データをOutPortから出力するRTCのため、まずInPortとOutPortが必要です。
また画像を反転させる方向の設定をコンフィギュレーションパラメータで設定できるようにします。

|||
|---|---|
|モジュール名|Flip|
|アクティビティ|onActivated、onDeactivated、onExecute|
|InPort|1個(originalImage)|
|OutPort|1個(flippedImage)|
|コンフィギュレーションパラメータ|1個(flipMode)|

以下はoriginalImageというInPortの仕様です。
originalImageは他のRTCから画像データを受信するポートに該当します。

|||
|---|---|
|ポート名|originalImage|
|型|RTC::CameraImage|

以下はflippedImageというOutPortの仕様です。
originalImageで受信した画像データを反転した画像を送信します。

|||
|---|---|
|ポート名|flippedImage|
|型|RTC::CameraImage|

以下はflipModeというコンフィギュレーションパラメータの仕様です。
コンフィギュレーションパラメータはRT System Editor等のツールから実行中のRTCのパラメータを操作するための機能です。

|||
|---|---|
|パラメーター名|flipMode|
|型|int|
|デフォルト値|0|
|制約|(0, -1, 1)|
|Widget|radio|

このコンフィギュレーションパラメータで画像反転パターンを設定します。

- 上下反転：flipMode=0
- 左右反転：flipMode=1
- 上下左右反転：flipMode=-1



### RTC BuilderでRTCのひな形コードを生成する
RTC BuilderはRTCのひな形コードを生成するためのGUIツールです。
先ほど決めた仕様をRTC Builderに入力すると、C++、Python、Java、Luaのコードを生成できます。

#### OpenRTPの起動
OpenRTPはRTC Builder、RT System Editorのツールを含む開発環境です。

Windowsの場合は、デスクトップのショートカットをダブルクリックしてください。

![image](https://user-images.githubusercontent.com/6216077/57674509-6aa76400-765a-11e9-9860-242adec2f17b.png)

もしくはWindows 10の場合は右下の「ここに入力して検索」にOpenRTPと入力して起動してください。

![image](https://user-images.githubusercontent.com/6216077/57674587-a5a99780-765a-11e9-8fd5-44083b66c5ca.png)

Ubuntuの場合は以下のコマンドを入力します。

```
openrtp
```

最初にワークスペースの指定が必要なため、適当な場所を指定して起動ボタンを押してください。

![image](https://user-images.githubusercontent.com/6216077/57674964-9ecf5480-765b-11e9-911a-b4468504bec1.png)



**OpenRTPが起動しない場合**

OpenRTPが起動、終了を繰り返したり、何らかのエラーメッセージを出す場合があります。
起動終了を繰り返す場合はOSを再起動しないと解決しない場合もあります。

問題が発生した場合は以下のフォルダを削除してからOpenRTPを起動してください。(ユーザー名は適宜変更してください)

```
C:\Users\{ユーザー名}\.eclipse
```


#### RTC Builderの起動
OpenRTPを最初に起動したときにWelcomeページが開きますが、不要のため×ボタンで閉じてください。

![image](https://user-images.githubusercontent.com/6216077/57675139-07b6cc80-765c-11e9-8325-7dd0e52cf498.png)

右上のパースペクティブを開くボタンを押してください。

![image](https://user-images.githubusercontent.com/6216077/57675174-22894100-765c-11e9-8bc8-aa05744401a8.png)

RTC Builderを選択して起動してください。

![image](https://user-images.githubusercontent.com/6216077/57675202-36cd3e00-765c-11e9-882d-89990c0419c8.png)

#### プロジェクト作成
RTC Buiderのプロジェクトを生成します。
以下のRTと書かれたアイコンをクリックしてください。

![image](https://user-images.githubusercontent.com/6216077/57675246-5bc1b100-765c-11e9-99fd-710631b03224.png)

今回はプロジェクト名にFlipと入力してプロジェクトを作成します。

![image](https://user-images.githubusercontent.com/6216077/57675395-d7236280-765c-11e9-905d-164118cf4ac1.png)

#### 仕様の入力
Flipコンポーネントの仕様を入力していきます。

##### 基本情報の設定
**基本**タブを選択して**モジュール名**に**Flip**と入力してください。

![image](https://user-images.githubusercontent.com/6216077/57675490-25386600-765d-11e9-91e2-0fc67c86426c.png)

##### アクティビティの設定
仕様通りにonActivated、onDeactivated、onExecuteを有効にします。
有効にするためには、**アクティビティ**タブからonActivate等の名前をクリックしてON・OFFを切り替えます。

![image](https://user-images.githubusercontent.com/6216077/57677474-db05b380-7661-11e9-8b95-5b31f8083042.png)

同じ手順でonDeactivated、onExecuteをONに切り替えます。

![image](https://user-images.githubusercontent.com/6216077/57677532-025c8080-7662-11e9-9968-554abe2c9de8.png)


##### データポートの設定
データポートのタブを選択して、InPort、OutPortを追加します。
InPort、OutPortの追加はAddボタンを押します。

![image](https://user-images.githubusercontent.com/6216077/57675639-7a747780-765d-11e9-87fe-133944eab0f6.png)

ポートの名前はポート名をクリックすることで変更できます。

![image](https://user-images.githubusercontent.com/6216077/57675668-8fe9a180-765d-11e9-9754-a4bc77969619.png)

InPortを仕様通りにポート名、データ型を設定します。


![image](https://user-images.githubusercontent.com/6216077/57677652-494a7600-7662-11e9-98a2-be57e5b0447a.png)

このとき必ず**RTC::CameraImage**を設定してください。Img::CameraImage、Img::TimedCameraImageと間違えないようにしてください。


OutPortを仕様通りにポート名、データ型を設定します。


![image](https://user-images.githubusercontent.com/6216077/57677794-a6dec280-7662-11e9-97f3-58024eac1736.png)


##### コンフィギュレーションパラメータ
コンフィギュレーションタブを選択して、コンフィギュレーションパラメータを追加します。

![image](https://user-images.githubusercontent.com/6216077/57677937-fd4c0100-7662-11e9-8d1b-e17487ca494b.png)


仕様通りに入力します。


![image](https://user-images.githubusercontent.com/6216077/57678980-41d89c00-7665-11e9-8c9c-8e62712841fc.png)

##### 言語
**言語・環境**タブから言語をC++に設定します。

![image](https://user-images.githubusercontent.com/6216077/57679499-713bd880-7666-11e9-9fe2-ff47ae71ef0b.png)


#### コード生成
**基本**タブに戻って**コード生成**ボタンを押します。

![image](https://user-images.githubusercontent.com/6216077/57679576-9b8d9600-7666-11e9-9b01-dddeca4fe1ef.png)


これでCPPファイル、ヘッダーファイルなどのソースコード、CMake設定ファイルなどが生成できます。

パッケージエクスプローラのFlipを右クリックして、**表示方法->システムエクスプローラー**で確認できます。

![image](https://user-images.githubusercontent.com/6216077/57679641-cd9ef800-7666-11e9-9f81-f52bf9706b33.png)

### 内部の処理を実装する
RTCの内部で画像を反転させる処理を実装してRTCの実行ファイルを作成します。

#### CMake設定ファイルの編集
画像処理にはOpenCVというライブラリを使用します。
RTCのビルドにはCMakeというビルドシステムを使用しており、使用するライブラリの設定などはCMakeLists.txtという設定ファイルに記述する必要があります。
OpenCVのライブラリとリンクするためには、コードを生成したフォルダ(Flip)の**src/CMakeLists.txt**を以下のように編集します。

```CMake
set(comp_srcs Flip.cpp )
set(standalone_srcs FlipComp.cpp)

find_package(OpenCV REQUIRED) #追加

if(${OPENRTM_VERSION_MAJOR} LESS 2)
```

```CMake
add_dependencies(${PROJECT_NAME} ALL_IDL_TGT)
target_link_libraries(${PROJECT_NAME} ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) #${OpenCV_LIBS}を追加

add_executable(${PROJECT_NAME}Comp ${standalone_srcs}
  ${comp_srcs} ${comp_headers} ${ALL_IDL_SRCS})
add_dependencies(${PROJECT_NAME}Comp ALL_IDL_TGT)
target_link_libraries(${PROJECT_NAME}Comp ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) #${OpenCV_LIBS}を追加
```

#### Visual Studioのプロジェクト生成(Ubuntuの場合はMakefile)
CMake設定ファイルからVisual Studioのプロジェクト、Makefile等を作成できます。
まずはcmake-guiを起動してください。Windows 10の場合は左下の「ここに入力して検索」にCMakeと入力してCMake(cmake-gui)を起動してください。

![image](https://user-images.githubusercontent.com/6216077/57680534-cd9ff780-7668-11e9-946d-2f01153c077f.png)

cmake-guiにFlip直下のCMakeLists.txtをドラッグアンドドロップしてください。
これでcmake-guiの「Where is the source code」にFlipのディレクトリが設定されます。

![image](https://user-images.githubusercontent.com/6216077/57680778-5d45a600-7669-11e9-9bd8-e251d6f0715a.png)

「Where to build the binaries」にはFlip以下のbuildフォルダを指定してください。

![image](https://user-images.githubusercontent.com/6216077/57680963-bc0b1f80-7669-11e9-940f-725729015f67.png)

次に**Configure**ボタンを押します。
この時、Flipコンポーネントのビルドに必要なライブラリの検出等を行います。

![image](https://user-images.githubusercontent.com/6216077/57681012-ce855900-7669-11e9-8397-b0eeb5bba90e.png)

コンパイラの種類を設定します。
おそらくOpenRTM-aistの64bit版をインストールしているはずのため、「Optional Platform for genarator」には**x64**を設定してください。

![image](https://user-images.githubusercontent.com/6216077/57681153-20c67a00-766a-11e9-8612-802cac532301.png)

※cmake-guiのバージョンが古い場合は操作画面の構成が違っています。古いバージョンの場合は「Visual Stuidio 15 2017 Win64」等を設定してください。

その後、Finishボタンを押すとConfigureを開始します。成功すると「Configuring done」と表示されます。

ここで失敗する場合はVisual StudioのC++コンパイラがインストールされていない可能性があります。

次に**Genarate**をクリックします。
これでVisual Studioのプロジェクトファイルを生成できました。

**Open Project**ボタンを押してVisual Studioのソリューションファイルを開いてください。

Ubuntuの場合は以下のコマンドでMakefileを生成できます。

```
mkdir build
cmake ..
```

#### ソースコードの編集
Visual Studioのソリューションエクスプローラから**Flip.h**、**Flip.cpp**を開いて編集します。

![image](https://user-images.githubusercontent.com/6216077/57681946-b31b4d80-766b-11e9-9276-bb23336d83c7.png)

##### Flip.hの編集
Flip.hの編集を行います。

以下のようにOpenCVのヘッダーファイルをインクルードします。

```CPP
#include <rtm/idl/ExtendedDataTypesSkel.h>
#include <rtm/idl/InterfaceDataTypesSkel.h>
//OpenCV用インクルードファイルのインクルード
#include <opencv2/opencv.hpp> //追加

// Service implementation headers
```

反転した画像の保存するメンバー変数を追加します。

```CPP
 private:
     // <rtc-template block="private_attribute">
  
     // </rtc-template>
 
     // <rtc-template block="private_operation">
  
     // </rtc-template>
         cv::Mat m_imageBuff; //追加
         cv::Mat m_flipImageBuff; //追加
```


##### Flip.cppの編集
Flip.cppの編集を行います。
下記のように、onActivated()、onDeactivated()、onExecute() を実装します。

```CPP
 RTC::ReturnCode_t Flip::onActivated(RTC::UniqueId ec_id)
 {
 
        // OutPortの画面サイズの初期化
        m_flippedImage.width = 0;
        m_flippedImage.height = 0;
 
        return RTC::RTC_OK;
 }
```

```CPP
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

```CPP
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

画像反転処理はonExecute関数に実装しており、以下のように動作します。

![image](https://user-images.githubusercontent.com/6216077/57682301-7dc32f80-766c-11e9-9073-718d2da96fb5.png)


#### ビルド
Visual Studioの「ビルド->ソリューションのビルド」を選択するとビルドします。


![image](https://user-images.githubusercontent.com/6216077/57682519-0772fd00-766d-11e9-9d23-06189e4a674b.png)

ビルドに成功すると`Flip/build/src/Release(もしくはDebug)`に**FlipComp.exe**が生成されます。

Ubuntuの場合はmakeコマンドでビルドしてください。


### 動作確認
#### RT System Editorの起動
Flipコンポーネントの動作確認には、Flipコンポーネントへ画像データの送信、変換後の画像データの受信するRTCが必要になります。
またデータポートが通信を行うためにはコネクタを生成する必要があります。
データポートの接続、RTCのアクティブ化等はRT System Editor等のツールで操作できます。

OpenRTPの右上のパースペクティブを開くボタンを押してください。

![image](https://user-images.githubusercontent.com/6216077/57675174-22894100-765c-11e9-8bc8-aa05744401a8.png)

RT System Editorを選択して起動してください。

![image](https://user-images.githubusercontent.com/6216077/57683266-49e90980-766e-11e9-8006-f5b68e83e0d5.png)

#### ネームサーバー起動
ネームサーバーは名前でオブジェクトを管理するための仕組みです。
RTCは自身の参照をネームサーバーに登録することで名前でRTCを管理できるようになります。

ネームサービスビューの以下のボタンで起動できます。

![image](https://user-images.githubusercontent.com/6216077/57683500-c5e35180-766e-11e9-8e5b-618d56929491.png)

#### OpenCVCameraコンポーネント、CameraViewerコンポーネントの起動
OpenCVCameraコンポーネントはUSBカメラの画像をOutPortから送信するRTC、CameraViewerコンポーネントはInPortの入力画像をGUIに表示するRTCです。
Windows 10の場合は右下の「ここに入力して検索」に**C++_OpenCV-Examples**を入力してサンプルコンポーネントをインストールしたフォルダを開きます。

![image](https://user-images.githubusercontent.com/6216077/57683746-4b670180-766f-11e9-8e50-830f6ad4c951.png)


OpenCVCamera.bat、CameraViewer.batをダブルクリックするとRTCが起動します。

![image](https://user-images.githubusercontent.com/6216077/57683848-85380800-766f-11e9-913d-fa728eaa61ad.png)

#### Flipコンポーネントの起動
ビルドして作成した**FlipComo.exe**をダブルクリックして起動してください。

#### データポートの接続
RT System EditorのONと書かれたボタンを押してSystem Diagramを起動します。
System Diagramにネームサーバーに登録されたRTCをドラッグアンドドロップします。

![image](https://user-images.githubusercontent.com/6216077/57684359-9897a300-7670-11e9-8307-70888cd7c97c.png)


ポートからポートにドラッグアンドドロップすることでコネクタを生成できます。これでOutPortとInPortが通信できるようになります。


![image](https://user-images.githubusercontent.com/6216077/57684580-08a62900-7671-11e9-9931-4167e4d46ea8.png)

以下のようにポートを接続してください。

![image](https://user-images.githubusercontent.com/6216077/57684629-22477080-7671-11e9-9535-798950bea3b1.png)

#### 動作確認
##### RTCのアクティブ化
以下のActivate Systemsボタンを押すとシステムダイアグラム上のRTCをアクティブ化します。
RTCがアクティブ状態に遷移するとシステムダイアグラム上で緑色に変化します。

![image](https://user-images.githubusercontent.com/6216077/57684754-620e5800-7671-11e9-8197-8db0fb3d2a0d.png)

アクティブ化後、カメラ画像を反転させた画像がGUI上に表示されます。

**Activate Systemsボタンが表示されない場合**
OpenRTPを一旦終了、再起動してシステムダイアグラムの起動、RTCの配置をやり直してください。


##### コンフィギュレーションパラメータの操作
コンフィギュレーションパラメータを操作することで画像反転モードを変更できます。
Flipコンポーネントをクリックして、Configuration Viewの編集ボタンを押してください。

![image](https://user-images.githubusercontent.com/6216077/57684946-caf5d000-7671-11e9-908e-3ec1113f5d93.png)

以下のラジオボタンを操作することで画像の反転方向を変更できます。

![image](https://user-images.githubusercontent.com/6216077/57685115-2627c280-7672-11e9-8d51-c07085b17280.png)

処理を中断する場合はDeactivate Systemsボタンを押してください。

![image](https://user-images.githubusercontent.com/6216077/57685376-b49c4400-7672-11e9-9783-1c62bb3713a9.png)

RTCを終了する場合はAll Exitボタンを押してください。

![image](https://user-images.githubusercontent.com/6216077/57685439-d72e5d00-7672-11e9-8723-43cfb6d5d2ff.png)
