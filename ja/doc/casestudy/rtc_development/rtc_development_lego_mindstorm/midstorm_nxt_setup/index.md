---
layout: page
title: mindstorm nxt 設定
---

<!-- Title: Mindstorm NXT 設定 -->
#contents

NXT を RTC化するにあたり、まずは NXT と PC の設定を行います。
PC と NXT は USB または Bluetooth で接続することができるますが、せっかく電池で動く NXT を紐付きでは使いたくないのでBluetoothで接続します。


## ブロックの組み立て
ここでは、写真に示すような構成を例にとり、NXT を RTC化します。

<!-- div align="center"><a href="TribotBase.png"><img src="TribotBase.png" width="100;"></a></div-->

TribotBase.png

これは、Tribot と呼ばれる構成の移動ベースの部分に、目玉のような超音波センサーを前面に取り付けただけの簡単な構成です。
移動ベースの組み立て方法は、Mindstorm NXT の箱に入っている「Start Here」と書かれた小箱の中の小冊子に詳しく記載されているので参照してください。
この小冊子で解説されている移動ベースに、いくつかの LEGOブロックを追加して、超音波センサーを取り付ければ完成です。


## Bluetoothデバイスのインストール
NXT のインテリジェントブロックには最初から Bluetooth が内蔵されています。
一方、PC に Bluetoothデバイスが内臓されていない場合は、写真のような Bluetoothデバイスを PC に取り付けることで、NXT と通信することができるようになります。

まずは、これらのデバイスを取り付けて、必要ならデバイスドライバをインストールするなどして使えるようにします。
Windows-XP などではたいていの市販の Bluetooth デバイスなら、ドライバを改めてインストールすることなくデフォルトのドライバで動作するようです。

<!-- div align="center"><a href="BluetoothDevices.png"><img src="BluetoothDevices.png" width="100;"></a></div-->
BluetoothDevices.png

Bluetooth が適切にインストールされていれば、コントロールパネルに Bluetooth のアイコンが現れます。
これをクリックすると図のような Bluetooth設定ダイアログが現れます。

<!-- div align="center"><a href="BthDialogOption.png"><img src="BthDialogOption.png" width="100;"></a></div -->
BluetoothDevices.png

「オプション」を開き、
- 「発見機能を有効にする」
- 「Bluetooth アイコンを通知領域に表示する」
をチェックします。

次は、NXT と PC を接続するので、このダイアログはとりあえずそのままにしておきます。


## PC と NXT の接続
PC と NXT を Bluetoothで接続する手順はおおよそ以下のとおりです。

1. NXT の電源を入れる
1. NXT を Bluetooth 検索モードにし検索する
1. 自分の PC を選択
1. チャネル選択
1. PC の Bluetooth 設定ダイアログから接続ウィザードを起動
1. パスキーを設定する
1. PC と NXT 両者で接続ボタンを押す
1. 接続後 NXT を再起動する


### NXT の起動
NXT のインテリジェントブロックの中央のオレンジ色のボタンを押して電源を入れます。
電源が入ると「ピロリロリ♪」と音が鳴ってブロックが起動します。(音量の設定を0にしている場合には音は出ない。)
電源を入れると、図のような画面「My files」モードになります。

<!-- div align="center"><a href="NXTBoot.png"><img src="NXTBoot.png" width="100;"></a></div-->
NXTBoot.png

このような画面にならない場合は、オレンジ色のボタンのしたの四角いボタンを何度か押すことで、「My files」モードにすることができます。

### Bluetooth デバイスの検索
「My files」モードの状態で、オレンジ色ボタンの左右にある、灰色の三角ボタンを押し「Bluetooth」モードにカーソルを合わせ、オレンジボタンを押します。

<!-- div align="center"><a href="NXTBluetooth.png"><img src="NXTBluetooth.png" width="100;"></a></div-->
NXTBluetooth.png

さらに、左右の三角ボタンを押し、「Search」モードにカーソルを合わせます。

<!-- div align="center"><a href="NXTBthSearch.png"><img src="NXTBthSearch.png" width="100;"></a></div-->
NXTBthSearch.png

この状態で、オレンジ色のボタンを押し、実際に接続先を検索します。
検索状態の画面を下に示します。
<!-- div align="center"><a href="NXTBthSearching.png"><img src="NXTBthSearching.png" width="100;"></a></div-->
NXTBthSearching.png


### デバイスの接続
PC の Bluetooth が有効で NXT から PC が見えれば、図のように PC の名前が表れるはずです。
ここで PC の名前とは Windows における「コンピューター名」です。

<!-- div align="center"><a href="NXTBthPCfound.png"><img src="NXTBthPCfound.png" width="100;"></a></div-->
NXTBthPCfound.png

近くに Bluetooth搭載 PC があれば、何台かの PC が見えるかもしれません。
三角ボタンを押して自分の PC にカーソルを合わせ、オレンジ色の確認ボタンを押します。

次に Bluetooth のチャネル選択画面になるので、そのままオレンジ色の確認ボタンを押します。
Connecting と表示された後、パスキー入力画面になるので、そのままオレンジボタンを押します。
<!--div align="center"><a href="NXTBthPasskey.png"><img src="NXTBthPasskey.png" width="100;"></a></div-->
NXTBthPasskey.png

PC側で図のようなバルーンが表示されるのでこのバルーンをクリックします。

<!-- div align="center"><a href="PCballoon.png"><img src="PCballoon.png" width="100;"></a></div-->
PCballoon.png

パスキーの入力を求められるので、先ほど NXT に表示されていたパスキーを入力します。
接続が完了すると、図のようなダイアログが現れます。
他のデバイスを認識しないように「発見機能を無効にする」をチェックし「完了」を押して終了します。

<!-- div align="center"><a href="PCConnectComp.png"><img src="PCConnectComp.png" width="100;"></a></div-->
PCConnectComp.png

### 接続の確認
Bluetooth設定ダイアログの「デバイス」タブで見ると、図のように NXT が接続されていることが確認できます。

<!-- div align="center"><a href="PCDevlistNXT.png"><img src="PCDevlistNXT.png" width="100;"></a></div-->
PCDevlistNXT.png



