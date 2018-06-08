---
layout: default
---

# OpenRTM-aist web on the github

このページは、github上に作成されたOpenRTM-aist臨時Webページです。
Webサイトのセキュリティアップデートのため、4月いっぱいの予定でOpenRTM-aistの公式Webページを一時停止します。
ご迷惑をおかけしますがご理解のほどよろしくお願いいたします。

This is the OpenRTM-aist official and templary website on the github.
Due to security updates of the website, OpenRTM-aist website might be closed during April.
Thank you for your cooperation and understanding.

## Downloading Packages
Linux (Ubuntu 14.04LTS, 16.04LTS) パッケージ、Windows msiインストーラ、コンパイル済みのJava（jar）パッケージのダウンロードができます。

Linux (Ubuntu 14.04LTS, 16.04LTS) packages and Windows msi installers are available.

### Linux packages

以下のリポジトリからUbuntu用のOpenRTM-aistパッケージがダウンロードできます。

| Dist/version  | URL                                      |
|:--------------|:-----------------------------------------| 
| Ubuntu 14.04  | [https://github.com/n-ando/trusty_package](https://github.com/n-ando/trusty_package) |
| Ubuntu 16.04  | [https://github.com/n-ando/xenial_package](https://github.com/n-ando/xenial_package) |


apt-get で直接インストールできませんので、リポジトリごとチェックアウトしてから dpkg コマンドで個別にインストールしてください。

Since you cannot install them by apt-get, please checkout package repository and install them by dpkg command as follows.


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

以下のコマンドでomniORB、CMake、Doxygen等をインストールしてください。

```shell
$ sudo apt-get install gcc g++ make python-yaml
$ sudo apt-get install libomniorb4-dev omniidl omniorb-nameserver
$ sudo apt-get install python-omniorb-omg omniidl-python
$ sudo apt-get install cmake doxygen
$ sudo apt-get install default-jdk
```

### Windows installer

以下のURLからWindows用のmsiファイルをダウンロードできます。ただし、ファイルが大きいためうまくダウンロードできないことがたまにあります。そういった場合は、時間をおいてダウンロードを試すか、以下のリポジトリから直接gitコマンドによりリポジトリをcloneすることで対応してください。

You can download msi-files for Windows. However, downloading from the following URLs fail sometimes. In that case, please retry again or consider checking-out msi repository by using git command.

| 32bit/64bit   | URL                                      |
|:--------------|:-----------------------------------------| 
| 32bit msi     | [https://github.com/n-ando/win32_package/raw/master/OpenRTM-aist-1.1.2-RELEASE_x86.msi](https://github.com/n-ando/win32_package/raw/master/OpenRTM-aist-1.1.2-RELEASE_x86.msi) |
| 64bit msi     | [https://github.com/n-ando/win64_package/raw/master/OpenRTM-aist-1.1.2-RELEASE_x86_64.msi](https://github.com/n-ando/win64_package/raw/master/OpenRTM-aist-1.1.2-RELEASE_x86_64.msi) |

#### Windows版msiファイルのリポジトリ

上記 URL から直接ダウンロードできない場合はgitコマンドをインストールし、以下のリポジトリをclone等することでダウンロードしてください。

| 32bit/64bit   | URL                                      |
|:--------------|:-----------------------------------------| 
| 32bit msi     | [https://github.com/n-ando/win64_package](https://github.com/n-ando/win64_package)  |
| 64bit msi     | [https://github.com/n-ando/win32_package](https://github.com/n-ando/win32_package)  |

具体的な手順は以下の通りです。

Please checkout msi file by the following process.

#### Git for Windowsのダウンロード

- Git for windows
  - [https://git-scm.com/download/win](https://git-scm.com/download/win)

#### gitによるダウンロード

```shell
> git clone https://github.com/n-ando/win64_pakage.git
> cd win64_package
win64_package の中に、OpenRTM-aist-1.1.2-RELEASE_x86_64.msi がダウンロードされています。
```
## Downloading Source-code (and jar file)

OpenRTM-aist (C++, Python, Java版) および Java版のコンパイル済みjarパッケージをダウンロードできます。

| 言語     |  URL  |
|:---------|:------| 
| C++版    | [OpenRTM-aist-1.1.2.tar.gz](https://github.com/n-ando/openrtm-src_packages/raw/master/cxx/1.1.2/OpenRTM-aist-1.1.2.tar.gz) <br> [OpenRTM-aist-1.1.2.tar.bz2](https://github.com/n-ando/openrtm-src_packages/raw/master/cxx/1.1.2/OpenRTM-aist-1.1.2.tar.bz2) <br> [OpenRTM-aist-1.1.2-win32.zip](https://github.com/n-ando/openrtm-src_packages/raw/master/cxx/1.1.2/OpenRTM-aist-1.1.2-win32.zip) |
| Python版 | [OpenRTM-aist-Python-1.1.2.tar.gz](https://github.com/n-ando/openrtm-src_packages/raw/master/python/1.1.2/OpenRTM-aist-Python-1.1.2.tar.gz) <br> [OpenRTM-aist-Python-1.1.2.zip](https://github.com/n-ando/openrtm-src_packages/raw/master/python/1.1.2/OpenRTM-aist-Python-1.1.2.zip) |
| Java版   | [OpenRTM-aist-Java-1.1.2-RELEASE-jar.zip](https://github.com/n-ando/openrtm-src_packages/raw/master/java/1.1.2/OpenRTM-aist-Java-1.1.2-RELEASE-jar.zip) <br> [OpenRTM-aist-Java-1.1.2-RELEASE.tar.gz](https://github.com/n-ando/openrtm-src_packages/raw/master/java/1.1.2/OpenRTM-aist-Java-1.1.2-RELEASE.tar.gz) <br> [OpenRTM-aist-Java-1.1.2-RELEASE.zip](https://github.com/n-ando/openrtm-src_packages/raw/master/java/1.1.2/OpenRTM-aist-Java-1.1.2-RELEASE.zip) |


## NEWS

### ROBOMECH2018 RTM講習会

#### 日時・場所
- 主催: 国立研究開発法人 産業技術総合研究所
- 協賛: ROBOMECH2018, (公社)計測自動制御学会システムインテグレーション部門
- 日時: 2018年6月3日(日), 10:00〜17:00 
- 場所: 北九州国際コンベンションゾーン
- 聴講料: 無料
  - 講習会のみの参加の場合ROBOMEC2018への参加登録は不要ですが、可能な限り参加登録をお願いします。
- 定員: 第1部50名, 実習（第2, 3部）30名程度を予定しております。定員になり次第申し込みは終了させていただきます。第1部のみご参加の方は申し込み不要です。
#### 申し込み
以下のフォームから申し込んでください。
- [申し込みフォーム(Google Form)](https://goo.gl/forms/vDW0jAmboChrlhkC2)


#### プログラム

| 10:00 -10:50	| 第1部(その1)：インターネットを利用したロボットサービスとRSiの取り組み2018 <br>　担当：成田雅彦 氏（産業技術大学院大学）|
| 11:00 -11:50	| 第1部(その2)：OpenRTM-aistおよびRTコンポーネントプログラミングの概要 <br> 担当：安藤慶昭 氏 (産総研) |
| 11:50 -12:00	| 質疑応答・意見交換 |
| 12:00 -13:00	| 昼食 |
| 13:00 -14:30	| 第2部: RTコンポーネントの作成入門 <br>担当：宮本信彦 氏 (産総研) 他 <br>概要：RTシステムを設計するツールRTSystemEditorおよびRTコンポーネント<br>を作成するツールRTCBuilderの使用方法について解説するとともに、<br>RTCBuilderを使用したRTコンポーネントの作成方法を実習形式で<br>体験していただきます。|
| 14:45 -17:00	| 第3部：プログラミング実習 <br>担当：宮本信彦 氏 (産総研) 他 <br>概要：OpenRTM-aistを利用してロボットを制御するプログラムを実際に作成します。|

- 問い合わせ： n-ando@aist.go.jp


