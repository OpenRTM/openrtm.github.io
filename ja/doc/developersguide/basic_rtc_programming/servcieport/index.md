---
layout: page
title: "サービスポート (基礎編)"
---

<!-- Title: サービスポート (基礎編) -->
#contents

このページでは、サービスポートの概要について説明しています。
簡単なサービスポートの設定手順については、以下のページに記載してあります。

- [サービスポートの設定手順]({{ site.baseurl }}/ja/doc/developersguide/basic_rtc_programming/servcieport/tutorial)

## サービスポートとは

ロボットシステムをコンポーネント指向で構築するためには、コンポーネント間のデータ通信だけでは十分ではなく、コマンドレベル(あるいは関数レベル)のコンポーネント間通信が必要になってきます。
例えば、ロボットアームを制御するマニピュレータコンポーネントの場合、手先の位置や速度などは、上位のアプリケーションやコンポーネントからデータポートで送られるべきデータです。

一方、ロボットアームの各種設定、座標系の設定、制御パラメーターの設定、動作モードの設定、などをデータポートで行うのは適切とは言えず、オブジェクト指向的にいえば、マニピュレータオブジェクトに対して、
setCoordinationSystem()、setParameter()、setMode() などの関数が用意されていて、これらの関数を必要に応じて適切なタイミングで呼ぶのが自然といえます。

<div align="center"><a href="serviceport_example_ja.png"><img src="serviceport_example_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスポートの例</strong></div>

サービスポートはこのようなコマンドレベルのコンポーネント間のやり取りを行うための仕組みを提供します。

一般にサービスとは、機能的に関連のあるひとまとまりのコマンド (関数、メソッド、オペレーションなどとも呼ばれます) 群であり、OpenRTM-aistにおいては、この機能を提供する側をサービスプロバイダ(インターフェース)、機能を利用する側をサービスコンシューマ(インターフェース)と呼びます。

なお、UML等の規約においては、サービスプロバイダを Provided Interface、またサービスコンシューマを Required Interface などと呼び、それぞれ下図のような記号 (ロリポップ (lollipop) 、ソケット (socket) ) で表します。
これは、一般的な用語および記述法なので覚えておいた方がよいでしょう。呼ぶあるいは呼ばれる方向でいえば、呼ばれるものがプロバイダ (Provided Interface) であり、呼ぶものがコンシューマ (Required Interface) という見方もできます。

<div align="center"><a href="provider_and_consumer_ja.png"><img src="provider_and_consumer_ja.png" width="40%;"></a></div>
<div align="center"><strong>プロバイダとコンシューマ</strong></div>

- プロバイダ (Provided Interface): 呼ばれる側、サービスを提供する側
- コンシューマ (Required Interface): 呼ぶ側、サービスを利用する側 

プロバイダおよびコンシューマをまとめてインターフェースまたは、サービスインターフェースと呼び、これらサービスインターフェースを持つポートをサービスポートと呼びます。

## サービスポートとインターフェース

サービスインターフェースとサービスポートの関係について詳しく説明します。

<div align="center"><a href="component_port_interface_ja.png"><img src="component_port_interface_ja.png" width="40%;"></a></div>
<div align="center"><strong>コンポーネント、ポート、インターフェース</strong></div>

ポートとはコンポーネントに付属し、コンポーネント間の接続の端点となる部分を指します。コンポーネント間の接続とは、コンポーネントに付属するポート間で接続に関する調停が行われ、何らかの相互作用 (データやコマンドのやり取り) が行える状態にすることを意味します。

ポート自体はデータやコマンドのやり取りに対して、何の機能も提供しません。実際にコマンドのやり取りを行うのはサービスインターフェース (プロバイダとコンシューマ) になります。
一般的にポートには機能的に関連のある任意の数の任意の方向のインターフェースを付加することができます。これにより、コマンドのやり取りを一方向だけでなく双方向にすることもできます。

コンシューマとプロバイダは、ポートが接続されたときに、ある条件に基づいて接続され、コンシューマからプロバイダの機能を呼び出すことが可能になります。
コンシューマとプロバイダを接続するためには、両者の**型**が同じ、または互換性がある必要があります。

同じ型である、とは同一のインターフェース定義を持つことであり、互換性があるとは、プロバイダのインターフェースがコンシューマのインターフェースのサブクラスの一つである、(逆にいえば、コンシューマのインターフェースがプロバイダのインターフェースのスーパークラスの一つである)ということになります。


### サービスポート

RTコンポーネントはデータポート同様、任意の数のサービスポートを持つことができます。また、サービスポートには、任意の種類、数のプロバイダまたはコンシューマを付加することができます。

以下は、OpenRTM-aistのサンプルコンポーネント MyServiceProvider から抜粋したポートとプロバイダの登録のためのコードです。

```
 RTC::ReturnCode_t MyServiceProvider::onInitialize()
 {
   // Set service provider to Ports
   m_MyServicePort.registerProvider("myservice0", "MyService", m_myservice0);
   
   // Set CORBA Service Ports
   addPort(m_MyServicePort);
   
   return RTC::RTC_OK;
 }
```

