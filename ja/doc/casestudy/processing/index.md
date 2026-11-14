---
layout: page
title: processing 活用事例
---

#contents

## Processingとは？

Processingはオープンソースのプログラミング言語で、以下の特長があることから初心者向けであるとされています。
- 視覚的な表現が他の言語と比較して簡単(グラフや図形のアニメーションやインタラクション等)
- 開発環境の導入が簡単

## 実習概要
Processingでグラフを描画するRTCを実行し、Raspberry Piマウスの移動軌跡をグラフに描画するシステムの作成します。

<br>

<div align="center"><a href="processing10.png"><img src="processing10.png" width="80%;"></a></div>
<br>

## drawGraphコンポーネントの作成

### RTCBuilderによるひな型コード生成

下記の仕様で、RTCBuilderでdrawGraphコンポーネントを作成します。

<table class="table-alt">
  <tr>
    <th>コンポーネント名称</th>
    <th>drawGraph</th>
  </tr>
  <tr>
    <td>アクティビティ</td>
    <td>onActivated、onExecute</td>
  </tr>
  <tr>
    <td>言語</td>
    <td><strong>Processing</strong></td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>in</td>
  </tr>
  <tr>
    <td>型</td>
    <td>RTC::TimedPose2D</td>
  </tr>
</table>

### RTC::TimedPose2D型について
RTC::CameraImage型は2次元平面状のを位置・姿勢を表現したデータ型です。

```
    struct Point2D
    {
        /// X coordinate in metres.
        double x;
        /// Y coordinate in metres.
        double y;
    };
 
    struct Pose2D
    {
        /// 2D position.
        Point2D position;
        /// Heading in radians.
        double heading;
    };
```

<br>

<div align="center"><a href="rtmtutorial12.png"><img src="rtmtutorial12.png" width="50%;"></a></div>
<br>


## Processing開発環境の起動
まずは、ProcessingのIDE(統合開発環境)を起動します。

Processingのリポジトリから開発環境一式をダウンロードしてください。

