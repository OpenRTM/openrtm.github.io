---
layout: page
title: 
---

<!-- Title: Ubuntu/Debianへのインストール -->
<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="100;" align="right"></a></div>

Python版のOpenRTM-aistは、UbuntuやDebian GNU Linuxで利用可能なdebパッケージが提供されています。
対応しているディストリビューションのバージョンは、ダウンロードページで確認できます。
Ubuntu/Debian GNU Linuxへのサポートバージョンや対応の有無は、予告なしに変更されることがありますので、あらかじめご了承ください。

#contents

## 一括インストールスクリプト
openrtm.orgが提供するインストール・スクリプト**pkg_install_ubuntu.sh**または**pkg_install_debian.sh**を指定のURLからダウンロードし、root権限で実行します。このスクリプトでは必要なパッケージを順次apt-getを用いてインストールしていきます。

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。

一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種類につきましては、「[一括インストールスクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script)」のページをご確認ください。<br>
<span style="color:red;">※最新バージョンが「1.2.2」である場合は、オプション指定で「1.2.1」のインストール、「1.2.2」から「1.2.1」へのダウングレードができます。</span>;

一括インストールスクリプトは、ダウンロードした後、ダウンロード先ディレクトリに移動し、

Ubuntuの場合は

```
 $ sudo sh pkg_install_ubuntu.sh -l python --yes
```
Debianの場合はsuでroot権限を得た後に

```
 # sh pkg_install_debian.sh -l python --yes
```
でインストールできます。




## OpenRTPのインストール
一般的なUbuntu/Debian環境での開発にはRTCBuilderやRTSystemEditorを使用しますが、その場合にはOpenRTPが必要です。一括インストールスクリプトを用いてOpenRTPをインストールしてください。Ubuntuではpkg_install_ubuntu.shが置いてあるディレクトリで

Ubuntuの場合は
```
 $ sudo sh ./pkg_install_ubuntu.sh -l openrtp --yes
```

Debianの場合はsuでroot権限を得た後に
```
 # sh pkg_install_debian.sh -l openrtp --yes
```

と入力するとOpenRTPをインストールできます。

## JDK8のインストール

OpenRTP(RTSystemEditorやRTCBuilderなど)の実行にはJDK8相当のJava環境が必要です。(デフォルトの環境でJDK8がインストールされている場合もありますが、Ubuntu 18.04ではJDK11がインストールされているため、JDK8のインストールが必要です。)　なお、rtshell/rtctree/rtsprofileの使用にはJDKは必要ありませんのでOpenRTPを使わない場合にはJDK8をインストールする必要はありません。JDK8の入手やインストールについては以下を参照してください。
- [JDK8のインストール]({{ site.baseurl }}/ja/doc/installation/common/install_jdk8)

## rtshellのインストール
制御コンピュータが小規模のシステムの場合など、CUIでRTCを制御したい場合にはOpenRTPのRTSystemEditor相当の機能をCUIから実行できるようなツールとしてrtshellと呼ばれるツールが提供されています。rtshellのインストールは一括インストールスクリプトを用いて、一括インストールスクリプト・ファイルが置かれているディレクトリで

Ubuntuの場合は
```
 $ sudo sh pkg_install_ubuntu.sh -l rtshell --yes
 $ sudo rtshell_post_install
```
Debianの場合はsuでroot権限を得た後に
```
 # sh pkg_install_debian.sh -l rtshell --yes
 # rtshell_post_install
```

でインストールできます。

## インストールの確認
- openrtpをインストールした場合

インストールを確認します。(下記は1.2.1の例です。)

```
 $ dpkg -l 'openrt*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
    状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリガ待ち/(T)トリガ保留
    / エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
    / 名前                          バージョン          アーキテクチャ      説明
 +++-=============================-===================-===================-===============================================================
 ii  openrtm-aist:amd64            1.2.1-0             amd64               OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-dev:amd64        1.2.1-0             amd64               OpenRTM-aist headers for development
 ii  openrtm-aist-idl:amd64        1.2.1-0             amd64               OpenRTM-aist idls for development
 ii  openrtm-aist-python           1.2.1-0             amd64               OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-python-doc       1.2.1-0             all                 Documentation for openrtm-aist-python
 ii  openrtm-aist-python-example   1.2.1-0             amd64               OpenRTM-aist-Python examples
 ii  openrtp:amd64                 1.2.1-0             amd64               OpenRTP, Open RT Platform distributed by AIST
```

