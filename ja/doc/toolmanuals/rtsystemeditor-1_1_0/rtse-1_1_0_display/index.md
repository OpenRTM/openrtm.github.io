---
layout: page
title: システムエディタ（rtc の表示 / 描画編集 編）
---

<!-- Title: システムエディタ（RTC の表示 / 描画編集 編） -->
#contents

RTC の表示と RTC の描画編集の操作を説明します。

&aname(RTCcolor);
### RTC の表示
システムエディタに配置された RTC は矩形で表示され、ポートはその矩形の周りに表示されます。また、それぞれの状態が色で表現されます。
<br>

<div align="center"><a href="fig43RTCDisplayExample.png"><img src="fig43RTCDisplayExample.png" width="50%;"></a></div>
<div align="center"><strong>RTC 表示の例</strong></div>
<br>

アイコンと状態色の一覧は以下のとおりです。
<br>

<div align="center"><strong>コンポーネントとポートのアイコン</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>名前</th>
    <th>形状</th>
    <th>状態</th>
    <th colspan="2" style="text-align: center;">デフォルト色（※）</th>
  </tr>
  <tr style="text-align: center;">
    <td>１</td>
    <td>RTC</td>
    <td><a href="IconShape.png"><img src="IconShape.png" width="30%;"></a></td>
    <td>CREATED</td>
    <td><a href="IconWhite.png"><img src="IconWhite.png" width="50%;"></a></td>
    <td>White</td>
  </tr>
  <tr style="text-align: center;">
    <td></td>
    <td></td>
    <td></td>
    <td>INACTIVE</td>
    <td><a href="IconBlue.png"><img src="IconBlue.png" width="50%;"></a></td>
    <td>Blue</td>
  </tr>
  <tr style="text-align: center;">
    <td></td>
    <td></td>
    <td></td>
    <td>ACTIVE</td>
    <td><a href="IconLightGreen.png"><img src="IconLightGreen.png" width="50%;"></a></td>
    <td>Light Green</td>
  </tr>
  <tr style="text-align: center;">
    <td></td>
    <td></td>
    <td></td>
    <td>ERROR</td>
    <td><a href="IconRed.png"><img src="IconRed.png" width="50%;"></a></td>
    <td>Red</td>
  </tr>
  <tr style="text-align: center;">
    <td></td>
    <td></td>
    <td></td>
    <td>UNKNOWN</td>
    <td><a href="IconBlack.png"><img src="IconBlack.png" width="50%;"></a></td>
    <td>Black</td>
  </tr>
  <tr style="text-align: center;">
    <td>2</td>
    <td>Execution Context <br>（1番目のみ）</td>
    <td>（RTCの矩形の外周線）</td>
    <td>RUNNING</td>
    <td><a href="IconGray.png"><img src="IconGray.png" width="50%;"></a></td>
    <td>Gray</td>
  </tr>
  <tr style="text-align: center;">
    <td></td>
    <td></td>
    <td></td>
    <td>STOPPED</td>
    <td><a href="IconBlack.png"><img src="IconBlack.png" width="50%;"></a></td>
    <td>Black</td>
  </tr>
  <tr style="text-align: center;">
    <td>3</td>
    <td>InPort</td>
    <td><a href="IconInPort.png"><img src="IconInPort.png" width="30%;"></a></td>
    <td>未接続</td>
    <td><a href="IconBlue.png"><img src="IconBlue.png" width="50%;"></a></td>
    <td>Blue</td>
  </tr>
  <tr style="text-align: center;">
    <td></td>
    <td></td>
    <td></td>
    <td>接続済（1つ以上）</td>
    <td><a href="IconLightGreen.png"><img src="IconLightGreen.png" width="50%;"></a></td>
    <td>Light Green</td>
  </tr>
  <tr style="text-align: center;">
    <td>4</td>
    <td>OutPort</td>
    <td><a href="IconOutPort.png"><img src="IconOutPort.png" width="30%;"></a></td>
    <td>未接続</td>
    <td><a href="IconBlue.png"><img src="IconBlue.png" width="50%;"></a></td>
    <td>Blue</td>
  </tr>
  <tr style="text-align: center;">
    <td></td>
    <td></td>
    <td></td>
    <td>接続済（1つ以上）</td>
    <td><a href="IconLightGreen.png"><img src="IconLightGreen.png" width="50%;"></a></td>
    <td>Light Green</td>
  </tr>
  <tr style="text-align: center;">
    <td>5</td>
    <td>ServicePort</td>
    <td><a href="IconServicePort.png"><img src="IconServicePort.png" width="30%;"></a></td>
    <td>未接続</td>
    <td><a href="IconLightBlue.png"><img src="IconLightBlue.png" width="50%;"></a></td>
    <td>Light Blue</td>
  </tr>
  <tr style="text-align: center;">
    <td></td>
    <td></td>
    <td></td>
    <td>接続済（1つ以上）</td>
    <td><a href="IconCyan.png"><img src="IconCyan.png" width="50%;"></a></td>
    <td>Cyan</td>
  </tr>
</table>

**'※各状態の色は、設定画面の [表示色]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_setting#color) にて変更することができます。**'

