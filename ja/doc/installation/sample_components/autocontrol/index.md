---
layout: page
title: "autocontrol"
---

<!-- Title: Autocontrol -->

#contents
このサンプルは、Python版にのみ付属しています。 
### 概要
InPortから入ったデータをある基準で判別してOutPortに別の形の出力をするコンポーネントです。SeqIn、SeqOutとともに使用できます。

各Port間を接続するとSeqOut側の出力値、SeqIn側の入力値がそれぞれのコンソール画面に表示されます。(Port間の接続にはRTSystemEditorを利用ください。)

### 起動画面

<div align="center"><a href="autocontrol_example_rtse.png"><img src="autocontrol_example_rtse.png" width="60%;"></a></div>
<div align="center"><strong>Autocontrol実行例(RTSystemEditor接続画面)</strong></div>

<div align="center"><a href="seqinout_console.png"><img src="seqinout_console.png" width="60%;"></a></div>
<div align="center"><strong>SeqInコンポーネントとSeqOutコンポーネントのコンソール画面</strong></div>

### 使い方
Autocontrolのサンプルは、Sensから入力したデータの4番目の要素をConfigurationで設定できるパラメータdistance_to_envと比較して、その値以下ならvelポートより(turn_vel, - turn_vel)をその値より大きければ(velocity, velocity)の出力をするコンポーネントです。

Autocntrol, SeqOutとSeqInの対応するポートをRTSystemEditor上で接続してください。両コンポーネントをアクティベートするとSeqOutだけでなくSeqInの出力される数値も連続的に変化し、データポートの入出力が観察できます。

- 手順

  1. RTSystemEditorを起動し、SystemEditorを用意します。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_2_0)を参照
  2. AutocontrolとSeqOut、SeqInコンポーネントを起動します。エクスプローラーでディレクトリ"\Program Files\OpenRTM-asit\1.2.x\Components\Python"より、”Autocontrol.bat"、”SeqIn.bat"、”SeqOut.bat"をダブルクリックしてください。
  3. RTSystemEditorのNameServiceViewに3つのコンポーネントが現れるので、それらをSystemEditor上にドラッグ＆ドロップします。
  4. 両コンポーネントの対応ポートを接続します。(上図実行例を参照)
  5. どちらかのコンポーネントを右クリックし、[Activate System]を選択します。
  6. [System Diagram]の中からAutocontrol0コンポーネントを選択し、画面下部にあらわれる[Configuration View]の[編集]ボタンをクリックします。[Configuration View]が表示されなければ、[Configuration View]タブが表示されているはずなので、それをクリックしてください。
  7. パラメータ値を変更します。このシステム構成例では、[velocity]を10.0、[turn_velocity]を1.0、[distance_to_env]を5.0に設定するのが分かりやすい設定値の例です。
  8. SeqOutのコンソール画面に表示されるfloatの4番目のデータ値と、SeqInのコンソール画面のSequence Dataの2つの値に注目してください。SeqOutの値が[distance_to_env]の値と比較され、SeqInのコンソール画面に[turn_vel]、- [turn_vel]か、[velocity]、[velocity]の値として出力されているのを確認してください。それぞれConfigurationパラメータを変化させて、入出力の関係がどのようになるかを見てみるのも良いでしょう。

