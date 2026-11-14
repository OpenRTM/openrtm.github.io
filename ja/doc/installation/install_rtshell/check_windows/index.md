---
layout: page
title: 動作確認(windows編)
---

<!-- Title: 動作確認(Windows編) -->

#contents(3)

## 動作確認環境
以下では、Windows 10にmsiインストーラーでOpenRTM-aistをデフォルトでインストールした環境をもとに説明します。

サンプルコンポーネントセットSimpleIOを使って、rtshellが正しくインストールされているかを確認します。

## サンプル(SimpleIO)を使用した動作確認

RTコンポーネントConsoleIn、ConsoleOutからなるサンプルセットを用います。ConsoleInはコンソールから入力された数値をOutPortから出力するコンポーネント、ConsoleOutはInPortに入力された数値をコンソールに表示するコンポーネントです。これらは簡単なI/O(入出力)を例示するためのサンプルです。ConsoleInのOutPortからConsoleOutのInPortへの接続をし、これらの2つのコンポーネントをアクティブ化(Activate)することで動作します。

## Name Serverの起動
まずは以下の手順でName Serverを起動します。
- 画面の左下の[ここに入力して検索]に"start naming service"と入力します。
- [Start Naming Service]をクリックします。
<div align="center"><a href="rtshell6.png"><img src="rtshell6.png" width="50%;"></a></div>
- 以下のような画面が表示されます。
<div align="center"><a href="rtshell5.png"><img src="rtshell5.png" width="50%;"></a></div>

## サンプルコンポーネントの起動
サンプルコンポーネントを起動します。

Windows 10の場合は右下の「ここに入力して検索」に**Python_Examples**と入力してサンプルコンポーネントの起動ファイルのディレクトリでエクスプローラを開きます。

<div align="center"><a href="rtm8-2.png"><img src="rtm8-2.png" width="50%;"></a></div>
<div align="center"><strong>サンプルコンポーネント起動ファイル</strong></div>

「ConsoleIn.bat」「ConsoleOut.bat」をそれぞれダブルクリックして2つのコンポーネントを起動します。起動すると、下図のような2つのコンソール画面が開きます。
また、サンプルコンポーネントは通常下記のディレクトリ下にインストールされますので、そこからエクスプローラで直接起動しても構いません。
- C:\Program Files\OpenRTM-aist\1.2.<span style="color:blue;">x</span>;\Components\Python

<div align="center"><a href="rtm9-2.png"><img src="rtm9-2.png" width="80%;"></a></div>
<div align="center"><strong>ConsoleInコンポーネントとConsoleOutコンポーネント</strong></div>


### コンポーネントが起動しない場合

コンポーネントが起動しない場合、いくつかの原因が考えられます。

#### コンソール画面が開いてすぐに消える

rtc.confの設定に問題があり、起動できないケースがあります。上記のサンプル起動ファイルがあるディレクトリ下Examples\SimpleIO￥rtc.confファイルを開いて設定を確認してください。例えば、corba.endpoint/corba.endpointsなどの設定が現在実行中のPCのホストアドレスとミスマッチを起こしている場合などは、CORBAが異常終了します。

以下のような最低限のrtc.confに設定しなおして試してみてください。

```
 corba.nameservers: localhost
```


#### omniORBpyがインストールされていない。

openrtm.orgが提供するmsiインストーラーにはomniORBpyが含まれていますが、カスタムインストールを選択すると、omniORBpyをインストールせずにOpenRTM-aist-Pythonをインストールできます。また、手動でインストールした場合には、omniORBpyが入っていない場合も考えられますので、omniORBpyがインストールされているか確認してください。

#### pyファイルの関連付けが違っている

ConsoleIn、ConsoleOutを起動するファイルは、

C:\Program Files\OpenRTM-aist\1.2.<span style="color:blue;">x</span>;\Components\Python\Examples\SimpleIO\ConsoleIn.py<br>
C:\Program Files\OpenRTM-aist\1.2.<span style="color:blue;">x</span>;\Components\Python\Examples\SimpleIO\ConsoleOut.py

ですので、これらのファイルをダブルクリックしてみてください。うまく起動しないようでしたらファイルの関連付けが間違っています。

#### その他

ホスト名やアドレスの設定の問題で、起動がうまくいかないケースがあります。その場合、利用しているPCのIPアドレスをomniNames.exeに教えてあげるとうまくいくケースがあります。
環境変数OMNIORB_USEHOSTNAMEを以下のように設定します(以下は自ホストのIPアドレスが192.168.0.11の場合の例)。

```
 変数名(N): OMNIORB_USEHOSTNAME
 変数値(V): 192.168.0.11
```

## rtshell操作

- コマンドラインコンソールを開きます。

- コマンドラインから以下のようにコマンドrtlsを実行し、以下のように表示されることを確認します。
```
 C:\Users\openrtm>rtls -R 127.0.0.1
 .:
 ConsoleIn0.rtc  ConsoleOut0.rtc
```

- ConsoleInコンポーネントとConsoleOutコンポーネントを接続します。
```
 rtcon /localhost/ConsoleIn0.rtc:out /localhost/ConsoleOut0.rtc:in
```

- ConsoleInコンポーネントとConsoleOutコンポーネントをActivateします。
```
 rtact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc
```

- するとConsoleInとConsoleOutのコンソールが以下のように変わり、ConsoleIn側コンソールに"Please Input number:"と表示されます。

<div align="center"><a href="rtm9-3.png"><img src="rtm9-3.png" width="80%;"></a></div>

- ConsoleInのコンソールから数値を(16bit整数の範囲で)入力しEnterキーを押します。

- ConsoleOutのコンソールにConsoleInのコンソールで入力した数値が表示されるのを確認します。
同じ数値が表示されていれば動作は確認できました。
- 以下のように入力しDeactivateします。
```
 rtdeact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc
```
この時ConsoleIn.py側のコンソールに数値を入力しEnterキーを押すことにより、入力待ち状態を解消してください。 その後
```
 rtexit /localhost/ConsoleIn0.rtc
 rtexit /localhost/ConsoleOut0.rtc
```
と入力し、コンソールが閉じることを確認してください。


