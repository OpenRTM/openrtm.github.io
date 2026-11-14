---
layout: page
title: "rtc開発の流れ"
---

<!-- Title: RTC開発の流れ -->
#contents

本節では、RTミドルウエア(OpenRTM-aist)を利用した、RTコンポーネントの開発方法について説明します。

## 開発の流れ

OpenRTM-aistは、コンポーネント化のためのフレームワークと、コンポーネントを管理/実行するためのミドルウエアから構成されています。

OpenRTM-aistは、コンポーネントを開発したいユーザー(コンポーネントデベロッパ)が持つ既存のソフトウエア資産、あるいは新たに作成したソフトウエアを容易にRTC化するためのフレームワークを提供します。RTC作成の大まかな流れは下図のようになります。

<div align="center"><a href="rtc_devel_flow_ja.png"><img src="rtc_devel_flow_ja.png" style="width:60%;"></a></div>
<div align="center"><strong>RTCおよびRTシステム開発の流れ</strong></div>

上述したように、RTコンポーネントが持つ共通インターフェースに関するコード、他のコンポーネントとのデータのやり取りの処理などは、RTコンポーネントフレームワークにより隠蔽されています。これらの処理は共通であるため、多くの部分はライブラリ化や自動生成が可能です。OpenRTM-aistでは RTCの雛型を生成するためのツールとしてRTCBuilderを提供しています。

RTC開発者は、自分が開発した既存のプログラムをコンポーネントフレームワークに組み込むことでRTコンポーネントを作成し、複数のRTCを組合わせてロボットシステムを構築します。既存のソフトウエア資源をソフトウエア部品であるRTコンポーネントとして作成しておけば、様々な場面での再利用が容易になります。作成されたRTCは、ネットワーク上のノードに配置し、任意の別のノードから利用することもできます。

RTCフレームワークに則って作成されたRTCは大きく分けて2種類の形態があります。スタンドアロンRTC(Standalone RT-Component)とローダブルモジュールRTC(Loadble Module RT-Component)です。スタンドアロンRTCは単一の実行形式のバイナリです。ローダブルモジュールRTCは動的にロード可能なバイナリファイルで、1プロセスで複数種類のRTCを同時起動する場合等に用いられます。

## RTCBuilderによるひな形コードの作成

RTCBuilderはRTコンポーネントの雛型コードを自動生成する開発ツールです。
このツールを用いて、RTCの基本プロファイルやデータポート、サービスポート、コンフィギュレーションに関する情報を入力することでコアロジック以外の大半のコードを自動生成することができます。対応している言語は、C++、Java、Python、Luaです。コンポーネントを作成する前に、おおよそ以下のことを決めておきます。

- プロファイル(名前、カテゴリ名、バージョン等)
- データポート(InPort/OutPort、ポート名、データ型)
- サービスポート(ポート名、サービスインターフェース)
- コンフィギュレーション(変数の名前、変数の型)

Eclipseメニューの [ファイル] > [新規] > [その他]と選択してダイアログを開き、表示されたツリーで [その他] > [RTCBuilder] 選択して [次へ] をクリックします。プロジェクト名を入力して [終了] をクリックします。下図の画面が表示され、「基本」「アクティビティ」「データポート」「サービスポート」「コンフィギュレーション」「ドキュメント生成」「言語・環境」「RTC.xml」のタブがあります。「基本」から「言語・環境」までのタブのページを順に必要に応じて項目を埋めていき、最後に、「基本」タブページにある、[コード生成] ボタンをクリックすることで、雛型コードが生成されます。生成されたコードは、Eclipse起動時に指定したワークスペース内にあるプロジェクト名のフォルダーの下に生成されます。

<div align="center"><a href="rtcbuilder_ja.png"><img src="rtcbuilder_ja.png" style="width:60%;"></a></div>
<div align="center"><strong>RTCBuilderの開発画面</strong></div>

## RTCの実装

RTコンポーネントのプログラミングでは通常のプログラミングと異なり、main関数に直接処理を実装することはありません。ここでは、例として C++版の実装について述べます。

