---
layout: page
title: "データポート (基礎編)"
toc: true
toc_levels: "h2,h3"
#toc: false
---
<!-- Title: データポート (基礎編) -->
<!-- -*- pukiwiki-edit -*- -->
<!-- *データポート(基本編) -->
<!-- #contents -->


## データポートとは

データポートは主に連続的なデータを RTC 間でやりとるするためのポートです。
データを他の RTC へ送信するためのデータポートを OutPort、他の RTC からデータを受信するためのデータポートを InPort と呼びます。「InPort」、「OutPort」をまとめて「データポート (DataPort)」と呼ぶことがあります。


<div align="center"><a href="dataport_ja.png"><img src="dataport_ja.png" width="60%;"></a></div>
<div align="center"><strong>データポート (InPort と OutPort)</strong></div>


RTC はいろいろなプログラミング言語で記述することができます。また、RTコンポーネントはネットワーク上に分散させることも、同じノード上に配置することも、あるいは同じプロセス上に置くこともできます。
そして、両端の RTC がどんな言語で記述されているか、ネットワーク的に分散しているかに関わらず、データポート間のデータの受け渡しは透過的に行われます。

RTC は必要に応じて任意の数のデータポートを持たせることができます。例えば、センサーからデータを取得するコンポーネントを作るとします。
このコンポーネントは少なくとも一つのセンサーデータを出力するための OutPort が必要になるでしょう。

あるいは、指定されたトルク値に従って、モーターを駆動するコンポーネントを作成するとします。このコンポーネントは、少なくとも一つの一つのトルク値指令を受け取る InPort が必要になります。
これらのコンポーネントを利用して、フィードバック制御を行うための制御器 (コントローラ) コンポーネントを作成するとすれば、センサーデータを受け取る InPort、指令値 (例えば速度指令) を受け取る InPort、トルク値を出力する OutPort のそれぞれが必要になります。


<div align="center"><a href="dataport_example_ja.png"><img src="dataport_example_ja.png" width="40%;"></a></div>
<div align="center"><strong>センサー、コントローラー、モーターとデータポートの例</strong></div>


プログラムとして実際に InPort と OutPort を利用する簡単な例を見てみます。各オブジェクトはそれぞれ以下の働きをします。

- encoderDevice: ハードウエア (例えばカウンタボード等) を制御してエンコーダから現在の角度を読み取るための機能が実装されたオブジェクト。ハードウエアベンダがそうしたライブラリ等を提供していなければ、自分で実装する必要がある。
- encoderData: OutPort 用にエンコーダのデータを保持する変数。ここでは、エンコーダの値をを保持する data というフィールド (構造体のメンバ) を持っているものとする。
- encoderDataOut: OutPort オブジェクト。encoderData オブジェクトに関連付けられている。


```
 // エンコーダコンポーネントの例
 encoderData.data = encoderDevice.read(); // カウンタから現在値を取得
 encoderDataOut.write();                  // OutPort からデータが出ていく
```


1行目では、encoderDevice オブジェクトの read() 関数を呼んで、エンコーダの現在値を読み込んでいます。読み込まれたデータは、encoderData オブジェクトの data メンバーに代入されます。
OutPort のインスタンスである encoderDataOut オブジェクトは、write() が呼ばれると、encoderData オブジェクトからデータを取り出し、接続されている InPort へデータを出力します。

一方、InPort を持つモーターコンポーネントは、以下のように書けます。

- motorDevice: ハードウエア(例えばモータードライバに接続されたDAボード等)を制御してモーター制御をするためのオブジェクト。ベンダからそうしたライブラリが提供されていなければ、自分で実装する必要がある。
- motorData: InPort から入力された値を保持する変数。ここでは、エンコーダの値をを保持する data というフィールド(構造体のメンバ)を持っているものとする。
- motorDataIn: InPort オブジェクト。motorData オブジェクトに関連付けられている。


```
 // モーターコンポーネントの例
 if (motorDataIn.isNew() {
   motorData.data = motorDataIn.read(); // InPort からデータを読む
   motorDevice.output(motorData.data);  // モータードライバへ指令値を出力
 }
```


1行目ではまず InPort にデータが来ているかどうか確かめています。データが到着していれば、motorDataIn の read() 関数を呼んで、InPort からデータを motorData の data メンバーに読み込んでいます。次に、実際にモーターに指令値を渡すため、motorDevice オブジェクトの output関数を呼び出しています。
同様に、InPort と OutPort を持つ制御器コンポーネントでは以下のようになるでしょう。


