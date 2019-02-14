

<a name="ROBOMECH2019"></a>
## ROBOMECH2019 RTM講習会

### 開催報告

2019年6月5日(水)に広島国際会議場において、ROBOMECH2019 RTミドルウエア講習会を開催いたします。

### 日時・場所
- 日時: 2019年6月5日(水)
- 場所: 広島国際会議場 (詳細未定)
- 聴講料: 無料


### 申し込み



<!--
以下のフォームから申し込んでください。
- [申し込みフォーム(Google Form)](https://goo.gl/forms/8V7nAiHtMl94zeR73)
-->

### プログラム(予定)

|||
|:---|:---|
|10:00 -10:50|第1部(その1)：未定 |
|11:00 -12:00|第1部(その2)：RTミドルウエア: OpenRTM-aist概要 <br>- 担当：安藤 慶昭(産総研)  <br>- 概要：RTミドルウエアはロボットシステムをコンポーネント指向で構築するソフトウエアプラットフォームです。RTミドルウエアを利用することで、既存のコンポーネントを再利用し、モジュール指向の柔軟なロボットシステムを構築することができます。RTミドルウエアの産総研による実装であるOpenRTM-aistについてその概要について説明します。|
|12:00 -13:00|昼食|
|13:00 -14:30|第2部：RTコンポーネントの作成入門 <br> - 担当：宮本 信彦(産総研) <br> - 概要：RTシステムを設計するツールRTSystemEditorおよびRTコンポーネントを作成するツールRTCBuilderの使用方法について解説するとともに、移動ロボットのシミュレータを用いた実習によりRTCBuilder、RTSystemEditorの利用法の学習します。 <br> [チュートリアル(第2部、Windows)](https://tmp.openrtm.org/openrtm/ja/node/6550)<br> [チュートリアル(第2部、Ubuntu)](https://tmp.openrtm.org/openrtm/ja/node/6551)| 
|14:30 -15:30|第3部：RTシステム構築実習 <br> - 担当：宮本 信彦(産総研) <br> - 概要：OpenRTM-aistを利用して移動ロボット実機を制御するプログラムを実際に作成します。  <br>[チュートリアル(第3部)](https://tmp.openrtm.org/openrtm/ja/node/6552)|
|15:30 -17:00|第4部：RTミドルウェア応用実習 <br> - 担当：宮本 信彦(産総研) <br> - 概要：ポータブル版LibreOffice用RTCの利用方法について解説を行うとともに、表計算ソフトによるRTCのテストの実行についての実習を行います。  <br>[チュートリアル(第4部)](https://www.slideshare.net/openrtm/rt2018rt)|
 	






<a name="install"></a>
### 事前準備

#### ノートPC
第2部ではノートPCを用いた実習を行うため、ノートPCの用意をお願いします。
ノートPCが用意できない場合は貸し出します。当日申し出てください。

ノートPCにウイルス対策ソフトをインストールしている場合は、教材ロボットと通信できなくなる場合があるため無効にしてください。
無効にできない場合はこちらで用意したノートPCを貸し出します。

#### 資料
説明資料等を講習会当日にUSBメモリで配布する予定ですが、何らかの理由によりUSBメモリを利用できない場合は以下のZIPファイルをダウンロードしてください。

* [RTM_Tutorial_ROBOMECH2019.zip](https://github.com/OpenRTM/RTM_Tutorial_ROBOMECH2019/raw/master/RTM_Tutorial_ROBOMECH2019.zip)

#### インストールするソフトウェア
##### Windowsの場合
以下のソフトウェアをインストールしてください。
* [Visual Studio 2017](vs_install.md)
  * **Visual C++がインストールされているかは必ず確認してください。**
* [Python 2.7](https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi)
* [CMake](https://cmake.org/files/v3.11/cmake-3.11.4-win64-x64.msi)
* [Doxygen](http://doxygen.nl/files/doxygen-1.8.14-setup.exe)
* [OpenRTM-aist-1.2.0-RELEASE](https://tmp.openrtm.org/pub/Windows/OpenRTM-aist/1.2/OpenRTM-aist-1.2.0-RC1_x86_64_0831.msi)


##### Ubuntuの場合
* OpenRTM-aist

```shell
$ git clone https://github.com/n-ando/xenial_package.git

ubuntu 16.04 (64bit) の場合
$ cd xenial_package/xenial/main/binary-amd64/

C++版のインストール
$ sudo dpkg -i openrtm-aist_1.1.2-0_amd64.deb
$ sudo dpkg -i openrtm-aist-example_1.1.2-0_amd64.deb
$ sudo dpkg -i openrtm-aist-dev_1.1.2-0_amd64.deb

Python版のインストール
$ sudo dpkg -i openrtm-aist-python_1.1.2-1_amd64.deb
$ sudo dpkg -i openrtm-aist-python-example_1.1.2-1_amd64.deb

RTSystemEditor/RTCBuilderのインストール
$ sudo dpkg -i openrtp_1.2.0-0_amd64.deb
```

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
$ sudo apt-get install default-jdk
```
* Premake

```shell
$ sudo apt-get install premake4
```

* RaspberryPiMouseSimulator コンポーネント

```shell
$ wget https://raw.githubusercontent.com/OpenRTM/ROBOMECH2019/master/script/install_raspimouse_simulator.sh
$ sudo sh install_raspimouse_simulator.sh
```

* Code::Blocks(任意)

```shell
$ sudo apt-get install codeblocks
```





