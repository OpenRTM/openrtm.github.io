---
layout: page
title: 開発環境のインストール
---

<!-- Title: 開発環境のインストール -->
<!-- * 開発環境のインストール -->
#contents

Raspberry Pi に開発環境をインストールすれば、Raspberry Pi上でのセルフコンパイルによる開発が可能です。(このサイズの組込み Linux ボードでは、通常クロスコンパイルによる開発が普通です。)

従って、PC上の RTCBuilder で生成した RTコンポーネントのコードを、Raspberry Pi上でコンパイル、実行することができます。
残念ながら Eclipse をインストールして実用的な速度で使用することは難しいようです。

この節では RTコンポーネントを開発するために必要なパッケージをインストールしていきます。

<!-- ------------------------------------------------------------ -->
## OpenRTM-aist のインストール
<!-- ------------------------------------------------------------ -->
OpenRTM-aist は、apt-get を使用してインストールすることが可能です。
まず sources.list を修正します。

```
 $ sudo vi /etc/apt/sources.list
```

sourcelist に以下の１行を加えてください。

```
 deb http://openrtm.org/pub/Linux/raspbian/ wheezy main
```

次に、以下の手順でインストールを行います。

```
 # apt-get update
 # apt-get -y --force-yes install gcc g++ make uuid-dev
 # apt-get -y --force-yes install libomniorb4-dev omniidl omniorb-nameserver
 # apt-get -y --force-yes install openrtm-aist openrtm-aist-dev openrtm-aist-example
 # apt-get -y --force-yes install openrtm-aist-python openrtm-aist-python-example
```

### サンプルコンポーネントの実行

OpenRTM-aist のインストール後、サンプルコンポーネントを起動してOpenRTM-aist が正しくインストールされたかどうか確認します。

下図のように、PC側でネームサーバと ConsoleIn コンポーネント、Raspberry Pi側でネームサーバと ConsoleOut コンポーネントを実行します。
コンポーネントはデフォルトで localhost のネームサーバに接続しますので、これを利用して rtc.conf に特定のネームサーバを設定することなく簡単にコンポーネントにアクセスします。
PC上の RTSystemEditor で、PC のネームサーバと Raspberry Pi上のネームサーバに接続し、ConsoleIn コンポーネントと ConsoleOut コンポーネントを接続します。

<div align="center"><a href="sample_component_test.png"><img src="sample_component_test.png" width="70%;"></a></div>
<div align="center"><strong>サンプルの実行</strong></div>


#### Raspberry Pi上で ConsoleOut の実行

Raspberry Pi に TeraTerm などで接続後、コンポーネントを起動します。
ネーミングサービスを起動してから ConsoleOut を起動します。

```
 $ rtm-naming
 $ /usr/share/OpenRTM-x.y/examples/ConsoleOutComp
 または
 $ python /usr/share/OpenRTM-x.y/examples/python/SimpleIO/ConsoleOutComp.py
```

上の omniorb-nameserver のインストール時に、システム起動時に自動的に omniORB のネームサービスが起動するようになっています。
しかし、ネームサービスの起動タイミングとネットワークインターフェースの起動タイミングによっては、外部からネームサーバに正しくアクセスできない場合があります。
その場合は、rtm-naming コマンドによりネームサーバを再起動することで、問題に対処できる場合があります。

#### PC側での ConsoleIn の実行

まず、ネームサーバを起動します。
Windows の場合、スタートメニューから 「OpenRTM-aist x.y」→「C++」→「tools」の下の**Start Naming Service** から起動します。
ついでに、RTSystemEditor も起動しておきます。

<div align="center"><a href="namingservice_on_windows.png"><img src="namingservice_on_windows.png" width="70%;"></a></div>
<div align="center"><strong>ネーミングサービスの起動</strong></div>

続いて、ConsoleIn を起動します。
「OpenRTM-aist x.y」→「C++」→「examples」の下の ConsoleOut をクリックして ConsoleOut コンポーネントを起動します。

#### RTSystemEditor により接続

RTSystemEditor の左側の NameService View のコンセントアイコンをクリックし、ネームサーバに接続します。
まず、自ホストのネームサーバに接続します。接続ダイアログに localhost と入力します。

<div align="center"><a href="connect_ns_localhost.png"><img src="connect_ns_localhost.png" width="70%;"></a></div>
<div align="center"><strong>ネームサーバへの接続(localhost)</strong></div>

次に、Raspberry Pi のネームサーバへ接続します。再度 NameService View の接続アイコンをクリックし、Raspberry Pi のホスト名+.localををダイアログに入力します。

<div align="center"><a href="connect_ns_myhost.png"><img src="connect_ns_myhost.png" width="70%;"></a></div>
<div align="center"><strong>ネームサーバへの接続(Raspberry Pi)</strong></div>

ネームサービスビューには2つのネームサーバの状態が表示され、それぞれのネームサーバの下に ConsoleIn0、ConsoleOut0 という2つのコンポーネントが見えているはずです。
RTSystemEditor のメニューバーのonlineエディタアイコン(ONと書かれたアイコン)をクリックし、SystemEditor を開きます。
NameService View から ConsoleIn0 と ConsoleOut0 をそれぞれ SystemEditor 上にドラッグアンドドロップし、InPort と OutPort を接続します。

<div align="center"><a href="rtsystemeditor_consoleinout.png"><img src="rtsystemeditor_consoleinout.png" width="70%;"></a></div>
<div align="center"><strong>RTSystemEditorによるConsoleInとConsoleOutの接続</strong></div>

メニューバーの緑の再生ボタンをクリックすると、2つのコンポーネントがアクティベートされ上図のような状態になります。

