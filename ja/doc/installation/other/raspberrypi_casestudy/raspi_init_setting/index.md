---
layout: page
title: raspberry pi の初期設定
---

<!-- Title: Raspberry Pi の初期設定 -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * Raspberry Pi の初期設定 -->

#contents

## Raspberry Pi の起動

Raspberry Pi に HDMIモニター、キーボード、ネットワークを接続してください。

SDカードを挿入し Raspberry Pi に始めて電源を投入すると、各種ドライバの読み込み画面が表示された後、以下の設定画面 (raspi-config) が表示されます｡

なお、後述の PiRT-Unit のシリアルコンソールから操作する場合、raspi-config は表示されません。
以下のユーザー名、パスワードでログインして raspi-config コマンドを実行することで初期設定を行うことができます。

- ''ID' : pi
- **パスワード** : raspberry

```
 Debian GNU/Linux 7.0 rtunit0 ttyAMA0
 
 rtunit0 login: pi
 Password:
 Last login: Sat Feb  9 03:40:44 UTC 2013 on ttyAMA0
 Linux rtunit0 3.6.11+ #371 PREEMPT Thu Feb 7 16:31:35 GMT 2013 armv6l
 
 The programs included with the Debian GNU/Linux system are free software;
 the exact distribution terms for each program are described in the
 individual files in /usr/share/doc/*/copyright.
 
 Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
 permitted by applicable law. 
 
 NOTICE: the software on this Raspberry Pi has not been fully configured. Please run 'sudo raspi-config'
 $ raspi-config
 
```
<div align="center"><a href="raspi-config2.png"><img src="raspi-config2.png" width="80%;"></a></div>
<div align="center"><strong>Raspberry Pi 初期設定画面</strong></div>

### 設定項目

各項目の内容を以下に示します。
必要に応じて各項目の設定を行ってください｡

<!-- | ''[info]'' | 本ツールに関する情報を表示します｡ | -->
<!-- | ''[expand_rootfs]'' | 使用する SDカードのパーティションを拡張します｡初期状態では、SDカードの先頭の2GBしか使用しないようになっています｡こちらの機能を使用することで全体を使用するように設定できます｡特に理由がなければ拡張を行ってください｡ | -->
<!-- | ''[overscan]'' | 画面周囲に余白が必要な場合に設定します｡ | -->
<!-- | ''[configure_keyboard]'' | 使用するキーボードの配列を設定します｡一般的な日本語キーボードを使用する場合は、[Generic 105-key (Intl) PC] → [Japanese] → [Japanese - Japanese(OADG109A)]を選択後、使用したいキー配列をしてください｡ | -->
<!-- | ''[change_pass]'' | 初期設定ユーザー ｢pi｣ のパスワードを変更します｡ 利用者のわかりやすいパスワードに変更してください｡ | -->
<!-- | ''[change_locale]'' | ロケール設定を行います｡必要に応じて [ja_JP.ECU-JP ECU-JP] などに設定してください｡| -->
<!-- | ''[change-timezone]' | タイムゾーンの設定を行います｡日本国内で使用する場合は [Asia]-[Tokyo] を設定してください｡| -->
<!-- | ''[memory_split]'' | 付属の GPU へのメモリー配分を指定します｡特に問題がない場合は、初期設定のままで構いません｡| -->
<!-- | ''[ssh]'' | SSH 接続を有効にしたい場合には [Enable] に設定してください｡| -->
<!-- | ''[boot_behaviour]'' | 起動時に X Windows のデスクトップを自動起動させた場合には [Yes] を設定してください｡| -->
<!-- | ''[update]'' | 設定プログラム(raspi-config)自身のアップデートを行います｡| -->
<table class="table-alt">
  <tr>
    <th>**1 Expand Filesystem**</th>
    <th>使用する SD カードのパーティションを拡張します｡初期状態では、SD カードの全体を使用していないので、特に理由がなければ拡張を行ってください｡</th>
  </tr>
  <tr>
    <td>**2 Change User Password**</td>
    <td>初期設定ユーザー ｢pi｣ のパスワードを変更します｡ 利用者のわかりやすいパスワードに変更してください｡</td>
  </tr>
  <tr>
    <td>**3 Enable Boot to Desktop/Scratch**</td>
    <td>起動時の画面の設定で、デフォルトはコンソール利用となっています。GUI 利用に変更したい場合には設定します。</td>
  </tr>
  <tr>
    <td>**4 Internationalisation Options**</td>
    <td>「ロケール」、「タイムゾーン」、「キーボード配列」の設定です。</td>
  </tr>
  <tr>
    <td>I1 Change Locale</td>
    <td>ロケール設定を行います｡キーボード配列は必要に応じて [ja_JP.ECU-JP ECU-JP] などに設定してください｡　その際は日本語フォントのインストールが必要となるようです。</td>
  </tr>
  <tr>
    <td>I2 Change Timezone</td>
    <td>タイムゾーンの設定を行います｡日本国内で使用する場合は [Asia]-[Tokyo] を設定してください｡</td>
  </tr>
  <tr>
    <td>I3 Change Keyboard Layout Set the keyboard layout to match your keyboard</td>
    <td>キーボードの設定を行います。必要に応じて日本語キーボード等に設定して下さい。</td>
  </tr>
  <tr>
    <td>**5 Enable Camera**</td>
    <td>カメラモジュールを接続している場合に設定してください｡</td>
  </tr>
  <tr>
    <td>**6 Add to Rastrack**</td>
    <td>Rastrack への登録</td>
  </tr>
  <tr>
    <td>**7 Overclock**</td>
    <td>オーバークロック</td>
  </tr>
  <tr>
    <td>**8 Advanced Options**</td>
    <td>その他のオプション。ここでは PiRT-Unit の環境で必要な項目のみ取り上げます。</td>
  </tr>
  <tr>
    <td>A6 SPI</td>
    <td>SPIを利用する場合は、Enable に設定します。（デフォルトはDisable）</td>
  </tr>
  <tr>
    <td>A7 I2C</td>
    <td>I2Cを利用する場合は、Enable に設定します。（デフォルトはDisable）</td>
  </tr>
  <tr>
    <td>**9 About raspi-config**</td>
    <td>本ツールに関する情報を表示します｡</td>
  </tr>
