---
layout: page
title: "データポート (応用編)"
---

<!-- Title: データポート (応用編) -->
<!-- -*- pukiwiki-edit -*- -->
<!-- *データポート(応用編) -->

#contents

データポート(基本編)では、データポートの基本的な使い方について説明しました。応用編では、もう少し踏み込んだ使い方について解説します。

<!-- ------------------------------------------------------------ -->
<!-- inaba **独自データ型の利用 -->
## データ型の利用

データポートでは、事前に定義されたデータ型 (例: TimedLong、TimedDouble 等) 以外に、自分で定義したデータ型を使用することもできます。
ただし、自分で新たなデータ型を作る前に、既に似たようなデータ型が定義されていないか確認して、その中に必要なデータ型がない場合にのみ新たなデータ型を定義することをお勧めします。

OpenRTM-aist では、以下の IDLファイルでデータポートに使用するデータ型が定義されています。

- BasicDataType.idl
- ExtendedDataTypes.idl
- InterfaceDataTypes.idl

保存場所は以下のとおりです。これを IDL ディレクトリーと呼びます。
- UNIX の場合： {prefix}/include/rtm/idl,{prefix}/include/openrtm-x.y/rtm/idl　( {prefix} は /usr/, /usr/local/, /opt/local/ など )
- Windows の場合： {ProgramFiles}/OpenRTM-aist/x.y/rtm/idl など。( {Program Files} は C:/ProgramFiles, C:/Program Files (x86)など)

<!-- (場所は UNIXなら {prefix}/include/rtm/idl,{prefix}/include/openrtm-x.y/rtm/idl, Windowsなら {ProgramFiles}/OpenRTM-aist/x.y/rtm/idl など。{prefix}はインストールprefix(/usr/, /usr/local/, /opt/local/ など), {Program Files} は C:/ProgramFiles, C:/Program Files (x86)などです。これを IDL ディレクトリーと呼びます。) -->


<!-- inaba*** IDLファイルの作成 -->
### 独自データ型IDLファイルの作成

データ型を定義する IDLファイルを作成します。データ型は struct キーワードで定義します。以下の基本型や、文字列型、シーケンス型が利用できます。

<table class="table-alt">
  <tr>
    <th>型</th>
    <th>意味</th>
    <th>宣言例</th>
  </tr>
  <tr>
    <td>short</td>
    <td>short型整数</td>
    <td>short shortVariable;</td>
  </tr>
  <tr>
    <td>long</td>
    <td>long型整数</td>
    <td>long longVariable;</td>
  </tr>
  <tr>
    <td>unsinged short</td>
    <td>short型整数</td>
    <td>unsigned short ushortVariable;</td>
  </tr>
  <tr>
    <td>unsigned long</td>
    <td>long型整数</td>
    <td>unsigned long ulongVariable;</td>
  </tr>
  <tr>
    <td>float</td>
    <td>単精度浮動小数点</td>
    <td>float floatVariable;</td>
  </tr>
  <tr>
    <td>double</td>
    <td>倍精度浮動小数点数</td>
    <td>double doubleVariable;</td>
  </tr>
  <tr>
    <td>char</td>
    <td>文字型</td>
    <td>char charVariable;</td>
  </tr>
  <tr>
    <td>wchar</td>
    <td>wchar文字型</td>
    <td>char charVariable;</td>
  </tr>
  <tr>
    <td>boolean</td>
    <td>bool型</td>
    <td>bool shortVariable;</td>
  </tr>
  <tr>
    <td>octet</td>
    <td>octet型</td>
    <td>octet octetVariable;</td>
  </tr>
  <tr>
    <td>longlong</td>
    <td>longlong型整数</td>
    <td>longlong longlongVariable;</td>
  </tr>
  <tr>
    <td>ulonglong</td>
    <td>unsinged longlong型整数</td>
    <td>ulonglong ulonglongVariable;</td>
  </tr>
  <tr>
    <td>sequence &lt;T&gt;</td>
    <td>シーケンス型</td>
    <td>sequence &lt;double&gt; doubleSeqVariable;</td>
  </tr>
</table>

ここでは、MyDataType.idl に MyData というデータ型を定義することにします。
表示のためにスペースを前方に入れていますが、これは実際にIDLファイルを使用する上で不要のため削除してください。

```
 // @file MyDataType.idl
 #include "BasicDataType.idl"
 
 module MyModule
 {
  struct MyData
  {
    RTC::Time tm;
    short shortVariable;
    long longVariable;
    sequence<double> data;
  };
 };
```

2行目に
```
 #include "BasicDataType.idl"
```
とあるのは、MyData 型の一番最初のフィールド tm (RTC::Time 型) を利用するために必要です。
特に理由がない場合、独自データ型でも、一番初めのフィールドはタイムスタンプを格納するために RTC::Time tm; と宣言してください。
また、module MyModule はネームスペースの指定です。データ型を定義する際は必ず適当なネームスペースを定義しその中でデータ型を定義してください。

<!-- inaba 上記内容のファイルを、C:\UserDefTypeフォルダーに作成します。 -->

<!-- 3行目はダミーの interface 定義です。これは RTCBuilder で読み込ませるために必要です。(RTCBuilderの将来のバージョンではこれは不要になるかもしれません。) -->
<!--  -->
<!-- interface dummy {}; -->

