---
layout: page
title: fedoraへのインストール
---

<!-- Title: Fedoraへのインストール -->
<div align="right"><a href="fedora_logo.png"><img src="fedora_logo.png" width="15%;" align="right"></a></div>

C++版 OpenRTM-aist は Fedora Linux で利用可能な RPM パッケージが提供されています。
対応している Fedora Linux のバージョンは、ダウンロードページから確認できます。
Fedora Linux への対応およびそのバージョンは、予告なしに変更または停止されることがありますので、予めご了承ください。

※ OpenRTM-aist 1.2.0版以降、一括インストール・スクリプト対応予定です。

Fedora Linux へのインストールの方法には大きく分けて以下の二種類のインストール方法があります。
- openrtm.org が提供する一括インストールスクリプトを使用
- yum パッケージマネージャを使用

#contents

## 一括インストール・スクリプト

openrtm.org が提供するインストール・スクリプト **pkg_install_fedora.sh** をダウンロードページからダウンロードし、root 権限で実行します。
このスクリプトは、必要なパッケージを順次 yum でインストールしていきます。

<!-- -[[パッケージインストールスクリプト:http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_fedora.sh]] -->

<!-- -[[新パッケージインストールスクリプト:http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_fedora.sh]] -->

OpenRTM-aist を開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。
<!-- //初めて OpenRTM-aist をインストールしてみる方にお勧めします。 -->
オプションを指定することで、目的に合わせたパッケージをインストールできるようになったので、
初めて OpenRTM-aist をインストールしてみる方にもソースをコンパイルしてみる方にもお勧めします。

ただし、OpenRTM-aist 関係のすべてのパッケージをインストールするので、必要ないものもインストールされる可能性があります。
詳しく理解している人は、手動でインストールした方がよいでしょう。

詳しいオプションやパッケージの種類につきましては、「[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)」のページをご確認ください

<!-- また、次のパッケージは対応していませんのでyumコマンドでインストールしてください。 -->

<!-- - OpenRTM-aist-1.1.2-RELEASE -->
<!-- - rtshell -->

<!-- 以下、一括インストールスクリプトを使用したインストールの手順です。 -->

<!-- > wget [pkg_install_fedora.sh のダウンロードURL] -->
<!-- > su -->
<!-- # sh pkg_install_fedora.sh -l c++ -->
<!-- //途中、いくつかの質問をたずねられるので、''y'' あるいは ''Y'' を入力しながら完了させる。 -->
<!-- //オプション "--yes" を追加することで、省略も可能。 -->

## yum を使う方法

### /etc/yum.repos.d/openrtm.repoの作成

openrtm.org では yum から利用可能なパッケージリポジトリを提供しています。
ただし、デフォルトのパッケージリポジトリには含まれていませんので、yum の設定を変更する必要があります。

以下のような設定を記録したファイル **/etc/yum.repos.d/openrtm.repo** を作成しておきます。作成には通常 root 権限が必要です。

```
 [openrtm]
 name=Fedora $releasever - $basearch
 failovermethod=priority
 baseurl=http://openrtm.org/pub/Linux/Fedora/releases/$releasever/Fedora/$basearch/os/Packages
 enabled=1
 gpgcheck=0
 gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora file:///etc/pki/rpm-gpg/RPM-GPG-KEY
```
<div align="center"><strong>/etc/yum.repos.d/openrtm.repo</strong></div>

### yum によるインストール

openrtm.repo を作成したら、次の手順でインストールを行います。
途中、いくつかの応答を求められるので、**y** を入力しながら完了させます。

```

 > su
 # yum install gcc-c++ python
 # yum install omniORB omniORB-devel omniORB-doc omniORB-servers omniORB-utils
 # yum install OpenRTM-aist OpenRTM-aist-devel OpenRTM-aist-doc OpenRTM-aist-example
```

### インストールの確認

最後に以下のコマンドでインストールの確認をします。

```
 # rpm -q OpenRTM-aist
 OpenRTM-aist-1.0.0-0.fcX
```


## パッケージの詳細
各パッケージの内容は以下の通りです

### OpenRTM-aist
openrtm-aist にはランタイムライブラリとコマンド群が含まれています。

- サンプル設定ファイル
```
 /etc/rtc.conf.sample
```

