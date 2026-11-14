---
layout: page
title: ビュー（プロパティビュー編）
---

<!-- Title: ビュー（プロパティビュー編） -->
<!-- #contents -->

ここではプロパティビューについて説明します。
<br>

<div align="center"><a href="fig34propertyView.png"><img src="fig34propertyView.png" width="70%;"></a></div>
<div align="center"><strong>プロパティビューの位置</strong></div>
<br>

プロパティビューでは、 System Dialog で選択された RTC やコネクタのプロファイル情報をリアルタイムに表示します。（ RTC の選択中であっても変更が検出されれば即座に反映されます）
<br>

<table class="table-alt">
  <tr>
    <th>RTCの場合</th>
    <th>複合RTCの場合</th>
    <th>マネージャの場合</th>
  </tr>
  <tr>
<td><a href="fig353TypePropertyView1.png"><img src="fig353TypePropertyView1.png" width="80%;"></a></td>
<td><a href="fig353TypePropertyView2.png"><img src="fig353TypePropertyView2.png" width="80%;"></a></td>
<td><a href="fig353TypePropertyView3.png"><img src="fig353TypePropertyView3.png" width="80%;"></a></td>
  </tr>
</table>

<div align="center"><strong>プロパティビュー</strong></div>
<br>

表示されるアイコンの意味は以下のとおりです。
<br>

<div align="center"><strong>プロパティアイコンの一覧</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>アイコン</th>
    <th>名前</th>
    <th>表示内容</th>
  </tr>
  <tr>
    <td>1</td>
<td><a href="IconRTC2.png"><img src="IconRTC2.png" width="30%;"></a></td>
<td>RTC</td>
<td>InstanceName、TypeName、Description、Vender、Category、State(※1番目の ExecutionContext の LifeCycleState を基にして表示される)</td>
  </tr>
  <tr>
    <th>2</th>
<td><a href="IconExecContext.png"><img src="IconExecContext.png" width="30%;"></a>
<td>ExecutionContext</td>
<td>State、Kind、Rate</td>
  </tr>
  <tr>
    <th>3</th>
<td><a href="IconServicePort.png"><img src="IconServicePort.png" width="30%;"></a></td>
<td>ServicePort</td>
<td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <th>4</th>
<td><a href="IconOutPort.png"><img src="IconOutPort.png" width="30%;"></a></td>
<td>Outport</td>
<td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <th>5</th>
<td><a href="IconInPort.png"><img src="IconInPort.png" width="30%;"></a></td>
<td>Inport</td>
<td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <th>6</th>
<td><a href="IconPIP.png"><img src="IconPIP.png" width="30%;"></a></td>
<td>PortInterfaceProfile</td>
<td>InterfaceName、TypeName、PortInterfacePolarity</td>
  </tr>
  <tr>
    <th>7</th>
<td><a href="IconMgr.png"><img src="IconMgr.png" width="30%;"></a></td>
<td>マネージャー</td>
<td>Components (生成したコンポーネント名のリスト)<br>Loadable Modules (ロード可能なモジュール名のリスト)<br>Loaded Modules (ロード済みのモジュール名のリスト)</td>
  </tr>
</table>

なお、RTC の仕様では、RTC  のLifeCycleState は ExecutionContext ごとに存在します。したがって、状態は複数存在しますが、RT System Editorでは1番目の ExecutionContext のみを使用して STATE を 表示します。
<br>

<!-- Title: ビュー（プロパティビュー編） -->
<!-- #contents -->

ここではプロパティビューについて説明します。
<br>

<div align="center"><a href="fig34propertyView.png"><img src="fig34propertyView.png" width="70%;"></a></div>
<div align="center"><strong>プロパティビューの位置</strong></div>
<br>

プロパティビューでは、 System Dialog で選択された RTC やコネクタのプロファイル情報をリアルタイムに表示します。（ RTC の選択中であっても変更が検出されれば即座に反映されます）
<br>

<table class="table-alt">
  <tr>
    <th>RTCの場合</th>
    <th>複合RTCの場合</th>
    <th>マネージャの場合</th>
  </tr>
  <tr>
<td><a href="fig353TypePropertyView1.png"><img src="fig353TypePropertyView1.png" width="80%;"></a></td>
<td><a href="fig353TypePropertyView2.png"><img src="fig353TypePropertyView2.png" width="80%;"></a></td>
<td><a href="fig353TypePropertyView3.png"><img src="fig353TypePropertyView3.png" width="80%;"></a></td>
  </tr>
</table>
<div align="center"><strong>プロパティビュー</strong></div>
<br>

表示されるアイコンの意味は以下のとおりです。
<br>

<div align="center"><strong>プロパティアイコンの一覧</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>アイコン</th>
    <th>名前</th>
    <th>表示内容</th>
  </tr>
  <tr>
    <td>1</td>
<td><a href="IconRTC2.png"><img src="IconRTC2.png" width="30%;"></a></td>
<td>RTC</td>
<td>InstanceName、TypeName、Description、Vender、Category、State(※1番目の ExecutionContext の LifeCycleState を基にして表示される)</td>
  </tr>
  <tr>
    <th>2</th>
<td><a href="IconExecContext.png"><img src="IconExecContext.png" width="30%;"></a></td>
<td>ExecutionContext</td>
<td>State、Kind、Rate</td>
  </tr>
  <tr>
    <th>3</th>
<td><a href="IconServicePort.png"><img src="IconServicePort.png" width="30%;"></a></td>
<td>ServicePort</td>
<td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <th>4</th>
<td><a href="IconOutPort.png"><img src="IconOutPort.png" width="30%;"></a></td>
<td>Outport</td>
<td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <th>5</th>
<td><a href="IconInPort.png"><img src="IconInPort.png" width="30%;"></a></td>
<td>Inport</td>
<td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <th>6</th>
<td><a href="IconPIP.png"><img src="IconPIP.png" width="30%;"></a></td>
<td>PortInterfaceProfile</td>
<td>InterfaceName、TypeName、PortInterfacePolarity</td>
  </tr>
  <tr>
    <th>7</th>
<td><a href="IconMgr.png"><img src="IconMgr.png" width="30%;"></a></td>
<td>マネージャー</td>
<td>Components (生成したコンポーネント名のリスト)<br>Loadable Modules (ロード可能なモジュール名のリスト)<br>Loaded Modules (ロード済みのモジュール名のリスト)</td>
  </tr>

なお、RTC の仕様では、RTC  のLifeCycleState は ExecutionContext ごとに存在します。したがって、状態は複数存在しますが、RT System Editorでは1番目の ExecutionContext のみを使用して STATE を 表示します。
<br>

