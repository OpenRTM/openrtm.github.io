---
layout: page
title: 自作の rtc で制御
---

<!-- Title: 自作の RTC で制御 -->
#contents

## 初心者用課題
### ひな形コードの作成
新規作成した RTC を EducatorVehicle と接続して制御するまでの手順を説明します。

まずは Windows、Ubuntu上で [このページ]({{ site.baseurl }}/ja/doc/toolmanuals/rtcbuilder-1_1_0) の手順に従って RTC を作成してください。
RTC の仕様は以下のように入力します。


<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">基本</th>
  </tr>
  <tr>
    <td>モジュール名</td>
    <td colspan="2" style="text-align: center;">EV3SampleCPP、もしくはEV3SamplePy</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">アクティビティ</td>
  </tr>
  <tr>
    <td>有効アクション</td>
    <td colspan="2" style="text-align;">onInitialize、onExecute、onActivated、onDeactivated</td>
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
    <td>touch</td>
    <td>RTC::TimedBooleanSeq</td>
    <td>タッチセンサーのオンオフ</td>
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
    <td>sound</td>
    <td>RTC::TimedString</td>
    <td>音声</td>
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
    <td>回転速度、デフォルト値は0.0、制約条件に-3.1<=x<=3.1、Widgetはslider、Stepは0.2</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">言語・環境</td>
  </tr>
  <tr>
    <td>言語</td>
    <td colspan="2" style="text-align: center;">C++、もしくは Python</td>
  </tr>
</table>

この RTC ではコンフィギュレーションパラメーター forward_velocity、rotate_velocity に入力した速度を target_velocity から EducatorVehicle に送信します。
さらに touch でタッチセンサーのオンオフを取得して、オンになった場合は停止して sound から発声する音を指令します。

※RTC は EV3上で動作させることを前提にしていますが、動作確認や講習会での利用には Windows や Ubuntu上で動作させても問題はないので、その場合はコードの編集をする前に CMake で Visual Studio、もしくは Code::Blocks のプロジェクトを生成しておくことをお勧めします。
CMake でプロジェクト生成からビルドまでの手順は以下のページに記載してあります。

- [Windows]({{ site.baseurl }}/ja/doc/toolmanuals/rtcbuilder-1_1_0/compile_win_cmake_cpp_rtcb_1_1_0)
- [Ubuntu]({{ site.baseurl }}/ja/content/build_ubuntu_codeblocks)

### コードの編集

まずは onExecute 関数を編集します。

以下はforward_velocity、rotate_velocityの 値を target_velocity から送信するコードです。

C++(src/EV3SampleCPP.cpp)

```
 RTC::ReturnCode_t EV3SampleCPP::onExecute(RTC::UniqueId ec_id)
 {
 	//コンフィギュレーションパラメータで設定した速度を送信する
 	m_target_velocity.data.vx = m_forward_velocity;
 	m_target_velocity.data.va = m_rotate_velocity;
 	setTimestamp(m_target_velocity);
 	m_target_velocityOut.write();
   return RTC::RTC_OK;
 }
```


Python(EV3SamplePy.py)
```
 	def onExecute(self, ec_id):
 		#コンフィギュレーションパラメータで設定した速度を送信する
 		self._d_target_velocity.data.vx = self._forward_velocity[0]
 		self._d_target_velocity.data.vy = 0
 		self._d_target_velocity.data.va = self._rotate_velocity[0]
 		OpenRTM_aist.setTimestamp(self._d_target_velocity)
 		self._target_velocityOut.write()
```


一応、非アクティブ状態の時は停止するように onDeactivated で速度0を送信するようにします。

C++(src/EV3SampleCPP.cpp)
```
 RTC::ReturnCode_t EV3SampleCPP::onDeactivated(RTC::UniqueId ec_id)
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

Python(EV3SamplePy.py)
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

[共通インターフェース仕様書](/ja/node/3853)（Projectページはリンク切れです）では進行方向をX軸正方向にしているため、Velocity2D型のvxに直進速度、vaに回転速度を入力します。


Pythonではさらにコンストラクタの以下の部分を修正してください。

Python(EV3SamplePy.py)
```
 		#self._d_target_velocity = RTC.TimedVelocity2D(*target_velocity_arg)
 		self._d_target_velocity = RTC.TimedVelocity2D(RTC.Time(0,0),RTC.Velocity2D(0,0,0))
