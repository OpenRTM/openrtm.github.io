---
layout: page
title: raspberry pi mouse 活用事例
---

<!-- Title: Raspberry Pi Mouse 活用事例 -->
<!-- #contents -->

Raspberry Pi Mouse (以下ラズパイマウス) はアールティが販売している二輪方式の移動ロボットです。
Raspberry Pi を搭載しているため Linux (Raspbian) 等での開発が可能です。

<div align="center"><a href="s_DSC00444.JPG"><img src="s_DSC00444.JPG" width="50%;"></a></div>

このドキュメントではラズパイマウスでの OpenRTM-aist の利用方法等を紹介します。


## 仕様

<table class="table-alt">
  <tr>
    <th colspan="2" style="text-align: center;">ラズパイマウスの仕様</th>
  </tr>
  <tr>
    <td>CPU</td>
    <td>Raspberry Pi 2 Model B</td>
  </tr>
  <tr>
    <td>モーター</td>
    <td>ステッピングモーターST-42BYG020 2個</td>
  </tr>
  <tr>
    <td>モータードライバー</td>
    <td>SLA7070MRPT 2個</td>
  </tr>
  <tr>
    <td>距離センサー</td>
    <td>赤色LED+フォトトランジスタ(ST-1K3) 4個</td>
  </tr>
  <tr>
    <td>モニター用赤色LED</td>
    <td>4個</td>
  </tr>
  <tr>
    <td>ブザー</td>
    <td>1個</td>
  </tr>
  <tr>
    <td>スイッチ</td>
    <td>3個</td>
  </tr>
  <tr>
    <td>バッテリー</td>
    <td>LiPo3セル(11.1V)1000mAh 1個</td>
  </tr>
</table>

<hr>

- [チュートリアル(Raspberry Pi Mouse)](./raspimouse_tutorial)
- [チュートリアル(Raspberry Pi Mouse、RTM講習会)](./raspimouse_tutorial_rtm_seminar)
- [チュートリアル(Raspberry Pi Mouse、強化月間用)](./raspimouse_tutorial_bootcamp)
- [初期設定等](./raspimouse_init)
- [動作確認](./raspimouse_test)
- [ラズパイマウス用 RTC のインストール(Raspbian)](./raspimouse_rtc_on_raspbian)
- [ラズパイマウス用 RTC のインストール(Windows)](./raspimouse_rtc_on_windows)
- [サンプルの RTシステムの実行]({{ site.baseurl }}/ja/content/sample_system_raspimouse)
- [自作の RTC で制御]({{ site.baseurl }}/ja/content/rtc_create_raspimouse)
- [補足等](./raspimouse_appendix)
- [シミュレーター利用方法](./raspimouse_simulator_use)
- [コンパイル方法 (Ubuntu、CMake、Code::Blocks利用)]({{ site.baseurl }}/ja/content/build_ubuntu_codeblocks)

