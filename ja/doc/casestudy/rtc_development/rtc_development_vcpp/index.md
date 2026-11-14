---
layout: page
title: rtコンポーネント作成(vc++編)
---

<!-- Title: RTコンポーネント作成(VC++編) -->
#contents

# データポートのあるコンポーネント

ここでは、データポートを2つ持つコンポーネント (MRCConvertor) を VC8 にて作成します。

## コンポーネントの概要 

入力デバイスからのデータを車輪2つの速度に変換し、OutPort から出力するコンポーネント。

Joystick等の入力デバイスにて移動ロボット(前輪2、後輪1、前輪だけが駆動)を操作する際に、使用することができる。


作成する RTC の仕様は以下のとおりです。

- InPort
  - 移動ロボットに対する速度 (TimedFloatSeq)

- OutPort
  - 移動ロボットの車輪の速度 (TimedFloatSeq)

## MRCConvertor の雛型を生成 

RtcTemplate にて雛型を生成します。

### 作業用フォルダーの作成 
適当な場所に作業用フォルダーを作成します。

今回は、フォルダー名をコンポーネント名 (MRCConvertor) と同じにします。

1. "マイコンピューター"をダブルクリック
1. 作業用フォルダーを作成したいフォルダーへ移動
1. 右クリックして [新規作成] > [フォルダー] でフォルダーを作成

### CUI版 rtc-template 編 (gen.bat)

rtc-template の実行を簡単にするために、下記のようなバッチファイルを先ほど作成した作業用フォルダーに作成します。

```
 rtc-template.py -bcxx^
  --module-name=MRCConvertor --module-desc="Convertor component for MobileRobot component"^
  --module-version=1.0.0 --module-vendor=AIST --module-category=Category^
  --module-comp-type=DataFlowComponent --module-act-type=PERIODIC^
  --module-max-inst=1^
  --inport=velFromInput:TimedFloatSeq^
  --outport=velToWheel:TimedFloatSeq
```

### rtc-template (gen.bat) の実行

下記のように gen.bat ファイルを実行します。

```
 >gen.bat
  rtc-template.py -bcxx
  --module-name=MRCConvertor
  --module-desc="Convertor component for MobileRobot component"
  --module-version=1.0.0 --module-vendor=AIST
  --module-category=Category
  --module-comp-type=DataFlowComponent --module-act-type=PERIODIC
  --module-max-inst=1
  --inport=velFromInput:TimedFloatSeq --outport=velToWheel:TimedFloatSeq

   File "MRCConvertor.h" was generated.
   File "MRCConvertor.cpp" was generated.
   File "MRCConvertorComp.cpp" was generated.
   File "Makefile.MRCConvertor" was generated.
   File "MRCConvertorComp_vc8.vcproj" was generated.
   File "MRCConvertor_vc8.vcproj" was generated.
   File "MRCConvertorComp_vc9.vcproj" was generated.
   File "MRCConvertor_vc9.vcproj" was generated.
   File "MRCConvertor_vc8.sln" was generated.
   File "MRCConvertor_vc9.sln" was generated.
   File "copyprops.bat" was generated.
   File "user_config.vsprops" was generated.
   File "README.MRCConvertor" was generated.
   File "MRCConvertor.yaml" was generated.
```

### Eclipse版 RtcTemplate 編 

Eclipse版 RtcTemplate での対応は下記のようになります。

- Programing language selection: C++
- Module definition
  - Module name: MRCConvertor
  - Module decription: Convertor component for MobileRobot component
  - Module version: 1.0.0
  - Module vender: AIST
  - Module category: Category
  - Component type: DataFlowComponent
  - Component's activity type: PERIODIC
  - Number of maximum instance: 1
- InPort definition
  - Ports: Name:velFromInput Type:TimedFloatSeq
- OutPort definition
  - Ports: Name:velToWheel, Type:TimedFloatSeq


### copyprops.bat の実行 

RtcTemplate 実行により、copyprops.bat ファイルが作業用フォルダーに生成されます。

