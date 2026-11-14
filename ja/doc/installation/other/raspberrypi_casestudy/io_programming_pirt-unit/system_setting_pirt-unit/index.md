---
layout: page
title: pirt-unitのためのシステム設定
---

<!-- Title: PiRT-Unitのためのシステム設定 -->
#contents

Raspberry Pi のデフォルトの設定 (raspbian armhf) では、SPI デバイスなどは利用できません。
ここで、PiRT-Unit を利用するために必要なデバイスの設定やプログラミング環境の構築を行います。

## セットアップスクリプト

以下の内容をスクリプト化したものがこちらにあります。

- セットアップスクリプト: [http://svn.openrtm.org/Embedded/trunk/RaspberryPi/tools/rpi.sh](http://svn.openrtm.org/Embedded/trunk/RaspberryPi/tools/rpi.sh)

Raspberry Pi のサイトからダウンロードしたイメージの適当な場所にダウンロードして以下のように実行します。

```
 $ wget http://svn.openrtm.org/Embedded/trunk/RaspberryPi/tools/rpi.sh
 $ chmod 755 rpi.sh
 $ sudo rpi.sh rtunit0 --type rtunit
 $ sudo rpi.sh rtunit0 --type rtunit_examples
```

以上で、以下の PiRT-Unit を利用するために行っている設定、パッケージのインストール、サンプルのインストールが自動で行われます。
バージョンアップ、ファイル配置の変更などによってエラーが出た場合にはメーリングリストなどへお知らせください。

### rpi.sh ヘルプ

```
 Usage: rpi.sh hostname --type <TYPE>
 
 TYPE are:  basic kobuki kobuki_only rtunit rtunit_only
   basic:           Installing avahi, cmake, subversion/git and OpenRTM
   kobuki:          Installing basic + Kobuki RTC
   kobuki_only:     Installing Kobuki RTC only
   rtunit:          Installing basic + spi/i2c tools and modules
   rtunit_only:     Installing spi/i2c tools and modules only
   rtunit_examples: Installing basic + PiRT-Unit examples
 
 EXAMPLE:
 1) Just change hostname
 # rpi.sh kobuki0
 
 2) Basic setup: Installing OpenRTM-aist (C++/Python)
 # rpi.sh kobuki --type basic
 "
 3) Kobuki setup: Installing OpenRTM-aist (C++/Python) and Kobuki RTC
 # rpi.sh kobuki --type kobuki
```

## システム設定ファイルの変更

spi と i2c のデバイスモジュールをロードする方法は、カーネルの3.18から変更になりました。Raspberry Pi用 OS Raspbian が2015年のバージョンから該当するようですが、カーネルのバージョンを確認して判断してください。<br>
spi と i2c を利用するためには、raspi-config で Enable に設定します。[Raspberry Pi の初期設定]({{ site.baseurl }}/ja/doc/installation/other/raspberrypi_casestudy/raspi_init_setting) のページをご覧ください。

これより古いバージョンでは、以下のファイルを設定します。

### raspi-blacklist.conf の編集

/etc/modprobe.d/raspi-blacklist.conf に

```
 blacklist spi-bcm2708
 blacklist i2c-bcm2708
```

という2行が設定されていますが、これをコメントアウトします。

```
 # blacklist spi and i2c by default (many users don't need them)
 
 #blacklist spi-bcm2708
 #blacklist i2c-bcm2708
```

これで、spi と i2c のデバイスモジュールがロードされるようになります。

### udev rules の設定

spi や i2c デバイスモジュールがロードされても、デフォルトでは一般ユーザーからアクセスできないようなパーミッションに設定されています。
少々不便なので、デバイス作成時に誰でもアクセスできるように設定しておきます。
新たに、/etc/udev/rules.d/50-udev.rules というファイルを作成し、中に以下の1行を追記します。

```
 KERNEL=="spidev*", SUBSYSTEM=="spidev", GROUP="spi", MODE="0666"
```

以上で準備は終了です。


<!-- ============================================================ -->
## Python 拡張モジュールのインストール

PiRT-Unit では AD および DA は SPI経由で接続されており、SPI デバイスを制御する Python モジュールをインストールすることで、Python から手軽に AD および DA を利用することができます。

### 事前準備

Python から SPI経由で AD、DA を利用するには、以下の拡張モジュールをインストールします。

- WiringPi-Python:[https://github.com/WiringPi/WiringPi-Python.git](https://github.com/WiringPi/WiringPi-Python.git)
  - wiringPi: git[https://git.drogon.net/wiringPi](https://git.drogon.net/wiringPi)
- py-spidev:[https://raw.github.com/doceme/py-spidev](https://raw.github.com/doceme/py-spidev)

下準備のため、以下のパッケージをインストールします。

- python-dev
- git-core
- i2c-tools
- python-smbus
- python-setuptools

```
 sudo apt-get update
 sudo apt-get upgrade
 sudo apt-get install python-dev git-core i2c-tools python-smbus
```

### py-spidev のインストール

py-spidev は github https://raw.github.com/doceme/py-spidev にあります。以下のようにしてインストールします。

```
 $ cd ~ (or 適当なディレクトリー)
 $ git clone git://github.com/doceme/py-spidev 
 $ cd py-spidev
 $ chmod 755 setup.py
 $ sudo ./setup.py install
```

これで、Python モジュール py-spidev が利用できるようになります。
試しに、spidev モジュールを利用してみます。

```
 $ sudo python
 sudo: unable to resolve host raspbian-armhf
 Python 2.7.3 (default, Jan 13 2013, 11:20:46)
 [GCC 4.6.3] on linux2
 Type "help", "copyright", "credits" or "license" for more information.
 >>> import spidev
 >>> spi = spidev.SpiDev()
 >>> spi.open(0,0)
 >>> print spi.xfer2([0x00,0,0,0])
```

これで、CN2のAD変換器の値を読みだしてプリントしています。AD変換器 (ADC104S021) は10bitのシングルエンド型で、サンプリングレートは最大200kHzです。(Linux上で200kHzのサンプリングレートを保証するものではありません。)
実際には、"spi.xfer2([0x00],0,0,0])" で出力される値を 1024 (bit) で割って、5.0 (V) を掛けた値が計測された電圧になります。

```
 >>> r = spi.xfer2([0x00,0,0,0])
 >>> print r[0] * 5.0 / 1024.0, " [V]"
```

ここまで、エラーなく実行できれば、spidev モジュールが正しくインストールされています。

### WiringPi-Python のインストール

WiringPi-Python は GPIO を制御するツール: WiringPi を Python から利用するためのモジュールです。
まずは WiringPi をインストールします。

```
 $ git clone git://git.drogon.net/wiringPi
 $ cd cd wiringPi
 $ git pull origin
 $ ./build
```

次に、WiringPi-Python 本体を以下のようにインストールします。

```
 $ sudo apt-get install python-dev  
 $ git clone https://github.com/WiringPi/WiringPi-Python.git  
 $ cd WiringPi-Python  
 $ git submodule update --init  
 $ sudo python setup.py install
```

以上で、必要なモジュールのインストールは終了です。
