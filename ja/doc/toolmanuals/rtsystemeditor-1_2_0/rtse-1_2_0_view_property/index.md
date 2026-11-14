---
layout: page
title: ビュー（プロパティビュー編）
---
<!-- Title: ビュー（プロパティビュー編） -->
<!-- #contents -->

ここではプロパティビューについて説明します。
<br>

<div align="center"><a href="SystemEditor_Property_01.jpg"><img src="SystemEditor_Property_01.jpg" width="85%;"></a></div>
<div align="center"><strong>プロパティビューの位置</strong></div>
<br>

プロパティビューでは、 System Dialog で選択された RTC やコネクタのプロファイル情報をリアルタイムに表示します。（ RTC の選択中であっても変更が検出されれば即座に反映されます）
<br>

<table class="table-alt">
  <tr>
    <td style="text-align: center;">RTCの場合</td>
    <td style="text-align: center;">複合RTCの場合</td>
    <td style="text-align: center;">マネージャの場合</td>
  </tr>
  <tr>
    <td><div align="center"><a href="fig353TypePropertyView1.png"><img src="fig353TypePropertyView1.png" width="80%;"></a></div></td>
    <td><div align="center"><a href="fig353TypePropertyView2.png"><img src="fig353TypePropertyView2.png" width="80%;"></a></div></td>
    <td><div align="center"><a href="fig353TypePropertyView3.png"><img src="fig353TypePropertyView3.png" width="80%;"></a></div></td>
  </tr>
</table>
<div align="center"><strong>プロパティビュー</strong></div>
<br>

表示されるアイコンの意味は以下のとおりです。
<br>

<div align="center"><strong>プロパティアイコンの一覧</strong></div>
<table class="table-alt">
  <tr>
    <td>No.</td>
    <td>アイコン</td>
    <td>名前</td>
    <td>表示内容</td>
  </tr>
  <tr>
    <td>1</td>
    <td><div align="center"><a href="IconRTC2.png"><img src="IconRTC2.png" width="50%;"></a></div></td>
    <td>RTC</td>
    <td>InstanceName、TypeName、Description、Vender、Category、State(※1番目の ExecutionContext の LifeCycleState を基にして表示される)</td>
  </tr>
  <tr>
    <td>2</td>
    <td><div align="center"><a href="IconExecContext.png"><img src="IconExecContext.png" width="50%;"></a></div></td>
    <td>ExecutionContext</td>
    <td>State、Kind、Rate</td>
  </tr>
  <tr>
    <td>3</td>
    <td><div align="center"><a href="IconServicePort.png"><img src="IconServicePort.png" width="50
%;"></a></div></td>
    <td>ServicePort</td>
    <td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <td>4</td>
    <td><div align="center"><a href="IconOutPort.png"><img src="IconOutPort.png" width="50%;"></a></div></td>
    <td>Outport</td>
    <td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <td>5</td>
    <td><div align="center"><a href="IconInPort.png"><img src="IconInPort.png" width="50%;"></a></div></td>
    <td>Inport</td>
    <td>Name、プロパティ情報のリスト</td>
  </tr>
  <tr>
    <td>6</td>
    <td><div align="center"><a href="IconPIP.png"><img src="IconPIP.png" width="50%;"></a></div></td>
    <td>PortInterfaceProfile</td>
    <td>InterfaceName、TypeName、PortInterfacePolarity</td>
  </tr>
  <tr>
    <td>7</td>
    <td><div align="center"><a href="IconMgr.png"><img src="IconMgr.png" width="50%;"></a></div></td>
    <td>マネージャー</td>
    <td>Components (生成したコンポーネント名のリスト)<br>Loadable Modules (ロード可能なモジュール名のリスト)<br>Loaded Modules (ロード済みのモジュール名のリスト)</td>
  </tr>
</table>



なお、RTC の仕様では、RTC  のLifeCycleState は ExecutionContext ごとに存在します。したがって、状態は複数存在しますが、RT System Editorでは1番目の ExecutionContext のみを使用して STATE を 表示します。
<br>
<br>

