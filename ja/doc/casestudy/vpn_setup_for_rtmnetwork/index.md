---
layout: page
title: vpnを利用したrtmネットワーク設定方法
---

<!-- Title: VPNを利用したRTMネットワーク設定方法 -->
#contents

OpenRTM-aist を利用していると、ルーター・Firewall や NAT の内と外の RTC 同士を接続したい場合があります。
NAT の設定を自分で変えることができる場合、NAT のポートフォワーディング機能を利用し、rtc.conf の [corba.alternate_iiop_addresses]()（リンク切れです） オプションを指定することで NA T内外の RTC 同士を連携させることも可能です。
しかし、RTC の数だけポートフォワーディングの設定が必要であり、また自分で設定できない NAT や会社や学校の Firewall に対してはこの方法を利用できません。

そこで、VPN により仮想ネットワークを構築し RTC 間の通信をすべて VPN で行うことにより、Firewall などがあってもその内外の RTC 同士を連携させることができます。
このドキュメントでは VPN 仮想ネットワークを構築しそこを介してRTC同士を接続する方法を述べます。

## VPN サーバーの設定 (Linux)

### pptpd のインストール

まずはじめに VPN サーバー PPTPDをインストールします。Ubuntu や Debian などではパッケージが提供されていますので、以下のように apt-get でインストールできます。

```
 $ sudo apt-get install pptpd
 [sudo] password for openrtm

 :
 
 Starting PPTP Daemon: pptpd.
```

### pptpd.confの設定

次に/etc/pptpd.confを編集し pptpd サーバーの設定を行います。

```
$ sudo vi /etc/pptpd.conf
```

viなどのエディタで pptpd.conf を開き、設定ファイル下にある localip,、remoteip を設定します。
以下では最後の2行に localipとして 192.168.22.1、remoteip として 192.168.22.10-100 を設定しています。

```
 [/etc/pptpd.confファイル］
 #localip 192.168.0.1
 #remoteip 192.168.0.234-238,192.168.0.245
 # or
 #localip 192.168.0.234-238,192.168.0.245
 #remoteip 192.168.1.234-238,192.168.1.245
 localip 192.168.22.1
 remoteip 192.168.22.10-100
```

ここに設定するアドレスは基本的に現在使用していないネットワークおよびIPアドレスを指定してください。
この例では外部から接続してきたクライアントには192.168.22.10～100までのアドレスを付与します。



### ネットワーク構成

通常 VPN クライアントに対してはサーバーは適当なIPアドレスを割り振るように設定することが多いようですが、RTM ネットワークとして設定する場合、クライアント PC の IPアドレスを固定に設定したほうが RTC の設定もやりやすくなります。

ここでは、RTM 用のネットワーク設定として以下のものを想定します。

<table class="table-alt">
  <tr>
    <th>PC名</th>
    <th>IPアドレス</th>
    <th>備考</th>
  </tr>
  <tr>
    <td>PC0</td>
    <td>192.168.22.1</td>
    <td>VPN サーバー, CORBA ネームサーバー</td>
  </tr>
  <tr>
    <td>PC1</td>
    <td>192.168.22.10</td>
    <td>RTC が動作する PC</td>
  </tr>
  <tr>
    <td>PC2</td>
    <td>192.168.22.11</td>
    <td>RTC が動作する PC</td>
  </tr>
  <tr>
    <td>PC3</td>
    <td>192.168.22.12</td>
    <td>RTC が動作する PC</td>
  </tr>
</table>

### /etc/ppp/chap-secretsの設定

上記のネットワーク構成を踏まえたうえで、次に PPTP 接続用のユーザID、パスワードを /etc/ppp/chap-secrets ファイルに設定します。


```
 $ sudo vi /etc/ppp/chap-secrets
 
 [/etc/ppp/chap-secretsファイル]
 # Secrets for authentication using CHAP
 # client     server     secret               IP addresses
 pc1 pptpd openrtm1 192.168.22.10
 pc2 pptpd openrtm1 192.168.22.11
 pc3 pptpd openrtm1 192.168.22.12
```

ここでは client（ユーザーID）としてpc1, pc2, pc3を定義し、serverにpptpd、secret（パスワード）にopenrtm1, openrtm2, openrtm3、IP address（クライアントに割り振るIPアドレス）は上で決めた IPアドレスを設定しています。

### サーバーの再起動

以上ができたら、pptpd を再起動します。

```
 $ sudo /etc/init.d/pptpd restart
```


## VPN クライアントの設定(Linux)

VPN クライアントの設定を行います。Linux の場合は、サーバー同様にまず pptpd をインストールします。

### エントリの作成

VPN 接続する際の設定情報を pptpsetup コマンドを利用して作成します。

```
 $ sudo pptpsetup --create pc1 --server pc0.mydomain --username pc1 --password openrtm1 --encrypt
```

コマンドの引数の意味は以下の通りです。

