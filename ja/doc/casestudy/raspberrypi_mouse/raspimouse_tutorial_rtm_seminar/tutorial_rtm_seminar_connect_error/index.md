---
layout: page
title: ポートの接続に失敗した場合の対処方法
---

<!-- ポートの接続に失敗した場合の対処方法 -->
#contents


## はじめに

このページでは別々のマシンで起動したRTCのデータポート、サービスポートを接続した場合に発生する問題の解決方法について解説する。

<div align="center"><a href="iorkakunin6.png"><img src="iorkakunin6.png" width="60%;"></a></div>


## RTSystemEditorで「接続に失敗しました」と表示される場合

以下のようにRTSystemEditorで「接続に失敗しました」と表示される場合、エンドポイントの設定が適切ではないか、あるいはファイアーウォールなどで通信が遮断されているケースが考えられます。

<div align="center"><a href="iorkakunin3.png"><img src="iorkakunin3.png" width="60%;"></a></div>

### ファイアーウォールで通信が遮断されることが原因の場合
&aname(firewall);

Windowsファイアウォールの場合はファイアウォールの場合はファイアウォールを無効にするか、RobotController.exeの通信を許可するように設定する必要があります。

- [Windows10 – アプリにファイアウォール経由の通信を許可/不許可](https://pc-karuma.net/windows-10-firewall-app-allow-communicate/)

ウィルス対策ソフトのファイアウォールで遮断されている場合は、使用しているウィルス対策ソフトのマニュアルなどを読んで対応してください。


### エンドポイントの設定が不適切のため到達できないアドレスに設定されていることが原因の場合

コマンドプロンプトを起動して、ipconfigコマンドでIPアドレスを確認してください。

- [ipconfig コマンド](https://www.pc-master.jp/trouble/ipconfig.html)

講習会で使用するRaspberry Piマウスのアクセスポイントに接続した場合は192.168.11.**のIPアドレスが設定されているはずです。
EV3のアクセスポイントの場合は192.168.0.**です。

次にPCで起動したRTCのエンドポイントの設定を確認します。

RTSystemEditorのネームサービスビューでRTCを右クリックしてIORを表示してください。

<div align="center"><a href="iorkakunin1.png"><img src="iorkakunin1.png" width="60%;"></a></div>

IOR表示の画面でProfileからIPアドレスを確認できます。

<div align="center"><a href="iorkakunin2.png"><img src="iorkakunin2.png" width="60%;"></a></div>

ここで確認したIPアドレスが192.168.11.**(もしくは192.168.0.**)でない場合はRTC起動時にエンドポイントの設定を行う必要があります。
rtc.confの**corba.endpoints**オプションで設定します。

```
 corba.endpoints: 192.168.11.**
```

rtc.confをテキストエディタで開いて編集して、RTCの実行ファイルと同じフォルダに配置して起動するか、コマンドラインオプションでrtc.confを指定して起動します。

```
 RobotControllerComp.exe -f rtc.conf
```

もしくは、コマンドラインオプションで直接**corba.endpoints**を設定することもできます。

```
  RobotControllerComp.exe -o corba.endpoints:192.168.11.**
```

## データポートの片方で色が変化しない、もしくはコネクタが表示されない場合
RTSystemEditorでデータポートの接続を行った場合に、以下のようにデータポートの片方の色が変化しない事があります。

<div align="center"><a href="iorkakunin4.png"><img src="iorkakunin4.png" width="60%;"></a></div>

もしくはコネクタが表示されない場合もあります。

この場合は、一旦System DiagramからRTCを削除してください。※終了(exit)ではありません。
<br>
RTCを選択してDeleteキーを押すか、右クリックしてDeleteを選択してください。

<div align="center"><a href="iorkakunin7.png"><img src="iorkakunin7.png" width="60%;"></a></div>

削除したら、もう一度ネームサービスビューからSystem Diagramにドラッグアンドドロップしてください。
これで問題が解決していれば、RTSystemEditorのコンポーネントオブザーバー機能が原因のため、大抵の場合はOpenRTPの再起動で解決します。


## RTSystemEditorが応答なしになる場合
RTSystemEditorが応答なしになる場合、もしくはしばらく待てば動くが片方のポートの色が変化しない場合等があります。
この場合は、[ファイアウォールなどで通信が遮断されていることが原因]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_connect_error#firewall)であることがほとんどです。

それで解決しない場合はRaspberry Pi、EV3側のRTCを再起動してください。RTCの実行中の問題で応答なしになっている可能性があります。

またSystem Diagramを長時間使用していると不具合が発生することがあります。
System Diagramを×を押して削除後、もう一度System Diagramを表示して下さい。
