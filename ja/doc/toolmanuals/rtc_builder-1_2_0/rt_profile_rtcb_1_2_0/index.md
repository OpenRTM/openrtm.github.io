---
layout: page
title: 画面構成と機能（rtプロファイルエディタ 編）
---

<!-- Title: 画面構成と機能（RTプロファイルエディタ 編） -->
#contents
<!-- *** RTプロファイルエディタ -->
ここでは、RTプロファイルエディタについて説明します。
<br>

<div align="center"><a href="fig3-2RTProfileEditor_ja.png"><img src="fig3-2RTProfileEditor_ja.png" width="50%;"></a></div>
<div align="center"><strong>RTプロファイルエディタ</strong></div>
<br>
　RTプロファイルエディタは、以下のページから構成されています。
<div align="center"><strong>RTプロファイルエディタ構成</strong></div>

<table class="table-alt">
  <tr>
    <th>№</th>
    <th>画面要素名</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>１</td>
    <td>基本プロファイル入力ページ</td>
    <td>RTコンポーネントのプロファイル情報など、コンポーネントの基本情報を入力します。</td>
  </tr>
  <tr>
    <td>２</td>
    <td>アクティビティ・プロファイル</td>
    <td>RTコンポーネントがサポートしているアクティビティ情報などを指定します。</td>
  </tr>
  <tr>
    <td>３</td>
    <td>データポート・プロファイル</td>
    <td>RTコンポーネントに付属するデータポートのプロファイルを入力します。</td>
  </tr>
  <tr>
    <td>４</td>
    <td>サービスポート・プロファイル</td>
    <td>RTコンポーネントに付属するサービスポートおよびサービスポートに付属するサービスインターフェースのプロファイルを入力します。</td>
  </tr>
  <tr>
    <td>５</td>
    <td>コンフィギュレーション</td>
    <td>RTコンポーネントに設定するユーザー定義のコンフィギュレーション・パラメーター報およびシステムのコンフィギュレーション情報を入力します。</td>
  </tr>
  <tr>
    <td>６</td>
    <td>ドキュメント生成</td>
    <td>生成対象の RTコンポーネントに追加する各種ドキュメント情報を入力します。</td>
  </tr>
  <tr>
    <td>７</td>
    <td>言語・環境</td>
    <td>生成対象のコード選択や OS などの実行環境に関する情報を入力します。</td>
  </tr>
  <tr>
    <td>８</td>
    <td>RTC.xml</td>
    <td>設定された情報を基に生成した RtcProfile の XML形式での表示・編集を行います。</td>
  </tr>
</table>

各ページの切り替えは、エディタ画面下部のタブを選択することで行うことができます。
<br>

### 基本プロファイル入力ページ 
RTコンポーネントのプロファイル情報など、コンポーネントの基本情報を入力するページです。
<br>

<div align="center"><a href="editor-basic.png"><img src="editor-basic.png" width="50%;"></a></div>
<div align="center"><strong>基本プロファイル入力ページ</strong></div>
<br>
以下に各入力項目について説明いたします。
<div align="center"><strong>基本プロファイル入力ページ　項目説明</strong></div>

