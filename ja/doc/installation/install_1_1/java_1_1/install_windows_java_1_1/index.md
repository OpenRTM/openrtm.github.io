---
layout: page
title: windows へのインストール
---

init
<!-- Title: Windows へのインストール -->
#contents

openrtm.org では Windows 用の msi (Microsoft Windows インストーラー)パッケージを提供しています。 msi パッケージを利用することで、RTSystemEditor といったツールも同時にインストールすることができます。


<!-- 通常インストールでは、インストーラを使用した方が便利でしょう。また、インストールの自由度を確保するために、必要なOpenRTM-aist-JavaライブラリコンポーネントをまとめたZipファイルも用意してあります。ユーザ独自の配置・組み合わせでインストールしたい場合などはこちらを利用してインストールすることもできます。 -->


## msi パッケージによるインストール

openrtm.org の[ダウンロードサイト]({{ site.baseurl }}/ja/download/openrtm-aist-java/openrtm-aist-java_1_1_2_release)から、msi パッケージをダウンロードします。msi パッケージには、必要な RTSystemEditor といったツールは含まれていますが、JDK は予めインストールしておく必要があります。

1.1.2 版からは一つの Windows 用インストーラーに3言語（C++、Java、Python）＋ツール（Eclipse＋rtshell）すべてが同梱されています。古いバージョンは予めアンインストールすることをお勧めします。
また、[ダウンロードサイト]({{ site.baseurl }}/ja/download/openrtm-aist-java/openrtm-aist-java_1_1_2_release)での赤字表記の注意書きをご覧ください。



### JDK のインストール
OpenRTM-aist-Java-1.1.2の動作には JDK8 を推奨しています。<br>
ダウンロードしたファイルを実行するとインストールが開始されます。途中、使用許諾やインストール先などを聞かれますので、お使いの環境に合わせて設定してください。
下記のインストール説明画像は JDK7 のものです。

<br>
[次へ] ボタンをクリックします。
<div align="center"><a href="oracleJDK7_001.jpg"><img src="oracleJDK7_001.jpg" width="60%;"></a></div>
<div align="center"><strong>Javaのインストール(1)</strong></div>
<br>
<br>
[次へ] ボタンをクリックします。
<div align="center"><a href="oracleJDK7_002.jpg"><img src="oracleJDK7_002.jpg" width="60%;"></a></div>
<div align="center"><strong>Javaのインストール(2)</strong></div>
<br>
<br>
[次へ] ボタンをクリックします。
<div align="center"><a href="oracleJDK7_003.jpg"><img src="oracleJDK7_003.jpg" width="60%;"></a></div>
<div align="center"><strong>Javaのインストール(3)</strong></div>
<br>
<br>
[閉じる] ボタンをクリックします。
<div align="center"><a href="oracleJDK7_004.jpg"><img src="oracleJDK7_004.jpg" width="60%;"></a></div>
<div align="center"><strong>Javaのインストール(4)</strong></div>
<br>

<br>
#### JDK のインストール確認
<!-- 環境変数の設定が完了後、インストールの確認を行います。 -->
コマンド プロンプト画面を表示（ [スタート] > [プログラム] > [アクセサリ] > [コマンド プロンプト] ）し、

 >java -version

と入力します。インストールした Java のバージョンが表示されればインストールは完了です。

<br>


<div align="center"><a href="java-version.png"><img src="java-version.png" width="60%;"></a></div>
<div align="center"><strong>インストールの確認(Windows)</strong></div>
<br>

- 参考：[FAQ: 「java -version」がインストールした JDK のバージョンと異なります。 ]({{ site.baseurl }}/ja/doc/faq/trouble_shooting#JDKver)


<br>
### OpenRTM-aist インストーラーの起動

手順については、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/quick_start_1_1_2) のページをご覧ください。

<br>
&aname(javazip);
<!-- *** zipファイルからのインストール -->
<!--  -->
<!-- Zipファイルのダウンロードと解凍を行います。&br; -->
<!--  -->
<!-- [[こちら >/ja/content/openrtm-aist-java-110-release]]から「jarファイルおよびサンプル」をダウンロードし、zipファイルを任意の場所に解凍します。解凍先は任意でかまいませんが、フォルダ構造は変更しないでください''※''。 &br; -->
<!-- また、この解凍先に含まれる「jar」フォルダへのパスは次に取り上げるシステム環境変数RTM_JAVA_ROOTに設定しなければなりません。 -->

