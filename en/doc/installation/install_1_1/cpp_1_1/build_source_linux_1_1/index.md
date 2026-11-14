---
layout: page
title: ソースからのビルド (linux編)
---
<br>
<a>No English version available.
</a>

<!-- Title: ソースからのビルド (Linux編) -->
パッケージが用意されていない UNIX 環境や、クロス開発環境、OpenRTM-aist 本体のソースを変更して利用したい場合には、ソースからコンパイルすることができます。
ここでは、ダウンロードページやリポジトリからソースを取得し Linux 上 で OpenRTM-aist をビルドする方法を解説します。


#contents

## 配布ソースのビルド

OpenRTM-aist (C++版) は autotools を利用したビルド環境を提供しているため、様々な環境で容易にビルドできます。

### 対応 OS およびディストリビューション 
OpenRTM-aist は下記の OS および Linux ディストリビューションで動作することが確認されています。

- FreeBSD
- Vine Linux
- Fedora
- Debian
- Ubuntu

これ以外の環境でも、一般的 Linux/UNIX 環境であれば、ビルドできる可能性があります。

### 依存ライブラリ

OpenRTM-aist-1.0.0 のインストールには下記の開発環境およびライブラリが必要です。

- gcc/g++ version3 以降: コンパイルに必要
- omniORB-4.x 以上: OpenRTM-aist のビルドに必要
  - omniORB-4.0.6 にはバグがありますので利用しないでください
- uuid ライブラリ: libuuid (Linux等デフォルトで uuid 生成関数を提供していない環境のみ) 
- python: ビルドツールを利用するために必要
  - PyYAML
- boost: 拡張モジュールをコンパイルする際に必要になる場合がある 

それぞれのライブラリ等のドキュメントに従いインストールを行ってください。
これらのパッケージが、標準のディレクトリー(/usr、/usr/local 等)下にインストールされていると、以降の OpenRTM-aist のコンパイル作業を比較的簡単に行うことができます。

UbuntuやFedora等特定のディストリビューション向けには、以下のリポジトリに ''pkg_install_OS名.sh’’という依存ライブラリやOpenRTMのパッケージをインストールするスクリプトが用意されています。

<!-- - https://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/ -->

これらのインストールスクリプトの使い方については、[「一括インストール・スクリプト」]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)のページをご覧ください。

### ソースのダウンロード

OpenRTM-aist のソースをダウンロードします。
ソースコードは、http://www.openrtm.org/pub/OpenRTM-aist/cxx/ の下のバージョン番号フォルダ以下からダウンロードできます。
バージョン1.1.2のソースコードは以下の場所にあります。
- http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.2/

### ソースコードの展開 

まずソースコード OpenRTM-aist-X.X.X.tar.gz を適当なディレクトリーに展開します。

```
 $ tar xvzf OpenRTM-aist-X.X.X.tar.gz
 $ cd OpenRTM-aist-X.X.X
```

### ビルド 

OpenRTM-aist はパッケージのビルドに autoconf、automake を使用しています。
ビルドの仕方は、他の autoconf、automake を使用したパッケージと同様に行います。

```
 $ ./configure --prefix=/usr [options]
```

[options]で使用可能なオプションは

```
 $ ./configure --help
```

で参照してください。

### make

configure が正常に終了したことを確認してください。正常に終了したら make します。

```
 $ make
```

ビルドが正常に終了したら、ヘッダファイル、ライブラリ、ユーティリティコマンド群をインストールします。

```
 $  su
 # make install
```

以上で、ソースコードからのビルドおよびインストールは終了です。


## リポジトリのソースのビルド

OpenRTM-aist は開発に利用している subversion リポジトリを一般に公開しています。
リポジトリからチェックアウトしたソースコードからビルドを行うこともできます。

### 必要なツール

リポジトリからチェックアウトしたソースは configure スクリプトや Makefile.in が含まれていません。これらを生成するには、

- automake
- libtool
- autoconf

等のツールが必要ですので予めインストールしておきます。
これらの必要なツールをインストールする際、Ubuntuなどでは上で紹介した[「一括インストール・スクリプト」]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)を利用することもできます。

- https://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/

Ubuntuではpkg_install_ubuntu.shを以下のように実行することで、OpenRTM-aist 本体の開発を行う開発者向けのツール(automake等含む)などもまとめてインストールすることができます。

```
 # pkg_install_ubuntu.sh -l c++ -c 
```

### ソースのチェックアウト

ソースをリポジトリからチェックアウトします。

```
 $ svn co http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist
 A    OpenRTM-aist/include
 A    OpenRTM-aist/include/rtm
 A    OpenRTM-aist/AUTHORS
 A    OpenRTM-aist/src
 A    OpenRTM-aist/src/ext
 A    OpenRTM-aist/src/ext/artlinux
 中略
 A    OpenRTM-aist/examples/Templates/PanTilt.xml
 A    OpenRTM-aist/INSTALL.jp
  U   OpenRTM-aist
 Checked out revision 2009.
```

### autogen.shの実行
チェックアウトすると、OpenRTM-aist というディレクトリーができているはずですので、そのディレクトリーに入ります。

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

build ディレクトリーの下に autogen というシェルスクリプトがあることを確認し、このスクリプトを実行します。
実行には、数分程度の時間がかかることがあります。

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

autogen の実行により、configure が OpenRTM-aist ディレクトリー内にできているはずですので、以降は通常のソースからのビルドと同様に、configur & make でビルドします。

```
 $ ls -l configure
 -rwxr-xr-x  1 n-ando  n-ando  812893 Jul  6 05:56 configure*
 $ ./configure --prefix=/usr
 $ make
```

### make dist

**make dist** を行うことで openrtm.org で配布しているようなソースのパッケージを作成することもできます。
また、make dist では Windows 上でビルド可能なソースコードのパッケージも同時に作成します。
ただし、make dist を行うには、doxygen や latex、qkc等、さらに追加のコマンドが必要となります。

```
 $ make dist
 数分程度かかる
 $ ls -l OpenRTM-aist*
 -rw-r--r--  1 n-ando  n-ando  9266837 Apr  7 09:53 OpenRTM-aist-1.0.0-win32.zip
 -rw-r--r--  1 n-ando  n-ando  4831099 Apr  7 09:53 OpenRTM-aist-1.0.0.tar.bz2
 -rw-r--r--  1 n-ando  n-ando  7258796 Apr  7 09:53 OpenRTM-aist-1.0.0.tar.gz
 $
```

生成されたソースパッケージはそれぞれ以下の通りです。

- OpenRTM-aist-1.0.0-win32.zip: Windows 用ソース
- OpenRTM-aist-1.0.0.tar.gz: 汎用ソース (gzip 圧縮)
- OpenRTM-aist-1.0.0.tar.bz2: 汎用ソース (bzip 圧縮)