- [https://github.com/processing/processing/releases/tag/processing-0270-3.5.4)](https://github.com/processing/processing/releases/tag/processing-0270-3.5.4)

展開したフォルダの**processing.exe**を実行してください。

Javaのバージョンの問題により、OpenRTM-aistをProcessing 4.0以降の環境では現在のところ実行はできません。

講習会などでUSBメモリの資料を配布している場合は、以下のファイルを実行してください。

- Windowsの場合は**Processing\processing-3.5.4-windows64\processing.exe**
- Ubuntuの場合は**Processing/processing-3.5.4-linux64/processing**



実行すると、以下の統合開発環境のGUIが起動します。

<br>

<div align="center"><a href="processing3.png"><img src="processing3.png" width="60%;"></a></div>
<br>


## OpenRTM-aist Processing用ライブラリのインストール
ProcessingでOpenRTM-aistの機能が使えるようにライブラリをインストールします。

まず、Processingでスケッチブックの場所を確認します。
「ファイル」->「設定」を選択して表示される画面で確認できます。

<br>

<div align="center"><a href="processing4.png"><img src="processing4.png" width="60%;"></a></div>
<br>

スケッチブックの場所をエクスプローラーで開いてください。

スケッチブックの場所の**libraries**フォルダに、以下のOpenRTMUtil.zipを展開したフォルダをコピーします。

- [OpenRTMUtil.zip](https://github.com/Nobu19800/OpenRTMProcessing/releases/download/robomech2024/OpenRTMUtil.zip)

※講習会などではUSBメモリ内のProcessing\OpenRTMUtilフォルダを使用します。

コピーすると、以下のようなディレクトリ構成になります。

```
 スケッチブックの場所
    ├ examples
    ├ modes
    ├ templates
    ├ tools
    └ libraries
         └ OpenRTMUtil
                └  library
                     ├ commons-cli-1.1.jar
                     ├ jna-4.2.2.jar
                     ├ jna-platform-4.2.2.jar
                     ├ LogicalTimeTriggeredEC.jar
                     ├ NameserviceFile.jar
                     ├ OpenRTM-aist-2.1.0.jar
                     ├ OpenRTMUtil.jar
                     ├ rtcd.jar
                     └ rtcprof.jar
```


## graficaのインストール

グラフ描画用ライブラリのgraficaをインストールします。

Processingで「スケッチ」→「ライブラリをインポート」→「ライブラリを追加」をクリックしてください。

<br>

<div align="center"><a href="processing5.png"><img src="processing5.png" width="60%;"></a></div>
<br>

Contribution Managerでgraficaを検索してインストールしてください。

<br>

<div align="center"><a href="processing1.png"><img src="processing1.png" width="60%;"></a></div>
<br>

## プログラミング
ProcessingでRTCのプログラミングを行います。

RTCBuilderで生成したソースコードの、**drawGraphMain.pde**をProcessingで開いてください。
drawGraphMain.pdeをprocessing.exeにドラッグアンドドロップすれば開けます。

Processingのエディタから、**drawGraphMain.pde**のsetup関数に画面サイズ、フレームレートの設定処理を追加します。

```
 public void setup() {
   //ウィンドウサイズを設定
   size(300, 300); //追加
   frameRate(10); //追加
```

次に、**drawGraphImpl.pde**を編集します。
下記のようにgrafinaライブラリのインポート文を追加してください。

```
 import RTC.ReturnCode_t;
 
 import grafica.*; //追加
```

次に、下記の変数dataを宣言します。変数dataに受信した位置姿勢データが格納されます。

```
    protected InPort<TimedPose2D> m_inIn;
    
    //グラフに描画する点のデータを格納する配列を宣言
    GPointsArray data; //追加
```

onActivated関数を下記のように編集します。

```
    @Override
    protected ReturnCode_t onActivated(int ec_id) {
        //配列dataの初期化
        data = new GPointsArray();
        return super.onActivated(ec_id);
    }
```

最後にonExecute関数を下記のように編集します。

```
    @Override
    protected ReturnCode_t onExecute(int ec_id) {
        //InPortでデータを受信した時の処理
        if (m_inIn.isNew())
        {
          //受信データの読み込み
          m_inIn.read();
          //配列dataに取得した位置を追加する
          data.add((float)m_in.v.data.position.x, 
                   (float)m_in.v.data.position.y);
      
          //配列の大きさが1000を超えた場合、古いデータは捨てる
          if (data.getNPoints() > 1000)
          {
            data.remove(0);
          }
        }
        //グラフをウィンドウの(0,0)から(300,300)の範囲に描画する
        GPlot plot = new GPlot(m_applet, 0, 0, 300, 300);
        //グラフの縦軸、横軸の上限、下限を設定する
        plot.setXLim(-1.0, 1.0);
        plot.setYLim(-1.0, 1.0);
        plot.setFixedXLim(true);
        plot.setFixedYLim(true);
        //配列dataをグラフに設定する
        plot.addPoints(data);
        //グラフの描画を開始する
        plot.beginDraw();
        //グラフに外枠、座標、折れ線、縦軸、横軸を描画する
        plot.drawBox();
        plot.drawPoints();
        plot.drawLines();
        plot.drawXAxis();
        plot.drawYAxis();
        //グラフの描画を終了する
        plot.endDraw();
        return super.onExecute(ec_id);
    }
```


## RTシステムの構築、動作確認
作成したdrawGraphコンポーネントの動作確認を行います。

Raspberry Piマウスシミュレータ(**RaspberryPiSimulator**)、もしくはRaspberry Piマウス実機(**RaspberryPiMouseRTC**)のRTCを使用します。
また、以下のチュートリアルで作成した**RobotController**も使用します。

- [チュートリアル(RTコンポーネントの作成入門、Raspberry Pi Mouse、Windows)]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_win_part2)

Processingで作成した**drawGraph**コンポーネントを起動します。
Processingの実行ボタンを押してください。

<br>

<div align="center"><a href="rtmtutorial13.png"><img src="rtmtutorial13.png" width="50%;"></a></div>
<br>

RTシステムエディタで以下のようにポートを接続してください。

<br>

<div align="center"><a href="processing7.png"><img src="processing7.png" width="60%;"></a></div>
<br>

RTCをアクティブ化して、RobotControllerのコンフィギュレーションパラメータをスライダで操作するとRaspberry Piマウスが移動して、移動の軌跡がグラフに描画されます。


## OpenRTM-aist 2.0以前の手順

OpenRTM-aist 2.0以前にはProcessingのコード生成機能がないため、下記のOpenRTMUtilライブラリを使ったソースコードが必要です。

Processingの開発環境で以下のコードを入力してください。
Processingでは実行開始時に1度だけ呼ばれる**setup**関数、一定間隔で呼ばれる**draw**関数を使用します。
setup関数でRTCの生成を実行しています。
draw関数でInPortのデータの読み込みとグラフの描画更新処理を実行しています。

```
 import grafica.*;
 import jp.go.aist.rtm.OpenRTMUtil;
 import jp.go.aist.rtm.RTC.port.InPort;
 import jp.go.aist.rtm.RTC.util.DataRef;
 import RTC.TimedPose2D;
 import RTC.Pose2D;
 import RTC.Point2D;
 import RTC.Time;
 
 //データ、InPortの変数を宣言
 DataRef<TimedPose2D> indata;
 InPort<TimedPose2D> inport;
 
 //グラフに描画する点のデータを格納する配列を宣言
 GPointsArray data;
 
 public void setup() {
  //ウィンドウサイズを設定
  size(300, 300);
 
  //RTCを"drawGraph"というインスタンス名で生成
  OpenRTMUtil util = new OpenRTMUtil();
  util.createComponent("drawGraph");
  //データの初期化
  TimedPose2D val = new TimedPose2D();
  val.tm = new Time();
  val.data = new Pose2D();
  val.data.position = new Point2D();
  indata = new DataRef<TimedPose2D>(val);
  //InPortを"pose"という名前で生成
  inport = util.addInPort("pose", indata);
 
  //配列dataの初期化
  data = new GPointsArray();
 }
 
 int count = 0;
 public void draw() {
 
  //InPortでデータを受信した時の処理
  if (inport.isNew())
  {
    //受信データの読み込み
    inport.read();
    //配列dataに取得した位置を追加する
    data.add((float)indata.v.data.position.x, (float)indata.v.data.position.y);
 
    //配列の大きさが1000を超えた場合、古いデータは捨てる
    if (data.getNPoints() > 1000)
    {
      data.remove(0);
    }
  }
  //グラフをウィンドウの(0,0)から(300,300)の範囲に描画する
  GPlot plot = new GPlot(this, 0, 0, 300, 300);
  //グラフの縦軸、横軸の上限、下限を設定する
  plot.setXLim(-1.0, 1.0);
  plot.setYLim(-1.0, 1.0);
  plot.setFixedXLim(true);
  plot.setFixedYLim(true);
  //配列dataをグラフに設定する
  plot.addPoints(data);
  //グラフの描画を開始する
  plot.beginDraw();
  //グラフに外枠、座標、折れ線、縦軸、横軸を描画する
  plot.drawBox();
  plot.drawPoints();
  plot.drawLines();
  plot.drawXAxis();
  plot.drawYAxis();
  //グラフの描画を終了する
  plot.endDraw();
 }
```
