---
layout: page
title: "コンフィギュレーション(基礎編) "
---
<!-- Title: コンフィギュレーション(基礎編) -->

#contents(4)

<!-- ============================================================ -->
## コンフィギュレーションとは

ロボットシステムを構築するうえで、システムの外部環境、使用状況や、個別のデバイス、ロボットの特性に応じて作成するプログラム内のパラメーターを変更ことが度々あります。
単純な実験をするための簡単なプログラムでは、パラメーターをハードコード(埋め込んで)して、変更する度に直接書き換え、コンパイルすることで対処できるかもしれません。
もう少し進んで、パラメーターをファイル等から読み込んだり、コマンドライン引数で渡したり等の工夫をすることで再利用性はぐっと高くなります。
一つのプログラムを用途に応じて再利用するためには、こうしたパラメーターを埋め込まずに外部化することが非常に重要になってきます。

RTコンポーネントによって構築されるRTシステムでは、様々な人が作った多様なコンポーネントが協調して動作しますので、コアロジック内部で使用されるパラメーターをユーザーが自由に定義し、実行時に外部から変更するための機能が用意されています。
これをコンフィギュレーション(機能)と呼びます。コンフィギュレーションは複数のパラメーターセットを持つことができ、パラメーターセットを一斉に入れ替えることもできます。
パラメーターを予め変更可能にしておくことで、RTCを様々なシステムで簡単に再利用することができます。

<div align="center"><a href="configuration_example_ja.png"><img src="configuration_example_ja.png" width="50%;"></a></div>
<div align="center"><strong>コンフィギュレーションの例</strong></div>

このセクションでは、RTコンポーネントの重要な機能の一つであるコンフィギュレーションについて、仕組みと実際の使い方について説明していきます。

## コンフィギュレーションの仕組み

下図はコンフィギュレーションの大まかな仕組みを表しています。

<div align="center"><a href="configuration_functionality_ja.png"><img src="configuration_functionality_ja.png" width="50%;"></a></div>
<div align="center"><strong>コンフィギュレーションの仕組み</strong></div>

パラメーターの<strong>名前</strong>と<strong>値</strong>のペアを<strong>コンフィギュレーションパラメーター</strong>と呼びます。
一つのコンポーネントは複数のコンフィギュレーションパラメーターを定義することができ、その集合を<strong>コンフィギュレーションセット</strong>と呼びます。

さらに一つのコンポーネントは複数のコンフィギュレーションセットを持つことができ、そのうち一つのコンフィギュレーションのみが、実際のパラメーターの値となります。
このコンフィギュレーションセットを、<strong>アクティブコンフィギュレーション</strong>と呼びます。コンフィギュレーションセットは名前を付けることができ、その名前により区別されます。

外部のツール(RTSystemEditorやrtshell等)を利用して、個々のパラメーター、あるいはアクティブなコンフィギュレーションセットを変更することができます。
コンフィギュレーションの内容は、コンフィギュレーションに結び付けられた変数(<strong>パラメーター変数</strong>)に反映され、RTコンポーネント内のロジックで使用することができます。
こうして、ロジック内部で使用されるパラメーターを外部から容易に変更できるようにすることでコンポーネントの再利用性を高めることができます。


- <strong>コンフィギュレーション</strong>: コンポーネント内のパラメーターを外部化するためのRTCの機能
- <strong>コンフィギュレーションパラメーター</strong>: 実際にコンポーネント内の外部化されるパラメーター。キーと値から構成される。
- <strong>コンフィギュレーションセット</strong>: キーと値のリストから構成される、パラメーターのリスト。RTCは複数のセットを持つことができる。
- <strong>コンフィギュレーションセット名</strong>: コンフィギュレーションセットにつけられた名前。セットはそれぞれ名前で区別される。
- <strong>アクティブコンフィギュレーション</strong>: RTCは複数のコンフィギュレーションセットを持つことができ、そのうち実際にパラメーターに反映される有効なセットをアクティブコンフィギュレーションと呼ぶ。
- <strong>パラメーター変数</strong>: コンフィギュレーションパラメーターに結び付けられた変数。コンフィギュレーションの内容が変更されると変数に代入されている値が変更されます。

型のある言語では、コンフィギュレーションパラメーターはその言語で利用可能な型であればどのような型でもパラメーターとして利用することができます。
もちろん、型のない言語でも同様ですが、重要な点は、こうしたパラメーターを外部から設定する際には、その値は文字列によって与えられるということです。

