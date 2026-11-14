---
layout: page
title: 玄箱hgへのインストール
---

<!-- Title: 玄箱HGへのインストール -->
#contents

<div align="center"><a href="kuro-box_hg_0.jpg"><img src="kuro-box_hg_0.jpg" width="100;"></a></div>

## 玄箱/HGスペック
<table class="table-alt">
  <tr>
    <td>CPU</td>
    <td>PowerPC 267MHz</td>
  </tr>
  <tr>
    <td>RAM</td>
    <td>128MB</td>
  </tr>
  <tr>
    <td>Flash ROM</td>
    <td>4MB</td>
  </tr>
  <tr>
    <td>LAN</td>
    <td>1000BASE-T/100BASE-TX/10BASE-T×1ポート</td>
  </tr>
  <tr>
    <td>外部IO</td>
    <td>USB2.0×2ポート</td>
  </tr>
  <tr>
    <td>HDD</td>
    <td>3.5インチUltraATA 1個を別途用意．</td>
  </tr>
  <tr>
    <td>OS</td>
    <td>デフォルトではMontavista Linux（Kernel2.4.17）</td>
  </tr>
</table>

## インストールの流れ
Debian、Vine、GentooLinux が動作するようであるが、パッケージの豊富さ、アップグレードのしやすさから Debian が最適でしょう。
大まかな手順は以下の通りです。