<table class="table-alt">
  <tr>
    <th>項目</th>
    <th>説明</th>
    <th>必須</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;" >RT-Component Basic Profile</td>
  </tr>
  <tr>
    <td>モジュール名</td>
    <td>RTコンポーネントを識別する名前です。必須入力項目。この名前は、生成されるソースコード中で、コンポーネントの名前に使用されます。英数字のみ入力可能です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>モジュール概要</td>
    <td>RTコンポーネントの簡単な概要説明です。</td>
    <td>-</td>
  </tr>
  <tr>
    <td>バージョン</td>
    <td>RTコンポーネントのバージョンです。原則 x.y.z のような形式でバージョン番号を入力します。</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ベンダ名</td>
    <td>RTコンポーネントを開発したベンダ名です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>モジュールカテゴリ</td>
    <td>RTコンポーネントのカテゴリです。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>コンポーネント型</td>
    <td>RTコンポーネントの型です。以下の選択肢の中から指定可能です。<br>・STATIC：静的に存在するタイプの RTC です。動的な生成、削除は行われません。<br>・UNIQUE：動的に生成・削除はできるが、各コンポーネントが内部に固有状態を保持しており、必ずしも交換可能ではないタイプの RTC です。<br>・COMMUTATIVE：動的に生成・削除が可能で、内部の状態を持たないため、生成されたコンポーネントが交換可能なタイプの RTC です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>アクティビティ型</td>
    <td>RTコンポーネントのアクティビティタイプです。以下の選択肢の中から指定可能です。<br>・PERIODIC ：一定周期でRTCのアクションを実行するアクティビティタイプ<br>・SPORADIC ：RTCのアクションを不定期に実行するアクティビティタイプ<br>・EVENT_DRIVEN ：RTC のアクションがイベントドリブンであるアクティビティタイプ</td>
    <td>○</td>
  </tr>
  <tr>
    <td>コンポーネント種類</td>
    <td>RTコンポーネントの実行形態の種類です。以下の選択肢から選択可能です。(複数選択肢の組み合わせ可)<br>・DataFlow ： 周期的にアクションを実行する実行形態<br>・FSM ： 外部イベントによってアクションを実行する形態<br>・MultiMode ： 複数の動作モードを持つ実行形態</td>
    <td>○</td>
  </tr>
  <tr>
    <td>最大インスタンス数</td>
    <td>RTコンポーネント　インスタンスの最大数です。自然数を入力してください。</td>
    <td>-</td>
  </tr>
  <tr>
    <td>実行型</td>
    <td>ExecutionContext の型です。 以下から選択可能です。<br>・PeriodicExecutionContext ： 周期実行を行うExecutionContext<br>・ExtTrigExecutionContext ： 外部トリガによって実行を行う ExecutionContex</td>
    <td>○</td>
  </tr>
  <tr>
    <td>実行周期</td>
    <td>ExecutionContext の実行周期です。正の double型の数値が入力可能です（単位Hz）。</td>
    <td>-</td>
  </tr>
  <tr>
    <td>概要</td>
    <td>RTコンポーネントに関する説明です。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>RTC Type</td>
    <td>特定機能を実現するRTコンポーネントを区別する必要がある場合に指定します。</td>
    <td>－</td>
  </tr>
</table>

<br>

### アクティビティ・プロファイル入力ページ
生成対象の RTコンポーネントがサポートしているアクティビティに関する情報を入力するページです。
<br>

<div align="center"><a href="fig3-4ActivityProfile_ja.png"><img src="fig3-4ActivityProfile_ja.png" width="50%;"></a></div>
<!-- CENTER:''図 3-4 データポート・プロファイル入力ページ'' -->
<div align="center"><strong>アクティビティ・プロファイル入力ページ</strong></div>
<br>
Documentation セクションの内容は、アクティビティ毎に設定します。Documentation セクションには、選択中のアクティビティに対応した内容が表示されます。
<br>
以下に各入力項目について説明いたします。
<br>