PC側の ConsoleIn コンポーネントのウインドウから適当な数字を入力します。

<div align="center"><a href="consolein_window.png"><img src="consolein_window.png" width="70%;"></a></div>
<div align="center"><strong>ConsoleIn (PC) 側から数値を入力</strong></div>

すると、下図のように Raspberry Pi側の ConsoleOut の表示に ConsoleIn で入力した数値が現れます。

<div align="center"><a href="consoleout_window.png"><img src="consoleout_window.png" width="70%;"></a></div>
<div align="center"><strong>ConsoleOut (Raspberry Pi) 側の表示</strong></div>

&aname(trouble);

### トラブルシューティング

ネットワーク環境や PC の設定により、上記の手順でうまくいかないことがあります。以下のトラブルシューティングを参考に問題を解決してください。

#### Raspberry Pi側のサービスのしたに ConsoleOut が表示されない

:ネームサーバの問題|ネームサーバのエンドポイントアドレスが不正な場合このような現象が起きます。rtm-naming で再度ネームサーバを起動しなおすと解決する場合があります。
このほか、Raspberry Pi の有線LANと無線LAN等2つ以上のネットワークインターフェースがある場合、PCとの接続に使用するどちらかのネットワークのみを使うように設定することで解決するケースもあります。

**コンポーネントの問題|コンポーネントが読み込んだ設定ファイル(rtc.conf)に localhost 以外のネームサーバが登録されている場合が考えられます。corba.nameservers**:  localhost と記述するなど localhost のネームサーバにコンポーネントを登録するよう設定してください。
また、Raspberry Pi の有線LANと無線LAN等2つ以上のネットワークインターフェースがある場合、PCとの接続に使用するどちらかのネットワークのみを使うように設定することで解決するケースもあります。

#### RTSystemEditor で接続できない、反応がなくなる等

:PC側のコンポーネントの問題|PCにネットワークインターフェースが2つ以上ある場合、Raspberry Pi で使用しない側のインターフェースアドレスがコンポーネントの参照として利用されている場合このような現象が起こります。
コマンドプロンプトから ipconfig で PC の IPアドレスを調べる等して、rtc.conf に使用する方の IPアドレスを以下のように設定します。

```
 corba.endpoints: 192.168.11.20
```

ただし、Vista 以降の Windows では、C:\Program Files 以下のファイルは簡単には編集ができなくなっています。c:\tmp など適当なディレクトリーに ConsoleIn.exe と rtc.conf をコピー(あるいは新たに作成)するなどして、対処してください。

:Raspberry Pi側のコンポーネントの問題|Raspberry Pi の有線LANと無線LAN等2つ以上のネットワークインターフェースがある場合で、それぞれが別のネットワークにつながっている場合、上述のPCと同様の問題が起こります。ifconfig で使用する方のIPアドレスを調べ、rtc.conf に以下のように記載します。

```
 corba.endpoints: 192.168.11.21
```

## CMake のインストール

cmake は apt-get を利用してインストールする事が可能です。root 権限を持つユーザでインストールを行います｡

```
 $ sudo apt-get update
 $ sudo apt-get install cmake
```

## Doxygen のインストールについて

CMake ベースの RTコンポーネントプロジェクトでは、デフォルトで doxygen を利用してドキュメントを生成するように設定されています。
しかしながら、doxygen をインストールすると、LaTeX等も同時にインストールされてしまい、SDカードの容量を圧迫しますのでこのチュートリアルでは Doxygen をインストールしません。

### ドキュメントを生成しない方法

CMake ベースの RTCプロジェクトにおいて doxygen でのドキュメント生成を抑制するには、トップレベルの CMakeLists.txt で、

```
 option(BUILD_DOCUMENTATION "Build the documentation" ON)
    ↓
 option(BUILD_DOCUMENTATION "Build the documentation" OFF)
```

のように変更します。

### Doxygen のインストール

SDカードの容量が十分ある場合 doxygen を apt-get で以下のようにインストールすることができます。

```
 $ sudo apt-get install doxygen
```

<span style="color:red;">※Doxygen のインストールが完了するまでには、十数分程度かかります｡</span>;

## Subversion/Git のインストール

ソースコードを外部から取得する際にたびたび使用するので subversion/git をインストールすることをお勧めします。

```
 $ sudo apt-get install subversion git
```


## コンパイルのテスト

コンポーネントのコンパイルが行えるかテストしてみます。
以下のリポジトリに移動ロボット Kobuki用コンポーネントがありますので、チェックアウトしてコンパイルしてみます。

- [KobukiAIST RTC](http://svn.openrtm.org/components/trunk/mobile_robots/kobuki)

### ソースコードのチェックアウト

ソースコードをチェックアウトしてみます。

```
 $ svn co http://svn.openrtm.org/components/trunk/mobile_robots/kobuki
```
   : 中略
```
 A    kobuki/libkobuki/doc/CMakeLists.txt
 A    kobuki/libkobuki/License.rtf
 A    kobuki/libkobuki/CMakeLists.txt
 A    kobuki/rtc.conf
 A    kobuki/CMakeLists.txt
 Checked out revision 2.
 $
```

kobuki ディレクトリーいかにソースコードがチェックアウトされましたので、build ディレクトリーを作成しその中でビルド、インストールします。

```
  $ cd kobuki
  $ mkdir build
  $ cd build
  $ cmake -DCMAKE_INSTALL_PREFIX=/usr ..
  $ make
  $ cd src
  $ make install
```

このソースコードはデフォルトで Doxygenに よるドキュメント生成が OFF になっていますので、Doxygen がインストールされていなくてもビルドできるでしょう。