コンフィギュレーションは、文字列をそれぞれのパラメーター型に変換して、実際の変数にセットします。
構造体や配列など、文字列からデータに簡単には変換できないようなデータ型でも、変換関数を定義することで、どのような型のデータでも同じように扱うことができます。
これは、あらかじめIDL定義が必要なデータポートやサービスポートとは大きく異なる点です。

<!-- ============================================================ -->
## パラメーターを定義する

RTコンポーネント内で利用するパラメーターを定義する方法にはいくつかあります。

- RTCBuilderでコンポーネント設計時に定義する
- rt-templateでコンフィギュレーションパラメーターを定義する
- 手動で必要なコードを書く

以下では、それぞれの方法について説明します。

<!-- ------------------------------------------------------------ -->
### RTCBuilderによる定義

コンフィギュレーションパラメーターを定義するもっとも簡単な方法はRTCの設計ツールであるRTCBuilderで、RTC設計時にコンフィギュレーションパラメーターを定義することです。

下図はRTCBuilderのコンフィギュレーションの定義画面です。
この画面で必要なパラメーターを定義することで、コンフィギュレーションパラメーターを利用するために必要なコードが言語を問わず自動的に生成されます。

<div align="center"><a href="configuration_rtcb00_ja.png"><img src="configuration_rtcb00_ja.png" width="50%;"></a></div>
<div align="center"><strong>RTCBuilderの設定画面</strong></div>

コンフィギュレーションパラメーターを利用するためには、RTCBuilderのコンフィギュレーションタブを押し、パラメーターリスト横の[Add]ボタンをクリックします。
すると、コンフィギュレーションパラメーターが一つ追加されますので、適切な

- 名称(必須)
- データ型(必須)
- デフォルト値(必須)

を入力します。

名称は(デフォルトではconf_name0等となっているので)、そのパラメーターの性質を端的に表す分かりやすい名前を付けてください。
ドロップダウンリストから選択できる型名は、各言語において適切に変換され定義されます。
Python等明示的に型宣言が必要ない言語では、ここで設定された型名はコード上には現れないかもしれません。

上でも述べたように、コンフィギュレーションパラメーターは値を文字列として与えて、文字列を特定の型に変換することで様々な型のパラメーターに対応可能です。
ただし、外部から文字列として値が入力されるため、変換不可能な文字列など不正なパラメーター入力があった場合、変換がエラーになる場合もあります。
ここで設定されたデフォルト値は、設定された値の変換が不正な場合に代わりに使用される値です。

このほか、必須でない項目として以下の項目があります。必要に応じて入力してください。

- 変数名: 変数名として使用する文字列。空の場合は名称が使用されます。
- 単位: このパラメーターの単位。現在のところ、人間が読む以外には使われていません。
- 制約条件: このパラメーターの制約条件を与えます。この条件はRTSystemEditorで使用されます。連続値の場合は不等号、列挙値の場合はカンマ区切りなど指定できます。
- Widget: RTSystemEditorでパラメーターを操作するときに使用されるコントロール。text、slider、spin、radioから選択できます。
- Step: 上記のWidgetがsliderやspinの場合のステップを指定します。
<br>
<br>

<div align="center"><div align="center"><a href="param1_slider_ja.png"><img src="param1_slider_ja.png" width="80%;"></a></div>;  <div align="center"><a href="param2_spin_ja.png"><img src="param2_spin_ja.png" width="50%;"></a></div>;</div>
<div align="center"><strong>スライダーとスピンの設定</strong></div>

<div align="center"><div align="center"><a href="param3_radio_ja.png"><img src="param3_radio_ja.png" width="80%;"></a></div>;  <div align="center"><a href="param4_text_ja.png"><img src="param4_text_ja.png" width="50%;"></a></div>;</div>
<div align="center"><strong>ラジオボタンとテキストの設定</strong></div>

詳細については、画面右側のヒントや、RTCBuilderのマニュアルを参照してください。

<!-- ------------------------------------------------------------ -->
### rtc-templateによる定義

rtc-templateはコマンドラインから使用するコンポーネントテンプレートジェネレータです。
rtc-templateでコンフィギュレーションを使用するには以下のように指定します。

