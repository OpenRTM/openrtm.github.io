---
layout: page
---
<!-- Title: インストール -->

<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="100;" align="right"></a></div>


OpenRTM-aistは、UbuntuやDebian GNU Linuxにおいて利用可能なdebパッケージが提供されています。
<!-- ２.０は現在、Debian、Ubuntu、Raspbian OSのディストリビューションに対応しています。 -->


#contents

2.0 は現在、Ubuntu 18.04, 20.04 (各amd64, arm64）に対応しています。
Ubuntu/Debian GNU Linuxへのサポートバージョンや対応の有無は、予告なしに変更されることがありますので、あらかじめご了承ください。

## 2.0系での変更点

C++と OpenRTP は 1.2系と2.0系の共存が可能となりました。　この対応で、インストールに関しては下記が変更となっています。

- 2.0系のdebパッケージ名を変更しました
- Python と Java は1.2系と2.0系の共存はできません
  - 一括インストールスクリプトを使用すれば、インストール済みの異なるバージョンを自動でアンインストールします
- 1.2系と2.0系の一括インストールスクリプトを分けました
  - 1.2系のインストール : pkg_install_ubuntu.sh
  - 2.0系のインストール : openrtm2_install_ubuntu.sh

また、インストールスクリプト（1.2系、2.0系どちらも）は、ダウンロードからインストールまでの一括処理に対応しました。

## 一括インストールスクリプト

2.0系のインストールは、下記をシェルプロンプトに貼り付けて実行してください。　C++版、 Python版、 Java版、 OpenRTP(amd64のみ)、 rtshell、JDK8 がインストールされます。　スクリプトはローカルに保存されません。<br>
※スクリプトの実行で、Javaの複数バージョンがインストールされても、Java８ 使用に切り替わっています

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

この実行により以下のdebパッケージと、pipによりrtshellがインストールされます。

```
 $ dpkg -l | grep openrt
 ii  openrtm2:amd64                          2.0.0-0                  amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:amd64                    2.0.0-0                  amd64        OpenRTM-aist headers for development
 ii  openrtm2-doc                               2.0.0-0                  all               Documentation for openrtm2
 ii  openrtm2-example:amd64             2.0.0-0                  amd64        OpenRTM-aist examples
 ii  openrtm2-idl:amd64                      2.0.0-0                  amd64        OpenRTM-aist idls for development
 ii  openrtm2-java:amd64                   2.0.0-0                  amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-doc                        2.0.0-0                  all               Documentation for openrtm2-java
 ii  openrtm2-java-example:amd64      2.0.0-0                  amd64        OpenRTM-aist-Java examples
 ii  openrtm2-python3                         2.0.0-0                  amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-doc                   2.0.0-0                  all               Documentation for openrtm2-python3
 ii  openrtm2-python3-example            2.0.0-0                  amd64        OpenRTM-aist-Python examples
 ii  openrtp2:amd64                            2.0.0-0                  amd64        OpenRTP, Open RT Platform distributed by AIST
```

&color(fuchsia){Ubuntu24.04ではデフォルトのpipバージョン利用で、 rtshellのインストールに失敗します。　インストールスクリプトが表示している黄文字のメッセージに従い、　/etc/pip.conf へ（存在しなければ
新規作成して）下記を追記後に再度インストールスクリプトを実行するとインストールできます。};

```
 $ vi /etc/pip.conf
 [global]
 break-system-packages = true
```

オプションを指定することで、目的に合わせたパッケージをインストールすることが可能です。 help は下記で確認できます。

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) --help
```

インストールされるパッケージの詳しい内容は「[OpenRTM-aist-2.0 debパッケージの詳しい内容]({{ site.baseurl }}/ja/doc/installation/install_2_0/install_linux_2_0/install_debpackages_workcontent_2_0) 」で確認できます。

## ROS用パッケージのインストール

2.0系ではROS通信機能用パッケージをインストールできます。（ROS用、ROS2用)  <br>
ここでは、ROS, ROS2 の両方をインストールしている環境へのパッケージインストール方法を説明します。

help に記載しているように、ROSパッケージインストールオプションは以下で対応しています。<br>
[-e ros|ros2|all] [--ros|--ros2]

すでにインストールスクリプトをオプション無しで実行済みで、追加でROS, ROS2用パッケージを追加インストールする場合は、「-l c++ -e all」で可能です。<br>
<span style="color:fuchsia;">ROS2のみサポートされているUbuntu22.04以降の環境では、-e all でROS2用パッケージのみがインストールされます。</span>;


```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l c++ -e all
```

最初からROS, ROS2用パッケージも加えてすべてインストールしたい場合は、「 -l all -e all」で可能です。
```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l all -e all
```

インストールされたパッケージを確認します。

```
 $ dpkg -l | grep openrt
 ii  openrtm2:amd64                          2.0.0-0       amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-dev:amd64                    2.0.0-0       amd64        OpenRTM-aist headers for development
 ii  openrtm2-doc                               2.0.0-0       all               Documentation for openrtm2
 ii  openrtm2-example:amd64             2.0.0-0       amd64        OpenRTM-aist examples
 ii  openrtm2-idl:amd64                      2.0.0-0       amd64        OpenRTM-aist idls for development
 ii  openrtm2-java:amd64                   2.0.0-0       amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-java-doc                        2.0.0-0       all               Documentation for openrtm2-java
 ii  openrtm2-java-example:amd64      2.0.0-0      amd64        OpenRTM-aist-Java examples
 ii  openrtm2-python3                         2.0.0-0      amd64        OpenRTM-aist, RT-Middleware distributed by AIST
 ii  openrtm2-python3-doc                   2.0.0-0      all               Documentation for openrtm2-python3
 ii  openrtm2-python3-example            2.0.0-0      amd64        OpenRTM-aist-Python examples
 ii  openrtm2-ros-tp:amd64                 2.0.0-0      amd64        OpenRTM-aist extension ROS package
 ii  openrtm2-ros2-tp:amd64               2.0.0-0      amd64        OpenRTM-aist extension ROS2 package
 ii  openrtp2:amd64                            2.0.0-0      amd64        OpenRTP, Open RT Platform distributed by AIST
