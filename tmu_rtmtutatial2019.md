このページは首都大学東京大学院のユビキタスロボティクス特論(2019年5月15日)で行うOpenRTM-aist 1.2.0のインストール、Flipコンポーネント作成の手順を記したページです。
本来は[openrtm.org](https://openrtm.org/openrtm/)のページに記載してあるのですが、授業当日にopenrtm.orgを閉じるらしいので臨時ページを作成しました。

## OpenRTM-aist 1.2.0のインストール
### 依存ソフトウェアのインストール
#### Windowsの場合
以下のソフトウェアをインストールしてください。

* [Visual Studio 2017](vs_install.md)
  * **Visual C++がインストールされているかは必ず確認してください。**
* [Python 2.7](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi)
* [CMake](https://github.com/Kitware/CMake/releases/download/v3.14.1/cmake-3.14.1-win64-x64.msi)
* [Doxygen](http://doxygen.nl/files/doxygen-1.8.14-setup.exe)

**Visual Studio 2019をインストールした場合について**

OpenRTM-aist 1.2.0はVisual Studio 2019に未対応ですが、一部ファイルを置き換えることで対応可能です。対応手順は後で説明します。

**Visual Studioをインストールすることが困難な場合について**
Visual Studioは大量のファイルをダウンロードする必要があるため、

#### Ubuntuの場合

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

## Flipコンポーネント作成手順
以下のようにInPortで受信した画像を左右上下に反転させてOutPortから出力するRTコンポーネント(RTC)を作成します。

![image](https://user-images.githubusercontent.com/6216077/57673335-7f81f880-7656-11e9-8be9-283cf3b0b314.png)

作成手順は以下のようになっています。

1. RTCの仕様を決める
2. RTC BuilderでRTCのひな形コードを生成する
3. 内部の処理を実装する
4. RTSystemEditorでRTシステムを作成、動作確認をする

### RTCの仕様を決める
RTCのモジュール名等の基本的な情報、にどのようなデータポート、サービスポート、コンフィギュレーションパラメータなどが使えるのか等の仕様をまず決める必要があります。
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
コンフィギュレーションパラメータはRTSystemEditor等のツールから実行中のRTCのパラメータを操作するための機能です。

|||
|---|---|
|パラメーター名|flipMode|
|型|int|
|デフォルト値|0|
|制約|(0、-1、1)|
|Widget|radio|

このコンフィギュレーションパラメータで画像反転パターンを設定します。

- 上下反転：flipMode=0
- 左右反転：flipMode=1
- 上下左右反転：flipMode=-1



### RTC BuilderでRTCのひな形コードを生成する
RTC BuilderはRTCのひな形コードを生成するためのGUIツールです。
先ほど決めた仕様をRTC Builderに入力すると、C++、Python、Java、Luaのコードを生成できます。

#### OpenRTPの起動
OpenRTPはRTC Builder、RTSystemEditorのツールを含む開発環境です。

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
有効にするためには、**アクティビティ**タブから



##### データポートの設定
データポートのタブを選択して、InPort、OutPortを追加します。
InPort、OutPortの追加はAddボタンを押します。

![image](https://user-images.githubusercontent.com/6216077/57675639-7a747780-765d-11e9-87fe-133944eab0f6.png)

ポートの名前はポート名をクリックすることで変更できます。

![image](https://user-images.githubusercontent.com/6216077/57675668-8fe9a180-765d-11e9-9754-a4bc77969619.png)

InPort
