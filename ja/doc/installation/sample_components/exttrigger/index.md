---
layout: page
title: "exttrigger"
---
<!-- Title: ExtTrigger -->

### 概要
外部からの入力(イベント)により処理が実行されるExecutionContextのサンプルです。
- ExtConsoleIn.batとExtConsoleOut.batを実行し、2つのサンプル・コンポーネントを起動します。
- 両コンポーネントを起動後、ExtConnector.batを実行し、2つのコンポーネントのPort間を接続します。

### 起動画面

<div align="center"><a href="java_exttrigsample0.png"><img src="java_exttrigsample0.png" width="80%;"></a></div>
<div align="center"><strong>ExtTrigger実行例(ExtConsoleIn)</strong></div>

<div align="center"><a href="java_exttrigsample1.png"><img src="java_exttrigsample1.png" width="80%;"></a></div>
<div align="center"><strong>ExtTrigger実行例(ExtConsoleOut)</strong></div>

<div align="center"><a href="java_exttrigsample2.png"><img src="java_exttrigsample2.png" width="80%;"></a></div>
<div align="center"><strong>ExtTrigger実行例(ExtConnector)</strong></div>

Port間の接続が成功すると、ExtConnectorを実行したコンソールにどのコンポーネントの処理を進めるか選択するメニューが表示されます。
この入力値により、それぞれのコンポーネントは処理を１周期づつ進めていきます。

