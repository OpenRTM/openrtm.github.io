---
layout: default
---

# OpenRTM-aist web on the github

このページは、github上に作成されたOpenRTM-aist臨時Webページです。
Webサイトのセキュリティアップデートのため、2018年度いっぱいの予定でOpenRTM-aistの公式Webページを一時停止します。
ご迷惑をおかけしますがご理解のほどよろしくお願いいたします。

This is the OpenRTM-aist official and templary website on the github.
Due to security updates of the website, OpenRTM-aist website might be closed during April.
Thank you for your cooperation and understanding.

## 目次

### [NEWS](#news)
- OpenRTM-aist-1.2 がリリースされました

### [ダウンロード](#download)
- [Linux Pakcages](#linux_packages)
- [Windows installer](#windows_packages)
- [Source Code](#source_code)

### ドキュメント
- [１０分ではじめよう！](10min_setup12.md)

### 今後のイベント
- [ROBOMECH2019 RTM講習会](ROBOMECH2019.md)


### 過去のイベント
- [RTミドルウェアコンテスト2018-表彰式の様子(2018/12/14)](contest2018-result)
- [RTミドルウェアコンテスト2018-結果発表](contest2018)
- [RTミドルウェア普及貢献賞授賞式](business_award2018)
- [Japan Robot Week 2018 RTM講習会](jrw2018)
- [RTミドルウェアサマーキャンプ2018(7/30〜8/2)](summercamp)

<!--
- [RTミドルウェアサマーキャンプ2018(7/30〜8/2)成果発表](summercamp2018)
-->

---


<a name="news"></a>

## NEWS
### OpenRTM-aist-1.2リリース

OpenRTM-aistの新バージョン、OpenRTM-aist-1.2 をリリースしました。
以下のダウンロードページからダウンロードできます。


<a name="download"></a>
## Downloading Packages
Linux (Ubuntu 14.04LTS, 16.04LTS, 18.04LTS, 18.10) パッケージ、Windows msiインストーラ、コンパイル済みのJava（jar）パッケージのダウンロードができます。

Linux (Ubuntu 14.04LTS, 16.04LTS, 18.04LTS, 18.10) packages and Windows msi installers are available.

<a name="linux_packages"></a>
### Linux packages

以下からUbuntu用のOpenRTM-aistパッケージがダウンロードできます。

<!--
| Dist/version  | URL                                      |
|:--------------|:-----------------------------------------| 
| Ubuntu 14.04  | [https://github.com/n-ando/trusty_package](https://github.com/n-ando/trusty_package) |
| Ubuntu 16.04  | [https://github.com/n-ando/xenial_package](https://github.com/n-ando/xenial_package) |
| Ubuntu 18.04  | [https://github.com/n-ando/bionic_package](https://github.com/n-ando/bionic_package) |

apt-get で直接インストールできませんので、リポジトリごとチェックアウトしてから dpkg コマンドで個別にインストールしてください。
また、openrtp (RTSystemEditor, RTCBulder) は git コマンドでは正常にダウンロードできないことがあります。
openrtpのdebファイルは正常にダウンロードできていれば200MB以上あります。
git に LFS (large file system) 拡張をインストールするか、以下のリンクからダウンロードして取得してください。
-->
apt-get で直接インストールできませんので、各パッケージ(tar.gz)に同梱している install-openrtm-deb-packages.sh スクリプトでインストールしてください。

Since you cannot install them by apt-get, please install it using the bundled install-openrtm-deb-packages.sh script.


#### OpenRTM-aist C++


| Dist/version         | OpenRTM-aist C++                                      |
|:---------------------|:-----------------------------------------| 
| Ubuntu 14.04 (32bit) | [OpenRTM-aist_1.2.0_ubuntu14.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist_1.2.0_ubuntu14.04_i386_package.tar.gz) |
| Ubuntu 14.04 (64bit) | [OpenRTM-aist_1.2.0_ubuntu14.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist_1.2.0_ubuntu14.04_amd64_package.tar.gz) |
| Ubuntu 16.04 (32bit) | [OpenRTM-aist_1.2.0_ubuntu16.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist_1.2.0_ubuntu16.04_i386_package.tar.gz) |
| Ubuntu 16.04 (64bit) | [OpenRTM-aist_1.2.0_ubuntu16.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist_1.2.0_ubuntu16.04_amd64_package.tar.gz) |
| Ubuntu 18.04 (64bit) | [OpenRTM-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz) |
| Ubuntu 18.10 (64bit) | [OpenRTM-aist_1.2.0_ubuntu18.10_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist_1.2.0_ubuntu18.10_amd64_package.tar.gz) |


#### OpenRTM-aist-Python


| Dist/version         | OpenRTM-aist-Python                                     |
|:---------------------|:-----------------------------------------| 
| Ubuntu 14.04 (32bit) | [OpenRTM-aist-Python_1.2.0_ubuntu14.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python_1.2.0_ubuntu14.04_i386_package.tar.gz) |
| Ubuntu 14.04 (64bit) | [OpenRTM-aist-Python_1.2.0_ubuntu14.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python_1.2.0_ubuntu14.04_amd64_package.tar.gz) |
| Ubuntu 16.04 (32bit) | [OpenRTM-aist-Python_1.2.0_ubuntu16.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python_1.2.0_ubuntu16.04_i386_package.tar.gz) |
| Ubuntu 16.04 (64bit) | [OpenRTM-aist-Python_1.2.0_ubuntu16.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python_1.2.0_ubuntu16.04_amd64_package.tar.gz) |
| Ubuntu 18.04 (64bit) | [OpenRTM-aist-Python_1.2.0_ubuntu18.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python_1.2.0_ubuntu18.04_amd64_package.tar.gz) |
| Ubuntu 18.10 (64bit) | [OpenRTM-aist-Python_1.2.0_ubuntu18.10_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python_1.2.0_ubuntu18.10_amd64_package.tar.gz) |


#### OpenRTM-aist-Java


| Dist/version         | OpenRTM-aist-Java                                     |
|:---------------------|:-----------------------------------------| 
| Ubuntu 14.04 (32bit) | [OpenRTM-aist-Java_1.2.0_ubuntu14.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java_1.2.0_ubuntu14.04_i386_package.tar.gz) |
| Ubuntu 14.04 (64bit) | [OpenRTM-aist-Java_1.2.0_ubuntu14.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java_1.2.0_ubuntu14.04_amd64_package.tar.gz) |
| Ubuntu 16.04 (32bit) | [OpenRTM-aist-Java_1.2.0_ubuntu16.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java_1.2.0_ubuntu16.04_i386_package.tar.gz) |
| Ubuntu 16.04 (64bit) | [OpenRTM-aist-Java_1.2.0_ubuntu16.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java_1.2.0_ubuntu16.04_amd64_package.tar.gz) |
| Ubuntu 18.04 (64bit) | [OpenRTM-aist-Java_1.2.0_ubuntu18.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java_1.2.0_ubuntu18.04_amd64_package.tar.gz) |
| Ubuntu 18.10 (64bit) | [OpenRTM-aist-Java_1.2.0_ubuntu18.10_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java_1.2.0_ubuntu18.10_amd64_package.tar.gz) |


#### OpenRTP-aist


| Dist/version         | OpenRTP-aist                                     |
|:---------------------|:-----------------------------------------| 
| Ubuntu 14.04 (32bit) | [OpenRTP-aist_1.2.0_ubuntu14.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/v1.2.0/OpenRTP-aist_1.2.0_ubuntu14.04_i386_package.tar.gz) |
| Ubuntu 14.04 (64bit) | [OpenRTP-aist_1.2.0_ubuntu14.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/v1.2.0/OpenRTP-aist_1.2.0_ubuntu14.04_amd64_package.tar.gz) |
| Ubuntu 16.04 (32bit) | [OpenRTP-aist_1.2.0_ubuntu16.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/v1.2.0/OpenRTP-aist_1.2.0_ubuntu16.04_i386_package.tar.gz) |
| Ubuntu 16.04 (64bit) | [OpenRTP-aist_1.2.0_ubuntu16.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/v1.2.0/OpenRTP-aist_1.2.0_ubuntu16.04_amd64_package.tar.gz) |
| Ubuntu 18.04 (64bit) | [OpenRTP-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/v1.2.0/OpenRTP-aist_1.2.0_ubuntu18.04_amd64_package.tar.gz) |
| Ubuntu 18.10 (64bit) | [OpenRTP-aist_1.2.0_ubuntu18.10_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/v1.2.0/OpenRTP-aist_1.2.0_ubuntu18.10_amd64_package.tar.gz) |

<!--
Since you cannot install them by apt-get, please checkout package repository and install them by dpkg command as follows.


```shell
$ git clone https://github.com/n-ando/xenial_package.git

ubuntu 16.04 (64bit) の場合
$ cd xenial_package/xenial/main/binary-amd64/

git でopenrtpがうまくダウンロードできない場合
$ rm openrtp_1.2.0-1_amd64.deb
$ wget https://github.com/n-ando/trusty_package/raw/master/xenial/main/binary-amd64/openrtp_1.2.0-1_amd64.deb

C++版のインストール
$ sudo dpkg -i openrtm-aist_1.2.0-0_amd64.deb
$ sudo dpkg -i openrtm-aist-example_1.2.0-0_amd64.deb
$ sudo dpkg -i openrtm-aist-dev_1.2.0-0_amd64.deb

Python版のインストール
$ sudo dpkg -i openrtm-aist-python_1.2.0-0_amd64.deb
$ sudo dpkg -i openrtm-aist-python-example_1.2.0-0_amd64.deb

Java版のインストール
$ sudo dpkg -i openrtm-aist-java_1.2.0-0_amd64.deb
$ sudo dpkg -i openrtm-aist-java-example_1.2.0-0_amd64.deb

RTSystemEditor/RTCBuilderのインストール
$ sudo dpkg -i openrtp_1.2.0-1_amd64.deb
```
-->


#### 必要なパッケージ

以下のコマンドでomniORB、CMake、Doxygen等をインストールしてください。

```shell
$ sudo apt-get install gcc g++ make python-yaml
$ sudo apt-get install libomniorb4-dev omniidl omniorb-nameserver
$ sudo apt-get install python-omniorb-omg omniidl-python
$ sudo apt-get install cmake doxygen
$ sudo apt-get install default-jdk
```

Ubuntu 18.04の場合はOpenJDK8のインストールが必要です。

```shell
$ sudo apt-get install openjdk-8-jdk
```

JDKを複数インストールしている場合はjava8に切り替えてください。

```shell
$ sudo update-alternatives --config java
```



<a name="windows_packages"></a>
### Windows installer

<!--
以下のURLからWindows用のmsiファイルをダウンロードできます。ただし、ファイルが大きいためうまくダウンロードできないことがたまにあります。そういった場合は、時間をおいてダウンロードを試すか、以下のリポジトリから直接gitコマンドによりリポジトリをcloneすることで対応してください。

You can download msi-files for Windows. However, downloading from the following URLs fail sometimes. In that case, please retry again or consider checking-out msi repository by using git command.
-->
以下からWindows用のmsiファイルをダウンロードできます。

You can download msi-files for Windows.

| 32bit/64bit   | URL                                      |
|:--------------|:-----------------------------------------| 
| 32bit msi     | [OpenRTM-aist-1.2.0-RELEASE_x86.msi](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86.msi) |
| 64bit msi     | [OpenRTM-aist-1.2.0-RELEASE_x86_64.msi](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86_64.msi) |


OpenRTM-aist以外に以下のソフトウェアをインストールしてください。

* Python 2.7 または 3.6 または 3.7
  * Python のインストールについては [１０分ではじめよう！](10min_setup12.md) のページをご覧ください
* [Visual Studio 2017](vs_install.md)
* [CMake](https://github.com/Kitware/CMake/releases/download/v3.13.2/cmake-3.13.2-win64-x64.msi)
* [Doxygen](http://doxygen.nl/files/doxygen-1.8.14-setup.exe)

<!--
#### Windows版msiファイルのリポジトリ

上記 URL から直接ダウンロードできない場合はgitコマンドをインストールし、以下のリポジトリをclone等することでダウンロードしてください。

| 32bit/64bit   | URL                                      |
|:--------------|:-----------------------------------------| 
| 32bit msi     | [https://github.com/n-ando/win32_package](https://github.com/n-ando/win32_package)  |
| 64bit msi     | [https://github.com/n-ando/win64_package](https://github.com/n-ando/win64_package)  |

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
-->

<a name="source_code"></a>
## Downloading Source-code (and jar file)

OpenRTM-aist (C++, Python, Java版) および Java版のコンパイル済みjarパッケージをダウンロードできます。

| 言語     |  URL  |
|:---------|:------| 
| C++版    | [OpenRTM-aist-1.2.0.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0.tar.gz) <br> [OpenRTM-aist-1.2.0.tar.bz2](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0.tar.bz2) <br> [OpenRTM-aist-1.2.0-win32.zip](https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-win32.zip) |
| Python版 | [OpenRTM-aist-Python-1.2.0.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python-1.2.0.tar.gz) <br> [OpenRTM-aist-Python-1.2.0.zip](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python-1.2.0.zip) |
| Java版   | [OpenRTM-aist-Java-1.2.0-RELEASE-jar.zip](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java-1.2.0-RELEASE-jar.zip) <br> [OpenRTM-aist-Java-1.2.0-RELEASE.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java-1.2.0-RELEASE.tar.gz) <br> [OpenRTM-aist-Java-1.2.0-RELEASE.zip](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/v1.2.0/OpenRTM-aist-Java-1.2.0-RELEASE.zip) |

