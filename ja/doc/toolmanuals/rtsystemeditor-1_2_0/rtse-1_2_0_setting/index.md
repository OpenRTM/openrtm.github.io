---
layout: page
title: 設定画面
---
<!-- Title: 設定画面 -->
#contents

<!-- **設定画面 -->
## RT System Editor
ここでは、 RT System Editor の設定画面について説明します。
RT System Editor の設定画面は、メニューの [window] > [preferences] > [RT System Editor] で表示することができます。

&aname(cycle);
### 接続
接続設定では、状態通知オブザーバーのハートビートの設定、および接続周期の設定を行います。<br>
状態通知オブザーバー対応のミドルウェア（OpenRTM-aist 1.1以降）では、オブザーバーへのハートビート送信により RTC の生存確認を行います。ハートビートの設定項目は以下のとおりです。

<div align="center"><strong>ハートビートの設定項目</strong></div>
<table class="table-alt">
  <tr>
    <th>名前</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>ハートビート有効化</td>
    <td>ハートビートによるタイムアウト検出を有効にするかを指定します。</td>
  </tr>
  <tr>
    <td>ハートビート受信間隔</td>
    <td>ハートビートの受信間隔を指定します。<br>単位は秒、デフォルトは1.0秒。</td>
  </tr>
  <tr>
    <td>ハートビート受信回数</td>
    <td>タイムアウト検出のためのハートビートの受信回数を指定します。<br>受信間隔ｘ受信回数＝タイムアウト時間 [秒]<br>デフォルトは３回。</td>
  </tr>
</table>

接続周期は、従来のミドルウェア（OpenRTM-aist 1.0以前）において、システムエディタがシステム情報を収集し、表示へ反映する周期です。<br>
単位はミリ秒、0 を指定した場合には同期は行われません。
<br>

<div align="center"><a href="fig87ConnectionCycleSetScreen.png"><img src="fig87ConnectionCycleSetScreen.png" width="60%;"></a></div>
<div align="center"><strong>接続周期設定画面</strong></div>
<br>


&aname(color);
### 表示色
表示色の設定画面では、システムエディタにて表示される RTC と ExecutionContext 状態の色を設定することができます。
それぞれの状態の意味については、[システムエディタのRTCの表示]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_display#RTCcolor)をご覧ください。
<br>

<div align="center"><a href="fig88DisplayColorSettingScreen.png"><img src="fig88DisplayColorSettingScreen.png" width="60%;"></a></div>
<div align="center"><strong>表示色設定画面</strong></div>
<br>


&aname(icon);
### アイコン
アイコンの設定画面では、システムエディタで表示する RTC に付与されるアイコン画像と、表示対象のパターンを設定することができます。
表示対象は RTC の種別、もしくはカテゴリのパターンを設定します。
アイコン画像の表示イメージは、[システムエディタのRTCの表示]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_display#RTCcolor)をご覧ください。
<br>

<div align="center"><a href="fig89IconSettingScreen.png"><img src="fig89IconSettingScreen.png" width="60%;"></a></div>
<div align="center"><strong>アイコン画像設定画面</strong></div>
<br>

[Add]、[Edit]、[Delete] ボタンでアイコン画像のエントリを追加、編集、削除します。
[Add]、[Edit] ボタンをクリックするとアイコン画像設定ダイアログが開き、表示対象のパターンとアイコン画像ファイルを設定します。
<br>

<div align="center"><a href="fig90IconSettingDialog.png"><img src="fig90IconSettingDialog.png" width="60%;"></a></div>
<div align="center"><strong>アイコン画像設定画面</strong></div>
<br>

表示パターンを設定後、[Apply]、もしくは [OK] ボタンをクリックすると設定が反映されます。<br>
[Import]、[Export] ボタンをクリックすれば、アイコン画像設定の一覧を XML ファイルから読み込み、
XML ファイルへ保存することができます。
<br>


&aname(offline);
### オフラインエディタ
オフラインエディタでポート接続時に選択できるパラメーターを設定することができます。<br>
設定可能な項目は [Interface Type]、[Data Flow Type]、[Subscription Type] で、ポート接続時にここで設定したパラメーターから値を選択することができます。
それぞれの意味についてはデータポート間接続を参照してください。<br>
<br>

<div align="center"><a href="fig91OfflineEditor.png"><img src="fig91OfflineEditor.png" width="60%;"></a></div>
<div align="center"><strong>オフライン設定画面</strong></div>
<br>


&aname(online);
### オンラインエディタ
オンラインエディタで、RTC のアクション実行時に、事前の実行確認を行うかを設定します。
初期値はチェックなし（確認を行わない）です。

<div align="center"><a href="fig92OnineEditor.png"><img src="fig92OnineEditor.png" width="60%;"></a></div>
<div align="center"><strong>オンライン設定画面</strong></div>
<br>


## RT Name Service View

&aname(ns-conn);
### 接続周期
接続周期とは、RT Name Service View がシステムの情報を収集して表示へ反映する周期のことです。&br
接続周期は、ネームサービスビューとシステムエディタの2つがあります。単位はミリ秒で、0 を指定した場合には、同期は行われません。

<div align="center"><a href="figNS20ConnectCycle.png"><img src="figNS20ConnectCycle.png" width="60%;"></a></div>
<div align="center"><strong>接続周期設定画面</strong></div>
<br>


&aname(ns-sync);
### 同期
タイムアウト待ち時間は、システムの情報を収集する際、システムとの接続が確立されない場合に待機する時間です（単位はミリ秒）。

<div align="center"><a href="figNS21SyncCycle.png"><img src="figNS21SyncCycle.png" width="60%;"></a></div>
<div align="center"><strong>接続周期設定画面</strong></div>
<br>

接続周期と同期タイムアウト待ち時間の関係は下図のようになります。<br>
（例 接続周期が1000ms、同期タイムアウト待ち時間が100msの場合）<br>

<div align="center"><a href="figNS22SyncCycleAndTimeOut.png"><img src="figNS22SyncCycleAndTimeOut.png" width="60%;"></a></div>
<div align="center"><strong>接続周期と同期タイムアウト待ち時間の関係</strong></div>
<br>