- ライブラリ
```
 /usr/lib/libRTC-1.0.0.so.0
 /usr/lib/libRTC-1.0.0.so.0.0.4
 /usr/lib/libRTC.a
 /usr/lib/libRTC.la
 /usr/lib/libRTC.so
 /usr/lib/libcoil.a
 /usr/lib/libcoil.la
 /usr/lib/libcoil.so
 /usr/lib/libcoil.so.0
 /usr/lib/libcoil.so.0.0.0
```

### OpenRTM-aist-devel
openrtm-aist-dev には、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/coil-config
 /usr/bin/rtc-template
 /usr/bin/rtcd
 /usr/bin/rtcprof
 /usr/bin/rtm-config
 /usr/bin/rtm-naming
 /usr/bin/rtm-skelwrapper
```

- ヘッダ
```
 /usr/include/coil/Allocator.h
 /usr/include/coil/Async.h
 中略
 /usr/include/coil/memory.h
 /usr/include/coil/stringutil.h
 中略
 /usr/include/rtm/BufferBase.h
 /usr/include/rtm/BufferStatus.h
 中略
 /usr/include/rtm/Typename.h
 /usr/include/rtm/config_rtc.h
```

- IDL およびスタブ・スケルトン
```
 /usr/include/rtm/idl/BasicDataType.hh
 /usr/include/rtm/idl/BasicDataType.idl
 中略
 /usr/include/rtm/idl/device_interfaces/RFID.idl
 /usr/include/rtm/idl/device_interfaces/Ranger.idl
```

- ライブラリ
```
 /usr/lib/openrtm-1.1/py_helper/README_gen.py
 /usr/lib/openrtm-1.1/py_helper/README_gen.pyc
 中略
 /usr/lib/openrtm-1.1/py_helper/yat.pyc
 /usr/lib/openrtm-1.1/py_helper/yat.pyo
 /usr/lib/pkgconfig/libcoil.pc
 /usr/lib/pkgconfig/openrtm-aist.pc
```


### OpenRTM-aist-doc
openrtm-aist-doc には、日本語と英語のクラスリファレンス、IDL インターフェース定義リファレンスが含まれています。

- クラスリファレンス
```
 /usr/share/openrtm-1.1/docs/ClassReference/html/ConnectorBase_8h-source.html
 /usr/share/openrtm-1.1/docs/ClassReference/html/RTC_8h.html
 中略
 /usr/share/openrtm-1.1/docs/ClassReference/html/FactoryInit_8h-source.html
```

- IDL リファレンス
```
 /usr/share/openrtm-1.1/docs/IDLReference/html/BasicDataType_8idl-source.html
 中略
 /usr/share/openrtm-1.1/docs/IDLReference/html/interfaceOpenRTM_1_1InPortCdr-members.html
```

- クラスリファレンス(英語)
```
 /usr/share/openrtm-1.1/docs/ClassReference-en/html/ConnectorBase_8h-source.html
 /usr/share/openrtm-1.1/docs/ClassReference-en/html/RTC_8h.html
 中略
 /usr/share/openrtm-1.1/docs/ClassReference-en/html/FactoryInit_8h-source.html
```

- IDL リファレンス(英語)
```
 /usr/share/openrtm-1.1/docs/IDLReference-en/html/BasicDataType_8idl-source.html
 /usr/share/openrtm-1.1/docs/IDLReference-en/html/structRTC_1_1FsmProfile.html
 中略
 /usr/share/openrtm-1.1/docs/IDLReference-en/html/interfaceOpenRTM_1_1InPortCdr-members.html
```

### OpenRTM-aist-example
openrtm-aist-example にはスタンドアロン RTC、ローダブル RTC それぞれのサンプルと、サンプル RTC のソースが含まれています。

- サンプル(スタンドアロン RTC)
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

- サンプル(ローダブル RTC)
```
 /usr/share/openrtm-1.1/examples/rtc/MyServiceConsumer.so.0.0.0
 /usr/share/openrtm-1.1/examples/rtc/SeqIn.so.0.0.0
 中略
 /usr/share/openrtm-1.1/examples/rtc/ConfigSample.so.0.0.0
 /usr/share/openrtm-1.1/examples/rtc/ConsoleOut.so.0.0.0
```

