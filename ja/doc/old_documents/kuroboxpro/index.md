---
layout: page
title: 玄箱proへのインストール
---

<!-- Title: 玄箱PROへのインストール -->
#contents
<div align="center"><a href="kuro-box_pro.jpg"><img src="kuro-box_pro.jpg" width="30%;"></a></div>

## 玄箱/PROスペック 
<table class="table-alt">
  <tr>
    <td>CPU</td>
    <td>Marvell88F5182 (ARM9Core/400MHz)</td>
  </tr>
  <tr>
    <td>RAM</td>
    <td>128MB(DDR2)</td>
  </tr>
  <tr>
    <td>Flashメモリ</td>
    <td>256MB(NAND)/Linux2.6.12.6</td>
  </tr>
  <tr>
    <td>LAN</td>
    <td>1000BASE-T/100BASE-TX/10BASE-T×1ポート</td>
  </tr>
  <tr>
    <td>外部IO</td>
    <td>USB2.0×2ポート, S-ATA×2, PCIex1×1, UART×1, GPIO×2, I2C×1, JTAG(ARM20pin)</td>
  </tr>
  <tr>
    <td>HDD</td>
    <td>3.5インチS-ATA 1個を別途用意．</td>
  </tr>
</table>

## インストールの流れ 
玄箱PROのDebian化については、幾つか例があるのですが、sushi-k日誌2さんのところが最も楽にDebian化できるようでした。
- [sushi-k日誌2さん](http://w3.quake3.jp/sushi-k/wp/?p=93)のところの手順に従ってDebian化する。
- 必要なパッケージをapt-getでインストール(もしくはインストールスクリプトを使用)
- OpenRTM-aistのビルド
- インストール

## OS入れ替え 
sushi-kさんのところの手順そのまま。
使用するハードディスクは未フォーマットの物である必要があります。

### tarの入れ替え
BusyBoxのtarは使えないらしいので、tarを入れ替えます。
```
 # wget http://w3.quake3.jp/sushi-k/pool/kuropro/debian/gnutar_kuropro.gz
 Windowsからsamba経由で玄箱に転送しても構いません
 # gzip -dc gnutar_kuropro.gz >/bin/tar
 # chmod a+x /bin/tar [Enter]
```

### Debian化キットのインストール 
Debian化キットをダウンロードしてルートに展開します。
```
 # wget http://w3.quake3.jp/sushi-k/pool/kuropro/debian/debian_kit.tar.gz [Enter]
 # tar xvzpf debian_kit.tar.gz -C / [Enter]
```

### Debianイメージの転送
玄箱PROは共有ディレクトリのmtd device (/mnt/mtd) に
- uImage.buffalo
- hddrootfs.tar.gz
- ChangeMeDevHDD
- ChangeMyUbootEnv

を入れて、背面のリセットスイッチを長押しすると、HDDブート用のシステム構築を自動で開始します。(マニュアルに記述あり)
そこで、Debianのディスクイメージを[ここ](http://w3.quake3.jp/sushi-k/pool/kuropro/debian/)からダウンロードし、これらのファイルをmtd deviceに置きます。
Windowsからsamba経由でもいいですし、wgetで取得してもOK。

### HDDブート環境構築 
背面のリセットスイッチを5秒くらい長押しします。
　すると、前面のオレンジのinfoランプが点滅してHDDのパーティショニング、フォーマット、イメージの展開などが行われます。
これらの作業中もログインしたままで中の様子を見ることができるので、あえてログアウトする必要はありません。
infoランプの点滅が消えたら作業が終了しているはずです。
再起動すればDebian化された玄箱が起動するはずです。

### 設定 
再起動直後、このシステムは以下の設定になっています。
<table class="table-alt">
  <tr>
    <td>IP アドレス</td>
    <td>192.168.1.81</td>
  </tr>
  <tr>
    <td>rootパスワード</td>
    <td>kuroadmin</td>
  </tr>
</table>
ログインはsshでのみ可能ですので、適当なsshクライアントからログインして設定します。

## OpenRTM-aistのビルド
### パッケージのインストール
パッケージのインストールにはOpenRTM-aist-0.4.0付属のDebian用パッケージインストーラ(pkg_install_debianSarge.sh)がそのまま使えます.
OpenRTM-aist-0.4.0のソース展開後, rootになりbuildディレクトリの下のpkg_install_debianSarge.shを実行するだけです.

```
 > tar xvzf OpenRTM-aist-0.4.0.tar.gz
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

これでパッケージのインストールは完了です.

### OpenRTM-aistのビルド 
　以降は通常のPCと全く同じです.

```
 > cd OpenRTM-aist-0.4.0
 > ./configure
 > make
 > su
 # make install
```

ただし, ビルドにはかなりの時間(1時間45分前後)を要します.

```
 > time make
 5898.850u 251.470s 1:43:47.10 98.7%     0+0k 0+0io 278pf+0w
```

玄箱HGとあまり大差なし。

## リンク
- [玄人志向 KURO-BOX/PRO](http://www.kuroutoshikou.com/modules/display/?iid=966)
- [KURO-BOX/PRO Debian化決定版？](http://w3.quake3.jp/sushi-k/wp/?p=93)
- [山下康成の”ハックしよう”](http://www.yamasita.jp/)