m_MyServicePort.registerProvider() でプロバイダをサービスポートオブジェクト m_MyServicePort に登録しています。第3引数が実体であるプロバイダオブジェクトです。
次に、コンポーネントのフレームワーククラスである RTObjectクラスのaddPort() 関数で、ポートをコンポーネントに登録しています。

同様に、サンプルコンポーネント MyServiceConsumer から抜粋したコードを示します。

```
 RTC::ReturnCode_t MyServiceConsumer::onInitialize()
 {
   // Set service consumers to Ports
   m_MyServicePort.registerConsumer("myservice0", "MyService", m_myservice0);
   
   // Set CORBA Service Ports
   addPort(m_MyServicePort);
 
   return RTC::RTC_OK;
 }
```

プロバイダの場合とほとんど同じで、m_MyServicePort.registerConsumer() 関数でコンシューマをポートに登録し、そのポートを addPort() 関数でコンポーネントに登録しています。

以上、特に説明もなしに、それぞれ m_myservice0 というオブジェクトが、プロバイダ、またはコンシューマであるとしてコード例を示しましたが、以下、これらのインターフェースがどのように定義され、オブジェクトがどのように実装されるかを説明していきます。

### インターフェース定義

インターフェースとは何でしょうか？ C++であれば、純粋仮想クラスをインターフェースと呼んだりしますし、Java は言語レベルで interface キーワードが用意されています。

OpenRTM-aist には、言語や OS に依存しない、ネットワーク透過であるといった特徴がありますが、これは CORBA と呼ばれる分散オブジェクトミドルウエアを利用することにより実現されています。
CORBAは、国際標準化団体OMGで標準化されている分散オブジェクトミドルウエアで、標準に従って、多くの会社や団体、個人などが多様な実装を提供しています。

OpenRTM-aistでは、インターフェースは IDL と呼ばれる CORBA のインターフェース定義言語によって定義します。この IDL は言語に依存しないインターフェース定義方法を提供し、また IDL コンパイラと呼ばれるスタブやスケルトンを生成ツールを利用することで、各種言語に対応したコードが自動的に生成されます。スタブとは、リモートのオブジェクトを呼び出すためのプロキシオブジェクトのためのコードであり、スケルトンとは、プロバイダを実装するためのベースとなるコードです。

これら自動生成されるコードのおかげで、異なる言語同士の呼び出しもシームレスに行うことができます。例えば、C++で実装されたプロバイダを、Python や Java 等で容易に呼び出すことができるのです。

以下は、OpenRTM-aist のサンプルで使用されている IDL 定義です。

```
 module SimpleService {
   typedef sequence<string> EchoList;
   typedef sequence<float> ValueList;
   interface MyService
   {
     string echo(in string msg);
     EchoList get_echo_history();
     void set_value(in float value);
     float get_value();
     ValueList get_value_history();
   };
 };
```

module とは C++ で言うところの名前空間のようなもので、これによりインターフェース名を修飾し衝突を防ぐことができます。

C言語等と同様に typedef キーワードがあります。上の例では、sequence と呼ばれる動的配列型を定義しています。
一つは、string (文字列型) 型のリストとして、EchoList 型、もうひとつは float 型のリストとして ValueList 型を定義しています。
特に sequence 型は、typedef せずに、定義中で直接使うことができないので、このように予め typedef しておく必要があります。

次に interface で始まる部分が実際のインターフェースの定義になります。
MyService インターフェースには、5つの関数 (IDLではオペレーションと呼びます) が定義されています。
ほとんどは、C言語やJavaなどと同じような定義ですが、IDL では引数が入力であるか出力であるかを明確にするために、引数宣言の前に、**in**, **out** または **inout** の修飾子が付きます。

### IDL コンパイル

図に、IDL 定義から IDL コンパイル、プロバイダの実装およびスタブの利用の流れを示します。

<div align="center"><a href="idlcompile_stub_skel_ja.png"><img src="idlcompile_stub_skel_ja.png" width="40%;"></a></div>
<div align="center"><strong>IDLコンパイルとスタブ、スケルトン</strong></div>

定義された IDL を IDL コンパイラに与えてコンパイルを行うと、通常スタブとスケルトン (またはサーバーとクライアントという呼び方をする場合もある) のためのコードが生成されます。

クライアント、すなわちサービスを利用する側は、スタブコードをインクルードするなどして、スタブとしてい定義されているプロキシ(代理)オブジェクトを利用して、リモートにある、サーバーの機能にアクセスします。以下に C++ でのコード例を示します。

```
 MyService_var mysvobj = <何からの方法でリモートオブジェクトの参照を取得>
 Retval retval = mysvobj->myoperation(argument);
```

MyService_var というのが、プロキシオブジェクトのための宣言です。
mysvobjにリモートオブジェクトの参照を何らかの形で代入すると、その下で行われている myoperation() 関数の呼び出しは、実際にはリモートに存在するオブジェクトにおいて行われます。
このMyService_var クラスが定義されているのがスタブにあたります。

一方、上記の方法によって実際に呼ばれるサーバー側のオブジェクトは、以下のようにスケルトンクラスを継承して以下のように実装されます。

```
 class MyServiceSVC_impl
```
   : public virtual MyService,