1. [玄箱うぉううぉう♪](http://kuro.dsk.jp/)から Debian イメージをダウンロードする
1. 玄箱付属CDに同封されている KuroBoxSetup.exe を使ってイメージを玄箱へ展開する
1. この段階では Debian3.0 (Woody) なので、Debian3.1(Sarge) へアップグレードする
1. pkg_install_debianSarge.sh でパッケージをインストールする
1. OpenRTM-aist-0.4.0 をビルド、インストールする

このように、Debian インストール後は、i386 の Debian と同じ手順でインストールすることができます。


## OS の入れ替え
### カーネルイメージの入手 
<!-- OS の入れ替え方法については[[玄箱ＨＧハック:http://kurobox.ath.cx/]](リンク切れ)の[[Debian化:http://kurobox.ath.cx/?Debian%B2%BD]](リンク切れ)がわかりやすい。ただし、[[玄箱うぉううぉう♪:http://kuro.dsk.jp/]]提供のイメージへのリンクが古いので、以下からダウンロードしてください。 -->
OS の入れ替え方法については、以下からダウンロードしてください。

ダウンロードしたイメージを、この後の手順で必要な名前にリネームしてZIP圧縮したものを以下に置きます。

- [image.zip]()（リンク切れです）
  - これを玄箱付属 CD-ROM内のファイル image.zip と入れ替える。
- [玄箱うぉううぉう♪](http://kuro.dsk.jp/)さんオリジナル配布物
  - ※玄箱うぉううぉう♪さんでは再配布推奨をしてるのでミラーしてます
  - [debian_2006_06_10_dist.tar.gz]()（リンク切れです）
  - [install_debian.txt]()（リンク切れです）
  - [install_debian_standalone.txt]()（リンク切れです）

### インストーラの準備
玄箱付属 CD-ROMの内容を適当なディレクトリーにコピーします。
KuroBoxSetup.exe が存在する場所(CD-ROMのルート)にある image.zip を image.zip.org などにリネームし、上記でダウンロードした image.zip を代わりにここに置きます。

### EMモードにする
玄箱を EMモードにします。[参考](http://www.yamasita.jp/linkstation/tips/em-mode.html)

EMモードはインストーラが認識可能なモードで、KuroBoxSetup.exe を使ってイメージを転送するにはこのモードにする必要があります。
購入直後、HDDを繋いだばかりのときはこのモードになっています。

すでに玄箱付属の Linux をインストールしてしまっている場合は、以下のように EMモードにすることができます.

- EMモードにする
```
 # echo -n 'NGNG' > /dev/fl3
   もしくは
 # /usr/bin/write_ng
 # reboot
```
電源を切り, 再度電源を入れる

- EMモードから戻る
```
 # echo -n 'OKOK' > /dev/fl3
   もしくは
 # /usr/bin/write_ok
 # reboot
```

 あるいは、HDDのファイルシステムを破壊することで強制的に EMモードにすることができます。
```
 # rm -rf /
   あるいは
 # dd if=/dev/zero of=/dev/hda bs=1024 count=1024
```

### イメージの転送
玄箱が EMモードになったら, 先ほど Debian のイメージに入れ替えた玄箱インストーラの KuroBoxSetup.exe を起動して、新しいイメージでセットアップします。
KuroBoxSetup.exe を起動しても「玄箱が見つかりません」というメッセージが表示されたら、EMモードになっていない可能性があります。
何事もなければ、セットアップは完了して、玄箱再起動後, 使用可能になります。

### 設定 
上記の Debianイメージに入れ替えた玄箱のデフォルトの設定は以下のようになっています。
<table class="table-alt">
  <tr>
    <th colspan="2" style="text-align: center;">デフォルトユーザー</th>
  </tr>
  <tr>
    <td>ユーザー名</td>
    <td>tmp-kun</td>
  </tr>
  <tr>
    <td>パスワード</td>
    <td>tmp-kun</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">root</td>
  </tr>
  <tr>
    <td>ユーザー名</td>
    <td>root</td>
  </tr>
  <tr>
    <td>パスワード</td>
    <td>root</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">ネットワーク設定</td>
  </tr>
  <tr>
    <td>IPアドレス</td>
    <td>192.168.0.100</td>
  </tr>
  <tr>
    <td>Gatewayアドレス</td>
    <td>192.168.0.1</td>
  </tr>
  <tr>
    <td>DNSアドレス</td>
    <td>192.168.0.1</td>
  </tr>
</table>

IPアドレスは固定です。
設定を行う PC にはターミナルソフトをインストールして、IPアドレスを玄箱につながるように(192.168.0.1 mask 255.255.255.0 など) 設定して LAN で接続します.

```
 telnet 192.168.0.100
 Debian GNU/Linux 3.0 KURO-BOX
 KURO-BOX login: tmp-kun
 Password: tmp-kun
 中略:
 Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
 permitted by applicable law.
 KURO-BOX:~> su
 # 
```

アカウント tmp-kun でログインし、rootになり設定を行います。

たとえば、IPアドレスを設定するには、# vi /etc/network/interfaces
- IPアドレスを編集
```
 # vi /etc/hosts.allow
 hosts.allowを編集
```

　IPアドレスを変更したとき、hosts.allowも忘れずに変更します。
これを忘れてデフォルトと違うネットワークアドレスにすると二度とログインできなくなります。

### Sargeをアップグレード
この段階では Debian3.0(Woody) がインストールされている。
現行バージョン Debian3.1(Sarge) にアップグレードする。

#### /etc/apt/sources.listの編集
デフォルトの/etc/apt/sources.lismaruiha\tはsources.list.orgなどにリネームし、以下の2行をsources.listに新たに記述する。

```
 deb http://cdn.debian.or.jp/debian/ sarge main contrib non-free
 deb-src http://cdn.debian.or.jp/debian/ sarge main contrib non-free
```

編集が終わったら、

```
 apt-get update
 apt-get dist-upgrade 
```

アップグレードの際、いろいろと聞かれるが基本的にデフォルトでよい。
ただし、/etc/init.d/haltが書き換えられてしまい、電源ボタンによる shutdown が無効になってしまうので、 /etc/init.d/haltのPATH の次の行に

```
 PATH=/sbin:/bin:/usr/sbin:/usr/bin
 echo -n "EEEE" > /dev/ttyS1
 sleep 3
```

のように2行追加する.

### TIPS 
xterm、kterm をインストールしておくと、リモートからアクセスするとき便利なのですが、デフォルトのままでは xterm、kterm ともに pty 周りのエラーで立ち上がりません。
/etc/fstab を以下のように変更する必要があります。
```
 /etc/fstab
 none   /dev/pts     devpts  gid=5,mode=20           0 0
 ↓このように変更
 none   /dev/pts     devpts  gid=5,mode=620          0 0
```

xterm、kterm をインストールする。XLib 関係も同時にインストールされるので、容量に注意すること。
```
 # apt-get install xterm
 # apt-get install kterm
```

## OpenRTM-aist のビルド
### パッケージのインストール
パッケージのインストールには OpenRTM-aist-0.4.0 付属の Debian用パッケージインストーラ(pkg_install_debianSarge.sh)がそのまま使えます。
OpenRTM-aist-0.4.0 のソース展開後、root になり build ディレクトリーの下の pkg_install_debianSarge.sh を実行するだけです。

```
 > tar xvzf OpeNRTM-aist-0.4.0.tar.gz
 > cd OpenRTM-aist-0.4.0
 > cd build
 > ls
 略
 README.Debian  makewrapper.py             pkg_install_vl32.sh
 autogen        pkg_install_debianSarge.sh  pkg_install_vl4.sh
 略
 > su
 # ./pkg_install_debianSarge.sh
```

これでパッケージのインストールは完了です。

### OpenRTM-aistのビルド
以降は通常のPCと全く同じです。

```
 > cd OpenRTM-aist-0.4.0
 > ./configure
 > make
 > su
 # make install
```

ただし、ビルドにはかなりの時間(1時間45分前後)を要します。


```
 > time make
 6048.130u 156.950s 1:43:36.53 99.8%     0+0k 0+0io 762267pf+0w
```


## 謝辞
玄箱への OpenRTM-aist のインストールにあたり、(株)前川製作所 技術研究所 基盤技術開発G 山下智輝氏の OpenRTM-aist-0.2.0 インストールレポートが大変参考になりました。また、下記の Webページの参考にさせていただきました。ありがとうございました。

## リンク
- [KURO-BOX/HG](http://www.kuroutoshikou.com/products/kuro-box/kuro-box_hgfset.html)
- [玄箱うぉううぉう♪](http://kuro.dsk.jp/)
<!-- -[[玄箱ＨＧハック:http://kurobox.ath.cx/]](リンク切れ) -->
- [玄人指向 KURO-BOX/HG Webページ](http://kuroutoshikou.com/modules/display/?iid=122)
- [LinkStation／玄箱をハックしよう](http://www.yamasita.jp/linkstation/)


