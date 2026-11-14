---
layout: page
title: "composite"
---

<!-- Title: Composite -->
#contents
このサンプルは、OpenRTM-aistのC++版、Python版、Java版に付属されています。 
### 概要 
複合コンポーネントCompositeの使用方法を示したサンプルです。
複合コンポーネントをActivateする前に、複合コンポーネントを構成している子のコンポーネント間を接続する必要があります。

- Compositeコンポーネントは、Sensor、Controller、Motorの３つのコンポーネントを子に持っています。
- Compositeコンポーネントの動作は、ConsoleIn/ConsoleOutコンポーネントと接続して確認できます。

### 起動画面
- Compositeコンポーネントを実行すると、Name Service Viewに４つのコンポーネント名が表示されます。
- Controller、Motor、Sensorの３つを複合化したコンポーネントがPeriodicECShareCompositeですので、これをSystem Editorにドラッグ＆ドロップします。

<div align="center"><a href="composite_001.jpg"><img src="composite_001.jpg" width="60%;"></a></div>
<div align="center"><strong>Composite実行例(複合コンポーネントをドラッグ＆ドロップ)</strong></div>
<br>

複合コンポーネント内を表示させるため、PeriodicECShareCompositeをダブルクリックすると、別のエディタに表示されますので、コンポーネント間を接続します。
<br>

<div align="center"><a href="composite_002.jpg"><img src="composite_002.jpg" width="60%;"></a></div>
<div align="center"><strong>Composite実行例(複合コンポーネントの子コンポーネント間を接続する)</strong></div>
<br>

ここではConsoleIn/ConsoleOutコンポーネントと接続した場合の動作例を示します。
<br>

<div align="center"><a href="composite_003.jpg"><img src="composite_003.jpg" width="60%;"></a></div>
<div align="center"><strong>Composite実行例(RTSystemEditor接続画面)</strong></div>
<br>

ConsoleInで「111」と入力した場合、ConsoleOutで「888」と表示されれば正しい動作です。
複合コンポーネントを構成している子コンポーネントは、入力値（コンソール画面に表示されている値）を2倍して出力しています。

<div align="center"><div align="center"><a href="composite_004.jpg"><img src="composite_004.jpg" width="50%;"></a></div>; <div align="center"><a href="composite_005.jpg"><img src="composite_005.jpg" width="50%;"></a></div>;</div>
<div align="center"><strong>Composite実行例(左：複合コンポーネント画面、右：ConsoleOut画面)</strong></div>

### 使い方
Compositeのサンプルは、入力データポートから受け取った値を、３つの子コンポーネントがそれぞれ2倍の値にして出力しているので、最終的にCompositeの出力データポートから8倍の値が出力されるサンプルです。

- 手順
  - RTSystemEditorを起動し、新規SystemEditorを開きます。RTSystemEditorの使用方法の詳細については[RTSystemEditor]({{ site.baseurl }}/ja/doc/toolmanuals/rtsystemeditor-1_2_0/)を参照
  - Compositeコンポーネントを起動します。コンポーネントの起動はOSやOpenRTM-aistの言語によって異なりますので、以下の表を参考に起動します。
<table class="table-alt">
  <tr>
    <th></th>
    <th>Windowsの場合</th>
    <th>Linuxの場合</th>
  </tr>
  <tr>
    <td>C++版</td>
    <td>Composite.bat</td>
    <td>Composite</td>
  </tr>
  <tr>
    <td>Python版</td>
    <td>Composite.bat</td>
    <td>Composite.py</td>
  </tr>
  <tr>
    <td>Java版</td>
    <td>Composite.bat</td>
    <td>Composite.sh</td>
  </tr>
</table>
  - RTSystemEditorのName Service ViewにPeriodicECShareCompositeが現れるので、それらをSystemEditor上にドラッグします。
  - PeriodicECShareCompositeをダブルクリックし、子コンポーネント間のポートを結びます
  - ConsoleInとConsoleOutの両コンポーネントを起動し、PeriodicECShareCompositeと対応ポートを接続します。(上図Composite実行例を参照)
  - どちらかのコンポーネントを右クリックし、[Activate Systems]を選択します。

