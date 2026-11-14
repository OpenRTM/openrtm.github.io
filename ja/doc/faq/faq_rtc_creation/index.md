---
layout: page
title: rtコンポーネント作成に関する faq
---


<!-- Adoc/faq/faq_rtc_creation -->

<!-- Title: RTコンポーネント作成に関する FAQ -->
#contents(4)

### サービスポートを持つ RTC を Eclipse でビルドするとエラーが表示される
RTCBuilder でサービスポートを持つ RTC を生成した場合、Eclipse のビルドで以下のような「***POA を型に解決できません」エラーが表示されます。

<div align="center"><a href="Error_POA.png"><img src="Error_POA.png" width="70%;"></a></div>

**原因：**
idl コンパイルは、サービスポートで使用する idlファイルから javaファイル(スタブソース、スケルトンソース、各種ユーティリティソース)を生成します。
idl コンパイルが実行される前にビルドが実行されると、ビルドに必要なこれらのソースファイル(javaファイル)が見つからずエラーになります。

**対処方法：**
Eclipse のパッケージエクスプローラから「build_JavaRTCTest.xml」を右クリックして [実行] > [antビルド] 実行してください。
これにより、idl コンパイルが実行され、javaファイルが生成されます。
「build_JavaRTCTest.xml」実行後に、[F5] キーなどでプロジェクトを更新すると、エラー表示が消えます。
<br>
<br>

### RTC がシステムエディタ上に表示されない
ネットワークの切り替え時に発生する現象で、NameService と RTC を再起動することで表示されるようになります。
<br>
<br>

### データポートで約2MB以上のデータを送りたい
画像データなどをデータポートで送る際、1回に送られるデータサイズ約2MBを超える場合には注意が必要です。
<br>
omniORBでは、giop (General Inter-ORB Protocol)で扱えるサイズはデフォルトで"2097152B(2MB)"となっています。
このサイズを超えるデータを1回で送ろうとすると、giop の制限のため正しいデータを送ることができません。
<br>
<br>
この最大サイズを変更するためには、下記の2つの方法があります。
<br>
<br>
- **rtc.conf にて最大サイズを指定する場合**
```
 # file: rtc.conf
 corba.nameservers: localhost
 naming.formats: %n.rtc
 corba.args: -ORBgiopMaxMsgSize 3145728 ※この行を追加 (Maxサイズを3Mに指定)
```
<br>
- **環境変数にて指定する場合**
```
  export ORBgiopMaxMsgSize=3145728
```