- openrtpの代わりにrtshellをインストールした場合

インストールを確認します。(下記は1.2.1の例です。)

```
 $ dpkg -l 'openrt*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
    状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリガ待ち/(T)トリガ保留
    / エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
    / 名前                          バージョン          アーキテクチャ      説明
 +++-=============================-===================-===================-===============================================================
 ii  openrtm-aist-python           1.2.1-0             amd64               OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-python-doc       1.2.1-0             all                 Documentation for openrtm-aist-python
 ii  openrtm-aist-python-example   1.2.1-0             amd64               OpenRTM-aist-Python examples
```

rtshellのインストールは
```
 $ pip show rtshell-aist
 Name: rtshell-aist
 Version: 4.2.2
 Summary: Shell commands for managing RT Components and RT Systems.
 Home-page: http://github.com/gbiggs/rtshell
 Author: Geoffrey Biggs and contributors
 Author-email: geoffrey.biggs@aist.go.jp
 License: LGPL3
 Location: /usr/local/lib/python2.7/dist-packages
 Requires: rtctree-aist, rtsprofile-aist
```
と確認できます。


## パッケージの詳細
各パッケージの内容は以下の通りです。

### openrtm-aist
openrtm-aist にはランタイムライブラリとコマンド群が含まれています。

- コマンド
```
 /usr/bin/rtcd
 /usr/bin/rtcprof
 /usr/bin/rtm-config
 /usr/bin/rtm-naming
```


- ライセンスなど
```
 /usr/share/doc/openrtm-aist/changelog.gz
 /usr/share/doc/openrtm-aist/README.Debian
 /usr/share/doc/openrtm-aist/README
 /usr/share/doc/openrtm-aist/README.jp
 /usr/share/doc/openrtm-aist/copyright
 /usr/share/doc/openrtm-aist/changelog.Debian.gz
```

- 設定ファイルサンプル
```
 /usr/etc/rtc.conf.sample
```

- ライブラリ
  - 32bit
```
 /usr/lib/i386-linux-gnu/libRTC-X.X.X.so
 /usr/lib/i386-linux-gnu/libRTC.a
 /usr/lib/i386-linux-gnu/libRTC.la
 /usr/lib/i386-linux-gnu/libcoil-X.X.X.so
 /usr/lib/i386-linux-gnu/libcoil.a
 /usr/lib/i386-linux-gnu/librtmCamera.a
 /usr/lib/i386-linux-gnu/librtmCamera.la
 /usr/lib/i386-linux-gnu/librtmCamera.so.X.X.X
 /usr/lib/i386-linux-gnu/librtmManipulator.a
 /usr/lib/i386-linux-gnu/librtmManipulator.la
 /usr/lib/i386-linux-gnu/librtmManipulator.so.X.X.X
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/FileNameservice.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/FileNameservice.so.X.X.X
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.a
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.so.X.X.X
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.so.X.X.X
 /usr/lib/i386-linux-gnu/openrtm-1.2/ssl/SSLTransport.la
 /usr/lib/i386-linux-gnu/openrtm-1.2/ssl/SSLTransport.so.X.X.X
 /usr/lib/i386-linux-gnu/pigconfig/openrtm-aist.pc
```
  - 64bit
```
 /usr/lib/x86_64-linux-gnu/libRTC-X.X.X.so
 /usr/lib/x86_64-linux-gnu/libRTC.a
 /usr/lib/x86_64-linux-gnu/libRTC.la
 /usr/lib/x86_64-linux-gnu/libcoil-X.X.X.so
 /usr/lib/x86_64-linux-gnu/libcoil.a
 /usr/lib/x86_64-linux-gnu/librtmCamera.a
 /usr/lib/x86_64-linux-gnu/librtmCamera.la
 /usr/lib/x86_64-linux-gnu/librtmCamera.so.X.X.X
 /usr/lib/x86_64-linux-gnu/librtmManipulator.a
 /usr/lib/x86_64-linux-gnu/librtmManipulator.la
 /usr/lib/x86_64-linux-gnu/librtmManipulator.so.X.X.X
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/FileNameservice.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/FileNameservice.so.X.X.X
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.a
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ec/LogicalTimeTriggeredEC.so.X.X.X
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.a
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/sdo/LoggerConsumer.so.X.X.X
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ssl/SSLTransport.la
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/ssl/SSLTransport.so.X.X.X
 /usr/lib/x86_64-linux-gnu/pigconfig/openrtm-aist.pc
```

