---
layout: page
title: rtコンポーネント作成(nxtway編)
---
<!-- Title: RTコンポーネント作成(NXTway編) -->
#contents
#clear

## はじめに
- NXT MINDSTORM と OpenRTM の Bluetooth コンポーネントと接続し、NXT MINDSTORM をコントロールする方法を説明する。
- NXT MINDSTORM に対するソフトウェアのインストール方法および基本的な操作、RTコンポーネントとの接続する方法を説明する。

<div align="center"><a href="gaiyou.png"><img src="gaiyou.png" width="70%;"></a></div>

## 環境構築
### LEGO の組み立て
- 必要な部品
  - LEGO MINDSTORMS Education NXT Base Set
    - Product ID: W979797
<div align="center"><a href="XL_979797withtrays.jpg"><img src="XL_979797withtrays.jpg" width="70%;"></a></div>
  - LEGO Education Resource Set
    - Product ID: W979648
<div align="center"><a href="XL_9648Kit.jpg"><img src="XL_9648Kit.jpg" width="70%;"></a></div>
  - NXT Gyro Sensor
    - Part No : NGY1044
<div align="center"><a href="Mindstorms_Gyro.jpg"><img src="Mindstorms_Gyro.jpg" width="70%;"></a></div>
- LEGOの組み立て方法
  - 「NXTway-GS_Building_Instructions.pdf」参照すること
  - Download : http://lejos-osek.sourceforge.net/NXTway-GS_Building_Instructions.pdf

### nxtOSEK 環境設定(Windows XP/Vista)

<div align="center"><a href="kannkyousetumei.png"><img src="kannkyousetumei.png" width="70%;"></a></div>

