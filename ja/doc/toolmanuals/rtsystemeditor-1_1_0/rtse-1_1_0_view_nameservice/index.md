---
layout: page
title: ビュー（ネームサービスビュー編）
---

<!-- Title: ビュー（ネームサービスビュー編） -->
#contents

ここでは、ネームサービスビューについて解説します。
<br>

OpenRTM-aist では RTC を管理・公開するためにネームサービスが使用されており、ネームサービスビューでは、この内容を表示/編集することができます。
<br>


### 機能概要
ネームサービスビューは、RTC をリアルタイムにグラフィカル操作する機能を持っています。提供される機能の一覧は以下のとおりです。
#clear

<div align="center"><strong>機能概要一覧</strong></div>
<table class="table-alt">
  <tr>
    <th>No.</th>
    <th>機能名称</th>
    <th>機能概要</th>
  </tr>
  <tr>
    <td>1</td>
    <td>ネームサーバー接続/編集機能</td>
    <td>ネームサーバーに接続し、登録されているコンポーネントをネームサービスビューにツリー形式で表示する。</td>
  </tr>
  <tr>
    <td>2</td>
    <td>コンポーネントプロファイル表示機能</td>
    <td>選択したコンポーネントのプロファイル情報をプロパティビューに表示する。</td>
  </tr>
</table>


### ネームサービスビューの起動

<div align="center"><a href="figNS3InitialOfNameServiceViewStart.png"><img src="figNS3InitialOfNameServiceViewStart.png" width="45%;"></a></div>
<div align="center"><strong>ビューの表示</strong></div>
<br>

メニューから[Window] > [Show View] > [Name Service View] を選択すると、ネームサービスビューが表示されます。
<br>

<div align="center"><a href="figNS4InitialOfNameServiceViewStart.png"><img src="figNS4InitialOfNameServiceViewStart.png" width="45%;"></a></div>
<div align="center"><strong>ネームサービスビューの初期起動時画面</strong></div>
<br>

同様に Eclipse に標準で用意されている「プロパティ」ビューも表示します。
<br>


### ネームサーバーに接続するには
ネームサーバーに接続するには、ネームサービスビューの上部に存在するボタンをクリックするか、コンテキストメニューにて [Add Name Service] を選択します。
<br>

<div align="center"><a href="figNS7ConnectNameService.png"><img src="figNS7ConnectNameService.png" width="50%;"></a></div>
<div align="center"><strong>ネームサーバーに接続する</strong></div>
<br>

ネームサーバー接続ダイアログでは、IPアドレスおよびポート番号を入力します。（ポート番号が省略された場合には、設定画面で設定されたポート番号が使用されます。デフォルトのポート番号は2809番ポートです）
<br>

<div align="center"><a href="figNS8NameServiceDialog.png"><img src="figNS8NameServiceDialog.png" width="50%;"></a></div>
<div align="center"><strong>ネームサーバーの接続ダイアログ</strong></div>
<br>

**※**Eclipseの（再）起動時には最後に接続したアドレスへ自動的に接続します。存在しない場合には、ローカルホストの2809番ポートに接続を試みます。


### ネームサーバーを画面から削除するには
接続しているネームサーバーを画面から削除するには、ネームサーバーを右クリックし [Delete from View] を選択します。
<br>

<div align="center"><a href="figNS9DeletefromView.png"><img src="figNS9DeletefromView.png" width="50%;"></a></div>
<div align="center"><strong>ネームサーバーを画面から削除する</strong></div>
<br>


### ネームサーバーの内容を表示する
接続したネームサーバーにコンポーネントが登録されていると、以下のように登録内容がツリー形式で表示されます。
<br>

<div align="center"><a href="figNS10View.png"><img src="figNS10View.png" width="50%;"></a></div><br>
<div align="center"><strong>ネームサービスビュー</strong></div>
<br>

各アイコンの意味は以下のとおりです。

<div align="center"><strong>ネームサーバーアイコンの一覧</strong></div>
<table class="table-alt">
  <tr>
    <td>№</td>
    <td>アイコン</td>
    <td>種類（KIND）</td>
    <td>名前</td>
  </tr>
  <tr>
    <td>1</td>