<!-- *** IDLファイルのコピー -->
<!--  -->
<!-- BasicDataType.idl など OpenRTM-aist で定義されている IDLファイルをインクルードする場合は、上記 BasicDataType.idl などが入っているディレクトリーからユーザー定義の IDLファイルが格納されているフォルダーに IDLファイルをコピーします。 -->
<!-- （BasicDataType.idlをC:\UserDefTypeにコピー） -->
<!--  -->
<!-- BasicDataType.idl 保存場所の例は以下のとおりです。 -->
<!-- - UNIX の場合： {prefix}/include/rtm/idl,{prefix}/include/openrtm-x.y/rtm/idl　( {prefix} は /usr/, /usr/local/, /opt/local/ など ) -->
<!-- - Windows の場合： {ProgramFiles}/OpenRTM-aist/x.y/rtm/idl など。( {Program Files} は C:/ProgramFiles, C:/Program Files (x86)など) -->


<!-- inaba *** RTCBuilder での確認 -->

<!-- &color(red){※ 新規プロジェクトを作成する際には、”デフォルト・ロケーションの使用(D)”のチェックを外し、先程作成したフォルダー(C:\UserDefType)を指定します。}; -->

<!-- #ref(data_port_01.png,100%,center) -->
<!-- CENTER: ロケーションに「UserDefType」 指定 -->

<!-- inaba RTCBuilder で以下のことを確認します。 -->

<!-- inaba データポート設定タブを開き、''Detail'' の ''*データ型'' のプルダウンをクリックし、MyData があるかどうか確認します。 -->

<!-- inaba #ref(data_port_03.png,100%,center) -->
<!-- inaba CENTER: Detail のデータ型 -->

<!-- inaba もし見つからなければ以下のことを確認します。 -->

<!-- - MyData.idl が BasicDataType.idl などが入っているディレクトリーにコピーされているか？ -->
<!-- inaba - Eclipse の [ウィンドウ] > [設定] > [RTCBUilder] > [データ型: IDLFile Directories] にユーザー定義の IDLファイルが入っているディレクトリー(C:\UserDefType)が設定されているかを確認します。設定されていなければ、MyDataType.idl が入っているディレクトリーを「新規」から追加し、Eclipse を再起動します。 -->

<!-- inaba #ref(data_port_02.png,100%,center) -->
<!-- inaba CENTER: MyData が表示されていない場合 -->

### RTC Builderでプロジェクト作成

RTCBuilder でプロジェクトの作成を行います。

「RTC Builder Project」のアイコンをクリックし、表示したウィンドウにプロジェクト名を入力し「終了」すると、左のウィンドウに生成したプロジェクトファイルが表示します。
<div align="center"><a href="idl_00000.png"><img src="idl_00000.png" width="80%;"></a></div>
<div align="center">「RTC Builder Project」ウィンドウを表示</div>

<div align="center"><a href="idl_002.png"><img src="idl_002.png" width="40%;"></a></div>
<div align="center">idlフォルダーの確認</div>

そこに独自データ型を配置するidlフォルダーがあるので独自データ型のIDLファイル（MyDataType.idl）を、ドラッグ&ドロップや[右クリック]>[貼り付け]などで置いてください。

プロジェクトフォルダーは、RTCBuilder起動直後に表示する「ディレクトリをワークスペースとして選択」をデフォルトで進めた場合、[ c:\Users\ユーザ名\workspase ]フォルダー以下にあります。

<!-- idlディレクトリ下に独自データ型のIDLファイル（MyDataType.idl）を置いてください。 -->

### データポートの作成

RTCBuilder で独自データ型のidlを使ったコンポーネントの作成を行います。

データポート設定タブを開き、データポート（InPort/OutPort）を定義します。

作成したデータポートで独自データ型を使いたい場合、[Reload] をクリックするとidlフォルダーのMyDataType.idlが読み込まれ、 ***データ型** のプルダウンで新たに定義した  MyData を選択できます。

<div align="center"><a href="idl_000.png"><img src="idl_000.png" width="50%;"></a></div>
<div align="center">[Reload] をクリック、MyData のデータ型を選択</div>

<!-- inaba RTCBuilder でコンポーネントの作成を行います。 -->
<!-- inaba データポート設定タブでは、新たに定義した MyData 型が選択できるようになっているので、新規データポート (InPort もしくは OutPort) を作成、データポート名とデータ型を設定します。 -->

<!-- inaba #ref(data_port_03.png,100%,center) -->
<!-- inaba CENTER: MyData のデータ型 -->
<!-- inaba CENTER: Detail のデータ型 -->

その他、コンポーネント作成に必要な項目の設定が終わったら、基本タブに戻り、[コード生成] ボタンをクリックし、コードの生成を行います。


<!-- *** プロジェクトディレクトリーへの IDL のコピー -->
<!--  -->
<!-- コード生成によってできたプロジェクトのディレクトリーへ先ほどの MyDataType.idl をコピーします。 -->


<!-- *** Windows での作業 -->

<!-- Windows では、プロジェクトディレクトリー内にある IDLファイルを自動的にコンパイルするようになっていますので、RTコンポーネントを試しに1度コンパイルします。 -->
<!-- すると、MyDataTypeSkel.h や MyDataTypeSkel.cpp などのファイルが生成されます。 -->
<!-- ただし、MyData を宣言したヘッダファイルがインクルードされていないので、コンポーネントのコンパイルには失敗するはずです。 -->

<!-- *** Linux での作業 -->
<!-- Makefile.<コンポーネント名> 中の SKEL_OBJ にオブジェクトファイルを指定します。(既に以下のような記述がある場合は不要。) -->

<!-- STUB_OBJ = MyDataTypeStub.o -->

<!-- こうすることで、MydataType のスタブオブジェクトがコンポーネントにリンクされます。 -->
<!-- また、MyDataType.idl から MyDataTypeStub.h と MyDataTypeStub.cpp を生成するための以下の行を追加します。(既に以下のような記述がある場合は不要。) -->

