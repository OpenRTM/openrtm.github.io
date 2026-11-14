---
layout: page
title: qnx  へのインストール
---

<!-- Title: QNX  へのインストール -->
<div align="right"><a href="qnx_logo.png"><img src="qnx_logo.png" width="15%;" align="right"></a></div>

#contents


## QNX

QNX（キューエヌエックス、またはキューニックス）は主に組み込みシステム向けに販売されている、商用リアルタイム OS です。
POSIX 準拠の UNIX系 OSで、組込み用 OS でありながら一般的な UNIX 同様プロセス型のオペレーティング・システムです。
カーネルはマイクロカーネルであり、様々な機能はサーバとしてモジュール化され、用途に応じて必要なサーバのみを動作させるため、コンパクトなシステムを構成することができます。
x86ファミリ、MIPS、PowerPC、SH-4、ARM、StrongARM、XScale など様々な CPU 上で動作可能であり、さらに機能安全規格 IEC61508 に準拠し認証を取得しているため、安全認証が必要な安全関連系にも利用することができます。

QNX には教育機関向けの無償ライセンスプログラムもあり、大学などでは比較的気軽に利用することができます。


- [QNX](http://www.qnx.com)
- [QNX-in-Educationプログラム](http://www.qnx.com/company/education/?lang=jp#apply)
- [QNXダウンロード](http://www.qnx.com/download/group.html?programid=20905)

## pkgsrc

pkgsrc は、UNIX 用のパッケージマネジメントシステムの一つであり、FreeBSD の ports collection から派生し、現在は NetBSD のパッケージマネジメント・システムとして利用されています。
pkgsrc自体は、特定の OS に依存するものではなく、NetBSD、Solaris、Linux、Mac OS X、FreeBSD、OpenBSD、IRIX, BSD/OS、AIX、Interix、DragonFlyBSD、OSF/1、HP-UX、QNX、Haiku、MINIX 3、Illumosといった UNIX系の様々な OS上で利用できます。

- [pkgsrc](http://www.netbsd.org/docs/software/packages.html)

### pkgsrc for QNX

QNX にはパッケージ管理システムはなく、QNX のユーザーフォーラムにおいて QNX 用の pkgsrc がメンテナンスされています。

- [QNX Community pkgsrc Project](http://community.qnx.com/sf/projects/pkgsrc/)
- [Binary packages:ftp]()（リンク切れです）


OS をインストール後、pkgsrc をリポジトリからチェックアウトするなどして、システムに配置します。(リポジトリへのアクセスには、QNX forum のアカウントが必要になります。)
svnリポジトリからのチェックアウトは大変時間がかかるので、[pkgsrc_HEAD650_r396.tgz](pkgsrc_HEAD650_r396.tgz) をダウンロードして利用することもできますが、事前に pkgsrc の最新バージョンをチェックすることをおすすめします。

- [QNX アカウント](https://www.qnx.com/account/login.html)
- [QNX フォーラム](https://www.qnx.com/account/index.html)
- [bootstrap](http://community.qnx.com/sf/wiki/do/viewPage/projects.pkgsrc/wiki/Bootstrap)
- [pkgsrc HEAD650(r396)のアーカイブ(.svn削除済み)](pkgsrc_HEAD650_r396.tgz)
- [pkgsrc HEAD650(r396)のアーカイブ(.svn含む)](pkgsrc_HEAD650_r396.tgz)


```
 # cd /usr/
 # svn checkout --username <username> http://community.qnx.com/svn/repos/pkgsrc/HEAD_650/pkgsrc
 # (cd pkgsrc/bootstrap && ./bootstrap)
 # (cd pkgsrc/misc/figlet && bmake install)
 # pkg_info
 または
 # cd /usr
 # tar xvzf <somewhere>/pkgsrc_HEAD650_r396.tgz
 # (cd pkgsrc/bootstrap && ./bootstrap)
 # (cd pkgsrc/misc/figlet && bmake install)
 # pkg_info
```

## OpenRTM-aist の pkgsrc によるインストール

pkgsrc は、バイナリパッケージによるインストールと、ソースからビルドしてインストールする方法があります。
すべてのパッケージがバイナリで提供されているわけではないので、必要に応じてソースからビルドする必要があります。

### OpenRTM.org の pkgsrc リポジトリ

OpenRTM-aist は、openrtm.org の以下の URL においてバイナリパッケージを提供しています。

- http://www.openrtm.org/pub/pkgsrc/packages/QNX/i386/6.5.0/All/

OpenRTM-aist で必要な omniORB も上述の[配布サイト:ftp]()（リンク切れです）にはバイナリパッケージが無いため、openrtm.org で提供されています。

### インストール

インストール方法は以下のとおりです。

- 環境変数 PKG_PATH に http://www.openrtm.org/pub/pkgsrc/packages/QNX/i386/6.5.0/All をセット
  - 6.5.0 は QNX のバージョンですので適宜読み替えてください
- pkg_add -v OpenRTM-aist-1.1.0-RELESE で OpenRTM-aist をインストール
  - omniORB も同時にインストールされます

```
 # export PKG_PATH=http://www.openrtm.org/pub/pkgsrc/packages/QNX/i386/6.5.0/All
 # pkg_add -v OpenRTM-aist-1.1.0-RELESE
 1.1.0-RELESE の部分は適宜インストールするバージョンに置き換えてください。
 Running install with PRE-INSTALL for omniORB-4.1.6.
 bin/omkdepend
 bin/omnicpp
   : omniORB のインストールが始まる
 man/man1/omniidl.1
 Running install with PRE-INSTALL for omniORB-4.1.6.
 Package omniORB-4.1.6 registered in /var/db/pkg/omniORB-4.1.6
   : OpenRTM-aist のインストールが始まる
 lib/libcoil.so
 lib/libcoil.la
 lib/libcoil-1.1.0.so
 　:
 share/openrtm-1.1/doc/IDLReference-en/html/unionSDOPackage_1_1Numeric.html
 etc/rtc.conf.sample
 Package OpenRTM-aist-1.1.0-RELEASE registered in /var/db/pkg/OpenRTM-aist-1.1.0-RELEASE
 #
 # pkg_info|grep OpenRTM
 OpenRTM-aist-1.1.0-RELEASE RT-Middleware and OMG RTC framework
```

以上でインストールは終了です。

## テスト

/usr/pkg/share/openrtm-1.1/examples の下にサンプルプログラムがインストールされています。
これを利用して OpenRTM-aist の動作確認を行います。

### ネームサーバーの起動

まず、ネームサーバーを起動します。

```
 # rtm-naming
 あるいは
 # cp /usr/pkg/share/examples/rc.d/omninames /etc/rc.d/
 # chmod 755 /etc/rc.d/omninames
 # /etc/rc.d/omninames
```

後者では、omninames の起動スクリプトを rc ディレクトリー (/etc/rc.d) にコピーしてからそれを起動しています。
なお、このスクリプトはネームサーバーの停止を行うこともできます。

```
 # /etc/rc.d/omninames stop
```

### ConsoleOut

まず、ConsoleOut コンポーネントを起動してみます。
下の例ではホームディレクトリーに tmp ディレクトリーを作り、そこにコピーしてから実行しています。

```
 # cd ; mkdir tmp ; cd tmp
 # cp -r /usr/pkg/share/openrtm-1.1/example .
 # cd example
 # ./ConsoleOutComp
 succeed.
 =================================================
  Component Profile
 -------------------------------------------------
 InstanceID:     ConsoleOut0
 Implementation: ConsoleOut
 Description:    Console output component
  :
 =================================================
 Port0 (name): ConsoleOut0.in
 -------------------------------------------------
 - properties -
 port.port_type: DataInPort
 dataport.data_type: IDL:RTC/TimedLong:1.0
 dataport.subscription_type: Any
 dataport.dataflow_type: push,pull
 dataport.interface_type: corba_cdr
```
 -------------------------------------------------

### ConsoleIn

```
 # cd ; cd tmp/example
 # ./ConsoleInComp
 Creating a component: "ConsoleIn"....succeed.
 =================================================
  Component Profile
 -------------------------------------------------
 InstanceID:     ConsoleIn0
 Implementation: ConsoleIn
 Description:    Console input component
  :
 =================================================
 Port0 (name): ConsoleIn0.out
 -------------------------------------------------
 - properties -
 port.port_type: DataOutPort
 dataport.data_type: IDL:RTC/TimedLong:1.0
 dataport.subscription_type: flush,new,periodic
 dataport.dataflow_type: push,pull
 dataport.interface_type: corba_cdr
 -------------------------------------------------
  :
 Please input number:
```

ここで、別の PC 上で RTSystemEditor を起動し、ポートを接続、アクティベートします。
ConsoleIn のプロンプトに対して数字を入力すると、ConsoleOut から出力されます。

<div align="center"><a href="qnx_test.png"><img src="qnx_test.png" width="70%;"></a></div>
<div align="center"><strong>QNX上で動作する ConsoleIn と ConsoleOut コンポーネント</strong></div>

<hr>
- [QNXでのビルド手順(OpenRTM-aist 1.2)](./qnx_build_proc_1_2)


