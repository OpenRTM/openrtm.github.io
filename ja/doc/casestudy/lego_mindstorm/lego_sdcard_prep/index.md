---
layout: page
title: sd カードの準備
---

<!-- Title: SD カードの準備 -->
<!-- -*- pukiwiki-edit -*- -->
#contents

## はじめに

ここでは、LEGO Mindstorms EV3 上で OpenRTM-aist とそのコンポーネントを動作させるための実行環境のインストールについて説明します。

ここでは、openrtm.org が提供する OpenRTM-aist 入りの OSイメージをダウンロードし、各種セットアップについて説明します。
EV3上で OpenRTM を使用できるようにするまでの大まかな手順は以下の通りです。

- SDカードに OSイメージを書き込む
- OS の基本的なセットアップ
- コンポーネントの実行テスト

## SD カード

EV3 には micro SD カードスロットが一つあり、ここに起動した OS を書き込んだ micro SD カードを差し込むと、任意の OS を起動することができます。

用意する SDカードは 2GB以上 32GB以下のも **micro SDカード** になります。mini SD や SDカードは刺さりませんのでご注意ください。
また、書き込むイメージは約2GB程度ありますので、最低で2GBの容量が必要となります。EV3 は 32GBより大きい SDXC仕様の SDカードには対応していませんので、注意してください。

- 用意するSDカード
  - micro SDカード
  - 2GB以上、32GB以下

## OSイメージのダウンロード

EV3上 での OpenRTM-aist の実行には ev3dev という OS を使用します。

- ev3dev Webページ: http://www.ev3dev.org

以下のサイトから ev3-ev3dev-jessie-2015-12-30.img.zip をダウンロードしてください。
名前が似たファイルが多数配布されているので間違えないようにしてください。

- https://github.com/ev3dev/ev3dev/releases

### ev3dev OSイメージのダウンロード

ev3dev とは EV3 上で Linux のディストリビューションの1つである、Debian GNU Linuxを EV3 に搭載した EV3用の Debian ディストリビューションです。
OpenRTM-aist を動作させるには、この ev3dev を micro SDカードに書き込み、EV3 を SDカードから起動させます。

上記の ev3dev オフィシャルWebページから ev3dev の OSイメージファイルがダウンロードできますが、OpenRTM-aist などはインストールされていません。
基本的には、以下のリンクから OpenRTM-aist (C++、Python) 入りの ev3dev イメージファイルをダウンロードしてください。


- [2015-08-05-ev3dev-openrtm.zip]({{ site.baseurl }}/ja/)

### サンプルコンポーネント入りのイメージ
Educator Vehicle等のサンプルコンポーネント入りのイメージです。