```
     public virtual PortableServer::RefCountServantBase
 {
 public:
    MyServiceSVC_impl() {};
    virtual ~MyServiceSVC_impl() {};
    Retval myoperation(ArgType argument)
    {
      return do_ something(argument);
    }
 };
```

さらに、ここで定義されたサーバントクラスをインスタンス化し、CORBA オブジェクトとしてアクティベートすることで、リモートからオペレーションを呼び出すことができます。

```
 // CORBAのORB等を起動するためのいろいろなおまじない
 MyServiceSVC_impl mysvc;
 POA->activate_object(id, mysvc);
```

IDL を定義して、コンパイルすることで、分散オブジェクトを定義し利用するのに必要な大半のコードが自動的に生成されます。
ただし、上記の「何らかの方法でリモートオブジェクトの参照を取得」したり、「CORBA の ORB を起動するためのいろいろなおまじない」といったものは、CORBA を直接利用する場合には依然としてコーディングする必要がある部分であり、これらは CORBA を利用するうえでも理解が難しかったり、煩雑な作業が必要となる部分です。

しかしながら、OpenRTM-aist を利用すれば、こうした CORBA の様々な呼び出しの大半は隠蔽され、実装者はクライアントの呼び出し、サーバントの実装にのみ集中することができます。以下では、サーバントを実装しプロバイダとしてコンポーネントに登録する方法、コンシューマとしてプロバイダを利用する方法について詳しく見ていきます。

## サービスポートの実装

サービスポートの実装に当たっては、RTCBuilder を利用するのが便利です。
自分でサービスポート、プロバイダおよびコンシューマを実装することもできますが、CORBA や IDL コンパイラに精通している必要がありますし、Makefile やコードの様々な部分を書き換える必要がありますのであまりお勧めできません。

RTCBuilder の詳細な使い方は、RTCBuilder のマニュアルを参照してください。

### IDL 定義

サービスポートを利用するには、利用するインターフェースを予め IDL で定義するか、既存の IDL ファイルを適当なディレクトリーに配置しておく必要があります。

IDL の定義方法については、ここでは詳細は述べませんが、おおよそ以下のようなフォーマットで定義することができ、C言語や Java に慣れた読者であれば、比較的容易に定義できるでしょう。

```
 // 名前空間のためにモジュールを定義することができる。
 // モジュール定義は積極的に利用することが推奨される。
 module <モジュール名>
 {
   // 構造体を定義することができる。
   struct MyStruct // 構造体名
   {
     short x; // int型は short と longの み利用可能
     short y;
     long  a;
     long  b;
     double dval; // 浮動小数点型は float と double のみ利用可能
     float fval;
     string strval; // 文字列のために string が利用可能
   };
 
   // 動的配列 sequence 型は予め typedef する必要がある
   typedef sequence<double> DvalueList;
   typedef sequence<MyStruct> MyStructList; // 任意の構造体もsequence型にできる
 
   // インターフェース定義
   interface MyInterface // インターフェース名
   {
     void op1(); // 戻り値なし、引数なしの場合
 
     // NG: 大文字・小文字を区別しない言語では以下の定義が問題になるため IDLではエラーになる
     // short op2(in MuStruct mystruct);
     short op2(in MyStruct mydata); // 引数は {in, out, inout} で方向を指定
 
     oneway void op3(); // 戻り値なしのオペレーションは onway キーワードが利用可能
 
     void op4(in short inshort, out short outshort, inout short ioshort);
 
     void op5(MyInterface myif); // MyInterface 自身を引数に利用することも可能
   };
 
   // 同一の IDL ファイルに複数の interface を定義することも可能
   interface YourInterface
   {
     void op1();
   };
 };
```


### RTCBuilder による設計

上のように IDL で定義したインターフェースを、これから開発する RTコンポーネントのサービスポートのプロバイダ、もしくはコンシューマとして用いるためには、コンポーネントのコードジェネレータである RTCBuilder でサービスポートを設計し、その際にこの IDL 定義を与えてやる必要があります。

RTCBuilder の新規プロジェクトを作成し、パースペクティブを開きます。各種プロファイル(コンポーネントの名称やカテゴリ名)等、必要な設定を行った後、サービスポートタブを開くと、次のような画面が表示されます。

<div align="center"><a href="rtcbuilder_serviceport_tab1_ja.png"><img src="rtcbuilder_serviceport_tab1_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスポート設計タブ</strong></div>

まず、[Add Port] ボタンをクリックし、サービスポートを一つ追加します。そうすると、sv_name というサービスポートが一つ追加され、下の BuildView のコンポーネントの箱に、小さな正方形のポートが一つ追加されます。RTCBuilder のエディタ左のポートリストの sv_name をクリックすると、右側に**RT-Component Service Port Profile**が表示されるので、ポート名を適当な名前 (ここでは**MyServiceProviderPort**) に変更します。

<div align="center"><a href="rtcbuilder_serviceport_tab2_ja.png"><img src="rtcbuilder_serviceport_tab2_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスポートの追加</strong></div>