- **pc1:** エントリ名
- **--server pc0.mydomain:** VPN サーバーの指定
- **--username pc1:** 上記で設定したユーザー名 **pc1**
- **--password openrtm1:** 上記で設定したパスワード **openrtm1**
- ''--encrypt::' 暗号化オプション

### サーバーへの接続

VPN サーバーへの接続は pppd コマンドを使って以下のように行います。

```
 $ sudo pppd call pc1
```

これでVPN サーバーに接続されます。IPアドレスが上で設定したpc1のアドレス(192.168.22.10) 確認してみます。

```
 $ ifconfig ppp0
 
 ppp0      Link encap:Point-to-Pointプロトコル  
           inetアドレス:192.168.22.10  P-t-P:192.168.22.1  マスク:255.255.255.255
           UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1496  メトリック:1
           RXパケット:5 エラー:0 損失:0 オーバラン:0 フレーム:0
           TXパケット:5 エラー:0 損失:0 オーバラン:0 キャリア:0
           衝突(Collisions):0 TXキュー長:3 
           RXバイト:62 (62.0 B)  TXバイト:68 (68.0 B)
```

上で設定したIPアドレス 192.168.22.10 が割り当てられていることが確認できました。

### ルーティングの設定

以上の操作で pc1と pc0の間に VPN トンネルができました。従って、pc1からはpc0に対して192.168.22.1というIPアドレスがアクセス可能です。
しかし、VPN サーバーに接続された他のクライアントには到達できません。PC2 (192.168.22.11) を VPN 接続した状態で ping を打ってみます。

```
 $ ping 192.168.22.11
 PING 192.168.22.11 (192.168.22.11) 56(84) bytes of data.
```

このように表示され止まってしまいます。Ctrl+Cで抜けてください。

VPN クライアント間で通信できるようにルーティングを設定します。

```
 $ sudo route add -net 192.168.22.0 gw 192.168.22.1 netmask 255.255.255.0
```

再度 ping を打って確かめます。

```
 $ ping 192.168.22.11
 PING 192.168.22.11 (192.168.22.11) 56(84) bytes of data.
 64 bytes from 192.168.22.11: icmp_seq=1 ttl=127 time=46.2 ms
 64 bytes from 192.168.22.11: icmp_seq=2 ttl=127 time=32.3 ms
 64 bytes from 192.168.22.11: icmp_seq=3 ttl=127 time=29.8 ms
 ^C
 --- 192.168.22.11 ping statistics ---
 3 packets transmitted, 3 received, 0% packet loss, time 2003ms
 rtt min/avg/max/mdev = 29.868/36.146/46.203/7.185 ms
```

これで、別のクライアントにも到達できるようになりました。

### VPN の切断

VPN から切断するときは pkill を使ってpptpのプロセスをkillします。

```
 $ sudo pkill pptp
```

## VPN クライアントの設定(Windows)

Widnows では標準で VPN が組み込まれており、ウィザードを利用して簡単に VPN をセットアップすることができます。

### VPN 設定ウィザード

まず、コントロールパネルから「ネットワークと共有センター」を開きます。
「ネットワーク設定の変更」→「新しい接続またはネットワークのセットアップ」をクリックします。

<div align="center"><a href="vpn_windows_00.png"><img src="vpn_windows_00.png" width="80%;"></a></div>
<div align="center"><strong>ネットワークと共有センター</strong></div>

すると、以下の画面「接続またはネットワークのセットアップ」に遷移します。ここで [職場に接続します] をクリックし [次へ] ボタンをクリックします。

<div align="center"><a href="vpn_windows_01.png"><img src="vpn_windows_01.png" width="80%;"></a></div>
<div align="center"><strong>接続またはネットワークのセットアップ</strong></div>

次に新規接続を作成します。上のラジオボタン「いいえ、新しい接続を作成します」を選択し [次へ] ボタンをクリックします。

<div align="center"><a href="vpn_windows_02.png"><img src="vpn_windows_02.png" width="80%;"></a></div>
<div align="center"><strong>職場への接続(1)：新しい接続の作成</strong></div>

次に接続方法を選びます。ここでは VPN を選択してください。

<div align="center"><a href="vpn_windows_03.png"><img src="vpn_windows_03.png" width="80%;"></a></div>
<div align="center"><strong>職場への接続(2)：VPN の使用</strong></div>

次に VPN サーバーのアドレスと接続名を入力します。VPN のサーバー名または IPアドレスを入力してください。接続先の名前は接続を他と区別するためにつける名前です。ここでは RTM-VPN としました。

<div align="center"><a href="vpn_windows_04.png"><img src="vpn_windows_04.png" width="80%;"></a></div>
<div align="center"><strong>職場への接続(3)：サーバーアドレスの設定</strong></div>

次にユーザー名とパスワードを入力します。サーバー上で設定したユーザー名とパスワードを入力します。ここでは pc2/openrtm2 を設定しています。最後に [接続] ボタンをクリックして接続します。

<div align="center"><a href="vpn_windows_05.png"><img src="vpn_windows_05.png" width="80%;"></a></div>
<div align="center"><strong>職場への接続(4)：ユーザー名とパスワードの入力</strong></div>

