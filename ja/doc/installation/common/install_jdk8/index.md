---

layout: page
title: jdk8のインストール

---


<!-- Title: JDK8のインストール -->
#contents(5)

OpenRTM-aist-Javaの実行には、CORBAと呼ばれる通信ミドルウェアが必要です。Javaにおいては、CORBAの機能はもともと標準機能として組み込まれていましたが、Java9以降はdeprecated (将来的に廃止される非推奨機能)として扱われ、Java11以降では完全に削除されます。したがって、OpenRTM-aist-Javaを利用するためには、Java8の開発環境パッケージJDK8を利用する必要があります。
JDK8は、配布元のOracleが配布やサポートを停止しつつありますが、まだJava8を必要としている人が多くいるため、JDK8自体はしばらくはいくつかのベンダーから入手可能です。ここでは、JDK8の入手方法、インストール方法を紹介します。

## JDK8配布元
JDK8の配布元として、こちらが見つけたもののいくつかを下記に示します。あくまでも、こちらが見つけたいくつかをリストしているだけで、ここにリストされないものがあったとしても、特に意図はないことを理解ください。また、それぞれのサイトにおける配布に関しては使用が有償のもの、サポートが有償のものとかいろいろ条件があったりしますので、それぞれのサイトで、各自確認の上使用してください。

### Oracle
Javaの開発・配布元のOracleにおいても、2019年11月現在、JDK8はダウンロード可能です。個人ユースや開発ユースは無償ライセンスがあるようですが、商用ユースでは有償ライセンスが必要なようです。正確なライセンス条件などついては下記リンクやオラクルからのメッセージを参照ください。

- [Oracle Java SE Subscription](https://www.oracle.com/technetwork/java/javaseproducts/overview/index.html)
  - [JDK8 Download](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) 
  - このページはOracleがJava8の配布をやめた場合削除される可能性があります。

### OpenJDK
OpenJDKは、Oracleによるオープンソース実装のJavaで、例外条項付きGPLv2(GPL v2 with Classpath Exception)で配布されています。ほとんどのJDKの実装はこのOpenJDKをベースにしたものになっています。
- [OpenJDK](http://openjdk.java.net/)

下記リンクよりJava SE 8xxxx (xxxxは2019年11月現在u231です)のところからJDKのDOWNLOADのボタンがありますので、それをクリックして、プラットフォームにあったものを入手してください。
  - [OpenJDK8 download](https://www.oracle.com/technetwork/java/javase/downloads/index.html) 

### Adopt Open JDK
AdoptOpenJDKは、IBMがスポンサーしコミュニティによりメンテナンスされているOpenJDKビルドを提供するプロジェクトです。JVMとしてHotSpotと呼ばれるOpenJDKコミュニティで開発されたものと、OpenJ9と呼ばれるEclipseコミュニティで開発されたものの2種類が提供されています。

下記リンクより[OpenJDK8(LTS)]と、JVM([HotSpot]か[OpenJ9])を選択し[Latest release]のボタンをクリックしてください。プラットフォームに合わせたものダウンロードが始まるはずです。違うプラットフォーム用のものが欲しい場合は、[Other platforms]のボタンをクリックして必要なJDKを入手してください。 またインストール方法については[Installation]と書かれたリンクより情報を得てください。
- [AdoptOpenJDK](https://adoptopenjdk.net/)
  - [Adopt Open JDK 8 サポート](https://adoptopenjdk.net/support.html)(2026年5月まで)

### Amazon Open JDK
Amazon CorrettoはAmazonの長期サポートを含むOpenJDKのビルドです。入手は下記リンクからWebサイトに行き、[Amazon Corretto8ダウンロードする]ボタンをクリックしてください。プラットウォームごとのビルドのリストが表示されますので、プラットフォームに合わせて必要なインストレーション用ファイルを入手してください。

- [Amazon Corretto](https://aws.amazon.com/jp/corretto/)
  - [Amazon Open JDK 8 サポート](https://aws.amazon.com/jp/corretto/faqs/#support) (2026年6月まで)

## Linux環境でのインストール
### リポジトリからのパッケージ入手
主なLinuxディストリビューションでは、標準パッケージとして、JDK8に相当するOpenJDKパッケージが配布されています。

#### Ubuntu/Debian/Raspbian
Ubuntu Linux, Debian Linuxなどでは apt コマンドで以下のようにインストールすることができます。

```
 $ sudo apt install openjdk-8-jdk
```

#### Fedora
Fedora Linuxではyumコマンドで以下のようにインストールすることができます。

```
 $ sudo yum -y install java-1.8.0-openjdk
```

### リポジトリからのパッケージ入手以外の方法
上記のサードパーティベンダのWebサイトから入手することもできます。インストール方法についてはそのサイトの情報に従うか、Javaの標準的方法でインストールしてください。

参考として、Raspberry Pi OS bookworm環境へAdoptium（名称Temurin）のパッケージをインストールする手順を示します。

```
 $ sudo apt install apt-transport-https
 $ wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null
 $ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/trusted.gpg.d/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
 $ sudo apt update
 $ sudo apt install temurin-8-jdk
```

バージョンを確認しておきます。

```
 $ java -version
 openjdk version "1.8.0_402" 
 OpenJDK Runtime Environment (Temurin)(build 1.8.0_402-b06)
 OpenJDK Client VM (Temurin)(build 25.402-b06, mixed mode)
```


### 既にJDK8以外がインストールされている場合
なお、JDK8以外のJDKがデフォルト状態でインストールされている可能性がありますので、

```
 $ java -version
```

コマンドでバージョンが1.8で始まるバージョンなどJDK8を意味するバージョンになっていることを確認してください。
もし、そうでなかったら

```
 $ sudo update-alternatives --config java
```

コマンドを用いてJDK8ベースのJava環境を選択してください。
ubuntu18.04の環境でopenjdk-8-jdkをインストールした後での実行例は以下のようになります。

```
 $ sudo update-alternatives --config java
 
   選択肢    パス                                          優先度  状態
 ------------------------------------------------------------
 * 0            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      自動モード
   1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      手動モード
   2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      手動モード
 
 現在の選択 [*] を保持するには <Enter>、さもなければ選択肢の番号のキーを押してください: 2
 update-alternatives: /usr/bin/java (java) を提供するためにマニュアルモードで /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java を使います
```

## Windows環境へのインストール

WindowsでのJDK８のインストールは上記のサイトなどからMSIファイルを入手し、それを実行することでインストールを行うか、MSI以外の形態のファイルにおいては入手元の指示に従いインストールを行ってください。インストール後は上記Linuxのケースと同様にコマンドプロンプトを開いて

```
 java -version
```

と入力し、インストールの確認を行ってください。


