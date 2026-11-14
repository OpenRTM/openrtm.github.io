---
layout: page
title: 動作確認 (linux編)
---

<!-- Title: 動作確認 (Linux編) -->
インストールが正常に終了したら、付属のサンプルで動作テストをします。サンプルは、通常は以下の場所にあります。

- /usr/share/openrtm-1.1/example
- /usr/local/share/openrtm-1.1/example (ソースからビルドしてインストールした場合)
- /opt/local/share/openrtm-1.1/examples (Mac OS X に MacPorts でインストールした場合)

ソースからビルドした場合は、ソースディレクトリー以下の

- OpenRTM-aist/examples/<サンプルコンポーネントセット名>

にもあります。

サンプルコンポーネントセット SimpleIO を使って、OpenRTM-aist が正しくビルド・インストールされているかを確認します。

#contents


## サンプルコンポーネントセット SimpleIO

RT コンポーネント ConsoleInComp、ConsoleOutComp からなるサンプルセットです。
ConsoleInComp はコンソールから入力された数値を OutPort から出力するコンポーネント、ConsoleOutComp は InPort に入力された数値をコンソールに表示するコンポーネントです。
これらは、最も Simple な I/O (入出力) を例示するためのサンプルです。
ConsoleInComp の OutPort から ConsoleOutComp の InPort へ接続を構成し、これらの2つのコンポーネントをアクティブ化 (Activate) することで動作します。

以降、簡単のためサンプルは /usr/share/openrtm-1.1/example 以下にあるものとして説明を記述します。


## サンプルを使用したテスト

### ネームサーバーを起動

まず、コンポーネントの参照を登録するためのネームサーバーを起動します。
Linux などのパッケージで omniORB をインストールした場合、すでにシステムのサービスとしてネームサーバー (omniNames) が起動している場合があります。

すでに omniNames が起動している場合、このようになります。
```
 $ ps ax | grep omni
 1550  ?        Sl     0:00 /usr/bin/omniNames -errlog /var/log/omniorb4-nameserver.log
 18418 pts/2    S+     0:00 grep --color=auto omni
```

omniNames が起動していない場合はこのようになります。、

```
 $ ps ax | grep omni
 18418 pts/2    S+     0:00 grep --color=auto omni
```

omniNames が起動していない場合、rtm-naming コマンドでネームサーバーを起動します。

```
 $ rtm-naming
 Starting omniORB omniNames: ubuntu910:9876
 
 Thu Dec  3 18:52:14 2009:
 
 Starting omniNames for the first time.
 Wrote initial log file.
 Read log file successfully.
 Root context is  IOR:010000002b00000049444c3a6f6d672e6f72672f436f734e616d696e672f4e616d696e67436f6e746578744578743a312e30000001000000000000007400000001010200100000003139322e3136382e3130302e31323500942600000b0000004e616d6553657276696365000300000000000000080000000100000000545441010000001c0000000100000001000100010000000100010509010100010000000901010003545441080000004e8a174b01000fef
 Checkpointing Phase 1: Prepare.
 Checkpointing Phase 2: Commit.
 Checkpointing completed.
```

### rtc.conf の作成

テストのための RTC コンフィギュレーションファイル rtc.conf を作成し、配置します。
まず、適当な作業ディレクトリーを作ります。ここでは便利のため、ホームディレクトリー直下に RTCwork というディレクトリーを作業ディレクトリーとしておくことにします。
作業ディレクトリー RTCwork に、次のような内容のファイル rtc.conf を作成し配置します。

/usr/share/OpenRTM-aist/examples の下にある rtc.conf はこの例では使えませんので、`/RTCWork/rtc.conf` として新たに作成してください。

```
 $ cd ~/RTCwork
 $ vi rtc.conf
```

作成するファイルの内容は以下のようになります。

```
 corba.nameservers: localhost
 naming.formats: %h.host_cxt/%n.rtc
 logger.enable: NO
 example.ConsoleOut.config_file: consout.conf
 example.ConsoleIn.config_file: consin.conf
```
<div align="center"><strong>rtc.conf</strong></div>

システムで IPv6 が設定されている場合、**localhost**というホスト名が正しく機能しない場合があります。
その場合、localhost の代わりに**127.0.0.1**に置き換えてください。

### ConsoleInComp の起動

ターミナルを起動して、次のように前節で作成した rtc.conf を参照させる形で ConsoleInComp を起動します。

