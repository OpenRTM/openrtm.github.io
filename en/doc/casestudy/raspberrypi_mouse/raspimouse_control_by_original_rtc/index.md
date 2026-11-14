---
layout: page
title: 自作の rtc で制御
---
<!-- Title: 自作の RTC で制御 -->
#contents

## 初心者用の課題
### ひな形コードの作成
新規作成した RTC を RaspberryPiMouseRTC と接続して制御するまでの手順を説明します。

まずは Windows、Ubuntu上で [このページ]({{ site.baseurl }}/en/doc/toolmanuals/rtcbuilder-1_1_0) の手順に従って RTC を作成してください。
RTC の仕様は以下のように入力します。


<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;" >基本</th>
  </tr>
  <tr>
    <td>モジュール名</td>
    <td>></td>
    <td>LEFT:RasPiMouseSampleCPP、もしくは RasPiMouseSamplePy</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">アクティビティ</td>
  </tr>
  <tr>
    <td>有効アクション</td>
    <td>></td>
    <td>LEFT:onInitialize、onExecute、onActivated、onDeactivated</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">データポート</td>
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
    <td>distance_sensor</td>
    <td>RTC::TimedShortSeq</td>
    <td>距離センサーの計測値</td>
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
    <td>target_velocity</td>
    <td>RTC::TimedVelocity2D</td>
    <td>目標速度</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">コンフィギュレーション</td>
  </tr>
  <tr>
    <td>名前</td>
    <td>型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>forward_velocity</td>
    <td>double</td>
    <td>直進速度、デフォルト値は0.0、制約条件に-0.20<=x<=0.20、Widgetはslider、Stepは0.02</td>
  </tr>
  <tr>
    <td>rotate_velocity</td>
    <td>double</td>
    <td>回転速度、デフォルト値は0.0、制約条件に-1.6<=x<=1.6、Widgetはslider、Stepは0.2</td>
  </tr>
  <tr>
    <td>stop_distance</td>
    <td>short</td>
    <td>距離センサーで物体を検知した場合に、前進しないようにする距離センサーの計測値、デフォルト値は300</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">言語・環境</td>
  </tr>
  <tr>
    <td>言語</td>
    <td>></td>
    <td>LEFT:C++、もしくは Python</td>
  </tr>
</table>


この RTC ではコンフィギュレーションパラメーター forward_velocity、rotate_velocity に入力した速度を target_velocity から RaspberryPiMouseRTC に送信します。
さらに distance_sensor で受信した距離センサーの計測値から、物体をある程度まで近づけると前進できなくなるようにします。

※RTC は Raspberry Pi 上で動作させることを前提にしていますが、動作確認や講習会での利用には Windows や Ubuntu上で動作させても問題はないので、その場合はコードの編集をする前に CMake で Visual Studio、もしくは Code::Blocks のプロジェクトを生成しておくことをお勧めします。CMake でプロジェクト生成からビルドまでの手順は以下のページに記載してあります。

- [Windows]({{ site.baseurl }}/en/doc/toolmanuals/rtcbuilder-1_1_0/compile_win_cmake_cpp_rtcb_1_1_0)
- [Ubuntu]({{ site.baseurl }}/en/content/build_ubuntu_codeblocks)

プロジェクトが生成できたら Visual Studio の場合は RasPiMouseSampleCPP.sln、Code::Blocks の場合は RasPiMouseSampleCPP.cbp を開いてソースコードの編集を行ってください。


### コードの編集

まずは onExecute 関数を編集します。

以下は forward_velocity、rotate_velocity の値を target_velocity から送信するコードです。

C++(src/RasPiMouseSampleCPP.cpp)
```
 RTC::ReturnCode_t RasPiMouseSampleCPP::onExecute(RTC::UniqueId ec_id)
 {
 	//コンフィギュレーションパラメーターで設定した速度を送信する
 	m_target_velocity.data.vx = m_forward_velocity;
 	m_target_velocity.data.va = m_rotate_velocity;
 	setTimestamp(m_target_velocity);
 	m_target_velocityOut.write();
   return RTC::RTC_OK;
 }
```


