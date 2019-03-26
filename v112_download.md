<a name="v112_download"></a>
## OpenRTM-aist 1.1.2版 ダウンロード

OpenRTM-aistの旧バージョン、OpenRTM-aist 1.1.2 を下記からダウンロードできます。

- [Linux Pakcages](#linux_packages)
- [Windows installer](#windows_packages)
- [Source Code](#source_code)

<a name="download"></a>
## Downloading Packages
Linuxパッケージ、Windows msiインストーラ、コンパイル済みのJava（jar）パッケージのダウンロードができます。

Linux packages and Windows msi installers are available.

<a name="linux_packages"></a>
### Linux packages

以下からUbuntu、Debian用のOpenRTM-aistパッケージがダウンロードできます。


apt-get で直接インストールできませんので、各パッケージ(tar.gz)に同梱している install-openrtm-deb-packages.sh スクリプトでインストールしてください。

Since you cannot install them by apt-get, please install it using the bundled install-openrtm-deb-packages.sh script.


#### OpenRTM-aist C++


| Dist/version         | OpenRTM-aist C++                                      |
|:---------------------|:-----------------------------------------| 
| Ubuntu 14.04 (32bit) | [OpenRTM-aist_1.1.2_ubuntu14.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_ubuntu14.04_i386_package.tar.gz) |
| Ubuntu 14.04 (64bit) | [OpenRTM-aist_1.1.2_ubuntu14.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_ubuntu14.04_amd64_package.tar.gz) |
| Ubuntu 16.04 (32bit) | [OpenRTM-aist_1.1.2_ubuntu16.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_ubuntu16.04_i386_package.tar.gz) |
| Ubuntu 16.04 (64bit) | [OpenRTM-aist_1.1.2_ubuntu16.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_ubuntu16.04_amd64_package.tar.gz) |
| Ubuntu 18.04 (64bit) | [OpenRTM-aist_1.1.2_ubuntu18.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_ubuntu18.04_amd64_package.tar.gz) |
| Deiban 8 (32bit) | [OpenRTM-aist_1.1.2_debian8_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_debian8_i386_package.tar.gz) |
| Deiban 8 (64bit) | [OpenRTM-aist_1.1.2_debian8_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_debian8_amd64_package.tar.gz) |
| Deiban 9 (32bit) | [OpenRTM-aist_1.1.2_debian9_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_debian9_i386_package.tar.gz) |
| Deiban 9 (64bit) | [OpenRTM-aist_1.1.2_debian9_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist_1.1.2_debian9_amd64_package.tar.gz) |


#### OpenRTM-aist-Python


| Dist/version         | OpenRTM-aist-Python                                     |
|:---------------------|:-----------------------------------------| 
| Ubuntu 14.04 (32bit) | [OpenRTM-aist-Python_1.1.2_ubuntu14.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python_1.1.2_ubuntu14.04_i386_package.tar.gz) |
| Ubuntu 14.04 (64bit) | [OpenRTM-aist-Python_1.1.2_ubuntu14.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python_1.1.2_ubuntu14.04_amd64_package.tar.gz) |
| Ubuntu 16.04 (32bit) | [OpenRTM-aist-Python_1.1.2_ubuntu16.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python_1.1.2_ubuntu16.04_i386_package.tar.gz) |
| Ubuntu 16.04 (64bit) | [OpenRTM-aist-Python_1.1.2_ubuntu16.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python_1.1.2_ubuntu16.04_amd64_package.tar.gz) |
| Deiban 8 (32bit) | [OpenRTM-aist-Python_1.1.2_debian8_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python_1.1.2_debian8_i386_package.tar.gz) |
| Deiban 8 (64bit) | [OpenRTM-aist-Python_1.1.2_debian8_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python_1.1.2_debian8_amd64_package.tar.gz) |
| Deiban 9 (32bit) | [OpenRTM-aist-Python_1.1.2_debian9_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python_1.1.2_debian9_i386_package.tar.gz) |
| Deiban 9 (64bit) | [OpenRTM-aist-Python_1.1.2_debian9_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python_1.1.2_debian9_amd64_package.tar.gz) |


#### OpenRTM-aist-Java

1.1.2版ではdebパッケージを提供しておりません。[コンパイル済みのJava（jar）パッケージ](#source_code)をご利用下さい。


#### OpenRTP-aist


| Dist/version         | OpenRTP-aist                                     |
|:---------------------|:-----------------------------------------| 
| Ubuntu 14.04 (32bit) | [OpenRTP-aist_1.2.0-RC1_ubuntu14.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_ubuntu14.04_i386_package.tar.gz) |
| Ubuntu 14.04 (64bit) | [OpenRTP-aist_1.2.0-RC1_ubuntu14.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_ubuntu14.04_amd64_package.tar.gz) |
| Ubuntu 16.04 (32bit) | [OpenRTP-aist_1.2.0-RC1_ubuntu16.04_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_ubuntu16.04_i386_package.tar.gz) |
| Ubuntu 16.04 (64bit) | [OpenRTP-aist_1.2.0-RC1_ubuntu16.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_ubuntu16.04_amd64_package.tar.gz) |
| Ubuntu 18.04 (64bit) | [OpenRTP-aist_1.2.0-RC1_ubuntu18.04_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_ubuntu18.04_amd64_package.tar.gz) |
| Deiban 8 (32bit) | [OpenRTP-aist_1.2.0-RC1_debian8_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_debian8_i386_package.tar.gz) |
| Deiban 8 (64bit) | [OpenRTP-aist_1.2.0-RC1_debian8_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_debian8_amd64_package.tar.gz) |
| Deiban 9 (32bit) | [OpenRTP-aist_1.2.0-RC1_debian9_i386_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_debian9_i386_package.tar.gz) |
| Deiban 9 (64bit) | [OpenRTP-aist_1.2.0-RC1_debian9_amd64_package.tar.gz](https://github.com/OpenRTM/OpenRTP-aist/releases/download/svn%252FRELEASE_1_2_0_RC1/OpenRTP-aist_1.2.0-RC1_debian9_amd64_package.tar.gz) |




#### 必要なパッケージ

以下のコマンドでomniORB、CMake、Doxygen等をインストールしてください。

```shell
$ sudo apt-get install gcc g++ make python-yaml
$ sudo apt-get install libomniorb4-dev omniidl omniorb-nameserver
$ sudo apt-get install python-omniorb-omg omniidl-python
$ sudo apt-get install cmake doxygen
$ sudo apt-get install default-jdk
```





<a name="windows_packages"></a>
### Windows installer


以下からWindows用のmsiファイルをダウンロードできます。

You can download msi-files for Windows.

| 32bit/64bit   | URL                                      |
|:--------------|:-----------------------------------------| 
| 32bit msi     | [OpenRTM-aist-1.1.2-RELEASE_x86.msi](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist-1.1.2-RELEASE_x86.msi) |
| 64bit msi     | [OpenRTM-aist-1.1.2-RELEASE_x86_64.msi](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist-1.1.2-RELEASE_x86_64.msi) |


OpenRTM-aist以外に以下のソフトウェアをインストールしてください。

* [Python 2.7](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi)
* Visual Studio
  * 1.1.2版が対応しているのは、Visual Studio 2008、2010、2012、2013、2015 です
* [CMake](https://github.com/Kitware/CMake/releases/download/v3.13.2/cmake-3.13.2-win64-x64.msi)
* [Doxygen](http://doxygen.nl/files/doxygen-1.8.14-setup.exe)



<a name="source_code"></a>
## Downloading Source-code (and jar file)

OpenRTM-aist (C++, Python, Java版) および Java版のコンパイル済みjarパッケージをダウンロードできます。

| 言語     |  URL  |
|:---------|:------| 
| C++版    | [OpenRTM-aist-1.1.2.tar.gz](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist-1.1.2.tar.gz) <br> [OpenRTM-aist-1.1.2.tar.bz2](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist-1.1.2.tar.bz2) <br> [OpenRTM-aist-1.2.0-win32.zip](https://github.com/OpenRTM/OpenRTM-aist/releases/download/svn%2FRELEASE_1_1_2/OpenRTM-aist-1.1.2-win32.zip) |
| Python版 | [OpenRTM-aist-Python-1.1.2.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python-1.1.2.tar.gz) <br> [OpenRTM-aist-Python-1.1.2.zip](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Python-1.1.2.zip) |
| Java版   | [OpenRTM-aist-Java-1.1.2-RELEASE-jar.zip](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Java-1.1.2-RELEASE-jar.zip) <br> [OpenRTM-aist-Java-1.1.2-RELEASE.tar.gz](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Java-1.1.2-RELEASE.tar.gz) <br> [OpenRTM-aist-Java-1.1.2-RELEASE.zip](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/download/svn%252FRELEASE_1_1_2/OpenRTM-aist-Java-1.1.2-RELEASE.zip) |

