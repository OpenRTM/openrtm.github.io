---
layout: page
title: sdカードの準備
---
<!-- Title: SDカードの準備 -->
<!-- -*- pukiwiki-edit -*- -->
#contents

## はじめに

ここでは、Raspberry Pi用 RTC(以下、RPI RTC)を動作させるための実行環境のインストールについて説明します。

なお、以下のインストール手順は、Windows 環境を前提としています｡
Windows 環境以外をご使用の方は以下のサイトなどをご参照ください｡

- [http://elinux.org/RPi_Easy_SD_Card_Setup](http://elinux.org/RPi_Easy_SD_Card_Setup)

ここでは、Raspberry Pi オフィシャルサイトから OSイメージをダウンロードし、各種セットアップについて説明します。
Raspberry Pi上で OpenRTM を使用できるようにするまでの大まかな手順は以下の通りです。

- SDカードに OSイメージを書き込む
- OSの基本的なセットアップ
- OpenRTM-aist のインストール
- コンポーネントの実行テスト

なお、OpenRTM-aist のインストールや、Kobuki コンポーネントがすでにインストールされたイメージをこちらに用意していますので、以下の手順はスキップすることができます。

- OpenRTM-aist のインストール(未)
- Kobuki コンポーネントのインストール(未)
- PiRT-Unit用セットアップ(未)

## SDカードの容量

使用する SDカードは最低 **2GB** 必要ですが、実際の使用では **4GB以上が必要** になります。必ず4GB以上の SDカードを用意してください。

## イメージのダウンロード

以下のサイトから、Raspberry Pi用 OS Raspbian “wheezy”をダウンロードします｡
Raspbian は Debian ベースのRaspberryPi用 Linux ディストリビューションです。
<!-- wheezyには armhf と armel の二つのタイプがありますが、''armhf'' を使用してください。 -->

- Raspbian Wheezy: [http://www.raspberrypi.org/downloads](http://www.raspberrypi.org/downloads)

<div align="center"><a href="raspbian_download_site2.png"><img src="raspbian_download_site2.png" width="80%;"></a></div>
<div align="center"><strong>Raspbian のダウンロード</strong></div>

ダウンロードしたファイル YYYY-MM-DD-wheezy-raspbian.zip を展開してください。
YYYY-MM-DD-wheezy-raspbian.img という2GB位のファイルが展開されているはずです。

```
 $ ls -al 
 total 4752840
 drwxr-xr-x  4 n-ando  staff         136  5 18 13:30 .
 drwxr-xr-x  9 n-ando  staff         306  5 18 13:30 ..
```
 -rw-r--r--  1 n-ando  staff  1939865600  2  9 12:44 2013-02-09-wheezy-raspbian.img
 -rwxr-xr-x  1 n-ando  staff   493587826  5  7 21:08 2013-02-09-wheezy-raspbian.zip

うまく展開できない場合、ダウンロードに失敗しファイルが壊れている可能性があります。壊れたファイルを削除して、再度ダウンロードしてみてください。

## イメージの書き込み

展開された yyyy-mm-dd-hweezy-raspbian.img はイメージファイルといい、Raspbian が起動するディスクの状態をディスクの最初から最後まで1バイトづつ抜き出したものです。
<span style="color:red;">このファイルをSDカードに単純にコピーしても使用することはできません！！</span>;

以下に説明する方法で SDカードに書き込んでください。

### イメージの書き込み (Windows)

Windows では Win32DiskImager というツールを使用することでイメージの書き込みができます。
以下のサイトからイメージデータ書き込みツール Win32DiskImager のバイナリをダウンロードします｡

- Win32DiskImager: [http://sourceforge.jp/projects/sfnet_win32diskimager/](http://sourceforge.jp/projects/sfnet_win32diskimager/)

<div align="center"><a href="win32diskimager_site.png"><img src="win32diskimager_site.png" width="80%;"></a></div>
<div align="center"><strong>Win32DiskImager のダウンロード</strong></div>

ダウンロードしたファイル (win32diskimager-vX.X-binary.zip ) を解凍します｡

<span style="color:red;">※Win32DiskImager は、2バイト文字に対応していないため、YYYY-MM-DD-wheezy-raspbian.zip は途中のパス名に全角文字や空白が含まれていない場所に解凍してください｡</span>;

Raspberry Pi で使用する SDカードをPCに挿入し、Win32DiskImager を起動します｡

<span style="color:red;">※SDカードはドライブとして認識されている必要があるので、事前に FAT32 形式でフォーマットしておいてください｡</span>;

｢Image File｣に解凍したRaspbian のイメージファイル (YYYY-MM-DD-wheezy-raspbian.img)、｢Drive｣に SDカードのドライブを指定し、｢Write｣ ボタンをクリックします｡

<div align="center"><a href="win32diskimager.png"><img src="win32diskimager.png" width="80%;"></a></div>
<div align="center"><strong>イメージデータの書き込み</strong></div>

以上で SDカードの準備は終了です｡
書き込みが終了したら、SDカードを Raspberry Pi に設置し、電源を投入します。

### イメージの書き込み (Linux)

Linux では ddコマンドを利用してイメージの読み書きができます。
ddコマンドは UNIX系の OSなら大抵デフォルトでインストールされています。

SDカードを差し込んでから、 dmesg コマンドでカーネルのメッセージを確認します。
```
 $ dmesg
   : 中略
 [333478.822170] sd 3:0:0:0: [sdb] Assuming drive cache: write through
 [333478.822174]  sdb: sdb1 sdb2
 [333478.839563] sd 3:0:0:0: [sdb] Assuming drive cache: write through
 [333478.839567] sd 3:0:0:0: [sdb] Attached SCSI removable disk
 [333479.094873] EXT4-fs (sdb2): mounted filesystem with ordered data mode
 [333527.658195] usb 1-1: USB disconnect, address 2
```

このメッセージから SDカードのデバイス名を確認します。この例では sdb が SDカードのデバイス名のようです。/dev/ の下を見てみます。

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
その場合、ディスクをアンマウントしてください。(Ubuntuではデスクトップにマウントしたファイルシステムのフォルダーが現れるので右クリックで取り外してください。それ以外は umount コマンドでアンマウントします。)

<div align="center"><a href="ubuntu_adcard_mount.png"><img src="ubuntu_adcard_mount.png" width="50%;"></a></div>
<div align="center"><strong>Ubuntu上でマウントされた SDカード(右クリックメニューで取り外すことができる)</strong></div>

**dd if=イメージファイル of=SDカードのデバイスファイル bs=1M** のようにコマンドを入力し実行します。
ただし、デバイスファイルへの書き込みは管理者(root)権限が必要ですので、sudo を使用してください。

```
 $ unzip  2013-02-09-wheezy-raspbian.zip
 Archive:  2013-02-09-wheezy-raspbian.zip
   inflating: 2013-02-09-wheezy-raspbian.img
 $ sudo dd if=2013-02-09-wheezy-raspbian.img of=/dev/sdb bs=1M
 1850+0 records in
 1850+0 records out
 1939865600 bytes (1.9 GB) copied, 201.543 s, 9.6 MB/s
```

実行中は別のターミナルなどで、iostat コマンドを実行して書き込みが正しく行われているかどうか見ることができます。
(最近のディストリビューションではデフォルトでインストールされていないことがあります。debian/ubuntu では apt-get install sysstat で iostat コマンドが使えるようになります。)

```
 $ iostat -mx 1
  avg-cpu:  %user   %nice %system %iowait  %steal   %idle
            0.00    0.00    0.00   50.25    0.00   49.75
 
 Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await  svctm  %util
 sda               0.00     0.00    0.00    1.00     0.00     0.00     8.00     0.00    0.00   0.00   0.00
 sdb               0.00  1856.00    0.00   78.00     0.00     9.14   240.00   143.40 1855.85  12.82 100.00
```

sdb の項目を見ると 9.14MB/sの書き込み速度が出ていることがわかります。
class 6 の SDカードなら 6MB/sec, class 10の SDカードなら 10MB/sec 程度の速度が出ていれば、問題なく書き込まれていると考えてよいでしょう。
書き込みが終了すると、ディストリビューションによっては自動でマウントされる場合があります。その場合、アンマウントしてからSDカードを抜いてください。

### イメージの書き込み (Mac OS X)

Mac OS Xも Linux と同様 ddコマンドを利用して書き込みます。
ただし、Mac では SDカードを挿入すると自動的にマウントされてしまい、マウント中は ddコマンドで SDカードに書き込むことができないので、アンマウント (OSから取り外す) する必要があります。

SDカードを差し込むと Finder に図のように SDカードのアイコンが現れます。
アンマウントするつもりで**イジェクトボタンを押さないよう**気を付けてください。

<div align="center"><a href="sdcard_mac.png"><img src="sdcard_mac.png" width="60%;"></a></div>
<div align="center"><strong>Mac にマウントされた SDカード</strong></div>

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
このSDカードを一旦アンマウント します。diskutil というコマンドを使用し **diskutil umount <マウントポイント>** のように入力します。

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
次にddコマンドを使用してイメージを書き込みます。
**dd if=イメージファイル of=/dev/rdisk1 bs=1m** のように入力します。
of=/dev/rdisk1 は先ほど覚えたデバイスファイル /dev/disk1s1 のうち後ろの **s1** を取り、さらにdiskの前に raw deviceであることを示す **r** を付けたデバイス名です。

このコマンドはデバイスファイルにアクセスするので管理者 (root) でなければ実行できません。sudoを使用して以下のように実行します。

```
 $ sudo dd if=2013-02-09-wheezy-raspbian.img of=/dev/rdisk1 bs=1m
 1850+0 records in
 1850+0 records out
 1939865600 bytes transferred in 302.377337 secs (6415380 bytes/sec)
 $
```

書き込み中は、「アクティビティモニタ」で「ディスクの動作」を見ることで書き込みが正しく行われているかどうかわかります。
class 6 の SDカードなら 6MB/sec, class 10の SDカードなら 10MB/sec 程度の速度が出ていれば、問題なく書き込まれていると考えてよいでしょう。

書き込みが終了すると、自動的に再度マウントされますので、今度は Finder のイジェクトボタンを押して SDカードを抜きます。



