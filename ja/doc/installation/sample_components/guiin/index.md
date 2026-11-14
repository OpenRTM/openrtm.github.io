---
layout: page
title: "guiin"
---

<!-- Title: GUIIn -->
#contents
このサンプルは、OpenRTM-aistのJava版のみに付属しています。C++版、Python版に付属していませんので注意ください。

### 概要・起動画面
GUI画面を持ったRTコンポーネントのサンプルです。Windowsの場合はGUIIn.bat、Linuxの場合はGUIIn.shを実行することでサンプル・コンポーネントが起動します。

<div align="center"><a href="GUIIn_example.png"><img src="GUIIn_example.png" width="40%;"></a></div>
<div align="center"><strong>GUIIn実行例(GUIIn)</strong></div>

<div align="center"><a href="GUIIn_example_rtse_ja.png"><img src="GUIIn_example_rtse_ja.png" width="60%;"></a></div>
<div align="center"><strong>GUIIn実行例(RTSystemEditor接続画面)</strong></div>

各GUI要素とPort間の関係は以下のとおりです。
- スライダ(上): TimedLong型OutPort
- テキスト・ボックス(中): TimedString型OutPort
- スピナ(下): TimedDouble型OutPort

各Portは該当するPort間を接続後、GUI要素横のチェックボックスをONにすることで、入力データを送信します。（Port間の接続にはRTSystemEditorをご利用ください。出力データの確認にはSeqInなどの他サンプルをご利用ください。）

### 使い方
GUIInコンポーネントのGUI画面でチェックを入れたコントロール(スライダー、スピナ)を操作すると、その値の変化にしたがってSeqInのコンソール画面上の値も変化します。

- 手順
  - RTSystemEditorを起動し、新規のSystemEditorを開きます。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_2_0)を参照
  - GUIInとSeqInの両コンポーネントを起動します。コンポーネントの起動はOSによって異なります。Windowsの場合はGUIIn.bat、Linuxの場合はGUIIn.shを起動します。
  - RTSystemEditorのName Service Viewにこれらのコンポーネントが現れるので、二つともSystem Editor上にドラッグします。
  - 両コンポーネントの対応ポートを結びます。(上図GUIIn実行例を参照)
  - どちらかのコンポーネントを右クリックし、[Activate Systems]を選択します。