<div align="center"><strong>アクティビティ・プロファイル入力ページ　項目説明</strong></div>
<table class="table-alt">
  <tr>
    <th>項目</th>
    <th>説明</th>
    <th>必須</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">Activity Profile</td>
  </tr>
  <tr>
    <td>onInitialize</td>
    <td>初期化処理です。コンポーネントライフサイクルの開始時に一度だけ呼ばれます。</td>
    <td>-</td>
  </tr>
  <tr>
    <td>onFinalize</td>
    <td>終了処理です。コンポーネントライフサイクルの終了時に1度だけ呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onStartup</td>
    <td>ExecutionContext が実行を開始するとき1度だけ呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onShutdown</td>
    <td>ExecutionContext が実行を停止するとき1度だけ呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onActivated</td>
    <td>非アクティブ状態からアクティブ化されるとき1度だけ呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onDeactivated</td>
    <td>アクティブ状態から非アクティブ化されるとき1度だけ呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onAborting</td>
    <td>ERROR 状態に入る前に1度だけ呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onError</td>
    <td>ERROR 状態にいる間に呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onReset</td>
    <td>ERROR 状態からリセットされ非アクティブ状態に移行するときに1度だけ呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onExecute</td>
    <td>アクティブ状態時に周期的に呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onStateUpdate</td>
    <td>on_execute の後毎回呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onRateChanged</td>
    <td>ExecutionContext の rate が変更されたとき呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onAction</td>
    <td>対応する状態に応じた動作を実行するために呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>onModeChanged</td>
    <td>モードが変更された時に呼ばれます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td style="text-align: center;" colspan="3">Documentation</td>
  </tr>
  <tr>
    <td>アクティビティ名</td>
    <td>現在選択されているアクティビティの名称を表示します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>動作概要</td>
    <td>対象アクティビティが実行する動作の概要説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>事前条件</td>
    <td>対象アクティビティを実行する前に成立すべき事前条件を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>事後条件</td>
    <td>対象アクティビティを実行した後に成立する事後条件を記述します。ただし、事前条件が満たされない状態で対象アクティビティが実行された場合は事後条件の成立は保証されません。</td>
    <td>－</td>
  </tr>
</table>

<br>



### データポート・プロファイル入力ページ 
RTコンポーネントに付属するデータポートの情報を入力するページです。
<br>

<div align="center"><a href="fig3-4InputDataPort_ja.png"><img src="fig3-4InputDataPort_ja.png" width="50%;"></a></div>
<div align="center"><strong>データポート・プロファイル入力ページ</strong></div>
<br>
各ポート (InPort/OutPort) を新規に追加する場合は、各セクションの [Add] ボタンをクリックしてください。
また、各セクションの [Delete] ボタンをクリックすると、選択中のポートを削除することができます。
ドキュメントセクションの内容はポート毎に設定することが可能です。ドキュメントセクションには、選択中のポートに対応した内容が表示されます。
以下に各入力項目について説明いたします。
<br>

<div align="center"><strong>データポート・プロファイル入力ページ　項目説明</strong></div>
<table class="table-alt">
  <tr>
    <th>項目</th>
    <th>説明</th>
    <th>必須</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">DataPortプロファイル</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>DataPort の名称です。半角英数字のみ入力可能です。<br>Data OutPort、Service Port と併せてポート名称は重複することができません。</td>
    <td>○</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">Detail</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>現在選択されている Data Port を｢ポート名(InPort/OutPort)｣の形式で表示します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>DataPort が扱うデータ型です。<br>設定画面にて指定した IDL 内で定義されているデータ型が利用可能です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>変数名</td>
    <td>DataPort に対応する変数名です。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>表示位置</td>
    <td>ビルドビュー内でのData InPortの表示位置です。</td>
    <td>○</td>
  </tr>
<!-- |Constraint|Data InPort で扱うデータに対する制約条件です。制約条件の記述方法については、3.2.9を参照してください。|－| -->
<!-- |Unit|Data InPort で扱うデータの単位です。|－| -->
<!-- |>|>|RT-Component Data OutPort Profile| -->
<!-- |Port name|Data OutPort の名称です。半角英数字のみ入力可能です。&br;Data InPort、Service Port と併せてポート名称は重複することができません。|○| -->
<!-- |Data Type|Data OutPort が扱うデータ型です。&br;設定画面にて指定したIDL内で定義されているデータ型が利用可能です。|○| -->
<!-- |Var Name|Data OutPort に対応する変数名です。|－| -->
<!-- |Disp. Position|ビルドビュー内での Data OutPort の表示位置です。|○| -->
<!-- |>|>|Documentation| -->
<!-- |ポート名|現在選択されている Data Port を｢ポート名(InPort/OutPort)｣の形式で表示します。|－| -->
  <tr>
    <td>概要説明</td>
    <td>データポートに対する概要説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>データポートの扱う型に対する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>データ数</td>
    <td>データが配列になる場合など、データ数に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>意味</td>
    <td>データの意味の説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>単位</td>
    <td>データ単位に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>発生頻度、周期</td>
    <td>データの発生頻度、周期に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>処理速度、周期</td>
    <td>データの処理速度、処理周期に関する説明を記述します。</td>
    <td>－</td>
  </tr>