エディタ左のポートリストの MyServiceProviderPort をクリックし、[Add Interface] ボタンをクリックすると、MyServiceProviderPort にインターフェース **if_name** が一つ追加されますので、先ほどと同様にエディタ左の**if_name**をクリックし、**RT-Component Service Port Interface Profile**上で**if_name**を適当な名前 (ここでは MyServiceProvider) に変更します。下の BuildeView では、正方形のポートにロリポップが追加され、プロバイダ (Provided Interface) がポートに付加されたことが視覚的に分かります。

<div align="center"><a href="rtcbuilder_serviceport_tab3_ja.png"><img src="rtcbuilder_serviceport_tab3_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスインターフェース(プロバイダ)の追加</strong></div>

エディタ右側の Interface Profile では、インターフェースのプロファイルを設定します。例えば**方向**のドロップダウンリストでは、対象のインターフェースがプロバイダ (Provided) かコンシューマ (Required) かを指定します。

<div align="center"><a href="rtcbuilder_direction_ddown_ja.png"><img src="rtcbuilder_direction_ddown_ja.png" width="70%;"></a></div>
<div align="center"><strong>サービスインターフェースの「方向」の設定</strong></div>

ここではプロバイダを追加しようとしているので、Provided のままにします。このほか、インスタンス名、変数名なども指定できますが、必須ではありません。インスタンス名は、接続時にプロバイダとコンシューマのインスタンス名が同じなら、対応関係を指定しなくてもポートの接続を自動的に行う場合に利用されます。

<div align="center"><a href="serviceif_autoconnection_ja.png"><img src="serviceif_autoconnection_ja.png" width="50%;"></a></div>
<div align="center"><strong>サービスインターフェースのインスタンス名と自動接続</strong></div>

ただし、インスタンス名が異なっていても、接続時に任意のインターフェース同士を接続できるので、入力は必須ではありません。
また、変数名はコードを生成した際にプロバイダオブジェクトを代入する変数名を指定するための項目ですが、これもインターフェース名から自動的に生成されるので、入力は任意Ωです。

次に IDL の指定と、インターフェース型の指定を行います。上で定義したような IDL を適当なディレクトリに配置し、IDL ファイル指定ボックス横の [Browse] ボタンをクリックし、対象となる IDL を指定します。すると、指定された IDL で定義されたインターフェースが、その下のインターフェース型のドロップダウンリストに現れます。このドロップダウンリストで、このポートに付加したインターフェース名を選択します。IDL ファイルに文法エラーなどがある場合には、ドロップダウンリストに希望するインターフェースが現れません。再度 IDL ファイルの定義をチェックしてください。

<div align="center"><a href="rtcbuilder_interfacetype_ddwon_ja.png"><img src="rtcbuilder_interfacetype_ddwon_ja.png" width="70%;"></a></div>
<div align="center"><strong>インターフェース型の選択</strong></div>

なお、上述の<strong>方向</strong>ドロップダウンリストで <strong>Required</strong>を指定すると、このインターフェースはコンシューマになります。
以下は別のコンポーネント<strong>MyServiceConsumer</strong> のサービスポートとインターフェースの設定画面の例です。

<div align="center"><a href="rtcbuilder_serviceport_tab4_ja.png"><img src="rtcbuilder_serviceport_tab4_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスインターフェース(コンシューマ)の追加</strong></div>

エディタ下の BuildView においてポートにソケットが追加されて、コンシューマ (Required interface) がポートに付加されたことが視覚的に分かります。

### サービスプロバイダの実装

プロバイダというのは文字通り、サービスをプロバイド(提供)するためのインターフェースです。したがって、IDL で定義したインターフェースを持つサービスの中身を実装する必要があります。

プロバイダインターフェースを持つコンポーネントを RTCBuilder で設計した場合、コード生成を行うと、コンポーネントのソースのひな形とともに、例えばC++の場合には、<サービスインターフェース名>SVC_impl.cpp と <サービスインターフェース名>SVC_impl.h という、プロバイダの実装コードのひな形も生成されます。

<div align="center"><a href="rtcbuilder_svcimpl_cxxsrc_ja.png"><img src="rtcbuilder_svcimpl_cxxsrc_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスプロバイダ実装ファイル (C++,Python,Java)</strong></div>

以下に、各言語で生成されるプロバイダの実装のひな形コードのファイル名を示します。

hogehogehoge

<div align="center"><a href="rtcbuilder_svcimpl_pysrc_ja.png"><img src="rtcbuilder_svcimpl_pysrc_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスプロバイダ実装ファイル (Python)</strong></div>

<div align="center"><a href="rtcbuilder_svcimpl_javasrc_ja.png"><img src="rtcbuilder_svcimpl_javasrc_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスプロバイダ実装ファイル (Java)</strong></div>

これらの実装のひな形には、IDLで定義されたインターフェースに相当するクラスがあらかじめ定義されています。

ここでは、C++での実装方法を例にとり、IDLで定義されたオペレーションのいくつかを実装していきます。

#### echo()関数の実装

はじめに、echo() メンバ関数を見てみます。

