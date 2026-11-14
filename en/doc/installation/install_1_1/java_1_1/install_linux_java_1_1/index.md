---
layout: page
title: linuxへのインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: Linuxへのインストール -->
#contents


## OpenRTM-aist-Javaのインストール 
<!-- &color(red){''※'' すでに OpenRTM-aist-0.4 を使用されている方へ}; -->
<!--  -->
<!-- 新しい OpenRTM-aist-Java-1.0 では以前の 0.4.2 で使用していた RtcLink、RTSystemEditor は使えません。すでに、Eclipse 上に RtcLink プラグイン、又は RTSystemEditor (0.4.2用) プラグインをインストールしている方は、OpenRTM-aist-1.0 Java を使う場合は、必ず RTSystemEditorも1.0.0 に対応したものに差し替えてください。 -->
<!-- #br -->
<!-- 参考： -->
<!-- -[[''FAQ:'' Q. RtcLink 上で RTC のポートが表示されない（Java版） :RtcLink.#RtcLinkport]] -->

### 動作条件 &aname(jyouken);
OpenJDK7 または oracleJDK7
<!-- -[[Java Development Kit 7.0(JDK 7):http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html]] -->
<!-- &color(red){※ Java1.4１では動作しません。}; -->

### インストールの流れ（概要）
インストールは次の3つの要件が整うことで完了します。
- java、javac といった Java のコマンドが動作する　→　[[Javaのインストール >#instjava]]
- OpenRTM-aist-Java が展開・配置されている（場所は任意）　→　[[OpenRTM-aist-Java のインストール >#instrtm]]
- 環境変数 RTM_JAVA_ROOT が設定されている　→　[[環境変数の設定 >#hensu]]

<!-- 本ページではこれらを以下で順に説明するとともに、[[インストール後の動作確認の方法 >#checkinst]]や[[RTCのサンプルコンポーネントの紹介 :/node/304#samplecomponent]]をしています。 -->


&aname(instjava);
### Java のインストール 
OpenRTM-aist-Java は、JDK7 上で動作します。oracle の対象プラットフォーム用 JDK については下記サイトなどを参考にしてください。
- [Java SE Development Kit 7u75 ダウンロードトップ ](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)
<!-- -[[JDK5 トップ(English):http://java.sun.com/javase/downloads/index_jdk5.jsp]] -->

### インストールの実行 
各ディストリビューションについて JDK 7 のインストール方法を[ JDK インストールのためのヒント  ](/en/content/tipsjava100)にまとめましたので参考にしてください。なお、Java のインストールはスーパーユーザーで実行してください。


<br>
<!-- &color(red){''※ Fedora Core への Java のインストールについては注意が必要です:''}; -->
※ Fedora でエラーになった場合は、以前の情報ですが下記が役立つかもしれません

　→ [**FAQ:** Java をインストールする際の FedoraCore での対応について ]({{ site.baseurl }}/en/doc/faq/trouble_shooting#javafedora)

　→ [**FAQ:** Q. Fedora Core 上でRtcLink の NameService View にエラーがでる ]({{ site.baseurl }}/en/doc/faq/faq_rtp_tools#fedoraNS)
<br>

### インストールの確認
ターミナルを起動し、
```
 $ java -version
```
と入力します。インストールした Java のバージョンが表示されればインストールは完了です。

```
 java version "1.7.0_75"
 OpenJDK Runtime Environment (IcedTea 2.5.4) (7u75-2.5.4-1~trusty1)
 OpenJDK Client VM (build 24.75-b04, mixed mode, sharing)
```


<!-- #br -->
<!--  -->
<!-- &color(red){''◆参考:''}; -->
<!-- -[[''FAQ:'' Java をインストールする際の FedoraCore での対応について >/node/151#javafedora]] -->
<!-- -[[''FAQ:'' Q. Fedora Core 上で RtcLink の NameService View にエラーがでる >RtcLink.#fedoraNS]] -->



&aname(instrtm);
### zipファイルのダウンロードと解凍 
[こちら ](/en/content/openrtm-aist-java-110-release#winpkg)から「 jar ファイルおよびサンプル」をダウンロードし、zip ファイルを任意の場所に解凍します。
解凍先は任意でかまいませんが、ディレクトリー構造は変更しないでください**※**。
また、この解凍先に含まれる「jar」フォルダーへのパスは次に取り上げるシステム環境変数 RTM_JAVA_ROOT に設定しなければなりません。

**※** 何らの事情で、解凍後のフォルダー構造を自由な配置・自由な選択としたい場合は[こちら ]({{ site.baseurl }}/en/doc/casestudy/rtc_development/about_rtc_creation#Antbuild)を参照してください。

<br>
参考：

　→ [**FAQ:** Q. 任意のフォルダーにクラスパスを設定して Ant ビルドを行う方法は？ ]({{ site.baseurl }}/en/doc/casestudy/rtc_development/about_rtc_creation#Antbuild)


&aname(hensu);
## 環境変数の設定 
環境変数の設定を行います。
ログインシェルが bash の場合は .bashrc を、csh の場合は .cshrc を…など適宜設定ファイルを選択し、次のような設定を記述しておきます。
または、個々のユーザーに対してではなくシステムワイドに設定を行いたい場合には、設定ファイルとして /etc/profile などを選択する方法もあります**※**。
- 変数名:RTM_JAVA_ROOT
- 変数値:解凍ディレクトリー以下に含まれる「jar」ディレクトリー**※※**までのベースパス（「jar」ディレクトリーの**親ディレクトリー**へのフルパス）


例えば、ログインシェルが bash の場合で、OpenRTM-aist-Javaを/usr/lib 以下に解凍した場合を考えたとき、.bashrc（あるいは /etc/profile **※**）の末尾に次の一文を追加します。
```
 export RTM_JAVA_ROOT=/usr/lib/OpenRTM-aist/<version>
```
この設定ファイルの編集が完了した時点で、

```
 > source `/.bashrc`
```
とするか（.bashrc に環境変数を設定した場合）、あるいはシステムを再起動します。

<br>
**※** 環境変数 RTM_JAVA_ROOTを.bashrc（bash の場合）などのユーザー設定にしたのか、あるいは、/etc/profile（bashの場合）などにシステムワイドに設定したのかで、GUI ツールである Eclipse の起動方法が変わってきます。 →　[Eclipse の起動方法 ]({{ site.baseurl }}/en/doc/faq/faq_rtp_tools#eclipse)を参照

**※※** 解凍時には「jar」ディレクトリーはクラスライブラリ「OpenRTM-aist-X.X.X.jar」(X.X.Xはバージョン)と「commons-cli-1.1.jar」の二つのファイルを含んだ状態で、「OpenRTM-aist\<version>」の直下にあります。
したがって、ディレクトリー構造を変えなければ、環境変数 RTM_JAVA_ROOT は必ずその値の末尾に「OpenRTM-aist\<version>」を持つという形になります。
<br>

<!-- なお、カレントユーザーに対してのみインストールする場合は、上記設定を｢システム環境変数」あるいは｢ユーザー環境変数｣のどちらかに行えばよく、特に、特権を持たないユーザー（制限ユーザー）としてインストールする場合にはこのことを利用します。 -->
すなわち、制限ユーザーがインストールする場合には｢システム環境変数」の設定が追加・変更できないので、上記設定を｢ユーザー環境変数｣に対して行うことになります。

<br>
<!-- *** インストールの確認 &aname(checkinst); -->
<!-- インストール時に配置したディレクトリー以下に RTコンポーネントのサンプルが用意されています。｢examples｣ディレクトリー内にあるサンプルを使用して、インストールを確認します。 -->
実行するには、ターミナルを起動し、カレントを｢examples｣ディレクトリーに移してから、該当するシェルスクリプトを起動してください。
<!-- #br -->
<!-- - インストール確認手順 -->
<!-- :1. NameServerの起動：｢start-orbd.sh｣を実行| -->
<!-- :2. ConsoleInサンプルの起動：｢ConsoleIn.sh｣を実行| -->
<!-- :3. ConsoleOutサンプルの起動：｢ConsoleOut.sh｣を実行| -->
<!--  -->
<!-- :4. RTコンポーネントの接続：｢Connector.sh｣を実行| -->
<!--  -->
<!-- :5. ConsoleIn側のウィンドウに| -->
<!-- Please input number: -->
<!-- :　というプロンプトが現れるので、そこに数字を入力する| -->
<!-- :6. その数字がConsoleOut側のウィンドウに表示されればインストールは成功です。| -->
<!--  -->
<!--  -->
<!-- #br -->
<!-- #br -->
<!--  -->
<!-- #ref(OpenRTM-javaComfirm.png,nolink,center) -->




## zip ファイルを解凍して展開される内容
```
 +--<install_dir>
     +--OpenRTM-aist
        +--<version>
           +--jar
           +--examples
           +--JavaDoc
           +--JavaDocEn
```
### jar
OpenRTM-aist-Java と 必要な jar ファイルが含まれています。
- jar/OpenRTM-aist-X.X.X.jar  （X.X.X はバージョン）
- jar/commons-cli-1.1.jar  
- jar/rtcd.jar  
- jar/rtcprof.jar

### examples
サンプルの class ファイルとそれを起動するためのシェルスクリプトとソースコードが含まれています。
- サンプルの class ファイル
```
 examples/RTMExamples/SeqIO/SeqIn.class
 examples/RTMExamples/SeqIO/view/SeqView.class
 examples/RTMExamples/SeqIO/view/RootPane.class
 examples/RTMExamples/SeqIO/view/SeqViewApp.class
 以下 省略
```

- サンプルを起動するためシェルスクリプト
```
 examples/AutoTestIn.sh
 examples/AutoTestOut.sh
 examples/Composite.sh
 examples/ConfigSample.sh
 examples/Connector.sh
 examples/ConsoleIn.sh
 examples/ConsoleOut.sh
 examples/ExtConnector.sh
 examples/ExtConsoleIn.sh
 examples/ExtConsoleOut.sh
 examples/GUIIn.sh
 examples/MyServiceConsumer.sh
 examples/MyServiceProvider.sh
 examples/SeqIn.sh
 examples/SeqOut.sh
 examples/SinCosOut.sh
 examples/rtcd_java.sh
 examples/start-orbd.sh
```

- サンプルのソースコード
```
 examples/RTMExamples/SeqIO/SeqInImpl.java
 examples/RTMExamples/SeqIO/SeqOut.java
 examples/RTMExamples/SeqIO/view/RootPane.java
 examples/RTMExamples/SeqIO/view/SeqView.java
 以下 省略
```

### JavaDoc
日本語のクラスリファレンス（Javadoc HTML 形式）が含まれています。

### JavaDocEn
英語のクラスリファレンス（Javadoc HTML 形式）が含まれています。

ここまで確認できたら[動作確認（Linux 編）]({{ site.baseurl }}/en/doc/installation/install_1_1/java_1_1/test_linux_java_1_1)へ進みましょう。