Python(RasPiMouseSamplePy.py)
```
 	def onExecute(self, ec_id):
 		#コンフィギュレーションパラメーターで設定した速度を送信する
 		self._d_target_velocity.data.vx = self._forward_velocity[0]
 		self._d_target_velocity.data.vy = 0
 		self._d_target_velocity.data.va = self._rotate_velocity[0]
 		OpenRTM_aist.setTimestamp(self._d_target_velocity)
 		self._target_velocityOut.write()
```


一応、非アクティブ状態の時は停止するように onDeactivated で速度0を送信するようにします。

C++(src/RasPiMouseSampleCPP.cpp)
```
 RTC::ReturnCode_t RasPiMouseSampleCPP::onDeactivated(RTC::UniqueId ec_id)
 {
 	//停止する
 	m_target_velocity.data.vx = 0;
 	m_target_velocity.data.vy = 0;
 	m_target_velocity.data.va = 0;
 	setTimestamp(m_target_velocity);
 	m_target_velocityOut.write();
 
   return RTC::RTC_OK;
 }
```

Python(RasPiMouseSamplePy.py)
```
 	def onDeactivated(self, ec_id):
 		#停止する
 		self._d_target_velocity.data.vx = 0
 		self._d_target_velocity.data.vy = 0
 		self._d_target_velocity.data.va = 0
 		OpenRTM_aist.setTimestamp(self._d_target_velocity)
 		self._target_velocityOut.write()
 		return RTC.RTC_OK
```

[共通インターフェース仕様書](/ja/node/3853)(No corresponding English project page available.) では進行方向をX軸正方向にしているため、Velocity2D型の vx に直進速度、va に回転速度を入力します。


Python ではさらにコンストラクタの以下の部分を修正してください。

Python(RasPiMouseSamplePy.py)
```
 		#self._d_target_velocity = RTC.TimedVelocity2D(RTC.Time(0,0),0)
 		self._d_target_velocity = RTC.TimedVelocity2D(RTC.Time(0,0),RTC.Velocity2D(0,0,0))
```


※ここまでの作業だけでもラズパイマウスの動作は可能なので、面倒ならば以下の手順は飛ばしてもらっても大丈夫です。


次に距離センサーで物体を検知した場合に停止する処理を書きます。
ここで distance_sensorにonExecute が呼び出された時に新規に受信したデータが必ず存在するとは限らないので、距離センサーのデータを一時的に格納しておく変数を宣言しておきます。


C++(include/RasPiMouseSampleCPP/RasPiMouseSampleCPP.h)

```
 private:
 	 int m_last_sensor_data[4]; /*センサーのデータを格納する変数*/
```


Python(RasPiMouseSamplePy.py)

```
 	def __init__(self, manager):
 		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
 
 		#センサーのデータを格納する変数
 		self._last_sensor_data = [0, 0, 0, 0]
```


次に onExecute に距離センサーが物体を検知した場合に停止する処理を追加します。

C++(src/RasPiMouseSampleCPP.cpp)

```
 RTC::ReturnCode_t RasPiMouseSampleCPP::onExecute(RTC::UniqueId ec_id)
 {
 	//ここから
 	//データを新規に受信した場合に、データをm_last_sensor_dataを格納する
 	if (m_distance_sensorIn.isNew())
 	{
 		m_distance_sensorIn.read();
 		if (m_distance_sensor.data.length() == 4)
 		{
 			for (int i = 0; i < 4; i++)
 			{
 				m_last_sensor_data[i] = m_distance_sensor.data[i];
 			}
 		}
 	}
 	//センサーの計測値がstop_distance以上の時に前進しないようにする
 	if (m_forward_velocity > 0)
 	{
 		for (int i = 0; i < 4; i++)
 		{
 			if (m_last_sensor_data[i] > m_stop_distance)
 			{
 				m_target_velocity.data.vx = 0;
 				m_target_velocity.data.vy = 0;
 				m_target_velocity.data.va = 0;
 				setTimestamp(m_target_velocity);
 				m_target_velocityOut.write();
 				return RTC::RTC_OK;
 			}
 		}
 	}
 	//ここまで
 	//コンフィギュレーションパラメーターで設定した速度を送信する
 	m_target_velocity.data.vx = m_forward_velocity;
 (以下略)
```


