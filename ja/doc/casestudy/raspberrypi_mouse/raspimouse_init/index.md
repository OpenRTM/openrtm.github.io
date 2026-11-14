---
layout: page
title: 初期設定等
---

<!-- Title: 初期設定等 -->
#contents


# Raspbian

[このページ]({{ site.baseurl }}/ja/doc/installation/other/raspberrypi_casestudy/prep_sdc) の手順に従ってRaspbian を SDカードに書き込んでください。
※フルキットに付属の SDカードを使用する場合はこの作業は不要です。

# 組み立て方
最初に Raspberry Pi に SDカードを挿入してください。一度組み立てると Raspberry Pi を取り外さない限り SDカードの交換はできません。
<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm2.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm2.png" width="70%;"></a></div>
まずは Raspberry Pi をラズパイマウス本体に載せます。
スペーサーに Raspberry Pi を付属のねじで留めてください。
<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm0.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm0.png" width="70%;"></a></div>
最後に Raspberry Pi とラズパイマウス本体のピンヘッダに部品を取り付ければ完成です。
<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm1.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm1.png" width="70%;"></a></div>


# Raspbian 起動

以下の作業は Rasbian を起動して行います。
まずは Raspberry Pi にディスプレイ、マウス、キーボード、LANケーブルを接続してください。

ラズパイマウスはバッテリー以外にも付属のケーブルでコンセントから電源をとれるのですが、ラズパイマウスに接続するコネクタの向きには注意してください。

ラズパイマウスの電源スイッチは以下の位置にあります。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm8.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm8.png" width="70%;"></a></div>

手前のスイッチがモーター電源で、内側のスイッチが Raspberry Pi の電源です。
内側のスイッチを ON にしてください。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm9.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm9.png" width="70%;"></a></div>

Raspbian が起動したらユーザー名が pi、パスワードが raspberry でログインできるはずなのでログインしてください。
ログインできたら以下のコマンドで X-Window を起動してください。

```
 startx
```

# デバイスドライバ


Raspbian 起動後、以下のコマンドでリポジトリをクローンしてください。
```
 git clone https://github.com/rt-net/RaspberryPiMouse.git
```
※git がインストールされていない場合は以下のコマンドを入力してください。
```
 sudo apt-get install git
```
そして以下のコマンドでカーネルのバージョンを確認してください。
```
 uname -r
```
仮に Raspberry Pi 2 model B のカーネルのバージョン 4.1.6-v7+ の場合は以下のコマンドでカーネルモジュールをロードしてください。
```
 cd RaspberryPiMouse/lib/Pi2B+/4.1.6-v7+/
 sudo insmod rtmouse.ko
```

SPI 機能を有効にしていない場合は以下のコマンド、もしくは [Menu] > [Preference] > [Raspberry Pi Configuration] で表示される画面で設定してください。

```
  sudo raspi-config
```

上下キーで「Advanced Options」を選択後 Enter キーを押してください。
次に A5 SPI を同じ手順で選択します。
そして左右キーで Yes を選択して OK で Enter キーを押せば有効になります。
元の画面に戻ったら
左右キーで [Finish] を選択して終了してください。
詳しくは [このページ](http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/) を参考にしてください。


※フルキットに付属の SDカードを使用する場合はこの作業は不要です。

# OpenRTM-aist

# C++版

Raspbian に C++版 OpenRTM-aist のインストールには以下のコマンドを入力します。

```
 wget http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_1/OpenRTM-aist/build/pkg_install_debian.sh
 sudo sh pkg_install_debian.sh
```




詳しくは [このページ]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_rasbian_1_1) を参考にしてください。

※母艦 PC の OS は Windows を想定しています。
Windows に OpenRTM-aist をインストールする手順については [このページ]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1) を参考にしてください。
Python版のサンプルコンポーネントも利用するので、Python版もインストールしてください。
またサンプルの RTシステムで rtshell を使用するため、[このページ]({{ site.baseurl }}/ja/doc/old_documents/install_rtshell) を参考にしてインストールしてください。

# Python版
Python版のインストールには最初に以下のコマンドを入力してください。

```
 wget http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_debian.sh
 sudo sh pkg_install_python_debian.sh
```