```

```
 		#self._d_sound = RTC.TimedString(*sound_arg)
 		self._d_sound = RTC.TimedString(RTC.Time(0,0),[])
```


※ここまでの作業だけでも Educator Vehicle の動作は可能なので、面倒ならば以下の手順は飛ばしてもらっても大丈夫です。

次にタッチセンサーが ON になった時に停止する処理を書きます。
ここで touch に onExecute が呼び出された時に新規に受信したデータが必ず存在するとは限らないので、タッチセンサーのデータを一時的に格納しておく変数を宣言しておきます。


C++(include/EV3SampleCPP/EV3SampleCPP.h)

```
 private:
 	 bool m_last_sensor_data[2];	/*センサーのデータを格納する変数*/
```


Python(EV3SamplePy.py)

```
 	def __init__(self, manager):
 		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
 
 		#タッチセンサーのデータを格納する変数
 		self._last_sensor_data = [False, False]
```


次に onExecute にタッチセンサーがオンの場合に停止、音声を出力する処理を追加します。

C++(src/EV3SampleCPP.cpp)

```
 RTC::ReturnCode_t EV3SampleCPP::onExecute(RTC::UniqueId ec_id)
 {
 	//ここから
 	//データを新規に受信した場合に、データを m_last_sensor_data を格納する
 	if (m_touchIn.isNew())
 	{
 		m_touchIn.read();
 		if (m_touch.data.length() == 2)
 		{
 			for (int i = 0; i < 2; i++)
 			{
 				//タッチセンサーがOFFからONになった時に音を鳴らす
 				if (!m_last_sensor_data[i] && m_touch.data[i])
 				{
 					m_sound.data = "beep";
 					setTimestamp(m_sound);
 					m_soundOut.write();
 
 					
 				}
 				m_last_sensor_data[i] = m_touch.data[i];
 			}
 		}
 	}
 	//タッチセンサーがONの時に前進しないようにする
 	if (m_forward_velocity > 0)
 	{
 		for (int i = 0; i < 2; i++)
 		{
 			if (m_last_sensor_data[i])
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


Python(EV3SamplePy.py)

```
	def onExecute(self, ec_id):
 		#ここから
 		#データを新規に受信した場合に、データをm_last_sensor_dataを格納する
 		if self._touchIn.isNew():
 			data = self._touchIn.read()
 			if len(data.data) == 2:
 				for i in range(2):
 					#タッチセンサーがOFFからONになった時に音を鳴らす
 					if not self._last_sensor_data[i] and data.data[i]:
 						self._d_sound.data = "beep"
 						OpenRTM_aist.setTimestamp(self._d_sound)
 						self._soundOut.write()
 				self._last_sensor_data = data.data[:]
 
 
 		#タッチセンサーが ON の時に前進しないようにする
 		if self._forward_velocity[0] > 0:
 			for d in self._last_sensor_data:
 				if d:
 					self._d_target_velocity.data.vx = 0
 					self._d_target_velocity.data.vy = 0
 					self._d_target_velocity.data.va = 0
 					OpenRTM_aist.setTimestamp(self._d_target_velocity)
 					self._target_velocityOut.write()
 					return RTC.RTC_OK
 
 
		#ここまで
		#コンフィギュレーションパラメーターで設定した速度を送信する
		self._d_target_velocity.data.vx = self._forward_velocity[0]
 (以下略)
```

### ビルド
ソースコードの編集が終了したらC++の場合はビルドを行います。
EV3上で動作させる場合はクロスコンパイル環境でビルドを行ってください。
ソースコードのあるディレクトリに移動して以下のコマンドを入力すればビルドできます。

```
 cd EV3SampleCPP
 cmake .
 make
```

※Visual Studio、もしくは Code::Blocks で編集している場合は GUI上の操作でビルドを行ってください。

生成された src/EV3SampleCPPComp を EV3 に転送してください。
※Windows、Ubuntu で動作させる場合は転送しないでください。

```
 sftp robot@<IPアドレス>
 sftp> put EV3SampleCPP/src/EV3SampleCPPComp
```

Python版もEV3SamplePy.py を転送してください。

```
 sftp robot@<IPアドレス>
 sftp> put EV3SamplePy/EV3SamplePy.py
```

cmake がインストールされていない場合は以下のコマンドを入力してください。
```
 sudo apt-get install cmake
```


### RTC 起動
ビルドが完了したら RTC を起動します。 以下のコマンドで起動できます。
#### C++
```
 EV3SampleCPPComp&
```
#### Python
```
 python EV3SamplePy.py&
```

※Windows上で RTC を起動する場合は EV3SampleCPPComp.exe (EV3SamplePy.py) をダブルクリックしてください。

次に EducatorVehicle を起動させます。 以下のコマンドで起動してください。

```
 Compomnents/EducatorVehicleComp&
```

### 動作確認
まずは動作確認のためにデータポートの接続を行います。
Windows側で RTシステムエディタを起動してください。 
最初に EV3 で起動しているネームサーバーを RTシステムエディタのビューに追加します。 
ネームサーバー追加ボタンを押下して EV3 の IPアドレスを入力してください。

<div align="center"><a href="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm11.png"><img src="https://raw.githubusercontent.com/Nobu19800/RaspberryPiMouseRTSystem_script/master/rpm11.png" width="60%;"></a></div>

ネームサーバーを追加したらデータポートを以下のように接続してください。

<div align="center"><a href="ev3_sample.png"><img src="ev3_sample.png" width="60%;"></a></div>

<table class="table-alt">
  <tr>
    <th colspan="2" style="text-align: center;">ポートの接続</th>
  </tr>
  <tr>
    <td>EV3SampleCPP0(EV3SamplePy0)</td>
    <td>EducatorVehicle0</td>
  </tr>
  <tr>
    <td>target_velocity</td>
    <td>velocity2D</td>
  </tr>
  <tr>
    <td>touch</td>
    <td>touch</td>
  </tr>
  <tr>
    <td>sound</td>
    <td>sound</td>
  </tr>
</table>

そして RTC をアクティブ化すると動作を開始します。

まずは EV3SampleCPP(EV3SamplePy) のコンフィギュレーションパラメーターを変更する事で Educator Vehicle を操作してみます。

RTシステムエディタで EV3SampleCPP0(EV3SamplePy0) を選択して、Configuration View の編集を選択してください。

<div align="center"><a href="ev3_conf.png"><img src="ev3_conf.png" width="80%;"></a></div>

すると以下のウインドウが起動します。

<div align="center"><a href="ev3_conf2.png"><img src="ev3_conf2.png" width="80%;"></a></div>

forward_velocity と rotate_velocity のスライダーによりEV3を操作できます。

次にタッチセンサーがオンになった場合に停止するかを確認してみます。
タッチセンサーに物体を接触させて停止するかを確認してください。
停止した時に音が鳴るかも確認してください。


## 応用(中級者用課題)
ここからはさらにタッチセンサーがオンになった場合に後退→回転のより障害物を回避する動作を実装します。
タッチセンサーのデータが入力された時に以下の処理を実行することで回避運動を行います。

<div align="center"><a href="flowChart_4.png"><img src="flowChart_4.png" width="50%;"></a></div>


### コンフィギュレーションパラメーター
新たに以下のコンフィギュレーションパラメーターを設定します。

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
    <td>back_speed</td>
    <td>double</td>
    <td>後退速度、デフォルト値は0.1</td>
  </tr>
  <tr>
    <td>back_time</td>
    <td>double</td>
    <td>後退運動の時間、デフォルト値は1.0</td>
  </tr>
  <tr>
    <td>rotate_speed</td>
    <td>double</td>
    <td>回転速度、デフォルト値は0.8</td>
  </tr>
  <tr>
    <td>rotate_time</td>
    <td>double</td>
    <td>回転運動の時間、デフォルト値は2.0</td>
  </tr>
</table>


### 関数の実装
新たに以下の関数を実装します。

<table class="table-alt">
  <tr>
    <th>関数名</th>
    <th>内容</th>
    <th>引数</th>
  </tr>
  <tr>
    <td>stop_robot</td>
    <td>停止する</td>
    <td>なし</td>
  </tr>
  <tr>
    <td>back_move</td>
    <td>後退する</td>
    <td>なし</td>
  </tr>
  <tr>
    <td>rotate_move</td>
    <td>回転する</td>
    <td>dir(回転方向)</td>
  </tr>
</table>


#### stop_robot 関数
stop_robot関数は以下のようになっています。
目標速度を0に設定して送信します。

```
 void ControlEducatorVehicle::stop_robot()
 {
 	m_target_velocity_out.data.vx = 0;
 	m_target_velocity_out.data.vy = 0;
 	m_target_velocity_out.data.va = 0;
 	setTimestamp(m_target_velocity_out);
 	m_target_velocity_outOut.write();
 }
```

#### back_move 関数
back_move 関数は以下のようになっています。
後退するための速度を出力後、sleep 関数で指定時間だけ待つことによりコンフィギュレーションパラメータ back_speed の 速度でback_time の時間だけ後退する運動を実現しています。

```
 void ControlEducatorVehicle::back_move()
 {
 	//後退運動を指令
 	m_target_velocity_out.data.vx = -m_back_speed;
 	m_target_velocity_out.data.vy = 0;
 	m_target_velocity_out.data.va = 0;
 	setTimestamp(m_target_velocity_out);
 	m_target_velocity_outOut.write();
 	
 	//一定時間待つ
 	double sec, usec;
 	usec = modf(m_back_time, &sec);
 	
 	coil::TimeValue ts((int)sec, (int)(usec*1000000.0));
 	coil::sleep(ts);
 
 	//一旦停止
 	stop_robot();
 }
```

※onExecute 関数内で sleep 関数などで待機すると、その間は RTシステムエディタ等による操作ができなくなるためあまり望ましい実装の方法ではありません。
ただ今回の場合は実行コンテキストを止めずに処理を実装すると処理が複雑化するためこのように実装しています。

#### stop_robot 関数
rotate_move 関数は以下のようになっています。
後退運動と同じく、コンフィギュレーションパラメーター rotate_speed の速度で rotate_time の時間だけ回転運動する処理を実装しています。

```
 void ControlEducatorVehicle::rotate_move(bool dir)
 {
 	//回転運動を指令
 	m_target_velocity_out.data.vx = 0;
 	m_target_velocity_out.data.vy = 0;
 	//左回転
 	if (dir)m_target_velocity_out.data.va = m_rotate_speed;
 	//右回転
 	else m_target_velocity_out.data.va = -m_rotate_speed;
 	setTimestamp(m_target_velocity_out);
 	m_target_velocity_outOut.write();
 	
 	//一定時間待つ
 	double sec, usec;
 	usec = modf(m_rotate_time, &sec);
 	coil::TimeValue ts((int)sec, (int)(usec*1000000.0));
 	coil::sleep(ts);
 
 	//一旦停止
 	stop_robot();
 }
```


### onExecute 関数の実装
最後にフローチャートのように、タッチセンサーのデータ入力時に回避運動を行う処理を実装すれば完成です。

```
 RTC::ReturnCode_t ControlEducatorVehicle::onExecute(RTC::UniqueId ec_id)
 {
 	//目標速度を変数に格納
 	if (m_target_velocity_inIn.isNew())
 	{
 		m_target_velocity_inIn.read();
 		vx = m_target_velocity_in.data.vx;
 		vy = m_target_velocity_in.data.vy;
 		va = m_target_velocity_in.data.va;
 	}
 	//タッチセンサーの処理
 	if (m_touchIn.isNew())
 	{
 		while(m_touchIn.isNew())m_touchIn.read();
 		if (m_touch.data.length() >= 2)
 		{
 			touch_r = m_touch.data[0];
 			touch_l = m_touch.data[1];
 			//前進しているときのみ
 			if (vx > 0)
 			{
 				//左タッチセンサー
 				if (m_touch.data[0])
 				{
 					停止→後退→右回転
 					stop_robot();
 					back_move();
 					rotate_move(true);
 
 				}
 				//右タッチセンサー
 				else if (m_touch.data[1])
 				{
 					停止→後退→左回転
 					stop_robot();
 					back_move();
 					rotate_move(false);
 
 				}
 
 			}
 		}
 
 	}
 
 	m_target_velocity_out.data.vx = vx;
 	m_target_velocity_out.data.vy = vy;
 	m_target_velocity_out.data.va = va;
 
 	
 	
 	setTimestamp(m_target_velocity_out);
 	//目標速度送信
 	m_target_velocity_outOut.write();
 	
 	return RTC::RTC_OK;
 }
```


## 発展(上級者用課題)
ここでは[超音波センサーにより地面までの距離を検知して滑落を回避する RTC]({{ site.baseurl }}/ja/doc/casestudy/lego_mindstorm/lego_ev3_rtc_install#toc6) を作成します。

<div align="center"><a href="ev3_sensor.png"><img src="ev3_sensor.png" width="80%;"></a></div>

超音波センサーで検知した地面までの高さが一定以上の場合に、以下の処理を実行します。

<div align="center"><a href="flowChart2.png"><img src="flowChart2.png" width="50%;"></a></div>

### データポート、コンフィギュレーションパラメーター
以下のデータポート、コンフィギュレーションパラメーターを追加してください。

<table class="table-alt">
  <tr>
    <th colspan="3" style="text-align: center;">データポート</th>
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
    <td>ultrasonic</td>
    <td>RTC::RangeData</td>
    <td>超音波センサーをレンジセンサーと仮定し、要素1の距離データを格納</td>
  </tr>
  <tr>
    <td>current_pose</td>
    <td>RTC::TimedPose2D</td>
    <td>現在の位置・姿勢</td>
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
    <td>angle</td>
    <td>RTC::TimedDouble</td>
    <td>モーターMの角度</td>
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
    <td>sensor_height</td>
    <td>double</td>
    <td>接地可能と判定する地面までの高さ、デフォルト値は0.20</td>
  </tr>
  <tr>
    <td>medium_motor_range</td>
    <td>double</td>
    <td>Mモーターの動作範囲、デフォルト値は1.6</td>
  </tr>
</table>


### 関数の実装

接地可能な地面を超音波センサーで調べる search_ground 関数と、ロボットを指定した角度だけ回転させる turn_move 関数を実装します。

```
 bool ControlEducatorVehicle::search_ground(double &a)
 {
 	//Mモーターを右回転
 	m_angle.data = (-1)*m_medium_motor_range;
 	setTimestamp(m_angle);
 	m_angleOut.write();
 	coil::TimeValue ts(2, 0);
 	coil::sleep(ts);
 
 	//地面までの距離が一定以下かを判定
 	if (m_ultrasonicIn.isNew())
 	{
 		while(m_ultrasonicIn.isNew())m_ultrasonicIn.read();
 		if (m_ultrasonic.ranges.length() >= 1)
 		{
 			
 			if (m_ultrasonic.ranges[0] < m_sensor_height)
 			{
 				//一定以下の場合は接地可能と判定して、接地可能な地面を検知した方向を変数に格納
 				a = m_medium_motor_range;
 				return true;
 			}
 		}
 	}
 	
 	//Mモーターを左回転
 	m_angle.data = (-1)*-m_medium_motor_range;
 	setTimestamp(m_angle);
 	m_angleOut.write();
 	ts = coil::TimeValue(4, 0);
 	coil::sleep(ts);
 
 	//地面までの距離が一定以下かを判定
 	if (m_ultrasonicIn.isNew())
 	{
 		while(m_ultrasonicIn.isNew())m_ultrasonicIn.read();
 		if (m_ultrasonic.ranges.length() >= 1)
 		{
 			
 			if (m_ultrasonic.ranges[0] < m_sensor_height)
 			{
 				//一定以下の場合は接地可能と判定して、接地可能な地面を検知した方向を変数に格納
 				a = -m_medium_motor_range;
 				return true;
 			}
 				
 		}
 	}
 	
 
 	m_angle.data = 0;
 	setTimestamp(m_angle);
 	m_angleOut.write();
 	
 
 	
 	return false;
 }
```



```
 void ControlEducatorVehicle::turn_move(double a)
 {
 
 	int max_count = 100;
 	coil::TimeValue ts(0,10000);
 
 	//現在の姿勢を取得する
 	double spos = 0;
 	for (int i = 0; i < max_count; i++)
 	{
 		if (m_current_poseIn.isNew())
 		{
 			m_current_poseIn.read();
 			spos = m_current_pose.data.heading;
 			break;
 		}
 		coil::sleep(ts);
 		//一定時間内にデータを取得できなかった場合は回転運動を中止する
 		if (i == max_count - 1)return;
 	}
 	max_count = 1000;
 
 	//回転運動を開始する
 	double data_new_count = 0;
 	double max_data_new_count = 100;
 	for (int i = 0; i < max_count; i++)
 	{
 		if (m_current_poseIn.isNew())
 		{
 			while(m_current_poseIn.isNew())m_current_poseIn.read();
 
 			//目標姿勢角との差に定数を掛けた値を目標速度とする
 			double pos = m_current_pose.data.heading - spos;
 			double k = 1;
 			m_target_velocity_out.data.vx = 0;
 			m_target_velocity_out.data.vy = 0;
 
 
 			double diff = (a - pos);
 			double vela = k * diff;
 			if(vela > m_rotate_speed)vela = m_rotate_speed;
 			if(vela < -m_rotate_speed)vela = -m_rotate_speed;
 
 			//目標速度出力
 			m_target_velocity_out.data.va = vela;
 
 			setTimestamp(m_target_velocity_out);
 			m_target_velocity_outOut.write();
 			
 		
 			
 			
 			//目標姿勢角との差が一定以下の場合は停止して処理終了
 			if(sqrt(pow(diff,2)) < 0.03)
 			{
 				stop_robot();
 				return;
 			}
 
 			data_new_count = 0;
 		}
 		else
 		{
 			//一定時間データが取得できなかった場合は処理終了
 			data_new_count += 1;
 			if(data_new_count > max_data_new_count)
 			{
 				stop_robot();
 				return;
 			}
 			coil::sleep(ts);
 		}
 
 
 	}
 	stop_robot();
 	
 }
```

### onExecute 関数
最後に onExecute 関数を以下のように実装します。


```
 RTC::ReturnCode_t ControlEducatorVehicle::onExecute(RTC::UniqueId ec_id)
 {
 	//目標速度を変数に格納
 	if (m_target_velocity_inIn.isNew())
 	{
 		m_target_velocity_inIn.read();
 		vx = m_target_velocity_in.data.vx;
 		vy = m_target_velocity_in.data.vy;
 		va = m_target_velocity_in.data.va;
 	}
 	
 	//超音波センサーのデータ入力時の処理開始
 	if (m_ultrasonicIn.isNew())
 	{
 		while(m_ultrasonicIn.isNew())m_ultrasonicIn.read();
 		if (m_ultrasonic.ranges.length() >= 1)
 		{
 			range = m_ultrasonic.ranges[0];
 			//前進しているかの判定
 			if (vx > 0)
 			{
 				//超音波センサーで検知した地面までの高さが一定以上かの判定
 				if (m_ultrasonic.ranges[0] > m_sensor_height)
 				{
 					//停止フラグをtrueにする
 					//(次の超音波センサーデータ入力時に距離が一定以下と判定した場合は停止フラグをfalseにする)
 					stop_flag = true;
 					//一旦停止
 					stop_robot();
 					//Mモーターの角度を0に設定
 					m_angle.data = 0;
 					setTimestamp(m_angle);
 					m_angleOut.write();
  					//Mモーターを回転させて接地可能な地面を検知
 					double a = 0;
 					bool ret = search_ground(a);
 					//Mモーターの角度を0に設定
 					m_angle.data = 0;
 					setTimestamp(m_angle);
 					m_angleOut.write();
 					
 
 					
 					//接地可能な地面が見つかった場合は回転運動を行う
 					if (ret)
 					{
 						turn_move(a);
 					}
 					coil::TimeValue ts(2, 0);
 					coil::sleep(ts);
 					
 				}
 				//超音波センサーで検知した地面までの高さが一定以下の場合は停止フラグを false にする
 				else
 				{
 					stop_flag = false;
 				}
 
 			}
 		}
 	}
 
 	
 	//停止フラグが true の場合は停止する
 	if (stop_flag)
 	{
 		m_target_velocity_out.data.vx = 0;
 		m_target_velocity_out.data.vy = 0;
 		m_target_velocity_out.data.va = 0;
 	}
 	//停止フラグがfalseの場合は目標速度をそのまま出力
 	else
 	{
 		m_target_velocity_out.data.vx = vx;
 		m_target_velocity_out.data.vy = vy;
 		m_target_velocity_out.data.va = va;
 	}
 	
 	
 	
 	setTimestamp(m_target_velocity_out);
 	m_target_velocity_outOut.write();
 	
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

RTCをアクティブ化するには rtstart コマンドを使用します。

```
 rtstart testSystem.rtsys
```

RTCの非アクティブ化はrtstopコマンドを使用します。

```
 rtstop testSystem.rtsys
```

ポートを切断する場合は rtteardownコマンドを使用します。

```
 rtteardown testSystem.rtsys
```

注意点として、RTC はデフォルトの設定だとネームサーバーにはホスト名 .host_cxt 以下に登録されます。
ホスト名は環境によって違うので、この手順で RTシステムを保存しても他の環境では再現できないという事になります。
このため、rtc.conf を編集してネームサーバーの Root 直下に登録するようにすると、他の環境でも RTシステムの復元ができるようになります。

```
 naming.formats: %n.rtc
```