Python(RasPiMouseSamplePy.py)

	def onExecute(self, ec_id):
		#ここから
		#データを新規に受信した場合に、データをm_last_sensor_dataを格納する
		if self._distance_sensorIn.isNew():
			data = self._distance_sensorIn.read()
			if len(data.data) == 4:
				self._last_sensor_data = data.data[:]
```
 
```
		#センサーの計測値がstop_distance以上の時に前進しないようにする
		if self._forward_velocity[0] > 0:
			for d in self._last_sensor_data:
				if d > self._stop_distance[0]:
					self._d_target_velocity.data.vx = 0
					self._d_target_velocity.data.vy = 0
					self._d_target_velocity.data.va = 0
					OpenRTM_aist.setTimestamp(self._d_target_velocity)
					self._target_velocityOut.write()
					return RTC.RTC_OK
		#ここまで
		#コンフィギュレーションパラメーターで設定した速度を送信する
		self._d_target_velocity.data.vx = self._forward_velocity[0]
```
 (以下略)
```

一応ですが、onActivate 関数で m_last_sensor_data を0に設定するようにします。

C++(src/RasPiMouseSampleCPP.cpp)
```
 RTC::ReturnCode_t RasPiMouseSampleCPP::onActivated(RTC::UniqueId ec_id)
 {
 	for (int i = 0; i < 4; i++)
 	{
 		m_last_sensor_data[i] = 0;
 	}
   return RTC::RTC_OK;
 }
```

Python(RasPiMouseSamplePy.py)
```
 	def onActivated(self, ec_id):
 		self._last_sensor_data = [0, 0, 0, 0]
 		return RTC.RTC_OK
```

Raspbianにdoxygen がインストールされていない場合は CMakeLists.txt の以下の部分を修正してください。

```
 #option(BUILD_DOCUMENTATION "Build the documentation" ON)
 option(BUILD_DOCUMENTATION "Build the documentation" OFF)
```

編集が完了したら Raspberry Pi にソースコードを転送してください。
Tera Term を使用している場合はZIP等に圧縮して転送してから Raspberry Pi 側で解凍してください。

※Windows、Ubuntuで動作させる場合は転送しないでください。

### ビルド
ソースコードの編集が終了したら C++ の場合はビルドを行います。

※Visual Studio、もしくは Code::Blocks で編集している場合は GUI 上の操作でビルドを行ってください。


ソースコードのあるディレクトリーに移動して以下のコマンドを入力すればビルドできます。

```
 cd RasPiMouseSampleCPP
 cmake .
 make
```

cmakeがインストールされていない場合は以下のコマンドを入力してください。
```
 sudo apt-get install cmake
```



### RTC 起動
ビルドが完了したら RTC を起動します。
以下のコマンドで起動できます。

#### C++
```
 src/RasPiMouseSampleCPPComp -f rtc.conf&
```

#### Python
```
 python RasPiMouseSamplePy.py -f rtc.conf&
```

※Windows上で RTC を起動する場合は RasPiMouseSampleCPPComp.exe(RasPiMouseSamplePy.py)をダブルクリックしてください。

次に RaspberryPiMouseRTC を起動させます。
以下のコマンドで起動してください。

```
 cd RaspberryPiMouseRTC
 src/RaspberryPiMouseRTCComp -f rtc.conf&
```


### 動作確認
まずは動作確認のためにデータポートの接続を行います。
Windows側で RTシステムエディタを起動してください。
最初に Raspberry Pi で起動しているネームサーバーを RTシステムエディタのビューに追加します。
[ネームサーバー追加] ボタンをクリックして Raspberry Pi の IPアドレスを入力してください。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm11.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm11.png" width="100;"></a></div>

Raspberry Pi の IPアドレスは以下のコマンドで確認できます。

```
 ifconfig
```

ネームサーバーを追加したらデータポートを以下のように接続してください。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm15.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm15.png" width="100;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="2" style="text-align: center;">ポートの接続</th>
  </tr>
  <tr>
    <td>RasPiMouseSampleCPP0(RasPiMouseSamplePy0)</td>
    <td>RaspberryPiMouseRTC0</td>
  </tr>
  <tr>
    <td>target_velocity</td>
    <td>target_velocity_in</td>
  </tr>
  <tr>
    <td>distance_sensor</td>
    <td>ir_sensor_out</td>
  </tr>
</table>

