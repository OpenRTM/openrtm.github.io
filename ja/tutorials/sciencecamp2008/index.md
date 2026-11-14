---
layout: page
title: サイエンスキャンプ(2008年8月21日)
---

#contents


- [サマーサイエンスキャンプWebページ](http://ppd.jsf.or.jp/camp/)

サイエンスキャンプは、文部科学省の科学技術関係人材総合プランの施策「サイエンス・パートナーシップ・プロジェクト」の一環として、最先端の研究施設・実験装置等を有する大学・公的研究機関・民間企業の研究所が、夏休み・冬休み・春休みの３日間高校生を受け入れて、ライフサイエンス、情報通信、環境、ナノテクノロジー・材料、エネルギー、製造技術、（宇宙・海洋等の）フロンティア、地球科学などの科学技術分野において、直接指導を行う実験や実習を主体とした、科学技術体験合宿プログラムです。


## 日時・参加人数
- **日時**: 2008年8月20日-22日
- **場所**: [産総研 本部・情報棟1F ネットワーク会議室](http://www.aist.go.jp/aist_j/guidemap/tsukuba/center/tsukuba_map_c02.html)
- **参加者**:5名

## 資料
- [1日目「RTで自分のアイディアを実現しよう」](./080820.pdf)(no_link)
- [2日目「ロボットはどのように動いているのか」](./080821.pdf)(no_link)

# プログラム
<table class="table-alt">
  <tr>
    <td>></td>
    <td>CENTER:**8月20日(初日)午後 (3h)**</td>
  </tr>
  <tr>
    <td>14:15-17:00 (担当：神徳)</td>
    <td>-自己紹介(各人5分)<br>-プロジェクト概要(45分)<br>-ロボットアームの基礎(45分)<br>-宿題の説明(15分)<br>-宿題：ロボットアームの設計と必要な計算式(各自：ロボットアームを組み立ててくる)</td>
  </tr>
  <tr>
    <td>></td>
    <td>CENTER:**8月21日(2日目)午前(3h)**</td>
  </tr>
  <tr>
    <td>9:00-12:00 (担当：安藤)</td>
    <td>-OpenRTMとNXTソフトのインストール<br>-ソフトウエア構成の概要<br>-インストール作業<br>-動作確認<br>-ロボットアームの課題<br> -(事前準備：自分のアームを動かして確かめる)</td>
  </tr>
  <tr>
    <td>></td>
    <td>CENTER:**8月21日(2日目) 午後(4h)**</td>
  </tr>
  <tr>
    <td>13:00-17:00 (担当：神徳・安藤)</td>
    <td>-ロボットアームの課題<br>-自己紹介(仲間との共通点探し)<br>-ロボットアームの課題<br> -課題：友達のアームを繋いで遠隔操作<br> - 発展課題：スケールを変える<br> - 発展課題：他のディバイスを繋ぐ<br>-宿題：プロジェクト成果まとめと将来実現してみたいこと。</td>
  </tr>
  <tr>
    <td>17:30-19:00</td>
    <td>懇親会</td>
  </tr>
  <tr>
    <td>></td>
    <td>CENTER:**8月22日(3日目) 午前(3h)**</td>
  </tr>
  <tr>
    <td>9:00-12:00 (担当：神徳、安藤)</td>
    <td>-プロジェクト成果発表<br>-グループ発表準備(30分)<br>-成果発表用システム構築(30分)<br> -皆のアームをつないで一度に動かす<br> - 感想とコメント(各人5分)</td>
  </tr>
</table>

## インストールするソフトウエア
- プログラミング言語Pythonのインタプリタ(exeを実行してインストール)
  - [Python2.5](http://www.python.org/ftp/python/2.5.1/python-2.5.1.msi)
- RTミドルウエアのPython版(msiを実行してインストール)
  - [OpenRTM-aist-Python](http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python2.5-0.4.1-RELEASE.msi)
- RTミドルウエアに必要なライブラリ(exeを実行してインストール)
  - [omniORBpy](http://www.openrtm.org/pub/Windows/omniORB/omniORBpy-3.1.msi)
- PythonからBluetoothを使うために必要なモジュール(exeを実行してインストール)
  - [pyBlues](http://pybluez.googlecode.com/files/PyBluez-0.15.win32-py2.5.exe)
- PythonからLEGO Mindstorm NXTを使うために必要なモジュール(下の指示に従ってインストール)
  - [nxtpython]()（リンク切れです）
 zipを展開後、展開したフォルダの中(setup.pyがあるフォルダ)でコマンドプロンプトから

```
 > c:\python25\python setup.py install
```
と入力
- USB汎用ドライバ、NXTをUSB経由で使うために必要(exeを実行してインストール)
  - [libusb]()（リンク切れです）
- PythonからUSBを使うために必要なモジュール(exeを実行してインストール)
  - [pyusbhttp]()（リンク切れです）
- RtcLink、RTミドルウエアを使うためのツール(zipを展開して出てきたフォルダのeclipse.exeを実行して起動)
  - [eclipse]()（リンク切れです）
- RTミドルウエアのC++版(exeを実行してインストール)
  - [OpenRTM-aist-C++]()（リンク切れです）
- RTミドルウエアC++版を使うために必要なライブラリ(exeを実行してインストール)
  - [omniORB](http://www.openrtm.org/pub/Windows/omniORB/omniORB-4.1.2_vc9.msi)
- RTミドルウエアC++版を使うために必要なライブラリ(exeを実行してインストール)
  - [ACE](http://www.openrtm.org/pub/Windows/ace/ACE-5.6_vc9.msi)
- RTミドルウエアC++版を使うために必要なライブラリ(Microsoftのサイトに飛ぶのでダウンロードボタンを押してインストール)
  - [VC2008DLL](http://www.microsoft.com/downloads/details.aspx?displaylang=ja&FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf)

- 講習会用サンプル(USBドライバも入っています。)
  - [講習会用サンプル](./ScienceCamp.zip)(no_link)
  - NXTをUSBで接続したら、デバイスドライバのインストールウィザードが表示されるので、「接続しない」を選んで「特定の場所からインストールするを選び」フォルダの参照ボタンを押してUSBDriverフォルダを選択して「次へ」を押すとインストールできます。