また、RTC の種別やカテゴリに合わせてアイコン画像をつけることができます。
<br>

<div align="center"><a href="fig44RTCDisplayIconExample.png"><img src="fig44RTCDisplayIconExample.png" width="70%;"></a></div>
<div align="center"><strong>RTC のアイコン画像表示の例</strong></div>
<br>

**'※アイコン画像は、設定画面の [アイコン]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_1_0/rtse-1_1_0_setting#icon) にて変更することができます。**'


### RTC の同期
システムエディタへ配置した RTC の状態を監視し、リアルタイムに表示を更新します。<br>
監視方法には状態通知オブザーバ方式（OpenRTM-aist 1.1以降）、もしくはポーリングによる周期チェックがあり、設定画面の接続にて監視パラメーターを変更することができます。<br>
システムエディタへ RTC を配置するときに、ミドルウェアのバージョンをチェックし、オブザーバ対応であれば RTC へオブザーバを登録します。オブザーバ未対応の場合は周期的に状態の問い合わせを行います。
<br>

<div align="center"><a href="fig45StatusObserver.png"><img src="fig45StatusObserver.png" width="70%;"></a></div>
<div align="center"><strong>状態通知オブザーバー</strong></div>
<br>

システムエディタから RTC を削除すると、オブザーバも解除します。<br>
状態通知オブザーバが通知する内容は次のとおりです。
<br>

<div align="center"><strong>状態通知オブザーバの通知内容</strong></div>
<table class="table-alt">
  <tr>
    <td>通知</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>COMPONENT_PROFILE</td>
    <td>RTC のコンポーネントプロファイルに変更があった場合に通知</td>
  </tr>
  <tr>
    <td>RTC_STATUS</td>
    <td>RTC の状態<br>新しい状態と対象となる EC の ID を通知</td>
  </tr>
  <tr>
    <td>EC_STATUS</td>
    <td>実行コンテキストの状態<br>実行レートの変更、EC の開始/停止、RTC のアタッチ/デタッチを通知</td>
  </tr>
  <tr>
    <td>PORT_PROFILE</td>
    <td>ポートの状態<br>ポートの追加/削除、コネクションの接続/切断を通知</td>
  </tr>
  <tr>
    <td>CONFIGURATION</td>
    <td>コンフィグレーションの状態<br>コンフィグレーションの追加/変更/削除、アクティブなコンフィグレーションの切り替えを通知</td>
  </tr>
</table>

また、RTC の生存確認のため、一定間隔でハートビートを通知します。<br>
ハートビートが一定回数通知されないと、RTC が異常終了したとみなしてシステムエディタ上から削除します。
<br>


### RTC の描画編集
ここでは、RTC の描画編集について説明していきます。(「編集」ではなく「描画編集」とあえてしているのは、ここで説明される作業は描画の編集であり、システムに対する影響は全くないためです。)

- RTC の大きさの変更と移動（システムに対する影響なし)~
RTC を移動するには、RTC を選択後、ドラッグして動かします。 RTC の大きさを変更するには、 RTC を選択することで表示されるハンドルをドラッグして動かします。
<br>

<div align="center"><a href="fig46RTCMoveResize.png"><img src="fig46RTCMoveResize.png" width="60%;"></a></div>
<div align="center"><strong> RTC の移動（左）とRTC の大きさの変更（右）</strong></div>
<br>

また、選択された RTC の位置と大きさがステータスバーに表示されます。
<br>

<div align="center"><a href="fig47StatusBar.png"><img src="fig47StatusBar.png" width="60%;"></a></div>
<div align="center"><strong>ステータスバー</strong></div>
<br>

- RTC の回転（システムに対する影響なし）~
対象のコンポーネントを選択し、Ctrlキーを押しながらマウスの右ボタンをクリックすることで、水平の向きへ回転します。Shiftキーを押しながらマウスの右ボタンをクリックすることで、垂直の向きへ回転します。それぞれ同じ操作を繰り返し行うことで逆の水平の向き、逆の垂直の向きへ変更でき、上下左右の向きへ操作することができます。
<br>

<div align="center"><a href="fig48RTCRotate.png"><img src="fig48RTCRotate.png" width="70%;"></a></div>
<div align="center"><strong>回転された RTC</strong></div>
<br>


- RTC の削除（システムに対する影響なし）~
RTC を削除するには、RTCを選択し [Delete] ボタンをクリックするか、コンテキストメニューから [Delete] を選択してください。
<br>

<div align="center"><a href="fig49DeleteComponent.png"><img src="fig49DeleteComponent.png" width="50%;"></a></div>
<div align="center"><strong>RTC の削除</strong></div>
<br>


- ポート間の接続線を移動する（システムに対する影響なし）~
接続線を移動するには、接続線を選択し表示されるハンドラを移動します。垂直線は左右に、水平線は上下に移動することができます。
<br>

<div align="center"><a href="fig50MoveConnection.png"><img src="fig50MoveConnection.png" width="70%;"></a></div>
<div align="center"><strong>垂直線（左）と水平線の（右）の接続線の移動</strong></div>
<br>

