---
layout: page
title: armadillo240へのインストール
---
<br>
<a>No English version available.
</a>


<!-- Title: Armadillo240へのインストール -->
#contents

<!-- CENTER:&ref(http://www.atmark-techno.com/files/images/a220/a220-angle-250.jpg,80%); &ref(http://www.atmark-techno.com/files/images/a240/a240-long-150.jpg,150%); -->

<!-- div align="center"><a href="https://www.atmark-techno.com/files/images/a220/a220-angle-250.jpg"><img src="https://www.atmark-techno.com/files/images/a220/a220-angle-250.jpg" width="80%;"></a></div>
<div align="center"><a href="https://www.atmark-techno.com/files/images/a240/a240-long-150.jpg"><img src="https://www.atmark-techno.com/files/images/a240/a240-long-150.jpg" width="80%;"></a></div-->


Armadillo240は　[アットマークテクノ](http://www.atmark-techno.com/)から販売されている、ARM を搭載した Linux 搭載可能な小型 CPU ボードです。
Atmark Techno, Inc.から、ATDE2 (Atmark Techno Development Environment)と、GNU クロス開発ツール、AtmarkDist という3つの開発ツールが提供され、簡単にクロス開発を行うことができます。<br>
ここでは、Armadillo で実行できる RTコンポーネントの実行ファイルをクロス開発します。 その後、Armadillo 起動後、RTコンポーネントが自動で起動するイメージファイル(romfs：ルートファイルシステム)を作成します。

## 作業の流れ 
- クロス開発環境の整備
- ATDE2 の整備（必要なパッケージのインストール）
- OpenRTM-aist のクロスコンパイルとインストール
- RTコンポーネントのクロスコンパイル
- Armadillo240 上で実行ファイルを起動
- Armadillo240 のイメージファイルを作成
- RtcLink 上で動作確認

## クロス開発環境の構築 
Armadillo で実行できる RTコンポーネントの実行ファイルをクロスコンパイルで作成します。 Atmark Techno, Inc.から Armadilloシリーズの開発環境が VMイメージで配布されており、クロス開発環境に必要なツールが事前にインストールされています。
### ATDE2 と VMware のダウンロード
:**ATDE2** | ATDE2(Atmark Techno Development Environment)は AtmarkTechno から配布されている Admadillo のクロス開発環境のための VMware用の仮想PCイメージです。実体は Debian GNU Linux で、クロス開発に必要なツールチェーンがあらかじめインストールされています。
  - [こちら](http://armadillo.atmark-techno.com/downloads)のページから無料で入手できます。

:**VMware Player** | VMware Inc. からフリーで配布されている仮想PCソフトで、VMware の仮想PCイメージを実行することができます。ATDE2 を起動するために必要です。Windows版と Linux版がありますが、以下、Windows版 の VMware Player を使用するものとして進めます。
  - [こちら](http://www.vmware.com/products/player/)のページから無料で入手できます。

### ATDE2 と VMwareの起動 
- VMware で ATDE2 を起動します。

※ATDE2-20071018.zip を解凍し、解凍したフォルダの中の ATDE2.vmx をダブルクリック、または VMwareのfile > Open から解凍したフォルダーの中の ATDE2-20071018のATDE2.vmx を選択してください。<br>

<div align="center"><a href="ATDE.png"><img src="ATDE.png" width="50%;"></a></div>
<div align="center"><strong>VMwareでATDE2を起動</strong></div>

- ”この仮想マシンを起動”で起動します。
- ログイン作業は無しで、ATDE2 の Desktop が表示されます。

### ATDE2 開発環境の整備 
ATDE2 はすでにクロスコンパイル環境が整っていますが、OpenRTM の RTコンポーネントをクロス開発できる環境に整える必要があります。
起動したATDE2 上で以下のソースとシェルスクリプトをダウンロードしホームディレクトリー以下の適当な作業ディレクトリーに入れておきます。

- ダウンロード
  - OpenRTM ソースコード
    - [OpenRTM-0.4.2.tar.gz](http://www.openrtm.org/pub/OpenRTM-aist/cxx/0.4.2/OpenRTM-aist-0.4.2-RELEASE.tar.gz)
    - [OpenRTM-1.0.0.tar.gz](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.0.0/OpenRTM-aist-1.0.0-RC1.tar.gz)
  - [config100.sh](http://www.openrtm.org/pub/OpenRTM-aist/armadillo/buildtools/config100.sh) ・ [config042.sh](http://www.openrtm.org/pub/OpenRTM-aist/armadillo/buildtools/config042.sh)
    - 展開した OpenRTM-0.4.2.tar.gz、又は OpenRTM-1.0.0.tar.gz の中で実行し、クロスコンパイルに必要なオプションを指定して configure を行うことができます。
    - OpenRTM-0.4.2 対応、OpenRTM-1.0.0 対応に分けました。2010/01/21
  - [arm-cross-install.sh](http://www.openrtm.org/pub/OpenRTM-aist/armadillo/buildtools/arm-cross-install.sh)
    - OpenRTM-1.0.0対応になりました。2009/12/28 
    - OpenRTMのARM クロスコンパイル環境を Debianホストに構築します。

- arm-cross-install.shはapt-get コマンドで debパッケージをダウンロードします。
deb パッケージを置いている URL を sources.list に加えます。su コマンドで root (パスワード：root)になり、**/etc/apt/sources.list**に下の URL を加えてください。
```
 deb http://downloads.pylone.jp/cross-toolchain/deb ./
 deb http://www.openrtm.org/pub/Linux/debian/ etch main
```
- root のまま、apt-get コマンドでパッケージをインストールします。
```
 # apt-get update
 # apt-get install python-yaml  (yesまたはYを入力してインストールを完了してください。)
```
python-yaml パッケージは OpenRTM のインストール後、rtc-template で必要です。
- arm-cross-install.sh で OpenRTM-aist の ARM クロスコンパイル環境を構築します。多数のデータがダウンロードされるので適当な作業ディレクトリーを作成しその中で arm-cross-install.sh を実行してください。
```
 # sh arm-cross-install.sh  (yesまたはYを入力してインストールを完了してください。)
```
- arm-cross-install.shを実行することでOpenRTM-aistをクロスコンパイルするために必要なパッケージ群がダウンロード・インストールされますが、その副作用としてgdmなどの一部のパッケージが削除されてしまいます。
gdmが削除されるとグラフィカルなデスクトップ画面が出なくなってしまいますので、戻したい場合は以下のようにgdmを再度インストールしなおします。
```
 # apt-get install gdm　　 (yesまたはYを入力してインストールを完了してください。)
 # /etc/init.d/gdm start
```
- 以上でATDE2環境の整備は完了です。

## OpenRTM-aist のクロスコンパイル
### OpenRTM-aist のビルド
OpenRTM-aist-0.4.2 のソースコードをホームディレクトリーなどの適当なディレクトリーに展開してください。展開後、作成されたディレクトリーに移動します。
```
 # tar zxvf OpenRTM-aist-0.4.2.tar.gz
 # cd OpenRTM-aist-0.4.2
```
通常、ここで configure を実行しますが、OpenRTM をクロスコンパイルするには configure に適切なオプションを指定する必要があります。
上記でダウンロードした config.sh を使用すると、クロスコンパイルに必要なオプションを指定して configure を実行することができますので、ここでは config.sh を使用します。
config.sh をカレントディレクトリーにコピーし、インストール先ディレクトリーを引数に指定して実行します。
```
 # cp ../config.sh ./
 # sh config.sh /usr/arm-linux-gnu
```
config.sh が正常に終了したことを確認してください。
ビルドが正常に終了したら make します。
```
 # make
```
インストールするためにはすくなくとも、
```
 OpenRTM-aist-0.4.2/rtm
 OpenRTM-aist-0.4.2/rtm/idl
 OpenRTM-aist-0.4.2/utils/rtm-config
 OpenRTM-aist-0.4.2/utils/rtm-naming
 OpenRTM-aist-0.4.2/utils/rtc-template
```
以下のディレクトリーが正常にビルドされている必要があります。ビルドが正常に終了したら、ヘッダファイル、ライブラリ、ユーティリティーコマンド群をインストールします。

### OpenRTM-aist のインストール
config.sh で指定した /usr/arm-linux-gnu/ にインストールされます。
```
 # make install
```
/usr/arm-linux-gnu/share/examples/ にサンプル実行ファイルが生成されてます。
## RTコンポーネントのクロス開発 
以上で、RTコンポーネントをクロス開発する環境が整いました。
ここでは例として、サンプルに含まれる SeqOutComp のソースを使用してクロスコンパイルしてみます。

### RTコンポーネントのクロス開発する 
- RTコンポーネントをクロス開発するには、クロス開発用のコマンドを使用する必要があるので、以下のように（/usr/arm-linux-gnu/bin）パスを通します。
パスを通す際に、/usr/arm-linux-gnu/binがPATH の先頭になるよう注意してください。
```
> export PATH=/usr/arm-linux-gnu/bin:$PATH
```

### rtc-template で SimpleIO の RTコンポーネントを生成する。 
サンプルを作成するため適当なディレクトリーを作成し、そこに OpenRTM のサンプル SeqOut のソースに含まれる以下のファイルをコピーしてください。
```
 SeqOutComp.cpp		SeqOut.h	SeqOut.cpp	Makefile.SeqOut
```

```
 > mkdir test
 > cp (インストールディレクトリー)/OpenRTM-aist-0.4.2/examples/SeqIO/SeqOutComp.cpp　./test/
 (上記のコマンドですべてコピーしてください)
```

OutPort を八つ持つ SeqOutComp というコンポーネントを生成します。

### RTコンポーネントのビルド 
生成された、Makefile.SeqOut の内容を確認してください。CXX=で始まる行がない場合、コンパイラにクロス用のコンパイラを以下のように指定する必要があります。

```
　環境変数を設定し make する<br>
 > CXX=arm-linux-gnu-g++ make -f Makefile.SeqOut
```
　又は、
```
 > export CXX=arm-linux-gnu-g++
 > make -f Makefile.SeqOut
```

make が正常に完了すると、SeqOutComp の実行ファイルが生成されます。

## RTコンポーネントの実行 
クロス開発した実行ファイル、ライブラリ、などを USBメモリーにコピーし、Armadillo240 上で起動します。
### USBメモリーの準備 
Armadillo240 上で RTコンポーネントを実行するのに必要なファイルを USBメモリーにコピー、生成します。

- **実行ファイル** 
  - Armadillo240 上で実行したい RTコンポーネントの実行ファイル。
この例では、先ほどクロスコンパイルした SeqOutComp を使用します。
SeqOutComp をUSBメモリーの適当な場所（ルートディレクトリー等）にコピーします。

- **ライブラリ**
  - ATDE2の/usr/arm-linux-gnu/lib以下にはARM用のライブラリが格納されています。
このディレクトリー内のライブラリのうち、以下のものを USBメモリーにコピーします。
　USBメモリーにライブラリを置くディレクトリーlibを作成します。

```
 >mkdir lib
 又は、
 GUI の場合、右クリックでフォルダーを作成します
```

/usr/arm-linux-gnu/lib のライブラリをコピーする際に、以下の通りに名前を変更してください。

- OpenRTM-aist-0.4.2 の場合
  - ライブラリ名変更
    - コピーする際に、以下の通りに名前を変更してください。

<table class="table-alt">
  <tr>
    <th>ライブラリ名</th>
    <th>ライブラリ名変更後</th>
  </tr>
  <tr>
    <td>libomniDynamic4.so.0.6</td>
    <td>libomniDynamic4.so.0</td>
  </tr>
  <tr>
    <td>libomniORB4.so.0.6</td>
    <td>libomniORB4.so.0</td>
  </tr>
  <tr>
    <td>libomnithread.so.3.1</td>
    <td>libomnithread.so.3</td>
  </tr>
  <tr>
    <td>libRTC-0.4.2.so.0.0.4</td>
    <td>libRTC-0.4.2.so.0</td>
  </tr>
  <tr>
    <td>librt.so.1</td>
    <td>librt.so.1(変更なし)</td>
  </tr>
  <tr>
    <td>libACE.so.5.4.7</td>
    <td>libACE.so.5.4.7(変更なし)</td>
  </tr>
</table>

- OpenRTM-aist-1.0.0 の場合
  - ライブラリ名変更
<table class="table-alt">
  <tr>
    <th>ライブラリ名</th>
    <th>ライブラリ名変更後</th>
  </tr>
  <tr>
    <td>libm-2.3.6.so</td>
    <td>libm.so.6</td>
  </tr>
  <tr>
    <td>libomiDynamic4.so.0.6</td>
    <td>libomniDynamic4.so.0</td>
  </tr>
  <tr>
    <td>libomnithread.so.3.1</td>
    <td>libomnithread.so.3</td>
  </tr>
  <tr>
    <td>librt.so.1</td>
    <td>librt.so.1(変更なし)</td>
  </tr>
  <tr>
    <td>libRTC-1.0.0.so.0.0.4</td>
    <td>libRTC-1.0.0.so.0</td>
  </tr>
  <tr>
    <td>libstdc++.so.6.0.8</td>
    <td>libstdc++.so.6</td>
  </tr>
  <tr>
    <td>libuuid.so.1.2</td>
    <td>libuuid.so.1</td>
  </tr>
</table>

- **rtc.conf**
  - 以下のようなrtc.confをテキストエディタなど使用して作成してください。
Armadillo上ではネームサーバを起動しませんので、別のPC上でネームサーバを起動しておいてください。
rtc.confのcorba.nameservers のオプションにはそのネームサーバを起動したPCのアドレスを指定します。

```
 corba.nameservers: 192.168.100.1　(自分のネームサーバーのIPアドレスを入力)
 naming.formats: %n.rtc
```

- ※ ATDE2でのUSBメモリのマウント
  - VMware(ATDE2)を起動中にPCにUSBフラッシュメモリを差し込むと、自動でマウントされDesktop上で確認できます。
  - 自動でマウントされないときはVMware(ATDE2)の端末でsuコマンドでrootになりmountをし直します。

- USBメモリのマウント

```
 > su
 # mkdir /mnt/(適当なディレクトリー)
 # mount -t vfat /dev/sdb1 /mnt/(上で作成したディレクトリー)
```

- USBメモリーのアンマウント<br>
　　Desktop上に USBメモリーのアイコンが表示されてるときは、右クリック ＞ アンマウントしてください。<br>
　　または、コンソールからコマンドでアンマウントできます。<br>
```
 # umount /mnt/(上で作成したディレクトリー)
```


### USBメモリーのディレクトリー構造
USBメモリーの準備を終えると、USBメモリーは下のようなディレクトリー構造になります。

- OpenRTM-aist-0.4.2

```
 　USBメモリー -+- lib --+- libomniDynamic4.so.0
```
<table class="table-alt">
  <tr>
    <th>+- libomniORB4.so.0</th>
  </tr>
  <tr>
    <td>+- libomnithread.so.3</td>
  </tr>
  <tr>
    <td>+- libRTC-0.4.2.so.0</td>
  </tr>
  <tr>
    <td>+- librt.so.1</td>
  </tr>
  <tr>
    <td>+- libACE.so.5.4.7</td>
  </tr>
  <tr>
    <td></td>
  </tr>
</table>
 　　　　　　      　 +- SeqOutComp 
<table class="table-alt">
  <tr>
    <th></th>
  </tr>
</table>
 　　　　　      　　 +- rtc.conf


- OpenRTM-aist-1.0.0

```
 　USBメモリー -+- lib --+- libm.so.6
```
<table class="table-alt">
  <tr>
    <th>+- libomniDynamic4.so.0</th>
  </tr>
  <tr>
    <td>+- ibomnithread.so.3</td>
  </tr>
  <tr>
    <td>+- librt.so.1</td>
  </tr>
  <tr>
    <td>+- libRTC-1.0.0.so.0</td>
  </tr>
  <tr>
    <td>+- libstdc++.so.6</td>
  </tr>
  <tr>
    <td>+- libuuid.so.1</td>
  </tr>
  <tr>
    <td></td>
  </tr>
</table>
 　　　　　　　       +- SeqOutComp 
<table class="table-alt">
  <tr>
    <th></th>
  </tr>
</table>
       　　　　　　　 +- rtc.conf

### Armadillo240 で実行ファイルを起動&aname(start240);

USBメモリーのマウント設定、ライブラリ PATH の設定を変更し、実行ファイルを動かします。
PC  とArmadillo をシリアルケーブルで接続し、Armadillo上 の Linux のシリアルコンソールからログインすることで Armadillo上 の Linux を操作することができます。
以下のやりやすい方法で進めてください。

#### ATDE2上から minicom で操作する

ATDE2上から端末エミュレーターのプログラム**minicom**で操作します。
PCのシリアルポートと Armadillo のシリアルポートをシリアルケーブルで接続してください。
シリアルポートがない PC の場合は USB－シリアル変換ケーブルなどを使用する必要があります。
Armadillo のシリアルケーブルの接続方法に関しては、Armadillo のマニュアルを参照してください。

※VMware の仮想マシンのデバイスの設定を以下のように行ってください。
```
 メニューバー > VM > 設定 > ハードウェアタグ
```
　　（VMwareWorkstation と VMwareConsole で設定できます。）

<div align="center"><a href="VMwareUseSerialSetting.png"><img src="VMwareUseSerialSetting.png" width="100;"></a></div>
<div align="center"><strong>VMware の USBシリアルポート設定</strong></div>

接続のチェックを確認してください。

<div align="center"><a href="VMwareComSeting.png"><img src="VMwareComSeting.png" width="100;"></a></div>
<div align="center"><strong>VMware のシリアルポート設定</strong></div>

デバイスステータスのチェックと、接続 > 物理シリアルポートを使用でポートを確認してください。
ATDE2 の端末から、端末エミュレーターminicom を起動します。
 > minicom
Enterを押すと Armadillo240 の login 画面になります。
以降は<span style="color:Maroon;">共通の操作</span>;に進んでください。

#### Windows から端末エミュレーター (teraterm) で操作する

Windowsから、TeraTerm などの端末エミュレーターを使用して Armadillo のシリアルコンソールと接続することもできます。TeraTerm は[こちら](http://hp.vector.co.jp/authors/VA002416/)から無料でダウンロードできます。
以下の設定で起動してください。

- メニューバー>設定＞シリアルポート設定＞
  - ポート/任意
  - ボーレート/115200
  - データ/8bit
  - パリティ/none
  - ストップ/1bit
  - フロー制御/none

上記の設定で起動すると、Armadillo240 のログイン画面が表示されます。
※表示されないときは Enter を押してください。
以降は共通の操作に進んでください。


#### 共通の操作

USBメモリーを Armadillo に差してください。
Armadillo のログイン画面で、root (パスワード:root) でログインしてください。
デフォルトの mount はオプション(umous=111)で、どのユーザーも実行のできないパーミッション設定です。

一度アンマウントしてから、書き込み・実行可能な -o rw オプションでリマウントします。
```
 # umount /dev/sda1
 # mount -t vfat -o rw /dev/sda1 /home/www-data/storage/
```
ライブラリパスを通すため、コマンドでゲストになり USBメモリーに移動します。
```
 # su guest
```
 > cd /home/www-data/storage
ライブラリのパスを通します。(ライブラリの置いてあるディレクトリーを指定してください。)
 > export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/www-data/storage/
 > ./SeqOutComp　(実行ファイルが実行されました)
RTコンポーネントが起動がします。

※RtcLink からも確認できます。

この方法では Armadillo の起動の度に設定を修正しなくてはなりません。
次の章では、Armadillo の起動後 RTコンポーネントが自動で起動するイメージファイルを作成し、Armadillo にダウンロードします。

## Armadillo240 のイメージファイルを作成する
これまでの方法だと、Armadillo の起動ごとに端末エミュレーターで設定を変更する必要があります。ここでは、AtmarkTechno,Inc から提供されている atmark-dist を使い、Armadillo240 の起動後 RTコンポーネントが自動で起動するイメージファイルを作成し、Armadillo にダウンロードします。

### 開発環境の整備
　RTコンポーネントをクロスコンパイルした ATDE2 の環境をそのまま使います。ATDE2上に以下の項目をダウンロードしてください。

:**Atmark-dist**| Armadillo の userland のイメージファイルを作成します。
  - [こちら](http://armadillo.atmark-techno.com/downloads)から無料で入手できます。

:**Linuxカーネル**| Atmark-dist でイメージファイルを作成する際必要です。
  - [こちら](http://armadillo.atmark-techno.com/armadillo-240/downloads)から無料で入手できます。(Armadillo240の場合)
  - [openrtm_new.patch](http://www.openrtm.org/pub/OpenRTM-aist/armadillo/buildtools/openrtm_new.patch), Atmark-dist(2009/03/18)のverアップに伴い patch ファイルを修正しました。(2010/02/12)

### atmark-distのビルドと設定
ここでは、Armadillo の userland のイメージファイルを作成します。
ここで作成するイメージファイルを使用すると、USBメモリーにあらかじめインストールされた RTコンポーネントを、自動的に起動できるようになります。

#### RTコンポーネントの起動の仕組み 
USBメモリーを /home/openrtm/にマウントし、Armadillo の 起動後/home/openrtm/boot.sh を起動させます。
boot.shは、USBメモリー内のライブラリパスを通し、実行ファイルを起動します。
- OSの設定
  - USBメモリーを書込、実行可能で /home/openrtm/ にマウントする。
  - USBメモリーマウント時に、USBメモリー直下の boot.sh を起動する。
- USBメモリーの内容<br>
USBメモリーに以下のファイルを用意してください。

:**boot.sh** | Armadillo240 起動後、起動するシェルスクリプトです。USBメモリーの直下に下のような boot.sh を用意してください。ライブラリ PATH を通し、実行ファイルを起動します。
  - ※rtc.confをUSBメモリー直下に、ライブラリを libディレクトリーに置いた時の設定です。USBメモリーのディレクトリー構造に応じて修正してください。

```
 #!bin/sh
 . /etc/default/openrtm.conf
 export LD_LIBRARY_PATH=$LIBPATH:/home/openrtm/lib/
 /home/openrtm/SeqOutComp(実行ファイル名) 　-f　 /home/openrtm/rtc.conf
```

#### atmark-distビルド 
ATDE2上で、atmark-dist と linuxカーネル、openrtm.patch をダウンロードし展開してください。
 > tar zxvf atmark-dist--20090318.tar.gz
 > tar zxvf linux-2.6.12.3-a9-15.tar.gz
展開された atmark-dist のディレクトリーに移動し、linuxカーネルのシンボリックリンクを張ります。
　　※リンク名は、linux の ver にかかわらず **./linux-2.6.x** にしてください。
 > ln -s ../linux-2.6.12.3-a9-15　./linux-2.6.x　
make configします。 以降の質問には下のように入力してください。
 > make config
```
 Select the Vendor you wish to target　　：Atmarktechno(入力)
 Select the Product you wish to target　 ：Armadillo-240.Recover(入力)
 Kernel is linux-2.6.x　　　　　　 　　　  ：default(enterでもOK)
 defined CONFIG_DEFAULTS_CROSSDEV_DEFAULT：none(enterでもOK)
 Default all settings 　　　　　　　 　　　：y(入力)
 Customize Kernel Settings 　　　　 　　　 ：n(enterでもOK)
 Customize Vendor/User Settings  　　　　 ：n(enterでもOK)
 Update Default Vendor Settings  　　　　 ：n(enterでもOK、終了)
```

openrtm.patchをコピーし以下の手順でパッチを当ててください。
 > cp openrtm.patch /atmark-dist-YYYYMMDD/vendor/AtmarkTechno/Armadillo-240.Recover/openrtm.patch
 > cd /atmark-dist-YYYYMMDD/vendor/AtmarkTechno/Armadillo-240.Recover/
 > patch -p1 <openrtm_new.patch
```
 　(パッチ終了)
```
atmark-dist-YYYYMMDDディレクトリーまで移動し、 make dep all　してください。
 > cd ../../../
 > make dep all
make dep all中、以下のようなエラーメッセージが表示されますが、romfs は正常に生成されます。
```
 /bin/sh: extensions/.dccp-test: 許可がありません
 /bin/sh: extensions/.layer7-test: 許可がありません
 /bin/sh: extensions/.statistic-test: 許可がありません
 make[2]: ディレクトリー `/home/atmark/Desktop/foratde/forkernel/atmark-dist-200807 17/user/iptables' に入ります
 romfs-inst.sh /bin/iptables
 romfs-inst.sh -l /bin/iptables /bin/iptables-save
 ln: `/bin/iptables' にアクセス中: そのようなファイルやディレクトリーはありません
 romfs-inst.sh -l /bin/iptables /bin/iptables-restore
 ln: `/bin/iptables' にアクセス中: そのようなファイルやディレクトリーはありません
```
make終了後、images ディレクトリーに4つのファイルが生成されます。
 > ls images
```
 　linux.bin　linux.bin.gz　romfs.img　romfs.img.gz
```
次の章で **romfs.img.gz** を Armadillo に書き込みます。

### イメージファイルを Armadillo240 にダウンロードする 
生成した userland のイメージファイル**romfs.img.gz**を Armadillo240 にダウンロードします。
Armadillo はジャンパピン(2)を**ショートして**、電源を入れておいてください（Armadillo[ハードウェアマニュアル](http://download.atmark-techno.com/armadillo-240/doc/armadillo-200_series_hardware_manual_ja-2.0.7d.pdf)のp.16を参考にしてください)

VMware(ATDE2)、Windows どちらからでもダウンロードできます。

#### ATDE2上からダウンロードする
[[こちら >#start240]]で VMware の仮想マシンのデバイス設定を行ってから進めてください。

- Armadillo-240 と PC を USBシリアルケーブル（又はシリアルケーブル）でつなぎます。
- ATDE2 の端末コンソールから hermitでimages/**romfs.img.gz**をダウンロードします。
 > hermit download -i images/romfs.img.gz -r userland --port /dev/ttyUSB0　(または、/dev/ttyS0)　
　ダウンロードには8分ほどかかります。<br>
- **completed** と表示されたら完了です。
```
 serial: completed 0x004455fd (4478461) bytes.　(完了)
```
<br>
　
　
### Windows上からダウンロードする
Armadillo240 に同梱されている CD-ROM の downloader > win32 > Hermit.zip を Widows上に置いてください。

- Windows上にHermit.zip を解凍し、Hermit.exe をダブルクリックで起動します。

<div align="center"><a href="hermit.png"><img src="hermit.png" width="100;"></a></div>
<div align="center"><strong>Windows上のHermit</strong></div>

- Armadillo240 をPCをシリアルポートで接続してください。
- ATDE2 に生成された romfs.img.gz を Windows上に移動してください。
- 表示されたダイアログでシリアルポートを設定し、Download を押します。images で作成した **romfs.img.gz** を、Region で **userland** を設定し実行ボタンを押してダウンロードします。(8分くらいかかります。)
- ダウンロードが完了すると、Hermit に表示されます。

## RTコンポーネントの実行・確認 
RTCLink を起動し、RTコンポーネントの起動を確認します。

- イメージファイルのダウンロード完了後、Armadillo のジャンパピン(2)の**ショートを外し**、電源のプラグを差し直し再起動します。
- RTコンポーネントを実行する際、rtc.conf で指定したネームサーバーを起動します。
  - Windowsの場合
    - プログラムメニューの「OpenRTM-aist」→「example」→「NameService.bat」を実行します。
    - あるいは、OpenRTM-aist\binにある rtm-naming.bat をダブルクリックして起動します。
  - linuxの場合
    - suコマンドで root になり、ネームサーバーを起動します。
 > su
```
 # /etc/init.d/omniorb4-nameserver start
```
- RTCLink を起動し、ネームサーバーにコンポーネントが生成されているのを確認してください。
  - ※ネームサーバーが表示されていない時は、Connect Name Server ボタンを押してネームサーバーを追加接続してください。

## 応用例 
### Armadillo + URG センサ ー

Armadillo と北陽電機URGセンサーと組み合わせ、分散センサーシステムを簡単に構築するためのユニットです。
Armadillo 上では URG センサー RTコンポーネントが動作します。（Armadillo 電源投入と同時に RTC が自動起動します。）
PoE (Power over Ether) 対応の Armadillo を使用することで、LANケーブルのみで通信・給電が可能です。
URG センサーも PoE からの電源供給で動作します。
ケーブル1本のみでセンサー配置が可能ですので、分散センサーシステムを容易に構築できます。

<div align="center"><a href="Armadillo_URG.png"><img src="Armadillo_URG.png" width="100;"></a></div>
<div align="center"><strong>分散 LRF ユニット</strong></div>

<div align="center"><a href="Armadillo_URG3.png"><img src="Armadillo_URG3.png" width="100;"></a></div>
<div align="center"><strong>PoE (Power over Ether) HUB により電力供給が可能</strong></div>