<!-- MyDataTypeStub.cpp : MyDatatype.idl -->
<!-- $(IDLC) $(IDLFLAGS) $< -->
<!-- $(WRAPPER) $(WRAPPER_FLAGS) --idl-file=$< -->
<!-- MyDataTypeStub.h : MyDatatype.idl -->
<!-- $(IDLC) $(IDLFLAGS) $< -->
<!-- $(WRAPPER) $(WRAPPER_FLAGS) --idl-file=$< -->
<!-- MyDataTypeStub.o: MyDataTypeStub.cpp MyDataTypeStub.h -->
<!-- $(CXX) $(CXXFLAGS) -c -o $@ $< -->

<!-- これらにより、MyDatatype.idl から MyDataTypeStub.cpp MyDataTypeStub.h が作成され、MyDataTypeStub.cpp MyDataTypeStub.h から MyDataTypeStub.o が作成されます。 -->

<!-- *** ヘッダの編集 -->
<!--  -->
<!-- コンポーネントのヘッダファイル (コンポーネント名が MyComponent の場合 MyComponent.h) をエディタで開き、以下のように MyDataTypeStub.h をインクルードします。 -->
<!--  -->
<!-- // Service Consumer stub headers -->
<!-- // <rtc-template block="consumer_stub_h"> -->
<!-- #include <MyDatatypeStub.h> -->
<!--  -->
<!-- // </rtc-template> -->

<!-- *** ビルド -->

<!-- ここまで終了したら、再度ビルドしてみます。 -->
<!-- エラーなどなくビルドが終了するはずです。 -->


<!-- ------------------------------------------------------------ -->
## データポート、コネクタのコールバックの利用

InPort は isNew() でデータの到着の有無を確認して、read() で読みだす、あるいは OutPort は write() でデータを送り出す、ということについてはすでに述べました。

例えば、InPort はデータが来てから、onExecute() 等などの関数内で、isNew() を呼び read() を呼び出すまでデータを取得することはできません。
onExecute() の周期が非常に速かったとしても、データが InPort に到着するタイミングと、実際に処理が行われるタイミングは非同期に行われます。

データが到着してすぐに、すなわち同期的に処理を行いたい場合にはどうすればよいのでしょうか。これを実現する方法として、OpenRTM-aist ではデータポートやコネクタの種々の処理のタイミングで呼び出されるコールバックを定義しています。

コールバックには大きく分けて、1) InPort、2) OutPort、3) コネクタ、4) ポート の4種類のコールバックが用意されています。

<!-- ------------------------------------------------------------ -->
### InPort のコールバック

InPort には、以下の2種類のコールバックが用意されています。
これらは rtm/PortCallback.h において定義されています。

<table class="table-alt">
  <tr>
    <td>OnRead</td>
    <td>InPort の read() が呼び出された際にコールされる InPort::setOnRead() 関数でセット。</td>
  </tr>
  <tr>
    <td>OnReadConvert</td>
    <td>InPort の read() が呼び出された際にデータを変換するためにコールされる。InPort::setOnReadConvert() 関数でセット。</td>
  </tr>
</table>

OnRead コールバックは read() が呼び出されたときに、OnReadConvert は read() が呼び出されたとき、呼び出し元にある種の変換を施したデータを返すために使用するコールバックです。

それぞれのコールバックは、rtm/PortCallback.h で定義されているそれぞれのファンクタの基底クラスを継承することにより実装します。

>ファンクタとは、オブジェクトを通常の関数と同じような文法で呼び出し可能にするもので、C++ であれば operator() をオーバーロードをすることで実現することができる。C言語では呼び出し元に関数ポインタを与えることでコールバックを実現するが、関数ポインタのみでは、コールバック自体に状態変数を与えることは難しい。ファンクタはそれ自身がオブジェクトであるため、状態変数を持たせることができ、その上、C言語の関数同様の呼び出しが可能になる。

以下にそれぞれの実装例を示します。

```
 #include <rtm/Portcallback.h>
 
 template <class T>
 class MyOnRead
  : public RTC::OnRead<T>
 {
 public:
   MyOnRead(std::ostream& os) : m_os(os) {};
   virtual void operator()()
   {
     m_os      << "read() 関数が呼ばれました。" << std::endl;
     std::cout << "read() 関数が呼ばれました。" << std::endl;
   }
 private:
   std::ostream& m_os;
 };
 
 template <class T> 
 class MyOnReadConvert
  : public RTC::OnReadConvert<T>
 {
 public:
   virtual T operator()(const T& value)
   {
     T tmp;
     tmp.data = value.data * value.data;
     return tmp;
   }
 };
```

OnRead を継承した MyOnRead ファンクタでは、コンストラクタで出力ストリーム std::ostream を渡しています。どこかでオープンしたファイル出力ストリーム std::ofstream 等を渡すことを意図しています。
ファンクタの実体である operator()() では、出力ストリームと標準出力に対して、文字列を出力しています。このように、ファンクタでは、予めコンストラクタなどで状態変数を渡すことで、他のオブジェクトに対する呼び出しも実現することができます。

一方 OnReadConvert<T> を継承した MyOnReadConvert は operator()(constT&) のみを実装しています。この関数の引数には、read() が呼ばれたときにInPort 変数に読みだされる前のデータが渡されます。
この関数内で何らかの処理を行い return で返したデータは InPort 変数に書き込まれます。この例では、データ型に data というメンバがあり、かつ乗算演算子が定義されているという前提で自乗を計算して返しています。
適切なメンバがない変数型を使用すればコンパイルエラーになります。