```
    /usr/local/bin/rtc-template -bcxx --module-name=ConfigSample 
```
    --module-type=DataFlowComponent 
    --module-desc=Configuration example component --module-version=1.0 
    --module-vendor=Noriaki Ando, AIST --module-category=example 
    --module-comp-type=DataFlowComponent --module-act-type=SPORADIC 
    --module-max-inst=10 --config=int_param0:int:0 
    --config=int_param1:int:1 --config=double_param0:double:0.11 
    --config=double_param1:double:9.9 
    --config=str_param0:std::string:hoge 
    --config=std_param:std::string:dara 
    --config=vector_param0:std::vector<double>:0.0,1.0,2.0,3.0,4.0
```
 
    # 実際には1行で入力するか、継続文字を行末に(UNIXでは\、Windowsでは^)を補ってください
```

これは、サンプルに付属しているConfigSampleでの指定例です。

 --config=<名称>:<データ型>:<デフォルト値>

のように指定します。データ型については、その言語で使用するデータ型を指定しますが、プリミティブ型以外ではうまく動作しなかったり、手動で修正が必要な場合があります。

<!-- ------------------------------------------------------------ -->
### 手動による定義

あまり推奨されませんが、手動でもコンフィギュレーションパラメーターを定義することができます。
新たにパラメーターを追加したくなった場合等に有効ですが、ドキュメントやRTC.xmlファイル等を更新しないと、第三者がこのRTCを使用した場合に仕様と実装の整合性が取れていないために、混乱を来たす可能性がありますので注意してください。

ただし、コンフィギュレーションがどのように宣言され使用されるのかを知ることは意味がありますのでここで説明します。

コンフィギュレーションを使用するには以下の手続きが必要です。

#### コンフィギュレーションパラメーター(以下パラメーター)の用途、名称、型を決める

上で述べたように、コンポーネントのどの部分でパラメーターを使用するのか、またそのパラメーターの特徴を表す名称と実装時の型名(型のある言語の場合)を決めます。

#### パラメーターの変数をコンポーネントのヘッダ(private/protected)に宣言する

RTCBuilderやrtc-templateで生成したファイルであれば、以下のようなタグに囲まれた部分がありますので、ここにコンフィギュレーションパラメーターのための変数を宣言します。

```
  // Configuration variable declaration
  // <rtc-template block="config_declare">
 
  // </rtc-template>
```

上のConfigSampleの例であれば以下のようになります。

```
  // Configuration variable declaration
  // <rtc-template block="config_declare">
  int m_int_param0;
  int m_int_param1;
  double m_double_param0;
  double m_double_param1;
  std::string m_str_param0;
  std::string m_str_param1;
  std::vector<double> m_vector_param0;
  
  // </rtc-template>
```

#### コンポーネントの実装ファイルのstatic変数<コンポーネント名>_spec[]にパラメーターの宣言とデフォルト値を追加する

コンフィギュレーションパラメーターはコンポーネント内で、Propertiesというデータストアに入れられ管理されます。このProperties内では、

```
 conf.<コンフィギュレーションセット名>.<パラメーター名>
```

というキーでコンフィギュレーションパラメーターを保持しています。デフォルト値として<strong>default</strong>というコンフィギュレーションセット名が予約済みとなっており、デフォルト値はすべてこの<strong>default</strong>コンフィギュレーションセットとして定義されます。

上のConfigSampleの場合、以下のように追加します。

```
 // Module specification
 // <rtc-template block="module_spec">
 static const char* configsample_spec[] =
   {
     "implementation_id", "ConfigSample",
     "type_name",         "ConfigSample",
     "description",       "Configuration example component",
     "version",           "1.0",
     "vendor",            "Noriaki Ando, AIST",
     "category",          "example",
     "activity_type",     "DataFlowComponent",
     "max_instance",      "10",
     "language",          "C++",
     "lang_type",         "compile",
     // Configuration variables
     "conf.default.int_param0", "0",
     "conf.default.int_param1", "1",
     "conf.default.double_param0", "0.11",
     "conf.default.double_param1", "9.9",
     "conf.default.str_param0", "hoge",
     "conf.default.str_param1", "dara",
     "conf.default.vector_param0", "0.0,1.0,2.0,3.0,4.0",
  
     ""
   };
 // </rtc-template>
```

Configuration variables以下の部分がデフォルトコンフィギュレーションセットの定義になります。

#### 各変数を初期化子で初期化する

RTCBuilderやrtc-templateで生成された変数はコンストラクタの初期化子による初期化は行われませんが、可能であればすべての変数はコンストラクタの初期化子で初期化したほうがよいでしょう。
また、各変数にデフォルト値がセットされるのはonInitialize()関数の中のbindParameter()関数が呼ばれた後ですので、原則としてそれ以前には使用してはいけません。


