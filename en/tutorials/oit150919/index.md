---
layout: page
title: 大阪工業大学rtミドルウェア講習会（９月１９日）
---
<br>
<a>No English version available.
</a>

<!-- -------jp page!!------- -->

<div align="center"><img src="oit_logo.png" width="50%;" align="center"></div>

#contents

## 大阪工業大学RTミドルウェア講習会

2015年9月19日(土)に大阪工業大学大宮キャンパスにおいて，RTミドルウェア講習会を開催いたしました．

<!-- 2015年9月19日(土)に大阪工業大学大宮キャンパスにおいて，RTミドルウェア講習会を開催します。&br; -->
<!-- 受講者には各自ノートPCをお持ちいただき、実習形式で実際にRTコンポーネントを作成、既存のコンポーネントなどと組み合わせて簡単なシステムを構築していただきます。&br; -->
<!-- 本講習会を受講することで、RTコンポーネント設計方法、実装の仕方、システムの作り方をマスターすることができます。&br; -->

## 日時・場所
- **日時**: 2015年9月19日(土), 10:00～15:00
- **場所**: [大阪工業大学　大宮キャンパス](http://www.oit.ac.jp/japanese/oit/access_omiya.html)、6号館13階情報演習室
- **主催**: 国立研究開発法人新エネルギー・産業技術総合開発機構、国立研究開発法人産業技術総合研究所
<!-- -''受講料'': 無料  -->
<!-- -''定員'': 20名程度を予定しております。定員になり次第申し込みは終了させていただきます。 -->
- **参加者**: 24名（+講師・スタッフ4名）
<!-- -''参加登録'': [[参加登録フォームはこちら>#entry]] -->
<!-- -- 参加登録には当Webページのユーザ登録が必要です。[[ユーザ登録はこちら:http://openrtm.org/openrtm/ja/user/register]] -->
<!-- -- [[メーリングリスト:http://www.openrtm.org/mailman/listinfo/openrtm-users]]への登録をお勧めします。必須ではありませんが、Webでご案内する事前準備についてはメーリングリストにてお知らせします。 -->
<!-- -- なお、登録の際に問題が生じた場合は、 [[こちら（support@openrtm.org）:mailto:support@openrtm.org]] までお問い合わせください。 -->

## プログラム

<table class="table-alt">
  <tr>
    <td>10:00 -11:00</td>
    <td>**第1部：RTミドルウエア: OpenRTM-aist概要** <br> **担当**：安藤慶昭(産総研)<br> **概要**：RTミドルウエアはロボットシステムをコンポーネント指向で構築するソフトウエアプラットフォームです。RTミドルウエアを利用することで、既存のコンポーネントを再利用し、モジュール指向の柔軟なロボットシステムを構築することができます。RTミドルウエアの産総研による実装であるOpenRTM-aistについてその概要について説明します。<br>**講義資料**: <div align="center"><a href="150919-01.pdf"><img src="150919-01.pdf" width="60%;"></a></div>;</td>
  </tr>
  <tr>
    <td>11:00 -12:30</td>
    <td>**第2部: RTコンポーネントの作成入門**<br> **担当**：安藤慶昭・原功(産総研)<br> **概要**：RTCBuilderを使用したRTコンポーネントの作成方法を説明します。 <br> <a href="{{ site.baseurl }}/en/doc/casestudy/opencv_comp_development/opencv_winxp_rtmtools_vc2010">チュートリアル（画像処理コンポーネントの作成 Windows編）</a> <br> <a href="{{ site.baseurl }}/en/doc/casestudy/opencv_comp_development/opencv_ubuntu_1404">チュートリアル（画像処理コンポーネントの作成 Linux編）</a></td>
  </tr>
  <tr>
    <td>13:30 -15:00</td>
    <td>**第3部：プログラミング実習** <br> 担当：安藤慶昭・原功(産総研) <br> **概要**：OpenRTM-aistを利用してコンポーネントを作成し、他のコンポーネントと組み合わせて動作させてみます。 <br></td>
  </tr>
</table>


### 必要機材
- ノートPC
  - OS: Windowsを推奨します。応用コースの方は自分で対処出来る場合はどちらでも結構です
  - Eclipseが動作する程度のスペックが必要です
  - メモリ: 1GB以上
  - CPU: Core2Duo以上
  - HDD空き: 5GB以上 (Visual C++ Expressの場合)
- USBカメラ (USBカメラ無しで申込まれた方には貸与いたします)

<span style="color:red;">Windowsのファイアウォールは必ず切っておいてください。</span>;

### 必要ソフトウエア

あらかじめインストールしておくべきソフトウエアは以下のとおりです。以下のリンクをクリックし、ファイルをダウンロード・インストールしてください。(一部のリンクはダウンロードページへ飛びますので、飛んだ先のページ内で適切なファイルをそれぞれダウンロードしてください。

- Visual Studio
  - [こちらのページ](https://www.visualstudio.com/ja-jp/downloads/download-visual-studio-vs#DownloadFamilies_2) からVisual Studio 2013をクリックすると、無償版の「Visual Studio Community 2013 with Update 5」 をダウンロードできます。   
  - インストールには時間がかかりますので、事前にインストールしておいてください。
  - すでに他のバージョン（2008, 2010, 2012, 2013(Express)）がインストールされている場合は、それをお使い下さい。
- OpenRTM-aist C++ 1.1.1-RELEASE版
  - <span style="color:red;">インストールされているVisual Studioに一致するバージョンをダウンロードしてください。</span>;
  - 上記Visual C++ 2013用のインストーラは[こちら](http://openrtm.org/pub/Windows/OpenRTM-aist/cxx/1.1/OpenRTM-aist-1.1.1-RELEASE_x86_vc12.msi)
  - 他のバージョン用は、[こちらのページ]({{ site.baseurl }}/en/download/openrtm-aist-cpp/openrtm-aist-cpp_1_1_1_release) からダウンロードできます。
  - インストーラは、デフォルトでOpenRTPとJREを一緒にインストールします。デフォルト設定のままインストールして下さい。
  - [OpenRTM-aistを10分で始めよう！]()(No corresponding page available.) を参考に、事前にサンプルコンポーネントを起動して動作確認を行っておいてください。
- [Python2.7(32bit)](https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi)
  - <span style="color:red;">OpenRTM-aistのPython版やPyYAMLをインストールする前にインストールしてください</span>;
  - OpenRTM-aist Python の64bit版をインストールされる場合は、[Python2.7(64bit)](https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi) をインストールしてください。　
- OpenRTM-aist Python 1.1.0-RELEASE
  - 32bit版インストーラは、[こちら](http://openrtm.org/pub/Windows/OpenRTM-aist/python/OpenRTM-aist-Python_1.1.0-RELEASE_x86.msi) からダウンロードできます。
  - 64bit版インストーラは、[こちらのページ]({{ site.baseurl }}/en/download/openrtm-aist-python/openrtm-aist-python_1_1_0_release) からダウンロードできます。　　
- [PyYAML(32bit)](http://pyyaml.org/download/pyyaml/PyYAML-3.11.win32-py2.7.exe)
  - Python2.7(64bit)をインストールされた場合は、[PyYAML(64bit)](http://pyyaml.org/download/pyyaml/PyYAML-3.11.win-amd64-py2.7.exe) をインストールしてください。　
- [CMake](http://www.cmake.org/files/v3.2/cmake-3.2.1-win32-x86.exe)
- [Doxygen](http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.9.1-setup.exe)
- 使い慣れたエディタ: EclipseやPythonに付属のエディタでも構いませんが、使い慣れたエディタが入っていた方が良いでしょう

#### Linux環境
<span style="color:red;">講習会は基本的にWindows環境を前提に行います。Linuxを利用したい場合は自己責任にてご参加ください。</span>;

Ubuntu14.04 x64 の環境へ以下をインストールして下さい。

- OpenRTM-aist C++ 1.1.1-RELEASE版
  - [JVRCオンラインチュートリアル](http://jvrc.github.io/tutorials/html-ja/index.html) にChoreonoidと共にインストールする方法が解説されています。
- OpenRTP
  - [こちらのページ]({{ site.baseurl }}/en/download/tools/openrtp_1_1_0_rc5) からLinux用の全部入りパッケージをダウンロードできます。
インストール方法も解説しています。
- OpenCV
  - 下記パッケージをインストールして下さい。<br>
$ sudo apt-get install libopencv-dev libcv2.4 libcvaux2.4 libhighgui2.4
- OpenCVサンプルコンポーネント(ImageProcessing)
  - [こちら]()(No corresponding page available.) からdebパッケージをダウンロード・インストールして下さい。<br>
$ sudo dpkg -i imageprocessing-1.1.0.deb

<!-- &aname(entry); -->
<!-- **講習会申し込みフォーム -->

<!-- 以下のフォームから講習会へお申し込みください。 -->
<!-- - 参加登録するまえに当Webページのユーザ登録をお願いします。[[ユーザ登録はこちら:http://openrtm.org/openrtm/ja/user/register]] -->
<!-- - 当Webサイトにログイン済みの方は&color(red){名前の欄のユーザ名を氏名に書き換えてください};。 -->
<!-- - フォーム送信後、確認メールをお送りいたします。1日たっても確認メールが届かない場合は、[[こちら（support@openrtm.org）:mailto:support@openrtm.org]] までお問い合わせください。 -->

### 講義資料
#### 第1部 RTミドルウエア: OpenRTM-aist概要、　第2部: RTコンポーネントの作成入門
- [講義資料(PDF)](/sites/default/files/5891/150919-01.pdf)


<!-- Invalid YouTube URL: http://www.slideshare.net/53135862 -->
{% include slideshare.html
   src="https://www.slideshare.net/slideshow/embed_code/key/lpIp1EwvTTVd0Q"
%}


## 講習会の様子
<div align="center"><a href="150919-01.jpg"><img src="150919-01.jpg" width="60%;"></a></div>
<br>

<div align="center"><a href="150919-02.jpg"><img src="150919-02.jpg" width="60%;"></a></div>
<br>

<div align="center"><a href="150919-03.jpg"><img src="150919-03.jpg" width="60%;"></a></div>
<br>

<div align="center"><a href="150919-04.jpg"><img src="150919-04.jpg" width="60%;"></a></div>
<br>

<div align="center"><a href="150919-05.jpg"><img src="150919-05.jpg" width="60%;"></a></div>
<br>
<!-- -------jp page!!------- -->
