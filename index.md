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

### RTM強化月間2018 in 名城大学

#### 日時・場所
- 日時: 2018年7月4日(水)
- 場所: 名城大学
- 聴講料: 無料
- 定員: 10名程度を予定しております。定員になり次第申し込みは終了させていただきます。
#### 申し込み

以下のフォームから申し込んでください。
- [申し込みフォーム(Google Form)](https://goo.gl/forms/vcGRgCx088dH1nFV2)

#### プログラム

ただいま準備中です。


### RTM強化月間2018 in 早稲田大学

#### 日時・場所
- 日時: 2018年7月6日(金), 13:00 - 17:00 
- 場所: 早稲田大学西早稲田キャンパス55号館S棟5階510室 (会議室C)
- 聴講料: 無料
- 定員: 10名程度を予定しております。定員になり次第申し込みは終了させていただきます。
#### 申し込み
以下のフォームから申し込んでください。
- [申し込みフォーム(Google Form)](https://goo.gl/forms/0H0lnVIiWMGMDSZx1)

#### プログラム

ただいま準備中です。


### RTM強化月間2018 in 都産技研

#### 日時・場所
- 日時: 2018年7月24日(火)
- 場所: 東京都立産業技術研究センター 本部
- 聴講料: 3,000円
- 定員: 10名

#### 申し込み

以下のページから申し込んでください。
- [申し込みページ(都産技研のサイトに移動します)](http://www.iri-tokyo.jp/seminar/180724-1.html)

#### プログラム

ただいま準備中です。

### サマーキャンプ2018 

#### 日時・場所
- 日時: 2018年7月30日(月)～8月3日
- 場所: 産業技術総合研究所つくばセンター中央第２
 - 産総研内の宿泊施設での宿泊が可能です。実費(約1000円/泊、食費)は参加者負担
- 参加費: 無料
- 定員: 20名程度を予定しております。定員になり次第申し込みは終了させていただきます。
- 対象者: RTM講習会に参加したことがある、もしくは同等程度の経験を有していること。 

#### 申し込み

ただいま準備中です。

#### プログラム

ただいま準備中です。

- 問い合わせ： n-ando@aist.go.jp


