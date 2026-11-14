---
layout: page
title: views (log view)
---

<!-- Title: ビュー（ログビュー編） -->
<!-- #contents -->

This section explains the Log View.
<br>

<div align="center"><a href="fig31LogView.jpg"><img src="fig31LogView.jpg" width="85%;"></a></div>
<div align="center"><strong>Location of the Log View</strong></div>
<br>

The Log View displays a list of RTCs targeted for log collection on the selected diagram, and displays log messages notified from the RTCs.<br>
You can select the RTCs you want to display, and you can also filter the display by log level.
<br>

<div align="center"><a href="fig32LogView.png"><img src="fig32LogView.png" width="100%;"></a></div>
<div align="center"><strong>Log View</strong></div>
<br>

<div align="center"><strong>Screen Layout of the Log View</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>①</td>
    <td>Displays a list of RTCs in the selected diagram that are targeted for log collection.<br>Logs of RTCs checked here are displayed.</td>
  </tr>
  <tr>
    <td>②</td>
    <td>Specifies the threshold of the log level to display.<br>Log messages at or above the specified level are displayed.</td>
  </tr>
  <tr>
    <td>③</td>
    <td>Displays log messages.<br> The display is filtered by RTC selection and log level specification.<br>The displayed items are as follows.<br>・Timestamp<br>・Log level (SILENT/ERROR/WARN/INFO/DEBUG/TRACE/VERBOSE/PARANOID)<br>・RTC instance name<br>・Log notification target<br>・Log message</td>
  </tr>
</table>
<!-- |③|ログメッセージを表示。&br; RTC の選択、およびログレベル指定により、表示をフィルタリングする。&br;表示項目は次のとおり。&br;・タイムスタンプ&br;・ログレベル（ERROR/WARN/INFO/NORMAL/DEBUG/TRACE/VERBOSE/PARANOID）&br;・RTC のインスタンス名&br;・ログ通知対象&br;・ログメッセージ| -->

When a diagram is selected, the list of RTCs targeted for log collection on the diagram is displayed in ①. Logs are notified from RTCs by the log notification observer function, and RTCs for which observers have been registered become targets for log collection.<br>
When you select (check) the RTCs whose logs you want to display from the list, messages are displayed in the log display table in ③.<br>
Log messages can also be filtered by log level. When you select the threshold level from the combo box in ②, only logs at or above the selected level are displayed. For example, if "INFO" is selected in the combo box, only "ERROR", "WARN", and "INFO" messages are displayed.
<br>

<div align="center"><a href="fig33LogFiltering.png"><img src="fig33LogFiltering.png" width="100%;"></a></div>
<div align="center"><strong>Filtering the Log Display</strong></div>
<br>
