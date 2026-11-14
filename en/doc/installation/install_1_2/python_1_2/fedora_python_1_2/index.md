---
layout: page
title: fedoraへのインストール
---
<br>
<a>No English version available.
</a>


<!-- Title: Fedoraへのインストール -->
現在、1.2系のOpenRTM-aistはFedoraの対応が不完全です。よって、本ページの情報はあくまでも参考情報として使用してください。

Python版OpenRTM-aistはFedora Linuxで利用可能なRPMパッケージが提供されています。
対応しているFedora Linuxのバージョンは、ダウンロードページから確認できます。
Fedora Linuxへの対応およびそのバージョンは、予告なしに変更または停止されることがありますので、あらかじめご了承ください。

Fedora Linuxへのインストールの方法には大きく分けて以下の二種類のインストール方法があります。
- openrtm.orgが提供する一括インストールスクリプトを使用
- yumパッケージマネージャを使用

#contents

## 一括インストール・スクリプト

openrtm.orgが提供するインストール・スクリプト**pkg_install_fedora.sh**をダウンロードページからダウンロードし、root権限で実行します。
このスクリプトは、必要なパッケージを順次yumを用いてインストールしていきます。

OpenRTM-aistを開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。一括インストール・スクリプトをダウンロードして

```
 sudo sh pkg_install_fedora.sh -l python --yes
```
でインストールできます。
一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種類につきましては、「[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)」のページをご確認ください。

## OpenRTPのインストール
一般的なUbuntu/Debian環境での開発にはRTC BuilderやRTSystem Editorを使用しますが、その場合にはOpenRTPが必要ですので、一括インストールスクリプトを用いてOpenRTPをインストールしてください。Ubuntuではpkg_install_ubuntu.shが置いてあるディレクトリで
```
 $ sudo sh ./pkg_install_fedora.sh -l openrtp --yes
```
と入力するとOpenRTPをインストールできます。

現状Fedora用一括インストールスクリプトでは-l pythonでPython用の環境をインストールした後に、-l openrtpをインストールした場合OpenRTPの実行に必要なファイルが一部インストールされないという問題がありますので上記実行後
```
 $ sudo yam install OpenRTM-aist
```
としてOpenRTM-aistをインストールしてください。

## JDK8のインストール

OpenRTP(RTSystem EditorやRTC Builderなど)の実行にはJDK8相当のJava環境が必要です。現時点でFedoraの環境では、一括インストールスクリプトがFedoraのrpmリポジトリよりOpenJDK8をインストールします。他のJDK8をインストールしたい場合は下記のリンクを参照してください。なお、rtshell/rtctree/rtsprofileの使用にはJDKは必要ありませんのでOpenRTPを使わない場合にはJDK8をインストールする必要はありません。 JDK8の入手やインストールについては以下を参照してください。
- [JDK8のインストール]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

## rtshellのインストール
制御用コンピューター・システムが小規模の場合など、CUIでRTCを制御したい場合にはOpenRTPのRTSystemEditor相当の機能をCUIから実行できるようなツールとしてrtshellと呼ばれるツールが提供されています。rtshellのインストールはターミナル上で一括インストールスクリプトを用いて、一括インストールスクリプト・ファイルが置かれているディレクトリで以下のように入力します。

```
 $ sudo sh pkg_install_fedora.sh -l rtshell --yes
```
<!-- $ sudo rtshell_post_install　現在動作しない -->

## yumとpipを使う方法

### /etc/yum.repos.d/openrtm.repoの作成

openrtm.orgではyumから利用可能なパッケージリポジトリを提供しています。
ただし、デフォルトのパッケージリポジトリには含まれていませんので、yumの設定を変更する必要があります。

以下のような設定を記録したファイル**/etc/yum.repos.d/openrtm.repo**を作成しておきます。作成には通常root権限が必要です。

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

### yumによるインストール

openrtm.repoを作成したら、次の手順でインストールを行います。
途中、いくつかの応答を求められるので、**y**を入力しながら完了させます。

- OpenRTM-aist-Pythonのインストール

```
 $ sudo yum install gcc-c++ python
 $ sudo yum install omniORB omniORB-devel omniORB-doc omniORB-servers omniORB-utils
 $ sudo yum install OpenRTM-aist-Python OpenRTM-aist-Python-doc OpenRTM-aist-Python-example
```

- OpenRTPのインストール

```
 $ sudo yum install OpenRTP
 $ sudo yum install OpenRTM-aist
```

- rtshellのインストール

