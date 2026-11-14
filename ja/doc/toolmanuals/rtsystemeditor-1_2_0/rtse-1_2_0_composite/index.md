---
layout: page
title: システムエディタ（複合コンポーネント編）

---

<!-- Title: システムエディタ（複合コンポーネント編） -->
#contents

複合コンポーネントの操作を説明します。

### 複合コンポーネントを作成する
複数のコンポーネントをまとめて複合コンポーネントにすることができます。<br>
複合コンポーネントにしたいコンポーネントを選択して、右クリックして「Create Composite Component」を選択すると、複合コンポーネント生成ダイアログが表示されます。
<br>

<div align="center"><a href="fig66CreateCompositeComponent.png"><img src="fig66CreateCompositeComponent.png" width="50%;"></a></div>
<div align="center"><strong>複合コンポーネントの作成</strong></div>
<br>

<div align="center"><a href="SystemEditor_1302.jpg"><img src="SystemEditor_1302.jpg" width="60%;"></a></div>
<div align="center"><strong>複合コンポーネント生成ダイアログ</strong></div>
<br>

ダイアログの各項目は以下のとおりです。<br>

<div align="center"><strong>複合コンポーネント生成のダイアログ項目と必要条件</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>ダイアログ説明</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>①</td>
    <td>Manager</td>
    <td>ネームサービスビューに表示されているマネージャ一覧からマネージャを選択します。ここで選択されたマネージャが複合コンポーネントを生成します。</td>
  </tr>
  <tr>
    <td>②</td>
    <td>Name</td>
    <td>複合コンポーネントのインスタンス名を指定します。</td>
  </tr>
  <tr>
    <td>③</td>
    <td>Type</td>
    <td>複合コンポーネントの種別を指定します。指定可能な種別は以下のとおり。<br>[PeriodicECShared]<br>各RTCが ExecutionContext のみを共有する形で動作します。各RTCの状態は独立しているため、複合コンポーネント内で複数の状態が存在することもあります。<br>[PeriodicStateShared]<br>各RTCが同一の ExecutionContext を共有するとともに、状態も共有する形で動作します。<br>[Grouping]<br>各RTCが何も共有しない複合コンポーネントで、各RTCがそれぞれ ExecutionContext、状態を保持します。</td>
  </tr>
  <tr>
    <td>④</td>
    <td>Path</td>
    <td>複合コンポーネントに設定するパスを指定します。</td>
  </tr>
  <tr>
    <td>⑤</td>
    <td>Port</td>
    <td>子のコンポーネントのポート一覧から、複合コンポーネントに表示するポートを選択します。<br>ここで選択されたポートに対して、複合コンポーネントにプロキシ用のポートが作成されます。<br></td>
  </tr>
  <tr>
    <td>⑥</td>
    <td>-</td>
    <td>ポートの全選択・全解除ボタン</td>
  </tr>
</table>

複合コンポーネントを作成すると、子のコンポーネントとして選択していたコンポーネントはシステムエディタ上から表示が消え、新しい複合コンポーネントが描画されます。<br>
複合コンポーネントのダイアグラムをダブルクリックするか、右クリックして「エディタで開く」を選択すると、新しいシステムダイアグラムが開き、複合コンポーネント内部が表示されます。<br>
<br>

<div align="center"><a href="fig68CompositeOpenWithSE.png"><img src="fig68CompositeOpenWithSE.png" width="60%;"></a></div>
<div align="center"><strong>複合コンポーネントをシステムエディタで開く</strong></div>

<br>

<div align="center"><a href="fig69ViewCompositeComponent.png"><img src="fig69ViewCompositeComponent.png" width="60%;"></a></div>
<div align="center"><strong>複合コンポーネント内を表示するシステムエディタ</strong></div>
<br>

※ ただし、システム構成の保存時には、コンポーネントの描画情報はコンポーネントに対して１つしか保存できないため、複合コンポーネント内を表示するシステムダイアグラムで変更した描画情報は保存されません。
<br>


### 複合コンポーネントの子を追加する
複合コンポーネント内を表示するシステムエディタを開いて、ネームサービスビューから RTC をドラッグ＆ドロップすることで、複合コンポーネントの子が追加されます。追加された子RTCのポートはすべて非公開に設定されます。
<br>

<div align="center"><a href="fig70CompositeComponentAddRTC.png"><img src="fig70CompositeComponentAddRTC.png" width="70%;"></a></div>
<div align="center"><strong>子RTCの追加</strong></div>
<br>