<!-- :''※'' 何らの事情で、解凍後のフォルダ構造を自由な配置・自由な選択としたい場合は[[こちら >/node/159#Antbuild]]を参照してください。| -->

<!-- #br -->
<!-- -参考： [[''FAQ:'' Q. 任意のフォルダにクラスパスを設定してAntビルドを行う方法は？ >/node/159#Antbuild]] -->
<!--  -->
<!-- #br -->
<!--  -->
<!-- システム環境変数の設定を行います。&br; -->
<!-- ''｢スタート｣''メニューから、''｢設定｣''－''｢コントロールパネル｣''を選択し、表示されたコントロールパネル画面から''｢システム｣''を選択します。''｢システムのプロパティ｣''画面では''｢詳細設定｣''タブを選択し、画面下部の''｢環境｣''ボタンをクリックします。 -->
<!--  -->
<!-- #br -->
<!--  -->
<!--  -->
<!-- #ref(SystemProperty_ja.PNG,60%,center) -->
<!-- CENTER:''PATHの設定(システムプロパティ)'' -->
<!-- #br -->
<!-- #br -->
<!--  -->
<!--  -->
<!-- #ref(EnvVariable_ja.PNG,60%,center) -->
<!-- CENTER:''PATHの設定(環境変数)'' -->
<!-- #br -->
<!--  -->
<!-- :画面下部の''｢システム環境変数｣''から、''｢新規｣''ボタンをクリックし、''｢新しいシステム変数｣''画面で以下の内容を入力します。| -->
<!-- - 変数名:RTM_JAVA_ROOT -->
<!-- - 変数値:解凍先フォルダ以下に含まれる「jar」フォルダ''※''までのベースパス（「jar」フォルダの''親フォルダ''へのフルパス） -->
<!-- #br -->
<!--  -->
<!-- :　上記を入力後、''｢OK｣''ボタンをクリックし、''｢システムのプロパティ｣''画面を閉じます。| -->
<!--  -->
<!-- :''※'' 解凍時には「jar」フォルダはクラスライブラリ「OpenRTM-aist-<version>.jar」と「commons-cli-1.1.jar」の二つのファイルを含んだ状態で、「OpenRTM-aist\<version>」の下にあります。したがって、フォルダ構造を変えなければ、システム環境変数RTM_JAVA_ROOTは必ずその値の末尾に「OpenRTM-aist\<version>」を持つという形になります。| -->
<!-- #br -->
<!--  -->
<!-- :　なお、カレントユーザに対してのみインストールする場合は、上記設定を｢システム環境変数」あるいは｢ユーザー環境変数｣のどちらかに行えばよく、特に、特権を持たないユーザ（制限ユーザ）としてインストールする場合にはこのことを利用します。すなわち、制限ユーザがインストールする場合には｢システム環境変数」の設定が追加・変更できないので、上記設定を｢ユーザー環境変数｣に対して行うことになります。| -->
<!--  -->
<!-- #br -->
<!--  -->
<!-- &br; -->

## インストールの詳細
### インストーラーの作業内容
インストーラーは以下の作業を行います。

- インストールディレクトリー (デフォルトは C:\Program Files) 以下に各種ファイルをコピー
- スタートメニュー以下に OpenRTM-aist フォルダーを作成し各種ショートカットを設定
- 環境変数の設定
  - 32bit 用 msi 利用時の設定

```
 RTM_BASE=C:\Program Files (x86)\OpenRTM-aist\\
 RTM_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\\
 RTM_VC_VERSION=vc12
 RTM_JAVA_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\\
 OMNI_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\omniORB\4.2.1_vc12\\
 OpenCV_DIR=C:\Program Files (x86)\OpenRTM-aist\1.1.2\OpenCV2.4.11\\
 OpenRTM_DIR=C:\Program Files (x86)\OpenRTM-aist\1.1.2\cmake\\
```

- PATH への追加設定
  - 32bit 用 msi 利用時の設定

```
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\bin\vc12\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\omniORB\4.2.1_vc12\bin\x86_win32\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\OpenCV2.4.11\x86\vc12\bin\ 
```

インストール環境の設定を確認するスクリプトを提供しています。スクリプトの使い方、確認できる内容について下記ページで解説しています。

- http://openrtm.org/openrtm/ja/content/rtm-install-check-script

### インストールされるファイル
ファイルは以下のような構造でインストールされます。<br>
上記のインストール環境の設定を確認する[スクリプト]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/windows_install_test_bat)を実行すると、tree コマンドによる OpenRTM-aist ディレクトリー構造をログファイルに保存しますので、詳細を確認することができます。

```
 <install_dir>
   + OpenRTM-aist
      + 1.x.x  :旧バージョンのランタイム
      + <version>
         + bin: dll, lib, 各種コマンド
         + cmake: OpenRTMConfig.cmake
         + coil: coil ヘッダファイル
         + Components
            + CXX:
               + Examples: C++ サンプルコンポーネント
               + OpenCV: OpenCV のC++ サンプルコンポーネント
            + Java: Java サンプルコンポーネント
            + Python: Python サンプルコンポーネント
         + etc: rtc.confサンプル
         + ext: ComponentObserverConsumer
         + jar: OpenRTM-aist と必要な jar ファイル
         + jre: OpenJDK JRE
         + omniORB
         + OpenCV
         + rtm: OpenRTM-aist ヘッダファイル
            + idl: OpenRTM-aist IDLファイル
         + util
            + OpenRTP:
            + RTSystemEditor:
            + rtc-template: 

```
