# RTミドルウェア強化月間 in 早稲田大学・RTミドルウェア講習会

## 目次

<!-- TOC -->

- [RTミドルウェア強化月間 in 早稲田大学・RTミドルウェア講習会](#rtミドルウェア強化月間-in-早稲田大学・rtミドルウェア講習会)
    - [目次](#目次)
    - [日時・場所](#日時・場所)
        - [他の強化月間講習会](#他の強化月間講習会)
    - [プログラム(プログラムは変更になる可能性があります）](#プログラムプログラムは変更になる可能性があります)
        - [必要機材](#必要機材)
        - [必要ソフトウエア](#必要ソフトウエア)
    - [講習会申し込みフォーム](#講習会申し込みフォーム)

<!-- /TOC -->

RTミドルウェア強化月間として、早稲田大学西早稲田キャンパスにおいて，RTミドルウェア講習会を開催します。
受講者には各自ノートPCをお持ちいただき、実習形式で実際にRTコンポーネントを作成、既存のコンポーネントなどと組み合わせて簡単なシステムを構築していただきます。
本講習会を受講することで、RTコンポーネント設計方法、実装の仕方、システムの作り方をマスターすることができます。

## 日時・場所
- **日時：** 2019年7月11日 (木) 13:00〜17:00
- **場所・アクセス：** [早稲田大学　西早稲田キャンパス](https://www.waseda.jp/fsci/access/)、55号館S棟4階 ゼミ・会議室A（407室）
  - [googleマップ](https://maps.google.co.jp/maps?q=35.705585,139.708339&hl=ja&ll=35.705585,139.708339&spn=0.008956,0.016512&sll=35.705593,139.708436&sspn=0.008956,0.016512&brcurrent=3,0x60188d24cf30335b:0x9cc4ed5b2edeb4a7,0&t=m&z=17)
   or http://www.sci.waseda.ac.jp/access/
- **主催：** 産業技術総合研究所
- **聴講料：** 無料 
- **定員**: 10名程度を予定しております。定員になり次第申し込みは終了させていただきます。
- **参加登録：** 参加登録フォームは[こちら](https://forms.gle/cEgtfQ8HUuTUCoL4A)

### 他の強化月間講習会

- [RTミドルウェア強化月間2019 in名城大学・RTミドルウェア講習会](bootcamp2019_meijyo)
- [都産技研主催・OpenRTM-aistによるロボット・ソフトウェア開発](https://www.iri-tokyo.jp/seminar/190709.html)

## プログラム(プログラムは変更になる可能性があります）

|**時間**|**概要**|
|:---|:---|
| 13:00 -14:00 | **第1部：RTミドルウエア: OpenRTM-aist概要** <br/> **担当：** 安藤慶昭(産総研) <br/> **概要：** RTミドルウエアはロボットシステムをコンポーネント指向で構築するソフトウエアプラットフォームです。RTミドルウエアを利用することで、既存のコンポーネントを再利用し、モジュール指向の柔軟なロボットシステムを構築することができます。RTミドルウエアの産総研による実装であるOpenRTM-aistについてその概要について説明します。 <br/> **講義資料**：|
| 14:15 -17:00 | **第2部: RTコンポーネントの作成入門** <br/> **担当：** 宮本信彦(産総研) <br/> **概要：** RTシステムを設計するツールRTSystemEditorおよびRTコンポーネントを作成するツールRTCBuilderの使用方法について解説するとともに、RTCBuilderを使用したRTコンポーネントの作成方法を実習形式で体験していただきます。 <br/> [チュートリアル（Raspberry Pi Mouse、Windows編）](https://openrtm.org/openrtm/ja/node/6310) <br/> [チュートリアル（Raspberry Pi Mouse、Ubuntu編）](https://openrtm.org/openrtm//ja/node/6311) <br/> **講義資料**： |


## 資料
説明資料等を講習会当日にUSBメモリで配布する予定ですが、何らかの理由によりUSBメモリを利用できない場合は以下のZIPファイルをダウンロードしてください。

* [RTM_Tutorial_RaspberryPiMouse.zip](https://github.com/OpenRTM/RTM_Tutorial_RaspberryPiMouse/archive/master.zip)

## 必要機材
- ノートPC
  - OS: Windowsを推奨します。
  - Eclipseが動作する程度のスペックが必要です
  - メモリ: 1GB以上
  - CPU: Core2Duo以上
  - HDD空き: 5GB以上 (Visual C++の場合)
- USBカメラ (USBカメラ無しで申込まれた方には貸与いたします)

**※ Windowsのファイアウォールは必ず切っておいてください。**
<br/>
**※ セキュリティーソフトにもファイアウォールが設定されている場合がありますので、そちらもOFFにしておいてください。**



## 必要ソフトウエア

### Windowsの場合

あらかじめインストールしておくべきソフトウエアは以下のとおりです。以下のリンクをクリックし、ファイルをダウンロード・インストールしてください。(一部のリンクはダウンロードページへ飛びますので、飛んだ先のページ内で適切なファイルをそれぞれダウンロードしてください。


- Visual Studio 2017推奨：[Visual Studio のダウンロード](https://visualstudio.microsoft.com/ja/downloads/?utm_source=mscom&utm_campaign=msdocs)
  - **Visual C++がインストールされているかは必ず確認してください。**
  - これからダウンロードされる場合、バージョンが2019となります。 [Visual Studio Community 2019のインストール](https://openrtm.org/openrtm/ja/vs_install_2019) ページの手順でダウンロードできます。
- [Python 2.7](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi)
- [CMake](https://github.com/Kitware/CMake/releases/download/v3.14.1/cmake-3.14.1-win64-x64.msi)
- [Doxygen](http://doxygen.nl/files/doxygen-1.8.14-setup.exe)
- [OpenRTM-aist-1.2.0-RELEASE](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86_64.msi)
  - **Visual Studio 2019を使用する場合は** [OpenRTM-aist-1.2.1-RC190514](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.1-RC190514_x86_64.msi) **をインストールしてください。**
  - デフォルト設定のままインストールして下さい。
- [OpenRTM-aistを10分で始めよう！](https://openrtm.org/openrtm/ja/node/6521) を参考に、事前にサンプルコンポーネントを起動して動作確認を行っておいてください。


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
$ wget https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz
$ tar xf OpenRTM-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz
$ cd OpenRTM-aist_1.2.0_ubuntu18.04_amd64_package
$ sudo sh install-openrtm-deb-packages.sh
$ cd ..

Python版のインストール
$ wget https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python_1.2.0_ubuntu18.04_amd64_package.tar.gz
$ tar xf OpenRTM-aist-Python_1.2.0_ubuntu18.04_amd64_package.tar.gz
$ cd OpenRTM-aist-Python_1.2.0_ubuntu18.04_amd64_package
$ sudo sh install-openrtm-deb-packages.sh
$ cd ..


$ RTSystemEditor/RTCBuilderのインストール
$ wget https://github.com/OpenRTM/OpenRTP-aist/releases/download/v1.2.0/OpenRTP-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz
$ tar xf OpenRTP-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz
$ cd OpenRTP-aist_1.2.0_ubuntu18.04_amd64_package
$ sudo sh install-openrtm-deb-packages.sh
$ cd ..
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
$ wget https://raw.githubusercontent.com/OpenRTM/RTM_Tutorial_RaspberryPiMouse/master/script/install_raspimouse_simulator.sh
$ sh install_raspimouse_simulator.sh
```



* Code::Blocks(任意)

```shell
$ sudo apt-get install codeblocks
```



* cmake-gui(任意)

```shell
$ sudo apt-get install cmake-qt-gui
```



## 講習会申し込みフォーム

以下のフォームから講習会へお申し込みください。
- [参加登録フォーム](https://forms.gle/cEgtfQ8HUuTUCoL4A)
  - フォーム送信後、確認メールをお送りいたします。1日たっても確認メールが届かない場合は、rtm-tutorial(at)aist.go.jp までお問い合わせください。
  (at)を＠におきかえてください。

