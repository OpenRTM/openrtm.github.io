---
layout: page
title: "choreonoid用openrtm連携プラグイン python版 チュートリアル(四足歩行ロボット)"
---

このページではRTCEditorアイテム、ComponentListアイテムの利用方法を四足歩行ロボットのシミュレータ作成を例にして解説します。


<br>

<div align="center"><a href="choreonoid-openrtm-py345.png"><img src="choreonoid-openrtm-py345.png" width="50%;"></a></div>
<br>


#contents


## アイテム追加

### ワールド、シミュレータ

まずはワールドアイテム、シミュレータアイテムを追加します。 ファイル、新規からワールドとAISTシミュレータを選択して追加してください。

この時点でアイテムツリーは以下のようになります。
```
 World(ワールドアイテム)
    |-AISTSimulator(AISTシミュレータ)
```


### モデル

次に地面、四足歩行ロボットのモデルを追加します。

ファイル、読み込みから**OpenHRP モデルファイル**を選択後、以下のファイルを読み込んでください。

- {Choreonoidインストールディレクトリ}/share/model/QuadrupedRobot/QuadrupedRobot.yaml
- {Choreonoidインストールディレクトリ}/share/model/house/floor.body


すると以下のように3Dモデルが表示されます。
表示されない場合はアイテムツリー上の該当アイテムのチェックボタンをオンにしてください。

<br>

<div align="center"><a href="cnoid-rtm-py14.png"><img src="cnoid-rtm-py14.png" width="80%;"></a></div>
<br>



この時点でアイテムツリーは以下のようになります。

```
 World(ワールドアイテム)
    |-AISTSimulator(AISTシミュレータ)
    |-QuadrupedRobot(model/QuadrupedRobot/QuadrupedRobot.yaml)
    |-floor(model/house/floor.body)
```


### RTコンポーネント

#### PyRTCアイテム
RTコンポーネントを追加します。 ファイル、新規から**PyRTCItem**を選択して追加してください。

QuadrupedRobotアイテムの下にアイテムを追加して、**QuadrupedRobotIO**と名前を付けてください。

この時点でアイテムツリーは以下のようになります。

```
 World(ワールドアイテム)
    |-AISTSimulator(AISTシミュレータ)
    |-QuadrupedRobot(model/QuadrupedRobot/QuadrupedRobot.yaml)
      |-QuadrupedRobotIO(PyRTCItem)
    |-floor(model/house/floor.body)
```

##### Pythonファイルの設定
**QuadrupedRobotIO**のプロパティから**RTC module**という項目を設定してください。

ファイル名に**QuadrupedRobot_Choreonoid.py**を設定してください。
これで四足歩行ロボット用の入出力RTCが起動します。


#### ComponentListアイテム
RTCランチャーを起動します。ファイル、アイテムから**ComponentListItem**を選択して追加してください。


<br>

<div align="center"><a href="cnoid-rtm-py9.png"><img src="cnoid-rtm-py9.png" width="50%;"></a></div>
<br>


次にビューの表示から**ComponentList**を選択してください。

<br>

<div align="center"><a href="choreonoid-openrtm-py30.png"><img src="choreonoid-openrtm-py30.png" width="50%;"></a></div>
<br>


すると以下のウインドウが表示されます。


<br>

<div align="center"><a href="cnoid-rtm-py10.png"><img src="cnoid-rtm-py10.png" width="50%;"></a></div>
<br>


RTCはカテゴリ別に分類されており、タブを切り替えることでほかのカテゴリのRTCを表示できます。
**Controller**のタブを開いて、以下の2つのRTCを起動します。

- Foot_Position_Controller(四足歩行ロボット足先位置制御コンポーネント)
- Intermittent_Crawl_Gait_Controller(四足歩行ロボット間歇クロール歩容コンポーネント)

**実行(rtcd、周期実行)**ボタンを押すだけで起動できます。


※本来はトリガー駆動の実行コンテキストを使用したいのですが、OpenRTM-aist C++版のバグにより実現できていません。

<br>