RTコンポーネントは、ある基底クラスを継承した一つのクラスとして実装されます。 RTコンポーネントにおいてコアロジックが行う処理は、その基底クラスのメンバ関数(メソッド)をオーバーライドする形で記述します。例えば、初期化時に行う処理は、**onInitialize**関数の中に、RTCがアクティブ時に周期的に処理したい内容は**onExecute**関数に記述します。 

```
 class MyComponent
```
  : public DataflowComponentBase
```
 {
 public:
   // 初期化時に実行したい処理
   virtual ReturnCode_t onInitialize()
   {
     if (mylogic.init())
       return RTC::RTC_OK;
     return RTC::RTC_ERROR;
   }
 
   // 周期的に実行したい処理
   virtual ReturnCode_t onExecute(RTC::UniqueId ec_id)
   {
     if (mylogic.do_someting())
       return RTC::RTC_OK;
     RTC::RTC_ERROR;
   }
 
 private:
   MyLogic mylogic;
   // ポート等の宣言
   //   ：
 };
```

上記はC++での実装例です。 この例では、説明のためにクラス宣言と実装が一体で記述されていますが、実際にはヘッダファイル(.h)と実装ファイル(.cpp)に分割されてコードが生成されます。 MyLogicクラスのオブジェクトmylogicは、このコンポーネントが実際に行うコアロジックが実装されたクラスのインスタンスです。
例では、非常に簡潔にmylogicの関数を呼ぶことでRTCが実装されています、実際の実装でも、コアロジックを予めこの例のように簡単に利用可能なクラス化しておき、コールバック関数内での呼び出しは最低限にする方がよいでしょう。

RTCBuilderにより同時に生成されるMakefileやプロジェクトファイルでこのコードをコンパイル/ビルドすることで、実行ファイルや共有オブジェクト(又はDLL)が作成できます。

## RTC ライフサイクル

上述したように、RTCの実装では、予め決められた関数(コールバック関数)に処理を記述することで、コンポーネントを作成します。どのような関数があり、どういったタイミングで呼ばれるのかを知るためには、RTCの状態遷移すなわちライフサイクルを理解する必要があります。下に、RTCの状態遷移図を示します。

<div align="center"><a href="rtc_state_machine_ja.png"><img src="rtc_state_machine_ja.png" style="width:40%;"></a></div>
<div align="center"><strong>RTC ライフサイクル (UML ステートマシン図)</strong></div>

コンポーネントは基本的に以下の状態を持ちます。 

- 生成状態(Created)
- 活動状態(Alive)
  - 非アクティブ状態(Inactive)
  - アクティブ状態(Active)
  - エラー状態(Error)
- 終了状態

これらの各状態や遷移時には、決められた関数(コールバック関数)がECによって呼び出されます。 表に、コールバック関数とそれぞれが呼ばれるタイミングを示します。

<table class="table-alt">
  <tr>
    <th>関数名</th>
    <th>概要</th>
  </tr>
  <tr>
    <td>onInitialize</td>
    <td>ライフサイクル初期化時に1度だけ呼ばれる。</td>
  </tr>
  <tr>
    <td>onActivated</td>
    <td>アクティブ化する際に1回呼ばれる。</td>
  </tr>
  <tr>
    <td>onDeactivated</td>
    <td>非アクティブ化する際に1回呼ばれる。</td>
  </tr>
  <tr>
    <td>onExecute</td>
    <td>アクティブ状態にあるとき周期的に呼ばれる。</td>
  </tr>
  <tr>
    <td>onStateUpdate</td>
    <td>onExecuteの後に毎回呼ばれる。</td>
  </tr>
  <tr>
    <td>onAborting</td>
    <td>エラー状態に移行する際に1回呼ばれる。</td>
  </tr>
  <tr>
    <td>onError</td>
    <td>エラー状態にあるとき周期的に呼ばれる。</td>
  </tr>
  <tr>
    <td>onReset</td>
    <td>エラー状態から復帰する際に1回呼ばれる。</td>
  </tr>
  <tr>
    <td>onShutdown</td>
    <td>ECの駆動が停止する際に1回呼ばれる。</td>
  </tr>
  <tr>
    <td>onStartup</td>
    <td>ECの駆動が開始する際に1回呼ばれる。</td>
  </tr>
  <tr>
    <td>onFinalize</td>
    <td>ライフサイクル終了時に1度だけ呼ばれる。</td>
  </tr>
</table>