</table>
<br>

### サービスポート・プロファイル入力ページ 
RTコンポーネントに付属するサービスポートの情報を入力するページです。
<br>

<div align="center"><a href="fig3-5InputServicePort_ja.png"><img src="fig3-5InputServicePort_ja.png" width="50%;"></a></div>
<div align="center"><strong>サービスポート・プロファイル入力ページ(サービスポート情報入力)</strong></div>
<br>
<br>

<div align="center"><a href="fig3-6InputServicePort2_ja.png"><img src="fig3-6InputServicePort2_ja.png" width="50%;"></a></div>
<!-- CENTER:''図 3-6 サービスポート・プロファイル入力ページ(サービスインターフェース情報入)'' -->
<div align="center"><strong>サービスポート・プロファイル入力ページ(サービスインターフェース情報入力)</strong></div>
<br>

新規サービスポートは、画面左側「 RT-Component Service Ports 」欄の｢ Add Port ｣を選択することで追加することができます。
画面左側「 RT-Component Service Ports 」にてサービスポートを選択した状態で、｢Add Interface ｣を選択することで新規サービスインターフェースを追加することができます。
画面左側「 RT-Component Service Ports 」にて、サービスポートもしくはサービスインターフェースを選択した状態で [Delete] を選択することで、選択したポート／インターフェースを削除することができます。
以下に各入力項目について説明いたします。


<br>
<div align="center"><strong> サービスポート・プロファイル入力ページ　項目説明(サービスポート)</strong></div>
<br>
<table class="table-alt">
  <tr>
    <th>項目</th>
    <th>説明</th>
    <th>必須</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">RT-Component Service Port Profile</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>サービスポートの名称です。半角英数字のみ入力可能です。<br>Data InPort、Data OutPort、Service Port名称は重複できません。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>表示位置</td>
    <td>ビルドビュー内でのサービスポートの表示位置です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">Documentation</td>
  </tr>
  <tr>
    <td>概要説明</td>
    <td>サービスポートに対する概要説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>I/F概要説明</td>
    <td>サービスポートに付属するサービスインターフェースの概要説明を記述します。</td>
    <td>－</td>
  </tr>
</table>

<br>

<div align="center"><strong> サービスポート・プロファイル入力ページ　項目説明(サービスポート)</strong></div>
<br>
<table class="table-alt">
  <tr>
    <th>項目</th>
    <th>説明</th>
    <th>必須</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">RT-Component Service Port Interface Profile</td>
  </tr>
  <tr>
    <td>インターフェース名</td>
    <td>サービスインターフェースの名称です。半角英数字のみ入力可能です。<br>サービスインターフェース名は重複することができません。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>方向</td>
    <td>サービスインターフェースの種類です。以下の選択肢から選択可能です。<br>・Provided：提供インターフェース(Service Provider用)<br>・Required：要求インターフェース(Service Consumer用)</td>
    <td>○</td>
  </tr>
  <tr>
    <td>インスタンス名</td>
    <td>サービスインターフェースのインスタンス名です。半角英数字のみ入力可能です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>変数名</td>
    <td>サービスインターフェースの変数名です。省略された場合は、インスタンス名を使用します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>IDLファイル</td>
    <td>サービスインターフェースで使用する IDL ファイル名を指定します。[Browse...] ボタンをクリックすると、ファイル選択ダイアログが表示されます。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>インターフェース型</td>
    <td>サービスインターフェースで使用するサービスの型です。IDL fileを指定するとIDL内で定義されている型情報が表示されます。半角英数字のみ入力可能です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>IDL Path</td>
    <td>IDLのサーチパスです。[Browse...] ボタンをクリックすると、ディレクトリー選択ダイアログが表示されます。</td>
    <td>－</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">Documentation</td>
  </tr>
  <tr>
    <td>概要説明</td>
    <td>サービスインターフェースに対する概要説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>引数</td>
    <td>サービスインターフェースの引数に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>戻り値</td>
    <td>サービスインターフェースの戻り値に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>例外</td>
    <td>サービスインターフェースの例外に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>事前条件</td>
    <td>サービスインターフェースのオペレーションを実行前に満たしておくべき事前条件に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>事後条件</td>
    <td>サービスインターフェースのオペレーションを実行後に満たす事後条件に関する説明を記述します。</td>
    <td>－</td>
  </tr>
