

<a name="ROBOMECH2019"></a>
## ROBOMECH2019 RTM講習会

### 開催案内

<!--
2019年6月5日(水)に広島国際会議場において、ROBOMECH2019 RTミドルウエア講習会を開催いたします。
-->
2019年6月5日(水)に広島国際会議場において、ROBOMECH2019 RTミドルウエア講習会を開催いたしました。

### 日時・場所
- 日時: 2019年6月5日(水) 10:00-17:00
- 場所: 広島国際会議場 地下1F 会議運営事務室2・3
- 主催：国立研究開発法人産業技術総合研究所
- 共催: SICE SI部門RTシステムインテグレーション部会
- 聴講料: 無料
<!-- - 人数：最大20名（第1部の聴講はどなたでも参加できます。）-->
- 参加人数: 10名

<!--
### 申し込み

以下のフォームから申お申し込みください。
- [申し込みフォーム(Google Form)](https://goo.gl/forms/8V7nAiHtMl94zeR73)

Googleフォームが利用できない場合、e-mail: rtm-tutorial@aist.go.jp まで
- 氏名（フリガナ）
- 所属
- メールアドレス（後ほど準備内容などお知らせすることがあります。）
をお知らせください。
なお、取得した個人情報はROBOMECH2019 RTM講習会運営以外では使用いたしません。
-->

### プログラム

|**時間**|**概要**|
|:---|:---|
|10:00 -10:50|第1部(その1)：RTミドルウエア: OpenRTM-aist概要 <br>- 担当：安藤 慶昭(産総研)  <br>- 概要：RTミドルウエアはロボットシステムをコンポーネント指向で構築するソフトウエアプラットフォームです。RTミドルウエアを利用することで、既存のコンポーネントを再利用し、モジュール指向の柔軟なロボットシステムを構築することができます。RTミドルウエアの産総研による実装であるOpenRTM-aistについてその概要について説明します。 <br> [講演資料(PDF)](190605-01.pdf)|
|11:00 -12:00|第1部(その2)：インターネットを利用したロボットサービスとRSiの取り組み2019 <br>- 担当：成田雅彦 氏（産業技術大学院大学）|
|12:00 -13:00|昼食|
|13:00 -14:30|第2部：RTコンポーネントの作成入門 <br> - 担当：宮本 信彦(産総研) <br> - 概要：RTシステムを設計するツールRTSystemEditorおよびRTコンポーネントを作成するツールRTCBuilderの使用方法について解説するとともに、移動ロボットのシミュレータを用いた実習によりRTCBuilder、RTSystemEditorの利用法の学習します。 <br> [チュートリアル(第2部、Windows)](https://tmp.openrtm.org/openrtm/ja/node/6550)<br> [チュートリアル(第2部、Ubuntu)](https://tmp.openrtm.org/openrtm/ja/node/6551)<br> [講演資料(PDF)](190605-02.pdf)| 
|14:30 -15:30|第3部：RTシステム構築実習 <br> - 担当：宮本 信彦(産総研) <br> - 概要：OpenRTM-aistを利用して移動ロボット実機を制御するプログラムを作成します。  <br>[チュートリアル(第3部)](https://tmp.openrtm.org/openrtm/ja/node/6552)<br> [講演資料(PDF)](190605-03.pdf)|
|15:30 -17:00|第4部：RTミドルウェア応用実習 <br> - 担当：宮本 信彦(産総研) <br> - 概要：ポータブル版LibreOffice用RTCの利用方法について解説を行うとともに、表計算ソフトによるRTCのテストの実行についての実習を行います。  <br>[チュートリアル(第4部)](https://tmp.openrtm.org/openrtm/ja/node/6586)<br> [講演資料(PDF)](190605-04.pdf)|
 	

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
  * ~~Visual Studio 2019はOpenRTM-aistが未対応のため使用できません。~~
* [Python 2.7](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi)
* [CMake](https://github.com/Kitware/CMake/releases/download/v3.14.1/cmake-3.14.1-win64-x64.msi)
* [Doxygen](http://doxygen.nl/files/doxygen-1.8.14-setup.exe)
* [OpenRTM-aist-1.2.0-RELEASE](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86_64.msi)
  * **Visual Studio 2019を使用する場合は[OpenRTM-aist-1.2.1-RC190514](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.1-RC190514_x86_64.msi)をインストールしてください。**



##### Ubuntuの場合

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

* Premake

```shell
$ sudo apt-get install premake4
```

* GLUT

```shell
$ sudo apt-get install freeglut3-dev
```

* RaspberryPiMouseSimulator コンポーネント

```shell
$ wget https://raw.githubusercontent.com/OpenRTM/RTM_Tutorial_ROBOMECH2019/master/script/install_raspimouse_simulator.sh
$ sudo sh install_raspimouse_simulator.sh
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


* Code::Blocks(任意)

```shell
$ sudo apt-get install codeblocks
```



* cmake-gui(任意)

```shell
$ sudo apt-get install cmake-qt-gui
```

