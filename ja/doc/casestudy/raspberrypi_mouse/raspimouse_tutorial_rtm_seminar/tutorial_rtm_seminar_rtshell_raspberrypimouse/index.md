---
layout: page
title: チュートリアル(rtshell入門、raspberry pi mouse)
---
<!--  チュートリアル(rtshell入門、Raspberry Pi Mouse) -->

#contents

## はじめに
ここではシミュレータ上のRaspberry Piマウスを操作するRTシステムの起動、終了を自動化するバッチファイル、シェルスクリプトの作成方法について説明します。
今まで実行ファイルをダブルクリックして起動したり、RTSystemEditorから操作してポートを接続したりしていたのが、スクリプトを実行するだけでシステムの起動に必要な処理を全て実行してくれます。

この実習では[RTコンポーネントの作成入門]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_win_part2)で作成したRobotControllerコンポーネントを使用します。

RTCの起動とRTSystemEditor上での操作を自動化するバッチファイル、シェルスクリプトを作成する実習を行います。

<div align="center"><a href="rtshell1_tutorial.png"><img src="rtshell1_tutorial.png" width="50%;"></a></div>

### rtshell

rtshellはコマンドラインからRTCを操作するためのツールで、RTSystemEditorと同等の機能を持ちます。

- [rtshell によるRTシステムの管理]({{ site.baseurl }}/ja/content/rtshell_managing_rt_systems)
- [rtshell入門]({{ site.baseurl }}/ja/./rtshell.pdf)

## RTシステム起動の自動化

シミュレータ上のRaspberryPiマウスをRobotControllerコンポーネントで制御するシステムの起動、終了手順は以下の通りです。

1. RaspberryPiMouseSimulatorコンポーネント、RobotControllerコンポーネントを起動する。
1. ポートをコネクタで接続する
1. RTCをアクティブ化する
1. RTCを終了する

### 事前準備
この実習ではコマンドラインによる操作を行うため、コマンドプロンプト(Windows)、ターミナル(Ubuntu)を起動してください。

