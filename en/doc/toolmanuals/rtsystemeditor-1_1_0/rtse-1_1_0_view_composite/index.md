---
layout: page
title: ビュー（複合コンポーネントビュー編）
---
-------jp page!!-------

<!-- Title: ビュー（複合コンポーネントビュー編） -->
<!-- #contents -->

ここでは複合コンポーネントビューについて説明します。
<br>

<div align="center"><a href="fig18CompositeComponentView.png"><img src="fig18CompositeComponentView.png" width="70%;"></a></div>
<div align="center"><strong>複合コンポーネントビューの位置</strong></div>
<br>

複合コンポーネントビューでは、選択された複合 RTC のポート公開情報が表示され、ポートの公開/非公開を設定することができます。
<br>

<div align="center"><a href="fig19CompositeComponentView.png"><img src="fig19CompositeComponentView.png" width="100%;"></a></div>
<div align="center"><strong>複合コンポーネントビュー</strong></div>
<br>

<div align="center"><strong>複合コンポーネントビューの画面構成</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>①</td>
    <td>複合 RTC のインスタンス名。</td>
  </tr>
  <tr>
    <td>②</td>
    <td>複合 RTC のタイプ名。</td>
  </tr>
  <tr>
    <td>③</td>
    <td>ポートの公開/非公開の状態。</td>
  </tr>
  <tr>
    <td>④</td>
    <td>複合 RTC に含まれる子 RTC のインスタンス名。</td>
  </tr>
  <tr>
    <td>⑤</td>
    <td>複合 RTC に含まれる子 RTC のポート名。</td>
  </tr>
  <tr>
    <td>⑥</td>
    <td>ポートの公開/非公開の変更を反映させます。</td>
  </tr>
  <tr>
    <td>⑦</td>
    <td>ポートの公開/非公開の変更をキャンセルします。</td>
  </tr>
</table>

複合コンポーネントビューで編集中の情報は、⑥の [Apply] ボタンがクリックされるまで適用されません。また、修正中(未適用)の情報は薄い赤色で表示されます。また、システムエディタ上で選択したポートは薄い黄色で表示されます。
<br>

<div align="center"><a href="fig20CompsiteComponentView.png"><img src="fig20CompsiteComponentView.png" width="60%;"></a></div>
<div align="center"><strong>ポート公開/非公開の編集中</strong></div>
<br>

<div align="center"><a href="fig21CompsiteComponentView.png"><img src="fig21CompsiteComponentView.png" width="60%;"></a></div>
<div align="center"><strong>システムエディタ上で選択中のポート</strong></div>
<br>

複合コンポーネントのポートが、別のコンポーネントのポートと接続されている場合は、複合コンポーネントビューで該当のポートがグレイで表示され、編集不可となります。
<br>

<div align="center"><a href="fig22CompsiteComponentView.png"><img src="fig22CompsiteComponentView.png" width="60%;"></a></div>
<div align="center"><strong>他のポートと接続中の場合</strong></div>
<br>

-------jp page!!-------
