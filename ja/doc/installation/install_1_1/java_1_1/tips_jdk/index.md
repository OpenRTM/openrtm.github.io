---
layout: page
title: tips
---

<!-- Title: Tips -->
## JDKインストールのためのヒント

JDKは、OpenJDK と OracleJDK のいずれかをインストールします。ここでは下記環境へのインストール方法を紹介します。
<!-- - [[Vine3.2 >#vine]]  -->
- [Ubuntu 14.04](#ubuntu)
- [Debian 7.0 Wheezy ](#debian7) 
- [Debian 6.0 Squeeze](#debian6) 
- [Fedora 20](#fedora)
<!-- - [[FreeBSD 7.0 >#nd416b5f]] -->

<br>
<!-- *** Vine3.2&aname(vine); -->
<!-- 一例として、Vine3.2へのインストール方法を述べます。以下の作業はスーパーユーザとして行ってください。 -->
<!-- #br -->
<!--  -->
<!-- - JDK 5インストール方法 -->
<!-- -- Linux RPM in self-extracting fileを入手した場合 -->
<!-- ターミナルを起動し、Linux RPM in self-extracting fileをダウンロードしたディレクトリにカレントを移動させて、次のようにコマンドを入力する。 -->
<!-- # ls -->
<!-- jdk-1_5_0_15-linux-i586-rpm.bin -->
<!-- # sh jdk-1_5_0_15-linux-i586-rpm.bin -->
<!-- ライセンス許諾条項が表示されるの適宜スペースを押して進んでいく。ライセンスを承諾するかどうか質問されるので、問題なければ「yes」と答える。 -->
<!--  -->
<!-- #br -->
<!--  -->
<!-- -- Linux self-extracting fileを入手した場合 -->
<!-- ターミナルを起動し、Linux self-extracting fileをダウンロードしたディレクトリにカレントを移動させて、次のようにコマンドを入力する。 -->
<!-- # ls -->
<!-- jdk-1_5_0_15-linux-i586.bin -->
<!-- # sh jdk-1_5_0_15-linux-i586.bin -->
<!-- ライセンス許諾条項が表示されるの適宜スペースを押して進んでいく。ライセンスを承諾するかどうか質問されるので、問題なければ「yes」と答える。 -->
<!-- # mkdir /usr/java -->
<!-- # mv jdk1.5.0_15/ /usr/java/ -->
<!-- などとして、/usr/java以下に解凍されたJDKを配置する。 -->
<!--  -->
<!-- #br -->
<!--  -->
<!-- - 環境変数の設定 -->
<!--  -->
<!-- /etc/profileの末尾に次の3行を追加する。 -->
<!--  -->
<!-- export JAVA_HOME=/usr/java/jdk1.5.0_15 -->
<!-- export PATH=$PATH:$JAVA_HOME/bin -->
<!-- export CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar -->
<!-- #br -->
<!--  -->
<!-- ''参考サイト（外部サイト）:'' -->
<!-- - [[Javaのインストール(Linux) >http://rat.cis.k.hosei.ac.jp/article/java/javalinux.html]] -->
<!-- - [[Linux環境におけるJavaインストール手順 >http://codezine.jp/a/article/aid/1744.aspx]] -->


<br>

### Ubuntu 14.04
&aname(ubuntu);
#### OpenJDK7

apt-getでインストールできます。
```
 $ sudo apt-get install openjdk-7-jdk
```

JDKの確認
```
 $ java -version
 java version "1.7.0_75"
 OpenJDK Runtime Environment (IcedTea 2.5.4) (7u75-2.5.4-1~trusty1)
 OpenJDK 64-Bit Server VM (build 24.75-b04, mixed mode)
```

ここでバージョンが、「1.6.0_xx」という用に表示されたら、JDK7 を使用するように変更します。この切替えは、update-alternatives コマンドで行います。
```
 $ sudo update-alternatives --config java
 alternative java (/usr/bin/java を提供) には 2 個の選択肢があります。
   選択肢    　　パス                                          優先度  　　状態
 -------------------------------------------------------------------------------------
 * 0            /usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java   1061      自動モード
   1            /usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java   1061      手動モード
   2            /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java   1051      手動モード
 現在の選択 [*] を保持するには Enter、さもなければ選択肢の番号のキーを押してください: 2
```
JDK7 を使用するので、番号の「2」を指定します。この操作後、java -version でJDKを確認します。

#### oracleJDK7

リポジトリを追加して、oracleJDK7をインストールします。
```
 $ sudo add-apt-repository ppa:webupd8team/java
 $ sudo apt-get update
 $ sudo apt-get install oracle-jdk7-installer
```

JDKの確認
```
 $ java -version
 java version "1.7.0_76"
 Java(TM) SE Runtime Environment (build 1.7.0_76-b13)
 Java HotSpot(TM) 64-Bit Server VM (build 24.76-b04, mixed mode)
```

OpenJDKもインストールしている場合は、選択状況を下記で確認できます。
```
 $ update-alternatives --config java
 alternative java (/usr/bin/java を提供) には 2 個の選択肢があります。
   選択肢   　　 パス                                          優先度  　　状態
 -------------------------------------------------------------------------------------
 * 0            /usr/lib/jvm/java-7-oracle/jre/bin/java          1072      自動モード
   1            /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java   1071      手動モード
   2            /usr/lib/jvm/java-7-oracle/jre/bin/java          1072      手動モード
 現在の選択 [*] を保持するには Enter、さもなければ選択肢の番号のキーを押してください: 
```

<br>

### Debian 7.0 Wheezy
&aname(debian7);
#### OpenJDK7

手順は上記の Ubuntu14.04 を参照して下さい。同じ手順で設定できます。

#### oracleJDK7（java-packageを使った方法：Debian7.0から対応）

右記の手順に従ってインストールします。
[https://wiki.debian.org/JavaPackage](https://wiki.debian.org/JavaPackage)

/etc/apt/sources.listの末尾に次の一文を追加します。
```
 deb http://http.debian.net/debian/ wheezy main contrib
```

JDKをインストールするために必要な java-package をインストールします。
```
 # apt-get update
 # apt-get install java-package
```

oracleのサイトからJDK （ここではjdk-7u75-linux-x64.tar.gz） をダウンロードします。
<br>
[http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)


debパッケージを生成してインストールします。
```
 $ make-jpkg jdk-7u75-linux-x64.tar.gz
 $ ls
 oracle-j2sdk1.7_1.7.0+update75_amd64.deb
 # dpkg -i oracle-j2sdk1.7_1.7.0+update75_amd64.deb
```

oracleJDKを選択します。
```
 # update-alternatives --config java
 alternative java (/usr/bin/java を提供) には 3 個の選択肢があります。
   選択肢    　　パス                                          優先度  　　状態
 -------------------------------------------------------------------------------------
   0            /usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java   1061      自動モード
   1            /usr/lib/jvm/j2sdk1.7-oracle/jre/bin/java        317       手動モード
   2            /usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java   1061      手動モード
 * 3            /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java   1051      手動モード
```
 現在の選択 [*] を保持するには Enter、さもなければ選択肢の番号のキーを押してください: 1

JDKの確認
```
 $ java -version
 java version "1.7.0_75"
 Java(TM) SE Runtime Environment (build 1.7.0_75-b13)
 Java HotSpot(TM) 64-Bit Server VM (build 24.75-b04, mixed mode)
```

### Debian 6.0 Squeeze
&aname(debian6);
#### OpenJDK7

/etc/apt/sources.list の最後にwheezyリポジトリを追加します。
```
 # vi /etc/apt/sources.list
 deb http://ftp.jp.debian.org/debian/ wheezy main
```

openjdk7 のインストールのためだけに追加したので、優先されるのはsqeezeバージョンということで、/etc/apt/apt.conf.d にlocalファイルを新設して以下を記述します。
```
 # vi /etc/apt/apt.conf.d/local
 APT::Default-Release "squeeze";
```

一方、wheezyに含まれるパッケージのプライオリティは最小にしておきます。squeeze環境で、主要なライブラリが不要にもアップグレードされてしまうことは避けたいためです。<br>
/etc/apt/preferences.d にwheezyファイルを新設し、以下を記述します。
```
 # vi /etc/apt/preferences.d/wheezy
 Package: *
 Pin: release n=wheezy
 Pin-Priority: 10
```

priorityは、インストールしているパッケージには100、インストールしていないパッケージには500が割り当てられるので、100より小さい値を指定しておきます。

```
 # apt-get update
 # apt-get install -t wheezy openjdk-7-jdk
```

OpenJDK7を選択します。
```
 # update-alternatives --config java
 alternative java (/usr/bin/java を提供) には 3 個の選択肢があります。
   選択肢    　　パス                                          優先度  　　状態
 -------------------------------------------------------------------------------------
 * 0            /usr/lib/jvm/java-6-openjdk/jre/bin/java         1061      自動モード
   1            /usr/bin/gij-4.7                                 1047      手動モード
   2            /usr/lib/jvm/java-6-openjdk/jre/bin/java         1061      手動モード
   3            /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java   1051      手動モード
 現在の選択 [*] を保持するには Enter、さもなければ選択肢の番号のキーを押してください: 3
```

JDKの確認
```
 # java -version
 java version "1.7.0_03"
 OpenJDK Runtime Environment (IcedTea7 2.1.7) (7u3-2.1.7-1)
 OpenJDK 64-Bit Server VM (build 22.0-b10, mixed mode)
```

**参考サイト（外部サイト）:**
- [Install Openjdk7 on Debian Squeeze ](http://serverfault.com/questions/465741/install-openjdk7-on-debian-squeeze)
- [Debian 管理者ハンドブック ](http://debian-handbook.info/browse/ja-JP/stable/sect.apt-get.html)

<br>

#### oracleJDK7（update-alternatives でインストールする方法）

Debian6.0 では java-package がサポートされていないので、update-alternatives でインストールします。
<br><br>

oracleのサイトからJDK （ここではjdk-7u75-linux-x64.tar.gz） をダウンロードします。<br>
[http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)
<br>

解凍し、生成されたディレクトリjdk1.7.0_75を /usr/lib に移動させます。
```
 # tar xvzf jdk-7u75-linux-x64.tar.gz
 # mv jdk1.7.0_75 /usr/lib/jvm/jdk1.7.0-oracle
```

update-alternatives コマンドでインストールします。この時、優先度を指定しますが、ここでは１としています。
```
 # update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.7.0-oracle/bin/java" 1
 # update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.7.0-oracle/bin/javac" 1
```

oracleJDKを選択します。
```
 # update-alternatives --config java
 alternative java (/usr/bin/java を提供) には 4 個の選択肢があります。
   選択肢    　　パス                                          優先度  　　状態
 -------------------------------------------------------------------------------------
   0            /usr/lib/jvm/java-6-openjdk/jre/bin/java         1061      自動モード
   1            /usr/bin/gij-4.7                                 1047      手動モード
   2            /usr/lib/jvm/java-6-openjdk/jre/bin/java         1061      手動モード
 * 3            /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java   1051      手動モード
   4            /usr/lib/jvm/jdk1.7.0-oracle/bin/java            1         手動モード
 現在の選択 [*] を保持するには Enter、さもなければ選択肢の番号のキーを押してください: 4
```

JDKの確認
```
 $ java -version
 java version "1.7.0_75"
 Java(TM) SE Runtime Environment (build 1.7.0_75-b13)
 Java HotSpot(TM) 64-Bit Server VM (build 24.75-b04, mixed mode)
```

<br>

**参考サイト（外部サイト）:**
- [Debian系LinuxへOracle JDKをインストールする ](http://astah.change-vision.com/ja/feature/install-linux-debian.html)

<br>

### Fedora 20 &aname(fedora);
#### OpenJDK7

既にインストールされています。
```
 $ java -version
 java version "1.7.0_75"
 OpenJDK Runtime Environment (fedora-2.5.4.2.fc20-x86_64 u75-b13)
 OpenJDK 64-Bit Server VM (build 24.75-b04, mixed mode)
```

#### oracleJDK7

oracleのサイトからJDK（ここではjdk-7u75-linux-x64.rpm）をダウンロードします。<br>
[http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)
<br>

インストール
```
 # rpm -ivh jdk-7u75-linux-x64.rpm
```

インストール先の確認
```
 # ls -l /usr/java/
 lrwxrwxrwx. 1 root root   16  3月 17 10:47 default -> /usr/java/latest
 drwxr-xr-x. 8 root root 4096  3月 17 10:46 jdk1.7.0_75
 lrwxrwxrwx. 1 root root   21  3月 17 10:47 latest -> /usr/java/jdk1.7.0_75
```

oracleJDKをalternativesへ登録します。この時、上のインストール先から /usr/java/latest のパスを使っていればJDKのバージョン番号に依存せずに済むことが分かります。<br>
登録前に、Javaの設定を確認しておきます。
```
 # update-alternatives --display java
 java - ステータスは手動です。
 リンクは現在 /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/java を指しています。
 /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/java - 優先項目 170075
  スレーブ keytool: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/keytool
  スレーブ orbd: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/orbd
  スレーブ pack200: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/pack200
  スレーブ rmid: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/rmid
  スレーブ rmiregistry: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/rmiregistry
  スレーブ servertool: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/servertool
  スレーブ tnameserv: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/tnameserv
  スレーブ unpack200: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/unpack200
  スレーブ jre_exports: /usr/lib/jvm-exports/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64
  スレーブ jre: /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre
  スレーブ java.1.gz: /usr/share/man/man1/java-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
  スレーブ keytool.1.gz: /usr/share/man/man1/keytool-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
  スレーブ orbd.1.gz: /usr/share/man/man1/orbd-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
  スレーブ pack200.1.gz: /usr/share/man/man1/pack200-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
  スレーブ rmid.1.gz: /usr/share/man/man1/rmid-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
  スレーブ rmiregistry.1.gz: /usr/share/man/man1/rmiregistry-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
  スレーブ servertool.1.gz: /usr/share/man/man1/servertool-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
  スレーブ tnameserv.1.gz: /usr/share/man/man1/tnameserv-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
  スレーブ unpack200.1.gz: /usr/share/man/man1/unpack200-java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64.1.gz
```

上記の結果で、orbd がスレーブとして登録されていることが分かります。ネームサーバを起動する際、orbd にパスが通っている必要があります。update-alternatives --install でインストールしたjavaと一緒に切り替えたいものをスレーブで指定しています。よって、oracleJDK を alternatives へ登録する際も --slave オプションで指定することにします。<br>
また、優先項目 170075 とは優先度のことです。update-alternatives --install 実行時に優先度を指定します。今回、OpenJDK7 と orcleJDK7 のバージョンが同じなので、oracleJDK7 を登録する際の優先度も 170075 を指定することにします。<br>

これらのことから、次の設定で登録します。
```
 # update-alternatives --install /usr/bin/java java /usr/java/latest/bin/java 170075 
   --slave /usr/bin/javac javac /usr/java/latest/bin/javac 
   --slave /usr/bin/javaws javaws /usr/java/latest/bin/javaws 
   --slave /usr/bin/keytool keytool /usr/java/latest/bin/keytool 
   --slave /usr/bin/orbd orbd /usr/java/latest/bin/orbd 
   --slave /usr/bin/pack200 pack200 /usr/java/latest/bin/pack200 
   --slave /usr/bin/rmid rmid /usr/java/latest/bin/rmid 
   --slave /usr/bin/rmiregistry rmiregistry /usr/java/latest/bin/rmiregistry 
   --slave /usr/bin/servertool servertool /usr/java/latest/bin/servertool 
   --slave /usr/bin/tnameserv tnameserv /usr/java/latest/bin/tnameserv 
   --slave /usr/bin/unpack200 unpack200 /usr/java/latest/bin/unpack200

```
oracleJDKを選択します。
```
 # update-alternatives --config java
 2 プログラムがあり 'java' を提供します。
   選択       コマンド
 -----------------------------------------------
 *+ 1           /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.fc20.x86_64/jre/bin/java
    2           /usr/java/latest/bin/java
 Enter を押して現在の選択 [+] を保持するか、選択番号を入力します:2
```

JDKの確認
```
 # java -version
 java version "1.7.0_75"
 Java(TM) SE Runtime Environment (build 1.7.0_75-b13)
 Java HotSpot(TM) 64-Bit Server VM (build 24.75-b04, mixed mode)
```

**参考サイト（外部サイト）:**
- [LinuxにOracleのJDKをインストールしたときのメモ ](http://d.hatena.ne.jp/lettas0726/20110614/1308032663)

<br>

<!-- *** FreeBSD 7.0 [#nd416b5f] -->
<!--  -->
<!--  -->
<!-- #br -->
<!--  -->
<!-- ''参考サイト（外部サイト）:'' -->
<!--  -->
<!-- → [[portsを最新にする >http://iris.homeunix.net/yayoi/freebsd/inst/cvsup.asp]] -->
<!--  -->
<!-- → [[FreeBSD-6.1にjdk-1.5をインストールする >http://d.hatena.ne.jp/i_youhei/20060923/1159008225]] -->
<!--  -->
<!-- → [[J2SDKのインストール(Linux,FreeBSD,Solaris) >http://park15.wakwak.com/~unixlife/java/j2sdk.html]] -->
<!--  -->
<!-- #br -->
<!--  -->