- [ev3-openrtm.img](https://drive.google.com/a/nobu777.net/uc?export=download&confirm=A1zJ&id=1nJ552cMdYkgDdRtF0RHYfkL1Bqu300Kv)


EV3の無線LANアダプタを交換した場合に、無線LANアクセスポイントモードが正常に動作しない場合があります。
その場合は他のアクセスポイントに接続する等して、以下のコマンドを実行して**70-persistent-net.rules**を編集します。
ユーザー名は**robot**、パスワードは**maker**でログインして操作してください。

```
 sudo nano /etc/udev/rules.d/70-persistent-net.rules
```


具体的には70-persistent-net.rulesのSUBSYSTEMから始まる行を全てコメントアウトします。

```
 # USB device 0x:0x (rtl8192cu)
 SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:22:cf:f6:52:a5", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="wlan*", NAME="wlan1"
```

### イメージの展開

ダウンロードしたファイル YYYY-MM-DD-ev3dev-openrtm.zip を展開してください。
YYYY-MM-DD-ev3dev-openrtm.img という2GB位のファイルが展開されているはずです。

#### Windows

ファイルを右クリックして「すべて展開」を選択すると、展開できます。

#### Linux

```
 $ unzip <イメージファイル>
```

で展開できます。unzip コマンドがない場合はインストールしてください。

```
 $ unzip 2015-08-06-ev3dev-openrtm.zip
 Archive:  2015-08-06-ev3dev-openrtm.zip
   inflating: 2015-08-06-ev3dev-openrtm.img
 $ ls -l
 合計 2321300

 -rw-rw-r-- 1 n-ando n-ando 1887436800  8月  4 21:37 2015-08-06-ev3dev-openrtm.img
 -rw-rw-r-- 1 n-ando n-ando  489565916  8月  5 10:13 2015-08-06-ev3dev-openrtm.zip
```

うまく展開できない場合、ダウンロードに失敗しファイルが壊れている可能性があります。壊れたファイルを削除して、再度ダウンロードしてみてください。

## イメージの書き込み

展開された yyyy-mm-dd-ev3dev-openrtm.img はイメージファイルといい、ev3dev が起動するディスクの状態をディスクの最初から最後まで1バイトづつ抜き出したものです。
<span style="color:red;">このファイルを SDカードに単純にコピーしても使用することはできません！！</span>;

以下に説明する方法で SDカードに書き込んでください。

### イメージの書き込み (Windows)

Windows では Win32DiskImager というツールを使用することでイメージの書き込みができます。
以下のサイトからイメージデータ書き込みツール Win32DiskImager のバイナリをダウンロードします｡

- Win32DiskImager: http://sourceforge.jp/projects/sfnet_win32diskimager/

<div align="center"><a href="win32diskimager_site.png"><img src="win32diskimager_site.png" width="80%;"></a></div>
<div align="center"><strong>Win32DiskImager のダウンロード</strong></div>

ダウンロードしたファイル (win32diskimager-vX.X-binary.zip ) を解凍します｡

<span style="color:red;">※Win32DiskImager は、2バイト文字に対応していないため、YYYY-MM-DD-ev3dev-openrtm.zip は途中のパス名に全角文字や空白が含まれていない場所に解凍してください｡</span>;

Raspberry Pi で使用する SD カードを PCに挿入し、Win32DiskImager を起動します｡

<span style="color:red;">※SD カードはドライブとして認識されている必要があるので、事前に FAT32 形式でフォーマットしておいてください｡</span>;

｢Image File｣に解凍したRaspbian のイメージファイル (YYYY-MM-DD-wheezy-raspbian.img)、｢Drive｣にSD カードのドライブを指定し、｢Write｣ボタンをクリックします｡

<div align="center"><a href="win32diskimager.png"><img src="win32diskimager.png" width="70%;"></a></div>
<div align="center"><strong>イメージデータの書き込み</strong></div>

以上で SD カードの準備は終了です｡
書き込みが終了したら、SD カードを Raspberry Pi に設置し、電源を投入します。

### イメージの書き込み (Linux)

Linux では dd コマンドを利用してイメージの読み書きができます。
dd コマンドは UNIX系の OS なら大抵デフォルトでインストールされています。

SDカードを差し込んでから、 dmesg コマンドでカーネルのメッセージを確認します。
```
 $ dmesg
```
   : 中略
```
 [333478.822170] sd 3:0:0:0: [sdb] Assuming drive cache: write through
 [333478.822174]  sdb: sdb1 sdb2
 [333478.839563] sd 3:0:0:0: [sdb] Assuming drive cache: write through
 [333478.839567] sd 3:0:0:0: [sdb] Attached SCSI removable disk
 [333479.094873] EXT4-fs (sdb2): mounted filesystem with ordered data mode
 [333527.658195] usb 1-1: USB disconnect, address 2
```

このメッセージから SDカードのデバイス名を確認します。この例では sdb が SDカードのデバイス名のようです。/dev/の下を見てみます。

```
 ls -al /dev/sd*
 brw-rw---- 1 root disk 8,  0 May  7 17:28 /dev/sda
 brw-rw---- 1 root disk 8,  1 May  7 17:28 /dev/sda1
 brw-rw---- 1 root disk 8,  2 May  7 17:28 /dev/sda2
 brw-rw---- 1 root disk 8,  5 May  7 17:28 /dev/sda5
 brw-rw---- 1 root disk 8, 16 May 18 14:19 /dev/sdb
 brw-rw---- 1 root disk 8, 17 May 18 14:19 /dev/sdb1
 brw-rw---- 1 root disk 8, 32 May 18 14:19 /dev/sdc
```

sda は大抵システムディスクなので、**絶対**に触ってはいけません。

ディストリビューションによっては、SDカード内にマウント可能なファイルシステムがある場合自動でマウントするケースもあるようです。
その場合、ディスクをアンマウントしてください。(Ubuntuではデスクトップにマウントしたファイルシステムのフォルダーが現れるので右クリックで取り外してください。
それ以外は umount コマンドでアンマウントします。)

<div align="center"><a href="ubuntu_adcard_mount.png"><img src="ubuntu_adcard_mount.png" width="50%;"></a></div>
<div align="center"><strong>Ubuntu場でマウントされたSDカード(右クリックメニューで取り外すことができる)</strong></div>

**dd if=イメージファイル of=SDカードのデバイスファイル bs=1M** のようにコマンドを入力し実行します。
ただし、デバイスファイルへの書き込みは管理者(root)権限が必要ですので、sudoを使用してください。

```
 $ sudo dd if=2015-08-05-ev3dev-openrtm.img of=/dev/sdb bs=1M
 1850+0 records in
 1850+0 records out
 1939865600 bytes (1.9 GB) copied, 201.543 s, 9.6 MB/s
```

実行中は別のターミナルなどで、iostat コマンドを実行して書き込みが正しく行われているかどうか見ることができます。
(最近のディストリビューションではデフォルトでインストールされていないことがあります。debian/ubuntu では apt-get install sysstat で iostatコマンドが使えるようになります。)

```
 $ iostat -mx 1
  avg-cpu:  %user   %nice %system %iowait  %steal   %idle
            0.00    0.00    0.00   50.25    0.00   49.75
 
 Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await  svctm  %util
 sda               0.00     0.00    0.00    1.00     0.00     0.00     8.00     0.00    0.00   0.00   0.00
 sdb               0.00  1856.00    0.00   78.00     0.00     9.14   240.00   143.40 1855.85  12.82 100.00
```

sdb の項目を見ると 9.14MB/s の書き込み速度が出ていることがわかります。
class 6 のSDカードなら 6MB/sec, class 10 の SDカードなら 10MB/sec 程度の速度が出ていれば、問題なく書き込まれていると考えてよいでしょう。
書き込みが終了すると、ディストリビューションによっては自動でマウントされる場合があります。その場合、アンマウントしてから SDカードを抜いてください。

### イメージの書き込み (Mac OS X)

Mac OS X も Linuxと同様 dd コマンドを利用して書き込みます。
ただし、Mac では SDカードを挿入すると自動的にマウントされてしまい、マウント中は dd コマンドで SDカードに書き込むことができないので、アンマウント (OSから取り外す) する必要があります。

SDカードを差し込むとFinderに図のように SDカードのアイコンが現れます。
アンマウントするつもりで**イジェクトボタンを押さないよう**気を付けてください。

<div align="center"><a href="sdcard_mac.png"><img src="sdcard_mac.png" width="50%;"></a></div>
<div align="center"><strong>MacにマウントされたSDカード</strong></div>

SDカードのボリューム名はここでは **Untitled** です。ボリューム名を覚えておきます。
コマンドプロンプトから df コマンドを入力すると以下のように表示されます。

```
 $ df -k
 Filesystem                        1024-blocks      Used Available Capacity   iused    ifree %iused  Mounted on
 /dev/disk0s2                        500000000 437664508  62079492    88% 109480125 15519873   88%   /
 devfs                                     194       194         0   100%       679        0  100%   /dev
 map -hosts                                  0         0         0   100%         0        0  100%   /net
 map auto_home                               0         0         0   100%         0        0  100%   /home
 /dev/disk1s1                            57288     18992     38296    34%       512        0  100%   /Volumes/Untitled
```

```
 一番下 ''/Volumes/Untitled'' とあるのが先ほどの SDカードのマウントポイントです。一番左の SDカードのデバイス名 /dev/disk1s1 を覚えておきます。
```
この SDカードを一旦アンマウント します。diskutil というコマンドを使用し **diskutil umount <マウントポイント>** のように入力します。

```
 $ diskutil umount /Volumes/Untitled
 Volume (null) on disk1s1 unmounted
 $ df -k
 Filesystem                        1024-blocks      Used Available Capacity   iused    ifree %iused  Mounted on
 /dev/disk0s2                        500000000 437664716  62079284    88% 109480177 15519821   88%   /
 devfs                                     194       194         0   100%       679        0  100%   /dev
 map -hosts                                  0         0         0   100%         0        0  100%   /net
 map auto_home                               0         0         0   100%         0        0  100%   /home
```

先ほどの /Volumes/Untitled が消えて、SDカードがアンマウントされていることがわかります。
次に dd コマンドを使用してイメージを書き込みます。
**dd if=イメージファイル of=/dev/rdisk1 bs=1m** のように入力します。
of=/dev/rdisk1 は先ほど覚えたデバイスファイル /dev/disk1s1 のうち後ろの **s1** を取り、さらに disk の前に raw deviceであることを示す **r** を付けたデバイス名です。

このコマンドはデバイスファイルにアクセスするので管理者 (root) でなければ実行できません。sudoを使用して以下のように実行します。

```
 $ sudo dd if=2015-08-05-ev3dev-openrtm.img of=/dev/rdisk1 bs=1m
 1850+0 records in
 1850+0 records out
 1939865600 bytes transferred in 302.377337 secs (6415380 bytes/sec)
 $
```

書き込み中は、「アクティビティモニタ」で「ディスクの動作」を見ることで書き込みが正しく行われているかどうかわかります。
class 6 の SDカードなら 6MB/sec, class 10のSDカードなら 10MB/sec 程度の速度が出ていれば、問題なく書き込まれていると考えてよいでしょう。

書き込みが終了すると、自動的に再度マウントされますので、今度は Finder のイジェクトボタンを押して SDカードを抜きます。