```
 /*
  * Methods corresponding to IDL attributes and operations
  */

 char* MyServiceSVC_impl::echo(const char* msg)
 {
   // Please insert your code here and remove the following warning pragma
 #ifndef WIN32
   #warning "Code missing in function <char* MyServiceSVC_impl::echo(const char* msg)>"
 #endif
   return 0;
 }
```

#warning プリプロセッサディレクティブがありますが、これは gcc でコンパイルした際にこの関数が実装されていないことを警告するためのものですので、#ifndefごと削除します。

```
 char* MyServiceSVC_impl::echo(const char* msg)
 {
   return msg;
 }
```

また、この関数は、echo() 関数の引数に与えられた文字列を、単に呼び出し側に返すだけの機能を提供するとします。したがって、以下のように実装すればよいように思えます。

```
 char* MyServiceSVC_impl::echo(const char* msg)
 {
   return msg;
 }
```

しかし、これはコンパイル時にエラーになります。const char* を char* に渡しているためです。また、CORBA のオブジェクトの実装方法としても間違っています。CORBAでは、return で返されるオブジェクトは、ORB (Object Request Broker、リモートオブジェクトの呼び出し部分を司る部分、CORBAのコア) によって解体されるというルールがあるためです。(return時にはオブジェクトの所有権を放棄する、とも言います。)

したがって、return には、別途領域を確保し、msg の内容をコピーした文字列を返す必要があります。これに従えば、以下のように実装すればよいように思うかもしれません。

```
 char* MyServiceSVC_impl::echo(const char* msg)
 {
   char* msgcopy;
   msgcopy = malloc(strlen(msg));
   strncpy(msgcopy, msg, strlen(msg));
   return msgcopy;
 }
```

ここでは、malloc で領域を確保していますが、ORB は free で領域を解体するのか、delete で解体するのかはわかりません。
実は、CORBA ではオブジェクト(構造体や配列、またその複合型等も含む)や文字列を扱うための方法が別途定められていて、それに従って関数の引数を受け取ったり、返したりする必要があるのです。

CORBA で定められた方法に従うと、echo() 関数は以下のように実装する必要があります。

```
 char* MyServiceSVC_impl::echo(const char* msg)
 {
   CORBA::String_var msgcopy = CORBA::string_dup(msg);
   return msgcopy._retn();
 }
```

関数内の1行目では、CORBA の文字列クラス CORBA::String のスマートポインタである CORBA::String_var 型を宣言しています。String_var 型はいわゆる所有権を管理するためのスマートポインタで STL の auto_ptr に似ています。

```
 CORBA::String_var msgcopy = CORBA::string_dup(msg);
```

この String_var 型の変数 msgcopy に引数の msg に格納されている文字列をコピーしているのが CORBA::string_dup() 関数です。この関数では引数に与えられた文字列を格納するのに十分なメモリー領域を確保し、その領域に引数の文字列をコピーしています。

次の行では、return で呼び出し元に msgcopy 内の文字列を返しつつ、オブジェクトの所有権を放棄、return 側に所有権を移譲しています。下図に示すように ORB では、return で返された文字列を、ネットワーク上の呼び出し元に送信してから、文字列オブジェクトを解放します。

<div align="center"><a href="serviceport_orb_and_provider_ja.png"><img src="serviceport_orb_and_provider_ja.png" width="50%;"></a></div>
<div align="center"><strong>ORBとオペレーション呼び出し、メモリ管理の関係</strong></div>

このルールをよく理解すると、msgcopy オブジェクトが echo() 関数内で使用されていないことから、echo() 関数の実装は最終的には以下のようにも書くこともできます。

```
 char* MyServiceSVC_impl::echo(const char* msg)
 {
   return CORBA::string_dup(msg);
 }
```

CORBA::string_dup() 関数で文字列領域の確保と内容のコピーを行ったうえで、その所有権を直に呼び出し元に与えていることになります。

このように、サービスプロバイダは CORBA のオブジェクトですので、その実装方法は通常の C++ の実装とは少し違ったやり方で行う必要があります。
特に、関数の引数および返り値の受け渡し規則は、少し複雑なように見えます。ただし、上記のように、オブジェクトの所有権という考え方を念頭において考えると、引数をどのように受け取るべきなのか、あるいは返り値をどのように返すべきなのかが自ずと明らかになります。
詳細については、Appendix や他の CORBA の参考書等を参考にしてください。


#### set_value(), get_value() と get_value_history()

次は、set_value() 関数, get_value() 関数および get_value_list() 関数を同時に実装していきます。
これらの関数は、set_value() で設定されたfloat型の値を保存しておき、get_value()でその値を返すという単純なものです。
また、get_value_history() では、今までにセットされた値の履歴を保存しておき、履歴をリストとして返すというものです。

まず、値を保存しておく変数を用意します。現在の値は MyServiceSVC_impl クラスに CORBA::Float 型 の private メンバーとして用意します。
一方、get_value_history() では、戻り値にSimpleService::ValueList という CORBA のシーケンス型が使われているので、これをメンバー変数として持つようにします。
これらの変数宣言を MyServiceSVC_impl.h の MyServiceSVC_impl クラス定義の最後の方に以下のように追加します。

```
 class MyServiceSVC_impl
```
   : public virtual POA_SimpleService::MyService,
