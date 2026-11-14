---
layout: page
title: "openrtm-aist 諸元"
---
<!-- Title: OpenRTM-aist 諸元 -->
#contents

OpenRTM-aistは、RTコンポーネントフレームワーク、RTミドルウエア、基本RTコンポーネント群、ライブラリ、基本サービス群、基本ツール群等から構成されています。
RTコンポーネントフレームワークは、RTコンポーネントを作るための基本クラスであり、すべてのRTコンポーネントはこの基本クラスのサブクラスとして作成されます。
RTミドルウエアは、フレームワークに基づいて作成されたRTコンポーネントのモジュールのロードや、インスタンスの生成・解体等のライフサイクルの管理、コンポーネントのネームサービスへの登録等を行う部分です。
これらの中には、ユーザーの利便性を向上させるライブラリ、RTコンポーネントの登録検索等の基本的サービス(現在はCORBAのNaming Serviceを利用)、RTコンポーネントの雛型コードを生成するRTCBuilder、RTコンポーネントの接続・制御等を行うRTSystemEditor等のツール群が含まれています。

現在のところ、OpenRTM-aistは C++、Python、Javaの各言語をサポートしており、Windows、UNIX系OS、μITRON(C++のみ対応)系の各OS上で動作可能です。
さらに、株式会社セックがOpenRTM-aist互換のミドルウエア:OpenRTM .NETを公開しており、C#を始めとする.NET環境でRTCを作成・実行することができます。
異なる言語で作成したRTCや異なるOS上で動作するRTCを相互に接続し連携させることが可能です。

## インターフェース仕様

- OMG Robotic Technology Component Specification 1.0準拠
  - [OMG仕様書 formal/12-09-01](https://www.omg.org/spec/RTC/1.1/)
- OMG Super Distributed Object Specification 1.1準拠
  - [OMG仕様書 formal/08-10-01](http://www.omg.org/spec/SDO/1.1/)

### 参考

- [OMG (Object Management Group)](http://www.omg.org)
- [OMG Specifications](http://www.omg.org/technology/documents/spec_catalog.htm)

## 構成

OpenRTM-aist は以下の各言語版のミドルウエアライブラリおよびツール群から構成されています。

<div align="center"><strong>OpenRTM-aistの構成</strong></div>

<table class="table-alt">
  <tr>
    <td>名前</td>
    <td>概要</td>
  </tr>
  <tr>
    <td>OpenRTM-aist (C++版)</td>
    <td>C++言語でRTコンポーネントを作成するためのコンポーネントフレームワークとミドルウエアライブラリおよびコマンド群</td>
  </tr>
  <tr>
    <td>OpenRTM-aist (Python版)</td>
    <td>Python言語でRTコンポーネントを作成するためのコンポーネントフレームワークとミドルウエアライブラリおよびコマンド群</td>
  </tr>
  <tr>
    <td>OpenRTM-aist (Java版)</td>
    <td>Java言語でRTコンポーネントを作成するためのコンポーネントフレームワークとミドルウエアライブラリおよびコマンド群</td>
  </tr>
  <tr>
    <td>RTCBuilder</td>
    <td>RTコンポーネントの設計、コード生成を行うためのEclipseプラグイン</td>
  </tr>
  <tr>
    <td>RTSystemEditor</td>
    <td>RTコンポーネントの操作およびRTシステムの設計・操作を行うためのEclipseプラグイン</td>
  </tr>
  <tr>
    <td>rtshell</td>
    <td>RTコンポーネント、RTシステムの操作をCUIから行うためのコマンド群</td>
  </tr>
</table>


これらの配布物はそれぞれEPLと個別契約のデュアルライセンスの元配布されています。


## 動作条件

### OpenRTM-aist (C++版)

<table class="table-alt">
  <tr>
    <td>コンパイラ</td>
    <td>gcc 3.x 以上、Visual C++ 2008、2010、2012、2013、2015、2017、2019</td>
  </tr>
  <tr>
    <td>OS</td>
    <td>Linux、FreeBSD、Windows、Mac OS X、TOPPERS ASP</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>i386、x86_64、ppc、arm</td>
  </tr>
  <tr>
    <td>依存ライブラリ</td>
    <td>omniORB 4.0以上、libuuid (Linux)</td>
  </tr>
</table>

### OpenRTM-aist (Python版)

<table class="table-alt">
  <tr>
    <td>Python</td>
    <td>Python 2.7、Python3.6、Python 3.7</td>
  </tr>
  <tr>
    <td>依存ライブラリ</td>
    <td>omniORBpy-2.3以上</td>
  </tr>
</table>


### OpenRTM-aist (Java版)

<table class="table-alt">
  <tr>
    <td>Java</td>
    <td>JDK5 以上</td>
  </tr>
  <tr>
    <td>依存ライブラリ</td>
    <td>JDK に含まれる Java IDL</td>
  </tr>
</table>

### RTCBuilder/RTSystemEditor

<table class="table-alt">
  <tr>
    <td>Eclipse</td>
    <td>3.4 以上</td>
  </tr>
  <tr>
    <td>Java</td>
    <td>JDK6 以上</td>
  </tr>
  <tr>
    <td>依存ライブラリ</td>
    <td>Eclipse EMF 2.2以上(SDO,XSD含む)、<br> Eclipse GEF 3.2以上(Draw2D含む)</td>
  </tr>
</table>

### rtshell

<table class="table-alt">
  <tr>
    <td>Python</td>
    <td>Python 2.7、Python3.6、Python 3.7</td>
  </tr>
  <tr>
    <td>依存ライブラリ</td>
    <td>omniORBpy-2.3以上</td>
  </tr>
</table>