さて、このファンクタを実際にコンポーネントに組み込んでみましょう。InPort を使用しているサンプルとして、ここでは OpenRTM-aist に含まれているサンプルである ConsoleOut を利用します。ConsoleOut は OpenRTM-aist のソースを展開すると、

```
 OpenRTM-aist-<version>/examples/SimpleIO/
```

の下に、また Linux 等でパッケージ等からインストールすると、

```
 /usr/share/OpenRTM-aist/examples/src/
```

の下にソースコードがあります。

まず、上記のクラス定義を、ConsoleOut.h に記述します。クラス定義は、本来別のソースに記述した方が良いのですが、ファンクタクラスは、このコンポーネント内でしか使用せず、内容も短いものですので、こういう場合はヘッダ内で実装も含めて定義しても構わないでしょう。

```
 // ConsoleOut.h
 
   中略
 // Service Consumer stub headers
 // <rtc-template block="consumer_stub_h">
 
 // </rtc-template>
 
 using namespace RTC; 
 
 // ここから追加分
 template <class T>
 class MyOnRead
 
  : public RTC::OnRead<T>
 {
 public:
   MyOnRead(std::ostream& os) : m_os(os) {};
   virtual void operator()()
   {
     m_os      << "read() 関数が呼ばれました。" << std::endl;
     std::cout << "read() 関数が呼ばれました。" << std::endl;
   }
 private:
   std::ostream& m_os;
 };
 
 template <class T> 
 class MyOnReadConvert
 
  : public RTC::OnReadConvert<T>
 
 {
 public:
   virtual T operator()(const T& value)
   {
     T tmp;
     tmp.data = value.data * value.data;
     return tmp;
   }
 };
 // ここまで追加分
 
 class ConsoleOut
 
   : public RTC::DataFlowComponentBase
 
 {
 
   中略
 
  protected:
   // DataInPort declaration
   // <rtc-template block="inport_declare">
   TimedLong m_in;
   InPort<TimedLong> m_inIn;
 
   中略
 
  private:
   //ここから追加分
   MyOnRead<TimedLong>* m_onread;
   MyOnReadConvert<TimedLong>* m_onreadconv;
   //ここまで追加分
 };
```

まず、ConsoleOut クラスの宣言の前に、コールバックファンクタ MyOnRead とMyOnReadConvert を宣言します。
これらのクラスのポインタ変数をメンバとして持たせるために、private の部分に、それぞれのポインタ変数を宣言します。
このとき、MyOnRead/MyOnReadConvert ともに、クラステンプレートの型引数にこのコンポーネントの InPort の型と同じ、TimedLong を与えていることに注意してください。



<!-- ------------------------------------------------------------ -->
### OutPort のコールバック

OutPort には、以下の2種類のコールバックが用意されています。
これらは rtm/PortCallback.h において定義されています。

<table class="table-alt">
  <tr>
    <td>OnWrite</td>
    <td>OutPort の write() が呼び出された際にコールされる OutPort::setOnWrite() 関数でセット。</td>
  </tr>
  <tr>
    <td>OnWriteConvert</td>
    <td>OutPort の write() が呼び出された際にデータを変換するためにコールされる。OutPort::setOnWriteConvert() 関数でセット。</td>
  </tr>
</table>

OnWrite コールバックは write() が呼び出された際に、OnWriteConvert はwrite() が呼び出された際に、ある種の変換を施したデータを送信するために使用するコールバックです。

それぞれのコールバックは、InPort と同様 rtm/PortCallback.h で定義されているそれぞれのファンクタの基底クラスを継承することにより実装します。

以下にそれぞれの実装例を示します。

```
 #include <rtm/Portcallback.h>
 
 template <class T>
 class MyOnWrite
 
  : public RTC::OnWrite<T>
 
 {
 public:
   MyOnWrite(std::ostream& os) : m_os(os) {};
   virtual void operator()()
   {
     m_os      << "write() 関数が呼ばれました。" << std::endl;
     std::cout << "write() 関数が呼ばれました。" << std::endl;
   }
 private:
   std::ostream& m_os;
 };
 
 template <class T> 
 class MyOnWriteConvert
 
  : public RTC::OnWriteConvert<T>
 
 {
 public:
   virtual T operator()(const T& value)
   {
     T tmp;
     tmp.data = 2 * value.data;
     return tmp;
   }
 };
```

コールバック用のファンクタの書き方は、InPort の OnRead/OnReadConvert とほぼ同じです。OnWrite を継承した MyOnWrite ファンクタでは、コンストラクタで出力ストリーム std::ostream を渡しています。
どこかでオープンしたファイル出力ストリーム std::ofstream 等を渡すことを意図しています。ファンクタの実体である operator() では、出力ストリームと標準出力に対して、文字列を出力しています。
このように、ファンクタでは、予めコンストラクタなどで状態変数を渡すことで、他のオブジェクトに対する呼び出しも実現することができます。

一方 OnReadConvert<T> を継承した MyOnReadConvert は operator()(constT&) のみを実装しています。この関数の引数には、read() を呼んだときに InPort 変数に読みだされる前のデータが渡されます。この関数内で何らかの処理を行い return で返したデータは InPort 変数に書き込まれます。
この例では、データ型に data というメンバがあり、かつ乗算演算子が定義されているという前提で自乗を計算して返しています。適切なメンバがない変数型を使用すればコンパイルエラーになります。

### コネクタ・バッファのコールバック

#### コネクタ

