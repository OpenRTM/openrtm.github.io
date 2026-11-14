---
layout: page
title: procedure for operating ev3 as a wireless lan access point
---

<!-- Title: Procedure for Operating EV3 as a Wireless LAN Access Point -->
This section explains the procedure for configuring the EV3 as a wireless LAN access point.

Since the procedure is almost the same as that for a Raspberry Pi, please refer to the following website for detailed information.

[http://hara.jpn.com/_default/ja/Topics/RasPiE3839EE382A6E382B9E38292E784A1E7B79ALANE382A2E382AFE382BBE382B9E3839DE382A4E383B3E38388E58C96.html](http://hara.jpn.com/_default/ja/Topics/RasPiE3839EE382A6E382B9E38292E784A1E7B79ALANE382A2E382AFE382BBE382B9E3839DE382A4E383B3E38388E58C96.html)

## Compiling hostapd with Realtek Device Support

Use the GW-USNANO2A wireless LAN adapter.

As described on the website above, the 8192CU chipset is not supported by hostapd by default. Therefore, enter the following commands in the cross-compilation environment and compile it.

```
 wget http://12244.wpc.azureedge.net/8012244/drivers/rtdrivers/cn/wlan/0001-RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911.zip
 unzip 0001-RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911.zip
 cd RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911/wpa_supplicant_hostapd/
 tar zxvf wpa_supplicant_hostapd-0.8_rtw_r7475.20130812.tar.gz
 cd wpa_supplicant_hostapd-0.8_rtw_r7475.20130812/hostapd/
 make
```

After compilation is complete, transfer hostapd to the EV3.

```
 sftp robot@<IP address>
 put hostapd
```

## Configuration

### Static IP Address

Add the following entries to `/etc/network/interfaces`.

```
 auto lo
 
 iface lo inet loopback
 
 iface eth0 inet dhcp
 
 auto wlan0
 iface wlan0 inet static
 address 192.168.11.1
 netmask 255.255.255.0
```

### Installing hostapd

Install hostapd with the following command.

```
 sudo apt-get install hostapd
```

After installation is complete, copy the hostapd file you transferred earlier to `/usr/sbin`.

```
 cp hostapd /usr/sbin/hostapd
```

Edit `/etc/hostapd/hostapd.conf` as follows.

Modify `ssid` and `wpa_passphrase` as appropriate.

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

Modify `/etc/default/hostapd` as follows.

```
 #DAEMON_CONF=""
 →
 DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

Restart the network.

```
 sudo /etc/init.d/networking restart
```

Start hostapd with the following command.

```
 sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf -dd
```

At this point, the configured SSID should be visible from other PCs.

## DHCP Server Configuration

Install the DHCP server with the following command.

```
 sudo apt-get install isc-dhcp-server
```

Modify `/etc/dhcp/dhcpd.conf` as follows.

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

Modify `/etc/default/isc-dhcp-server` as follows.

```
 INTERFACES="wlan0"
```

## Configuring the Startup Script

Finally, add the following entries to `rc.local`.

```
 ifdown wlan0
 ifup wlan0
 service hostapd start
 service isc-dhcp-server start
```

Before rebooting, if you have configured wireless LAN according to the procedure on [this page]({{ site.baseurl }}/en/doc/casestudy/lego_mindstorm/lego_setup_ev3_ev3dev#toc6), set **Wireless and Networks → Wifi → Powered** to **OFF**. Also set **Wireless and Networks → Offline Mode** to **ON**.

All procedures are now complete. Reboot the EV3 and verify that you can connect successfully.

If the connection fails, connect to the EV3 via a wired connection and verify that the configuration has been performed correctly.

## Procedure for Starting the Access Point Using Button Operations

This section explains how to start the access point using the EV3 buttons.

First, create the following script file in `/home/robot` (named `start_ap.sh` in this example).

```
 #!/bin/sh
 sudo ifdown wlan0
 sudo ifup wlan0
 sudo service hostapd start
 sudo service isc-dhcp-server start
```

Change the file permissions with the following command.

```
 chmod +x start_ap.sh
```

This file will be launched from **File Browser → start_ap.sh** using the EV3 buttons. However, since it is not possible to enter a password when executing sudo from the EV3 button interface, configure sudo so that it can be executed without a password.

Enter the following command.

```
 sudo visudo
```

Then add the following lines.

```
 robot ALL=(ALL)     ALL
 %robot ALL=(ALL)     NOPASSWD: ALL
```

The setup is now complete. Launch **File Browser → start_ap.sh** using the EV3 buttons.