- [Windows10 – コマンドプロンプトを起動する方法](https://pc-karuma.net/windows10-open-command-prompt-window/)
- [【Linux FAQ】Ubuntuで「端末」を開いて「コマンド」を実行するには？](https://linuxfan.info/ubuntu-open-terminal-emulator)

コマンドプロンプト、ターミナルを起動したら「**rtls**」と入力してください。
**‘rtls’ は、内部コマンドまたは外部コマンド、操作可能なプログラムまたはバッチ ファイルとして認識されていません。**と表示された場合、PythonのScriptsフォルダ(例えば「C:\Python38\Scripts」)が環境変数Pathに設定されていません。
Pythonをインストール場所を確認して環境変数を設定してください。

- [Pythonのインストール場所について（Windows）](https://gammasoft.jp/blog/python-install-location/)
- [Windows 10でPath環境変数を設定／編集する](https://www.atmarkit.co.jp/ait/articles/1805/11/news035.html)

### ポートの接続自動化
データポートの接続を自動化する手順は以下の通りです。

- RTSystemEditor(もしくはrtshellのrtconコマンド)でポートを接続する。
- rtshellの**rtcryo**コマンドで接続情報をファイルに保存する。
- 再起動時にrtshellの**rtresurrect**コマンドで接続を復元する。

前準備として接続情報を保存したXMLファイルを保存し、自動起動時にはrtresurrectコマンドで状態を復元します。

**RobotControllerComp**、**RaspberryPiMouseSimulatorComp**を起動後、RTSystemEditor上でポートを接続してください。

現在の状態は以下のようになっています。

<div align="center"><a href="rtshell3_tutorial.png"><img src="rtshell3_tutorial.png" width="70%;"></a></div>

接続後、以下のコマンドでXMLファイルを保存します。
XMLファイルの保存場所は自分で分かる場所に変更してください。

```
 rtcryo -o C:\work\robotcontroller.xml localhost
```

次にrtresurrectコマンドを試してみます。
まずは全てのコネクタを削除してください。
RTSystemEditorでコネクタをクリックしてDeleteキーを押すか、右クリックしてDeleteを選択してください。

<div align="center"><a href="rtshell2_tutorial.png"><img src="rtshell2_tutorial.png" width="70%;"></a></div>

現在は以下の状態になっています。

<div align="center"><a href="rtshell4_tutorial.png"><img src="rtshell4_tutorial.png" width="70%;"></a></div>

以下のコマンドを入力してください。
XMLファイルの場所は保存した場所に変更してください。

```
 rtresurrect C:\work\robotcontroller.xml
```

ポートが接続された状態に戻ったかを確認してください。
現在は以下の状態になっているはずです。

<div align="center"><a href="rtshell3_tutorial.png"><img src="rtshell3_tutorial.png" width="70%;"></a></div>

### RTCのアクティブ化の自動処理

rtshellの**rtstart**でRTCをアクティブ化します。
以下のコマンドを入力してください。

```
 rtstart C:\work\robotcontroller.xml
```

現在は以下の状態になっており、シミュレータ上のRaspberryPiマウスが操作可能になっているはずです。

<div align="center"><a href="rtshell5_tutorial.png"><img src="rtshell5_tutorial.png" width="70%;"></a></div>

次にRTCの非アクティブ化を試してみます。
以下の**rtstop**コマンドを入力してください。

```
 rtstop C:\work\robotcontroller.xml
```

これでRTCが非アクティブ化されて以下の状態になっているはずです。

<div align="center"><a href="rtshell3_tutorial.png"><img src="rtshell3_tutorial.png" width="70%;"></a></div>

### RTCの終了の自動化

rtshellの**rtexit**でRTCを終了します。

以下のコマンドを試してみてください。

```
 rtexit localhost/RaspberryPiMouseSimulator0.rtc
 rtexit localhost/%COMPUTERNAME%.host_cxt/RobotController0.rtc
```

RTCはデフォルトの設定でホスト名.host_cxtのコンテキストの下にコンポーネントを登録します。

<div align="center"><a href="rtshell6_tutorial.png"><img src="rtshell6_tutorial.png" width="50%;"></a></div>

※Ubuntuの場合は**HOSTNAME=`hostname`**を追加して、**%COMPUTERNAME%**を**${HOSTNAME}**に変更してください。

これでRTCが終了したはずです。

### バッチファイル、シェルスクリプトの作成

RTシステムを起動、終了するバッチファイル、シェルスクリプトを作成します。

Windowsの場合は以下のバッチファイルを作成してください。

- robotcontroller_start.bat
- robotcontroller_exit.bat

バッチファイルの作成手順は以下の通りです。

- [バッチファイルの作成方法：Windowsバッチファイルに初めて触れる方へ](https://jj-blues.com/cms/wantto-howtomakebatforbeginer/)

名前変更時に、エクスプローラーで拡張子を非表示にしている場合は注意してください。

バッチファイルはメモ帳などで開いてください。

Ubuntuの場合は以下のシェルスクリプトを作成してください。

- robotcontroller_start.sh
- robotcontroller_exit.sh


#### 起動スクリプトの作成

まずは**robotcontroller_start.bat**、**robotcontroller_start.sh**を編集します。

robotcontroller_start.batをメモ帳などで開いて、RobotControllerComp、RaspberryPiMouseSimulatorCompを起動する手順をバッチファイル、シェルスクリプトに記述します。

Windowsの場合は以下のコマンドを記述してください。

```
 start "" /d C:\workspace\RobotController\build\src\Release RobotControllerComp.exe
 start "" /d C:\work\RTM_Tutorial\EXE RaspberryPiMouseSimulatorComp.exe
 timeout 2
```

Ubuntuの場合は以下のコマンドを記述してください。

```
 cd ~/workspace/RobotController/build/src/
 ./RobotControllerComp&
 cd ~/RasPiMouseSimulatorRTC/build
 src/RaspberryPiMouseSimulatorComp&
 sleep 2
```

RobotControllerComp、RaspberryPiMouseSimulatorCompのパスは環境に合わせて変更してください。
RTCが起動しないと後のコマンドが実行できないためtimeout、sleepコマンドで待機するようにしてあります。


次にポートの接続、RTCのアクティブ化を実行するコマンドを記述してください。

```
 rtresurrect C:\work\robotcontroller.xml
 rtstart C:\work\robotcontroller.xml
```


編集が終わったら、robotcontroller_start.bat、robotcontroller_start.shを実行してみてください。
問題がなければRTCが自動起動してシミュレータが実行されているはずです。
RTCが起動しない、ポートが接続されないなどの場合は、実行ファイルのパス、XMLファイルのパスを確認してください。

#### 終了スクリプトの作成

次に**robotcontroller_exit.bat**、**robotcontroller_exit.sh**を編集します。

以下のコマンドを記述してください。

```
 rtexit localhost/RaspberryPiMouseSimulator0.rtc
 rtexit localhost/%COMPUTERNAME%.host_cxt/RobotController0.rtc
```

Ubuntuの場合は以下のコマンドを記述してください。

```
 HOSTNAME=`hostname`
 rtexit localhost/RaspberryPiMouseSimulator0.rtc
 rtexit localhost/${HOSTNAME}.host_cxt/RobotController0.rtc
```

編集が終わったら、robotcontroller_exit.bat、robotcontroller_exit.shを実行してみてください。
問題がなければ実行中のRTCが終了するはずです。