#### bindParameter()関数でパラメーターと変数をバインドする

最後に変数とパラメーターの名称、デフォルト値、さらに変換関数をバインドすることで、単なる変数をコンフィギュレーションパラメーターにします。
RTObjectクラスのメンバ関数(メソッド)であるbindParameter()を使用します。

```
 bindParameter(<パラメーター名称(文字列)>, 変数, <デフォルト値(文字列)>, <変換関数>)
```

上のConfigSample(C++の例)では以下のようになります。

```
  // <rtc-template block="bind_config">
  // Bind variables and configuration variable
  bindParameter("int_param0", m_int_param0, "0");
  bindParameter("int_param1", m_int_param1, "1");
  bindParameter("double_param0", m_double_param0, "0.11");
  bindParameter("double_param1", m_double_param1, "9.9");
  bindParameter("str_param0", m_str_param0, "hoge");
  bindParameter("str_param1", m_str_param1, "dara");
  bindParameter("vector_param0", m_vector_param0, "0.0,1.0,2.0,3.0,4.0");
  
  // </rtc-template>
```

こうすることで、各変数とコンフィギュレーションパラメーターがバインドされ、RTSystemEditor等からこれらの変数を操作することができる、コンフィギュレーションパラメーターが利用可能になります。

なお、bindParameter()に与える変換関数は、組込み型については、上記の例のように不要で、特に明示的に与える必要はありません。
しかし、独自の構造体や複雑な型等をコンフィギュレーションパラメーターとして使用したい場合は、文字列からそれらの型への変換を定義しここに与える必要があります。
変換関数の詳細については後述します。

<!-- ============================================================ -->
## パラメーターを使う

パラメーターを使うのは非常に簡単です。これまで述べてきたように、コンフィギュレーションパラメーターとして宣言された変数を単に利用するだけです。
ただし、使用に当たってはいくつかの条件があり、これを守って利用する必要があります。

<!-- ------------------------------------------------------------ -->
### 変数が使用できるコールバック関数

コンフィギュレーション変数は、特定のコールバック関数(onXXX())内でしか利用することはできません。
外部からのコンフィギュレーション変数の変更は非同期的に行われます。
通常このような場合には、ミューテックス等で変数への排他アクセス制御を行う必要がありますが、これを実現するにはコンポーネント開発者も各変数へのアクセス時にミューテックス保護を行う必要があります。
これを回避するために、OpenRTM-aistでは外部からのコンフィギュレーションの変更は、コールバック関数の外で行われるようになっています。

利用できるコールバック関数は、以下のものになります。

- onInitialize() (※)
- onActivated()
- onExecute()
- onStateUpdate()
- onDeactivate()
- onAborting()
- onError()
- onReset()
- onFinalize() (※)

ほぼすべてのコールバック関数内でコンフィギュレーションパラメーターを利用することができます。
ただし、onInitialize()においては、bindParameter()を行う前には当然コンフィギュレーションパラメーターを利用できません。
また、onFinalize()内では、その呼び出しの直前にコンフィギュレーションパラメーターに対してなされた変更が反映されない可能性があります。

<!-- ------------------------------------------------------------ -->
### 変数は読み出し専用

コンフィギュレーションパラメーターの変数は、コンポーネントの外部から変更されその値がパラメーター用変数に代入されます。しかし、パラメーター用変数に
onExecute()等内部の関数内で書きこんでも、外から見えるパラメーターの値には反映されません。

このように、変数の値の変更は一方通行ですので、コンポーネント内部からの変数に対する書き込みは意味がありません。
コンフィギュレーション変数はread onlyで使いましょう。

<!-- ------------------------------------------------------------ -->
### 値が正しいか常にチェックする

コンフィギュレーションパラメーターの値は、上述したように外部から文字列として与えられたものを変換関数で変換したものが実際使用される変数に代入されます。
文字列ですので、本来数値が代入されるべきところに文字列が代入されたり、short intで宣言された変数に、上限以上の大きさの数値が代入されることもあり得ます。
従って、受け取った側では変数が想定されている値の範囲内に入っているか、あり得ない値が代入されていないかについて、プログラム上で使用前には常にチェックすることが推奨されます。


<!-- ============================================================ -->
## パラメーターを設定する

