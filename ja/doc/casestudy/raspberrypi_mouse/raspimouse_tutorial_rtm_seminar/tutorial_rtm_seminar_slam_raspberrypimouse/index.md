---
layout: page
title: チュートリアル(slam実習)
---

init
<!-- チュートリアル(SLAM実習) -->
#contents

## はじめに

このページではLiDAR付RaspberryPiマウスを用いてSLAMによるナビゲーションを行います。

<div align="center"><a href="https://rt-net.jp/mobility/wp-content/uploads/2019/12/23b47429c42d672e7f94ae0a3c9c9d6c.png"><img src="https://rt-net.jp/mobility/wp-content/uploads/2019/12/23b47429c42d672e7f94ae0a3c9c9d6c.png" width="70%;"></a></div>

SLAMはSimultaneous Localization and Mappingの略で、環境地図作成と自己位置推定を同時に実行することを指し、本チュートリアルでは[[
移動ロボットのナビゲーションに関わるRTコンポーネント群:https://ogata-lab.jp/ja/technology_ja/mobile_nav_rtcs_ja.html]]を使用します。

移動ロボットのナビゲーションに関わるRTコンポーネント群は[MRPT](https://www.mrpt.org/)という自己位置推定、環境地図作成、経路計画などの機能を提供するクロスプラットフォームなライブラリを使用しています。

## 事前準備

### LiDARの取り付け
まずRaspberryPiマウスにLiDARを取り付けます。

LiDARマウントには2種類あります。以下に記載の(1)専用LiDARマウント、(2)マルチLiDARマウントの取付手順を参考にしてRaspberry Piマウス本体に取り付けてください。

#### 専用LiDARマウント

以下の画像のように2本のねじで止めるマウントの場合、下記の手順で取り付けてください。


<div align="center"><a href="DSC04139.JPG"><img src="DSC04139.JPG" width="50%;"></a></div>


以下のRaspberry Piマウス本体、LiDAR、タッピングビスを用意してください。


<div align="center"><a href="slam29_2.png"><img src="slam29_2.png" width="50%;"></a></div>


次にRaspberry Piマウス底面のねじを外してください。

<div align="center"><a href="slam30.png"><img src="slam30.png" width="50%;"></a></div>

基盤部分をフレームごとずらしてください。

<div align="center"><a href="slam31.png"><img src="slam31.png" width="50%;"></a></div>

次にスペーサーを手で回して外してください。

<div align="center"><a href="slam32.png"><img src="slam32.png" width="50%;"></a></div>

センサ基盤を外してください。


<div align="center"><a href="slam33.png"><img src="slam33.png" width="50%;"></a></div>
<div align="center"><a href="slam34.png"><img src="slam34.png" width="50%;"></a></div>

LiDARをRaspberry Piマウスの上部分に載せてビスで固定してください。

<div align="center"><a href="slam35.png"><img src="slam35.png" width="50%;"></a></div>
<div align="center"><a href="slam36.png"><img src="slam36.png" width="50%;"></a></div>
<div align="center"><a href="slam37.png"><img src="slam37.png" width="50%;"></a></div>

Raspberry PiマウスとLiDARをUSBポートで接続してください。

<div align="center"><a href="slam38.png"><img src="slam38.png" width="50%;"></a></div>
<div align="center"><a href="slam39.png"><img src="slam39.png" width="50%;"></a></div>

外したパーツを元に戻せば完成です。

#### マルチLiDARマウント

以下の画像のように4つのツメを引っかけるマウントの場合、下記の手順で取り付けてください。

<div align="center"><a href="DSC04142.JPG"><img src="DSC04142.JPG" width="50%;"></a></div>

以下のように4つのツメをRaspberry Piマウス本体に引っかけます。

まず、前方の2つのツメを引っかけてください。

<div align="center"><a href="DSC04145.JPG"><img src="DSC04145.JPG" width="50%;"></a></div>

次に後ろのツメを引っかけます。

<div align="center"><a href="DSC04146.JPG"><img src="DSC04146.JPG" width="50%;"></a></div>

そして、マルチLiDARマウントの前方2か所をなべタッピングネジ3-8で固定すれば取付完了です。

<div align="center"><a href="DSC04151.JPG"><img src="DSC04151.JPG" width="50%;"></a></div>

<div align="center"><a href="DSC04147.JPG"><img src="DSC04147.JPG" width="50%;"></a></div>

Raspberry PiマウスとLiDARをUSBポートで接続してください。

<div align="center"><a href="DSC04148.JPG"><img src="DSC04148.JPG" width="50%;"></a></div>


LiDARの取り付け作業が完了したらRaspberryPiマウスの電源スイッチをオンにしてアクセスポイントに接続してください。

<!-- *** MapServer、NavigationManagerのダウンロード -->

<!-- 講習会でUSBメモリを配布している場合は、ダウンロードは不要です。 -->

<!-- MapServer、NavigationManagerはGUIで操作します。 -->
<!-- Raspberry Piでも起動可能ですが、その場合Raspberry Piをディスプレイに接続するか、X Window Systemで他のPCに画面を表示するかする必要があります。 -->
<!-- 今回はMapServer、NavigationManagerをPC上で起動するため、以下から実行に必要なファイルをダウンロードしてください。 -->

<!-- - [[RTM_Tutorial.zip:https://github.com/OpenRTM/RTM_Tutorial/releases/download/20220930/RTM_Tutorial.zip]] -->

<!-- MapServer、NavigationManagerはRTM_Tutorial.zipを展開したフォルダの''Navigation''フォルダに含まれています。 -->

<!-- *** 起動済みのRTC終了 -->

<!-- RobotController、RaspberryPiMouseRTCなどが起動済みの場合は終了します。 -->

<!-- RaspberryPiMouseRTCはWEBブラウザの操作でStopをクリックしてください。 -->

<!-- #ref(slam47.png,/jp/node/7098,center) -->

## SLAMによるナビゲーション地図生成システム

この章では自己位置推定をしながら環境地図生成を行うシステムを試してみます。
MRPTは[ICP-SLAM、RBPF-SLAM](https://www.mrpt.org/List_of_SLAM_algorithms)などのアルゴリズムが使用可能ですが、移動ロボットのナビゲーションに関わるRTコンポーネント群ではICP-SLAMを使用します。
ICPアルゴリズムは2つの点群データ(地図データ、LRFで取得した最新のデータ)を平行移動、回転を繰り返すことで、対応関係にある点の距離が最短になるように位置合わせをするアルゴリズムです。
ICPアルゴリズムで作成中の地図データの点群データとLRFで取得したデータを位置合わせすることで現在の位置を計算します。


### Mapperシステムの起動(Raspberry Pi)
まずはWEBブラウザの操作でMapperシステムを起動します。

<div align="center"><a href="slam1.png"><img src="slam1.png" width="50%;"></a></div>

元の画面に戻らない場合は「Back to the top page.」を押してください。

<div align="center"><a href="slam2.png"><img src="slam2.png" width="50%;"></a></div>


### NavigationManagerの起動(PC)
次にNavigationManagerを起動します。
Navigationフォルダ内の以下のバッチファイル、シェルスクリプトを実行してください。

- NavigationManager.bat(Windows)
- NavigationManager.sh(Ubuntu)

すると以下のGUIが起動します。

<div align="center"><a href="slam48.png"><img src="slam48.png" width="50%;"></a></div>

### ポートの接続、RTCのアクティブ化

RTSystemEditorのネームサービスビューは以下の状態になっているはずです。

<div align="center"><a href="slam28.png"><img src="slam28.png" width="50%;"></a></div>

まずはWEBブラウザの操作で**Connect**ボタンを押してください。
これでRaspberry Pi上のRTCのポートは接続されます。

<div align="center"><a href="slam14.png"><img src="slam14.png" width="50%;"></a></div>

システムダイアグラム上で以下のように接続してください。

<div align="center"><a href="slam46.png"><img src="slam46.png" width="50%;"></a></div>

NavigationManagerに関わる部分以外は接続済みのため、以下のポートを接続します。

<table class="table-alt">
  <tr>
    <th>コンポーネント名</th>
    <th>ポート名</th>
    <th>コンポーネント名</th>
    <th>ポート名</th>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>mapperService</td>
    <td>Mapper_MRPT0</td>
    <td>gridMapper</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>currentPose</td>
    <td>Mapper_MRPT0</td>
    <td>estimatedPose</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>targetVelocity</td>
    <td>RaspberryPiMouseRTC0</td>
    <td>target_velocity_in</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>range</td>
    <td>RPLiderRTC0(RobotisLDSensor0)</td>
    <td>range</td>
  </tr>
</table>


接続したらRTCをアクティブ化してください。
<div align="center"><a href="slam5.png"><img src="slam5.png" width="50%;"></a></div>

### 地図作成

NavigationManagerのGUIの**Start Mapping**ボタンを押してください。

<div align="center"><a href="slam6.png"><img src="slam6.png" width="50%;"></a></div>

次にRTCをアクティブ化した時に以下のジョイスティックGUIが起動しているため、黄色い円をマウスで操作してください。
それでRaspberry Piマウスが移動します。

<div align="center"><a href="slam8.png"><img src="slam8.png" width="50%;"></a></div>

しばらく操作すると以下のように環境地図が得られます。

<div align="center"><a href="testMap.png"><img src="testMap.png" width="50%;"></a></div>

地図生成が終了したら**Stop Mapping**ボタンを押してください。

<div align="center"><a href="slam10.png"><img src="slam10.png" width="50%;"></a></div>

次に地図データを保存します。
**Save Map**ボタンを押してください。

<div align="center"><a href="slam11.png"><img src="slam11.png" width="50%;"></a></div>


ファイル名を**testMap**と設定して、Navigationフォルダに保存してください。
<br>※**開く**ボタンをクリックすると保存されます。

<div align="center"><a href="slam45.png"><img src="slam45.png" width="50%;"></a></div>

最後にWEBブラウザの操作でMapperシステムを終了させます。

<div align="center"><a href="slam13.png"><img src="slam13.png" width="50%;"></a></div>


## ナビゲーション(経路計画)システムの実行

ここからは作成した環境地図データを用いてRaspberry Piマウスの経路計画を試してみます。

### PathPlanシステムの起動(Raspberry Pi)
WEBブラウザの操作でPathPlanシステムを起動します。

<div align="center"><a href="slam15.png"><img src="slam15.png" width="50%;"></a></div>

元の画面に戻らない場合は「Back to the top page.」を押してください。




### NavigationManager、MapServerの起動(PC)
次にNavigationManagerとMapServerを起動します。
NavigationManagerが起動済みの場合はMapServerのみを起動してください。
Navigationフォルダ内の以下のバッチファイル、シェルスクリプトを実行してください。

- NavigationManager.bat(Windows)、NavigationManager.sh(Ubuntu)
- MapServer.bat(Windows)、MapServer.sh(Ubuntu)


### ポートの接続、RTCのアクティブ化

RTSystemEditorのネームサービスビューは以下の状態になっているはずです。

<div align="center"><a href="slam18.png"><img src="slam18.png" width="50%;"></a></div>

まずはWEBブラウザの操作で**Connect**ボタンを押してください。
これでRaspberry Pi上のRTCのポートは接続されます。

<div align="center"><a href="slam16.png"><img src="slam16.png" width="50%;"></a></div>

システムダイアグラム上で以下のように接続してください。

<div align="center"><a href="slam19.png"><img src="slam19.png" width="50%;"></a></div>


<table class="table-alt">
  <tr>
    <th>コンポーネント名</th>
    <th>ポート名</th>
    <th>コンポーネント名</th>
    <th>ポート名</th>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>mapServer</td>
    <td>MapServer0</td>
    <td>mapServer</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>pathPlanner</td>
    <td>PathPlanner_MRPT0</td>
    <td>pathPlanner</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>pathFollower</td>
    <td>SimplePathFollower0</td>
    <td>PathFollower</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>currentPose</td>
    <td>Localization_MRPT0</td>
    <td>estimatedPose</td>
  </tr>
  <tr>
    <td>NavigationManager0</td>
    <td>range</td>
    <td>RPLiderRTC0(RobotisLDSensor0)</td>
    <td>range</td>
  </tr>
  <tr>
    <td>MapServer0</td>
    <td>mapServer</td>
    <td>Localization_MRPT</td>
    <td>mapServer</td>
  </tr>
</table>

接続したらRTCをアクティブ化してください。

<div align="center"><a href="slam20.png"><img src="slam20.png" width="50%;"></a></div>

### 経路生成
まずはRaspberry Piマウスの目標位置、目標姿勢角を設定します。
NavigationManagerのGUIの地図上の目標位置となる場所をクリックしてください。
地図上の白い部分が障害物を検出しなかった範囲のため、白い範囲のどこかをクリックしてください。

<div align="center"><a href="slam21.png"><img src="slam21.png" width="50%;"></a></div>

以下の画面が表示されるので、目標角度を設定します。


<div align="center"><a href="slam22.png"><img src="slam22.png" width="50%;"></a></div>

適当な場所をクリックすると中心から延びる赤い線の角度が変化するので、適当な角度に設定してください。

<div align="center"><a href="path23.png"><img src="path23.png" width="50%;"></a></div>

**OK**ボタンを押すと地図上に目標位置が表示されます。

<div align="center"><a href="slam23.png"><img src="slam23.png" width="50%;"></a></div>

次に**Plan Path**ボタンを押してください。

<div align="center"><a href="slam24.png"><img src="slam24.png" width="50%;"></a></div>

これで目標位置までの目標経路が計算されました。

<div align="center"><a href="slam25.png"><img src="slam25.png" width="50%;"></a></div>

### 経路追従

**Follow**ボタンを押すと経路追従を開始します。

<div align="center"><a href="slam26.png"><img src="slam26.png" width="50%;"></a></div>

動作確認が終了したら、WEBブラウザのStopボタンからPathPlanシステムを終了してください。
<!-- [[Raspberry Piマウスの電源をオフ:/ja/node/6550#shutdown]]にしてください。 -->

<div align="center"><a href="slam27.png"><img src="slam27.png" width="50%;"></a></div>