```

## 1.2系インストール環境への2.0系インストール

1.2系のインストールスクリプトも、URL指定で実行可能となっています。スクリプトをオプション無しで全パッケージインストールします。

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh)
```

インストールされたパッケージを確認します。

```
 $ dpkg -l | grep openrt
 ii  openrtm-aist:amd64                         1.2.2-0
 ii  openrtm-aist-dev:amd64                   1.2.2-0
 ii  openrtm-aist-doc                              1.2.2-0
 ii  openrtm-aist-example:amd64            1.2.2-0
 ii  openrtm-aist-idl:amd64                     1.2.2-0
 ii  openrtm-aist-java:amd64                  1.2.2-0
 ii  openrtm-aist-java-doc                       1.2.2-0
 ii  openrtm-aist-java-example:amd64     1.2.2-0
 ii  openrtm-aist-python3                        1.2.2-0
 ii  openrtm-aist-python3-doc                  1.2.2-0
 ii  openrtm-aist-python3-example           1.2.2-0
 ii  openrtp:amd64                                  1.2.2-4
```

続けて2.0系をインストールすると、c++とopenrtpは1.2系、2.0系が共存しますが、javaとpythonは2.0系のみがインストールされている状態になります。

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

スクリプト実行中、1.2系のjavaとpythonパッケージのアンインストールについて、「Do you want to continue? [Y/n] 」と聞かれますので、Enterキーを押してください。 <br>
インストールされたパッケージを確認します。

```
 $ dpkg -l | grep openrt
 ii  openrtm-aist:amd64                         1.2.2-0
 ii  openrtm-aist-dev:amd64                   1.2.2-0
 ii  openrtm-aist-doc                              1.2.2-0
 ii  openrtm-aist-example:amd64            1.2.2-0
 ii  openrtm-aist-idl:amd64                     1.2.2-0
 ii  openrtm2:amd64                              2.0.0-0
 ii  openrtm2-dev:amd64                        2.0.0-0
 ii  openrtm2-doc                                   2.0.0-0
 ii  openrtm2-example:amd64                 2.0.0-0
 ii  openrtm2-idl:amd64                          2.0.0-0
 ii  openrtm2-java:amd64                        2.0.0-0
 ii  openrtm2-java-doc                             2.0.0-0
 ii  openrtm2-java-example:amd64           2.0.0-0
 ii  openrtm2-python3                              2.0.0-0
 ii  openrtm2-python3-doc                       2.0.0-0
 ii  openrtm2-python3-example                2.0.0-0
 ii  openrtp:amd64                                  1.2.2-4
 ii  openrtp2:amd64                                2.0.0-0
```

これに伴い、rtshellもインストールし直されます。

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python    2.0.0
 rtctree-aist           4.2.3
 rtshell-aist           4.2.9
 rtsprofile-aist        4.1.5
```

## 2.0系インストール環境への1.2系インストール

c++とopenrtpは1.2系、2.0系が共存しますが、javaとpythonは1.2系のみがインストールされている状態になります。 

```
 $ dpkg -l | grep openrt
 ii  openrtm-aist:amd64                        1.2.2-0
 ii  openrtm-aist-dev:amd64                 1.2.2-0
 ii  openrtm-aist-doc                             1.2.2-0
 ii  openrtm-aist-example:amd64           1.2.2-0
 ii  openrtm-aist-idl:amd64                    1.2.2-0
 ii  openrtm-aist-java:amd64                 1.2.2-0
 ii  openrtm-aist-java-doc                      1.2.2-0
 ii  openrtm-aist-java-example:amd64    1.2.2-0
 ii  openrtm-aist-python3                       1.2.2-0
 ii  openrtm-aist-python3-doc                 1.2.2-0
 ii  openrtm-aist-python3-example          1.2.2-0
 ii  openrtm2:amd64                             2.0.0-0
 ii  openrtm2-dev:amd64                       2.0.0-0
 ii  openrtm2-doc                                  2.0.0-0
 ii  openrtm2-example:amd64                2.0.0-0
 ii  openrtm2-idl:amd64                         2.0.0-0
 ii  openrtp:amd64                                1.2.2-4
 ii  openrtp2:amd64                             2.0.0-0
```

rtshellも OpenRTM-aist-Python1.2.2 に対してインストールし直されます。

```
 $ pip3 list | grep aist
 OpenRTM-aist-Python    1.2.2
 rtctree-aist           4.2.3
 rtshell-aist           4.2.9
 rtsprofile-aist        4.1.5
```


