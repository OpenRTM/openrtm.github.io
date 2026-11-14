---
layout: page
title: "comp_conf_reference"
---
#contents(3)

このドキュメントではコンポーネントごとの設定を行うファイルの設定項目を説明します。
このファイル名称は任意の名前をつけることができますが、便宜上 component.conf とします。
component.conf は以下のように rtc.conf 内でコンポーネントのカテゴリ名とコンポーネント名やインスタンス名をキーとするオプションで指定します。

```
 <コンポーネントカテゴリ名>.<コンポーネント名>.config_file: <任意のファイル名>.conf
 or
 <コンポーネントカテゴリ名>.<コンポーネントインスタンス名>.config_file: <任意のファイル名>.conf
```

サンプルに含まれる ConsoleIn コンポーネントを例にして、実際の指定方法を示します。

```
 example.ConsoleIn.config_file: consolein.conf ← ConsoleInコンポーネント全体の設定
 example.ConsoleIn0.config_file: consolein0.conf ← 0番目のインスタンスの設定
 example.ConsoleIn1.config_file: consolein1.conf ← 1番目のインスタンスの設定
 example.ConsoleIn2.config_file: consolein2.conf ← 2番目のインスタンスの設定
```

<!-- ============================================================ -->
## 基本設定
<!-- ============================================================ -->

### Basic Profile
RTCのBasic Profile (RTCBuilderの基本タブで設定する項目) の以下の項目は、component.conf で値を上書きすることができます。

- implementation_id
- type_name
- description
- version
- vendor
- category
- activity_type
- max_instance
- language
- lang_type


<!-- ============================================================ -->
## 実行コンテキストオプション
<!-- ============================================================ -->

### exec_cxt.periodic.type

Periodic型ExecutionContextの指定。
使用するECの型を指定します。以下の方が利用できます。

- PeriodicExecutionContext: デフォルト。OpenRTMライブラリに埋め込み。
- ExtTrigExecutionContext:   外部トリガEC。OpenRTMライブラリに埋め込み。
- SynchExtTriggerEC: 同期型外部トリガEC。OpenRTMライブラリに埋め込み。通常OpenHRP3とともに使用される。
- RTPreemptEC:               Linux RTプリエンプティブパッチカーネルのリアルタイム実行コンテキスト。

その他のEC

- SimulatorExecutionContext: 並列型外部トリガEC。ChoreonoidのOpenRTMPluginに内蔵されており、Choreonoid内で自動的に使用される。
- ArtExecutionContext:       ARTLinux用リアルタイムEC。廃止予定。(http://sourceforge.net/projects/art-linux/)

- 設定: (PeriodicExecutionContext|ExTrigExecutionContext|SynchExtTriggerEC|RTPreemptEC)
- デフォルト: PeriodicExecutionContext
- 例:
```
 exec_cxt.periodic.type: PeriodicExecutionContext
```

<!-- ------------------------------------------------------------ -->
### exec_cxt.periodic.rate

ExecutionContextの実行周期
<!-- The execution cycle of ExecutionContext -->

このオプションはRTC特有のECの周期を指定します。このECの実行周期は、元のRTCのデフォルトのECレートを上書きします。

- 設定: Read/Write, period [Hz]
- デフォルト: 1000 [Hz]
- 例:
```
 exec_cxt.periodic.rate: 1000
```

<!-- ------------------------------------------------------------ -->
### exec_cxt.sync_transition
### exec_cxt.sync_activation
### exec_cxt.sync_deactivation
### exec_cxt.sync_reset

状態遷移モードの指定。
RTCはアクティブ化、非アクティブ化、およびリセットにより状態が遷移します。
一部の実行コンテキストは、メインロジックを異なるスレッドで実行します。
これらのフラグが YES に設定されている場合、アクティブ化、非アクティブ化、およびリセットは同期して実行されます。
つまり、これらのフラグが YES の場合、状態遷移の完了後にアクティブ化/非アクティブ化/リセット処理から返ります。

"synchronous_transition" は、同期遷移フラグを他のすべての同期遷移フラグに設定します（synchronous_activation / deactivation / resetting)。

- 設定: YES/NO
- デフォルト: YES
- 例:
```
 exec_cxt.sync_transition: YES
 exec_cxt.sync_activation: YES
 exec_cxt.sync_deactivation: YES
 exec_cxt.sync_reset: YES
```

