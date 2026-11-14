---
layout: page
title: fedoraへのインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: Fedoraへのインストール -->
#contents

Python 版 OpenRTM-aist は Fedora Linux で利用可能な RPM パッケージが提供されています。
対応している Fedora Linux のバージョンは、ダウンロードページから確認できます。
Fedora Linux への対応およびそのバージョンは、予告なしに変更または停止されることがありますので、予めご了承ください。

<!-- ※  OpenRTM-aist 1.2.0版以降、一括インストール・スクリプト対応予定です。 -->

Fedora Linuxへのインストールの方法には大きく分けて以下の二種類のインストール方法があります。

- openrtm.org が提供する一括インストールスクリプトを使用
- yum パッケージマネージャを使用

## 一括インストール・スクリプト

openrtm.org が提供するインストール・スクリプト **pkg_install_fedora.sh** をダウンロードページからダウンロードし、root 権限で実行します。このスクリプトは、必要なパッケージを順次 yum でインストールしていきます。

<!-- -[[パッケージインストールスクリプト:http://www.openrtm.org/OpenRTM-aist/download/install_scripts/]] -->
<!-- -[[一括インストールスクリプト:http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_fedora.sh]] -->

- [一括インストールスクリプト](http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_fedora.sh)

OpenRTM-aist を開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。
<!-- 初めて OpenRTM-aist をインストールしてみる方にお勧めします。 -->
オプションを指定することで、目的に合わせたパッケージをインストールできるようになったので、
初めて OpenRTM-aist をインストールしてみる方にもソースをコンパイルしてみる方にもお勧めします。

ただし、OpenRTM-aist 関係のすべてのパッケージをインストールするので、必要ないものもインストールされる可能性があります。
詳しく理解している人は、手動でインストールした方がよいでしょう。

詳しいオプションやパッケージの種類につきましては、[こちら]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)をご確認ください。

<!-- また、次のオプションとパッケージは未対応です。yumコマンドでインストールしてください。 -->

<!-- - オプション ''all''  (OpenRTM-aist 1.2.0版以降対応予定) -->
<!-- - OpenRTM-aist-1.1.2-RELEASE -->
<!-- - rtshell -->

<!-- 以下、一括インストールスクリプトを使用したインストールの手順です。 -->

<!-- > wget [pkg_install_python_fedora.sh のダウンロード URL ] -->
<!-- > su -->
<!-- # sh pkg_install_fedora.sh -l python -->
<!-- 途中、いくつかの質問をたずねられるので、''y'' あるいは ''Y'' を入力しながら完了させる。 -->
<!-- オプション " --yes" を追加することで省略も可能。 -->

## yum を使う方法

### /etc/yum.repos.d/openrtm.repo の作成

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
 # yum install python
 # yum install omniORB-servers omniORBpy omniORBpy-devel omniORBpy-standard
 # yum install OpenRTM-aist-Python OpenRTM-aist-Python-example
```

### インストールの確認

最後に以下のコマンドでインストールの確認をします。

```
 # rpm -qa | grep  OpenRTM-aist-Python
 OpenRTM-aist-Python-example-1.1.0-RELEASE0.fcx.i386
 OpenRTM-aist-Python-1.1.0-RELEASE0.fcx.i386
```


## パッケージの詳細
各パッケージの内容は以下の通りです。

### OpenRTM-aist-Python
OpenRTM-aist-Python には Python モジュールとコマンド群が含まれています。

- コマンド
```
 /usr/bin/rtcprof_python
 /usr/bin/rtcd_python
```

<!-- -サンプル設定ファイル -->
<!-- /usr/lib/python<version>/site-packages/OpenRTM_aist/examples/rtc.conf.sample -->

- OpenRTM-aist 本体の Python モジュール
```
 /usr/lib/python<version>/site-packages/OpenRTM_aist/*
```

- OpenRTM-aist のユーティリティモジュール
```
 /usr/lib/python<version>/site-packages/OpenRTM_aist/utils/rtcprof
 /usr/lib/python<version>/site-packages/OpenRTM_aist/utils/rtcd
 /usr/lib/python<version>/site-packages/OpenRTM_aist/utils/rtc-template
 /usr/lib/python<version>/site-packages/OpenRTM_aist/utils/rtm-naming
```

### OpenRTM-aist-Python-example
OpenRTM-aist-Python-example には RTC のサンプルが含まれています。

- サンプル
```
 /usr/share/openrtm-1.1/example/python/SimpleIO/
 /usr/share/openrtm-1.1/example/python/SimpleService/
 中略
```


以上、インストールが終了しましたら、[動作確認]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/test_linux_python_1_1)へ進みましょう。