</table>


<br>
### コンフィギュレーション・プロファイル入力ページ
RT コンポーネントに設定するユーザー定義のコンフィギュレーション・パラメーター情報およびその他システムのコンフィギュレーション情報を入力するページです。

<br>

<div align="center"><a href="fig3-7InputConfigProfile_ja.png"><img src="fig3-7InputConfigProfile_ja.png" width="50%;"></a></div>
<!-- CENTER:''図 3-7 コンフィギュレーション・プロファイル入力ページ'' -->
<div align="center"><strong>コンフィギュレーション・プロファイル入力ページ</strong></div>
<br>
ユーザー定義コンフィギュレーション・パラメーター情報およびシステム・コンフィギュレーション情報を新規に追加する場合は、各セクションの [Add] ボタンをクリックしてください。
また、各セクションの [Delete] ボタンをクリックすると、選択中のコンフィギュレーション情報を削除することができます。
<br>
Detail セクションおよび Documentation セクションの内容は、ユーザー定義コンフィギュレーション・パラメーター毎に設定することが可能です。
各セクションには、選択中のユーザー定義コンフィギュレーション・パラメーターに設定した内容が表示されます。
<br>
以下に各入力項目について説明いたします。
<div align="center"><strong>コンフィギュレーション・プロファイル入力ページ　項目説明</strong></div>