そして RTC をアクティブ化すると動作を開始します。
動作開始前にモーター電源スイッチはONにしておいてください。


まずは RasPiMouseSampleCPP(RasPiMouseSamplePy) のコンフィギュレーションパラメーターを変更する事でラズパイマウスを操作してみます。

RTシステムエディタで RasPiMouseSampleCPP0(RasPiMouseSamplePy0) を選択して、Configuration View の編集を選択してください。

<div align="center"><a href="raspi_conf.png"><img src="raspi_conf.png" width="80%;"></a></div>

すると以下のウインドウが起動します。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm13.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm13.png" width="80%;"></a></div>

forward_velocity と rotate_velocity のスライダーによりラズパイマウスを操作できます。


次に距離センサーが障害物を検知した場合に停止するかを確認してみます。
forward_velocity を0.2等に設定して前進させてください。その状態で障害物を進行方向に置いて動作を確認してください。

停止した場合は forward_velocity を0未満に設定して後退すれば前進できるようになります。

参考までにですが、/dev/rtlightsensor0のデバイスファイルから取得できる数値とセンサーまでの距離との関係は以下のようになっています。


<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm14.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm14.png" width="100;"></a></div>


<table class="table-alt">
  <tr>
    <th>デバイスファイルから取得した数値</th>
    <th>実際の距離[m]</th>
  </tr>
  <tr>
    <td>1394</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>792</td>
    <td>0.02</td>
  </tr>
  <tr>
    <td>525</td>
    <td>0.03</td>
  </tr>
  <tr>
    <td>373</td>
    <td>0.04</td>
  </tr>
  <tr>
    <td>299</td>
    <td>0.05</td>
  </tr>
  <tr>
    <td>260</td>
    <td>0.06</td>
  </tr>
  <tr>
    <td>222</td>
    <td>0.07</td>
  </tr>
  <tr>
    <td>181</td>
    <td>0.08</td>
  </tr>
  <tr>
    <td>135</td>
    <td>0.09</td>
  </tr>
  <tr>
    <td>100</td>
    <td>0.10</td>
  </tr>
  <tr>
    <td>81</td>
    <td>0.15</td>
  </tr>
  <tr>
    <td>36</td>
    <td>0.20</td>
  </tr>
  <tr>
    <td>17</td>
    <td>0.25</td>
  </tr>
  <tr>
    <td>16</td>
    <td>0.30</td>
  </tr>
</table>


手作業で測った数値なので、あくまで参考までに利用してください。