### openrtm-aist-dev
openrtm-aist-devには、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/coil-config
 /usr/bin/rtc-template
 /usr/bin/rtm-skelwrapper
```

- ライセンスなど
```
 /usr/share/doc/openrtm-aist-dev/changelog.Debian.gz
 /usr/share/doc/openrtm-aist-dev/changelog.gz
 /usr/share/doc/openrtm-aist-dev/copyright
```

- ヘッダなど
```
 /usr/include/coil-1.2/coil/Affinity.h
 /usr/include/coil-1.2/coil/Allocator.h
 中略
 /usr/include/coil-1.2/coil/stringutil.h
 /usr/include/openrtm-1.2/rtm/BufferBase.h
 /usr/include/openrtm-1.2/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-1.2/rtm/config_rtc.h
 /usr/include/openrtm-1.2/rtm/ext/CameraCommonInterface.hh
 /usr/include/openrtm-1.2/rtm/ext/CameraCommonInterface.idl
 中略
 /usr/include/openrtm-1.2/rtm/ext/ManipulatorCommonInterface_MiddleStub.h
 /usr/include/openrtm-1.2/rtm/ext/ec/artlinux/ArtExecutionContext.h
 /usr/include/openrtm-1.2/rtm/ext/ec/artlinux/rtc.conf.sample
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/LogicalTimeTriggeredEC.h
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/LogicalTimeTriggeredEC.idl
 中略
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/LogicalTimeTriggeredECStub.h
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredEC.hh
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredEC.idl
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredECDynSK.cc
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredECSK.cc
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt/RTPreemptEC.h
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt/rtc.conf.sample
 /usr/include/openrtm-1.2/rtm/ext/local_service/nameservice_file/FileNameservice.h
 /usr/include/openrtm-1.2/rtm/ext/logger/fluentbit_stream/FluentBit.h
 /usr/include/openrtm-1.2/rtm/ext/logger/fluentbit_stream/fluentbit.conf
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/Logger.hh
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/Logger.idl
 中略
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/LoggerStub.h
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserver.idl
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserverConsumer.h
 中略
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserverStub.h
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserver.hh
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserver.idl
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserverDynSK.cc
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserverSK.cc
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.hh
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.idl
 中略
 /usr/include/openrtm-1.2/rtm/idl/device_interfaces/Ranger.idl
 /usr/include/openrtm-1.2/rtm/version.h
 /usr/include/openrtm-1.2/rtm/version.txt
```

- ライブラリ・その他
 - 32bit

```
 /usr/lib/i386-linux-gnu/openrtm-1.2/cmake/OpenRTMConfig.cmake
 /usr/lib/i386-linux-gnu/openrtm-1.2/py_helper/README_gen.py
 /usr/lib/i386-linux-gnu/openrtm-1.2/py_helpver/cxx_gen.py
 中略
 /usr/lib/i386-linux-gnu/openrtm-1.2/py_helpver/yat.py
 /usr/lib/i386-linux-gnu/pkgconfig/libcoil.pc
 
```
 - 64bit

```
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/cmake/OpenRTMConfig.cmake
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/py_helper/README_gen.py
 /usr/lib/x86-64-linux-gnu/openrtm-1.2/py_helpver/cxx_gen.py
 中略
 /usr/lib/x86_64-linux-gnu/openrtm-1.2/py_helpver/yat.py
 /usr/lib/x86_64-linux-gnu/pkgconfig/libcoil.pc
```

### openrtm-aist-python3

OpenRTM-aist 1.2.2 からメインPythonバージョンが2系から3系へ変更されました。

- コマンド
```
 /usr/bin/rtcd_python3
 /usr/bin/rtcprof_python3
