---
layout: page
title: 開発環境の構築
---

<!-- Title: 開発環境の構築 -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * 開発環境の構築 -->
#contents

EV3 および ev3dev 上で動作するコンポーネントを開発するには、EV3上で開発する方法と、クロス開発環境で開発する方法があります。

ただし、EV3 はメモリが64MB、CPUクロックが300MHz程度と、今どきの開発環境としてはだいぶ遅いマシンですので、EV3上での開発はかなり大変です。

クロス開発というのは、異なるアーキテクチャ、つまり一般的な PCのアーキテクチャである Intel 系の CPU上で、ARM などの異なる種類で動作する実行ファイルを作成することです。

クロス開発では、コンパイル即実行という形はとれませんが、コンパイル時間が圧倒的に速いので、結果として開発効率は高くなります。

## Ubuntu のインストール

開発環境は Linux のディストリビューションの1つである Ubuntu (14.04 LTS) を使用します。

- [Ubuntu 14.04 LTS](https://www.ubuntulinux.jp/News/ubuntu1404-ja-remix)

こちらの URL から ISOイメージをダウンロードして OS をインストールしてください。

PC のそのままインストールして使用することもできますし、バーチャルマシンとしてインストールして使用しても構いません。

バーチャルマシン環境としては、主に以下のようなものがあります。

- VMware Player
  - 2015年8月現在: [https://my.vmware.com/jp/web/vmware/free#desktop_end_user_computing/vmware_player/7_0](https://my.vmware.com/jp/web/vmware/free#desktop_end_user_computing/vmware_player/7_0)
  - もしくは VMware Player で検索してください
- Virtual Box
  - 2015年8月現在: [http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html?ssSourceSiteId=otnjp](http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html?ssSourceSiteId=otnjp)
  - もしくは Virtual Box で検索してください
- Parallels (MAC)
  - 2015年8月現在[http://www.parallels.com/jp/](http://www.parallels.com/jp/)
  - もしくは Parallels で検索してください

これらの詳細な使用方法については、それぞれの Webサイトもしくは、解説の Webページを検索してみてください。

## brickstrap

ここからは、Ubuntu14.04 がインストールされたものとして、話を進めます。
まず、brickstrap というツールをインストールします。brickstrap は上述の ev3dev の OSイメージを作成するためのツールですが、クロス開発を行うためのツールとしても利用可能です。

## brickstrap のインストール

brickstap は下記の github 上で開発が行われています。

- [ev3dev](https://github.com/ev3dev/ev3dev)
  - [brickstrap を用いたクロス開発について](https://github.com/ev3dev/ev3dev/wiki/Using-brickstrap-to-cross-compile-and-debug)

まずは、brickstrap をインストールします。通常の debian リポジトリには存在しないコマンドですので、パッケージリポジトリに ev3dev.org を追加しています。

```
 $ sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 2B210565

<!-- $ sudo apt-add-repository http://ev3dev.org/debian -->

 $ sudo apt-add-repository "deb http://archive.ev3dev.org/ubuntu trusty main"
 $ sudo apt-get update
 $ sudo apt-get install brickstrap
```

### イメージ作成のための準備

まずは supermin appliance を作成するために以下のコマンドを実行します。

```
 $ sudo update-guestfs-appliance
 $ sudo usermod -a -G kvm <username>
 $ sudo chmod +r /boot/vmlinuz*
```

### 開発環境の作成

ここまでできたら、いよいよ開発環境を作成します。特定のディレクトリーに、EV3 に搭載するシステムのファイルシステムを模擬したものを作成します。
場所としては、自分のホームディレクトリー以下の適当な場所が良いでしょう。ここでは、ホームディレクトリー以下の work ディレクトリーに作成します。

```
 $ cd ~
 $ mkdir work
 $ cd work
```

以下のコマンドでファイルシステムの作成～イメージの作成を行います。

```
 $ brickstrap -b ev3-ev3dev-jessie -d ev3-ev3dev-work all
```

このコマンドの実行には10分から20分かかります。
実際に行われていることは、ev3dev の Linux　システムに必要なコマンド群、パッケージなどを仮想的な root ディレクトリー ev3-ev3dev-work 以下にインストールし、それを SDカードに書き込み可能なイメージファイルとして構成する作業です。

終了後には、ev3-ev3dev-work.tar と ev3-ev3dev-work.img というファイルシステムのアーカイブとイメージファイルが作成されているはずです。
この .img ファイルを SDカードに書き込むと EV3 で ev3dev を起動できます。

### proot を入れ替える

ubuntu14.04 x86_64 では、brickstrap 内部で使われている proot のバージョンが古く、一部のユーザーIDやグループIDを扱う関数が実行できないため、apt-get でエラーが発生します。
これを避けるために、バージョン4.0以降の proot を使用します。

- [http://proot.me/#downloads](http://proot.me/#downloads)

ここから、x86_64用バイナリをダウンロードし、当該マシンにコピーします。

```
 $ wget http://portable.proot.me/proot-x86_64
 $ sudo mv /usr/bin/proot /usr/bin/proot_3.0.2
 & sudo mv proot /usr/bin/
 $ chmod 755 /usr/bin/proot
```

### シェルを起動する

以上で、クロス開発環境ができましたので、OpenRTM-aist をコンパイル・インストールして、さらに RTコンポーネントを開発します。
brickstrap を利用すると、あたかも EV3 上でパッケージのインストールやソースコードのコンパイルをしているように振る舞うモードを利用することができます。

以下のコマンドを入力します。

```
user@host:`/work$` brickstrap -b ev3-ev3dev-jessie -d ev3-ev3dev-work shell
```

すると、コマンドプロンプトが **#** となり、上述のモードとなります。

## OpenRTM-aist のコンパイル

OpenRTM を自分でコンパイル・インストールする場合には、以下の手順に従ってください。ビルド済みのパッケージを利用する場合は、次の章へ移動してください。

まず、OpenRTM-aist をコンパイルします。OpenRTM-aist のビルドに必要なパッケージをインストールします。

```
 # apt-get update
 # apt-get install libomniorb4-dev omniidl
 # apt-get install gcc g++ make uuid-dev libboost-filesystem-dev
 # apt-get install doxygen
 # apt-get install build-essential debhelper devscripts
 # apt-get install subversion texlive texlive-lang-cjk xdvik-ja python-yaml
 # apt-get install wget
```

次に、OpenRTM-aist のソースコードをダウンロードします。

```
 # cd /home
 # wget http://tmp.openrtm.org/pub/OpenRTM-aist/cxx/x.y.z/OpenRTM-aist-x.y.z.tar.gz
 # tar xvzf OpenRTM-aist-x.y.z.tar.gz
 # cd OpenRTM-aist
 # ./configure --prefix=/usr
 # cd packages
 # make
```

これで、packages の下に OpenRTM-aist のパッケージが生成されます。
その後は、

```
 # dpkg -i openrtm-aist-*
```

のようにして、パッケージをインストールしてください。
OpenRTM-aist-Python についても同様にソースコードをダウンロードして、コンパイル(正確には、パッケージ作成)します。

```
 # wget http://tmp.openrtm.org/pub/OpenRTM-aist/python/x.y.z/OpenRTM-aist-Python-x.y.z-RELEASE.zip
 # cd OpenRTM-aist-Python
 # cd packages
 # make
```

C++版同様に package ディレクトリー以下に作成されたパッケージが作成されます。
インストールは、

```
 # dpkg -i openrtm-aist-python-*
```

のように行います。


## OpenRTM-aist のインストール

上述のように、OpenRTM-aist を自分でソースからインストールせずに、事前にコンパイル済みのパッケージをインストールしても構いません。
ev3dev に OpenRTM-aist をインストールする方法について述べた、上述の方法とほぼ同様です。

### sources.list の編集

openrtm.org をパッケージリポジトリとして追加するために、/etc/sources.list を編集します。

```
 # vi /etc/apt/sources.list
```

のように、vi で /etc/apt/sources.list を開き、

```
 deb http://ftp.debian.org/debian jessie main contrib non-free
 deb http://ev3dev.org/debian jessie main
 deb http://openrtm.org/pub/Linux/debian jessie main ← この行を追加
```

この例のように、最下行に openrtm.org のリポジトリを追加します。

その後、
```
 # apt-get update
```
として、パッケージリポジトリのデーターベースを更新します。
EV3 は遅いので、パッケージデータベースの更新もかなり時間がかかります。

### OpenRTM-aist パッケージのインストール

以上で、openrtm.org のパッケージリポジトリにアクセスできるようになりましたので、以下のようにしてパッケージをインストールします。

```
 # apt-get install openrtm-aist openrtm-aist-dev openrtm-aist-example
 # apt-get install openrtm-aist-python openrtm-aist-python-example
```