```
 // 制御器コンポーネントの例
 if (positionDataIn.isNew() && referenceDataIn.isNew()) {
 
   positionDataIn.read();  // 位置データを InPort から読み込む
   referenceDataIn.read(); // 速度指令を InPort から読み込む
 
   // 制御アルゴリズムに従ってモーターに与えるトルク値を計算
   torqueData.data = controller.calculate(positionData.data,
                                           referenceaData.data);
   torqueDataOut.write(); // モータートルク値を OutPort から出力
 }
```

行っていることは、それぞれ InPort、OutPort だけの場合とそれほど変わりませんので、詳しい説明は省略します。相手の RTC がどの言語で書かれているか、あるいは、ネットワーク上の別のノード上にあるのかローカルにあるのか等の違いについては、RTコンポーネントフレームワークにより隠蔽されているので、このように簡単にデータの送受信を行うことができます。


<!-- ------------------------------------------------------------ -->
## 変数の型

ここまでの例では、各オブジェクトの宣言が示されていないので、C++ や Java等、型のある言語に慣れている方は、サンプルプログラムの各変数がどのような型なのか気になったかもしれません。

### 基本型
上の例のデータ格納変数で想定していたのは、TimedDouble というデータ型
です。C/C++ の構造体で書くと、ほぼ以下のような構造体と同等のものです。

```
 struct Time
 {
   long int sec;
   long int usec;
 };
 
 struct TimedDouble
 {
   Time tm;
   double data;
 };
```

データポートの型に関しては、以下のような決まりや特徴があります。

- データポートにはそれぞれ特有の型がある。
- 型の定義は IDL (Interface Definition Language)という言語非依存のインターフェース定義言語によって定められている。
- 言語が異なっても、IDL 定義の型が同じなら接続できる。
- 型の異なるデータポート同士は接続できず、データの送受信は行えない。

従って、上記の例で、エンコーダ、制御器、モーターの各コンポーネントを接続するためには、ポートのデータ型がそれぞれ TimedDouble 型でなければなりません。


なお、OpenRTM-aist では、デフォルトで以下のようなデータポート型を用意しており、特に定義することなく利用することができます。これらのデフォルト定義の基本型にはタイムスタンプ保持用に tm フィールドが用意されています。

<table class="table-alt">
  <tr>
    <th>型名</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>TimedShort</td>
    <td>タイムスタンプと short int 型</td>
  </tr>
  <tr>
    <td>TimedUShort</td>
    <td>タイムスタンプと unsigned short int 型</td>
  </tr>
  <tr>
    <td>TimedLong</td>
    <td>タイムスタンプと long int 型</td>
  </tr>
  <tr>
    <td>TimedULong</td>
    <td>タイムスタンプと unsigned long int 型</td>
  </tr>
  <tr>
    <td>TimedFloat</td>
    <td>タイムスタンプと float 型</td>
  </tr>
  <tr>
    <td>TimedDouble</td>
    <td>タイムスタンプと double 型</td>
  </tr>
  <tr>
    <td>TimedString</td>
    <td>タイムスタンプと string 型</td>
  </tr>
  <tr>
    <td>TimedWString</td>
    <td>タイムスタンプと wstring 型</td>
  </tr>
  <tr>
    <td>TimedChar</td>
    <td>タイムスタンプと char 型</td>
  </tr>
  <tr>
    <td>TimedWChar</td>
    <td>タイムスタンプと wchar 型</td>
  </tr>
  <tr>
    <td>TimedOctet</td>
    <td>タイムスタンプと バイト 型</td>
  </tr>
  <tr>
    <td>TimedBool</td>
    <td>タイムスタンプと bool 型</td>
  </tr>
</table>


これらのうち、TimedChar、TimedWChar、TimedOctet はあまり使用する場面はないかもしれません。

IDL型から各言語固有の方への対応関係をマッピングといいます。それぞれの型から各言語上の型へのマッピングは CORBA の言語マッピング仕様書または「言語マッピング」の章を参照してください。


### 少し複雑なデータ型

上記の基本型には、～Seq というシーケンス型と呼ばれる型が用意されています。
これは簡単にいえば配列を保持できる型です。

```
 seqdata.length(10); // 配列を10個分確保する
 for (int i(0); i < seqdata.length(); ++i) // 引数なし length は長さを返す
 {
   seqdata[i] = i; // 代入する
 }
```