コネクタはバッファおよび通信路を抽象化したオブジェクトです。図に示すように、OutPort と InPort の間に存在し、OutPort からは write() 関数によりデータの書き込み、InPort からは read() 関数によりデータの読み出しが行われます。
コネクタは、データがどのような手段で OutPort から InPort へ伝送されるかを抽象化し隠蔽します。


OutPort はコネクタ内のバッファに対して、
- 書き込み
- 各種制御 (読み戻し、未読データへのアクセス等)
- バッファフル状態の通知およびタイムアウトの通知を行う(または通知を受ける)ことができます。
- データの読み出し
- 各種制御(読み戻し、未読データへのアクセス等)
- バッファエンプティ状態の通知およびタイムアウト通知を行う(または通知を受ける)ことができます。

OutPort は複数の InPort へ接続することができますが、一つの接続につき、一つのコネクタが生成されます。(実際には InPort も複数の接続を同時に持つこともできますが、データを区別する方法がないので、通常は用いません。) 
つまり、接続が3つあれば、コネクタが3つ存在し、それぞれに対して書き込みのステータスが存在することになります。

また、これらの機能のために、OutPort/InPort 一対に対して、それぞれ一つコネクタが存在する必要があることがわかります。
さらに、コネクタをサブスクリプション型に対応した実装レベルでモデル化するにあたり、パブリッシャと呼ばれる非同期通信のためのオブジェクトを導入しました。

データポートは接続が確立されると、1つの接続につき1つのコネクタオブジェクトを生成します。コネクタは、OutPort と InPort をつなぐデータストリームの抽象チャネルです。

<table class="table-alt">
  <tr>
    <td>ON_BUFFER_WRITE</td>
    <td>バッファ書き込み時</td>
  </tr>
  <tr>
    <td>ON_BUFFER_FULL</td>
    <td>バッファフル時</td>
  </tr>
  <tr>
    <td>ON_BUFFER_WRITE_TIMEOUT</td>
    <td>バッファ書き込みタイムアウト時</td>
  </tr>
  <tr>
    <td>ON_BUFFER_OVERWRITE</td>
    <td>バッファ上書き時</td>
  </tr>
  <tr>
    <td>ON_BUFFER_READ</td>
    <td>バッファ読み出し時</td>
  </tr>
  <tr>
    <td>ON_SEND</td>
    <td>InProtへの送信時</td>
  </tr>
  <tr>
    <td>ON_RECEIVED</td>
    <td>InProtへの送信完了時</td>
  </tr>
  <tr>
    <td>ON_RECEIVER_FULL</td>
    <td>InProt側バッファフル時</td>
  </tr>
  <tr>
    <td>ON_RECEIVER_TIMEOUT</td>
    <td>InProt側バッファタイムアウト時</td>
  </tr>
  <tr>
    <td>ON_RECEIVER_ERROR</td>
    <td>InProt側エラー時</td>
  </tr>
</table>

<table class="table-alt">
  <tr>
    <td>ON_BUFFER_EMPTY</td>
    <td>バッファが空の場合</td>
  </tr>
  <tr>
    <td>ON_BUFFER_READTIMEOUT</td>
    <td>バッファが空でタイムアウトした場合</td>
  </tr>
  <tr>
    <td>ON_SENDER_EMPTY</td>
    <td>OutPort側バッファが空</td>
  </tr>
  <tr>
    <td>ON_SENDER_TIMEOUT</td>
    <td>OutPort側タイムアウト時</td>
  </tr>
  <tr>
    <td>ON_SENDER_ERROR</td>
    <td>OutPort側エラー時</td>
  </tr>
  <tr>
    <td>ON_CONNECT</td>
    <td>接続確立時</td>
  </tr>
  <tr>
    <td>ON_DISCONNECT</td>
    <td>接続切断時</td>
  </tr>
</table>

### ポートのコールバック
#### ステータス
データポートは、データの送受信を行った際に、ステータスを返します。
ステータスは、rtm/DataPortStatus.h で定義されています。

<table class="table-alt">
  <tr>
    <td>PORT_OK</td>
    <td>正常終了</td>
  </tr>
  <tr>
    <td>PORT_ERROR</td>
    <td>異常終了</td>
  </tr>
  <tr>
    <td>BUFFER_ERROR</td>
    <td>バッファエラー</td>
  </tr>
  <tr>
    <td>BUFFER_FULL</td>
    <td>バッファフル</td>
  </tr>
  <tr>
    <td>BUFFER_EMPTY</td>
    <td>バッファエンプティ</td>
  </tr>
  <tr>
    <td>BUFFER_TIMEOUT</td>
    <td>バッファタイムアウト</td>
  </tr>
  <tr>
    <td>SEND_FULL</td>
    <td>データを送信したが相手側がバッファフル状態</td>
  </tr>
  <tr>
    <td>SEND_TIMEOUT</td>
    <td>データを送信したが相手側がタイムアウトした</td>
  </tr>
  <tr>
    <td>RECV_EMPTY</td>
    <td>データを送信したがデータが空状態</td>
  </tr>
  <tr>
    <td>RECV_TIMEOUT</td>
    <td>データを受信しようとしたがタイムアウトした</td>
  </tr>
  <tr>
    <td>INVALID_ARGS</td>
    <td>不正な引数</td>
  </tr>
  <tr>
    <td>PRECONDITION_NOT_MET</td>
    <td>事前条件を満たしていない</td>
  </tr>
  <tr>
    <td>CONNECTION_LOST</td>
    <td>接続が切断された</td>
  </tr>
  <tr>
    <td>UNKNOWN_ERROR</td>
    <td>不明なエラー</td>
  </tr>
</table>

