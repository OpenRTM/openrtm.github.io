---
layout: page
title: ev3 を無線lanアクセスポイントとして動作させるまでの手順
---

<!-- Title: EV3 を無線LANアクセスポイントとして動作させるまでの手順 -->
ここでは EV3 をアクセスポイント化するまでの手順を説明します。

Raspberry Pi とほとんど手順は同じなので、詳しいことは以下のサイトなどを参考にしてください。

[http://hara.jpn.com/_default/ja/Topics/RasPiE3839EE382A6E382B9E38292E784A1E7B79ALANE382A2E382AFE382BBE382B9E3839DE382A4E383B3E38388E58C96.html](http://hara.jpn.com/_default/ja/Topics/RasPiE3839EE382A6E382B9E38292E784A1E7B79ALANE382A2E382AFE382BBE382B9E3839DE382A4E383B3E38388E58C96.html)


## Realtek 製品対応の hostapd のコンパイル

無線LANアダプタは GW-USNANO2A を使います。
まず上記のサイトにもあるように 8192CU は hostapd にはデフォルトで対応していないので、クロス環境で以下のコマンドを入力してコンパイルを行います。

```
 wget http://12244.wpc.azureedge.net/8012244/drivers/rtdrivers/cn/wlan/0001-RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911.zip
 unzip 0001-RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911.zip
 cd RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911/wpa_supplicant_hostapd/
 tar zxvf wpa_supplicant_hostapd-0.8_rtw_r7475.20130812.tar.gz
 cd wpa_supplicant_hostapd-0.8_rtw_r7475.20130812/hostapd/
 make
```


コンパイルが終了したら、hostapdをEV3 に転送してください。

```
 sftp robot@<IPアドレス>
 put hostapd
```




## 各種設定
### 固定IPアドレス
/etc/network/interfaces に以下の記述を追加してください。

```
 auto lo
 
 iface lo inet loopback
 
 iface eth0 inet dhcp
 
 auto wlan0
 iface wlan0 inet static
 address 192.168.11.1
 netmask 255.255.255.0
```


### hostapd のインストール

以下のコマンドで hostapd をインストールしてください。

```
 sudo apt-get install hostapd
```

インストールが完了したら、先ほど転送した hostapdを/usr/sbin にコピーしてください。

```
 cp hostapd /usr/sbin/hostapd
```


/etc/hostapd/hostapd.conf は以下のように記述します。
ssid、wpa_passphrase は適宜変更してください。

```
 interface=wlan0
 driver=rtl871xdrv
 ssid=ev3_0
 hw_mode=g
 channel=6
 macaddr_acl=0
 auth_algs=1
 ignore_broadcast_ssid=0
 wpa=2
 wpa_passphrase=ev3atx9fr
 wpa_key_mgmt=WPA-PSK
 wpa_pairwise=TKIP
 rsn_pairwise=CCMP
```


/etc/default/hostapd を以下のように変更します。

```
 #DAEMON_CONF=""
 →
 DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

ネットワークを再起動します。

```
 sudo /etc/init.d/networking restart
```

以下のコマンドで hostapd を起動します。

```
 sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf -dd
```

これで他の PC から設定した SSID が見えるようにはなったはずです。

## DHCP サーバーの設定

以下のコマンドで DHCP サーバーをインストールします。

```
 sudo apt-get install isc-dhcp-server
```

/etc/dhcp/dhcpd.conf を以下のように修正してください。


```
 # option definitions common to all supported networks...
 #option domain-name "example.org";
 #option domain-name-servers ns1.example.org, ns2.example.org;
 
 ping-check true;
 
 #default-lease-time 600;
 #max-lease-time 7200;
 
 authoritative;
 
 subnet 192.168.11.0 netmask 255.255.255.0 {
 option routers 192.168.11.1;
 option broadcast-address 192.168.11.255;
 option subnet-mask 255.255.255.0;
 option domain-name "local";
 option domain-name-servers 8.8.8.8,8.8.4.4;
 default-lease-time 600;
 max-lease-time 7200;
 range 192.168.11.101 192.168.11.199;
 }
```

/etc/default/isc-dhcp-server を以下のように修正します。
```
 INTERFACES="wlan0"
```



## 起動スクリプトの設定

最後の rc.local に以下の記述を追加します。

```
 ifdown wlan0
 ifup wlan0
 service hostapd start
 service isc-dhcp-server start
```


再起動する前に [このページ]({{ site.baseurl }}/ja/doc/casestudy/lego_mindstorm/lego_setup_ev3_ev3dev#toc6)の手順で無線LANを設定している場合は、Wireless and Networks→Wifi→Powered を OFF に設定してください。また Wireless and Networks→Offline Mode を ON にしてください。

これで全ての手順が終了したので、再起動して接続できるかを確認してください。
失敗する場合は有線で EV3 と接続して設定が正しく行われているかを確認してください。

## ボタン操作でアクセスポイントを起動する手順

EV3 のボタン操作でアクセスポイントを起動する手順を説明します。

まず /home/robot に以下のスクリプトファイル(ここでは start_ap.sh) を作成してください。

```
 #!/bin/sh
 sudo ifdown wlan0
 sudo ifup wlan0
 sudo service hostapd start
 sudo service isc-dhcp-server start
```

以下のコマンドで権限を変更してください。

```
 chmod +x start_ap.sh
```

このファイルを EV3 のボタン操作で File Browser→start_ap.sh で起動するのですが、EV3 のボタン操作で sudo 実行時のパスワードが入力できないので sudo をパスワードなしで実行できるように設定します。

以下のコマンドを入力してください。

```
 sudo visudo
```

そして以下の記述を追加してください。

```
 robot ALL=(ALL)     ALL
 %robot ALL=(ALL)     NOPASSWD: ALL
```

これで準備完了です。EV3 のボタン操作で File Browser→start_ap.sh を起動してください。