- Cygwin のインストール
  - Cygwin は Windows 環境で各種の Linux ソフトウェアを実行できることである
  - Download : [http://www.cygwin.com/](http://www.cygwin.com/)
  - 設定オプション
    - Root Directory : 「c:\cygwin」
    - Select Packages : Devel カテゴリにある「make 3.81-1」と Libs カテゴリにある「libintl3」を選択してインストールする

- GNU ARM のインストール(必ず4.0.2) 
  - GNU ARM は NXT の ARM7コアプロセッサ(AT91SAM7S256)に対応した GCC コンパイラパッケージである
  - Download : [bu-2.16.1_gcc-4.0.2-c-c++_nl-1.14.0_gi-6.4.exe ](http://www.gnuarm.com/bu-2.16.1_gcc-4.0.2-c-c++_nl-1.14.0_gi-6.4.exe)
  - 設定オプション
    - Diriectory : 「c:\cygwin\GNUARM」
    - Select Components : 「Floating Point Unit」選択しない
    - Select Additional Tasks : 「Install Cygwin DLLs...」選択しない

- LEGO MINDSTORMS NXT Drive rのインストール
  - LEGO 社から提供される NXT とのUSB 通信ドライバーである
  - Download : http://mindstorms.lego.com/en-us/support/files/Driver.aspx
  - Driver 1.02 の PC バージョンをインストールする

- NeXTTool のダウンロード
  - NeXTTool は NXTと通信用 PC コンソールで、*.rxe(アプリ) と *.rfw(ファームウェア)を NXT にアップできる
  - Download : [http://bricxcc.sourceforge.net/nexttool.zip](http://bricxcc.sourceforge.net/nexttool.zip)
  - 設定オプション
    - 解凍ディレクトリ : 「c:\cygwin\nexttool」

- 拡張 NXT ファームウェアのダウンロード
  - 拡張 NXT ファームウェアは標準 NXT ファームウェアをベースに機能拡張したものである
  - NXT の ARM7 コアCPUのネイティブコードも実行できる
  - Download : [http://bricxcc.sourceforge.net/nexttool.zip](http://bricxcc.sourceforge.net/lms_arm_jch.zip)
  - 設定オプション
    - 「lms_arm_nbcnxc_107.rfw」だけをコピーする
    - コピーディレクトリー : 「c:\cygwin\nexttool」

- nxtOSEK のダウンロード
  - バージョン2.13 をダウンロードする
  - Download : [http://bricxcc.sourceforge.net/nexttool.zip](http://sourceforge.net/projects/lejos-osek/files/nxtOSEK/)
  - 設定オプション
    - 解凍ディレクトリ : 「c:\cygwin\nxtOSEK」

- 「sg.exe」ファイル追加
  - Download : [http://www.toppers.jp/download.cgi/osek_os-1.1.lzh](http://www.toppers.jp/download.cgi/osek_os-1.1.lzh)
  - 解凍して「toppers_osek」フォルダーの下に「sg」フォルダーの下にある「sg.exe」ファイルを「c:\cygwin\nxtOSEK\toppers_osek\sg」フォルダーにコピーする

## 拡張 NXT ファームウェアの NXT へのアップロード 
- NXT ファームウェアアップデートモード
  - 電流が ON の状態でリセットボタンを安全ピンの先で5秒ぐらい押し続ける
<div align="center"><a href="resetButton.jpg"><img src="resetButton.jpg" width="70%;"></a></div>
  - NXT スピーカーに小さなクリック音が聞こえるようになる
  - NXT と PC の USB 接続
- Cygwin 起動及び拡張ファームウェアアップロード
<a href="cygwin-icon.gif"><img src="cygwin-icon.gif" width="5%;"></a>
cygwinを起動する
  - 下記のコマンドを入力
```
 $cd c:\cygwin\nexttool
 $./NeXTTool.exe /COM=usb -firmware=lms_arm_nbcnxc_107.rfw
```
  - アップロードが完了すると、NXT の液晶画面が砂嵐画面のようになる
  - NXT のボタン操作できない場合は NXT のバッテリを外し再び装着することで拡張 NXT ファームウェアが起動

## NXTway ソース修正及びコンパイル
### NXT 側のソース修正及びコンパイル、アップロード
- ソース修正
  - 「c:\cygwin\nxtOSEK\samples_c++\cpp\NXTway_GS++」フォルダーにある「sample.cpp」の中で
<div align="center"><a href="samplecpp.png"><img src="samplecpp.png" width="70%;"></a></div>

  - 「btConnection.connect」で検索したら、下記の「Main Task」の中にある関数が検索できる

```
 //=============================================================================
 // Main Task
 TASK(TaskMain)
 {
 	// establish blutooth connection with a PC to use a PC HID GamePad controller
 	BTConnection btConnection(bt, lcd, nxt);
 	(void)btConnection.connect(BT_PASS_KEY);
 
 	for (U32 i = 5; i <= Lcd::MAX_CURSOR_Y; i++) lcd.clearRow(i);
 	lcd.cursor(0,5);
 	lcd.putf("snsns", "TOUCH:START/STOP", "STAND IT UP AND", "WAIT FOR A BEEP.");
 	lcd.disp();
 	SetRelAlarm(Alarm4msec, 1, 4); // Set 4msec periodical Alarm for the drive event
 
 	while(1)
 	{
 		sonarDriver.checkObstacles(sonar);
 		clock.wait(40); // 40msec wait
 	}
 }
```

  - 「(void)btConnection.connect(BT_PASS_KEY);」を下記のように修正する

```
 (void)btConnection.connect(BT_PASS_KEY, "alias")
```

  - "alias"の部分に自分が確認できる名前を入力する
- コンパイル
<a href="cygwin-icon.gif"><img src="cygwin-icon.gif" width="5%;"></a>cygwinを起動する
```
 $cd c:\cygwin\nxtOSEK\samples_c++\cpp\NXTway_GS++
```

  - cygwinの上で上のフォルダ「C:\cygwin\nxtOSEK\samples_c++\cpp\NXTway_GS++」で
```
 $make all
 ...
 Generating binary image file: nxtway_gs++_rom.bin
 Generating binary image file: nxtway_gs++_ram.bin
 Generating binary image file: nxtway_gs++_.rxe
 $
```

  - 上のようなメッセージを確認すればコンパイル完了
- NXT にアップロード
  - 拡張 NXT ファームウェアが入っている NXT を USB で接続する
  - コンパイルした cygwin の状態で
```
 $sh ./rxeflash.sh
 Executing NeXTTool to upload nxtway_gs++.rxe...
 nxtway_gs++.rxe=34240
 NeXTTool is terminated.
 $
```
  - 上のようなメッセージを確認したらアップロード完了

## 動作確認 
### NXT側の起動 
- 下の図で⑦番の状態で待機する
<div align="center"><a href="NXTStart.jpg"><img src="NXTStart.jpg" width="70%;"></a></div>;

### PC 側 RTC の起動
- OpenRTM-aist の Naming Service をスタートする
<div align="center"><a href="NamingServiceStart.png"><img src="NamingServiceStart.png" width="70%;"></a></div>
- TkJoyStickComp コンポーネントを起動する
<div align="center"><a href="TkJoyStickCompStart.png"><img src="TkJoyStickCompStart.png" width="70%;"></a></div>
- Bluetooth 接続
  - Bluetooth を ＰＣ に接続する
<div align="center"><a href="BluetoothPlus.png"><img src="BluetoothPlus.png" width="70%;"></a></div>
  - "alias"の部分で入れたネームの Bluetooth ディバイスを接続する
<div align="center"><a href="BluetoothPlus2.png"><img src="BluetoothPlus2.png" width="100;"></a></div>
  - Password は基本的に「1234」に設定されている
<div align="center"><a href="BluetoothPass.png"><img src="BluetoothPass.png" width="70%;"></a></div>
  - 接続した Bluetooth の Comport を確認する
<div align="center"><a href="BluetoothComport.png"><img src="BluetoothComport.png" width="70%;"></a></div>
- Bluetooth コンポーネントを起動
  - [BluetoothComp.zip]()（リンク切れです）をダウンロード
  - BluetoothComp.zipを解凍した後、「components」フォルダーにある「NXTBlueToothComp.exe」ファイルを実行する
<div align="center"><a href="NXTBluetoothCompStart.png"><img src="NXTBluetoothCompStart.png" width="70%;"></a></div>

- RT System Editor を起動
  - 下の図のようにRT System Editor を起動する
<div align="center"><a href="RTSystemEditorStart.png"><img src="RTSystemEditorStart.png" width="70%;"></a></div>
- Naming Service 追加
  - 下の図のように追加ボタンをクリックし、「127.0.0.1」を追加する
<div align="center"><a href="NamingServicetuika.png"><img src="NamingServicetuika.png" width="70%;"></a></div>
- コンポーネント配置
  - 下の図のようにコンポーネントを配置する
<div align="center"><a href="Componenthiichi.png"><img src="Componenthiichi.png" width="70%;"></a></div>
- TkJoyStickComp と Bluetooth コンポーネントを接続する
  - 下の図のように TkJoyStickComp と BluetoothComp を接続する
<div align="center"><a href="Componentsetuzoku.png"><img src="Componentsetuzoku.png" width="70%;"></a></div>
  - Bluetooth コンポーネントの Configuration View で「m_COM」変数に確認した Comport の番号を入れる
<div align="center"><a href="Setupm_COM.jpg"><img src="Setupm_COM.jpg" width="70%;"></a></div>
- Activate する
<div align="center"><a href="Activate.png"><img src="Activate.png" width="50%;"></a></div>
  - 接続が完了したら NXT 側が下の図のようになる
<div align="center"><a href="8.png"><img src="8.png" width="70%;"></a></div>

