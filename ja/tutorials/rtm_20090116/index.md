---
layout: page
title: 石川県産業大学講座・技術セミナー(2009年1月16日)
---

#contents


## 参加人数
7名

## 資料
- [第1部：RTミドルウエアの現状と今後の展開について(1)(PDF)](./090116-01.pdf)(no_link)
- [第2部：RTミドルウエアの現状と今後の展開について(2)(PDF)](./090116-02.pdf)(no_link)
- [第3部：コンポーネント開発実習)(PDF)](./090116-03.pdf)(no_link)

## 開催案内 **石川県産業大学講座・技術セミナー(2009年1月16日)** 
Windows版OpenRTM-aist-0.4.2を対象とした講習会を1月16日、(財)石川県産業創出支援機構主催、[石川県産業大学講座・技術セミナー](http://www.irii.jp/kenshu/sandai.html#schedule)にてさせていただきました。

- [**(財)石川県産業創出支援機構のセミナー案内ページ**](http://dgnet.isico.or.jp/etc/view.phtml?uk=00031233)
- [**石川県工業試験場の案内ページ**](http://www.irii.jp/kenshu/sandai.html#schedule)
- [セミナー開催案内(FAX申込用紙)]()（リンク切れです）

<br>

今回の講習会ではWindows版OpenRTM-aist(C++/Python)を対象としたコンポーネント作成の実習を行う予定ですので、OpenRTM-aistを予めご自分のノートPC上の[[Windowsへインストール>インストール(C++, Windows)]]した上でご参加くださいますようお願いいたします。

- **日時**: 2009年1月16日, 10:00`16:00`
- **場所**: [石川県工業試験場 トライアルセンター５階第２研修室](http://www.irii.go.jp/traf/traf.htm)
- **石川県工業試験場へのアクセス**:[マップ](http://www.irii.go.jp/traf/traf.htm)
- **定員**： 約20名（ノートPCによる実習)
- **聴講料**：1,000円
- **申込方法**：(財)石川県産業創出支援機構・産業振興部・人材支援課
  - e-mail: seminar@irii.go.jp
  - TEL: (076)267-8081
  - FAX: (076)267-8090
  - [セミナー開催案内(FAX申込用紙)]()（リンク切れです）

- **プログラム**:
<table class="table-alt">
  <tr>
    <td>**10:00-10:45**</td>
    <td>**第1部：RTミドルウエアの現状と今後の展開について(1)**</td>
  </tr>
  <tr>
    <td></td>
    <td>担当：神徳徹雄 (産総研)</td>
  </tr>
  <tr>
    <td></td>
    <td>概要：RTミドルウエアプロジェクト概要、OMG標準化、RSi連携、NEDO知能化PJ等について解説します。</td>
    <td></td>
  </tr>
  <tr>
    <td>**11:00-12:00**</td>
    <td>**第2部：RTミドルウエアの現状と今後の展開について(2)**</td>
  </tr>
  <tr>
    <td></td>
    <td>担当：安藤慶昭 (産総研)</td>
  </tr>
  <tr>
    <td></td>
    <td>概要：コンポーネント指向ロボット開発の基本的な考え方，OMG RTC標準、OpenRTM-aist、開発の実際について解説します。</td>
  </tr>
  <tr>
    <td>**13:00-16:00**</td>
    <td>**第3部：コンポーネント開発実習**</td>
  </tr>
  <tr>
    <td></td>
    <td>担当：安藤慶昭 (産総研)</td>
  </tr>
  <tr>
    <td></td>
    <td>概要：OpenRTM-aistでのコンポーネント作成方法を実際に体験していただきます。</td>
    <td></td>
  </tr>
</table>


## 事前準備 
実習形式の講習会ですので、以下のものを事前にご準備いただきますようお願いいたします。

- LANケーブル(1本、2～3m程度の物)
  - こちらで用意するHUBから自分のPCへ繋ぐ為:2～3m, 1本
  - LANは基本的に有線接続でお願いします。
- テーブルタップ(1本、2～3m程度の物)
  - こちらで用意するタップから自分のPCに配電する為

- ノートPC (WindowsXPがインストールされている物)
  - Windows Vista はこちらで動作確認ができて居りませんので推奨しません。
  - バッテリは十分充電して置いてください。
  - IPアドレスはDHCPで配りますのでDHCPを有効にしておいてください。
  - 実習時はファイヤーウォール(Windowsのものや、セキュリティソフトのモノ等)を切った状態でご参加
  - 以下のソフトウエアを事前にインストールした状態でご参加ください。

## インストールするソフトウエア
- プログラミング言語Pythonのインタプリタ(exeを実行してインストール)
  - [Python2.5](http://www.python.org/ftp/python/2.5.1/python-2.5.1.msi)
- RTミドルウエアのPython版(msiを実行してインストール)
  - [OpenRTM-aist-Python](http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python2.5-0.4.1-RELEASE.msi)
- RTミドルウエアに必要なライブラリ(exeを実行してインストール)
  - [omniORBpy](http://www.openrtm.org/pub/Windows/omniORB/omniORBpy-3.1.msi)
- PythonからBluetoothを使うために必要なモジュール(exeを実行してインストール)
  - [pyBlues](http://pybluez.googlecode.com/files/PyBluez-0.15.win32-py2.5.exe)
- PythonからLEGO Mindstorm NXTを使うために必要なモジュール(下の指示に従ってインストール)
  - [nxtpython]()（リンク切れです）
 zipを展開後、展開したフォルダの中(setup.pyがあるフォルダ)でコマンドプロンプトから
```
 > c:\python25\python setup.py install
```
 と入力
- USB汎用ドライバ、NXTをUSB経由で使うために必要(exeを実行してインストール)
  - [libusb]()（リンク切れです）
- PythonからUSBを使うために必要なモジュール(exeを実行してインストール)
  - [pyusb]()（リンク切れです）
- RtcLink、RTミドルウエアを使うためのツール(zipを展開して出てきたフォルダのeclipse.exeを実行して起動)
  - [eclipse]()（リンク切れです）
- RTミドルウエアのC++版(exeを実行してインストール)
  - [OpenRTM-aist-C++]()（リンク切れです）
- RTミドルウエアC++版を使うために必要なライブラリ(exeを実行してインストール)
  - [omniORB](http://www.openrtm.org/pub/Windows/omniORB/omniORB-4.1.2_vc9.msi)
- RTミドルウエアC++版を使うために必要なライブラリ(exeを実行してインストール)
  - [ACE](http://www.openrtm.org/pub/Windows/ace/ACE-5.6_vc9.msi)
- RTミドルウエアC++版を使うために必要なライブラリ(Microsoftのサイトに飛ぶのでダウンロードボタンを押してインストール)
  - [VC2008DLL](http://www.microsoft.com/downloads/details.aspx?displaylang=ja&FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf)

- 講習会用サンプル(USBドライバも入っています。)
  - [講習会用サンプル]()（リンク切れです）
  - NXTをUSBで接続したら、デバイスドライバのインストールウィザードが表示されるので、「接続しない」を選んで「特定の場所からインストールするを選び」フォルダの参照ボタンを押してUSBDriverフォルダを選択して「次へ」を押すとインストールできます。

# 講習会の様子
<div align="center"><a href="090116-01.jpg"><img src="090116-01.jpg" width="60%;"></a></div>
<br>

<div align="center"><a href="090116-02.jpg"><img src="090116-02.jpg" width="60%;"></a></div>
<br>

<div align="center"><a href="090116-03.jpg"><img src="090116-03.jpg" width="60%;"></a></div>
<br>