コンフィギュレーションパラメーターは、いくつかのセットを持ち、実行時にそれらを同時に変更できることを上で述べました。
その一方で、RTCBuilderやrtc-templateでコンポーネントを設計する時点では、デフォルトコンフィギュレーションセットしか定義できませんでした。
ここでは、コンフィギュレーションセットの使い方について説明します。

<!-- ------------------------------------------------------------ -->
### コンポーネント設定ファイル

デフォルトコンフィギュレーションセットはソースコードに埋め込まれます。
同じ方法で、他のコンフィギュレーションセットも原理的にはソースコードに埋め込むことで増やすことができます。
しかし、RTCコンフィギュレーション機能の目的は、ソースコードを変更しないで、用途に応じてパラメーターを変更することで、一つのコンポーネントを様々な用途に使うことでしたので、ソースコードに他のコンフィギュレーションセットを埋め込むのは本末転倒です。

コンフィギュレーションセットはコンポーネントのコンフィギュレーションファイルで与えることができます。
コンポーネントの設定を行うファイルにはrtc.confがありますが、これは主にコンポーネントを管理するミドルウエアのための設定ファイルで、コンポーネントのための設定ファイルは、rtc.conf内で以下のように指定することができます。

```
 corba.nameservers: localhost
 naming.formats: %h.host_cxt/%n.rtc
 example.ConfigSample.config_file: configsample.conf
```

example.ConfigSample.config_fileの部分がコンポーネントのコンフィギュレーションファイルの指定部分です。コンフィギュレーションファイルを指定する部分は以下のようになっています。

```
 <カテゴリ名>.<モジュール名>.config_file: <ファイル名>
```

また、コンポーネントのモジュール名の代わりにインスタンス名を与えることもできます。

```
 <カテゴリ名>.<インスタンス名>.config_file: <ファイル名>
```

したがって、インスタンス毎に異なるコンフィギュレーションファイルを与えることもできます。

```
 example.ConfigSample0.config_file: consout0.conf
 example.ConfigSample1.config_file: consout1.conf
 example.ConfigSample2.config_file: consout2.conf
```

<!-- ------------------------------------------------------------ -->
### コンフィギュレーションセットの設定

コンフィギュレーションファイルの中には、使用したいコンフィギュレーションセットを記述します。

```
 configuration.active_config: mode1
 
 conf.mode0.int_param0: 12345
 conf.mode0.int_param1: 98765
 conf.mode0.double_param0: 3.141592653589793238462643383279
 conf.mode0.double_param1: 2.718281828459045235360287471352
 conf.mode0.str_param0: mode0
 conf.mode0.str_param1: foo
 conf.mode0.vector_param0: 0.0,0.1,0.2,0.3,0.4
 
 conf.mode1.int_param0: -999
 conf.mode1.int_param1: 999
 conf.mode1.double_param0: 297992458
 conf.mode1.double_param1: 2.97992458e+8
 conf.mode1.str_param0: mode1
 conf.mode1.str_param1: AIST
 conf.mode1.vector_param0: 1,2,3,4,5,6,7,8,9
 
 conf.__widget__.int_param0: slider.1
 conf.__widget__.int_param1: spin
 conf.__widget__.double_param0: slider.0.1
 conf.__widget__.double_param1: text
 conf.__widget__.str_param0: radio
 conf.__widget__.str_param1: text
 conf.__widget__.vector_param0: text
 
 conf.__constraints__.int_param0: 0<=x<=150
 conf.__constraints__.int_param1: 0<=x<=1000
 conf.__constraints__.double_param0: 0<=x<=100
 conf.__constraints__.double_param1: 
 conf.__constraints__.str_param0: (default,mode0,mode1,foo,bar,radio)
 conf.__constraints__.str_param1: 
 conf.__constraints__.vector_param0: 
```

<!-- ------------------------------------------------------------ -->
### アクティブコンフィギュレーションセットの指定

最初の行のconfiguration.active_configで、アクティブなコンフィギュレーションセット名を指定しています。ここではmode1というセット名で、当然、存在するセット名を指定する必要があります。

```
 configuration.active_config: mode1
```

<!-- ------------------------------------------------------------ -->
### コンフィギュレーションセットの設定

次に、conf.mode0で始まるパラメーターのリストがありますが、これがセット名<strong>mode0</strong>のコンフィギュレーションパラメーターのリストです。指定の仕方は、ソースコードとほぼ同じように

```
 conf.<セット名>.<パラメーター名>: <デフォルト値>
```

