---
layout: page
title: ソースからのビルド(linux編)
---
<br>
<a>No English version available.
</a>

<!-- Title: ソースからのビルド(Linux編) -->
パッケージが用意されていないUNIX系の環境や、クロス開発環境などで、OpenRTM-aist本体のソースを変更したり再ビルドて、OpenRTM-aistを利用したい場合には、ソースからビルド可能です。ここでは、ダウンロードページやリポジトリからソースを取得しLinux上でOpenRTM-aist をビルドする方法を説明します。


#contents

## 配布ソースのビルド

OpenRTM-aist(C++版)はautotoolsを利用したビルド環境を提供しているため、さまざまな環境でビルドできます。

### 対応 OS およびディストリビューション 
OpenRTM-aistは下記のLinuxディストリビューションでビルドできることが確認されています。

- Fedora(限定されたバージョンのみ)
- Debian(限定されたバージョンのみ)
- Ubuntu
- Raspbian(未確認)

これ以外の環境でも、一般的Linux/UNIX環境であれば、ビルドできる可能性があります。

### 必要ツールとライブラリ

OpenRTM-aist-1.2.xをソースからビルドするには下記の開発用ツールおよびライブラリが必要です。

- gcc/g++ version3以降: コンパイルに必要
- omniORB-4.x以上: OpenRTM-aistのビルドに必要
- uuidライブラリ: libuuid (Linux環境ではデフォルトでuuid生成関数を提供していないため) 
- python: ビルドツールを利用するために必要
- boost: 拡張モジュールをコンパイルする際に必要になる場合がある 
- openssl: OpenSSLによるセキュアな通信機能を使用するために必要


それぞれのライブラリなどのドキュメントに従いインストールを行ってください。これらが標準のディレクトリ(/usr、/usr/localなど)下にインストールされていると、以降のOpenRTM-aistのコンパイル作業を比較的簡単に行うことができます。

UbuntuやFedoraなどの特定のディストリビューション向けには、一括インストール・スクリプト ''pkg_install_OS名.sh’’という依存ライブラリやOpenRTMのパッケージをインストールするスクリプトが用意されていて、それにより必要なツールをインストールすることができます。下記のリンクに入手方法やコマンドラインオプションなどが説明されています。

このスクリプトを-cオプションを用いて実行することにより、コア(OpenRTM-aist自体の)開発用のツールをインストールすることができます。それを実行するか、別個に必要なツールをインストールしておいてください。

- [一括インストール・スクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)

### ソースのダウンロード

OpenRTM-aistのソースをダウンロードします。
ソースコードは、https://github.com/OpenRTM/OpenRTM-aist/releases のバージョン番号のタグからダウンロードできます。バージョン1.2.1のソースコードは以下の場所にあります。
- https://github.com/OpenRTM/OpenRTM-aist/releases/tag/v1.2.1

### ソースコードの展開 

まずソースコードOpenRTM-aist-X.X.X.tar.gzを適当なディレクトリに展開します。

```
 $ wget https://github.com/OpenRTM/OpenRTM-aist/releases/tag/v1.2.1/OpenRTM-aist-1.2.1.tar.gz
 $ tar xvzf OpenRTM-aist-1.2.1.tar.gz
 $ cd OpenRTM-aist-1.2.1
```

### ビルド 

OpenRTM-aistはパッケージのビルドにautoconf、automakeを使用しています。上記の方法でダウンロードできるソースコードのパッケージは、あらかじめそれらのツールを使用して構成されているものです。

```
 $  ./configure --prefix=/usr --enable-fluentd=no --enable-observer=yes --enable-ssl=yes [options]
```

基本的には[options]の指定はいりませんが、特別な設定をしたい場合の[options]で使用可能なオプションは

```
 $ ./configure --help
```

で参照してください。

### make

configureが正常に終了したことを確認してください。正常に終了したらmake します。

```
 $ make
```

ビルドが正常に終了したら、ヘッダファイル、ライブラリ、ユーティリティコマンド群をインストールします。

```
 $  sudo make install
```

以上で、ソースコードからのビルドおよびインストールは終了です。


## GitHubリポジトリ上のソースを用いたビルド

OpenRTM-aistは開発に利用しているgithubリポジトリを一般に公開しています。リポジトリからクローンしたソースコードを用いてもビルド可能です。

### 必要なツール

リポジトリからチェックアウトしたソースはconfigureスクリプトやMakefile.inが含まれていません。これらを生成するには、

- automake
- libtool
- atoconf

などのツールが必要ですのであらかじめインストールしておきます。これらの必要なツールやOmniORBなどのライブラリをインストールするのにあたって、Ubuntuなどでは上記で説明した[一括インストール・スクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)を利用可能です。このスクリプトをあらかじめ実行しておくことを推奨します。

- https://github.com/OpenRTM/OpenRTM-aist

Ubuntuでは上記で推奨した一括インストールスクリプトpkg_install_ubuntu.shを以下のように実行することで、OpenRTM-aist本体の開発(ここで行うソースからのビルドも含みます)のためのツール(automakeなどを含む)などをまとめてインストール可能です。

```
 # sudo sh pkg_install_ubuntu.sh -l c++ -c 
```

### GitHubリポジトリからのソースのクローン

ソースをリポジトリからクローンします。