```
    public virtual PortableServer::RefCountServantBase
 {
```
   : (中略)
```
 private:
   CORBA::Float m_value; // この行を追加する
   SimpleService::ValueList m_valueList; // この行を追加する
   };
```

変数の初期化も忘れずに行います。MyServiceSVC_impl.cpp のコンストラクタ
で、m_value は 0.0に、m_valueList は長さ0に初期化しておきます。

```
 MyServiceSVC_impl::MyServiceSVC_impl()
```
 : m_value(0.0), m_valueList(0)
```
 {
   // Please add extra constructor code here.
 }
```

次に、set_value() 関数を実装します。引数に与えられた数値をメンバ変数 m_value に代入するとともに、m_valueListにも追加します。
CORBA のシーケンス型は、動的配列型で、[]オペレータとともに、length()、length(CORBA::ULong) の関数を利用することができます。length() 関数は、現在の配列の長さを返し、length(CORBA::ULong) 関数は現在の配列の長さを設定します。
実装は以下のようになります。

```
 void MyServiceSVC_impl::set_value(CORBA::Float value)
   throw (CORBA::SystemException)
 {
   m_value = value; // 現在値
 
   CORBA::ULong len(m_valueList.length()); // 配列の長さを取得
   m_valueList.length(len + 1); // 配列の長さを1つ増やす
   m_valueList[len] = value; // 配列の最後尾にvalueを追加
 
   return;
 }
```

echo() 関数とは異なり、CORBA::Long 型は C++のlong int と等価で、オブジェクトの所有権、領域確保や廃棄等は考える必要はありません。
したがって、上記のように単純な代入で構いません。また、配列型は、2種類の length() 関数と []オペレータを利用して、配列の長さを1つ増やして最後尾に引数の値を代入しています。
なお、OpenRTM-aistでは、CORBA のシーケンス型を STL の vector に近い形で利用するための関数テンプレートを提供しており、それを使うと、

```
 void MyServiceSVC_impl::set_value(CORBA::Float value)
   throw (CORBA::SystemException)
 {
   m_value = value; // 現在値
   CORBA_SeqUitl::push_back(m_valueList, value);
 
   return;
 }
```

のように書くことができます。CORBA_SeqUtil.h では、 for_each()、find()、push_back()、insert()、front()、back()、erase()、clear() といった関数が定義されています。

get_value() は以下のようになります。

```
 CORBA::Float MyServiceSVC_impl::get_value()
   throw (CORBA::SystemException)
 {
   return m_value;
 }
```

保存された値を return で呼び出し元に返すだけです。ここでも、先ほどの echo() の例とは異なり、CORBA::Float がプリミティブ型なので所有権等を考慮する必要はありません。

最後に、get_value_history() の実装を見ていきます。値の履歴が格納された m_valueList を返せばいいだけのように思えますが、先ほどの述べた所有権と領域の解放の問題があるため、以下のように実装する必要があります。

```
 SimpleService::ValueList* MyServiceSVC_impl::get_value_history()
   throw (CORBA::SystemException)
 {
   SimpleService::ValueList_var vl;
   vl = new SimpleService::ValueList(m_valueList);
   return vl._retn();
 }
```

関数内1行目では、シーケンス型オブジェクトのためのスマートポインタである、SimpleService::valueList_var 型の変数を宣言しています。さらに次の行で、このスマートポインタに対して、コピーコンストラクタを呼び出してそのポインタを代入しています。
これにより、領域の確保と、値のコピーが同時に行われます。最後に、vl._retn() で、vl が保持しているシーケンス型のオブジェクトの所有権を放棄して、return 側にオブジェクトを渡しています。

そして、vl は関数内で使用されていないので、以下のように書くこともできます。

```
 SimpleService::ValueList* MyServiceSVC_impl::get_value_history()
   throw (CORBA::SystemException)
 {
   return new SimpleService::ValueList(m_valueList);
 }
```


以上、プロバイダの実装についてみてきましたが、プロバイダがいわゆる CORBA オブジェクトであるので、使用する型、変数の受け渡しの仕方など、CORBA のルールに従って実装しなければなりません。
はじめは煩わしく感じるかもしれませんが、プリミティブ型については従来通りの実装、複雑なオブジェクトについてはメモリーの確保と解放がどこで行われるか、所有権はどちらにあるかを理解すると、どのように実装するべきなのか理解できると思います。


### サービスコンシューマの実装

コンシューマでは、上で実装したサービスプロバイダを呼び出し、その機能を利用することになります。コンシューマを持つコンポーネントのひな形コードを RTCBuilder で生成した場合には、プロバイダの場合とは異なり特別なファイルは生成されません。

その代わり、コンポーネントのヘッダに以下のようなプロバイダのプレースホルダであるコンシューマオブジェクトが宣言されます。

```
      : (中略)
   // Consumer declaration
   // <rtc-template block="consumer_declare">
   /*!
    */
   RTC::CorbaConsumer<SimpleService::MyService> m_MyServiceConsumer;
 
   // </rtc-template>
 
  private:
      : (中略)
```

