

<a name="tutorial_waseda"></a>
## RTM強化月間2018 in 早稲田大学

### 日時・場所
- 日時: 2018年7月6日(金), 13:00 - 17:00 
- 場所: 早稲田大学西早稲田キャンパス55号館S棟5階510室 (会議室C)
- 聴講料: 無料
- 定員: 10名程度を予定しております。定員になり次第申し込みは終了させていただきます。
### 申し込み
以下のフォームから申し込んでください。
- [申し込みフォーム(Google Form)](https://goo.gl/forms/0H0lnVIiWMGMDSZx1)


### プログラム(予定)
13:00 -14:00 第1部：RTミドルウエア: OpenRTM-aist概要 
- 担当：安藤 慶昭(産総研)
- 概要：RTミドルウエアはロボットシステムをコンポーネント指向で構築するソフトウエアプラットフォームです。RTミドルウエアを利用することで、既存のコンポーネントを再利用し、モジュール指向の柔軟なロボットシステムを構築することができます。RTミドルウエアの産総研による実装であるOpenRTM-aistについてその概要について説明します。

14:00 -17:00 第2部: RTコンポーネントの作成入門
- 担当：宮本 信彦(産総研)
- 概要：コンポーネント開発ツールRTCBuilder、システム構築支援ツールRTSystemEditorの使用方法を説明します。実習としてRaspberry Piマウスのシミュレータ、実機を制御するRTシステムの作成を行います。

<a name="install"></a>
### 事前準備

#### ノートPC
第2部ではノートPCを用いた実習を行うため、ノートPCの用意をお願いします。
ノートPCが用意できない場合は貸し出します。当日申し出てください。

ノートPCにウイルス対策ソフトをインストールしている場合は、教材ロボットと通信できなくなる場合があるため無効にしてください。
無効にできない場合はこちらで用意したノートPCを貸し出します。

#### 資料
説明資料等を講習会当日にUSBメモリで配布する予定ですが、何らかの理由によりUSBメモリを利用できない場合は以下のZIPファイルをダウンロードしてください。

* [RTM_Tutorial_Waseda2018.zip](https://github.com/OpenRTM/RTM_Tutorial_Waseda2018/raw/master/RTM_Tutorial_Waseda2018.zip)

#### インストールするソフトウェア
##### Windowsの場合
以下のソフトウェアをインストールしてください。
* [Visual Studio 2017](vs_install)
  * Visual C++がインストールされているかは必ず確認してください。
* [Python 2.7](https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi)
* [CMake](https://cmake.org/files/v3.11/cmake-3.11.4-win64-x64.msi)
* [Doxygen](http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.11-setup.exe)
* [OpenRTM-aist-1.2.0-RC1](https://drive.google.com/uc?id=1-sJPFro2qA82HyESidYSqhbmgj_2fo_O&export=download)

※1.2.0-RC1の不具合によりRTCをビルドする際にエラーが出る場合があります。リリース版では解消する予定です。
問題が発生する場合は生成したひな型コードのidlフォルダ内のCMakeLists.txtの先頭部分を変更します。

    set(idls BasicDataTypes.idl ExtendedDataTypes.idl)

この部分からBasicDataTypes.idl等を削除してください。

    set(idls )

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
$ wget https://raw.githubusercontent.com/OpenRTM/RTM_Tutorial_Waseda2018/master/script/install_raspimouse_simulator.sh
$ sudo sh install_raspimouse_simulator.sh
```

* Code::Blocks(任意)

```shell
$ sudo apt-get install codeblocks
```