この copyprops.bat ファイルを用い、コンポーネントのビルドに必要な rtm_config.vsprops を作業フォルダーにコピーします。

copyprops.bat ファイルをダブルクリックしてください。


## MRCConvertor の実装 

### Visual Studio の起動 

MRCConvertorComp_vc8.vcproj をダブルクリックし、Visual Studio を起動します。

### ヘッダファイルの編集

Visual Studio のソリューションエクスプローラーにて、MRCConvertorComp > Header Files の順にクリックし、 MRCConvertor.h をダブルクリックします。

#### ヘッダファイルのインクルード
今回は、std::vector と math ライブラリを使用しますので、2つのヘッダファイルをインクルードします。

```
 #include <vector>
 // VC8 にて Math::M_PI を使用するため
 #define _USE_MATH_DEFINES
 #include <math.h>
```


- "virtual RTC::ReturnCode_t onExecute(RTC::UniqueId ec_id);"関数のコメントをはずします。

- メンバー変数とメソッドの宣言~
今回は、MobileRobot (前輪2、後輪1、前輪だけが駆動) の移動ベクトルを車輪速度に変換するためのメソッド convert()、変換に必要な係数 m_k を宣言します。


```
 private:  float m_k;
 
  /*!
   * @brief InPortからのデータ(X、Y) をMobileRobot用の車輪速度データに変換する。
   *        m_velFromInput.data[0]とm_velFromInput.data[1]だけを使用する。
   */
  std::vector<float> convert(float x, float y) {
	float th = atan2(y,x);
	float v  = m_k * hypot(x,y);
	std::vector<float> ret_val;
	ret_val.push_back(v * cos(th - (M_PI/4.0))); // left vel
	ret_val.push_back(v * sin(th - (M_PI/4.0))); // right vel
	return ret_val;
  }
```

### ソースファイルの編集 

Visual Studio のソリューションエクスプローラーにて、MRCConvertorComp > Source Files の順にクリックし、 MRCConvertor.cpp をダブルクリックします。


#### onExecute() の実装
onExecute() のコメントをはずし、以下のように実装します。


```
 /*!
  * @brief InPort からのデータ (X、Y) を MobileRobot用の車輪速度データに変換し、
  *        OutPort から出力する。
  */

 RTC::ReturnCode_t MRCConvertor::onExecute(RTC::UniqueId ec_id)
 {
   if (m_velFromInputIn.isNew()) {
 	m_velFromInputIn.read();
 	if (m_velFromInput.data.length() > 2) {
 	  std::vector<float>  con_val = this->convert(m_velFromInput.data[0],m_velFromInput.data[1]);
 	  for (int i = 0; i < 2; i++)
 		m_velToWheel.data[i] = con_val[i];
 	  m_velToWheelOut.write();
 	}
   }
   return RTC::RTC_OK;
 }
```

ここで行われていることは、

1. m_velFromInputIn.isNew() にて InPort にデータが届いているかをチェックする。
1. 新しいデータが届いていたら、m_velFromInputIn.read() で変数にデータを読み込む。
1. 読み込んだデータを convert() にて車輪速度に変換する。
1. 変換したデータを OutPort の変数にセットし、OutPort のバッファに書き込む。


## ビルド

Visual Studio のメニューから [ビルド] > [ソリューションのビルド] をクリックしコンポーネントのビルドを行います。


## rtc.conf の作成 

エディタにて以下の内容を記述し、rtc.conf というファイル名で Debug あるいは Release フォルダーに保存します。

```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```

## 実行

ビルドにてエラーが無かった場合、Debug あるいは Release フォルダーに rtc.conf を作成し、MRCConvertorComp.exe を実行します。

MRCConvertorComp.exe を実行する前に NamingService を起動してください。
### ネームサーバーの起動

＜OpenRTM-aist インストールフォルダー＞\bin\rtm-naming.batをダブルクリックしCORBAネームサーバーを起動します。


### MRCConvertorComp.exe の実行

Debug あるいは Release フォルダーに移動し、MRCConvertorComp.exe を実行します。