となっています。必ず、存在するすべてのコンフィギュレーションパラメーターについて指定してください。
指定がない場合はデフォルト値が使用されます。その次に、conf.mode1で始まるパラメーターのリストがありますが、これもmode0同様、mode1というセット名のパラメーターの設定です。

<!-- ------------------------------------------------------------ -->
### 拡張機能
#### conf._ widget_ 設定
次に、conf._ widget_で始まる設定リストがあります。これは、RTSystemEditorで使用される特殊なパラメーターです。
RTCBuilderでコンフィギュレーションパラメーターを設定するときwidgetを指定できることを上で説明しましたが、ここで設定された内容が、conf.<u>widget</u>設定されます。
slider、radio、spin、textの4種類を設定することができ、それぞれRTSystemEditorでコンフィギュレーションパラメーター設定ダイアログを開いたときに、スライダー、ラジオボタン、スピンボタン、テキストボックスでパラメーターを操作することができます。

```
 conf.__widget__.<パラメーター名>: ウィジェット名
```

- スライダー(slider)を設定した場合
```
 conf.__widget__.int_param0: slider.5
```

上記ののように設定することで、スライダーの刻み幅を5にすることができます。現在のところ、この刻み幅を小数にすることはできません。
ただし、今後のバージョンアップで改善される可能性があります。

- スピンボタン(spin)を設定した場合
```
 conf.__widget__.int_param1: spin
```

スピンボタンのステップ幅は常に1刻みです。int等の整数値パラメーターにのみ使用することをお勧めします。

- ラジオボタン(radio)を設定した場合
```
 conf.__widget__.str_param0: radio
```

- テキスト(text)を設定した場合
```
 conf.__widget__.str_param1: text
```

これらconf.<u>widget</u>パラメーターを設定した場合、conf._ constraints_パラメーターも設定する必要があります。

#### conf.__onstraints_の設定
conf._ constraints_パラメーターは、値の範囲を設定するための特殊なパラメーターです。下記に設定例を示します。不正なパラメーターを設定すると、ウィジェットが正常に表示されないので注意が必要です。

- スライダー(slider)を設定した場合は、以下のように仮変数<strong>x</strong>と等号、不等号を用いて指定します。
```
 conf.__constraints__.int_param0: 0<=x<=150
```

- スピンボタン(spin)を設定した場合もスライダーと同様に仮変数<strong>x</strong>と等号、不等号を用いて指定します。
```
 conf.__constraints__.int_param0: 0<=x<=1000
```

- ラジオボタン(radio)を設定した場合は、括弧内にボタン名称をカンマで区切ります。複数のボタン名称を指定することができます。
```
 conf.__constraints__.str_param0: (default,mode0,mode1)
```

- テキスト (text) を設定した場合は、表示させたい文字を指定します。
```
 conf.__constraints__.str_param1: AIST
```

下記に、上記設定によるRTSystemEditorでの表示例を示します。

<div align="center"><a href="configuration_constraints_ja.png"><img src="configuration_constraints_ja.png" width="70%;"></a></div>
<div align="center"><strong>conf.__onstraints_の表示例</strong></div>

<!-- ------------------------------------------------------------ -->
### 変換関数について

C++等では、intやdoubleなどの組込み型については特に変換関数を指定する必要はありません。一方で、構造体やSTLコンテナなどユーザー独自の型を利用した
い場合もあります。この場合、文字列からそれぞれの型への変換をどのようにするかをbindParameter()に関数として与えてあげる必要があります。

変換関数については以下のように、各言語ごとにルールがあります。以下、各言語ごとの方法を述べます。

#### C++の場合の変換関数

C++におおいては、bindParameterのプロトタイプ宣言は

```
 template <typename VarType>
     bool bindParameter(const char* param_name, VarType& var,
 		       const char* def_val,
 	            bool (*trans)(VarType&, const char*) = coil::stringTo)
               
```

のようになっており、第4引数の trans に適当な関数ポインタを与えることで、文字列から当該型への変換が行われます。デフォルトでは、coilライブラリ関数の stringTo() 関数が与えられています。
自分でこのstringTo() に相当する変換関数を書いて、関数ポインタを与えることもできますが、coil::stringTo() 関数自体も関数テンプレートとなっており、std::stream に対する operator >>()関数

```
 std::istream& operator>>(std::istream&, T)
```

が定義されていれば、自動的にこれを利用して文字列から特定の型への変換が行われます。