```
 $ sudo pip3 install rtshell-aist
```
<!-- $ sudo rtshell_post_install 現在動作しない -->

### インストールの確認

以下のコマンドでインストールの確認ができます。

- OpenRTPもインストールしている場合
```
 $ rpm -qa OpenRT*
 OpenRTM-aist-devel-1.2.0-0.fc29.x86_64
 OpenRTM-aist-Python-1.2.0-0.29.x86_64
 OpenRTM-aist-Python-example-1.2.0-0.29.x86_64
 OpenRTP-1.2.0-1.fc29.x86_64
 OpenRTM-aist-1.2.0-0.fc29.x86_64
 OpenRTM-aist-Python-doc-1.2.0-0.29.x86_64
```

- OpenRTPをインストールしていない場合
```
 $ rpm -qa OpenRT*
 OpenRTM-aist-Python-1.2.0-0.29.x86_64
 OpenRTM-aist-Python-example-1.2.0-0.29.x86_64
 OpenRTM-aist-Python-doc-1.2.0-0.29.x86_64
```

- rtshellのインストールは
```
 $ pip3 show rtshell-aist
 Name: rtshell-aist
 Version: 4.2.2
 Summary: Shell commands for managing RT Components and RT Systems.
 Home-page: http://github.com/gbiggs/rtshell
 Author: Geoffrey Biggs and contributors
 Author-email: geoffrey.biggs@aist.go.jp
 License: LGPL3
 Location: /usr/local/lib/python3.7/dist-packages
 Requires: rtctree-aist, rtsprofile-aist
```
と確認できます。

## パッケージの詳細
各パッケージの内容は以下の通りです(64bit版Fedoraの場合)

### OpenRTM-aist-Python

- コマンド
```
 /usr/bin/rtcd_python
 /usr/bin/rtcprof_python
```

- OpenRTM-aist 本体の Python モジュール
```
 usr/lib/python3.7/site-packages/OpenRTM-aist/*
```

- OpenRTM-aist用Python検索パスファイル
```
 /usr/lib/python3.7/site-packages/OpenRTM_aist.ph
```

- ユーティリティ
```
 /usr/lib/python3.7/site-packages/OpenRTM_aist/utils/__init__.py
 /usr/lib/python3.7/site-packages/OpenRTM_aist/utils/rtc-template/*
 /usr/lib/python3.7/site-packages/OpenRTM_aist/utils/rtcd/*
 /usr/lib/python3.7/site-packages/OpenRTM_aist/utils/rtcprof/*
 /usr/lib/python3.7/site-packages/OpenRTM_aist/utils/rtm-naming/*
```

### openrtm-aist-python-example

```
 /usr/share/openrtm-1.2/components/python/__init__.py
 /usr/share/openrtm-1.2/components/python/rtcd.conf
 /usr/share/openrtm-1.2/components/python/components.conf
 /usr/share/openrtm-1.2/components/python/AutoControl/*
 /usr/share/openrtm-1.2/components/python/AutoTest/*
 /usr/share/openrtm-1.2/components/python/Composite/*
 /usr/share/openrtm-1.2/components/python/ConfigSample/*
 /usr/share/openrtm-1.2/components/python/ExtTrigger/*
 /usr/share/openrtm-1.2/components/python/MobileRobotCanvas/*
 /usr/share/openrtm-1.2/components/python/SeqIO/*
 /usr/share/openrtm-1.2/components/python/SimpleIO/*
 /usr/share/openrtm-1.2/components/python/SimpleService/*
 /usr/share/openrtm-1.2/components/python/Slider_and_Motor/*
 /usr/share/openrtm-1.2/components/python/Templates/*
 /usr/share/openrtm-1.2/components/python/Throughput/*
 /usr/share/openrtm-1.2/components/python/TkJoyStick/
 /usr/share/openrtm-1.2/components/python/TkLRFViewer/*
```

### openrtm-aist-python-doc

- クラスリファレンス(英語)
```
 /usr/share/openrtm-1.2/doc/python/ClassReference-en/html/_async_8py.html
 /usr/share/openrtm-1.2/doc/python/ClassReference-en/html/_buffer_base_8py.html
 中略
 /usr/share/openrtm-1.2/doc/python/ClassReference-en/html/uuid_8py.html
```
- クラスリファレンス(日本語)
```
 /usr/share/openrtm-1.2/doc/python/ClassReference-jp/html/_async_8py.html
 /usr/share/openrtm-1.2/doc/python/ClassReference-jp/html/_buffer_base_8py.html
 中略
 /usr/share/openrtm-1.2/doc/python/ClassReference-jp/html/uuid_8py.html 
```

