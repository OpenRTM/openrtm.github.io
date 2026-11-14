---
layout: page
title: openrtm-aist (java版) に関する faq 
---

<!-- Title: OpenRTM-aist (Java版) に関する FAQ -->
#contents(3)

## OS 共通

### Java版コンポーネントでデータ転送に時間がかかる
Java版の RTコンポーネントと C++版など他の言語のコンポーネントとの間で、特に大きなデータ（100kB以上でみられることが多い。）を送受信する場合に、極端に速度が低下する場合があります。これは Java の CORBA 側の問題であることが知られており、タイムアウトを適切に設定することにより回避することができます。~
Java版の RTC が読み込む rtc.conf に以下のように記述することで、Java の CORBA のタイムアウトを設定します。~
```
 corba.args: -ORBTCPReadTimeouts 1:60000:300:1
```
Java (JDK1.5以降) ではデフォルトで、**100:3000:300:20** となっていますが、これを **1:60000:300:1** に変更するという意味です。各項目は左から、
- CORBA データを read するときに、0byte であったときに Read Thread が休止させられる時間(ms)
- CORBA データの read 時に Read Thread が待たされる累積最大時間 (ms)
- GIOP のヘッダーを read するときのタイムアウト(ms)
- CORBA データを read するときに、Read Thread が休止させられたときに、次回の休止の時間を増加する割合(%)

という意味になっています。したがって、**1:60000:300:1** は
- read して0byteのとき、Read Thread を 1ms休止する
- Read Thread が待つ最大累積時間は 6000ms
- GIOP のヘッダを read するときのタイムアウト時間は 300ms
- Read Thread の休止時間は1%づつ増加させる

という意味になります。~
大きなデータの場合、1回の read でデータが読み切れないので、通常何回か read を行います。~
次のデータはすぐには来ませんので、read は読み込みバイト数を 0byte として戻りますが、通常1ms以内には次のデータはやってきます。デフォルトの設定だと Read Thread が100ms待たされますが、そんなに長時間待つ必要はなく1ms程度待てば、すぐに次のデータを読み込むことができます。~
デフォルト設定の場合、100ms待って、さらにもう一度読み込み read が0を返すので、さらに100ms+20%の120ms待ちます。データが大きすぎれば、これを12回繰り返すと最大累積時間の3000msに達してしまうので、タイムアウトしてしまいますし、データが小さくても、データの分割数×100msの時間がかかってしまうので、非常に遅くなります。~
Java の CORBA ではデータを100kBで分割するので、これを超えるデータをやり取りする際には、上記の設定を rtc.conf にて行っておいたほうがよいでしょう。
<br>
<br>

## Windows

### ネームサーバーのコンソール画面が開かない
「Start Java Naming Service」は %RTM_ROOT%\bin\rtm-naming.bat にあるバッチファイルからネームサーバー (omniNames.exe) を起動します。
この際、omniNames.exe を参照するために環境変数 OMNI_NAMES を利用しています。
通常インストーラーで OpenRTM-aist をインストールした場合には、OMNI_ROOT 環境変数が自動で設定されます。しかし、何らかの理由で環境変数が無効になっていたり、手動でインストールした場合は、環境変数が設定されていないことがあります。
<br>
<br>

### サンプルコンポーネントが起動しない
rtc.conf の設定に問題があります。rtc.conf の設定を以下のように設定し直して確認してください。
```
 corba.nameservers: localhost
```
例えば、corba.endpoint/corba.endpoints などの設定が現在実行中の PC のホストアドレスとミスマッチを起こしている場合などは、CORBA が異常終了します。
<br>
<br>

### サンプルコンポーネントを起動させると、ランタイムエラーで終了する
ライブラリー等が適切にインストールされていない、設定されていない等の原因でラインタイムエラーが表示される場合があります。
PCを再起動する または OpenRTM-aist をすべてアンインストールし、再インストールすることで改善される場合があります。
<br>
<br>

## UNIX

&aname(fedoraNS);
### FedoraCore で RTSystemEditor の NameService View にエラーが表示される
OS が FedoraCore の場合、yum にて Java をインストールすると GCJ (The GNU Compiler for Java ) がインストールされてしまい、その GCJ を使用すると RTSystemEditorのNameService View にエラーが表示されることがあります。~
エラーが表示された場合は、まず、Oracle の Java が使用されているか確認してください。~
Eclipse だけで Oracle の Java を使用したい場合は、jdk-xxx-linux-i586.bin をダウンロード後、実行してできた jre ディレクトリーを Eclipse インストールディレクトリーへコピーしてご使用ください。~
```
 $ sh jdk-6u4-linux-i586.bin
 $ cp -r jdk1.6.0_04/jre eclipse/
```
- (JPackage,alternativesというのを使用する事で、使用する Java を選択する事も可能なようです。)
<br>
<br>

&aname(javafedora);
### FedoraCore で Java をインストールする際の対応 
OS が FedoraCore の場合、yum にて Java をインストールすると GCJ (The GNU Compiler for Java ) がインストールされてしまい、その GCJ を使用するといくつかの不具合が生じる事があります。~
不具合が発生した場合は、まず、Oracle の Java が使用されているかの確認をしてください。

- 参考 
  - [JDKインストールのためのヒント]({{ site.baseurl }}/ja/doc/installation/install_1_1/java_1_1/tips_jdk#fedora)
  - [UNIX系環境で簡易に Oracle の Java を Eclipse に適用する方法]({{ site.baseurl }}/ja/doc/faq/faq_rtp_tools#rtclinksunjava)


