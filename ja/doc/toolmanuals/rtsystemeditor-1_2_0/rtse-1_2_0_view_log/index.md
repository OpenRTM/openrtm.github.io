---
layout: page
title: ビュー（ログビュー編）
---

<!-- Title: ビュー（ログビュー編） -->
<!-- #contents -->

ここではログビューについて説明します。
<br>

<div align="center"><a href="fig31LogView.jpg"><img src="fig31LogView.jpg" width="85%;"></a></div>
<div align="center"><strong>ログビューの位置</strong></div>
<br>

ログビューは、選択したダイアグラム上のログ収集対象の RTC 一覧を表示し、RTC から通知されたログメッセージを表示します。<br>
表示したい RTC を選択でき、また、ログレベルによって表示をフィルタリングすることもできます。
<br>

<div align="center"><a href="fig32LogView.png"><img src="fig32LogView.png" width="100%;"></a></div>
<div align="center"><strong>ログビュー</strong></div>
<br>

<div align="center"><strong>ログビューの画面構成</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>①</td>
    <td>選択中のダイアグラム内の RTC のうち、ログ収集対象となっているものの一覧を表示。<br>ここでチェックをつけた RTC のログが表示される。</td>
  </tr>
  <tr>
    <td>②</td>
    <td>表示するログレベルのしきい値を指定。<br>指定されたレベル以上のログメッセージを表示する。</td>
  </tr>
  <tr>
    <td>③</td>
    <td>ログメッセージを表示。<br> RTC の選択、およびログレベル指定により、表示をフィルタリングする。<br>表示項目は次のとおり。<br>・タイムスタンプ<br>・ログレベル（SILENT/ERROR/WARN/INFO/DEBUG/TRACE/VERBOSE/PARANOID）<br>・RTC のインスタンス名<br>・ログ通知対象<br>・ログメッセージ</td>
  </tr>
</table>
<!-- |③|ログメッセージを表示。&br; RTC の選択、およびログレベル指定により、表示をフィルタリングする。&br;表示項目は次のとおり。&br;・タイムスタンプ&br;・ログレベル（ERROR/WARN/INFO/NORMAL/DEBUG/TRACE/VERBOSE/PARANOID）&br;・RTC のインスタンス名&br;・ログ通知対象&br;・ログメッセージ| -->

ダイアグラムを選択すると、ダイアグラム上のログ収集対象 RTC の一覧を①に表示します。ログは、ログ通知オブザーバー機能により RTC から通知され、オブザーバーを登録したものがログ収集対象となります。<br>
一覧からログを表示したい RTC を選択（チェック）すると、③のログ表示テーブルにメッセージを表示します。<br>
また、ログメッセージはログレベルによって表示をフィルタリングすることができます。②のコンボボックスでしきい値となるレベルを選択すると、選択したレベル以上のログのみ表示します。たとえば、コンボボックスで「INFO」を選択すると、「ERROR」「WARN」「INFO」のメッセージのみ表示されます。
<br>

<div align="center"><a href="fig33LogFiltering.png"><img src="fig33LogFiltering.png" width="100%;"></a></div>
<div align="center"><strong>ログ表示のフィルタリング</strong></div>
<br>