データポートのデータ経路上のエラー発生個所から呼び出し側へエラー情報を伝えるためにこのエラーコードを使用します。
主に、伝送路上のエラー、伝送先のエラーなどが考えられますが、各部分で発生するエラーを以下に示します。
<br>

- Push 型
  - InPortConsumer と Publisher/Activity 間で発生するリターンコード
<br>
PORT_OK, PORT_ERROR, SEND_FULL, SEND_TIMEOUT, CONNECTION_LOST, UNKNOWN_ERROR
  - Activity と OutPort の Buffer/Connector 間で発生するリターンコード
<br>
PORT_OK, PORT_ERROR, BUFFER_ERROR, BUFFER_FULL, BUFFER_TIMEOUT, UNKNOWN_ERROR
- Pull 型
  - Activity と InPort の間で発生するリターンコード
<br>
PORT_OK, PORT_ERROR, RECV_EMPTY, RECV_TIMEOUT, CONNETION_LOST, UNKNOWN_ERROR

<br>

## 独自データポートインターフェースの作成
独自データポートインターフェースの作成例を示します。

以下の関数、クラスの定義が必要です。

- プロバイダクラス (InPortTestProvider)
- コンシューマクラス (InPortTestConsumer)
- プロバイダ、コンシューマ登録関数 (InPortTestInterfaceInit)

### プロバイダクラス (InPortTestProvider)
データポートインターフェース(Push型)のプロバイダクラスです。
コンシューマ側で put関数を呼び出した際に、何らかの方法によりプロバイダ側にデータを転送する必要があります。
このサンプルではコンシューマ側の put関数呼び出し時にファイルにデータを書き込み、プロバイダ側でファイルからデータを読み込むことでデータの転送を行っています。

```
 //InPortTestProvider.cpp
 
 #include "InPortTestProvider.h"
 #ifdef WIN32
 #pragma warning( disable : 4290 )
 #endif
 
 namespace RTC
 {
   InPortTestProvider::InPortTestProvider(void)
 
	  : m_buffer(0), m_running(true), m_filename("data.dat")
 
  {
    setInterfaceType("test");
    activate();
  }
  
  InPortTestProvider::~InPortTestProvider(void)
  {
	  m_running = false;
	  wait();
  }
 
  //プロバイダ生成時に呼び出される関数
  //コネクタプロファイル、ポートのプロパティの情報を受け取る
  void InPortTestProvider::init(coil::Properties& prop)
  {
  }
 
  void InPortTestProvider::
  setBuffer(BufferBase<cdrMemoryStream>* buffer)
  {
    m_buffer = buffer;
  }
 
  void InPortTestProvider::setListener(ConnectorInfo& info, ConnectorListeners* listeners)
  {
    m_profile = info;
    m_listeners = listeners;
  }
 
  void InPortTestProvider::setConnector(InPortConnector* connector)
  {
    m_connector = connector;
  }
 
  //別スレッドにより実行される関数
  //周期的にファイルからデータを読み込んでバッファに書き込む
  //この関数はこのサンプルでは必要ですが、独自インターフェースを作成するうえで
  //必須ではありません
  int InPortTestProvider::svc()
  {
     coil::sleep(1);
     while (m_running)
     {
 
	  std::ifstream  fin;
	  fin.open(m_filename, std::ios::in | std::ios::binary);
 
          if (fin)
          {
               while (!fin.eof())
               {
                    int data_size = 0;
                    fin.read((char*)&data_size, sizeof(int));
                    if (data_size > 0)
                    {
                        CORBA::OctetSeq data;
                        data.length(data_size);
                        fin.read((char*)&data[0], data_size);
 
                        //cdrMemoryStream型変数にデータを格納してバッファに書き込む
                        //以下の記述方法はomniORB特有なため、TAOやORBexpressに対応する場合は
                        //分ける必要がある
                        cdrMemoryStream cdr;
                        //エンディアンの設定を行う
                        bool endian_type = m_connector->isLittleEndian();
                        cdr.setByteSwapFlag(endian_type);
                        //データを書き込む
                        cdr.put_octet_array(&(data[0]), data.length());
                        //バッファに書き込む
                        m_buffer->write(cdr);
                    }
               }
               fin.close();
 
	  }
 
     }
     return 0;
  }
 
  //コネクタ接続時に呼び出される関数
  //この関数はコンシューマ側のsubscribeInterface関数よりも前に呼び出される
  //このため、publishInterface関数で設定した情報をコンシューマ側のsubscribeInterface関数で
  //取得することができる
  //何か問題があった時はfalseを返してコネクタを切断する
  bool InPortTestProvider::
 
	  publishInterface(SDOPackage::NVList& properties)
 
   {
        //データを書き込むファイル名の情報を格納する
        CORBA_SeqUtil::
                  push_back(properties,
                  NVUtil::newNV("dataport.test.filename", m_filename.c_str()));
 
	return true;
 
   }
 };
 
 extern "C"
 {
     //この関数をモジュールロード時に呼び出す必要がある
    void InPortTestProviderInit(void)
    {
         RTC::InPortProviderFactory& factory(RTC::InPortProviderFactory::instance());
         factory.addFactory("test",
 
                       ::coil::Creator< ::RTC::InPortProvider,
                                        ::RTC::InPortTestProvider>,
                       ::coil::Destructor< ::RTC::InPortProvider,
                                           ::RTC::InPortTestProvider>);
 
     }
 };
```

<br>

データポートインターフェース(Push型)のコンシューマクラスです。InPortProvider を継承する必要があります。
Taskクラスの継承はこのサンプル独自のものなので必須ではありません。