これは、RTC::CorbaConsumer クラステンプレートに型引数 SimpleService::MyService を与えて、MyService 型のコンシューマを宣言していることになります。
また、実装ファイルの方では、onInitialize() 関数において、コンシューマのポートへの登録と、ポートのコンポーネントへの登録が行われていることが確認できます。

```
 RTC::ReturnCode_t MyServiceConsumer::onInitialize()
 {
   : (中略)   
  // Set service consumers to Ports
   m_MyServiceConsumerPortPort.registerConsumer("MyServiceConsumer",
                                                "SimpleService::MyService",
                                                m_MyServiceConsumer);
  
   // Set CORBA Service Ports
   addPort(m_MyServiceConsumerPortPort);
   // </rtc-template>
 
   return RTC::RTC_OK;
 }
 
```

ヘッダで宣言されていた m_MyServiceConsumer 変数が、registerConsumer() メンバ関数によってポートに登録されていることが分かります。
第1引数では、このコンシューマの「インスタンス変数」が、第2引数ではコンシューマの「インターフェース型」が、そして第3引数ではコンシューマのインスタンスである m_MyServiceConsumer 変数がそれぞれ与えられています。
これによって、コンシューマがインスタンス名、型名ともにポートに関連付けられていることになります。


コンシューマ m_MyServiceConsumer は上でも述べたように、プロバイダのプレースホルダになっています。
C++では、オブジェクトへのポインタのように扱うことができます。

MyService インターフェースでは、string 型 (CORBAのstring型) 引数を一つ取る echo() オペレーションが定義されていました。
したがって、例えば以下のように echo() 関数を呼び出すことができます。

```
 m_MyServiceConsumer->echo("Hello World");
```

C++ では上のようにポインタ、Java や Python では参照のように、オペレーションを呼び出すことができるのです。

さて、ここで勘の良い方は、ポインタまたは参照の指す先は一体どうなっているんだとお思いでしょう。C++等でも、例えば以下のようなコードは segmentation fault で即座に落ちます。

```
 class A {
 public:
   const char* echo(const char* msg) {
     std::cout << msg << std::endl;
     return msg;
   }
 };
 
 int main (void) {
   A* a;
   a->echo("Hello World!!");
 }
```

a は null ポインタですので、何もオブジェクトを指していません。これと同様に、上の m_MyServiceConsumer も、コンポーネントの起動直後には、いかなるオブジェクトも指していませんので、当然オペレーションを呼び出すことができません。
上記の class A の場合では、

```
 int main (void) {
   A* a;
   a = new A();
   a->echo("Hello World!!");
 }
```

オブジェクトを new で生成して、変数 a に代入してあげれば a はその時点であるオブジェクトを指し示す正当なポインタですので、class Aのメンバ関数である echo() を呼ぶことができます。

しかしながら、コンポーネント内のコンシューマが呼び出したいのは、ネットワーク上のどこかにあるオブジェクトのオペレーションです。
したがって、m_MyServiceConsumer が指し示すのはリモートオブジェクトの参照 (CORBAオブジェクト参照(リファレンス)) です。

実は下図に示すように、コンシューマはそのポートがプロバイダを持つポートと接続されるときに、対応するオブジェクト参照を受け取ります。
接続によりコンシューマは正当なオブジェクトを指すことになり、こうして初めてオペレーションを呼び出すことができるのです。

hogehogee

<div align="center"><a href="serviceport_connection_and_reference_ja.png"><img src="serviceport_connection_and_reference_ja.png" width="40%;"></a></div>
<div align="center"><strong>サービスポートの接続とオブジェクト(参照)リファレンス</strong></div>

接続後は(相手のポートに適当なプロバイダが存在すれば)コンシューマのオペレーションを呼び出すことができますが、接続していない場合、または有効な参照がセットされていない場合は、コンシューマオブジェクトは例外を投げます。
そして、コンシューマを利用する場合、いつ接続が行われるか、またいつ接続が切断されるかは分かりませんので、常にこの例外を捕捉して適切に処理する必要があります。

```
 try
 {
   m_MyServiceConsumer->echo("Hello World!!");
 }
 catch (CORBA::SystemException &e)
 {
   // 例外捕捉時の処理
      std::cout << "ポートが接続されていません"" << std::endl;
 }
 catch (...)
 {
   // その他の例外
 }
```

なお、onExecute() メンバ関数内で例外が発生し、関数内部で捕捉されなかっ
た場合、RTC はエラー状態へ遷移します。

以上を踏まえて、MyServiceConsumer コンポーネント実装します。この例では、onExecute() でユーザーからの入力待ちを行い、各オペレーションに対応したコマンドを受け取り、コマンドに応じてリモートのプロバイダのオペレーションを呼び出し結果を返すといった簡単なものです。

では、まずユーザーに利用できるコマンドを提示する部分からみていきます。