```

- OpenRTM-aist 本体の Python モジュール
```
 usr/lib/python3/dist-packages/OpenRTM-aist/*
```

- OpenRTM-aist用Python検索パスファイル
```
 /usr/lib/python3/dist-packages/OpenRTM_aist.ph
```

- ユーティリティ
```
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/__init__.py
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtc-template/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcd/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtcprof/*
 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtm-naming/*
```

### openrtm-aist-python3-example

```
 /usr/share/openrtm-1.2/components/python3/__init__.py
 /usr/share/openrtm-1.2/components/python3/rtcd.conf
 /usr/share/openrtm-1.2/components/python3/components.conf
 /usr/share/openrtm-1.2/components/python3/AutoControl/*
 /usr/share/openrtm-1.2/components/python3/AutoTest/*
 /usr/share/openrtm-1.2/components/python3/Composite/*
 /usr/share/openrtm-1.2/components/python3/ConfigSample/*
 /usr/share/openrtm-1.2/components/python3/ExtTrigger/*
 /usr/share/openrtm-1.2/components/python3/MobileRobotCanvas/*
 /usr/share/openrtm-1.2/components/python3/SeqIO/*
 /usr/share/openrtm-1.2/components/python3/SimpleIO/*
 /usr/share/openrtm-1.2/components/python3/SimpleService/*
 /usr/share/openrtm-1.2/components/python3/Slider_and_Motor/*
 /usr/share/openrtm-1.2/components/python3/Templates/*
 /usr/share/openrtm-1.2/components/python3/Throughput/*
 /usr/share/openrtm-1.2/components/python3/TkJoyStick/
 /usr/share/openrtm-1.2/components/python3/TkLRFViewer/*
```

### openrtm-aist-python3-doc

- クラスリファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/python3/ClassReference-en/html/_async_8py.html
 /usr/share/openrtm-1.2/doc/python3/ClassReference-en/html/_buffer_base_8py.html
 中略
 /usr/share/openrtm-1.2/doc/python3/ClassReference-en/html/uuid_8py.html
```

- クラスリファレンス(日本語)
```
 /usr/share/openrtm-1.2/doc/python3/ClassReference-jp/html/_async_8py.html
 /usr/share/openrtm-1.2/doc/python3/ClassReference-jp/html/_buffer_base_8py.html
 中略
 /usr/share/openrtm-1.2/doc/python3/ClassReference-jp/html/uuid_8py.html 
```

### openrtp

openrtpでは大量のファイルがインストールされるため、ここではリストしません。必要に応じて

```
 $ dpkg -L openrtp
```
と入力して各自での確認をしてください。

### rtshell

- コマンド用スクリプト
```
 /usr/local/bin/rtact
 /usr/local/bin/rtcat
 /usr/local/bin/rtcheck
 /usr/local/bin/rtcomp
 /usr/local/bin/rtcon
 /usr/local/bin/rtconf
 /usr/local/bin/rtcryo
 /usr/local/bin/rtdeact
 /usr/local/bin/rtdel
 /usr/local/bin/rtdis
 /usr/local/bin/rtdoc
 /usr/local/bin/rtexit
 /usr/local/bin/rtfind
 /usr/local/bin/rtfsm
 /usr/local/bin/rtinject
 /usr/local/bin/rtlog
 /usr/local/bin/rtls
 /usr/local/bin/rtmgr
 /usr/local/bin/rtprint
 /usr/local/bin/rtpwd
 /usr/local/bin/rtreset
 /usr/local/bin/rtresurrect
 /usr/local/bin/rtshell_post_install
 /usr/local/bin/rtstart
 /usr/local/bin/rtstodot
 /usr/local/bin/rtstop
 /usr/local/bin/rtteardown
 /usr/local/bin/rtvlog
 /usr/local/bin/rtwatch
```

- コマンド本体 (下記はUbuntu20.04の例です。)
```
 /usr/local/lib/python3.8/dist-packages/rtctree/*
 /usr/local/lib/python3.8/dist-packages/rtshell/*
 /usr/local/lib/python3.8/dist-packages/rtsprofile/*
```

- パッケージ情報 (下記はUbuntu20.04の例です。)
```
 /usr/local/lib/python3.8/dist-packages/rtctree_aist-4.2.0.egg-info/*
 /usr/local/lib/python3.8/dist-packages/rtshell_aist-4.2.2.dist-info/*
 /usr/local/lib/python3.8/dist-packages/rtsprofile_aist-4.1.2.dist-info/*
```