```
 //InPortTestProvider.h
 
 #ifndef RTC_INPORTTESTPROVIDER_H
 #define RTC_INPORTTESTPROVIDER_H
 #include <rtm/BufferBase.h>
 #include <rtm/InPortProvider.h>
 #include <rtm/CORBA_SeqUtil.h>
 #include <rtm/Manager.h>
 #include <rtm/ConnectorListener.h>
 #include <rtm/ConnectorBase.h>
 #include <fstream>
 #ifdef WIN32
 #pragma warning( disable : 4290 )
 #endif
 
 namespace RTC
 {
    class InPortTestProvider
 
      : public InPortProvider,
	public coil::Task
 
    {
    public:
       InPortTestProvider(void);
       virtual ~InPortTestProvider(void);
       virtual void init(coil::Properties& prop);
       virtual void setBuffer(BufferBase<cdrMemoryStream>* buffer);
       virtual void setListener(ConnectorInfo& info,
                             ConnectorListeners* listeners);
       virtual void setConnector(InPortConnector* connector);
       virtual bool publishInterface(SDOPackage::NVList& properties);
       virtual int svc();
 
  private:
      CdrBufferBase* m_buffer;
      ConnectorListeners* m_listeners;
      ConnectorInfo m_profile;
      InPortConnector* m_connector;
      bool m_running;
      std::string m_filename;
   }; 
 };
 
 extern "C"
 {
 
	DLL_EXPORT void InPortTestProviderInit(void);
 
 };
 
 #ifdef WIN32
 #pragma warning( default : 4290 )
 #endif
 #endif
```

<br>

### コンシューマクラス (InPortTestConsumer)
データポートインターフェース(Push型)のコンシューマクラスです。Push型の場合は InPort側にコンシューマ、OutPort側にプロバイダを生成します。
コンシューマ側で put関数を呼び出した際に、何らかの方法によりプロバイダ側にデータを転送する必要があります。
このサンプルではコンシューマ側の put関数呼び出し時にファイルにデータを書き込み、プロバイダ側でファイルからデータを読み込むことでデータの転送を行っています。

```
 //InPortTestConsumer.cpp
 
 #include <rtm/NVUtil.h>
 #include "InPortTestConsumer.h"
 
 namespace RTC
 {
    InPortTestConsumer::InPortTestConsumer(void)
 
    : rtclog("InPortTestConsumer")
 
    {
    }
  
    InPortTestConsumer::~InPortTestConsumer(void)
    {
       RTC_PARANOID(("~InPortTestConsumer()"));
    }
 
    //コネクタプロファイル、ポートのプロパティの情報を受け取る
    void InPortTestConsumer::init(coil::Properties& prop)
    {
       m_properties = prop;
    }
  
    //データ転送時に呼び出される関数
    //put関数内でプロバイダ側にデータを転送する処理を記述する
    InPortConsumer::ReturnCode InPortTestConsumer::
 
	  put(const cdrMemoryStream& data)
 
    {
         RTC_PARANOID(("put()"));
 
         //このサンプルでは、コンシュマー側でファイルにデータを書き込んで、プロバイダ側で
         //ファイル内のデータを読み込むことにしている
         //バイナリファイルを開く
         m_file.open(m_filename, std::ios::out | std::ios::binary | std::ios::trunc);
         //データサイズと生データをファイルに書き込む
         int data_size = data.bufSize();	
         m_file.write((char*)&data_size, sizeof(int));
         m_file.write((char*)data.bufPtr(), data_size);
         //ファイルを閉じる
         m_file.close();
 
         return PORT_OK;
      }
 
      //コネクタ接続時に呼び出される関数
      //この関数はプロバイダ側のpublishInterface関数よりも後に呼び出される
      //このため、プロバイダ側のpublishInterface関数で設定した情報を取得することができる
      //return: 何か問題があった時はfalseを返してコネクタを切断する
 
      bool InPortTestConsumer::
      subscribeInterface(const SDOPackage::NVList& properties)
      {
          //プロバイダ側で設定したファイル名を取得する
          CORBA::Long index = NVUtil::find_index(properties,
                                          "dataport.test.filename");
          const char* filename(0);
          properties[index].value >>= filename;
 
          //取得したファイル名のファイルを開く
          m_filename = filename;
          m_file.open(m_filename, std::ios::out | std::ios::binary | std::ios::trunc);
          m_file.close();
  
         return true;
     }
  
     //コネクタ切断時に呼び出される関数
     void InPortTestConsumer::
     unsubscribeInterface(const SDOPackage::NVList& properties)
     {
     }
 
     void InPortTestConsumer::publishInterfaceProfile(SDOPackage::NVList& properties)
     {
     }
 };
 
 extern "C"
 { 
     //コンシューマ登録関数
     //この関数をモジュールロード時に呼び出す必要がある
     void InPortTestConsumerInit(void)
    {
        RTC::InPortConsumerFactory& factory(RTC::InPortConsumerFactory::instance());
        factory.addFactory("test",
 
                       ::coil::Creator< ::RTC::InPortConsumer,
                                        ::RTC::InPortTestConsumer>,
                       ::coil::Destructor< ::RTC::InPortConsumer,
                                           ::RTC::InPortTestConsumer>);
 
     }
 };
```

<br>

データポートインターフェース(Push型)のコンシューマクラスです。InPortConsumer を継承する必要があります。

