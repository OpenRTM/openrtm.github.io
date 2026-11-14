---
layout: page
title: サンプルの rtシステムの実行
---

<!-- ~/jekyll_workdir/openrtm_test/ja/doc/casestudy/lego_mindstorm/lego_sample_rts_exec-->
<!-- Title: サンプルの RTシステムの実行 -->
#contents

## 事前準備
### Windows
#### RTC のインストール
サンプルの RTシステムの一部で以下の RTC を使用するためインストールしてください。

##### DirectInputRTC
ジョイスティックで操作するためのRTCです。
以下のサイトからインストーラーをダウンロードして実行してください。

- [http://ysuga.net/?p=130](http://ysuga.net/?p=130)

##### JoystickToVelocity
DirectInputRTC のアウトポートからの pos からの出力 (TimedLongSeq型) を TimedVelocity2D型に変換する RTC です。
以下のサイトからインストーラーをダウンロードして実行してください。


- [http://ysuga.net/?p=130](http://ysuga.net/?p=130)
<!-- - http://ysuga.net/?p=130-->

##### FloatSeqToVelocity

FloatSeqToVelocity は OpenRTM-aist-Python のサンプルTkJoyStick の出力 (TimedFloatSeq型) をTimeVelocity2D型でに変換してアウトポートから出力する RTC です。

[ここ](https://github.com/Nobu19800/FloatSeqToVelocity/archive/master.zip) からダウンロードしてください。

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">ducatorVehicle</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>in</td>
    <td>TimeFloatSeq</td>
    <td>変換前のデータ</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>データ型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>in</td>
    <td>TimedVelocity2D</td>
    <td>変換後のデータ</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">コンフィギュレーションパラメーター</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>デフォルト値</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>rotation_by_position</td>
    <td>-0.02</td>
    <td>ジョイスティックのX座標に対する回転角速度</td>
  </tr>
  <tr>
    <td>velocity_by_position</td>
    <td>0.002</td>
    <td>ジョイスティックのY座標に対する直進速度</td>
  </tr>
</table>

<div align="center"><a href="ev3_10.png"><img src="ev3_10.png" width="70%;"></a></div>

#### スクリプトファイル
RTC の起動、RTシステムの復元を自動化するためのスクリプトファイルです。
[ここ](https://github.com/Nobu19800/EducatorVehicle_script/archive/master.zip) からダウンロードしてください。

#### ネームサーバー、RTシステムエディタの起動
##### Windows
まず最初に Windows でネームサーバー、RTシステムエディタを起動してください。
詳しい手順は [このページ]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/test_windows_1_1) を参考にしてください。

##### ev3dev
EV3 の [一括インストールの項目](../lego_ev3_rtc_install#toc7) でダウンロードしたファイルの中に rtc.conf があるので、rtc.conf の以下の ppp.pp.pp.ppp の部分を Windows側の IPアドレスに変更してください。

```
 corba.nameservers: ppp.pp.pp.ppp
```

これで起動したコンポーネントが Windows のネームサーバーに登録されるようになります。

Windows で IPアドレスを確認するには以下のコマンドを入力します。

```
 ipconfig
```




<!-- OpenRTM-aist入りのev3devイメージファイルを使用している場合は、/home/robot/componentsの中にrtc.confがあるので、rtc.confの以下のppp.pp.pp.pppの部分をWindows側のIPアドレスに変更してください。 -->

<!-- Windows側のPCにゲームパッドを接続してから起動してください。 -->

<!-- corba.nameservers: ppp.pp.pp.ppp -->

<!-- これで起動したコンポーネントがWindowsのネームサーバーに登録されるようになります。 -->

<!-- WindowsでIPアドレスを確認するには以下のコマンドを入力します。 -->

<!-- ipconfig -->

## RTC の起動
### Windows
Windows側の RTC は [スクリプトファイルの項目](../lego_ev3_rtc_install#toc12) でダウンロードしたファイルの中に start_component.bat というバッチファイルがあるのでそれを実行すれば以下の RTC が起動します。
※64bit版 Windows、32bit版 OpenRTM-aist を対象にしています。32bit版 Windows の場合は start_component_32.bat、64bit版 OpenRTM-aist を利用する場合は start_component_64.bat を起動してください。
※Python のインストールしたディレクトリーにパスが通っていない場合、TkJoyStick は起動できません。お手数ですが [このページ]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/test_windows_python_1_1#toc7) の手順を参考にして手動で起動してください。

### ev3dev
[一括インストールの項目](../lego_ev3_rtc_install#toc7) でダウンロードしたフォルダーの中の start_rtc.sh を実行することで起動できます。

```
 cd RaspberryPiMouseRTSystem_script_Raspbian
 sh start_rtc.sh
```

これで以下の RTC が起動します。

```
 ControlEducatorVehicle0
 EducatorVehicle0
```

## RTシステムの復元、開始
Windows側で[スクリプトファイルの項目](../lego_sample_rts_exec#toc6) でダウンロードしたファイルの JoystickControlEV3 フォルダー内の JoystickControlEV3_resurrect.bat を実行してください。
これでデータポートの接続、コンフィギュレーションパラメーターの設定などが行われます。
次に JoystickControlEV3_activate.bat を実行すると RTC をアクティブ化します。
JoystickControlEV3 はジョイスティックコンポーネントから EV3 を操作する RTシステムです。



非アクティブにする際は JoystickControlEV3_stop.bat を起動してください。
JoystickControlEV3_teardown.bat を起動するとポートの接続を切断します。


## サンプルの詳細

JoystickControlEV3 以外のサンプルも `****_resurrect.bat` で RTシステム復元、`****_activate.bat` でアクティブ化、`****_stop.bat` で非アクティブ化、`****_teardown.bat` でポートの切断ができます。 
<table class="table-alt">
  <tr>
    <th>ファイル名</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>`****_resurrect.bat`</td>
    <td>RTシステム復元</td>
  </tr>
  <tr>
    <td>`****_activate.bat`</td>
    <td>アクティブ化</td>
  </tr>
  <tr>
    <td>`****_stop.bat`</td>
    <td>非アクティブ化</td>
  </tr>
  <tr>
    <td>`****_teardown.bat`</td>
    <td>ポートの切断</td>
  </tr>
</table>

### GamePadSimpleControlEV3
このサンプルはゲームパッドのアナログスティックで傾けた方向に Educator Vehicle を操作する RTシステムです。
Windows側の PC にゲームパッドを接続してから起動してください。

<div align="center"><a href="ev3_9.png"><img src="ev3_9.png" width="70%;"></a></div>

### JoystickSimpleControlEV3
このサンプルは OpenRTM-aist-Python のサンプルコンポーネント TkJoyStick で傾けた方向に Educator Vehicle を操作する RTシステムです。

<div align="center"><a href="ev3_8.png"><img src="ev3_8.png" width="70%;"></a></div>

### GamePadControlEV3
このサンプルはゲームパッドのアナログスティックで傾けた方向に Educator Vehicle を操作することに加えて、[タッチセンサー、超音波センサー、カラーセンサーを利用した制御](../lego_ev3_rtc_install#toc6) を行う RTシステムです。

<div align="center"><a href="ev3_6.png"><img src="ev3_6.png" width="70%;"></a></div>

### JoystickControlEV3
このサンプルは OpenRTM-aist-Python のサンプルコンポーネント TkJoyStick で傾けた方向に Educator Vehicle を操作することに加えて、[タッチセンサー、超音波センサー、カラーセンサーを利用した制御](../lego_ev3_rtc_install#toc6) を行う RTシステムです。

<div align="center"><a href="ev3_7.png"><img src="ev3_7.png" width="70%;"></a></div>