### 複合コンポーネントの子を削除する
複合コンポーネント内を表示するシステムエディタを開いて、そこで子のコンポーネントを削除することで、複合コンポーネントの子が削除されます。<br>
削除された子のコンポーネントは、複合コンポーネント内から表示が消え、元のシステムダイアグラム（複合コンポーネント自身が表示されているダイアグラム）に表示されます。
<br>

<div align="center"><a href="fig71DeleteChildComponent.png"><img src="fig71DeleteChildComponent.png" width="70%;"></a></div>
<div align="center"><strong>複合コンポーネント内から子のコンポーネントを削除</strong></div>
<br>

<div align="center"><a href="fig72ChildComponent.png"><img src="fig72ChildComponent.png" width="70%;"></a></div>
<div align="center"><strong>複合コンポーネントが表示されているシステムエディタ上に子のコンポーネント表示</strong></div>
<br>


### 複合コンポーネントを削除する
複合コンポーネント上で右クリックして「Delete」を選択すると、複合コンポーネントがダイアグラムから削除されます。<br>
削除時に複合コンポーネントを別のシステムダイアグラムで開いていると、エディタの終了確認のダイアログが表示されます。
<br>

<div align="center"><a href="fig73DeleteCompositeComponent.png"><img src="fig73DeleteCompositeComponent.png" width="70%;"></a></div>
<div align="center"><strong>複合コンポーネントの削除</strong></div>
<br>

<div align="center"><a href="fig74CloseCompositeComponentDialog.png"><img src="fig74CloseCompositeComponentDialog.png" width="50%;"></a></div>
<div align="center"><strong>複合コンポーネントを表示するエディタの終了確認ダイアログ</strong></div>
<br>


### 複合コンポーネントを解除する
複合コンポーネント上で右クリックして「Decompose Composite Component」を選択すると、複合コンポーネントへexist()が送られ、コンポーネント自体を終了します。<br>
解除時に複合コンポーネントを別のシステムダイアグラムで開いていると、エディタの終了確認のダイアログが表示されます。<br>
複合コンポーネントが解除されると、子のコンポーネントが元のシステムダイアグラム（複合コンポーネントが表示されていたダイアグラム）に表示されます。
<br>

<div align="center"><a href="fig75DecomposeCompositeComponent.png"><img src="fig75DecomposeCompositeComponent.png" width="50%;"></a></div>
<div align="center"><strong>複合コンポーネントの解除</strong></div>
<br>

<div align="center"><a href="fig76CloseCompositeComponentDialog.png"><img src="fig76CloseCompositeComponentDialog.png" width="70%;"></a></div>
<div align="center"><strong>複合コンポーネントを表示するエディタの終了確認ダイアログ</strong></div>
<br>


### ポートの公開/非公開を切り替える
複合コンポーネント内を表示するシステムエディタにあるコンポーネントのポートが複合コンポーネント上に公開されている場合、下記のように別のアイコンで表示されます。
<br>

<div align="center"><strong>子RTCの公開されているポートのアイコン</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>名前</th>
    <th>形状</th>
  </tr>
  <tr>
    <td>1</td>
    <td>InPort</td>
    <td><div align="center"><a href="IconExportedInPort.png"><img src="IconExportedInPort.png" width="100;"></a></div></td>
  </tr>
  <tr>
    <td>2</td>
    <td>OutPort</td>
    <td><div align="center"><a href="IconExportedOutPort.png"><img src="IconExportedOutPort.png" width="100;"></a></div></td>
  </tr>
  <tr>
    <td>3</td>
    <td>ServicePort</td>
    <td><div align="center"><a href="IconExportedServicePort.png"><img src="IconExportedServicePort.png" width="100;"></a></div></td>
  </tr>
</table>

公開されているポートを右クリックして、「Unexport」を選択すると、そのポートが公開されていない状態に変わります。また、公開されていないポートを右クリックして、「Export」を選択すると、そのポートが公開されている状態に変わります。
<br>

<table class="table-alt">
  <tr>
    <th><div align="center"><a href="fig77ExportPort.png"><img src="fig77ExportPort.png" width="100%;"></a></div></th>
    <th><div align="center"><a href="fig77UnexportPort.png"><img src="fig77UnexportPort.png" width="100%;"></a></div></th>
  </tr>
</table>

<div align="center"><strong>ポートの公開/非公開</strong></div>
<br>

ただし、ポートが別のコンポーネントのポートと接続されている場合は、「Unexport」にすることができません。
<br>

<div align="center"><a href="fig78CantUnexport.png"><img src="fig78CantUnexport.png" width="70%;"></a></div>
<div align="center"><strong>ポートの接続がある場合</strong></div>
<br>


