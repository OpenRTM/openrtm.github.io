---
layout: page
title: 動作確認 (linux編)
---
<br>
<a>No English version available.
</a>

<!-- Title: 動作確認 (Linux編) -->
#contents

インストールが正常に終了したら、付属のサンプルで動作テストをします。サンプルは、zip ファイルを展開したディレクト配下の以下の場所にあります。

- `/OpenRTM-aist/<version>/examples`

ソースからビルドした場合は、プロジェクトディレクトリー配下の以下の場所にあります。
(X.X.Xはバージョン)

- `/OpenRTM-X.X.X-Java/installer/resources/Source/examples`

サンプルコンポーネントセット SimpleIO を使って、OpenRTM-aist-Java が正しくビルド・インストールされているかを確認します。

## サンプルコンポーネントセット SimpleIO

RTコンポーネント ConsoleInComp、ConsoleOutComp からなるサンプルセットです。
ConsoleInComp はコンソールから入力された数値を OutPort から出力するコンポーネント、ConsoleOutComp は InPort に入力された数値をコンソールに表示するコンポーネントです。
これらは、最も Simple な I/O (入出力) を例示するためのサンプルです。
ConsoleInComp の OutPort から ConsoleOutComp のInPort へ接続を構成し、これらの2つのコンポーネントをアクティブ化 (Activate) することで動作します。

以降、説明を簡単にするため OpenRTM-aist-Java が /home/openrtm/OpenRTM-aist/ にインストール（展開）されているとします。


## サンプルを使用したテスト

### ネームサーバーを起動

まず、コンポーネントの参照を登録するためのネームサーバーを起動します。
OpenRTM-aist-Javaでは、orbd（Java CORBA naming servic）の起動用シェルスクリプトを準備しています。
Linux などのパッケージで omniORB をインストールした場合、すでにシステムのサービスとしてネームサーバー (omniNames) が起動している場合があります。
orbd の代わりに omniNames を使用しても正常に動作します。

すでに omniNames が起動している場合、このようになります。
```
 $ ps ax | grep omni
 1550  ?        Sl     0:00 /usr/bin/omniNames -errlog /var/log/omniorb4-nameserver.log
 18418 pts/2    S+     0:00 grep --color=auto omni
```

omniNames が起動していない場合はこのようになります。
```
 $ ps ax | grep omni
 18418 pts/2    S+     0:00 grep --color=auto omni
```

ネームサーバーが起動していない場合、 start-orbd.sh コマンドでネームサーバーを起動します。
start-orbd.shは、/home/openrtm/OpenRTM-aist/1.1/examples に格納されています。

```
 $ sh /home/openrtm/OpenRTM-aist/1.1/examples/start-orbd.sh
 Starting Java CORBA naming service (orbd).
```

oebd はブロックします。 


<!-- *** rtc.conf の作成 -->
<!--  -->
<!-- テストのためのRTCコンフィギュレーションファイル rtc.conf を作成し、配置します。まず、適当な作業ディレクトリを作ります。ここでは便利のため、ホームディレクトリ直下に RTCwork というディレクトリを作業ディレクトリとしておくことにします。作業ディレクトリ RTCwork に、次のような内容のファイル rtc.conf を作成し配置します。 -->
<!--  -->
<!-- /usr/share/OpenRTM-aist/examples の下にあるrtc.confはこの例では使えませんので、~/RTCWork/rtc.conf として新たに作成してください。 -->
<!--  -->
<!-- $ cd ~/RTCwork -->
<!-- $ vi rtc.conf -->
<!--  -->
<!-- 作成するファイルの内容は以下のようになります。 -->
<!--  -->
<!-- corba.nameservers: localhost -->
<!-- naming.formats: %h.host_cxt/%n.rtc -->
<!-- logger.enable: NO -->
<!-- example.ConsoleOut.config_file: consout.conf -->
<!-- example.ConsoleIn.config_file: consin.conf -->
<!-- CENTER:''rtc.conf'' -->

システムで IPv6 が設定されている場合、**localhost** というホスト名が正しく機能しない場合があります。
その場合、localhost の代わりに**127.0.0.1**に置き換えてください。

### ConsoleInComp の起動

ターミナルを起動して ConsoleInComp を起動します。