接続には10数秒程度かかります。

<div align="center"><a href="vpn_windows_06.png"><img src="vpn_windows_06.png" width="80%;"></a></div>
<div align="center"><strong>職場への接続(5)：接続中</strong></div>

接続が完了すると以下の画面になります。

<div align="center"><a href="vpn_windows_07.png"><img src="vpn_windows_07.png" width="80%;"></a></div>
<div align="center"><strong>職場への接続(6)：接続完了</strong></div>

### ルーティングの設定

上述の Linux の場合と同様に、ルーティングの設定をする必要があります。

まず、コマンドプロンプトを管理者権限で開きます。
スタートメニューの「プログラムとファイルの検索」に **cmd** と入力し Ctrl+Shift+Enter を押します。
画面全体が暗くなりユーザーアカウント制御のダイアログが現れますので [はい] をクリックして続けます。

```
 C:\> route add 192.168.22.0 mask 255.255.255.0 192.168.22.1
```

ipconfig コマンドで VPN のアドレスが 192.168.22.11 になっていることを確認します。

```
 C:\> ipconfig
```

さらに、もう一つのクライアント pc1 に対して ping を打ってみます。

```
 C:\ ping 192.168.22.11
```

これで ping が通っていれば VPN 接続成功です。

### VPNの接続・切断

VPN の切断は「ネットワークと共有センター」から右の「アダプタの設定の変更」を選択します。

<div align="center"><a href="vpn_windows_00.png"><img src="vpn_windows_00.png" width="80%;"></a></div>
<div align="center"><strong>ネットワークと共有センター</strong></div>

アダプタの一覧の中に RTM-VPN がありますので、右クリックで「切断」を選ぶと切断できます。
再度接続する場合もこの画面から RTM－VPN を右クリックし「接続」を選ぶことで接続できます。

<div align="center"><a href="vpn_windows_08.png"><img src="vpn_windows_08.png" width="80%;"></a></div>
<div align="center"><strong>アダプタの設定の変更</strong></div>

## RTC等の設定

以上の設定で VPN ネットワークが構成できました。このネットワーク上で RTC を動作させるための設定を行います。

### ネームサーバー

ネームサーバーは VPN サーバーと同じ pc0 上で動作させることになっていました。
VPN 接続後 rtm-naming コマンドでネームサーバーを再起動します。

```
 $ rtm-naming
```

### RTCの設定 (rtc.conf)


VPN サーバー(pc0)または VPN クライアント(pc1,pc2,pc3)上で RTC を動作させる場合は、以下のように endpoint を設定します。

```
 [pc0用のrtc.conf]
 corba.nameservers: 192.168.22.1
 corba.endpoints: 192.168.22.1
```
　
```
 [pc1用のrtc.conf]
 corba.nameservers: 192.168.22.1
 corba.endpoints: 192.168.22.10
```
　
```
 [pc2用のrtc.conf]
 corba.nameservers: 192.168.22.1
 corba.endpoints: 192.168.22.11
```
　
```
 [pc3用のrtc.conf]
 corba.nameservers: 192.168.22.1
 corba.endpoints: 192.168.22.12
```

これで、すべてのRTC間通信はVPNを通じて行われます。

## パフォーマンス

VPN 接続経由で通信すると、通常よりもパフォーマンスが低下する場合があります。
パフォーマンスを上げる方法に関してはここでは詳しく述べませんが、簡単なベンチマークとしてカメラコンポーネントとビューアコンポーネントで画像の転送を行った場合のパフォーマンスの例を挙げます。

- pc0
  - Ubuntu 10.04 x86_64
  - Dell PowerEdge 2900
    - Intel(R) Xeon(R) CPU X5450 @3.00GHz x2
    - Memory 16GB

- pc1
  - Ubuntu 10.04 i386
  - VMware Fusion 6 (on Mac Book Retina 2.7GHz Corei7, 16GB Memory, OS X 10.9)
    - 2.7GHz Corei7 x2
    - Memory 1GB

- pc2
  - Windows7 64bit
  - VMware Fusion 6 (on Mac Book Retina 2.7GHz Corei7, 16GB Memory, OS X 10.9)
    - 2.7GHz Corei7 x2
    - Memory 4GB

<table class="table-alt">
  <tr>
    <th></th>
    <th>通常</th>
    <th>暗号化あり</th>
    <th>暗号化なし</th>
  </tr>
  <tr>
    <td>pc1->pc2 (VGA)</td>
    <td>8 fps</td>
    <td>0.5 fps</td>
    <td>1.1 fps</td>
  </tr>
  <tr>
    <td>pc2->pc1 (QVGA)</td>
    <td>22 fps</td>
    <td>2.3 fps</td>
    <td>5.8 fps</td>
  </tr>
</table>

暗号化ありの場合と無しの場合では約倍程度の速度の差がありますが、いずれの場合も通常の通信時に比べ1/10～1/20程度の速度になっていることがわかります。
Windows の VPN が特に遅いという報告もありますが、詳細は不明です。