```
 $ git clone -b svn/RELENG_1_2 https://github.com/OpenRTM/OpenRTM-aist
 Cloning into 'OpenRTM-aist'...
 remote: Enumerating objects: 24, done.
 remote: Counting objects: 100% (24/24), done.
 remote: Compressing objects: 100% (24/24), done.
 remote: Total 42092 (delta 14), reused 2 (delta 0), pack-reused 42068
 Receiving objects: 100% (42092/42092), 10.41 MiB | 8.36 MiB/s, done.
 Resolving deltas: 100% (31578/31578), done.
```


### autogen.shの実行
クローンすると、OpenRTM-aistというディレクトリができているはずですので、そのディレクトリに入ります。

```
 $ ls 
 OpenRTM-aist
 $ cd OpenRTM-aist
 $ ls
 AUTHORS         Makefile.am     acinclude.m4    examples/       win32/
 COPYING.LIB     NEWS            build/          include/
 COPYRIGHT*      README          configure.ac    openrtm.m4
 ChangeLog       README.jp       docs/           src/
 INSTALL.jp      TUTORIAL.jp     etc/            utils/
```

buildディレクトリの下にautogenというシェルスクリプトがあることを確認し、このスクリプトを実行します。実行には、数分程度の時間がかかることがあります。

```
 $ls build/autogen
 build/autogen*
 $ sh build/autogen
 
 Setting up environment to generate configure script.
 
 ------------------------------------------------------------
  Searching Autotools
 ------------------------------------------------------------
 autoconf   was found in /usr/local/bin/autoconf.
 autoheader was found in /usr/local/bin/autoheader.
 autom4te   was found in /usr/local/bin/autom4te.
 autoreconf was found in /usr/local/bin/autoreconf.
 autoupdate was found in /usr/local/bin/autoupdates.
 automake   was found in /usr/local/bin/automake-1.9.
 aclocal    was found in /usr/local/bin/aclocal-1.9.
 libtool    was found in /usr/local/bin/libtool.
 libtoolize was found in /usr/local/bin/libtoolize.
 
 ------------------------------------------------------------
  Searching libtool.m4
 ------------------------------------------------------------
 file was found: /usr/local/share/aclocal/libtool.m4
 
  Copying libtool.m4 from /usr/local/share/aclocal/libtool.m4
 
 ------------------------------------------------------------
  Doing autoreconf
 ------------------------------------------------------------

 autoreconf-2.62: Entering directory `.'
 autoreconf-2.62: configure.ac: not using Gettext
 autoreconf-2.62: running: /usr/local/bin/aclocal-1.9 --force
 autoreconf-2.62: configure.ac: tracing
 autoreconf-2.62: configure.ac: adding subdirectory src/lib/coil to autoreconf
 autoreconf-2.62: Entering directory `src/lib/coil'
 autoreconf-2.62: running: /usr/local/bin/libtoolize --copy --force
 You should update your `aclocal.m4' by running aclocal.
 autoreconf-2.62: running: /usr/local/bin/autoconf --force
 autoreconf-2.62: running: /usr/local/bin/autoheader --force
 autoreconf-2.62: running: /usr/local/bin/automake-1.9 --add-missing --copy --force-missing
 configure.ac: installing `./install-sh'
 configure.ac: installing `./missing'
 ace/coil/Makefile.am: installing `./depcomp'
 Makefile.am: installing `./INSTALL'
 autoreconf-2.62: Leaving directory `src/lib/coil'
 You should update your `aclocal.m4' by running aclocal.
 configure.ac: installing `./install-sh'
 configure.ac: installing `./missing'
 examples/AutoTest/Makefile.am: installing `./depcomp'
 Makefile.am: installing `./INSTALL'
 autoreconf-2.62: Leaving directory `.'
 done
 $
```

### configure & ビルド

autogenの実行により、configureがOpenRTM-aistディレクトリ内にできているはずですので、以降は通常のソースからのビルドと同様に、configure & makeでビルドします。

```
 $ ls -l configure
 -rwxr-xr-x  1 n-ando  n-ando  812893 Jul  6 05:56 configure*
 $  ./configure --prefix=/usr --enable-fluentd=no --enable-observer=yes --enable-ssl=yes
 $ make
```

### make dist

**make dist**を行うことでopenrtm.orgで配布しているようなソースのパッケージの作成も可能です。
また、make dist では Windows上でビルド可能なソースコードのパッケージも同時に作成します。
ただし、make distを行うには、doxygenやlatex、qkcなど、追加のコマンドが必要です。

```
 $ make dist
 数分程度かかります。
 $ ls -l OpenRTM-aist*
 -rw-r--r--  1 n-ando  n-ando  9266837 Apr  7 09:53 OpenRTM-aist-1.2.1-win32.zip
 -rw-r--r--  1 n-ando  n-ando  4831099 Apr  7 09:53 OpenRTM-aist-1.2.1.tar.bz2
 -rw-r--r--  1 n-ando  n-ando  7258796 Apr  7 09:53 OpenRTM-aist-1.2.1.tar.gz
 $
```

生成されるソースパッケージはそれぞれ以下の通りです。

- OpenRTM-aist-1.2.1-win32.zip: Windows用ソース
- OpenRTM-aist-1.2.1.tar.gz: 汎用ソース (gzip圧縮)
- OpenRTM-aist-1.2.1.tar.bz2: 汎用ソース (bzip圧縮)