<div align="center"><a href="cnoid-rtm-py48.png"><img src="cnoid-rtm-py48.png" width="50%;"></a></div>
<br>


この時点でRTCリストビューを更新すると以下のように表示されます。

<br>

<div align="center"><a href="cnoid-rtm-py12.png"><img src="cnoid-rtm-py12.png" width="30%;"></a></div>
<br>


#### RTCEditorアイテム

RTCエディタを起動します。ファイル、アイテムから**RTCEditorItem**を選択してワールドアイテムの下に追加してください。


<br>

<div align="center"><a href="cnoid-rtm-py13.png"><img src="cnoid-rtm-py13.png" width="50%;"></a></div>
<br>


すると以下のウインドウが表示されます。

<br>

<div align="center"><a href="cnoid-rtm-py2-2.png"><img src="cnoid-rtm-py2-2.png" width="50%;"></a></div>
<br>


##### データポート追加
四足歩行ロボットの目標速度を設定するアウトポートを追加します。
右側のウインドウから以下の設定を行ってください。

<table class="table-alt">
  <tr>
    <th>ポート名</th>
    <th>out</th>
  </tr>
  <tr>
    <td>ポート</td>
    <td>DataOutPort</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>RTC::TimedVelocity2D</td>
  </tr>
</table>


作成ボタンを押すとデータポートを作成します。

<br>

<div align="center"><a href="cnoid-rtm-py15.png"><img src="cnoid-rtm-py15.png" width="50%;"></a></div>
<br>


#### コード編集
ソースコードの編集を行います。

##### データポート変数名について
先ほど作成したデータポートにかかわる変数名については、右側の**データポート変数名**タブからコピーできます。


<br>

<div align="center"><a href="cnoid-rtm-py16.png"><img src="cnoid-rtm-py16.png" width="50%;"></a></div>
<br>


##### コード記述

左側のコード編集ウインドウは各アクティビティ+α(setBody、inputFromSimulator、outputToSimulator、グローバル)で実行する処理が記述できます。

**onExecute**関数の処理に以下を記述してください。

```
 self._d_out.data.vx = 0.03
 self._d_out.data.va = 0
 self._outOut.write()
 
 return RTC.RTC_OK
```


変更した内容は更新ボタンを押すと反映されます。

<br>

<div align="center"><a href="cnoid-rtm-py17.png"><img src="cnoid-rtm-py17.png" width="50%;"></a></div>
<br>


この時点でアイテムツリーは以下のようになります。

```
 World(ワールドアイテム)
    -AISTSimulator(AISTシミュレータ)
    -QuadrupedRobot(model/QuadrupedRobot/QuadrupedRobot.yaml)
    -QuadrupedRobotIO(PyRTCItem)
    -floor(model/house/floor.body)
    -ComponentList
    -RTCEditor
```

### RTシステム構築
**RTシステム**アイテム追加後、表示、ビューの表示から**RTCダイアグラム**を表示してください。

RTCの各ポートを以下のように接続してください。


<br>

<div align="center"><a href="cnoid-rtm-py18.png"><img src="cnoid-rtm-py18.png" width="50%;"></a></div>
<br>


この時点でアイテムツリーは以下のようになります。

```
 World(ワールドアイテム)
    |-AISTSimulator(AISTシミュレータ)
    |-QuadrupedRobot(model/QuadrupedRobot/QuadrupedRobot.yaml)
      |-QuadrupedRobotIO(PyRTCItem)
    |-floor(model/house/floor.body)
    |-ComponentList
    |-RTCEditor
    |-RTSystem
```

### シミュレータ起動

最後にシミュレーションを開始すると四足歩行ロボットが前進します。



#### 実行中のコード変更

シミュレータ起動中に例えば以下のようにRTCEditorのonExecute関数のコードを変更して更新ボタンを押すと、シミュレーション実行中に四足歩行ロボットが前進から旋回する運動に変化することが確認できます。


```
 self._d_out.data.vx = 0
 self._d_out.data.va = 0.8
 self._outOut.write()
 
 return RTC.RTC_OK
```



