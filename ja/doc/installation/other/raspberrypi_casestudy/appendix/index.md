---
layout: page
title: 付録
---

<!-- Title: 付録 -->
#contents

## Raspberry Pi へのファイルコピー

Raspberry Pi の設定画面(Raspi-config)にて SSH を有効に設定することで、sFTP が利用できるようになります｡ Windows から sFTP で Raspberry Pi に接続する場合には sFTP に対応したソフト(WinSCP など)を使用します｡

[こちら](http://winscp.net/eng/docs/lang:jp)から WinSCP のダウンロードページに移動することができます。


<div align="center"><a href="4_app1.png"><img src="4_app1.png" width="60%;"></a></div>
<div align="center"><a href="4_app2.png"><img src="4_app2.png" width="60%;"></a></div>
<div align="center"><strong>図4-1 sFTP 接続</strong></div>


## VNC(Virtual Network Computing)の利用

Raspbian のGUI 環境を開発用PC上で操作するために、VNCサーバーをインストールします｡

[こちら](http://www.vector.co.jp/soft/win95/net/se324464.html) から VNC をダウンロードすることができます。

<nowiki><blockcode>
$ su
# apt-get install tightvncserver
</blockcode></nowiki>

インストール途中で、VNCサーバーに接続する際のパスワード入力を求められますので、適当なパスワードを設定します｡
VNCサーバーをインストール後、開発用PC からターミナルを使用して Raspberry Pi に SSH 接続し、VNCサーバーを起動します｡

<nowiki><blockcode>
$ vncserver :1 -geometry 1024x600 -depth 16 -pixelformat rgb565
</blockcode></nowiki>

<div align="center"><a href="4_app3.png"><img src="4_app3.png" width="60%;"></a></div>
<div align="center"><strong>図4-2 VNCサーバーの起動</strong></div>

Windows から VNCサーバーに接続する場合には、VNCクライアントソフト(RealVNC など)を使用します｡

<div align="center"><a href="4_app4.png"><img src="4_app4.png" width="60%;"></a></div>
<div align="center"><strong>図4-3 VNC 接続</strong></div>


