---
layout: page
title: ラズパイマウス用 rtc のインストール(windows)
---

<!-- Title: ラズパイマウス用 RTC のインストール(Windows) -->
#contents


# スクリプトファイル
RTC の起動、RTシステムの復元を自動化するためのスクリプトファイルです。
[ここ](https://github.com/Nobu19800/RaspberryPiMouseRTSystem_script/archive/master.zip) からダウンロードしてください。

# RaspberryPiMouseGUI
ラズパイマウス操作用GUIです。
スクリプトファイルの項目でダウンロードしたファイルの中に同梱されています。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseGUI/RaspberryPiMouseGUI.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseGUI/RaspberryPiMouseGUI.png" width="60%;"></a></div>

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseGUI_comp.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/Components/RaspberryPiMouseGUI_comp.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">RaspberryPiMouseGUI</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>current_velocity</td>
    <td>RTC::TimedVelocity2D</td>
    <td>現在の速度</td>
  </tr>
  <tr>
    <td>current_pose</td>
    <td>RTC::TimedPose2D</td>
    <td>現在の位置、姿勢</td>
  </tr>
  <tr>
    <td>distance_sensor</td>
    <td>RTC::TimedShortSeq</td>
    <td>距離センサの計測値</td>
  </tr>
  <tr>
    <td>orientation</td>
    <td>RTC::TimedOrientation3D</td>
    <td>現在の姿勢</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>target_velocity</td>
    <td>RTC::TimedVelocity2D</td>
    <td>目標速度</td>
  </tr>
  <tr>
    <td>target_position</td>
    <td>RTC::TimedPoint2D</td>
    <td>目標位置(未使用)</td>
  </tr>
  <tr>
    <td>update_pose</td>
    <td>RTC::TimedPose2D</td>
    <td>位置再設定</td>
  </tr>
</table>