<table class="table-alt">
  <tr>
    <th>項目</th>
    <th>説明</th>
    <th>必須</th>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">RT-Component Configuration Parameter Definitions</td>
  </tr>
  <tr>
    <td>名称</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターの名称です。半角英数字のみ入力可能です。<br>ユーザー定義コンフィギュレーション・パラメーター名称は重複することができません。</td>
    <td>○</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">Detail</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>現在選択されているユーザー定義コンフィギュレーション・パラメーターを表示します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>データ型</td>
    <td>ユーザ定義コンフィギュレーション・パラメーターのデータ型です。<br>設定画面にて指定したIDL内で定義されているデータ型が利用可能です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターのデフォルト値です。２バイト文字を含む任意の値を設定可能です。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>変数名</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターの変数名です。半角英数字のみ入力可能です。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>単位</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターの単位です。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>制約条件</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターに対する制約条件を記述します。制約条件の記述方法については、[[制約情報の記述方式>#seiyaku]] を参照してください。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>RTSystemEditorのConfigurationViewにてコンフィギュレーション・パラメーターを設定する際に利用するコントロールを指定します。以下の値から選択可能です。<br>・text：テキストボックス(デフォルト設定)<br>・slider：スライダ<br>・spin：スピンボタン<br>・radio：ラジオボタン<br>・check：チェックボックス<br>・ordered_list：順序付きリスト</td>
    <td>○</td>
  </tr>
  <tr>
    <td>Step</td>
    <td>入力用コントロールとして、｢slider｣を選択した場合に、スライダの刻み幅を指定します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>現在選択されているユーザー定義コンフィギュレーション・パラメーターを表示します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>データ名</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターの名称に対する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターのデフォルト値に対する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>概要説明</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターに対する概要説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>単位</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターの単位に対する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>データレンジ</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターのデータ範囲に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>制約条件</td>
    <td>ユーザー定義コンフィギュレーション・パラメーターの制約条件に関する説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">RT-Component Configuration Parameter</td>
  </tr>
  <tr>
    <td>Configuration</td>
    <td>設定を行うコンフィギュレーション名です。一覧から選択します。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>設定対象コンフィギュレーションのデフォルト値です。予めデフォルト値が設定されている項目については、名称選択時にデフォルト値が設定されます。</td>
    <td>－</td>
  </tr>
</table>

<br>

### ドキュメント情報設定ページ
生成対象のRTコンポーネントに関する各種ドキュメント情報を入力します。<br>

<br>

<div align="center"><a href="fig3-8Documentinfo.png"><img src="fig3-8Documentinfo.png" width="100;"></a></div>
<!-- CENTER:''図 3-8 言語・環境情報入力ページ'' -->
<div align="center"><strong>ドキュメント情報入力ページ</strong></div>
<br>
このページで入力された情報は、生成されたコードに doxygen 形式で埋め込まれます。
<br>
以下に各入力項目について説明いたします。
<div align="center"><strong> ドキュメント情報設定ページ　項目説明</strong></div>

<table class="table-alt">
  <tr>
    <td>項目</td>
    <td>説明</td>
    <td>必須</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">コンポーネント概要</td>
  </tr>
  <tr>
    <td>概要説明</td>
    <td>生成するRTコンポーネントの概要説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>入出力</td>
    <td>RTコンポーネントの入出力に関する概略説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>アルゴリズムなど</td>
    <td>RTコンポーネントが使用しているアルゴリズムなどの説明を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">その他</td>
  </tr>
  <tr>
    <td>作成者・連絡先</td>
    <td>RTコンポーネントの作成者および連絡先に関する情報を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>ライセンス、使用条件</td>
    <td>RTコンポーネントのライセンス情報、使用条件に関する情報を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>参考文献</td>
    <td>参考文献情報を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">バージョンアップログ</td>
  </tr>
  <tr>
    <td>VersionUp Log</td>
    <td>今回の変更内容に関するログ情報を記述します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>ライセンス、使用条件</td>
    <td>過去のバージョンアップ時のログ情報を表示します。</td>
    <td>－</td>
  </tr>
</table>



### 言語・環境情報入力ページ 
入力した RT コンポーネント仕様に基づき生成するテンプレート・ソースコードの言語選択や、OS 等の実行環境、依存ライブラリなどを入力するページです。
<br>

<div align="center"><a href="editor-lang.png"><img src="editor-lang.png" width="50%;"></a></div>
<div align="center"><strong>言語・環境情報入力ページ</strong></div>
<br>

生成対象の言語ごとにセクションが分かれています。生成したい言語のセクションを選択し、各言語固有の設定情報を入力してください。
あるセクションを選択した場合には、他のセクションは全て閉じるようになっています。
コード生成実行時（基本プロファイル入力ページの [コード生成] ボタンクリック時）に選択されていたセクションの言語用テンプレートコードが生成されます。
以下に各入力項目について説明いたします。

<div align="center"><strong>言語・環境情報入力ページ　項目説明</strong></div>

<table class="table-alt">
  <tr>
    <td>項目</td>
    <td>説明</td>
    <td>必須</td>
  </tr>
  <tr>
    <td>言語</td>
    <td>生成対象の言語を指定します。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>Use old build environment.</td>
    <td>このチェックボックスを ON にすると、旧バージョンと同様なコード(Cmakeを利用しない形式)を生成します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">環境</td>
  </tr>
  <tr>
    <td>Version</td>
    <td>生成対象 RTC を実装している言語のバージョン情報を設定します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>OS</td>
    <td>生成対象 RTC が動作する OS 情報を設定します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>OS Version</td>
    <td>生成対象 RTC が動作する OS のバージョン情報を設定します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>生成対象 RTC が動作する CPU アーキテクチャ情報を設定します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>その他 OS 情報</td>
    <td>生成対象 RTC が動作する OS について、バージョン情報以外の補足情報を設定します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>その他 CPU 情報</td>
    <td>生成対象 RTC が動作する CPU について、アーキテクチャ情報以外の補足情報を設定します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td colspan="3" style="text-align: center;">ライブラリ情報</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>生成対象 RTC が利用する外部ライブラリの名称を指定します。</td>
    <td>○</td>
  </tr>
  <tr>
    <td>Version</td>
    <td>生成対象 RTC が利用する外部ライブラリのバージョン情報を指定します。</td>
    <td>－</td>
  </tr>
  <tr>
    <td>Info.</td>
    <td>生成対象 RTC が利用する外部ライブラリの補足情報を指定します。</td>
    <td>－</td>
  </tr>
</table>

<!-- Java セクションの Jar File の追加/削除は、セクション横の [Add]、[Delete] ボタンにて行うことができます。 -->
[Add] ボタンをクリックすると、一覧中に項目行が追加されます。そして、追加された行をクリックすると、ファイル選択ダイアログが表示されるますので対象ファイルを選択してください。
<!-- ~''※'' Ruby および C# については、現状では未対応です。 -->
<br>

### RTC プロファイル XML 編集ページ
入力した RTコンポーネント仕様を記した XML ファイル (RTC.xml) の内容確認、編集を行うページです。
他のページで設定した内容を確認したり、GUI 画面からは入力できない項目を直接編集するために使用します。
<br>


<div align="center"><a href="fig3-9InputLangEnv2_ja.png"><img src="fig3-9InputLangEnv2_ja.png" width="60%;"></a></div>
<div align="center"><strong>言語・環境情報入力ページ</strong></div>
<br>

表示される RTコンポーネント仕様の内容は、このページに切り替えた時に他ページで設定されている内容を基に作成されます。
<br>
画面右上の [Update] ボタンをクリックすると、このページで設定、変更した内容を他のページに反映させることができます (他のページへ反映させるのみで、ファイルへの書き込みは行いません) 。
また、以下のような画面が表示され、変更点を確認することができます。修正内容を他ページへ反映する場合には [OK] をクリックしてください。
<br>


<div align="center"><a href="fig3-9InputLangEnv3_ja.png"><img src="fig3-9InputLangEnv3_ja.png" width="50%;"></a></div>

<div align="center"><strong>XML編集内容比較画面</strong></div>
<br>


このページで直接入力した内容は、このページを表示している状態で保存した場合のみ保存されます。
このページにて内容編集後、他ページを開いた状態で保存すると、他のページにて入力した項目が優先されます。
このページの内容を保存する場合には、RTC.xml のスキーマ定義に従ったバリデーションが行われます。
バリデーション時にエラーが発見された場合は、以下のようなエラーメッセージが表示されますので、表示内容を参考に該当箇所を修正してください。
<br>


<div align="center"><a href="fig3-10ErrorXML_ja.png"><img src="fig3-10ErrorXML_ja.png" width="50%;"></a></div>
<div align="center"><strong>XML バリデーションエラーの例</strong></div>
<br>

&aname(seiyaku);
### 制約情報の記述方式
データポートおよびユーザ定義コンフィギュレーション・パラメーターへの制約条件は以下の書式で設定します。


<div align="center"><strong>制約条件の記述方式</strong></div>

<table class="table-alt">
  <tr>
    <th>設定内容</th>
    <th>設定書式</th>
  </tr>
  <tr>
    <td>指定なし</td>
    <td>空白</td>
  </tr>
  <tr>
    <td>100（即値）</td>
    <td>100</td>
  </tr>
  <tr>
    <td>100以上</td>
    <td>x >= 100</td>
  </tr>
  <tr>
    <td>100以下</td>
    <td>x<=100</td>
  </tr>
  <tr>
    <td>100超</td>
    <td>x>100</td>
  </tr>
  <tr>
    <td>100未満</td>
    <td>x<100</td>
  </tr>
  <tr>
    <td>100以上200以下</td>
    <td>100<=x<=200</td>
  </tr>
  <tr>
    <td>100超200未満</td>
    <td>100<x<200</td>
  </tr>
  <tr>
    <td>列挙型</td>
    <td>(9600,19200,115200)</td>
  </tr>
  <tr>
    <td>配列型</td>
    <td>x>100, x>200, x>300</td>
  </tr>
  <tr>
    <td>ハッシュ型</td>
    <td>{key0: 100<x<200, key1: x>=100}</td>
  </tr>
</table>