C++ではこのように利用することができます。配列よりは便利で、STL の vector に似ていますが、vector よりはだいぶ低機能です。
Java では配列専用のホルダークラスが自動的に生成されこれを利用することができます。
また、Python では Python の配列に直接マッピングされます。

先ほどの例では、エンコーダーとモーターは一つでしたが、実際のロボットでは多くの自由度を扱う必要があります。
その時に、各自由度ごとにポートを設けるのは、通信効率、同期の問題などから得策ではありません。
そのような場合では、こうしたシーケンス型を利用することで、複数のデータを効率的に扱うことができます。

### 独自のデータ型

さらに、もっと複雑なデータ構造を扱いたい場合もあります。その場合は、自分でデータ型を定義して、データポートで利用することもできます。詳細は「データポート(応用編)」を参照してください。

<!-- ------------------------------------------------------------ -->
## データポートの接続

### コネクタ

RTC が持つ InPort と OutPort を接続するには、RTSystemEditor や rtcshell などのツールを使用します。ポートを接続すると OutPort から送信されたデータは、ネットワーク等を経由して InPort によって受信されます。
接続は、システムの構造やコンポーネントの特性に応じて、以下のようにいくつかの種類を選択することができます。

- データフロー型
- インターフェース型
- サブスクリプション型
- データ送信ポリシー

### インターフェース型

インターフェース型では、データをどのプロトコルで送受信するかを指定します。デフォルトでは、corba_cdr型という方法のみ利用できるようになっており、通常はこれを利用すれば特に問題ありません。
ただし、システムの構成によっては、別のインターフェース型を利用するように、拡張することも可能です。


<div align="center"><a href="dataport_interfacetype_ja.png"><img src="dataport_interfacetype_ja.png" width="50%;"></a></div>
<div align="center"><strong>インターフェース型</strong></div>

### データフロー型

データの送受信の方法には、OutPort が InPort にデータを送る push 型のものと、逆に InPort から OutPort に問い合わせてデータを取ってくる pull 型のものがあります。

push 型では、OutPort側のコンポーネントの主にアクティビティ (通常はon_execute() コールバック関数) が主体となりデータを受信側に送ります。送るタイミングは次のサブスクリプション型で指定します。
一方、pull 型では、InPort側のコンポーネントの主にアクティビティ (通常は on_execute() コールバック関数) が主体となりデータを受信側に送ります。
データを受信するタイミングは、InPort側が read() を読んだ時点となります。

<div align="center"><a href="dataport_dataflowtype_ja.png"><img src="dataport_dataflowtype_ja.png" width="50%;"></a></div>
<div align="center"><strong>データフロー型</strong></div>

### サブスクリプション型

サブスクリプション型は、データフロー型が push のときにだけ有効なプロパティです。デフォルトでは、同期型送信方式の flush, および非同期型送信方式の new, periodic の3種類が提供されています。

flush 型は OutPort から InPort へデータを push するとき、OutPort の write 関数内で直接データの送信を行います。つまり、write() 関数から戻った時には、InPort にデータが届いていることが保証されます。
一方で、相手先の InPort がネットワーク的に遠い場所にあり、通信に時間がかかる場合には、write() で長い時間待たされる可能性があります。したがって、例えばアクティビティのロジックをリアルタイム実行したい場合には flush 型では問題が生じる場合があります。

new 型と periodic 型には、publisher という送信のためのスレッドが接続毎に用意されます。これらのタイプでは、OutPort の write() 関数を呼ぶと、データは一旦バッファに書きこまれ write() 関数はすぐに終了します。
データの実際の送信は、publisher の別スレッドが行います。

<div align="center"><a href="dataport_subscriptiontype_ja.png"><img src="dataport_subscriptiontype_ja.png" width="50%;"></a></div>
<div align="center"><strong>サブスクリプション型</strong></div>

new 型は書き込みと同時に送信待ちしている publisher に対してシグナルを送り、起こされた publisher スレッドが実際のデータ送信を行います。
バッファへのデータの書き込み周期に対して、データ送信時間が十分に短ければ、flush とほぼ同じですが、データ送信に時間がかかる場合には、必ずしもすべてのデータが受信側に届くわけではないことに注意してください。
そういった意味で new 型はベストエフォート的なデータ送信方法です。