### OpenRTM-aist
openrtm-aistにはランタイムライブラリとコマンド群が含まれています。

- サンプル設定ファイル
```
 /etc/rtc.conf.sample
```

- コマンド
```
 /usr/bin/rtcd
 /usr/bin/rtcprof
 /usr/bin/rtm-config
 /usr/bin/rtm-naming
```

- ライブラリ
```
 /usr/lib64/libRTC-1.2.0.so
 /usr/lib64/libRTC.a
 /usr/lib64/libRTC.la
 中略
 /usr/lib64/librtmManipulator.so.0.0.0
 /usr/lib64/openrtm-1.2/ec/FileNameservice.la
 /usr/lib64/openrtm-1.2/ec/FileNameservice.so
 中略
 /usr/lib64/openrtm-1.2/ssl/SSLTransport.so.0.0.0
```


### OpenRTM-aist-devel
openrtm-aist-devには、開発に必要なコマンド群とヘッダが含まれています。

- コマンド
```
 /usr/bin/coil-config
 /usr/bin/rtc-template
 /usr/bin/rtm-skelwrapper
```

- ヘッダ
```
 /usr/include/coil-1.2/coil/Affinity.h
 /usr/include/coil-1.2/coil/Allocator.h
 中略
 /usr/include/coil-1.2/coil/stringutil.h
 /usr/include/openrtm-1.2/rtm/BufferBase.h
 /usr/include/openrtm-1.2/rtm/BufferStatus.h
 中略
 /usr/include/openrtm-1.2/rtm/version.txt
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
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt/RTPreemptEC.h
 /usr/include/openrtm-1.2/rtm/ext/ec/rtpreempt/rtc.conf.sample
 /usr/include/openrtm-1.2/rtm/ext/local_service/nameservice_file
 /usr/include/openrtm-1.2/rtm/ext/local_service/nameservice_file/FileNameservice.h
 /usr/include/openrtm-1.2/rtm/ext/logger/fluentbit_stream/FluentBit.h
 /usr/include/openrtm-1.2/rtm/ext/logger/fluentbit_stream/fluentbit.conf
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/Logger.hh
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/Logger.idl
 中略
 /usr/include/openrtm-1.2/rtm/ext/sdo/logger/LoggerStub.h
```

- IDLおよびスタブ・スケルトン


```
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserver.idl
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserverConsumer.h
 中略
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/ComponentObserverStub.h
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredEC.hh
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredEC.idl
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredECDynSK.cc
 /usr/include/openrtm-1.2/rtm/ext/ec/logical_time/idl/LogicalTimeTriggeredECSK.cc
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserver.hh
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserver.idl
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserverDynSK.cc
 /usr/include/openrtm-1.2/rtm/ext/sdo/observer/idl/ComponentObserverSK.cc
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.hh
 /usr/include/openrtm-1.2/rtm/idl/BasicDataType.idl
 中略
 /usr/include/openrtm-1.2/rtm/idl/SharedMemoryStub.h
 /usr/include/openrtm-1.2/rtm/idl/device_interfaces/AIO.idl
 /usr/include/openrtm-1.2/rtm/idl/device_interfaces/ActArray.idl
 中略
 /usr/include/openrtm-1.2/rtm/idl/device_interfaces/Ranger.idl
```

- ライブラリ

```
 /usr/lib64/openrtm-1.2/cmake/OpenRTMConfig.cmake
 /usr/lib64/openrtm-1.2/py_helper/README_gen.py
 /usr/lib64/openrtm-1.2/py_helper/cxx_gen.py
 中略
 /usr/lib64/openrtm-1.2/py_helper/yat.py
 /usr/lib64/pkgconfig/libcoil.pc
 /usr/lib64/pkgconfig/openrtm-aist.pc
```

### OpenRTP
OpenRtpでは大量のファイルがインストールされるため、ここではリストしません。必要に応じて
```
 $ rpm -ql  OpenRTP
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

- コマンド本体
```
 /usr/local/lib/python3.7/dist-packages/rtctree/*
 /usr/local/lib/python3.7/dist-packages/rtshell/*
 /usr/local/lib/python3.7/dist-packages/rtsprofile/*
```

- パッケージ情報
```
 /usr/local/lib/python3.7/dist-packages/rtctree_aist-4.2.0.egg-info/*
 /usr/local/lib/python3.7/dist-packages/rtshell_aist-4.2.2.dist-info/*
 /usr/local/lib/python3.7/dist-packages/rtsprofile_aist-4.1.2.dist-info/*
```

