---
layout: page
title: "simpleio"
---
<!-- Title: SimpleIO -->

#contents
このサンプルは、OpenRTM-aistのC++版、Python版、Java版に付属されています。

### 概要
InPort、OutPortの使用方法のサンプルです．ConsoleInコンポーネントとConsoleOutコンポーネントを起動させます。
Port間を接続すると、ConsoleIn側で入力した数字が、ConsoleOut側に表示されます．Port間はRTSystemEditorを用いる以外にrtshellコマンドを実行することで接続できます。

### 起動画面

<div align="center"><a href="SimpleIO_example_rtse_ja.png"><img src="SimpleIO_example_rtse_ja.png" width="60%;"></a></div>
<div align="center"><strong>SimpleIO実行例(RTSystemEditor接続画面)</strong></div>

<div align="center"><a href="open_consolein_out.png"><img src="open_consolein_out.png" width="60%;"></a></div>
<div align="center"><strong>ConsoleInコンポーネントとConsoleOutコンポーネントの実行例</strong></div>
### 使い方
SimpleIOのサンプルは、ConsoleInで入力された数字をデータポートからConsoleOutへ送って、ConsoleOut側にも同じ数字を表示させるサンプルです。
ConsoleInの画面から数字を入力してください。そうするとConsoleOutで入力した数字が出力されます。


  - OpenRTPを起動し、RTSystemEditorを開きます。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_2_0)を参照
  - ConsoleInとConsoleOutの両コンポーネントを起動します。
コンポーネントの起動はOSやOpenRTM-aistの言語によって異なってます。以下の表を参考に起動します。
<table class="table-alt">
  <tr>
    <th></th>
    <th colspan="2">Windowsの場合</th>
    <th colspan="2">Linuxの場合</th>
  </tr>
  <tr>
    <td></td>
    <td>ConsoleInコンポーネント</td>
    <td>ConsoleOutコンポーネント</td>
    <td>ConsoleInコンポーネント</td>
    <td>ConsoleOutコンポーネント</td>
  </tr>
  <tr>
    <td>C++版</td>
    <td>ConsoleIn.bat</td>
    <td>ConsoleOut.bat</td>
    <td>ConsoleInComp</td>
    <td>ConsoleOutComp</td>
  </tr>
  <tr>
    <td>Python版</td>
    <td>ConsoleIn.bat</td>
    <td>ConsoleOut.bat</td>
    <td>ConsoleIn.py</td>
    <td>ConsoleOut.py</td>
  </tr>
  <tr>
    <td>Java版</td>
    <td>ConsoleIn.bat</td>
    <td>ConsoleOut.bat</td>
    <td>ConsoleIn.sh</td>
    <td>ConsoleOut.sh</td>
  </tr>
</table>
  - RTSystemEditorのName Service Viewに両コンポーネントが現れるので、それらをSystemEditor上にドラッグします。
  - 両コンポーネントのポートを結びます。（上図SimpleIO実行例を参照）
  - どちらかのコンポーネントを右クリックし、[Activate Systems]を選択します。
  - ConsoleInの画面に「Please input number:」のプロンプトが現れるので、数字を入力します。
  - ConsoleOutの画面にその数字が表示されます。



