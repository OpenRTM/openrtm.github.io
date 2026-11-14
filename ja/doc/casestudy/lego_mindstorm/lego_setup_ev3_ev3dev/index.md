---
layout: page
title: ev3 および ev3dev の初期設定
---

<!-- Title: EV3 および ev3dev の初期設定 -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * EV3 および ev3dev の初期設定 -->

#contents

## 電池・無線LAN・SDカードのセット

### 電池

EV3 は単3電池6本、または専用のバッテリーパックで動作します。単3電池6本、もしくは専用のバッテリーをセットしてください。

<div align="center"><a href="EV3_with_AAAbattery.png"><img src="EV3_with_AAAbattery.png" width="40%;"></a></div>
<div align="center"><strong>単3電池</strong></div>

<div align="center"><a href="EV3_with_battery.png"><img src="EV3_with_battery.png" width="40%;"></a></div>
<div align="center"><strong>EV3専用バッテリーパック</strong></div>

### 無線LAN

USB接続の無線LANインターフェースをを用意します。EV3 は PCと有線接続して、PC経由でインターネットに接続することもできますが、ここでは無線LAN接続を前提として説明します。

最近の無線LANドングルであれば、大抵のものが使用可能なはずですが、一例として以下の無線LANドングルは動作確認ができています。

- BUFFALO WLI-UC-GNM2 Wireless LAN Adapter
- BUFFALO WLI-UC-GN Wireless LAN Adapter
- PLANEX GW-USMicro300

<div align="center"><a href="wlan_dongle.png"><img src="wlan_dongle.png" width="60%;"></a></div>
<div align="center"><strong>無線LANドングルの例</strong></div>

その他の接続方法に関しては、ev3dev の Webページをご覧ください。