</table>

上記の各項目を設定した後は、[Tab] キーにて [Finish] を選択して実行してください。
Raspberry Pi 本体が再起動し、各種設定が有効となります。

再起動後、コマンド入力待ち状態で、｢startx｣を実行すると Raspbian のデスクトップ画面が表示されます｡

<div align="center"><a href="raspberry_xwindow.png"><img src="raspberry_xwindow.png" width="70%;"></a></div>
<div align="center"><strong>Raspbian デスクトップ画面</strong></div>

<!-- 必要に応じて、ターミナル画面から root のパスワードを設定してください｡ -->
<!--  -->
<!-- $ sudo sh -->
<!-- # passwd -->

終了する場合は、以下のコマンドで停止した後、本体から電源を抜いてください｡

```
 $ sudo halt
```

## 無線LAN の設定

Raspberry Pi の USB に無線LANドングルを挿入し設定することで、Raspberry Pi を無線化できます。
移動ロボットなどに搭載する際には便利です。

### /etc/network/interfaces の編集

まず、/etc/network/interfaces を以下のように編集します。

```
 $ sudo vi /etc/network/interfaces
```

以下の2か所を書き換えます。

```
 iface wlan0 inet manual
         ↓
 iface wlan0 inet dhcp
```

```
 wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
                      ↓
 wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

### /etc/wpa_supplicant/wpa_supplicant.conf の編集

次に、無線LANの ESSID とキーを登録します。

```
 $ sudo bash
 # cd /etc/wpa_supplicant
 # wpa_passphrase ESSID pass >> wpa_supplicant.conf
```

SSID には無線LANの ESSID、pass には無線LANのキーを入力します。リダイレクトの際、**>** ではなく **>>** (追記)を使用するよう注意してください。
結果は以下のようになっていると思います。

```
 ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
 update_config=1
 network={
         ssid="OpenRTM"
         #psk="4332221111"
         psk=142914b76be167767055ff945898baaaf83c42b3ad3b99afb0ae531e8fb15e5e
 }
```

無線LAN アクセスポイントの設定によっては、追加の設定が必要になるかもしれません。
以下に、一例を示します。

```
 ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
 update_config=1
 network={
         ssid="OpenRTM"
         proto=WPA2
         key_mgmt=WPA-PSK
         pairwise=TKIP CCMP
         group=TKIP CCMP
         #psk="4332221111"
         psk=142914b76be167767055ff945898baaaf83c42b3ad3b99afb0ae531e8fb15e5e
 }
```

最後に、インターフェースを初期化します。

```
 # ifdown wlan0
 # ifup wlan0
 Internet Systems Consortium DHCP Client 4.2.2
 Copyright 2004-2011 Internet Systems Consortium.
 All rights reserved.
 For info, please visit https://www.isc.org/software/dhcp/
  : 中略
 DHCPREQUEST on wlan0 to 255.255.255.255 port 67
 DHCPOFFER from 192.168.11.1
 DHCPACK from 192.168.11.1
 bound to 192.168.11.26 -- renewal in 34810 seconds.
```

ここで、無線LAN に接続できない場合、/etc/network/interfaces, /etc/wpa_supplicant/wpa_supplicant.conf の設定を見直してください。
```
 
 # ifconfig wlan0
 wlan0     Link encap:Ethernet  HWaddr XX:XX:XX:XX:XX:XX
           inet addr:192.168.11.26  Bcast:192.168.11.255  Mask:255.255.255.0
           UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
           RX packets:1218 errors:0 dropped:0 overruns:0 frame:0
           TX packets:21 errors:0 dropped:0 overruns:0 carrier:0
           collisions:0 txqueuelen:1000
           RX bytes:250608 (244.7 KiB)  TX bytes:4506 (4.4 KiB)
