---
layout: page
title: 東京大学jsk講習会(2010年6月9日)
---

東京大学大学院 情報理工学系研究科 創造情報学特論IIとして、RTミドルウエアの講習会を行いました。
## 開催案内: 東京大学JSK講習会 

- **日時**: 2010年6月9日, 13:00~
- **場所**: 工学部2号館231号講義室(前半), 工学部2号館232講義室(2-301)/JSK研究室(後半)

- **プログラム**:
<table class="table-alt">
  <tr>
    <td>**13:00-14:30**</td>
    <td>**第1部：ロボットソフトウエアプラットフォーム**</td>
  </tr>
  <tr>
    <td></td>
    <td>担当：安藤慶昭 (産総研)</td>
  </tr>
  <tr>
    <td></td>
    <td>概要：様々なロボット用ソフトウエアプラットフォーム、および、RTミドルウエア概要、OMG標準化、OpenRTM-aist-1.0および、現在、NEDO次世代ロボット知能化技術開発プロジェクトで開発している共通プラットフォーム「OpenRTプラットフォーム」等について解説します。</td>
    <td></td>
  </tr>
  <tr>
    <td>**14:45-**</td>
    <td>**第2部：コンポーネント開発実習**</td>
  </tr>
  <tr>
    <td></td>
    <td>担当：安藤慶昭 (産総研)</td>
  </tr>
  <tr>
    <td></td>
    <td>概要：RTコンポーネントを作成するツールRTCBUilder、およびRTシステムを設計するツールRTSystemEditorの使い方について解説するとともに、実際にコンポーネント開発を体験していただきます。</td>
    <td></td>
  </tr>
</table>


## 資料
[ロボットミドルウエア標準：OpenRTM-aist](./100609-01.pdf)(no_link)

## 事前準備について
<span style="color:red;">現在、準備中です。内容は変更される場合があります。最終的な案内は、6月2日に掲示いたします。</span>;
### 用意するもの
第2部の実習には以下の準備が必要です。
- ノートPC
- USBカメラ
  - Windowsでも、Linuxでも構いませんが、USBカメラがOpenCVからつかえることが前提です。
  - あらかじめLANにつながるように設定しておいてください。

### ソフトウエアのインストール 
あらかじめ下記のソフトウエアをインストールしておいてください。
Windows推奨ですが、Linuxでも実習可能です。

- OpenRTM-aist-1.0.0-RELEASE
  - C++版
  - Python版
- Eclipseおよび、RTSystemEditor, RTCBUilder
- 開発環境
  - C++: WindowsではVisual C++ 2008 (Express版でもOK、2010は未対応)
  - Python: Python 2.6 推奨

詳細は、[ダウンロード]({{ site.baseurl }}/ja/download/)ページをご覧ください。

#### Windowsで必要なソフトウエア 
- C++版で必要なもの
  - [C++版, Win32 VC2008](http://www.openrtm.org/pub/Windows/OpenRTM-aist/cxx/OpenRTM-aist-1.0.0-RELEASE_vc9_100212.msi)
  - [Visual C++ Express](http://www.microsoft.com/japan/msdn/vstudio/2008/product/express/offline.aspx)
  - [OpenCV1.0](http://downloads.sourceforge.net/opencvlibrary/OpenCV_1.0.exe?modtime=1161287502&big_mirror=1)
  - [OpenCV2.1(VC2008用)](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.1/OpenCV-2.1.0-win32-vs2008.exe/download)
  - [PyYAML(rtc-templateで使用)](http://pyyaml.org/download/pyyaml/PyYAML-3.09.win32-py2.6.exe)

<span style="color:red;">OpenCV1.0とOpenCV2.1は共存可能です。OpenRTMに付属しているサンプルを動作させるのにOpenCV1.0が必要になります。実習では、OpenCV2.1ベースのコンポーネント群を使用します。</span>;

- Python版で必要なもの
  - [Python版, Win32](http://www.openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python-1.0.0.msi)
  - [Python2.6](http://www.python.org/ftp/python/2.6.2/python-2.6.2.msi)

- RTSystemEditor,RTCBilder
  - [Eclipse3.4.2+RTSE(1.0.0-RELEASE)+RTCB(1.0.0-RELEASE)Windows用全部入り]()（リンク切れです）

#### Linuxで必要なソフトウエア 
基本的に、[ダウンロード]({{ site.baseurl }}/ja/download/)ページを参照して、必要なソフトウエアをダウンロードしてください。
Ubuntu, Fedora などメジャーなディストリビューション用のパッケージが用意されています。
また、これ等の加えてOpenCV2.0をインストールしてください。
F