```
 $ /usr/share/openrtm-1.1/example/ConsoleInComp -f rtc.conf 
 Creating a component: "ConsoleIn"....succeed.
 =================================================
  Component Profile
```
 -------------------------------------------------
```
 InstanceID:     ConsoleIn0
 Implementation: ConsoleIn
 Description:    Console input component
 Version:        1.0
 Maker:          Noriaki Ando, AIST
 Category:       example
   Other properties   
 =================================================
 =================================================
 Port0 (name): out
 -------------------------------------------------
 - properties -
 port.port_type: DataOutPort
 dataport.data_type: TimedLong
 dataport.subscription_type: flush,new,periodic
 dataport.dataflow_type: push
 dataport.interface_type: corba_cdr
 -------------------------------------------------
 
```

自分でビルド・インストールした場合は、

```
 $ <source_dir>/OpenRTM-aist/examples/SimpleIO/ConsoleInComp -f ~rtc.conf
```

などとして ConsoleInComp を起動します。

### ConsoleOutComp の起動

ターミナルを起動して、同様に先ほど作成した rtc.conf を参照する形で ConsoleOutComp を起動します。

```
 $ /usr/share/openrtm-1.1/example/ConsoleOutComp -f rtc.conf 
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
 Port0 (name): in
 -------------------------------------------------
 - properties -
 port.port_type: DataInPort
 dataport.data_type: TimedLong
 dataport.subscription_type: Any
 dataport.dataflow_type: push,pull
 dataport.interface_type: corba_cdr
 ------------------------------------------------- 
```

自分でビルド・インストールした場合は、同様に

```
 $ <source_dir>/OpenRTM-aist/examples/SimpleIO/ConsoleOutComp -f ~rtc.conf
```

などとして ConsoleOutComp を起動します。

### RTSystemEditor の起動

RTSystemEditor を使って、RTコンポーネントの接続とアクティブ化を行います。RTSystemEditor はツール OpenRTP に含まれておりますので、[こちら]({{ site.baseurl }}/ja/download/tools/openrtp_1_1_0_rc5)から Eclipse 全部入りパッケージをダウンロードし解凍してください。

RTSystemEditor は Java Development Kit7 を使用します。以下のマニュアルを参考にインストールしてください。また、Ubuntu 等では、デフォルトの Java 環境は OpenJDK が推奨されています。そうした場合、OpenJDK でも利用することは可能です。

  - [Java SE Development Kit 7](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)~
  - [JDKインストールのためのヒント ]({{ site.baseurl }}/ja/doc/installation/install_1_1/java_1_1/tips_jdk)

[こちら]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_1_0)のページを参考に RTSystemEditor の起動してください。

### ネームサーバーの参照と確認

ネームサーバーへ接続し登録内容を確認します。
ネームサーバーへの接続は、左側の Name Service View のコンセント型アイコンのボタンをクリックし、ダイアログで

```
 localhost
 または
 localhost:2809
```

と入力します。(omniNamesのデフォルトのポート番号は2809です。)

<div align="center"><a href="c_unix100_NameServer.png"><img src="c_unix100_NameServer.png" width="50%;;"></a></div>
<div align="center">ネームサーバーへの接続</div>

ネームサーバーに登録された RTコンポーネントをシステムエディタに配置します。
左の Name Service View の ConsoleOut0 および ConsoleIn0 を中央のエディタ上にドラッグアンドドロップします。次に、コンポーネントの右端、左端に出ている突起上のアイコンを、片方からもう片方でドラッグアンドドロップします。
接続ダイアログが表示されますが、すべてデフォルトのままで結構ですので [OK] をクリックして接続は完了します。

<div align="center"><a href="c_unix100_oneditor.png"><img src="c_unix100_oneditor.png" width="50%;;"></a></div>
<div align="center">RTSystemEditorによるシステムの編集</div>

メニューの下の緑色の [再生] ボタンをクリックすると、エディタ上のすべてのコンポーネントがアクティブ化されます。

### 数値入力と出力の確認

ConsoleInComp と ConsoleOutComp のポートを接続したら、

```
 Please input number: 
```

というプロンプトが現れるので、そこに数字を入力します。入力する数字は、short int に収まる範囲の数値を入力してください。

ConsoleInComp 側のターミナルに数字を打ち込むと、ConsoleOutComp 側のターミナルに、入力した数値が現れます。
以上で、OpenRTM-aist が正しくインストールされていることが確認できました。