今回作成したサンプルコードは [ここ](https://github.com/Nobu19800/RasPiMouseSample) から入手できます。

## 応用(中級者用課題)
ここからはさらに距離センサーで計測した距離が一定以下になった場合に回転のより障害物を回避する動作を実装します。
まず、ラズパイマウスのセンサーは以下のように取り付けられてあります。

<div align="center"><a href="ras.png"><img src="ras.png" width="100;"></a></div>

このため、右側のセンサーで計測した距離が一定以下の場合は左方向へ、左側のセンサーで計測した距離が一定以下の場合は右方向へ回転運動することで回避運動を行います。

### コンフィギュレーションパラメーター
新たに以下のコンフィギュレーションパラメーターを設定します。
前進する速度が stop_velocity 以上で、さらにセンサーの値が sensor_limit 以下の場合に回避運動を行います。

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">コンフィギュレーション</th>
  </tr>
  <tr>
    <td>名前</td>
    <td>型</td>
    <td>説明</td>
  </tr>
  <tr>
    <td>sensor_limit</td>
    <td>double</td>
    <td>回避運動を行う距離センサーの値、デフォルト値は10</td>
  </tr>
  <tr>
    <td>rotational_speed</td>
    <td>double</td>
    <td>回転速度、デフォルト値は1.6</td>
  </tr>
  <tr>
    <td>stop_velocity</td>
    <td>double</td>
    <td>前進しているとみなす速さ、デフォルト値は0.01</td>
  </tr>
</table>


### onExecute 関数の実装

onExecute 関数の実装を以下のように実装します。
ここで [動作確認の項目]({{ site.baseurl }}/en/content/rtc_create_raspimouse#toc6) で述べたように距離センサーは距離が短くなるほど大きな値を出力するので注意してください。

```
 RTC::ReturnCode_t RaspberryPiMouseController_DistanceSensor::onExecute(RTC::UniqueId ec_id)
 {
 	//距離センサーのデータを変数に格納
 	if (m_distance_sensorIn.isNew())
 	{
 		m_distance_sensorIn.read();
 		if (m_distance_sensor.data.length() >= 4)
 		{
 			m_ir_sensor_r0 = m_distance_sensor.data[0];
 			m_ir_sensor_r1 = m_distance_sensor.data[1];
 			m_ir_sensor_l1 = m_distance_sensor.data[2];
 			m_ir_sensor_l0 = m_distance_sensor.data[3];
 		}
 
 	}
 	//目標速度のデータを変数に格納
 	if (m_target_velocity_inIn.isNew())
 	{
 		m_target_velocity_inIn.read();
 		m_target_vx = m_target_velocity_in.data.vx;
 		m_target_vy = m_target_velocity_in.data.vy;
 		m_target_va = m_target_velocity_in.data.va;
 	}
 
```

```
 	double vel = sqrt(m_target_vx*m_target_vx);
 	//右側のセンサーの値が一定以上かを判定(動作確認の項で述べた通り、センサーの値は距離が短くなるほど大きな値を出力する)
 	//さらに前進速度が一定以上かを判定
 	if (((m_ir_sensor_r0 > m_sensor_limit) || (m_ir_sensor_r1 > m_sensor_limit)) && (vel > m_stop_velocity))
 	{
 		//左回転する速度を出力
 		m_target_velocity_out.data.vx = 0;
 		m_target_velocity_out.data.vy = 0;
 		m_target_velocity_out.data.va = m_rotational_speed;
 		setTimestamp(m_target_velocity_out);
 
 		m_target_velocity_outOut.write();
 	}
 	//右側のセンサーの値が一定以上化か判定
 	else if (((m_ir_sensor_l0 > m_sensor_limit) || (m_ir_sensor_l1 > m_sensor_limit)) && (vel > m_stop_velocity))
 	{
 		//右回転する速度を出力
 		m_target_velocity_out.data.vx = 0;
 		m_target_velocity_out.data.vy = 0;
 		m_target_velocity_out.data.va = -m_rotational_speed;
 		setTimestamp(m_target_velocity_out);
 
 
 		m_target_velocity_outOut.write();
 	}
 	//センサーが何も検知しない場合
 	else
 	{
 		//入力速度をそのまま出力
 		m_target_velocity_out.data.vx = m_target_vx;
 		m_target_velocity_out.data.vy = m_target_vy;
 		m_target_velocity_out.data.va = m_target_va;
 		setTimestamp(m_target_velocity_out);
 
 		m_target_velocity_outOut.write();
 	}
   return RTC::RTC_OK;
 }
```

## RTシステムの保存について
RTシステムの保存については RTシステムエディタ上でもできるのですが、rtshell により RTシステムの復元を自動化することができます。
RTシステムエディタでポートの接続、コンフィギュレーションパラメーターを設定後、rtcryo コマンドを実行してください。

```
 rtcryo localhost -o testSystem.rtsys
```

これで、testSystem.rtsys というファイルにRTシステムの情報が保存されます。

ただし今回の課題のように複数のネームサーバーに登録された RTC を使用する場合、以下のように複数のネームサーバーを指定する必要があります。

```
 rtcryo localhost 192.168.11.1 -o testSystem.rtsys
```

保存した RTシステムを復元するためには rtresurrect コマンドを使用します。

```
 rtresurrect testSystem.rtsys
```

RTC をアクティブ化するには rtstart コマンドを使用します。

```
 rtstart testSystem.rtsys
```

RTC の非アクティブ化は rtstop コマンドを使用します。

```
 rtstop testSystem.rtsys
```

ポートを切断する場合は rtteardown コマンドを使用します。

```
 rtteardown testSystem.rtsys
```

注意点として、RTC はデフォルトの設定だとネームサーバーにはホスト名. host_cxt 以下に登録されます。
ホスト名は環境によって違うので、この手順で RTシステムを保存しても他の環境では再現できないという事になります。
このため、rtc.conf を編集してネームサーバーの Root 直下に登録するようにすると、他の環境でも RTシステムの復元ができるようになります。

```
 naming.formats: %n.rtc
```