- [Bluetooth経由でのネット接続](http://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-bluetooth/)
- [USB経由での接続](http://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-usb/)
- [Bluetoothによるテザリング接続](http://www.ev3dev.org/docs/tutorials/using-bluetooth-tethering/)
- [USBによるテザリング接続](http://www.ev3dev.org/docs/tutorials/using-usb-tethering/)

### SDカードの挿入

無線LANドングルと共に、EV3 のコントローラの側面に ev3dev イメージを書き込んだ SDカードを以下のように挿入してください。

<div align="center"><a href="ev3_wlan_sdcard.png"><img src="ev3_wlan_sdcard.png" width="60%;"></a></div>
<div align="center"><strong>EV3の側面に、無線LANドングルと SDカードを挿入</strong></div>

## ev3dev の起動

SDカードを挿入し、電源ボタン（十字キーボタンの中央の濃いグレーのボタン）を押して EV3 に電源を投入すると、以下のような起動画面が表示され、十字キーのあたりの LED が点滅します。

<div align="center"><a href="ev3dev_screen_booting.png"><img src="ev3dev_screen_booting.png" width="60%;"></a></div>
<div align="center"><strong>ev3dev 起動画面</strong></div>

暫く(1分前後)して起動が完了すると、以下のような初期画面が表示されます。

<div align="center"><a href="ev3dev_screen.png"><img src="ev3dev_screen.png" width="60%;"></a></div>
<div align="center"><strong>起動直後の画面</strong></div>

## ssh ログイン

### ネットワークへの接続

起動直後の EV3 は、まだネットワークにつながっていません。
初期画面の状態から、十字キーで、**Wireless and Networks** を選択し、決定ボタン（中央の濃いグレーのボタン）を押します。

```
 ------------------------------
                       V [8.12>
 ------------------------------
  File Brower                >
  Device Browser             >
 [Wireless and Networks      > ]
  Battery                    >
  About                      >
 ------------------------------
```

選択すると、以下のような画面になります。

```
 ------------------------------
      Wireless and Network
 ------------------------------
        Status: Offline
 ------------------------------
 Bluetooth                    >
 USB                          >
 Wifi                         >
 All Network Connections      >
 Tethering                    >
 Offline Mode                □
 ------------------------------

```

**WiFi** を選択すると、以下の画面に遷移します。

```
 ------------------------------
           WiFi
 ------------------------------
 Powered                      □
 Start Scan
            Networks
 ------------------------------
 [* MyWirelessNetwork   ?? ]

 ------------------------------
```

Powered を選択し、電源をONにし、スキャンして現れた SSID のうち接続したい ID を選択します。

```
 ------------------------------
      MyWirelessNetwork
 ------------------------------
 Status:                 Online
 Signal                     83%
 Security        WPA/2 PSK, WPS
 IP Address:
 [    Connect   ]
 [      Network Connection     ]
```

**Connect** を選択し決定ボタンを押すと、KEYを入力するダイアログが現れます。再度、決定ボタンを押すと、以下のようなキーボードが現れるので、KEY を入力します。


```
 [_                           ]
 [ABC] [abc] [123] [!@# ] [INS]
 [Q][W][E][R][T][Y][U][I][O][P]
 [A][S][D][F][G][H][J][K][L][ ]
 [ ][Z][X][C][V][B][N][M][ ][ ]
 [ Accept ]          [ Cancel ]
```

KEY を入力後、Accept を選択し決定ボタンを押すと、先どのダイアログに KEY が入力された状態で表示されるので、再度 **Accept** を押します。
暫くすると、指定した無線LANアクセスポイントにつながるはずです。何度か戻るボタン（画面の左下のボタン）を押すと初期画面に戻ります。
左上に割り当てらえた IPアドレスが表示されているはずです。


```
 --------------------------
 192.168.11.3          V [8.12>
 --------------------------
  File Brower                >
  Device Browser             >
 [Wireless and Networks      > ]
  Battery                    >
  About                      >
  
 --------------------------

```

### USBケーブルでの接続

無線LANが何らかの理由で使用できない場合は USBケーブルで接続することもできます。

EV3 と PCを付属の USBケーブルで接続してください。

<div align="center"><a href="s_DSC00467.JPG"><img src="s_DSC00467.JPG" width="40%;"></a></div>

ev3dev の初期画面で Wireless and Networks を選択してください。
次に All Network Connections を選択します。

```
 ------------------------------
      Wireless and Network
 ------------------------------
        Status: Offline
 ------------------------------
 Bluetooth                    >
 Wifi                         >
 All Network Connections      > ]
 Tethering                    >
 Offline Mode                □
 ------------------------------
```

Wiredを選択します。

```
 ------------------------------
      All Network Connections
 ------------------------------
 Wired                        ψ ]
 ------------------------------
```

Connectを選択すると接続します。

```
 ------------------------------
             Wired
 ------------------------------
        Status: Offline
 ------------------------------
 Connect                        ]
 Connect automatically       □
 IPv4                         >
 DNS                          >
 ENET                         >
 ------------------------------
```

#### テザリングの設定
EV3 で USBテザリングの設定を行う手順を説明します。
まず ev3dev の初期画面で Wireless and Networks を選択してください。

次に Tehering を選択します。

```
 ------------------------------
      Wireless and Network
 ------------------------------
        Status: Offline
 ------------------------------
 Bluetooth                    >
 Wifi                         >
 All Network Connections      >
 Tethering                    > ]
 Offline Mode                □
 ------------------------------
```

Gadget をオンにすれば完了です。


```
 ------------------------------
           Tethering
 ------------------------------
 Bluetooth                   □
 Gadget                      ■
 Network Info                 >
 ------------------------------
```


### ログイン

EV3 に割り当てられた IPアドレスに sshで接続します。デフォルトでは、ev3dev は以下の ID とパスワードが設定されています。

<table class="table-alt">
  <tr>
    <td>ID</td>
    <td>robot</td>
  </tr>
  <tr>
    <td>Password</td>
    <td>maker</td>
  </tr>
</table>

Windows では、TeraTerm などのターミナルソフトウェアを利用します。
Linux などでは、ターミナル画面から、

```
 $ ssh robot@<IPアドレス>
```

として、ログインします。ログインすると、以下のような画面が表示されるはずです。

```
              _____     _
    _____   _|___ /  __| | _____   __
   / _ \ \ / / |_ \ / _` |/ _ \ \ / /
  |  __/\ V / ___) | (_| |  __/\ V /
   \___| \_/ |____/ \__,_|\___| \_/

 Debian jessie on LEGO MINDSTORMS EV3!
 
 The programs included with the Debian GNU/Linux system are free software;
 the exact distribution terms for each program are described in the
 individual files in /usr/share/doc/*/copyright.
 
 Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
 permitted by applicable law.
 Last login: Tue Aug  4 01:34:12 2015 from openrtm.org
 root@ev3dev:~#
```

### TeraTerm のインストール(参考)

Windows から EV3 に ssh 経由でログインするためには、ssh クライアントをインストールする必要があります。
Windows で利用可能なクライアントは多数ありますが、ここでは Tera Term を紹介します。

- [Tera Term](http://sourceforge.jp/projects/ttssh2/)

こちらから、TeraTerm をダウンロード、インストールしてください。

<div align="center"><a href="teraterm_connect.png"><img src="teraterm_connect.png" width="60%;"></a></div>
<div align="center"><strong>TeraTerm による接続</strong></div>

TeraTerm をインストール後、起動すると接続ダイアログが現れるので、先ほど設定したホスト名+**.local** を「ホスト」のテキストボックスに入力しOKを押します。


## 設定

### 無線LANの設定

上記で行ったEV3 の無線LAN設定は、再起動すると消えてしまいます。起動後に自動で無線LAN に接続するためには、EV3 にログインして無線LANの接続設定を行う必要があります。

### /etc/wpa_supplicant/wpa_supplicant.conf の編集

次に、無線LAN の ESSID とキーを登録します。

```
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

通常は、これだけで接続できるはずです。ただし、無線LANアクセスポイントの設定によっては、追加の設定が必要になるかもしれません。
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
 # ifdown wlan0 ; ifup wlan0
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

実際には、いったん無線LANインターフェースがOFFになるので、このような表示は見えません。また、場合によっては、ssh 接続が切断される可能性があるので、その場合は、再度接続してみてください。

最後に、設定が正しく行われているか確認するため、再起動してみます。

```
 # reboot
```

EV3 がシャットダウンされ、再び起動画面が表示されます。しばらくすると、初期画面が表示され、設定が正しく行われていれば、画面の左上に IPアドレスが表示されるはずです。

### ホスト名でリモート接続する

EV3 に ssh でリモートログインで操作する場合、上記のように無線LAN接続後、画面左上に表示される IPアドレスにssh接続することができます。
IPアドレスは DHCP で割り当てられているので、接続の度に代わる可能性があり、そのたびに異なる IPアドレスで接続しなければならないので不便です。

ev3dev には avahi という Bonjour互換のサービスがインストールしてあります。
Bonjour は Apple が提唱するネットワーク上のサービスを自動的に検索して利用できるようにするためのサービスです。
avahiを使うと、DHCP で IPアドレスを割り振っている EV3 に対してもホスト名でアクセスすることができるようになります。

#### ホスト名の設定

ev3dev ではデフォルトで **ev3dev** というホスト名が設定してあります。他の avahi や Bonjour がインストールしてあるマシンからは、**ev3dev.local** という **.local** がついたホスト名でアクセスできます。

EV3 が複数台ネットワーク上にある場合には、他のホスト名と衝突しないホスト名を選び設定する必要があります。

```
 $ sudo vi /etc/hostname
```

/etc/hostname の1行目にホスト名を記載します。デフォルトでは ev3dev となっていますので、好みの名前に設定してください。
。
### avahi-daemon のインストール

Linux ホストから EV3 へアクセスする場合、avahiというサービスをインストールする必要があります。
最近のLinuxディストリビューションでは、たいていデフォルトでこのサービスがインストールされていますが、もしインストールされていない場合は、以下のように avahi デーモンをインストールします。(debian系のディストリビューションの場合)

```
 $ sudo apt-get update
 $ sudo apt-get install avahi-daemon
```

EV に対して ping を打ってみます。ホスト名の後に .local を付けた名前を使います。

```
 $ ping ev3dev.local
```

これで ping が返ってくれば、avahi がほぼ正しく設定されていることになります。


### Bonjour のインストール (Windowsのみ)

PC から EV3 にアクセスするためには、PC側にも avahi か Bonjour がインストールされている必要があります。

Windows ではデフォルトでは Bonjour はインストールされていません。
最も簡単に Bonjour を導入する方法は [iTunes](http://www.apple.com/jp/itunes/download/) をインストールすることです。

- [iTunesダウンロード](http://www.apple.com/jp/itunes/download/)

どうしても iTunes をインストールしたくない場合は、アーカイバアプリケーションなどで、ダウンロードした iTunesSetup.exe を展開すると BonjourSetup.exe を抽出することもできます。

また、以下の Apple Bonjour 印刷サービスにも Bonjour が同梱されています。(iTunesに同梱されているものよりバージョンが若干古いようです。)

- [Apple Bonjour](http://www.apple.com/jp/support/bonjour/)
  - [Bonjour 印刷サービス (v2.0.2.0)](http://support.apple.com/kb/DL999)

現在 Applie では Bonjour for Windows 単体としては配布は行なっていませんが、かつて配布していたものを再配布しているサイトも幾つかあります。(ただし、古いバージョンしか入手できないようです。)
以下は Appleサイト以外の Bonjourダウンロードサイトです。自己責任でご利用ください。

- [BonjourSetup.exe (v1.0.6.2)](http://www.download3k.com/Install-Bonjour.html)
- [Bonjour64Setup.exe (v1.0.6.2)](http://download.techworld.com/760/apple-bonjour-for-windows-106-64-bit/)
- [Apple Bonjour SDK (Apple developer へのログインが必要)](https://developer.apple.com/downloads/index.action?q=Bonjour%20SDK%20for%20Windows)

#### Bonjour がうまく機能しない場合

ファイヤウォールが動作している場合、Bonjour がうまく機能しないことがあります。
その場合、UDPポート5353を開放するかファイヤウォールをOFFにしてください。

- [ファイアウォールの設定が原因で Bonjour for Windows が動作しない](http://support.apple.com/kb/TS2235?viewlocale=ja_JP)