<!-- ------------------------------------------------------------ -->
### exec_cxt.transition_timeout
### exec_cxt.activation_timeout
### exec_cxt.deactivation_timeout
### exec_cxt.reset_timeout

同期遷移時のタイムアウト時間。
同期遷移フラグをYESに設定すると、タイムアウト設定が利用可能になります。 
"transition_timeout" が設定されている場合、値はアクティブ化/非アクティブ化およびリセットの他のすべてのタイムアウトに設定されます

- 設定: タイムアウト時間 [s]
- デフォルト: 0.5 [s]
- 例:
```
 exec_cxt.transition_timeout: 0.5
 exec_cxt.activation_timeout: 0.5
 exec_cxt.deactivation_timeout: 0.5
 exec_cxt.reset_timeout: 0.5
```

<!-- ------------------------------------------------------------ -->
### exec_cxt.cpu_affinity

ECのCPU affinity (割当)の設定。
このオプションは、ECを特定のCPUにバインドします。 オプションは、CPU IDを識別するために、1つ以上のコンマ区切りの番号でなければなりません。 CPU IDは0から始まり、最大数はCPUコアの数-1です。 無効なCPU IDを指定すると、すべてのCPUがECに使用されます。

- 設定: CPU番号
- デフォルト: なし
- 例:
```
 exec_cxt.cpu_affinity: 0
```

<!-- ------------------------------------------------------------ -->
### execution_contexts

実行コンテキストの指定。
RTCは、0個以上の実行コンテキストにアタッチできます。 
"execution_contexts" オプションは、RTC固有にアタッチするECとその名前を指定します。
オプションが指定されていない場合、ECに関連する内部グローバルオプションまたはrtc.confオプションが使用されます。 
Noneを指定すると、ECは作成されません。
指定可能なECの種類は、"exec_cxt.type" で指定できるものと同じです。
また、ECの種類を指定すると同時に、その名前も指定することができます。
名前は、ECの周期などを指定するオプションのキーとしてに利用されます。

- 設定: None or <EC0>,<EC1>,...
  - <EC?>: ECtype(ECname)
- デフォルト: None
- 例:
```
 execution_contexts: PeriodicExecutionContext(pec1000Hz), \
                               PeriodicExecutionContext(pec500Hz)
```

<!-- ------------------------------------------------------------ -->
### ec.<EC name>.rate
### ec.<EC name>.synch_transition
### ec.<EC name>.transition_timeout

EC 特有の設定。
各ECは独自のコンフィグレーションを持つことができます。 
ECタイプ名またはECインスタンス名を使用して、個々の構成を指定できます。 
接続されたECは、<ECタイプ名>（<ECインスタンス名>）のような "execution_context" オプションで指定されます。
EC固有のオプションは、次のように指定できます。

- 設定: ec.<EC type name>.<option> or ec.<EC instance name>.<option>
- デフォルト: なし
- 例:
```
 ec.PeriodicExecutionContext.sync_transition: NO
 ec.pec1000Hz.rate: 1000
 ec.pec1000Hz.synch_transition: YES
 ec.pec1000Hz.transition_timeout: 0.5
 ec.pec500Hz.rate: 500
 ec.pec500Hz.synch_activation: YES
 ec.pec500Hz.synch_deactivation: NO
 ec.pec500Hz.synch_reset: YES
 ec.pec500Hz.activation_timeout: 0.5
 ec.pec500Hz.reset_timeout: 0.5
```

<!-- End of Execution context settings -->
<!-- ============================================================ -->

<!-- ============================================================ -->
## ポート設定
<!-- Port configurations -->
<!-- ============================================================ -->

### InPort オプション

- 書式
```
 port.inport.<port_name>.* -> InPortBase.init() の引数に渡される
 port.inport.dataport.*    -> InPortBase.init() の引数に渡される
```

- 例
```
 port.inport.dataport.provider_types: corba_cdr, direct, shm_memory
 port.inport.dataport.consumer_types: corba_cdr, direct, shm_memory
 port.inport.dataport.connection_limit: 1
```


### OutPort オプション

- 書式
```
 port.outport.<port_name>.* -> OutPortBase.init() の引数に渡される
 port.outport.<port_name>.* -> OutPortBase.init() の引数に渡される
```