一方 periodic 型は、publisher が一定周期でバッファからデータを取り出しデータ送信を行います。送信周期は、接続時に外部から与えることができます。
データ送信周期に比べて、データ送信時間が長い場合、送信周期が守られない可能性があります。また、データをバッファに書き込む周期 (アクティビティの周期) と、バッファからデータを取り出して送信する周期 (publisher の周期)、および後述するデータ送信ポリシーの整合性を考慮しなければ、定常的にバッファフル状態またはバッファエンプティ状態を引き起こす可能性があります。いわゆる、生産者・消費者問題を考慮する必要がある接続タイプになΩます。


#### サブスクリプション型まとめ

<table class="table-alt">
  <tr>
    <td> <strong>Subscription Type</strong></td>
    <td> <strong>同期・非同期</strong></td>
    <td> <strong>概要</strong></td>
  </tr>
  <tr>
    <td><strong>New</strong></td>
    <td><strong>非同期通信</strong></td>
    <td>データポートにデータが write された後、非同期で<strong>できるだけ速く</strong>送る。 <br> 基本的には到達保証はないが、インター
フェース型が corba_cdr の場合TCP通信であるため、トランスポート層レベルでは到達が保証されている。他のインターフェース型に>ついては、その伝送方式による。 <br> <strong>[ユースケース]:</strong> データ送信側がリアルタイム実行、データ受信型が外部ノードの場合は New か Periodic を利用する。</td>
  </tr>
  <tr>
    <td><strong>Periodic</strong></td>
    <td><strong>非同期通信</strong></td>
    <td>データポートにデータが write された後、非同期で<strong>周期的に</strong>送る。 <br> 基本的には到達保証はなく、<strong>間引き</strong>も可能
であるため、すべてのデータが送信される保証もない。ただし、送られたデータについてはインターフェース型が corba_cdr の場合TCP通信であるため、トランスポート層レベルでは到達が保証されている。他のインターフェース型については、その伝送方式による。 <br> <strong>[ユースケース]:</strong> データ送信側のデータ生成周期と受信側の消費周期が異なる場合にここれを利用する。</td>
  </tr>
  <tr>
    <td><strong>Flush</strong></td>
    <td><strong>同期通信</strong></td>
    <td>データポートに write された後、データを同期転送する。write 関数から戻ると受信側にデータが届いたことが保証される。
(受信側が消滅しているばあいを除く。) <br> <strong>[ユースケース]</strong> 複数の RTC を複合化しリアルタイム実行しており、それらの RTC 間の通信は通常 Flush で実行する。リモートノードに対するデータ通信でも、到達を保証したい場合は Flush を使用する。</td>
  </tr>
</table>


### データ送信ポリシー

サブスクリプション型が、new または periodic の場合、OutPort はバッファを持ちます。データを送信するタイミングで、バッファに溜まっているデータをどのような方針で送信するかをデータ送信ポリシーと呼びます。

データ送信ポリシーには、バッファに保持されているデータをすべて送信する <strong>all</strong>、先入れ先だし方式で一つずつ送信する <strong>fifo</strong>、バッファに保持されているデータをいくつかおきに送信する <strong>skip</strong>、そして最新値のみ送信し、その他のデータはすべて捨ててしまう <strong>new</strong> の四種類があります。

<table class="table-alt">
  <tr>
    <th>ポリシー名</th>
    <th>意味</th>
  </tr>
  <tr>
    <td>all</td>
    <td>バッファに残っているデータをすべて送信</td>
  </tr>
  <tr>
    <td>fifo</td>
    <td>先入れ先だし方式で、データを一つずつ送信</td>
  </tr>
  <tr>
    <td>skip</td>
    <td>n 個おきにデータを送信し、それ以外は捨てる</td>
  </tr>
  <tr>
    <td>new</td>
    <td>最新値のみ送信し、古い値は捨てる</td>
  </tr>
</table>

サブスクリプション型を new や periodic 等の非同期型にした場合、データの生成速度、消費速度、さらに通信路の帯域幅を事前に見積もったうえで、これらのポリシーを適切に設定する必要があります。


<!-- ------------------------------------------------------------ -->
## InPort プログラミング

ここからは実際のプログラムでデータポートがどのように使われるのかを見ていきます。

InPort を使う際には、以下のルールを念頭に置いたうえでプログラミングすることを推奨します。

- データは来ていないかもしれないとして処理する
- データは正しくないかもしれないとして処理する
- 配列の長さは常に変化するかもしれないとして処理する
- データは途中から来なくなるかもしれないとして処理する

