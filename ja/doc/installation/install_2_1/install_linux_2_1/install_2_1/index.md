---
layout: page
title: インストール
---

<!-- Title: インストール -->

<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="100;" align="right"></a></div>


OpenRTM-aistは、UbuntuやDebian GNU Linuxにおいて利用可能なdebパッケージが提供されています。
<!-- ２.０は現在、Debian、Ubuntu、Raspbian OSのディストリビューションに対応しています。 -->


#contents

2.1 は現在、Ubuntu 22.04, 24.04 (各amd64, arm64）に対応しています。
Ubuntu/Debian GNU Linuxへのサポートバージョンや対応の有無は、予告なしに変更されることがありますので、あらかじめご了承ください。

## 2.1系での変更点

新しく [SSM通信機能]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ssm_comm_use) をインストールできるようになりました。<br>
SSMライブラリを静的リンクしているので、別途SSMをインストール必要はありません。openrtm2-ssm-tpのdebパッケージで下記がインストールされます。

```
 usr/
 ├── bin
 │   ├── killssm
 │   ├── lsssm
 │   ├── psssm
 │   ├── ssm-advance-player
 │   ├── ssm-coordinator
 │   ├── ssm-date
 │   ├── ssm-graph
 │   ├── ssm-logger
 │   ├── ssm-monitor
 │   ├── ssm-player
 │   ├── ssm-proxy
 │   ├── ssm-transporter
 │   └── topssm
 ├── etc
 │   └── transport
 │       └── rtc.ssm.conf
 └── share
     └── openrtm-2.1
         └── transport
             └── SSMTransport.so
```

この機能は次の項で説明している「一括インストールスクリプト」をオプション無しで実行した場合はインストールされません。<br>
オプションとして「-l c++ --ssm」と指定するとインストールできます。 --help で確認できます。

## 一括インストールスクリプト

2.0系のインストールは、下記をシェルプロンプトに貼り付けて実行してください。　C++版、 Python版、 Java版、 OpenRTP(amd64のみ)、 rtshell、JDK8 がインストールされます。　スクリプトはローカルに保存されません。<br>
※スクリプトの実行で、Javaの複数バージョンがインストールされても、Java８ 使用に切り替わっています

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

この実行により以下のパッケージがインストールされます。

```
 $ dpkg -l | grep openrt
 ii  openrtm2:arm64                         2.1.0-0             arm64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:arm64                  2.1.0-0              arm64       OpenRTM-aist headers for development
 ii  openrtm2-doc                             2.1.0-0              all             Documentation for openrtm2
 ii  openrtm2-example:arm64            2.1.0-0             arm64       OpenRTM-aist examples
 ii  openrtm2-idl:arm64                     2.1.0-0             arm64       OpenRTM-aist idls for development
 ii  openrtm2-java:arm64                  2.1.0-0             arm64       OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-example:arm64     2.1.0-0            arm64        OpenRTM-aist-Java examples
 ii  openrtm2-naming:arm64              2.1.0-0            arm64        OpenRTM-aist name server launcher
 ii  openrtm2-python3                       2.1.0-0            arm64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-example          2.1.0-0            arm64        OpenRTM-aist-Python examples
```

デフォルトのpipバージョン利用で、 rtshellのインストールに失敗します。<br>
インストールスクリプトが表示している黄文字のメッセージに従い、　/etc/pip.conf へ（存在しなければ 新規作成して）下記を追記して下さい。

```
 $ vi /etc/pip.conf
 [global]
 break-system-packages = true
```

上記設定後に再度インストールスクリプトを実行するとrtshellをインストールできます。

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python        2.1.0
 rtctree-aist                       4.2.5
 rtshell-aist                       4.2.10
 rtsprofile-aist                    4.1.6
```

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。 help は下記で確認できます。

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) --help
```

インストールされるパッケージの詳しい内容は「[OpenRTM-aist-2.1 debパッケージの詳しい内容]({{ site.baseurl }}/ja/doc/installation/install_2_1/install_linux_2_1/install_debpackages_workcontent_2_1) 」で確認できます。

## ROS用パッケージのインストール

2.1系ではROS通信機能用パッケージをインストールできます。（ROS2用)  <br>
ここでは、ROS2 をインストールしている環境へのパッケージインストール方法を説明します。

help に記載しているように、ROSパッケージインストールオプションは以下で対応しています。<br>

'''
[-e ros2|all] [--ros2]
'''

すでにインストールスクリプトをオプション無しで実行済みで、追加でROS2用パッケージを追加インストールする場合は、「-l c++ --ros2」で可能です。

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l c++ --ros2
```

最初からROS2用パッケージも加えてすべてインストールしたい場合は、「 -l all --ros2」で可能です。

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l all --ros2
```

インストールされたパッケージを確認します。

```
 $ dpkg -l | grep openrt
 ii  openrtm2:amd64                          2.1.0-0       amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:amd64                    2.1.0-0       amd64        OpenRTM-aist headers for development
 ii  openrtm2-doc                               2.1.0-0       all               Documentation for openrtm2
 ii  openrtm2-example:amd64             2.1.0-0       amd64        OpenRTM-aist examples
 ii  openrtm2-idl:amd64                      2.1.0-0       amd64        OpenRTM-aist idls for development
 ii  openrtm2-java:amd64                   2.1.0-0       amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-example:amd64      2.1.0-0      amd64        OpenRTM-aist-Java examples
 ii  openrtm2-naming:arm64               2.1.0-0      arm64        OpenRTM-aist name server launcher
 ii  openrtm2-python3                         2.1.0-0      amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-example            2.1.0-0      amd64        OpenRTM-aist-Python examples
 ii  openrtm2-ros2-tp:amd64               2.1.0-0      amd64        OpenRTM-aist extension ROS2 package
 ii  openrtp2:amd64                            2.1.0-0      amd64        OpenRTP, Open RT Platform distributed by AIST
```


