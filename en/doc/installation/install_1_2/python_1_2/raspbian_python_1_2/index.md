---
layout: page
title: raspbianへのインストール
---
<br>
<a>No English version available.
</a>

<!-- node/6924-->
<!-- Title: Raspbianへのインストール -->


#contents

Python版OpenRTM-aistはRaspberry Pi用Raspbianl用debパッケージが提供されています。
Raspbianへの対応およびそのバージョンは、予告なしに変更または停止されることがありますので、あらかじめご了承ください。

## 対応バージョン

現在パッケージが用意されているRaspbianのバージョンは

- Buster

です。

## SDカードの準備

### OSイメージのダウンロード
以下のリンクからRasbianのイメージ(「Raspbian Buster with desktop and recommended software」のイメージを推奨しますが、必要に応じて他のイメージを選択してもかまいません)をダウンロードし、解凍し、SDカードに書き込みます。SDカードの容量は4GB以上はあったほうがよいでしょう。
- [Raspbian Downloads](https://www.raspberrypi.org/downloads/raspbian/)

### SDカードへの書き込み
SDカードへの書き込み方法については [RPi Easy SD Card Setup](http://elinux.org/RPi_Easy_SD_Card_Setup) を参照してください。

このリンクではいくつかの方法が説明されています。そのうちのいくつかの概要を示すと:

#### Windowsの場合
- [Win32 Disk Imager](https://forest.watch.impress.co.jp/docs/review/1067836.html)などを利用して書き込みます。

Windowsを用いる方法の方がLinuxやMac OSを用いるより簡単なので、初心者にはWindowsを用いる方法を推奨します。

#### LinuxやMac OSの場合
- ’’dd’’コマンドを以下のように利用して書き込みます。

```
 $ sudo dd of=/dev/<SDカードのデバイスファイル> if=<ダウンロード・解凍したイメージファイル> bs=4M status=progress
 $ sudo sync
```

上記コマンドによるSDカードへの書き込みはかなり長い時間を必要とします。(数分から10数分)。また、SDカードのデバイスファイル名を見つけるには
```
 $ df -h
```
と入力し、表示されるデバイスのサイズからどのデバイスがSDカードかを見つけます。例えば、現在Rasbianがインストールされている16GBのSDカードを用いている場合、あるデバイスが14GBのデバイスとして表示され、そのデバイスが/dev/sdf7と表示されます。他にも/dev/sdf5、/dev/sdf6などの後尾の数字だけが違うデバイスが表示されます。これらがSDカードで使われているデバイス名となります。これらのデバイス全て以下のようにumountしてください。
```
 $ umount /dev/sdf5
 $ umount /dev/sdf6
 $ umount /dev/sdf7
```

その後、上記の’’dd’’コマンドを実行しますが、この例でのデバイスファイル名は/dev/sdfになります。


## OpenRTM-aist-Pythonのインストール

openrtm.orgが提供するインストール・スクリプト**pkg_install_raspbian.sh**を指定のURLからダウンロードし、root 権限で実行します。このスクリプトでは必要なパッケージを順次apt-getを用いてインストールしていきます。

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。一括インストール・スクリプトをダウンロードして
```
 $ sudo sh pkg_install_raspbian.sh -l python --yes
```
でインストールできます。

一括インストールスクリプトのダウンロードや詳しいインストール方法、指定可能なオプションの種類につきましては、「[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)」のページをご確認ください。

## rtshellのインストール
RTCをRaspbianにインストールしてそのホスト上からローカルにRTCをコントロールしたい場合にはrtshellが必要です。一括インストールスクリプトを用いてrtshellをインストールしてください。Raspbianではpkg_install_raspbian.shが置いてあるディレクトリで
```
 $ sudo sh pkg_install_raspbian.sh -l rtshell --yes
 $ sudo rtshell_post_install
```

でインストールできます。

## インストールの確認
インストールを確認します。

```
 $ dpkg -l 'openrt*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
    状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリガ待ち/(T)トリガ保留
    / エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)
    / 名前                        バージョン   アーキテクチ 説明
 +++-===========================-============-============-===============================================
 ii  openrtm-aist-python         1.2.1-0      armhf        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm-aist-python-doc     1.2.1-0      all          Documentation for openrtm-aist-python
 ii  openrtm-aist-python-example 1.2.1-0      armhf        OpenRTM-aist-Python examples
```

rtshellのインストールも確認します。

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

## パッケージの詳細
各パッケージの内容は以下の通りです。

### openrtm-aist-python

- コマンド

```
 /usr/bin/rtcd_python
 /usr/bin/rtcprof_python
```

- OpenRTM-aist 本体の Python モジュール

```
 usr/lib/python2.7/dist-packages/OpenRTM-aist/*
```

- OpenRTM-aist用Python検索パスファイル

```
 /usr/lib/python2.7/dist-packages/OpenRTM_aist.ph
```

- ユーティリティ

```
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/__init__.py
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtc-template/*
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtcd/*
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtcprof/*
 /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtm-naming/*
```

<!-- /usr/lib/python2.7/dist-packages/OpenRTM_aist_Python-1.2.0.egg-info -->

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
 /usr/local/lib/python2.7/dist-packages/rtctree/*
 /usr/local/lib/python2.7/dist-packages/rtshell/*
 /usr/local/lib/python2.7/dist-packages/rtsprofile/*
```

- パッケージ情報
```
 /usr/local/lib/python2.7/dist-packages/rtctree_aist-4.2.0.egg-info/*
 /usr/local/lib/python2.7/dist-packages/rtshell_aist-4.2.2.dist-info/*
 /usr/local/lib/python2.7/dist-packages/rtsprofile_aist-4.1.2.dist-info/*
```