```
 $ sh /home/openrtm/OpenRTM-aist/1.1/examples/ConsoleIn.sh
 
 Creating a component: "ConsoleIn"....
 succeed.
 =================================================
  Component Profile
 -------------------------------------------------
 InstanceID:     ConsoleIn0
 Implementation: ConsoleIn
 Description:    Console input component
 Version:        1.0
 Maker:          Noriaki Ando, AIST
 Category:       example
   Other properties   
 =================================================
 =================================================
 Port0 (name): 
 ConsoleIn0.out
 -------------------------------------------------
 - properties -
 port.port_type:DataOutPort
 dataport.data_type:TimedLong
 dataport.subscription_type:new, flush, periodic
 dataport.dataflow_type:push,pull
 dataport.interface_type:corba_cdr
 -------------------------------------------------
```
 
   
<!-- 自分でビルド・インストールした場合は、 -->
<!--  -->
<!-- $ <source_dir>/OpenRTM-aist/examples/SimpleIO/ConsoleInComp -f ~rtc.conf -->
<!--  -->
<!-- などとして ConsoleInComp を起動します。 -->

### ConsoleOutComp の起動

ターミナルを起動して、同様に ConsoleOutComp を起動します。

```
 $ sh /home/openrtm/OpenRTM-aist/1.1/examples/ConsoleOut.sh
  
 Creating a component: "ConsoleOut"....
 succeed.
 =================================================
  Component Profile
 -------------------------------------------------
 InstanceID:     ConsoleOut0
 Implementation: ConsoleOut
 Description:    Console output component
 Version:        1.0
 Maker:          Noriaki Ando, AIST
 Category:       example
   Other properties   
 =================================================
 =================================================
 Port0 (name): 
 ConsoleOut0.in
 -------------------------------------------------
 - properties -
 port.port_type:DataInPort
 dataport.data_type:TimedLong
 dataport.subscription_type:Any
 dataport.dataflow_type:push,pull
 dataport.interface_type:corba_cdr
 -------------------------------------------------
```
 
 
 
<!-- 自分でビルド・インストールした場合は、同様に -->
<!--  -->
<!-- $ <source_dir>/OpenRTM-aist/examples/SimpleIO/ConsoleOutComp -f ~rtc.conf -->
<!--  -->
<!-- などとして ConsoleOutComp を起動します。 -->
<!--  -->
### RTSystemEditor の起動

RTSystemEditor を使って、RTコンポーネントの接続とアクティブ化を行います。
[こちら]({{ site.baseurl }}/en/download/tools/openrtp_1_1_0_rc5)から Eclipse 全部入りパッケージをダウンロードし解凍してください。

RTSystemEditor は Java Development Kit7 を使用します。以下のマニュアルを参考にインストールしてください。
また、Ubuntu 等では、デフォルトの Java 環境は OpenJDK が推奨されています。そうした場合、OpenJDK でも利用することは可能です。

  - [Java SE Development Kit 7](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)
  - [JDKインストールのためのヒント ]({{ site.baseurl }}/en/doc/installation/install_1_1/java_1_1/tips_jdk)

[こちら]({{ site.baseurl }}/en/doc/toolmanuals/rtsystemeditor-1_1_0)のページを参考にRTSystemEditorの起動してください。

### ネームサーバーの参照と確認

ネームサーバーへ接続し登録内容を確認します。
ネームサーバーへの接続は、左側の Name Service View のコンセント型アイコンのボタンをクリックし、ダイアログで

```
 localhost
 または
 localhost:2809
```

と入力します。(orbd のデフォルトのポート番号は2809です。)

<div align="center"><a href="c_unix100_NameServer_ja.png"><img src="c_unix100_NameServer_ja.png" width="70%;"></a></div>
<div align="center">ネームサーバへーの接続</div>

ネームサーバに登録された RTコンポーネントをシステムエディタに配置します。
左の Name Service View のConsoleOut0 および ConsoleIn0 を中央のエディタ上にドラッグアンドドロップします。
次に、コンポーネントの右端、左端に出ている突起上のアイコンを、片方からもう片方でドラッグアンドドロップします。
接続ダイアログが表示されますが、すべてデフォルトのままで結構ですので [OK] をクリックすると接続は完了します。

<div align="center"><a href="c_unix100_oneditor_ja.png"><img src="c_unix100_oneditor_ja.png" width="70%;"></a></div>
<div align="center">RTSystemEditorによるシステムの編集</div>

メニューの下の緑色の [再生] ボタンをクリックすると、エディタ上のすべてのコンポーネントがアクティブ化されます。

### 数値入力と出力の確認

ConsoleInComp と ConsoleOutComp のポートを接続したら、

```
 Please input number: 
```

というプロンプトが表示されるので、そこに数字を入力します。入力する数字は、short int に収まる範囲の数値を入力してください。

ConsoleInComp 側のターミナルに数字を打ち込むと、ConsoleOutComp 側のターミナルに、入力した数値が表示されます。
以上で、OpenRTM-aist-Java が正しくインストールされていることが確認できました。