※ giopMaxMsgSize を指定する場合、server、client 共に (対になるコンポーネント) 設定する必要があります。
<br>
(omniORB configuration and API)<br>
[http://omniorb.sourceforge.net/omni41/omniORB/omniORB004.html](http://omniorb.sourceforge.net/omni41/omniORB/omniORB004.html)

<br>

### Raspberry Pi との接続時に、IPアドレスが割り当てられない
Raspberry Pi を再起動してください。
<br>
<br>

### Raspberry Pi 上のデータポートと PC上のデータポートを接続すると接続エラーになる
Raspberry Pi が起動する前に PC側の NameService を立ち上げていたためと思われます。再度、NameService を立ち上げ直してください。
<br>
<br>

### Raspberry Pi に接続した場合に RTC と通信できなくなる
ウイルス対策ソフトの影響の可能性があります。WiFi 設定を WPA2 に変更してください。
<br>
<br>

### Raspberry Pi 側のサービスに ConsoleOut が表示されない

- **ネームサーバの問題**
  - ネームサーバのエンドポイントアドレスが不正な場合このような現象が起きます。rtm-naming で再度ネームサーバを起動しなおすと解決する場合があります。
このほか、Raspberry Pi の有線LANと無線LAN等2つ以上のネットワークインターフェースがある場合、PCとの接続に使用するどちらかのネットワークのみを使うように設定することで解決するケースもあります。

- **コンポーネントの問題**
  - コンポーネントが読み込んだ設定ファイル(rtc.conf)に localhost 以外のネームサーバが登録されている場合が考えられます。corba.nameservers:  localhost と記述するなど localhost のネームサーバにコンポーネントを登録するよう設定してください。
また、Raspberry Pi の有線LANと無線LAN等2つ以上のネットワークインターフェースがある場合、PCとの接続に使用するどちらかのネットワークのみを使うように設定することで解決するケースもあります。
<br>
<br>


### PCにネットワークインターフェースが2つ以上ある場合、RTSystemEditor で接続できない、反応しなくなるなどの問題がある

- **PC側のコンポーネントの問題**
  - PCにネットワークインターフェースが2つ以上ある場合、Raspberry Pi で使用しない側のインターフェースアドレスがコンポーネントの参照として利用されている場合このような現象が起こります。
エンドポイントを設定するため、rtc.conf に使用する方の IPアドレスを以下のように設定します。

```
 corba.endpoints: 192.168.11.20
```

ただし、Vista 以降の Windows では、C:\Program Files 以下のファイルは簡単には編集ができなくなっています。c:\tmp など適当なディレクトリーに ConsoleIn.exe と rtc.conf をコピー(あるいは新たに作成)するなどして、対処してください。

- **Raspberry Pi側のコンポーネントの問題**
  - Raspberry Pi の有線LANと無線LAN等2つ以上のネットワークインターフェースがある場合で、それぞれが別のネットワークにつながっている場合、上述のPCと同様の問題が起こります。エンドポイントを設定するため、rtc.conf に以下のように記載します。

```
 corba.endpoints: 192.168.11.21
```
<br>
<br>

### RTコンポーネントのインスタンス命名規則について
RTコンポーネントのインスタンス命名規則は、**[RTコンポーネント type名] + [数字 (0、1、2、3...)]** のようになっています。
<br>
<br>
RTコンポーネント type名は、rtc-template で --type-name オプションで指定した名前、もしくは、コンポーネントプロファイル (通常は *.cppファイルの先頭に記述) "type_name" に指定されている名前です。
番号は、同一マネージャ上で生成されたコンポーネントに対して、0、1、2、3...のような連番を振ります。
<br>
<br>
同一のコンポーネントが別プロセスで複数起動された場合には、インスタンスの番号はそれぞれ 0 から始まるので、同一の名前のコンポーネントが複数起動されたことになります。
場合によっては、ネームサービスに同一の名前として複数のコンポーネントが登録されることになり、前に登録されたものは後で登録されたもので上書きされます。
<br>
<br>
これを回避するには、以下の方法があります。

- **同一プロセスで複数のコンポーネントを起動させる**
- **rtc.conf の naming.formats オプションでそれぞれ衝突しない名前フォーマットを指定する**

<br>


### 標準以外のデータ型を InPort / OutPort で使うには
通常 OpenRTM-aist では rtm/idl/BasicDataType.idl で定義されている
<br>
<br>
TimedShort、TimedLong、TimedUShort、TimedULong、TimedFloat、TimedDouble、TimedChar<br>
TimedBooleanTimedOctet、TimedString、TimedShortSeq、TimedLongSeq、TimedUShortSeq<br>
TimedULongSeq、TimedFloatSeq、TimedDoubleSeq、TimedCharSeq、TimedBooleanSeq<br>
TimedOctetSeq、TimedStringSeq
<br>
<br>
の20種類のデータ型を InPort および OutPort のデータ型として使用することができます。
<br>
<br>
これ以外のデータ型を定義し InPort / OutPort で使用したい場合は、そのデータ型を IDL で定義し、コンポーネントをコンパイルするときに同時にコンパイル・リンクする必要があります。<br>
<br>
仮に画像を格納するため、サイズ(width, height)、デプス、イメージデータ、各メンバを持つデータ型を使用したいとします。IDL ではこのデータ型を以下のように定義します。<br>
```
 #include <BasicDataType.idl>
 module RTC
 {
   struct TimedImage
   {
     Time tm;
     long width;
     long height;
     long depth;
     sequence<octet> data;
   };
 };
```
Time型は OpenRTM で定義されているタイムスタンプのための型です。無くても構いませんが、含めておいたほうが良いでしょう。
これを TimedImage.idl として、ファイルに保存します。
<br>
<br>
このファイルをコンポーネントを作成するディレクトリーにおきます。
次に、rtc-template  でコンポーネントを作成します。その際、この IDL ファイルを --consumer-idl オプションに指定します。
```
 rtc-template -bcxx
   --module-name=ConsoleIn --module-type='DataFlowComponent'
   --module-desc='Console input component'
   --module-version=1.0 --module-vendor='Noriaki Ando, AIST'
   --module-category=example
   --module-comp-type=DataFlowComponent --module-act-type=SPORADIC
   --module-max-inst=10 --outport=out:TimedImage
   --consumer-idl=TimedImage.idl
```

<br>
この例では、TimedImage.idl で定義した TimedImage型を OutPort のデータ型として用いています。生成されたコードをコンパイルします。

<br>
```
 make -f Makefile.ConsoleIn
```
これで、TimedImage.idl が IDL コンパイラでコンパイルされ、スタブが生成されると共に、コンポーネントにリンクされます。
コンポーネント内でのデータの使用方法は通常のものと同じです。
これと同じデータ型を他のコンポーネントでも使用したい場合は、この IDL ファイルだけコピーして、同様に rtc-template の --consumer-idl オプションでファイルを指定してください。
これで、このデータ型を用いてコンポーネント間で通信できるようになります。

<br>


<!-- **入出力ポートのデータ型の選択  -->
<!-- **ConsoleOut でコールバックが必要な訳は？ -->

&aname(errorjavaJDK);
### 新規 Java プロジェクトが JDK6(1.6)準拠として作成できない
新規プロジェクトで Java プロジェクトを作成しようとすると、次のようなダイアログが表示されて、JDK準拠が選択できないことがあります。
<br>
RTCBuilder を利用し、Java で RTコンポーネント作成するプロジェクトでは、このダイアログにおいて指定する JRE（Java実行環境）を JDK 内に含まれている JRE とする必要があります。このままでは JDK内の JRE を選択できないため設定を変更します。
<br>
<br>

1. 下図のように JRE フレーム内の「JREを構成...」リンクをクリックします。（あるいは、一旦このダイアログをキャンセルして Eclipse のメニューバーの[ウィンドウ] > [設定] > 「設定」ダイアログの左のツリー部分から「Java」の下の「インストール済みのJRE」を選択します。）
<br>
<br>
<div align="center"><a href="new_project_name_ja.png"><img src="new_project_name_ja.png" width="50%;"></a></div>
<div align="center"><strong>新規Javaプロジェクトのダイアログ（JDKの選択がない場合）</strong></div>
<br>
2. [追加] ボタンをクリックします。
<br>
<div align="center"><a href="new_JRE_setting_ja.png"><img src="new_JRE_setting_ja.png" width="80%;"></a></div>
<div align="center"><strong>インストール済みのJREのダイアログ（JDKの表示はまだない）</strong></div>
<br>
3.「標準VM」 を選択して [次へ] ボタンをクリックします。
<br>
<div align="center"><a href="new_JRE_VM_setting_ja.png"><img src="new_JRE_VM_setting_ja.png" width="60%;"></a></div>
<div align="center"><strong>JREの型の選択のダイアログ</strong></div>
<br>
4. [ディレクトリー] ボタンをクリックして、JDK6 までのパスを選択します。（参考：通常、JDK6 のパスはC:\Program Files\Java\jdk1.6.0_XX）
<br>
<div align="center"><a href="add_JRE_ja.png"><img src="add_JRE_ja.png" width="50%;"></a></div>
<div align="center"><strong>JRE の追加ダイアログ</strong></div>
<br>
<div align="center"><a href="select_JDK_ja.png"><img src="select_JDK_ja.png" width="70%;"></a></div>
<div align="center"><strong>JDK6 までのパスを選択し、「JRE の追加」ダイアログに JDK を参照させる</strong></div>
<br>
5. JDK までのパスの参照に成功すると、「JRE の追加」ダイアログが下図のようになりますので、[完了] ボタンをクリックしてダイアログを閉じます。
<br>
<div align="center"><a href="load_JDK_ja.png"><img src="load_JDK_ja.png" width="50%;"></a></div>
<div align="center"><strong>JDK6 のパス参照に成功</strong></div>
<br>
6.「インストール済みの JRE」ダイアログに戻ってくるので（JDK が追加された状態で）、下図のようにアクティブとする JRE にチェックを入れ、[OK] ボタンをクリックします。
<br>
<div align="center"><a href="set_active_JDK_ja.png"><img src="set_active_JDK_ja.png" width="80%;"></a></div>
<div align="center"><strong>「インストール済みの JRE」ダイアログに JDK が追加されているので、アクティブチェックを JDK に変更</strong></div>
<br>
7.「新規 Java プロジェクト」のダイアログで JDK が選択できるようになります。
<br>
<div align="center"><a href="SelectJDKasJRE_ja.png"><img src="SelectJDKasJRE_ja.png" width="50%;"></a></div>
<div align="center"><strong>「JRE」としてJDK内の JRE で構成するように指定する</strong></div>
<br>


&aname(Antbuild);
### 任意のフォルダーにクラスパスを設定して Ant ビルドを行う方法は？
環境変数 RTM_JAVA_ROOT に OpenRTM-aist (Java版)ライブラリ「OpenRTM-aist-X.X.X.jar」（X.X.Xはバージョンです。）が存在するフォルダー「jar」へのベースパス（親フォルダまでのパス）を設定し、それをクラスパスの設定に用いることで、OpenRTM-aist (Java版)は RTCBuilder でのコード生成と Ant でのビルド実行の連携を築いています。したがって、RTM_JAVA_ROOT は OpenRTM-aist (Java版) のライブラリフォルダーへのパス（ベースパス）を必ず保持していなければならないわけです。ところが、RTM_JAVA_ROOT は本来、OpenRTM-aist (Java版) のインストール場所を指すものなので、結果 OpenRTM-aist (Java版) のライブラリと他のコンポーネント（ドキュメント・サンプル・ユーティリティツール類）は常にそのフォルダー構造を保っていなければなりません。
<br>
<br>
環境変数 RTM_JAVA_ROOT をクラスパス設定専用に使う方法も考えられます。OpenRTM-aist (Java版)のライブラリフォルダーを自由な位置に配置し、それに合わせて RTM_JAVA_ROOT 設定するという使い方もできるでしょう。ただし、この場合は、「環境変数 RTM_JAVA_ROOTをライブラリへのクラスパスの用途以外には使用していない」という保証が必要です。
<br>
<br>
そこで、何らかの事情で RTM_JAVA_ROOT が指示しているところとは別のところにクラスパスを設定したい場合、クラスパスをどのように設定したらよいのかをここで説明します。
<br>
<br>

- **Eclipse の Ant 設定ダイアログを呼び出す**
<br>
Eclipse の通常左のビュー「パッケージ・エクスプローラー」から build_<CompName>.xml を右クリックして、[実行] > [Antビルド...] を選択する。
<br>
<br>
<div align="center"><a href="Call_Ant_Setting_ja.png"><img src="Call_Ant_Setting_ja.png" width="80%;"></a></div>
<div align="center"><strong>Ant設定ダイアログを呼び出す</strong></div>

<br>

- **クラスパスの設定**<br>
1. Ant の設定ダイアログが表示されるので、「クラスパス」タブを選択する。
<br>
<br>
<div align="center"><a href="Ant_Setting_Classpath_ja.png"><img src="Ant_Setting_Classpath_ja.png" width="80%;"></a></div>
<div align="center"><strong>「クラスパス」タグを選択する</strong></div>

<br>

2.「ユーザーエントリ」を一度選択し、その後「外部 JAR の追加」ボタンをクリックする。
<br>
<br>
<div align="center"><a href="Ant_External_Jar_ja.png"><img src="Ant_External_Jar_ja.png" width="80%;"></a></div>
<div align="center"><strong>外部JARの追加</strong></div>

<br>

3.「JAR の選択」ダイアログが現れたら、目的の JAR ライブラリまでのパスを指定する。結果、下図のように追加した JAR ライブラリが Ant の設定ダイアログに表示される。
<br>
<br>
<div align="center"><a href="Ant_Add_Jar_ja.png"><img src="Ant_Add_Jar_ja.png" width="80%;"></a></div>
<div align="center"><strong>追加された JAR</strong></div>

<br>

**重要な留意点**<br>
環境変数 RTM_JAVA_ROOT は必ず設定しなければなりません（ただし、ダミーでも可）。クラスパスを任意に指定することで、たとえ RTM_JAVA_ROOT の設定が不要となったとしても、その設定削除をしたり、設定そのものをしなかったりするとビルド時にエラーとなります。また、RTM_JAVA_ROOT が指し示すパスの先には（空でもいいので）必ず「jar」という名前のフォルダーが実在していなければなりません。
<br>
<br>


&aname(Antbuilderror);
### Java で Ant を使ってコマンドラインからビルドするときに例外が表示される
Java で Ant を実行すると以下のような例外が表示される場合があります。

```
 >ant -f build_ModuleName.xml
 Exception in thread "main" java.lang.UnsupportedClassVersionError: org/apache/to
 ols/ant/launch/Launcher : Unsupported major.minor version 52.0
        at java.lang.ClassLoader.defineClass1(Native Method)
        at java.lang.ClassLoader.defineClass(ClassLoader.java:800)
        at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
        at java.net.URLClassLoader.defineClass(URLClassLoader.java:449)
        at java.net.URLClassLoader.access$100(URLClassLoader.java:71)
        at java.net.URLClassLoader$1.run(URLClassLoader.java:361)
        at java.net.URLClassLoader$1.run(URLClassLoader.java:355)
        at java.security.AccessController.doPrivileged(Native Method)
        at java.net.URLClassLoader.findClass(URLClassLoader.java:354)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:425)
        at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:308)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:358)
        at sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:482)
```

**原因：**Java のバージョンが古い可能性があります。<br>
Java と Ant のバージョン要件は以下のリンクを参照してください。必要に応じてアップデートを実行してください。<br>
<br>
[Java と Ant のバージョン要件](http://ant.apache.org/faq.html#java-version)
<br>


