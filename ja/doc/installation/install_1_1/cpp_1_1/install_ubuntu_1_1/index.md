---
layout: page
title: ubuntu/debianへのインストール
---

<!-- Title: Ubuntu/Debianへのインストール -->
<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="100;" align="right"></a></div>


C++版の OpenRTM-aist は、Ubuntu や Debian GNU Linux で利用可能な deb パッケージが提供されています。
対応しているディストリビューションのバージョンは、ダウンロードページから確認できます。
Ubuntu/Debian GNU Linux への対応およびそのバージョンは、予告なしに変更または停止されることがありますので、予めご了承ください。

インストールの方法には大きく分けて以下の2種類のインストール方法があります。

- openrtm.org が提供する一括インストールスクリプトを使用
- apt-get や synaptic パッケージマネージャを仕様

好みの方法でインストールしてください。

#contents

## 一括インストール・スクリプトを使う方法

openrtm.org が提供するインストール・スクリプト **pkg_install_ubuntu.sh** または **pkg_install_debian.sh** をダウンロードページからダウンロードし、root 権限で実行します。このスクリプトは、必要なパッケージを順次 apt-get でインストールしていきます。

<!-- -[[パッケージインストールスクリプト:http://www.openrtm.org/pub/OpenRTM-aist/cxx/install_scripts/]] -->
<!-- -[[ソースコードリポジトリの最新スクリプト:http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install100_ubuntu.sh]] -->

<!-- -[[一括インストールスクリプト(Ubuntu):http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_ubuntu.sh]] -->
<!-- -[[一括インストールスクリプト(Debian):http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_debian.sh]] -->

<!-- -[[一括インストールスクリプト(Ubuntu):http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_ubuntu.sh]] -->
<!-- -[[一括インストールスクリプト(Debian):http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_debian.sh]] -->

オプションを指定することで、目的に合わせたパッケージをインストールできるようになったので、
初めて OpenRTM-aist をインストールしてみる方にもソースをコンパイルしてみる方にもお勧めします。

<!-- ただし、OpenRTM-aist 関係のすべてのパッケージをインストールするので、必要ないものもインストールされる可能性があります。 -->
<!-- 詳しく理解している人は、手動でインストールした方がよいでしょう。 -->

一括インストールスクリプトのダウンロード、及び、詳しいインストール方法や、オプション・パッケージの種類につきましては、「[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)」のページをご確認ください。

<!-- 以下、一括インストールスクリプトを使用したインストールの手順です。 -->
<!-- （pkg_install_debian.sh のオプション設定も同じ） -->

<!-- > wget [pkg_install_ubuntu.sh のダウンロードURL] -->
<!-- > su -->
<!-- # ./pkg_install_ubuntu.sh -l c++ -->
<!-- //途中、いくつかの質問をたずねられるので、''y'' あるいは ''Y'' を入力しながら完了させる。 -->
<!-- //オプション "--yes" を追加することで、省略も可能。 -->

## apt-get を使う方法

### source.list の編集

openrtm.org では apt-get から利用可能なパッケージリポジトリを提供しています。ただし、デフォルトのパッケージリポジトリには含まれていませんので、apt-get の設定を変更する必要があります。

/etc/apt/sources.list に以下の行を追加します。

```
 > su
 # vi /etc/apt/sources.list # "sources.list" を編集
```

```
  deb http://openrtm.org/pub/Linux/ubuntu/ (code name) main
  または
  deb http://openrtm.org/pub/Linux/debian/ (code name) main
```

の1行を追加。"(code name)" の部分には以下の debian/ubuntu のバージョンに対応したコードネームを指定します。

<table class="table-alt">
  <tr>
    <td>バージョン</td>
    <td>code name</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Debian GNU Linux</td>
  </tr>
  <tr>
    <td>Debian 7.0</td>
    <td>wheezy</td>
  </tr>
  <tr>
    <td>Debian 8.0</td>
    <td>jessie</td>
  </tr>
  <tr>
    <td>Debian 9.0</td>
    <td>stretch</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Ubuntu</td>
  </tr>
  <tr>
    <td>Ubuntu 14.04 LTS</td>
    <td>trusty</td>
  </tr>
  <tr>
    <td>Ubuntu 16.04 LTS</td>
    <td>xenial</td>
  </tr>
  <tr>
    <td>Ubuntu 16.10</td>
    <td>yakkety</td>
  </tr>
  <tr>
    <td>Ubuntu 17.04</td>
    <td>zesty</td>
  </tr>
</table>

Ubuntun の過去・現在のバージョン/コードネームは、[https://wiki.ubuntu.com/Releases](https://wiki.ubuntu.com/Releases) から確認できます。

### apt-get によるインストール

次の手順でインストールを行います。途中、いくつかの応答を求められるので、
**y** を入力しながら完了させてください。

```
 # apt-get update
 # apt-get install gcc g++ make uuid-dev
 # apt-get install libomniorb4-dev omniidl
```
<!-- # apt-get install python-support (Debian 3.1 Sargeでのみ必要) -->
```
 # apt-get install openrtm-aist openrtm-aist-doc openrtm-aist-dev openrtm-aist-example
```

<!-- 新しい ubuntu では幾つかのパッケージ名が変更されているかもしれません。 -->
<!-- ( omniidl4 -> omniidl, omniorb4-nameserver -> omniorb-nameserver ) -->

なお、インストール済みの OpenRTM-aist を特定バージョンのまま保持したい場合には、**/etc/apt/preferences**を編集して以下の行を追加します。（この例では1.0系列にバージョンを固定します。）

```
 Package: OpenRTM-aist
 Pin: version 1.0.*
```

詳しくは
[http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.ja.html#s-pin](http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.ja.html#s-pin)
を参照してください。

### Launchpad/PPA のパッケージ

<div align="right"><a href="Launchpad_logo.png"><img src="Launchpad_logo.png" width="100; margin:20 20 20 20px;" align="right"></a></div>

Launchpad は Canonical Ltd. により開発・管理されている、オープンソースソフトウエア開発のためのウェブアプリケーション及びウェブサイト( https://launchpad.net/ )です。
Launchpad サイト内には有志による Ubuntu のパッケージリポジトリ: PPA (Private Package Archive)があり、誰でも自分のソフトウエアのパッケージを公開することができます。

OpenRTM-aist も PPA で Ubuntu 用のパッケージを公開しており、自由に利用することができます。
PPA 上の OpenRTM-aist パッケージを利用する利点は、自分が作成した RTC を PPA 上で公開する場合、依存関係に PPA上の OpenRTM-aist のパッケージを含めることができ、また第3者がその RTC をインストールする際には PPA 上でパッケージの依存関係を完結させることができる点です。

- [OpenRTM-aist@Launchpad](https://launchpad.net/`openrtm)`

以下、PPA上 の OpenRTM-aist のパッケージをインストールする手順を説明します。

#### PPA パッケージのインストール

PPA のパッケージインストールする方法は非常に簡単です。

まず、パッケージリポジトリに OpenRTM-aist の PPA のを追加します。OpenRTM-aist の PPAリポジトリ名は **openrtm/stable** です。

```
 $ sudo add-apt-repository ppa:openrtm/stable
```

パッケージデータベースをアップデート。

```
 $ sudo aptitude update
```

パッケージのインストールを行います。パッケージは、openrtm-aist(ランタイム)、openrtm-aist-dev(開発用ヘッダ)、openrtm-aist-doc(ドキュメント)、openrtm-aist-example(サンプル) の4種類の中から必要なものを選択しインストールします。

```
 $ sudo aptitude install openrtm-aist1.1 openrtm-aist1.1-dev openrtm-aist1.1-example
```

以上です。

#### OpenRTM-aist の PPAリポジトリ構成

OpenRTM-aist の PPAリポジトリは以下の3種類から構成されています。

<table class="table-alt">
  <tr>
    <th>リポジトリ名</th>
    <th>概要</th>
  </tr>
  <tr>
    <td>ppa:openrtm/stable</td>
    <td>基本リポジトリ。通常インストールするパッケージ。命名規則は <br> openrtm-aist[-]{dev,doc,example}: 最新版パッケージ <br> openrtm-aistX.Y[-]{dev,doc,example}: マイナーバージョン別パッケージ</td>
  </tr>
  <tr>
    <td>ppa:openrtm/archives</td>
    <td>アーカイブリポジトリ。過去のすべてのバージョンのパッケージ。命名規則は <br> openrtm-aistX.Y.Z[-]{dev,doc,example}: リビジョン別パッケージ</td>
  </tr>
  <tr>
    <td>ppa:openrtm/unstable</td>
    <td>不安定版リポジトリ。RC 版、ベータ版等のパッケージ。 命名規則は <br> openrtm-aistX.Y.ZrcW[-]{dev,doc,example}: リビジョン・RC番号別パッケージ</td>
  </tr>
</table>

### インストールの確認

インストールを確認します。

```
 $ dpkg -l 'openrtm*'
 Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Installed/Config-f/Unpacked/Failed-cfg/Half-inst/t-aWait/T-pend
 |/ Err?=(none)/Hold/Reinst-required/X=both-problems (Status,Err: uppercase=bad)
 ||/ Name           Version        Description
 +++-==============-==============-============================================
 ii  openrtm-aist   1.0.0-0        OpenRTM-aist runtime libraries and configura
 ii  openrtm-aist-d 1.0.0-0        Header files for OpenRTM-aist development
 pn  openrtm-aist-d <none>         (no description available)
 ii  openrtm-aist-e 1.0.0-0        OpenRTM-aist examples
```

## パッケージの詳細
各パッケージの内容は以下の通りです。

### openrtm-aist
openrtm-aist にはランタイムライブラリとコマンド群が含まれています。

- コマンド
```
 /usr/bin/rtcd
 /usr/bin/rtm-naming
```

- ライセンス等
```
 /usr/share/doc/openrtm-aist/changelog.gz
 /usr/share/doc/openrtm-aist/README.Debian
 /usr/share/doc/openrtm-aist/README
 /usr/share/doc/openrtm-aist/README.jp
 /usr/share/doc/openrtm-aist/NEWS.gz
 /usr/share/doc/openrtm-aist/copyright
 /usr/share/doc/openrtm-aist/changelog.Debian.gz
```

- 設定ファイルサンプル
```
 /usr/etc/rtc.conf.sample
```

- ライブラリ
```
 /usr/lib/libRTC-X.X.X.so.X.X.X
 /usr/lib/libRTC.a
 /usr/lib/libRTC.la
 /usr/lib/libRTC.so
 /usr/lib/libRTC-X.X.X.so.X
```

  - 1.1.1版では、Debian は7.0以降、Ubuntu は12.04以降において、32/64bit のパスはそれぞれ以下のようになっています。

```
 ***** 32bit
 /usr/lib/i386-linux-gnu/libRTC-X.X.X.so.X.X.X
 /usr/lib/i386-linux-gnu/libRTC.a
 /usr/lib/i386-linux-gnu/libRTC.la
 ***** 64bit
 /usr/lib/x86_64-linux-gnu/libRTC-X.X.X.so.X.X.X
 /usr/lib/x86_64-linux-gnu/libRTC.a
 /usr/lib/x86_64-linux-gnu/libRTC.la
```

### openrtm-aist-dev
openrtm-aist-devには、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/rtc-template
 /usr/bin/rtm-config
 /usr/bin/rtm-skelwrapper
```

- ライセンス等
```
 /usr/share/doc/openrtm-aist-dev/changelog.gz
 /usr/share/doc/openrtm-aist-dev/copyright
 /usr/share/doc/openrtm-aist-dev/changelog.Debian.gz
```

- ヘッダ
```
 /usr/include/rtm/DefaultPeriodicTask.h
 /usr/include/rtm/OutPortPullConnector.h
 中略
 /usr/include/rtm/ExecutionContextBase.h
 /usr/include/rtm/Manager.h
 /usr/include/coil/OS.h
 /usr/include/coil/UUID.h
 中略
 /usr/include/coil/Properties.h
```

- ライブラリ・その他
```
 /usr/lib/openrtm-1.1/py_helper/cxx_svc_impl.py
 /usr/lib/openrtm-1.1/py_helper/profile_gen.py
 中略
 /usr/lib/openrtm-1.1/py_helper/gen_base.py
 /usr/lib/openrtm-1.1/py_helper/yat.py
 /usr/lib/pkgconfig/libcoil.pc
```

  - 1.1.1版 では、Debian は 7.0以降、Ubuntu は 12.04以降において、32/64bit のパスはそれぞれ以下のようになっています。

```
 ***** 32bit
 /usr/lib/i386-linux-gnu/openrtm-1.1/py_helper/cxx_svc_impl.py
 /usr/lib/i386-linux-gnu/pkgconfig/libcoil.pc
 ***** 64bit
 /usr/lib/x86_64-linux-gnu/openrtm-1.1/py_helper/cxx_svc_impl.py
 /usr/lib/x86_64-linux-gnu/pkgconfig/libcoil.pc
```

### openrtm-aist-example
openrtm-aist-example にはスタンドアロン RTC、ローダブル RTC それぞれのサンプルと、サンプル RTC のソースが含まれています。

- サンプル(スタンドアロンRTC)
```
 /usr/share/openrtm-1.1/examples/ConsoleOutComp
 /usr/share/openrtm-1.1/examples/ConsoleInComp
 中略
```

- サンプル(ソース)
```
 /usr/share/openrtm-1.1/examples/src/Composite/README.Motor
 /usr/share/openrtm-1.1/examples/src/Composite/Makefile.Sensor
 /usr/share/openrtm-1.1/examples/src/Composite/Motor.cpp
 中略
 /usr/share/openrtm-1.1/examples/src/SimpleService/Makefile.MyServiceProvider
 /usr/share/openrtm-1.1/examples/src/SimpleService/rtc.conf
```

- サンプル(ローダブルRTC)
```
 /usr/share/openrtm-1.1/examples/rtc/MyServiceConsumer.so.0.0.0
 /usr/share/openrtm-1.1/examples/rtc/SeqIn.so.0.0.0
 中略
 /usr/share/openrtm-1.1/examples/rtc/ConfigSample.so.0.0.0
 /usr/share/openrtm-1.1/examples/rtc/ConsoleOut.so.0.0.0
```

- ライセンス等
```
 /usr/share/doc/openrtm-aist-example/changelog.gz
 /usr/share/doc/openrtm-aist-example/copyright
 /usr/share/doc/openrtm-aist-example/changelog.Debian.gz
```

### openrtm-aist-doc
openrtm-aist-doc には、日本語と英語のクラスリファレンス、IDL インターフェース定義リファレンスが含まれています。

- クラスリファレンス
```
 /usr/share/openrtm-1.1/doc/ClassReference/html/ConnectorBase_8h-source.html
 /usr/share/openrtm-1.1/doc/ClassReference/html/RTC_8h.html
 中略
 /usr/share/openrtm-1.1/doc/ClassReference/html/FactoryInit_8h-source.html
```

- IDL リファレンス
```
 /usr/share/openrtm-1.1/doc/IDLReference/html/BasicDataType_8idl-source.html
 中略
 /usr/share/openrtm-1.1/doc/IDLReference/html/interfaceOpenRTM_1_1InPortCdr-members.html
```

- クラスリファレンス(英語)
```
 /usr/share/openrtm-1.1/doc/ClassReference-en/html/ConnectorBase_8h-source.html
 /usr/share/openrtm-1.1/doc/ClassReference-en/html/RTC_8h.html
 中略
 /usr/share/openrtm-1.1/doc/ClassReference-en/html/FactoryInit_8h-source.html
```

- IDL リファレンス(英語)
```
 /usr/share/openrtm-1.1/doc/IDLReference-en/html/BasicDataType_8idl-source.html
 /usr/share/openrtm-1.1/doc/IDLReference-en/html/structRTC_1_1FsmProfile.html
 中略
 /usr/share/openrtm-1.1/doc/IDLReference-en/html/interfaceOpenRTM_1_1InPortCdr-members.html
```

- ライセンス等
```
 /usr/share/doc/openrtm-aist-doc/changelog.gz
 /usr/share/doc/openrtm-aist-doc/copyright
 /usr/share/doc/openrtm-aist-doc/changelog.Debian.gz
```


## 履歴

- 2010-07-26 23:24:55 +0900: 初期バージョン
- 2012-07-06 01:34:30 +0900: PPAを利用したインストールについて追加
- 2015-02-20 17:00:00 +0900: 1.1.1版リリースに合わせて修正
