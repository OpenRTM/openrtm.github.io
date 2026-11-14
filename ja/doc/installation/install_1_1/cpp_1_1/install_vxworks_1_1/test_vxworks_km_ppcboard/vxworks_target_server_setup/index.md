---
layout: page
title: vxworksターゲットサーバ－接続の生成手順
---

<!-- Title: VxWorksターゲットサーバ－接続の生成手順 -->
#contents

このページではWind River WorkbenchとVxWorksとを接続するコネクションの生成手順を説明します。

## ターゲットサーバの追加

Define a connection to remote systemボタンを押してシミュレータを追加してください。

<br>

<div align="center"><a href="sim1.png"><img src="sim1.png" width="60%;" align="center"></a></div>

<br>


New ConnectionウインドウのSelect Remote System Typeで""Wind River VxWorks 6.x Target Server Connection""を選択して次へ進んでください。


<br>

<div align="center"><a href="target4.png"><img src="target4.png" width="60%;" align="center"></a></div>

<br>


Target Server Optionsでは以下の設定を行ってください。

<table class="table-alt">
  <tr>
    <th>Backend</th>
    <th>wdbrpc</th>
  </tr>
  <tr>
    <td>Target name or address</td>
    <td>IPアドレス(例：172.30.1.10)</td>
  </tr>
  <tr>
    <td>Kernel Image</td>
    <td>Fileを選択する。ファイルパスにはVxWorksイメージファイルを指定する。</td>
  </tr>
</table>


<br>

<div align="center"><a href="target3.png"><img src="target3.png" width="60%;" align="center"></a></div>

<br>

Finishボタンをクリックするとターゲットサーバーとの接続を生成します。