<td><a href="IconHostCxt.png"><img src="IconHostCxt.png" width="30%;"></a></td>
<td>host_cxt</td>
<td>ホストコンテキスト</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href="IconMgrCxt.png"><img src="IconMgrCxt.png" width="30%;"></a></td>
<td>mgr_cxt</td>
<td>ネージャコンテキスト</td>
  </tr>
  <tr>
    <td>3</td>
<td><a href="IconCateCxt.png"><img src="IconCateCxt.png" width="30%;"></a></td>
<td>cate_cxt</td>
<td>カテゴリコンテキスト</td>
  </tr>
  <tr>
    <td>4</td>
<td><a href="IconModCxt.png"><img src="IconModCxt.png" width="30%;"></a></td>
<td>mod_cxt</td>
<td>モジュールコンテキスト</td>
  </tr>
  <tr>
    <td>5</td>
<td><a href="IconElse.png"><img src="IconElse.png" width="30%;"></a></td>
<td>上記以外</td>
<td>フォルダー（上記以外のコンテキスト）</td>
  </tr>
  <tr>
    <td>6</td>
<td><a href="IconRTC.png"><img src="IconRTC.png" width="30%;"></a></td>
<td>なし</td>
<td>RTC</td>
  </tr>
  <tr>
    <td>7</td>
<td><a href="IconMgr.png"><img src="IconMgr.png" width="30%;"></a></td>
<td>なし</td>
<td>マネージャ</td>
  </tr>
  <tr>
    <td>8</td>
<td><a href="IconObj.png"><img src="IconObj.png" width="30%;"></a></td>
<td>なし</td>
<td>オブジェクト（RTC 以外のオブジェクト）</td>
  </tr>
  <tr>
    <td>9</td>
<td><a href="IconZombi.png"><img src="IconZombi.png" width="30%;"></a></td>
<td>なし</td>
<td>ネームサーバーにエントリされてはいるが、実体のオブジェクトにアクセスできないゾンビオブジェクト</td>
  </tr>
</table>

ネームサービスビューは、接続先の各ネームサーバーを常に監視し、表示の同期・更新を行っています。（監視の周期は、設定画面の[[接続周期:]]で変更することができます）。
また、明示的にネームサーバーの内容を再取得する場合にはリフレッシュを行うことができます。リフレッシュを行うには、ネームサービスビューの上部の [Refresh] ボタンをクリックするか、コンテキストメニューにて [Refresh] を選択します。
<br>

<div align="center"><a href="figNS11Refresh.png"><img src="figNS11Refresh.png" width="50%;"></a></div>
<div align="center"><strong>リフレッシュ</strong></div>
<br>


### ネームサービスビューの表示範囲を変更する
ネームサービスビューでは、RTC の数が多くなることによって操作する範囲が煩雑化するのを防ぐために、表示ルートの位置を移動する機能があります。<br>
表示ルートを移動するには、移動する先を選択し、ネームサービスビューの上部の [Go Into] ボタンをクリックするか、コンテキストメニューにて [Go Into] を選択します。
<br>

<div align="center"><a href="figNS12ChangeView.png"><img src="figNS12ChangeView.png" width="50%;"></a></div>
<div align="center"><strong>表示ルート変更</strong></div>
<br>

<div align="center"><a href="figNS13ChangeView.png"><img src="figNS13ChangeView.png" width="50%;"></a></div>
<div align="center"><strong>表示ルート変更例</strong></div>
<br>

移動後は、[Go Back] で1階層上に上ることができます。また、[Go Home] で最上位の階層に戻ります。


### ネームサービスビューの表示内容をフィルターする
ネームサービスビューでは、RTC の数が多くなることによって操作する範囲が煩雑化するのを防ぐための、もうひとつの方法として、フィルター（表示するエントリの種類を限定）する機能があります。<br>
フィルタを行うには、ネームサービスビューの上部に存在する [Name Serviceview Filter] ボタンをクリックします。
<br>

<div align="center"><a href="figNS14NameServiceFilter.png"><img src="figNS14NameServiceFilter.png" width="70%;"></a></div>
<div align="center"><strong>フィルターの指示</strong></div>
<br>

「Name Service Filters」ダイアログでは、非表示にするエントリの種類を、「Select elements to exclude from the view」欄から選択します。
<br>