InPort に接続される OutPort は他のノードの RTC の OutPort かもしれません。ポートは接続されていないかもしれないし、データを送ってないかもしれません。
配列が含まれるデータ型の場合、配列の長さは次のデータでは変化するかもしれません。また、ネットワーク接続が切れたり、相手の RTC が停止してしまった場合、途中からデータを送らなくなるかもしれません。

モジュール化する上で、仮定や前提条件を少なくし、他の要素に依存しないように作るということは非常に重要で、これによって再利用性が高く使いやすいモジュールになるかどうかが変わってきてしまいます。

さて、InPort の実際の使い方を見ていく前に、InPort の構造を説明します。

<div align="center"><a href="dataport_inport_ja.png"><img src="dataport_inport_ja.png" width="50%;"></a></div>
<div align="center"><strong>InPort の構造</strong></div>

InPort の実体はオブジェクトです。C++ では、クラステンプレート InPort<T>型として定義されています。T にはデータポートが使用するデータ型が入ります。下の例は、サンプルに付属している ConsoleOut コンポーネントの InPort 宣言の例です。
InPort が TimedLong 型で宣言されているのがわかります。

```
  TimedLong m_in;
  InPort<TimedLong> m_inIn;
```

宣言や初期化は、RTCBuilder や rtc-template を使っていれば自動的に記述してくれます。InPort を使用する際には、InPort オブジェクトに結び付けられた T型の変数が一つ定義されます。
先ほどの例で、TimedLong 型の m_in というものがその変数です。これを InPort 変数と呼びます。

InPort と InPort 変数は初期化時に関連付けられ、InPort のデータ読み出し関数 read() を呼ぶと、InPort が持つバッファからデータが一つ読みだされ InPort 変数にコピーされます。
InPort にやってきたデータを使用する際にはこのように InPort 変数を介して利用します。

### InPort オブジェクト

InPort クラステンプレートで定義されている関数を以下の表に示します。

これは C++ の InPort クラスの関数ですが、他の言語においてもほぼ同一の名前で各関数が提供されています。
なお、これらの関数のリファレンスマニュアルは、Windows では、「スタート」>「OpenRTM-aist」>「C++」>「documents」>「Class reference」から見ることができます。
Linux 等ではドキュメントがインストールされていれば、
${prefix}/share/OpenRTM-aist/docs/ClassReference 等からアクセスすることができます。
マニュアルは doxygen 形式で記述されており、上部メニューの「ネームスペース」からクラス一覧を表示させ、InPort を参照してください。

<table class="table-alt">
  <tr>
    <th>InPort (const char *name, DataType &value)</th>
    <th>コンストラクタ</th>
  </tr>
  <tr>
    <td>`InPort` (void)</td>
    <td>デストラクタ</td>
  </tr>
  <tr>
    <td>const char *  name ()</td>
    <td>ポート名称を取得する。</td>
  </tr>
  <tr>
    <td>bool  isNew ()</td>
    <td>最新データが存在するか確認する</td>
  </tr>
  <tr>
    <td>bool  isEmpty ()</td>
    <td>バッファが空かどうか確認する</td>
  </tr>
  <tr>
    <td>bool  read ()</td>
    <td>DataPort から値を読み出す</td>
  </tr>
  <tr>
    <td>void  update ()</td>
    <td>バインドされた T 型の変数に InPort バッファの最新値を読み込む</td>
  </tr>
  <tr>
    <td>void  operator>> (DataType &rhs)</td>
    <td>T 型のデータへ InPort の最新値データを読み込む</td>
  </tr>
  <tr>
    <td>void setOnRead (OnRead< DataType > *on_read)</td>
    <td>InPort バッファへデータ読み込み時のコールバックの設定</td>
  </tr>
  <tr>
    <td>void  setOnReadConvert (OnReadConvert< DataType > *on_rconvert)</td>
    <td>InPort バッファへデータ読み出し時のコールバックの設定</td>
  </tr>
</table>


主に使用する関数は、isNew() および read() 関数となります。実際に使われている例を見てみます。

```
 RTC::ReturnCode_t ConsoleOut::onExecute(RTC::UniqueId ec_id)
 {
   if (m_inIn.isNew())
     {
       m_inIn.read();
       std::cout << "Received: " << m_in.data << std::endl;
       std::cout << "TimeStamp: " << m_in.tm.sec << "[s] ";
       std::cout << m_in.tm.nsec << "[ns]" << std::endl;
     }
   return RTC::RTC_OK;
 }
```

