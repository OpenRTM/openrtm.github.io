---
layout: page
title: オフラインシステムエディタ
---
<!-- Title: オフラインシステムエディタ -->
#contents
<!-- オフラインシステムエディタ -->


### 概要
ここでは、オフラインシステムエディタの概要について説明します。
<br>

<div align="center"><a href="fig86OfflineSysetmEditor.png"><img src="fig86OfflineSysetmEditor.png" width="70%;"></a></div>
<div align="center"><strong>オフラインシステムエディタの位置</strong></div>
<br>

オフラインシステムエディタでは、レポジトリビュー上のコンポーネントをドラッグ＆ドロップでダイアグラムに追加することで、RTシステムの編集を行います。基本的な操作はオンラインのシステムエディタと同じですが、RTC の状態を変更することはできません。また、リアルタイムに RTC の状態が変更される、または更新されることもありません。
<br>


### 基本機能

#### オフラインシステムエディタを開く
新しいオフラインシステムエディタを開くには、ツールバーの「Open New Offline System Editor」ボタンをクリックするか、メニューバーの [File] > [Open New Offline System Editor] を選択します。
<br>


<div align="center"><a href="fig87OpenNewOfflineSystemEditorFromToolbar.png"><img src="fig87OpenNewOfflineSystemEditorFromToolbar.png" width="60%;"></a></div>
<div align="center"><strong>ツールバーから Open New Offline System Editor</strong></div>
<br>

<div align="center"><a href="fig88FileOpenNewOfflineEditor.png"><img src="fig88FileOpenNewOfflineEditor.png" width="50%;"></a></div>
<div align="center"><strong>Fileメニューから Open New Offline System Editor</strong></div>
<br>


#### コンポーネント仕様をオフラインシステムエディタに配置する
コンポーネント仕様をオフラインシステムエディタに配置するには、リポジトリビューからコンポーネント仕様をドラッグ＆ドロップします。
<br>

<div align="center"><a href="fig89OfflineEditorComponentDnD.png"><img src="fig89OfflineEditorComponentDnD.png" width="70%;"></a></div>
<div align="center"><strong>コンポーネント仕様をオフラインシステムエディタに配置する</strong></div>
<br>

リポジトリビュー上で Ctrlキーを押しながらクリックし、複数コンポーネント仕様を選択すれば、まとめてオフラインシステムエディタ上へ配置することができます。
<br>

<div align="center"><a href="fig90OfflineEditorComponentMultiDnD.png"><img src="fig90OfflineEditorComponentMultiDnD.png" width="70%;"></a></div>
<div align="center"><strong>複数のコンポーネント仕様をまとめてオフラインシステムエディタに配置する</strong></div>
<br>


#### コンポーネント仕様をオフラインシステムエディタで編集する
オフラインシステムエディタでは、システムエディタで行えることのうち、実行時コンポーネントの動作に関すること以外のほとんどの操作を、システムエディタと同様の操作で行うことができます。
<br>


### デプロイ機能

ここでは、オフラインシステムエディタを使用したデプロイ機能の概要について説明します。
<br>

デプロイ機能を用いることで、オフラインシステムエディタで作成したオフラインプロファイルから実際のシステム構築を行うことが可能となります。

#### デプロイ情報の設定
オフラインエディタ上に配置したコンポーネントを右クリックし、表示されたメニュー中から｢Set Deploy Info.｣を選択すると、デプロイ情報設定画面が表示されます。
<br>

<div align="center"><a href="fig91DeploySetting.png"><img src="fig91DeploySetting.png" width="60%;"></a></div>
<div align="center"><strong>デプロイ情報の設定</strong></div>
<br>

<table class="table-alt">
  <tr>
    <td><div align="center"><a href="fig92DeployComp.png"><img src="fig92DeployComp.png" width="60%;"></a></div></td>
    <td><div align="center"><a href="fig92DeployManager.png"><img src="fig92DeployManager.png" width="60%;"></a></div></td>
  </tr>
  <tr>
    <td style="text-align: center;"><strong>稼働中のRTC</strong></td>
    <td style="text-align: center;"><strong>稼働中のManager</strong></td>
  </tr>
</table>

<div align="center"><strong>デプロイ情報設定画面</strong></div>
<br>

デプロイ情報設定画面では、現在稼働中の RTC、Manager の一覧が表示されます。対象 RTC をデプロイする際に使用する要素を選択してください。
<br>

※デプロイ情報設定画面の内容は、NameServiceView に表示されている項目を使用しています。稼働している要素の情報が表示されない場合は、NameServiceView の表示内容を確認し、必要に応じて Refresh を行ってください。
<br>

※複合 RTC を選択した場合、Manager 情報一覧のみが表示されます。デプロイ時に使用する Manager を選択してください。
<br>


#### デプロイ情報の保存・読み込み
設定したデプロイ情報は、RtsProfile とは別に保存、読込する事が可能です。オフラインエディタを右クリックして表示されるメニュー中から「Save Deploy Info.」｢Load Deploy Info.｣をそれぞれ選択してください。
<br>

<div align="center"><a href="fig93DeploySave.png"><img src="fig93DeploySave.png" width="80%;"></a></div>
<div align="center"><strong>デプロイ情報の保存・読み込み</strong></div>
<br>

※デプロイ情報を読み込む際には、コンポーネントID(ベンダ名、カテゴリ名、コンポーネント名、バージョン番号)をキーとして、該当 RTC の検索を行います。
<br>


#### デプロイの実行
設定したデプロイ情報を基に、実際のシステムを構築(デプロイ)する場合は、オフラインエディタを右クリックして表示されるメニュー内から｢Deploy System｣を選択します。
<br>

<div align="center"><a href="fig94Deploy.png"><img src="fig94Deploy.png" width="80%;"></a></div>
<div align="center"><strong>デプロイ</strong></div>
<br>

デプロイを実行すると、設定されたデプロイ情報を基に実システムの構築(デプロイ)を行います。そして、新規オンラインエディタを開き、デプロイ結果を表示します。
<br>

対象となるオフラインシステム内に、デプロイ情報が設定されていないコンポーネントが存在する場合や、設定したデプロイターゲットがデプロイ時に起動していない場合には、以下のような警告画面が表示されます。
<br>

<div align="center"><a href="fig95DeployWarning.png"><img src="fig95DeployWarning.png" width="70%;"></a></div>
<div align="center"><strong>デプロイ時警告画面</strong></div>
<br>

警告画面中で｢キャンセル｣を選択した場合は、デプロイ処理を中断します。[OK] を選択した場合は、起動中のデプロイターゲットを使用して、可能な限りシステムの構築(デプロイ)を実行します。