RTC::ReturnCode_t MyServiceConsumer::onExecute(RTC::UniqueId ec_id)
{
```
  try
    {
      std::cout << std::endl;
      std::cout << "Command list: " << std::endl;
      std::cout << " echo [msg]       : echo message." << std::endl;
      std::cout << " set_value [value]: set value." << std::endl;
      std::cout << " get_value        : get current value." << std::endl;
      std::cout << " get_echo_history : get input messsage history." << std::endl;
      std::cout << " get_value_history: get input value history." << std::endl;
      std::cout << "> ";
      
      std::string args;
      std::string::size_type pos;
      std::vector<std::string> argv;
      std::getline(std::cin, args);
```

まず、上で述べたようにコンシューマが発する例外を捕捉するためにtry節で囲みます。
利用可能なコマンドリストを表示して、ユーザの入力をgetline()関数で受け取っています。

```
      
      pos = args.find_first_of(" ");
      if (pos != std::string::npos)
        {
          argv.push_back(args.substr(0, pos));
          argv.push_back(args.substr(++pos));
        }
      else
        {
          argv.push_back(args);
        }
```

これらのコマンドのうち、引数を取るものは echo と set_value だけで、かつこれらのコマンドは引数を一つだけとります。
受け取った文字列を最初の空白で分割し、argv[0] = コマンド、argv[1] = 引数として string の vector に格納します。
echo, set_value コマンドでは argv[1] を引数として利用し、他のコマンドでは単純に無視することにします。

```
        
      if (argv[0] == "echo" && argv.size() > 1)
        {
          CORBA::String_var retmsg;
          retmsg = m_myservice0->echo(argv[1].c_str());
          std::cout << "echo return: " << retmsg << std::endl;
          return RTC::RTC_OK;
        }
```

echo コマンドの実装です。argv[0] が  <strong>echo</strong> の場合、argv[1] を引数にして echo() 関数を呼び出します。
echo() のCORBAのstring型の戻り値を受け取るための変数として、retmsg を宣言しています。
echo() の戻り値の所有権はこちら側にあるので、受け取った後に適切に領域を解放する必要があるのですが、String_var 型のスマートポインタを利用すると、不要になった時点で適切に領域解放を行ってくれます。
戻り値を表示して、return RTC::RTC_OK としてonExecute() 関数を抜けています。

```
        
      if (argv[0] == "set_value" && argv.size() > 1)
        {
          CORBA::Float val(atof(argv[1].c_str()));
          m_myservice0->set_value(val);
          std::cout << "Set remote value: " << val << std::endl;
          return RTC::RTC_OK;
        }
```

set_value コマンドの実装です。引数 argv[1] の文字列を CORBA::Float 型に変換して、set_value() オペレーションの引数に与えています。

```
        
      if (argv[0] == "get_value")
        {
          std::cout << "Current remote value: "
                    << m_myservice0->get_value() << std::endl;
          return RTC::RTC_OK;
        }
```

get_value コマンドは set_value コマンドで設定した値を取得します。
get_value() オペレーションは、戻り値が CORBA::Float で値渡しのためオブジェクトの所有権などは特に考えなくとも構いません。
ここでは、戻り値をそのまま std::cout でコンソールに表示させています。

```
      if (argv[0] == "get_echo_history")
        {
          EchoList_var elist = m_myservice0->get_echo_history();
          for (CORBA::ULong i(0), len(elist.length(); i <len; ++i)
          {
            std::cout << elist[i] << std::endl;
          }
          return RTC::RTC_OK;
        }
```

get_echo_history コマンドでは、get_echo_history() の結果を受け取り、それまで echo コマンドで引数に与えられた文字列のリストを返しています。
get_echo_history() 関数の戻り値は CORBA のシーケンス型である EchoListです。
シーケンス型についてもスマートポインタである _var 型が定義されていますので、これを利用します。
配列の長さを取得するための length() 関数が利用できるので、長さを調べて for 文ですべての要素を表示しています。
シーケンス型の_var型では、上記のように[]オペレータを利用して C言語の配列のように各要素にアクセスできます。

```
      if (argv[0] == "get_value_history")
        {
          ValueList_var vlist = m_myservice0->get_value_history();
          for (CORBA::ULong i(0), len(vlist.length()); i < len; ++i)
          {
            std::cout << vlist[i] << std::endl;
          }
          return RTC::RTC_OK;
        }
```

最後に、get_value_history コマンドです。get_value_history() オペレーションを呼び出し、これまで設定された値のリストを表示します。
get_value_hitory() 関数の戻り値は CORBA::Float のシーケンス型の ValueList です。要素は CORBA::Float のためオブジェクトの所有権等といったことは考えなくてもよいのですが、シーケンス型はそれ自身オブジェクトですので、所有権を考慮しなければならないのでここでは _var 型の変数で受け取っています。

```
 std::cout << "Invalid command or argument(s)." << std::endl;
     }
   catch (CORBA::SystemException &e)
     {
       std::cout << "No service connected." << std::endl;
     }
   return RTC::RTC_OK;
 }
```

最後に、上のどれにも当てはまらなかったコマンドの場合に、メッセージを出しています。また、コンシューマに参照がセットされていない場合の例外を含めて捕捉するための catch 節があります。

以上、コンシューマによるオペレーションの呼び方について簡単な例を交えて説明しました。
コンシューマを利用する際には、必ずしもオブジェクト参照がセットされているとは限らないので、必ず例外を捕捉し対処することと、各オペレーションの呼び出しが、CORBA のルールに基づいて行われることに留意してください。