```
 //InPortTestConsumer.h
 
 #ifndef RTC_INPORTTESTCONSUMER_H
 #define RTC_INPORTTESTCONSUMER_H
 #include <rtm/InPortConsumer.h>
 #include <rtm/Manager.h>
 #include <fstream>
 
 namespace RTC
 {
     class InPortTestConsumer
 
       : public InPortConsumer
 
    {
       public:
        DATAPORTSTATUS_ENUM
        InPortTestConsumer(void);
        virtual ~InPortTestConsumer(void);
        virtual void init(coil::Properties& prop);
        virtual ReturnCode put(const cdrMemoryStream& data);
        virtual void publishInterfaceProfile(SDOPackage::NVList& properties);
        virtual bool subscribeInterface(const SDOPackage::NVList& properties);
        virtual void unsubscribeInterface(const SDOPackage::NVList& properties);
 
      private:
        mutable Logger rtclog;
        coil::Properties m_properties;
        std::ofstream  m_file;
        std::string m_filename;
   };
 };
 
 extern "C"
 {
 
	DLL_EXPORT void InPortTestConsumerInit(void);
 
 };
 #endif
```

<br>

### プロバイダ、コンシューマ登録関数 (InPortTestInterfaceInit)
OpenRTM-aist のマネージャは「XXX.dll」というダイナミックリンクライブラリをロードした場合に「XXXInit」関数を呼び出します。
このサンプルの場合は「InPortTestInterface.dll」をロードして、以下の「InPortTestInterfaceInit」関数を呼び出します。

```
 //InPortTestInterface.cpp
 
 #include "InPortTestConsumer.h"
 #include "InPortTestProvider.h"
 
 extern "C"
 {
 
	DLL_EXPORT void InPortTestInterfaceInit(RTC::Manager* manager)
	{
		InPortTestProviderInit();
		InPortTestConsumerInit();
	}
 
 };
```

### 確認手順
1. OpenRTM-aistがインストールされている環境を用意します。<br>
<br>
2. ビルドのために CMake設定ファイル (CMakeLists.txt) を作成します。<br>
以下は、独自インターフェースのサンプルをビルドするための CMake設定ファイルです。

```
 //OpenRTM-aistのライブラリを見つけるための記述
 
 cmake_minimum_required (VERSION 2.6)
 
 find_package(OpenRTM HINTS /usr/lib64/openrtm-1.1/cmake)
 if(${OpenRTM_FOUND})
   MESSAGE(STATUS "OpenRTM configuration Found")
 else(${OpenRTM_FOUND})
   message(STATUS "Use cmake/Modules/FindOpenRTM.cmake in the project")
   list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake/Modules)
   find_package(OpenRTM REQUIRED)
 endif(${OpenRTM_FOUND})
 
 if (DEFINED OPENRTM_INCLUDE_DIRS)
   string(REGEX REPLACE "-I" ";"
     OPENRTM_INCLUDE_DIRS "${OPENRTM_INCLUDE_DIRS}")
   string(REGEX REPLACE " ;" ";"
     OPENRTM_INCLUDE_DIRS "${OPENRTM_INCLUDE_DIRS}")
 endif (DEFINED OPENRTM_INCLUDE_DIRS)
 
 if (DEFINED OPENRTM_LIBRARY_DIRS)
   string(REGEX REPLACE "-L" ";"
     OPENRTM_LIBRARY_DIRS "${OPENRTM_LIBRARY_DIRS}")
   string(REGEX REPLACE " ;" ";"
     OPENRTM_LIBRARY_DIRS "${OPENRTM_LIBRARY_DIRS}")
 endif (DEFINED OPENRTM_LIBRARY_DIRS)
 
 if (DEFINED OPENRTM_LIBRARIES)
   string(REGEX REPLACE "-l" ";"
     OPENRTM_LIBRARIES "${OPENRTM_LIBRARIES}")
   string(REGEX REPLACE " ;" ";"
     OPENRTM_LIBRARIES "${OPENRTM_LIBRARIES}")
 endif (DEFINED OPENRTM_LIBRARIES)
 
 include_directories(${OPENRTM_INCLUDE_DIRS})
 include_directories(${OMNIORB_INCLUDE_DIRS})
 add_definitions(${OPENRTM_CFLAGS})
 add_definitions(${OMNIORB_CFLAGS})
 
 link_directories(${OPENRTM_LIBRARY_DIRS})
 link_directories(${OMNIORB_LIBRARY_DIRS})
 
 //プロジェクト名設定
 project (InPortTestInterface)
 
 //動的ライブラリを作成する
 add_library(InPortTestInterface SHARED InPortTestProvider.cpp InPortTestConsumer.cpp InPortTestProvider.h InPortTestConsumer.h InPortTestInterface.cpp)
 
 //リンクするライブラリの設定
 target_link_libraries(InPortTestInterface ${OPENRTM_LIBRARIES})
```

3. CMake により Visual Studio のプロジェクトファイルを生成します。
<br>
<br>
4. Visual Studio でビルドします。<br>
ビルド後に、Debugフォルダーに InPortTestInterface.dll が生成されます。
<br>
<br>
5. rtc.conf を作成します<br>
rtc.conf を作成して、Manager 起動時にロードするモジュールで InPortTestInterface.dll を指定します。

```
 manager.modules.preload: InPortTestInterface.dll
```

InPortTestInterface.dll が、RTC を実行するディレクトリーと異なる場合は、別途モジュール探索パスを設定します。

```
 manager.modules.load_path: C:¥workspace¥InPortTestInterface¥build¥Debug
```
<br>

6. 上記の rtc.conf を読み込んで RTCを 起動します。<br>
```
 ConsoleInComp.exe -f ../rtc.conf
```
<br>

7. ポート接続時にInterface Typeに「test」を指定する。<br>
RTSystemEditor上から Interface Type を指定できます。