すなわち、std::cin >> <ある型の変数>のような書き方ができるのであれば、その型はoperator>>()が定義されており、特に変換関数を書かなくともコンフィギュレーションのパラメーターとして利用することができます。

もし、変換関数がない場合、例えば、以下のようにカンマ区切りの数値列

```
 0.0,1.0,2.0,3.0,4.0
```

を std::vector<double>へ変換するための変換関数は、

```
 #include <istream>
 #include <ostream>
 #include <vector>
 #include <string>
 #include <coil/stringutil.h>
 
 template<typename T>
 std::istream& operator>>(std::istream& is, std::vector<T>& v)
 {
   std::string s;
   std::vector<std::string> sv;
   is >> s;
   sv = coil::split(s ,",");
   v.resize(sv.size());
   for (int i(0), len(sv.size()); i < len; ++i)
     {
       T tv;
       if (coil::stringTo(tv, sv[i].c_str()))
         {
           v[i] = tv;
         }
     }
   return is;
 }
```

このように実装することができます。なお、これはOpenRTM-aist C++版のサンプル、ConfigSampleコンポーネントのソースに含まれるVectorConvert.hです。

これを、bindParameter()が呼ばれるソース(例えば、ConfigSampleコンポーネントであればConfigSample.cpp)、通常はコンポーネントの実装ソースでincludeしてあげれば、コンパイル時にコンパイラが判断して適当な変換関数が利用されます。

#### Javaの場合の変換関数

Javaの場合は、変換関数というものを別途与えるのではなく、コンフィギュレーション変数のホルダクラスにおいて定義されるstringFrom()メソッドに文字列から実際の型への変換を記述します。

以下に、OpenRTM-aist Java版のConfigSampoleで定義されている、カンマ区切り数値列をVector型に変換するための変換関数を示します。

```
 package RTMExamples.ConfigSample;
 
 import java.io.Serializable;
 import java.util.Vector;
 
 import jp.go.aist.rtm.RTC.util.ValueHolder;
 
 public class VectorHolder  implements ValueHolder, Serializable {
 
     /
```
      * Vector型データ設定値
      */
```
     public Vector value = null;
 
     /**
```
      * デフォルトコンストラクタ
      *
      */
```
     public VectorHolder() {
     }
 
     /**
```
      * コンストラクタ
      *
      * @param initialValue　初期値
      *
      */
```
     public VectorHolder(Vector initialValue) {
         value = new Vector(initialValue);
     }
 
     /**
```
      * 文字列からVector型に変換して設定
      *
      * @param def_val　設定値文字列表現
      *
      */
```
     public void stringFrom(String def_val) throws Exception {
         value = new Vector();
         String values[] = def_val.split(",");
         for( int intIdx=0;intIdx<values.length;intIdx++ ) {
             value.add(values[intIdx]);
         }
     }
     /**
```
      * 設定値の取得
      *
 　   * @return 設定値
      *
      */
```
     public Vector getValue(){
         return value;
     }
     /**
```
      * 設定値を文字列に変換
      *
 　   * @return 変換文字列
      *
      */
```
     public String toString(){
         StringBuffer retVal = new StringBuffer();
         while(value.iterator().hasNext()) {
             retVal.append(value.iterator().next());
             if(value.iterator().hasNext()) retVal.append("'");
         }
         return retVal.toString();
     }
 }
```


#### Pythonの場合の変換関数

Python版OpenRTM-aistでは、デフォルトでは基本型とそのリストに対応しており、それ以外の変換が必要なら、bool stringTo(type, string)であるような関数を定義して、bindParameter()の第4引数に関数オブジェクトを渡します。


<!-- ============================================================ -->
## 何をパラメーターにするか？

RTコンポーネントを作成するうえで、何をコンフィギュレーションパラメーターにすればよいのか考えてみましょう。

あるパラメーターがあり、これを外部から変更するにはいくつかの方法が考えられます。
データポートを利用して変更する方法、サービスポートを利用して変更する方法、そしてコンフィギュレーションを利用して変更する方法です。

コンフィギュレーション機能はコンポーネント内部のパラメーターを変更するための機能です。
したがって、ロジック内のパラメーターはコンフィギュレーションパラメーターとして外部から変更できるようにするべきです。
しかし、ある変量をコンフィギュレーションパラメーターにすべきなのかそうでないのか迷うケースもあると思います。
ここではそういったケースについて少し考えてみます。

<!-- ------------------------------------------------------------ -->
### 更新頻度

