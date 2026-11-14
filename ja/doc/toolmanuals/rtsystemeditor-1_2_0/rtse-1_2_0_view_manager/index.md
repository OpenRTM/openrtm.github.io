---
layout: page
title: ビュー（マネージャコントロールビュー編）
---
<!-- Title: ビュー（マネージャコントロールビュー編） -->
<!-- #contents -->

ここではマネージャコントロールビューについて説明します。
<br>

<div align="center"><a href="fig12ManagerControlView.png"><img src="fig12ManagerControlView.png" width="70%;"></a></div>
<div align="center"><strong>マネージャコントロールビューの位置</strong></div>
<br>

ネームサービスビューでマネージャを選択すると、マネージャコントロールビューがアクティブになり、選択されたマネージャを制御できるようになります。
<br>

<div align="center"><a href="fig13ManagerControlView.png"><img src="fig13ManagerControlView.png" width="100%;"></a></div>
<div align="center"><strong>マネージャコントロールビュー</strong></div>
<br>

<div align="center"><strong>マネージャコントロールビューの画面構成</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>①</td>
    <td>ロード可能モジュール一覧表示ボタン。</td>
  </tr>
  <tr>
    <td>②</td>
    <td>ロード済みモジュール一覧表示ボタン。</td>
  </tr>
  <tr>
    <td>③</td>
    <td>コンポーネント一覧表示ボタン。</td>
  </tr>
  <tr>
    <td>④</td>
    <td>コンポーネント生成ボタン。<br>コンポーネント作成ダイアログを開き、新しくコンポーネントを生成します。生成されたコンポーネントは③のコンポーネント一覧表示で表示されます。</td>
  </tr>
  <tr>
    <td>⑤</td>
    <td>マネージャ複製ボタン。新しいマネージャを起動します。※現在、仕様未定のため使用不可</td>
  </tr>
  <tr>
    <td>⑥</td>
    <td>マネージャ終了ボタン。選択中のマネージャを終了します。※現在、仕様未定のため使用不可</td>
  </tr>
  <tr>
    <td>⑦</td>
    <td>モジュール、およびコンポーネントの一覧を表示するテーブル。</td>
  </tr>
  <tr>
    <td>⑧</td>
    <td>モジュールを URL 指定でロードする場合に URL を指定します。</td>
  </tr>
  <tr>
    <td>⑨</td>
    <td>モジュールのロード、アンロードボタン。<br>⑦のテーブルで選択中のモジュール、もしくは URL で指定したモジュールをロード、アンロードします。</td>
  </tr>
</table>

マネージャにモジュールをロードするには [Loadable Modules] ボタンをクリックし、表示されたロード可能モジュールを選択すると、[Load] ボタンが有効になり、クリックするとモジュールがロードされます。<br>
また、「URL:」のテキストボックスにモジュールの URL を入力して [Load] ボタンをクリックすることにより、URL 指定でモジュールを追加することもできます。
<br>

<div align="center"><a href="fig14LoadModule.png"><img src="fig14LoadModule.png" width="100%;"></a></div>
<div align="center"><strong>モジュールのロード</strong></div>
<br>

モジュールをアンロードするには [Loaded Modules] ボタンをクリックし、表示されたロード済みモジュールを選択すると、[Unload] ボタンが有効になり、クリックするとモジュールがアンロードされます。
<br>

<div align="center"><a href="fig15UnLoadModule.png"><img src="fig15UnLoadModule.png" width="100%;"></a></div>
<div align="center"><strong>モジュールのアンロード</strong></div>
<br>

新しくコンポーネントを生成するには [Create] ボタンをクリックして、コンポーネント生成ダイアログを開き、生成するコンポーネントの種別を選択し、[OK] をクリックするとコンポーネントが生成されます。<br>
生成されたコンポーネントはマネージャによってネームサービスに登録され、[Active Components] ボタンで表示されるコンポーネント一覧に表示されるようになります。
<br>

<div align="center"><a href="fig16ComponentDialog.png"><img src="fig16ComponentDialog.png" width="60%;"></a></div>
<div align="center"><strong>コンポーネント生成ダイアログ</strong></div>
<br>

コンポーネントの種別は、マネージャにロード済みのモジュールで定義されているコンポーネントから選択します。<br>
Parameter にはコンポーネント生成パラメーターを指定することができ、「param1=value1&param2=value2」の形式で記述します。以下の共通パラメーターは、すべてのコンポーネントで設定可能です。
<br>

<div align="center"><strong>コンポーネント生成の共通パラメーター</strong></div>
<table class="table-alt">
  <tr>
    <th>パラメーター名</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>instance_name</td>
    <td>コンポーネントのインスタンス名。<br>指定しない場合はコンポーネント種別 (type_name)に通番を付与</td>
  </tr>
  <tr>
    <td>type_name</td>
    <td>コンポーネントの種別</td>
  </tr>
  <tr>
    <td>description</td>
    <td>コンポーネントの説明</td>
  </tr>
  <tr>
    <td>version</td>
    <td>コンポーネントのバージョン</td>
  </tr>
  <tr>
    <td>vendor</td>
    <td>コンポーネントの提供元</td>
  </tr>
  <tr>
    <td>category</td>
    <td>コンポーネントのカテゴリ</td>
  </tr>
</table>

<br>
また、コンポーネント生成パラメーターで ConfigurationSet の値も指定することができます。<br>
ConfigurationSet のパラメーターは「conf.NNNN.PPPP=VVVV」の形式で、NNNN には ConfigurationSet 名、PPPP にはパラメーター名、VVVV には設定値をそれぞれ指定します。<br>
例として、ConsoleIn のコンポーネントを生成し、mode1という名前の ConfigurationSet を作成し、input_mode、input_cycle というパラメーターを指定する場合は以下のようになります。
<br>

<div align="center"><a href="fig17ConfigurationSet.png"><img src="fig17ConfigurationSet.png" width="100%;"></a></div>
<div align="center"><strong>コンポーネント生成時に ConfigurationSet パラメーターを指定</strong></div>
<br>

その他にも、コンポーネントによって任意のパラメーターを指定することができます。
<br>