```

無事、無線LAN wlan0 に IPアドレスが割り振られました。


## ホスト名でリモート接続する

Raspberry Pi に ssh でリモートログインで操作する場合、固定IPアドレスを割り振っていなければ、通常 Raspberry Pi の IPアドレスをコンソールで調べて接続する必要があります。

そこで Bonjour互換の avahi というサービスをインストールします。
Bonjour は Apple が提唱するネットワーク上のサービスを自動的に検索して利用できるようにするためのサービスです。
avahi を使うと、DHCP で IPアドレスを割り振っている Raspberry Pi に対してもホスト名でアクセスすることができるようになります。

### ホスト名の設定

他のホスト名と衝突しないホスト名を選び設定します。

```
 $ sudo vi /etc/hostname
```

/etc/hostname に1行目にホスト名を記載します。初期値は raspberrypi となっています。
さらに、/etc/hosts の 127.0.1.1 raspberrypi となっている部分を上で決めた自分のホスト名に書き換えます。

```
 $ sudo vi /etc/hosts
```

### avahi-daemon のインストール

以下のコマンドで avahi デーモンをインストールします。

```
 $ sudo apt-get update
 $ sudo apt-get install avahi-daemon
```

自ホストに対してping を打ってみます。ホスト名の後に .local を付けた名前を使います。

```
 $ ping myhost.local
```

これで ping が返ってくれば、avahi がほぼ正しく設定されていることになります。


### Bonjour のインストール (Windowsのみ)

PC から avahi が設定された RaspberryPi にアクセスするためには、PC側にも avahi か Bonjour がインストールされている必要があります。

Linux では、RaspberryPi と同様に avahi-daemon をインストールすれば使用できます。また
Mac はデフォルトで Bonjour がインストールされているので、特に何もする必要がありません。

Windows ではデフォルトでは Bonjour はインストールされていません。
最も簡単に Bonjour を導入する方法は [iTunes](http://www.apple.com/jp/itunes/download/) をインストールすることです。

- [iTunesダウンロード](http://www.apple.com/jp/itunes/download/)

どうしても iTunes をインストールしたくない場合は、アーカイバアプリケーションなどで、ダウンロードした iTunesSetup.exe を展開すると BonjourSetup.exe を抽出することもできます。

また、以下の Apple Bonjour 印刷サービスにも Bonjour が同梱されています。(iTunesに同梱されているものよりバージョンが若干古いようです。)

- [Apple Bonjour](http://www.apple.com/jp/support/bonjour/)
  - [Bonjour 印刷サービス (v2.0.2.0)](http://support.apple.com/kb/DL999)

現在 Applie では Bonjour for Windows 単体としては配布は行なっていませんが、かつて配布していたものを再配布しているサイトも幾つかあります。(ただし、古いバージョンしか入手できないようです。)
以下は Appleサイト以外の Bonjour ダウンロードサイトです。自己責任でご利用ください。

- [BonjourSetup.exe (v1.0.6.2)](http://www.download3k.com/Install-Bonjour.html)
- [Bonjour64Setup.exe (v1.0.6.2)](http://download.techworld.com/760/apple-bonjour-for-windows-106-64-bit/)
- [Apple Bonjour SDK (Apple developer へのログインが必要)](https://developer.apple.com/downloads/index.action?q=Bonjour%20SDK%20for%20Windows)

#### Bonjour がうまく機能しない場合

ファイヤウォールが動作している場合、Bonjour がうまく機能しないことがあります。
その場合、UDPポート5353を開放するかファイヤウォールを OFF にしてください。

- [ファイアウォールの設定が原因で Bonjour for Windows が動作しない](http://support.apple.com/kb/TS2235?viewlocale=ja_JP)

### TeraTerm のインストール

Windows から RaspberryPi に ssh 経由でログインするためには、ssh クライアントをインストールする必要があります。
Windows で利用可能なクライアントは多数ありますが、ここでは Tera Term を紹介します。

- [Tera Term](http://sourceforge.jp/projects/ttssh2/)

<div align="center"><a href="teraterm_connect.png"><img src="teraterm_connect.png" width="60%;"></a></div>
<div align="center"><strong>TeraTermによる接続</strong></div>

TeraTerm をインストール後、起動すると接続ダイアログが現れるので、先ほど設定したホスト名+**.local** を「ホスト」のテキストボックスに入力しOKを押します。
パスワードが変更されていなければ、

- ID: pi
- パスワード: raspberry

でログインできます。

なお、Linux や Mac はターミナルウインドウを開いて

```
 $ ssh pi@myhost.local
```

のようにして接続します。

