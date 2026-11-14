---
layout: page
title: "tklrfviewer"
---

<!-- Title: tkLRFViewer -->

#contents

このサンプルは、Python版にのみ付属しています。 

### 概要
tkLRFViewerは、Laser Range Finderセンサーからの出力を表示するRTCの例です。レーザレンジファインダーから入力を扱うRTCを接続して使います。接続するRTCは各自接続するデバイスに合わせて入力してください。例えば、[北陽電機株式会社 URGシリーズ]({{ site.baseurl }}/node/4974)（Projectページはリンク切れです）を参照してみてください。また、LRFセンサーはLaser距離計を回転させながら空間をスキャンし、測定した距離データを逐次送り出すようなセンサーです。データとして、回転角の初期値、終わり値、各距離データの測定を行う角度間隔、そして測定した距離データの列というような形でデータが出力されます。本コンポーネントは、そのスキャンしたデータがどのようになるかを見るためのコンポーネントです。

<!-- 英語ページはnote/5085 -->
### 起動画面
このコンポーネントを起動すると以下のGUI画面が表示されます。

<div align="center"><a href="tkLRFViewGUI.png"><img src="tkLRFViewGUI.png" width="100%;"></a></div>
<div align="center"><strong>tkLRFViewer GUI画面</strong></div>

### 使い方
このRTCを使うには、上記で述べたように、外部につなぐLaser Range Finderセンサーからセンサー出力を読みこみ、それを変換して[RangeData型](https://github.com/Nobu19800/DataTypeManual/blob/master/docs/RobotInterface.md#rangedata)の出力としてOutPortより出力するRTCが必要です。上記のLaser Range Finderに関するリンクを参考にRTCを準備してください。

- このtkLRFViewerコンポーネントは、Windows環境ではエクスプローラで"Program Files\OpenRTM-aist\1.2.x\Components\Python" ディレクトリでtkLRFViewer.batをダブルクリックすることで起動できあす。センサー用のRTCを起動して、RTSystemEditorなどで本コンポーネントに接続して使用してください。
- tkLRFViewerのGUIには4つのスライダーがあり、それぞれ「Scale Factor]、[Threshold]、[Filter(Time)]、[Filter(Spacial)]のパラメータを決めます。また[Axis]、[Grid]、[Line]、「Fill]、「Threshold]、「Filter(Time)]、[Fileter(Spacial)] のチェックボックス、「Reset  Scale]ボタンがあります。それぞれの機能を下記表に示します。

<table class="table-alt">
  <tr>
    <th>名前</th>
    <th>機能</th>
  </tr>
  <tr>
    <td>Scale Factor</td>
    <td>描画をするにあたって、その距離のベースを480m x 480mの空間のを基本として、スケール値による描画の拡大縮小を行う、一般的な数m X 数ｍぐらいの範囲の検出には0.01とかの値になるように設定した方が良い※</td>
  </tr>
  <tr>
    <td>Reset Scale ボタン</td>
    <td>Scale Factor 1.0にリセットするボタン</td>
  </tr>
  <tr>
    <td>Axisチェックボックス</td>
    <td>このチェックボックスにチェックされているとX軸とY軸の軸が表示される</td>
  </tr>
  <tr>
    <td>Gridチェックボックス</td>
    <td>このチェックボックスがチェックされていると目盛線が表示される</td>
  </tr>
  <tr>
    <td>Lineチェックボックス</td>
    <td>このチェックボックスがチェックされていると測距データを曲線で描画</td>
  </tr>
  <tr>
    <td>Fillチェックボックス</td>
    <td>このチェックボックスがチェックされていると測距データを塗りつぶされた図形として描画</td>
  </tr>
  <tr>
    <td>Thresholdチェックボックスとスライダー</td>
    <td>チェックされているとパラメータが有効になり、下限値※の処理が行われる、その値より入力距離が小さい場合は、無効と見なし検出距離が1000ｍと見なす</td>
  </tr>
  <tr>
    <td>Fileter(Time}チェックボックスとスライダー</td>
    <td>チェックされている時間軸方向の変化に対するフィルターが融合になり、スライダーで効果度合いを調整</td>
  </tr>
  <tr>
    <td>Fileter(Spacial)チェックボックスとスライダー</td>
    <td>チェックされていると回転方向のスキャンデータの変化に対してのフィルタが有効になり。スライダーで効果度合いを調整</td>
  </tr>
</table>
※ 現状の表示スケールや、Thresholdの働き方は、あまり現実的に有効な設定となっていません。実際の使用においては、ユーザー環境にあわせてソースコードを書き換え調整することを推奨します。

# GUI出力例
GUIには以下の画面のような出力がでます。
<div align="center"><a href="tkLRFViewGUIinUse.png"><img src="tkLRFViewGUIinUse.png" width="100%;"></a></div>
<div align="center"><strong>使用中のGUI画面</strong></div>