<div align="center"><a href="figNS15FilterDialog.png"><img src="figNS15FilterDialog.png" width="50%;"></a></div>
<div align="center"><strong>ネームサービスフィルタダイアログ</strong></div>
<br>

ネームサービスビューの表示から除外したい要素にチェックをつけると、ネームサービスビューに表示されなくなります。<br>
「Naming object name」を有効にすると、オブジェクト名の条件に一致するものが非表示となります。<br>
オブジェクト名の条件は前方一致と部分一致が選択できます。
<br>

<div align="center"><a href="figNS16Filtering.png"><img src="figNS16Filtering.png" width="70%;"></a></div>
<div align="center"><strong>オブジェクト名によるフィルタリング</strong></div>
<br>


### ネームサービスからエントリを削除する
ネームサービスビューでは、ネームサービスのネーミングオブジェクトのエントリを削除することができます。ネーミングオブジェクトを削除するには、コンテキストメニューにて [Delete From Name Service] ボタンをクリックします。
<br>

<div align="center"><a href="figNS17DeleteFromNameService.png"><img src="figNS17DeleteFromNameService.png" width="70%;"></a></div>
<div align="center"><strong>ネームサービスから削除する</strong></div>
<br>


### ネームサービスへオブジェクトを登録する
ネームサービスビューで、ネームサービスにオブジェクトのエントリを登録することができます。<br>
オブジェクトを登録するには、配下にオブジェクトを追加したいコンテキストおよびオブジェクトのコンテキストメニューから、[Add Object] を選択します。
<br>

<div align="center"><a href="figNS18AddObject.png"><img src="figNS18AddObject.png" width="60%;"></a></div>
<div align="center"><strong>オブジェクトを追加する</strong></div>
<br>

<div align="center"><a href="figNS19AddObjectDialog.png"><img src="figNS19AddObjectDialog.png" width="60%;"></a></div>
<div align="center"><strong>オブジェクト追加ダイアログ</strong></div>
<br>

「オブジェクトを追加」ダイアログでは、オブジェクトの名前(Name)、種類(Kind)、および IOR を指定します。


### ネームサービスへコンテキストを登録する
ネームサービスビューで、ネームサービスにコンテキストのエントリを登録することができます。<br>
コンテキストを登録するには、配下にコンテキストを追加したいコンテキストのコンテキストメニューから、[Add Context] を選択します。
<br>

<div align="center"><a href="figNS20AddContext.png"><img src="figNS20AddContext.png" width="50%;"></a></div>
<div align="center"><strong>コンテキストを追加する</strong></div>
<br>

<div align="center"><a href="figNS21AddContextDialog.png"><img src="figNS21AddContextDialog.png" width="50%;"></a></div>
<div align="center"><strong>コンテキスト追加ダイアログ</strong></div>
<br>

「コンテキストを追加」ダイアログでは、コンテキストの名前(Name)、種類(Kind)を指定します。<br>
種類(Kind)には以下のいずれかの値を選択します。

<div align="center"><strong>コンテキストの種類(kind)の一覧</strong></div>
<table class="table-alt">
  <tr>
    <th>№</th>
    <th>種類（Kind）</th>
    <th>名前</th>
  </tr>
  <tr>
    <td>1</td>
    <td>host_cxt</td>
    <td>ホストコンテキスト</td>
  </tr>
  <tr>
    <td>2</td>
    <td>mgr_cxt</td>
    <td>マネージャコンテキスト</td>
  </tr>
  <tr>
    <td>3</td>
    <td>cate_cxt</td>
    <td>カテゴリコンテキスト</td>
  </tr>
  <tr>
    <td>4</td>
    <td>mod_cxt</td>
    <td>モジュールコンテキスト</td>
  </tr>
  <tr>
    <td>5</td>
    <td>上記以外を入力</td>
    <td>フォルダー（上記以外のコンテキスト）</td>
  </tr>
</table>


### ゾンビオブジェクトを削除する
ネームサービスビューには、ゾンビオブジェクトを一括して削除する機能があります。ゾンビオブジェクトをすべて削除するには、ネームサービスビュー上部の [Kill All Zombies] ボタンをクリックします。
<br>

<div align="center"><a href="figNS22KillAllZonbies.png"><img src="figNS22KillAllZonbies.png" width="50%;"></a></div>
<div align="center"><strong>ゾンビをクリア</strong></div>
<br>

