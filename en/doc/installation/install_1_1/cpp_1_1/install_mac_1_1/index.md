---
layout: page
title: mac os x への macports によるインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: Mac OS X への MacPorts によるインストール -->
<div align="right"><a href="osx_logo2.png"><img src="osx_logo2.png" width="15%;" align="right"></a></div>


C++版 OpenRTM-aist は Mac OS X 用のパッケージ管理ステム MacPorts で利用可能な ports が提供されています。
MacPorts への対応およびそのバージョンは、予告なしに変更または停止されることがありますので、予めご了承ください。

#contents


## MacPorts

MacPorts は Mac OS X 上で利用可能なオープンソースのパッケージ管理システムです。
MacPorts は FreeBSD の ports というパッケージ管理システムと同様に、ports と呼ばれるパッケージをビルドするためのレシピに基づき、自動でソースのダウンロード、パッチの適用、コンパイル、インストールまでを行ってくれるシステムです。
Mac OS X 用のパッケージ管理システムとしては他に Fink があります。

- [The MacPorts Project Official Homepage](http://www.macports.org/)

### MacPorts のインストール

MacPorts を利用するには、Apple の Xcodeおよび、X11 環境を予めインストールする必要があります。
Xcode および X11 は Mac OS X のインストールCD からインストールすることもできます。
詳細は、上記 MacPorts の Webページを参照してください。

MacPorts 自体は dmg パッケージ形式になっており、自分の Mac の OS のバージョンに合わせた dmg パッケージをダウンロード、インストールすることで簡単にインストールすることができます。
dmg パケージは MacPorts の Webページ、または下記リンクからダウンロードできます。

- [for Snow Leopard](http://distfiles.macports.org/MacPorts/MacPorts-1.9.1-10.6-SnowLeopard.dmg)
- [for Leoperd](http://distfiles.macports.org/MacPorts/MacPorts-1.9.1-10.5-Leopard.dmg)
- [for Tiger](http://distfiles.macports.org/MacPorts/MacPorts-1.9.1-10.4-Tiger.dmg)

## OpenRTM-aist ports によるインストール

Portfile のダウンロード、展開、ビルドを一括でおこなうスクリプトが以下に用意されています。

- [Portfile]()(No corresponding page available.)
- [インストールスクリプト]()(No corresponding page available.): ports.tgz のダウンロード、OpenRTM-aistのビルド・インストールまで自動で行います。

適当なディレクトリーで、以下のようにスクリプトを実行します。実行は一般ユーザーで構いません。ただし、途中で当該ユーザーのパスワードを聞かれることがあります。

```
 $ sh port_install100_mac.sh
 sh port_install.sh
 file:///Users/n-ando/ports/
 Getting Portfile from:  http://www.openrtm.org/pub/MacOSX/macports//ports.tgz
 --2010-07-27 23:21:06--  http://www.openrtm.org/pub/MacOSX/macports//ports.tgz
 Resolving www.openrtm.org (www.openrtm.org)... 182.48.18.55
 Connecting to www.openrtm.org (www.openrtm.org)|182.48.18.55|:80... connected.
 HTTP request sent, awaiting response... 200 OK
 Length: 3600 (3.5K) [application/x-gzip]
 Saving to: `ports.tgz.1'
 
 100%[================================================>] 3,600       --.-K/s   in 0.002s
 
 2010-07-27 23:21:06 (2.02 MB/s) - `ports.tgz' saved [3600/3600]
 
 x ports/
 x ports/devel/
 x ports/PortIndex
 x ports/PortIndex.quick
 x ports/devel/OpenRTM-aist/
 x ports/devel/OpenRTM-aist/Portfile
 x ports/devel/OpenRTM-aist/files/
 x ports/devel/OpenRTM-aist/Portfile~
 x ports/devel/OpenRTM-aist/files/patch-src-lib-rtm-InPortConsumer.h
 x ports/devel/OpenRTM-aist/files/patch-src-lib-coil-posix-coil-UUID.cpp
 x ports/devel/OpenRTM-aist/files/patch-src-lib-coil-posix-coil-Routing.cpp
 x ports/devel/OpenRTM-aist/files/patch-examples-SimpleService-Makefile.in
 x ports/devel/OpenRTM-aist/files/patch-examples-Composite-Makefile.in
 x ports/devel/OpenRTM-aist/files/patch-examples-ConfigSample-Makefile.in
 x ports/devel/OpenRTM-aist/files/patch-examples-SeqIO-Makefile.in
 x ports/devel/OpenRTM-aist/files/patch-examples-SimpleIO-Makefile.in
 x ports/devel/OpenRTM-aist/files/patch-src-lib-rtm-idl-Makefile.in
 Creating port index in /Users/n-ando/ports
 Adding port devel/OpenRTM-aist
 
 Total number of ports parsed:   1
 Ports successfully parsed:      1
 Ports failed:                   0
 Up-to-date ports skipped:       0
  
 Adding local ports repository entry to sources.conf
 # A password may be required for sudo. Input your password.
 Password:
 Installing OpemRTM-aist...it may take several minutes.
 # A password may be required for sudo. Input your password.
 --->  Computing dependencies for OpenRTM-aist
 --->  Fetching OpenRTM-aist
 --->  Verifying checksum(s) for OpenRTM-aist
 --->  Extracting OpenRTM-aist
 --->  Applying patches to OpenRTM-aist
 --->  Configuring OpenRTM-aist
 --->  Building OpenRTM-aist
 --->  Staging OpenRTM-aist into destroot
 --->  Installing OpenRTM-aist @1.0.0_2
 --->  Activating OpenRTM-aist @1.0.0_2
 --->  Cleaning OpenRTM-aist
 Cleaning local ports repository entry in sources.conf
 # A password may be required for sudo. Input your password.
 Password:
 $
```

ports は、依存関係を自動的に解決し、ビルドに必要なパッケージが入っていない場合には自動でそのパッケージのビルドも行いますので、多少時間がかかる場合があります。

### インストールの詳細

詳細は一括インストールシェルスクリプト port_installXXX_mac.sh に書いてあります。インストール手順は、おおよそ以下のようになっています。

- Portfile をダウンロードする
- Portfile を展開する
- sources.conf に展開した Portfile の場所を追記する
- port コマンドでビルド・インストールする

MacPorts では、port コマンドでインストールするよう指定されたパッケージを、設定ファイル sources.conf に記載されている特定の場所以下から探し出して、Porrtfile に従いソースをダウンロードしビルドを行います。