- 例
```
 port.inport.dataport.provider_types: corba_cdr, direct, shm_memory
 port.inport.dataport.consumer_types: corba_cdr, direct, shm_memory
 port.inport.dataport.connection_limit: 1
```


### サービスポートオプション
- 書式
```
 port.corbaport.<port_name>.* -> CorbaPortBase.init() の引数に渡される
 port.corba.* -> CorbaPortBase.init() の引数に渡される 
```

<!-- End of Port configurations -->
<!-- ============================================================ -->

<!-- ============================================================ -->
## RTSystemEditorのコンフィギュレーションセットGUI設定

コンフィギュレーションパラメータは、RTSystemEditorのコンフィギュレーションセット設定ダイアログのGUIウィジェットから操作可能です。
通常、RTCBuilderでRTCを設計する場合、各パラメーターに割り当てるGUIウィジェットの種類を指定できますが、component.confからGUIウィジェットの割り当てを指定することもできます。

- 例
```
 conf.[configuration_set_name].[parameter_name]:
 conf.__widget__.[parameter_name]: GUI control type for RTSystemEditor
 conf.__constraint__.[parameter_name]: Constraints for the value
```

### 利用可能なウィジェット [<u>widget</u>] の一覧

#### 書式
```
 conf.__widget__.[widget_name]: [widget_type].[widget_option]
```

#### 書式詳細
- [widget_name]: widgetの名称=Configuration Setパラメータ名
  - text:          テキストボックス (デフォルト)
  - slider.<step>: 水平スライダー。<step> はスライダーのステップ単位。範囲制約オプション（後述）が必要。
  - spin:          スピンボタン。範囲制約オプション（後述）が必要。
  - radio:         ラジオボタン。列挙型制約オプション（後述）が必要。
  - checkbox:      チェックボックス。列挙型制約オプションが必要。パラメータはカンマ区切りのリストを解釈可能でなければならない。
  - ordered_list:   順序付きリスト。列挙型制約オプションが必要。パラメータはカンマ付きリストを解釈可能でなければならない。このコントロールでは、リストの中に列挙型の要素が1つ以上現れる。
- [widget_type]: 使用するwidgetのタイプ, (text, slider, spin, radio, checkbox, ordered_list,)
- [widget_option]: sliderのみステップ単位を指定可能

#### 例
```
 conf.__widget__.int_param0: slider.10
 conf.__widget__.int_param1: spin
 conf.__widget__.double_param0: slider.10
 conf.__widget__.double_param1: text
 conf.__widget__.str_param0: radio
 conf.__widget__.vector_param0: checkbox
 conf.__widget__.vector_param1: ordered_list
```

<!-- ------------------------------------------------------------ -->
### 利用可能な制約条件 [<u>constraints</u>] の一覧
<!-- GUI control constraint options [__constraints__]: -->

#### 書式
```
 conf.__constraints__.[parameter_name]:
```

#### 書式詳細
- なし:（空白）
- 即値: 100 (制約値)
- 範囲: <, >, <=, >= および変数 "x" が利用可能
- 列挙値:  (enum0, enum1, ...)
- 配列: <constraints0>, <constraints1>, ... for only array value
- ハッシュ値: {key0: value0, key1:, value0, ...}

#### 制約指定例
- 制約なし              : (blank)
- 即値                     : 100 (read only)
- 100 以上                : x >= 100
- 100 以下                : x <= 100
- 100 より大きい       : x > 100
- 100 未満                : x < 0
- 100 以上 200 以下: 100 <= x <= 200
- 100 より大きく 200 、未満 : 100 < x < 200
- 列挙型制約                : (9600, 19200, 115200)
- 配列                      : x < 1, x < 10, x > 100
- ハッシュ                 : {key0: 100<x<200, key1: x>=100}

- 例
```
 conf.__constraints__.int_param0: 0<=x<=150
 conf.__constraints__.int_param1: 0<=x<=1000
 conf.__constraints__.double_param0: 0<=x<=100
 conf.__constraints__.double_param1:
 conf.__constraints__.str_param0: (default,mode0,mode1)
 conf.__constraints__.vector_param0: (dog,monkey,pheasant,cat)
 conf.__constraints__.vector_param1: (pita,gora,switch)
```