コンフィギュレーションパラメーターは、通常はシステムが動き出す前に1度だけ、あるいは設定変更が必要になった場合にだけ、外部からパラメーターを与えるために利用します。
更新頻度がシステムのライフサイクル上で1回ないしは数回程度であれば、コンフィギュレーションを使うのがよいでしょう。

また、上記でも述べましたが、コンフィギュレーションはツールやアプリケーションからは文字列として与えられ、コンポーネント内でそれぞれの型に変換します。
変換にはある程度(最近のPCでは数usから数百us程度ですが)時間がかかりますので、例えば1ms周期でデータを送る用途には向きません。
ではそのくらいの頻度でパラメーターを変更できるのでしょうか？実際に使用する際には、パラメーターの数やコンピューター、ネットワークの速度にも依存しますが、数百msまたはそれ以上の頻度では事実上問題なくパラメーターを変更できます。
ただし、そのように周期的に何度も値を変更する必要があるものはデータポートを使うべきでしょう。

<!-- ------------------------------------------------------------ -->
### 更新のタイミング

コンフィギュレーションパラメーターはRTSystemEditorやrtshellなどのツールから、いつでも更新することができます。
しかし、実際に変更されたパラメーターはonExecuteやonActivatedなどの関数で使用する関数内で参照される前にあるタイミングで実際の変数に反映されます。
更新のタイミングは以下の通りです。

<table class="table-alt">
  <tr>
    <td>初期化時</td>
    <td>onInitialize()の直後</td>
  </tr>
  <tr>
    <td>アクティブ化時</td>
    <td>onActivated()が呼ばれる直前</td>
  </tr>
  <tr>
    <td>エラー時</td>
    <td>onError()の直後</td>
  </tr>
  <tr>
    <td>アクティブ状態</td>
    <td>onStateUpdate()の直後 ≒ onExecuteの後、次のonExecute()の直前</td>
  </tr>
</table>

<!-- ------------------------------------------------------------ -->
### データかパラメーターか？

例えば、遠隔地のセンサーから定期的にデータを中央のサーバに送るシステムを考えます。
データは1時間に1回だけ送られ、サーバー側ではそれをログに記録するとします。
このとき、このデータはデータポートを使って送るべきでしょうか？それとも、サービスポートを使うべきか、あるいはコンフィギュレーションを使うべきなのでしょうか？

送られるものはセンサーの<strong>データ</strong>ですので、データポートを利用して送るのが最も適しているといえます。
コンフィギュレーションは外部からパラメーターを<strong>設定</strong>するための仕組みですので、たとえ更新頻度が1時間に一回であっても、このデータをコンフィギュレーションでコンポーネントに伝達するのは不適切といえます。
ただし、データポートでは実現できなクライアントとサーバー側の複雑なやり取り(トランザクション等)を実現したい場合は、サービスポートが使われるかもしれません。

<!-- ------------------------------------------------------------ -->
### サービスかパラメーターか？

データポートにすべきか、コンフィギュレーションにすべきかは、実際にはあまり迷うことはないでしょう。
一方で、RTCロジック内のパラメーターをサービスポートから変更するべきか、コンフィギュレーションパラメーターにすべきか迷う場面は多いと思います。

コンポーネントがある種の典型的かつある程度まとまった機能を提供する場合、その機能はサービスポートのインターフェースによって外部に提供されます。
サービスインターフェースでは、対象の状態を取得したり、設定・モード・パラメーターを変更したりするためのオペレーションを提供します。
状態の取得は別として、設定を行ったり、モード・パラメーターを変更したりする機能はコンフィギュレーションと大変似ています。

結局のところはどちらで設定しても大差ないのですが、対象とするRTCの機能がすでにサービスインターフェースとして定義されていたり、状態の取得と設定が必要になるなど、ある程度複雑な機能を提供する場合、サービスインターフェースを介した操作が適していると言えるでしょう。
それ以外の簡単なパラメーター・モード等の設定にはコンフィギュレーションを利用するとよいでしょう。

<!-- ============================================================ -->
## まとめ

ここでは、コンフィギュレーション機能について定義の仕方や使い方について説明しました。
ロジック内のパラメーターはコンポーネントの再利用性を向上させるために、できるだけこの機能を利用して外部化するべきです。
何をコンフィギュレーションパラメーターにすべきか、すべきでないかといったことについても注意を払う必要があります。
コンフィギュレーション機能を有効に利用すれば、作成するコンポーネントも再利用性の高いものになるでしょう。