m_inIn.isNew() でデータが来ているかを確認し、m_inIn.read() で InPort 変数 m_in にデータを読み込んでいます。その後、m_in の内容を cout で表示しています。

通常は、この例のように InPort のデータの処理は、onExecute() 関数内で行い、InPort にやってくるデータを周期的に処理するようにプログラムします。

他の関数は説明からすぐにわかると思いますが、コールバックオブジェクトセットする関数 setOnRead と setOnRedConvert については、応用編で改めて説明します。


## OutPort

OutPort は InPort と比べると、単に自分がデータを送りだすだけですので、少し簡単になります。

<div align="center"><a href="dataport_outport_ja.png"><img src="dataport_outport_ja.png" width="50%;"></a></div>
<div align="center"><strong>OutPort の構造</strong></div>

構造は InPort とほぼ同じで、C++ であれば、OutPort は T型の型引数をとるクラステンプレートになっています。T は OutPort のデータ型で、この T が同じ InPort に対してしかデータを送ることはできません。
OutPort も InPort 同様、OutPort 変数と一緒に利用します。OutPort 変数にデータを書き込んだ後、OutPort の write() 関数を呼ぶとデータが OutPort から接続されている InPort へ送り出されます。

### OutPort オブジェクト

OutPort クラステンプレートで定義されている関数を以下の表に示します。

OutPort についても InPort 同様、他の言語においてもほぼ同一の名前で各関数が提供されています。リファレンスマニュアルについても InPort 同様、doxygen の「ネームスペース」から<strong>OutPort</strong>を見てください。

<table class="table-alt">
  <tr>
    <th>OutPort (const char *name, DataType &value)</th>
    <th>コンストラクタ</th>
  </tr>
  <tr>
    <td>`OutPort` (void)</td>
    <td>デストラクタ</td>
  </tr>
  <tr>
    <td>bool  write (DataType &value)</td>
    <td>データ書き込み</td>
  </tr>
  <tr>
    <td>bool  write ()</td>
    <td>データ書き込み</td>
  </tr>
  <tr>
    <td>bool  operator<< (DataType &value)</td>
    <td>データ書き込み</td>
  </tr>
  <tr>
    <td>DataPortStatus::Enum  getStatus (int index)</td>
    <td>特定のコネクタへの書き込みステータスを得る</td>
  </tr>
  <tr>
    <td>DataPortStatusList  getStatusList ()</td>
    <td>特定のコネクタへの書き込みステータスリストを得る</td>
  </tr>
  <tr>
    <td>void  setOnWrite (OnWrite< DataType > *on_write)</td>
    <td>OnWrite コールバックの設定</td>
  </tr>
  <tr>
    <td>void  setOnWriteConvert (OnWriteConvert< DataType > *on_wconvert)</td>
    <td>OnWriteConvert コールバックの設定</td>
  </tr>
</table>


OutPort で主に使用する関数は write() と getStatusList() になります。


```
 RTC::ReturnCode_t ConsoleIn::onExecute(RTC::UniqueId ec_id)
 {
   std::cout << "Please input number: ";
   std::cin >> m_out.data;
   if (!m_outOut.write())
     {
       DataPortStatusList stat = m_outOut.getStatusList();
 
       for (size_t i(0), len(stat.size()); i < len; ++i)
         {
           if (stat[i] != PORT_OK)
             {
               std::cout << "Error in connector number " << i << std::endl;
             }
         }
     }
   return RTC::RTC_OK;
 }
```

まず、std::cin >> m_out.data で標準入力から OutPort へデータを代入します。その後、m_outOut.write() でデータを OutPort から送り出しています。
戻り値が false の場合、ポートのステータスを調べてどの接続でエラーが起きているのかを表示しています。


## データポートのまとめ

ここでは、データポート (InPort、OutPort) の基本的な概念と使い方について解説しました。
データポートの宣言は、RTCBuilder や rtc-template で行ってくれますが、実際にどのようにデータを与えるのか、あるいは利用するのかについてはコンポーネント開発者が記述する必要があります。
ただし、簡単に使用するだけであれば、InPort では、isNew() と read() 関数だけ、OutPort では、write() と getStatusList() 関数だけ覚えておけば十分でしょう。

