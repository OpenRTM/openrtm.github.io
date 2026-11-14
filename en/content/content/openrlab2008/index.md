---
layout: page
title: 産総研オープンラボ2008
---

No English version available.

#contents


## 開催概要 
- 会期：2008年10月20,21日
  - 20日（月）　 　　13：00～17：00
  - 21日（火） 　　　10：00～16：30
- 場所：
  - 独立行政法人 産業技術総合研究所 つくばセンター
- 対象：
  - 産業界、大学、公的研究機関等の皆様
- 主な当部門の展示：
  - 生活支援ヒューマノイドロボット，RTミドルウェア，ロボットのためのユニバーサルデザイン，高機能３次元視覚システム，トイレアシスト等19件．
- 技術講演会：
  - 「次世代ロボット産業化基盤技術」（21日14：30～16：30）
  - 「産業変革研究イニシアティブ　－死の谷の克服と産業化シナリオ－」（21日12：30～16：30）など
- 参加費：
  - 無料
- 事前登録：
  - **ホームページ（[http](//www.aist-openlab.jp/index.html::http://www.aist-openlab.jp/index.html)）からの事前来場登録（来場申し込み）とラボ事前予約（講演会含む）が必要となります。**なお、技術講演会は会場確保の都合がありますので、お早めに事前登録をして
くださるようお願いいたします。
- 交通機関：
  - つくばエクスプレス「つくば駅」（秋葉原から快速45分）より無料バスを運行予定
- 公式Webページ
  - [http](//www.aist-openlab.jp/index.html:http://www.aist-openlab.jp/index.html)

# 展示内容 
RTミドルウエア関連の展示は以下のとおりです。
- I-35:作業技能
- I-42:RTミドルウエア(OpenRTM-aist)
- I-44:RTミドルウエア技術
- I-45:解体作業支援ＲＴシステム

## I-42:RTミドルウエア(OpenRTM-aist) 
### RTミドルウエア：OpenRTM-aist 
**出展者**

[産総研・知能システム研究部門・安藤慶昭](http://unit.aist.go.jp/is/)

**概要**

RTミドルウエア（OpenRTM-aist）はロボットシステムを容易に構築するためのソフトウエアプラットフォームです。ロボットの機能要素（センサ、アクチュエータ、アルゴリズム等）を、RTコンポーネントと呼ばれる単位でモジュール化し、その組み合わせでシステムを構成します。ミドルウエアには、モジュール化とその再利用を容易にするための機能が備わっており、ロボットシステムの開発期間の短縮、コストの削減に貢献します。
RTコンポーネントは、言語（C++、Java、Python）、OS（UNIX、Windows、MacOS X等）を問わず作成・動作が可能で、異言語・OS上のRTコンポーネント同士をネットワーク経由で容易に連携させることができます。RTミドルウエア（OpenRTM-aist）のインターフェース仕様は、産総研が中心となって策定されたOMG（Object Management Group）の国際標準：RTC (Robotic Technology Component)仕様に準拠しています。OpenRTM-aistは今年のロボット大賞2007 ソフトウエア・部品部門優秀賞受賞ソフトウエアです。

**特徴**

- ロボットをモジュール単位で容易に構築するソフトウエアプラットフォーム
- モジュール化と再利用によって開発期間の短縮、コスト削減が可能
- ロボット特有なソフトウエア機能、異言語・異OS間で連携する機能を提供

### OpenRTM-aistツール(RTCBuilder・RTSystemEditor) 

**出展者**

[産総研・知能システム研究部門・安藤慶昭**: http](//unit.aist.go.jp/is/)

**概要**

現在、NEDO「次世代ロボット知能化技術開発プロジェクト(通称：知能化プロジェクト)」(2007-2011)において、ロボットシステム開発のための統合開発プラットフォーム **OpenRT Platform** が開発されています。このソフトウエアプラットフォームは、OpenRTMをベースとし、多くのツール群(ツールチェーン)によりロボットの開発効率の向上を目指しています。
旧OpenRTMツール(RtcTemplate・RtcLink)も、OpenRT Platform ツールチェーンに取り込まれ、様々な機能追加・改良を行った RTCBuilder・RTCSystemEditor として新たにリリースされました。
本展示では、新しいツールの新機能・改良点などをご紹介します。

**特徴**

- **RTCBuilder**
  - わかりやすいGUIで、コンポーネントの設計をより簡単に
  - C++、Java、Python、C#のひな型コードを自動生成
- **RTSystemEditor**
  - RTコンポーネントシステムを簡単に設計・操作可能
  - 新機能・オフラインエディタ

<br>

<div align="center"><a href="RTCBuilder.jpg"><img src="RTCBuilder.jpg" width="60%;"></a></div>
<div align="center"><strong>RTCBuilder</strong></div>
<br>

### 組込みCPU向けRTコンポーネント(実演) 
**出展者**

[産総研・知能システム研究部門・安藤慶昭](http://unit.aist.go.jp/is/)

**概要**

組込みLinux向けのRTコンポーネント開発環境と、RTコンポーネントを搭載した組込みデバイスの実例([アットマークテクノ社製](http://www.atmark-techno.com/) [Armadillo](http://armadillo.atmark-techno.com/)シリーズ)をご紹介します。

**特徴**

- 組込みLinux用RTコンポーネントクロス開発環境
- [アットマークテクノ社製](http://www.atmark-techno.com/) [Armadillo](http://armadillo.atmark-techno.com/)シリーズ用RTコンポーネントを簡単に開発
- USBメモリにインストールされたRTコンポーネントを自動起動
- 実例としてArmadilloとURGセンサを組み合わせた分散LRFユニットを展示

<br>

<div align="center"><a href="Armadillo_URG.png"><img src="Armadillo_URG.png" width="60%;"></a></div>
<br>

<div align="center"><a href="Armadillo_URG3.png"><img src="Armadillo_URG3.png" width="60%;"></a></div>
<div align="center"><strong>PoE (Power over Ether) により給電可能</strong></div>
<br>
## I-44:RTミドルウエア技術

- [RTミドルウエア技術カタログ（産総研オープンラボ2008版）]()(no_link) を配布しております。

### 人検知・追跡多目的ロボット(実演) 

**出展者**

[株式会社セック**: http](//www.sec.co.jp)

**概要**

レーザレンジファインダで人を検知・追跡し、カメラで人を撮影するロボットシステムです。 国際標準仕様のロボット部品化技術であるRTミドルウェアを採用することで、高い拡張性と保守性を実現しています。 オフィスの受付ロボットや博物館での来場者数・動線計測ロボット、倉庫での監視ロボットなどに応用することができます。

<br>

<div align="center"><a href="TrackingSystem.png"><img src="TrackingSystem.png" width="60%;"></a></div>
<div align="center"><strong>人検知・追跡多目的ロボット</strong></div>
<br>
### PatterWeaver for RT-Middleware(実演)

**出展者**

[株式会社テクノロジックアート**: http](//www.tech-arts.co.jp/)

**概要**

UMLモデリングツールをベースとしたRTコンポーネントの設計ツールです．

**主な特徴**
- GUIを用いた直感的な操作によるコンポーネント設計が可能
- C++版RTC・Java版RTC・Python版RTCのスケルトンコードの自動生成
- CORBA IDLの自動生成
- 設計情報の再利用をサポート

<br>

<div align="center"><a href="pw_for_rtm.png"><img src="pw_for_rtm.png" width="60%;"></a></div>
<div align="center"><strong>PatterWeaver for RT-Middleware</strong></div>
<br>

### 分散レーザレンジファインダのキャリブレーション支援コンポーネント群(実演)

** RT ミドルウエアコンテスト 2007 最優秀賞受賞作品**

** 出展者 **

[東京大学橋本研究室・佐々木毅氏](http://dfs.iis.u-tokyo.ac.jp/ja/)

**概要**

空間に分散配置されたレーザレンジファインダ（LRF）の位置・姿勢のキャリブレーシ ョンを支援するコンポーネント群を紹介します。この手法では、LRFから得られる物体 のセンサ座標系での位置とその物体の基準座標系での位置の対応からキャリブレーシ ョンを行います。また、キャリブレーション処理だけでなく、LRF、移動物体トラッキ ングといった各機能要素に関してもコンポーネント化を行っています。

<br>

<div align="center"><a href="calibration_concept.png"><img src="calibration_concept.png" width="60%;"></a></div>
<div align="center"><strong>LRFキャリブレーション</strong></div>
<br>

<br>

<div align="center"><a href="calibration_result.png"><img src="calibration_result.png" width="60%;"></a></div>
<div align="center"><strong>人間のトラッキング</strong></div>
<br>

### OpenCV を使った画像処理コンポーネント(実演)

**RTミドルウエアコンテスト2007 知能モジュール賞受賞作品**

**出展者**

[大阪大学新井研究室・田窪朋仁先生](http://www-arailab.sys.es.osaka-u.ac.jp/)

**概要**

USBカメラで取り込んだ画像をOpenCVで提供されているライブラリで処理し出力するためのコンポーネント群を開発しました．コンポーネント間のデータのやりとりは画像のみに限定し，複数コンポーネントの処理を重ねることで様々な画像処理結果を得ることができます．画像処理における各種パラメータはRTCLinkのConfigurationViewから調整可能にすることで高機能画像処理ライブラリの機能を容易に試用することができます．

**特徴**

- 広く利用されている画像処理ライブラリOpenCVをRTMコンポーネントにすることで作成例を学ぶ．
- 複数の実用性のある画像処理を簡単に連結できる．
- 主要な処理パラメータをRTCLinkから調整できるようにすることでライブラリの試用ができる．
- VMWareイメージにより仮想環境を配布．すぐに試せる．


<br>

<div align="center"><a href="opencv.png"><img src="opencv.png" width="60%;"></a></div>
<div align="center"><strong>OpenCV を使った画像処理コンポーネント</strong></div>
<br>

### CLUE リーダコンポーネント(実演) 

**出展者**

[大阪大学新井研究室・大原賢一先生](http://www-arailab.sys.es.osaka-u.ac.jp/)

**概要**

デンソーウェーブ社製に次元バーコードリーダQD25にQRコードの座標出力機能を装備したものを用いて，QRコードに保存された情報と，マークの位置情報の双方の情報を獲得することを可能にするコンポーネント群

**特徴**

- QRコードリーダコンポーネントとしても利用できる．
- QRコードの4角の情報を用いることで，ビジュアルサーボなどの用途に利用可能
- 上述のQRコードの座標出力機能を装備したQD25はデンソーウェーブ様より標準実装された状態で購入可能

<br>

<div align="center"><a href="clue_reader.png"><img src="clue_reader.png" width="60%;"></a></div>
<div align="center"><strong>CLUE リーダコンポーネントとその応用例</strong></div>
<br>

### β-RNAによる学習推論コンポーネント(実演) 
**出展者**

[株式会社アドイン研究所](http://www.adin.co.jp/)

**概要**

β-RNAは、株式会社アドイン研究所が開発・販売する「ファジィニューロ学習・推論エンジン」です。従来の学習系とは違い、ファイジィ理論とニューラルネットワークの利点を合わせ持つ、新しい学習・推論エンジンです。手本となるデータを学習させるだけで、自分でルールを生成し、学習したルールに基づいて作業を実行します。β-RNAは

- 画像による不良品判別システム
- 基盤検査システム
- トンネル掘削機方向・姿勢制御システム
- 建設ロボット制御システム
- 飼料調合支援システム
- 装置系の故障・故障予兆検知

など、信号処理、制御等、様々な分野に適用されています。

**特徴**

- 学習コンポーネントに、サンプルデータを教示だけでルールを自動的に生成します
- 未知のデータを入力すると、学習したルールを用いて、データのカテゴリを出力します。
- 分類ルールをプログラム記述するのが難しいデータでもカテゴリ分類を行うことができます。

<br>

<div align="center"><a href="learning.gif"><img src="learning.gif" width="60%;"></a></div>
<div align="center"><strong>学習・推論コンポーネントに、りんごとみかんのサンプルデータを入力して、教示を行う</strong></div>
<br>

<br>

<div align="center"><a href="reasoning.gif"><img src="reasoning.gif" width="60%;"></a></div>
<div align="center"><strong>学習・推論コンポーネントに、未知のデータを入力して、推論させる</strong></div>
<br>
### DAQミドルウエア(パネル展示)

**出展者**

[高エネルギー加速器研究機構](http://www.kek.jp)

**概要**

OpenRTM-aistを基盤とした粒子線物理実験用データ収集(DAQ: Data Acquisition System)のためのミドルウエアです。
粒子線物理実験用データ収集(DAQ)システムはニュートリノ振動実験やB中間子の崩壊（BELLE）実験などに必須の装置ですが、誰にでも簡単に再利用可能なものにはなっていません。DAQミドルウエアはこの問題に対する解答を求めて研究開発されています。DAQミドルウエアは[大強度陽子加速器施設J-PARC( Japan Proton Accelerator Research Complex )](http://j-parc.jp/index.html)において、データ収集ミドルウエアとして使用が予定されています。
<br>

<div align="center"><a href="jpark.png"><img src="jpark.png" width="60%;"></a></div>
<div align="center"><strong>DAQミドルウエアが使われる予定のJ-PARC 装置群</strong></div>
<br>


### RTC-CANopen 
**出展者**

[芝浦工業大学水川研究室](http://www.hri.ee.shibaura-it.ac.jp/)

**概要**

RTC-CANopenとは、安全バスシステムとして最も使用されているCANopenの特徴を取り入れた組込み向けのRT-Middlewareです。RTC-CANopenは、ネイティブバスであるCANを介して接続される各種デバイスと汎用PC上のEthernetで接続されるデバイスやアルゴリズムと相互に接続することが可能となっている他、PnP機能をサポートしており柔軟なロボットシステムの構築が可能となっております。

**特徴**

- CANopenを使用した安全バスシステム
- PnP機能をサポート
- 組込み向けRT-Middleware
- 既存のCANopen製品が使用可能
- ソフトウェア・ハードウェアの再利用性向上
- データのリアルタイム性

<br>

<div align="center"><a href="RTC-CANopen.png"><img src="RTC-CANopen.png" width="60%;"></a></div>
<div align="center"><strong>RTC-CANopen System</strong></div>
<br>


### マルチCPU分散制御ロボットへのRTミドルウェアの適用

**出展者**

[芝浦工業大学水川研究室](http://www.hri.ee.shibaura-it.ac.jp/)

**概要**

ベクター・ジャパン社製のCANインターフェイスを用いたCAN Controller ComponentとGPSによるナビゲーションを行うNavi Componentを屋外自律移動ロボットへ適用しました．Navi Componentにより，屋外ナビゲーションの容易な適用が可能となります．また，CAN Controller ComponentによりCAN通信を意識せず分散制御ロボットやシステムを開発することが可能となります．

**特徴**

- マップデータによる経路設定
- 再利用性を重視したシステム構成
- ベクター・ジャパン社製XLファミリー製品を使用
- 受信メッセージのフィルタ機能を実装

<br>

<div align="center"><a href="PAR-NE07.png"><img src="PAR-NE07.png" width="60%;"></a></div>
<div align="center"><strong>PAR-NE07</strong></div>
<br>

### 複数CPU間のための共有メモリコンポーネントと接続ツール群 

**出展者**

[中央大学國井研究室](http://www.hmsl.elect.chuo-u.ac.jp/)

**概要**

- OpenRTMにて複数のCPU間の共有メモリを提供する枠組みを実現
- コンポーネント間で簡単に共有メモリを利用可能に

**特徴**

- 複数CPU間で共有メモリを仮想的に使用し高速な通信を実現
- 同期機能によりデータの送信と受信を同時に行うことができる
- クライアントはサイズと特定の文字列のみ送るため負荷が少ない
<br>

<div align="center"><a href="shared_mem.png"><img src="shared_mem.png" width="60%;"></a></div>
<div align="center"><strong>共有メモリコンポーネント</strong></div>
<br>

### RTミドルウエアを用いた遠隔自律システムの構築
**出展者**

[中央大学國井研究室](http://www.hmsl.elect.chuo-u.ac.jp/)

**概要**

- 惑星探査ローバの遠隔・自律システムをRTミドルウエアで構築
- 分散システムとすることで下位CPUの負荷を低減

**特徴**

- 惑星探査ローバシステムを分散システムとして構築
- 上位層（決定層）：Host Agent、Rover Agentを高性能CPUにて実行
- 下位層（実行層）：アクチュエータ、センサ等は組込みCPUにて実行
<br>

<div align="center"><a href="rover_system.png"><img src="rover_system.png" width="60%;"></a></div>
<div align="center"><strong>惑星探査ローバシステム</strong></div>
<br>

<div align="center"><a href="rover_op.png"><img src="rover_op.png" width="60%;"></a></div>
<div align="center"><strong>惑星探査ローバ遠隔自律システムによるオペレーション</strong></div>
<br>
