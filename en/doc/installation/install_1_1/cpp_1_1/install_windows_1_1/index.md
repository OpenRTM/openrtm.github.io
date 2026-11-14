---
layout: page
title: windowsへのインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: Windowsへのインストール -->

<div align="left"><a href="windows_logo.png"><img src="windows_logo.png" width="10%;" align="left"></a></div>

openrtm.org では Windows 用の msi (Microsoft Windows インストーラー)パッケージを提供しています。
msi パッケージを利用することで、依存ライブラリである omniORB や、RTSystemEditor といったツールも同時にインストールすることができます。

#clear
#contents


## msi パッケージによるインストール

openrtm.org の[ダウンロードサイト]({{ site.baseurl }}/en/download/openrtm-aist-cpp/openrtm-aist-cpp_1_1_2_release)から、msi パッケージをダウンロードします。Python、PyYAML、CMake、Doxygen も必要ですのでインストールしてください。<br>
コンポーネントの開発を行う場合は、Visual Studio が必要です。[こちらのページ](https://www.visualstudio.com/ja-jp/downloads/download-visual-studio-vs#DownloadFamilies_2) から無償版をダウンロードできます。


1.1.2 版からは一つの Windows 用インストーラーに3言語（C++、Java、Python）＋ツール（Eclipse＋rtshell）すべてが同梱されています。古いバージョンは予めアンインストールすることをお勧めします。
また、[ダウンロードサイト]({{ site.baseurl }}/en/download/openrtm-aist-cpp/openrtm-aist-cpp_1_1_2_release)での赤字表記の注意書きをご覧ください。

### インストーラーの起動

手順については、1.1.2 版用の [OpenRTM-aistを10分で始めよう！](./quick_start_1_1_2) のページをご覧ください。<br>
1.1.1 版をご利用の場合は、[OpenRTM-aistを10分で始めよう！(OpenRTM-aist 1.1.1)]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/quick_start_1_1_2) のページをご覧ください。<br>
1.0.0 版をご利用の場合は、[OpenRTM-aistを10分で始めよう！(OpenRTM-aist 1.0.0)]()(No corresponding page available.) のページをご覧ください。


## インストールの詳細
### インストーラーの作業内容
インストーラーは以下の作業を行います。

- インストールディレクトリー (デフォルトは C:\Program Files) 以下に各種ファイルをコピー
<!-- --OpenRTM-aist ヘッダ、スクリプト、ライブラリ、サンプルを OpenRTM-aist\<version_number> 以下にコピー -->
<!-- --インストーラ・オプションの選択に合わせてスタンドアロン版 RTSystemEditor と OpenRTP をコピー -->
<!-- --インストーラ・オプションの選択に合わせてOpenJDK JRE をコピー -->
<!-- --omniORB ヘッダ、ライブラリ、コマンド等を omniORB 以下にコピー -->
<!-- --Visual C++ランタイムをシステムディレクトリへコピー -->
- スタートメニュー以下に OpenRTM-aist フォルダーを作成し各種ショートカットを設定
<!-- --rtcd、ネームサーバ等のショートカットを作成 -->
<!-- --サンプルRTCのショートカットを作成 -->
<!-- --doxygen によるクラスリファレンス、IDLリファレンスショートカットを作成 -->
- 環境変数の設定
  - 32bit 用 msi 利用時の設定

```
 RTM_BASE=C:\Program Files (x86)\OpenRTM-aist\\

 RTM_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\\

 RTM_VC_VERSION=vc12

 RTM_JAVA_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\\

 OMNI_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\omniORB\4.2.1_vc12\\

 OpenCV_DIR=C:\Program Files (x86)\OpenRTM-aist\1.1.2\OpenCV2.4.11\\

 OpenRTM_DIR=C:\Program Files (x86)\OpenRTM-aist\1.1.2\cmake\\
```

- PATH への追加設定
  - 32bit 用 msi 利用時の設定

```
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\bin\vc12\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\omniORB\4.2.1_vc12\bin\x86_win32\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\OpenCV2.4.11\x86\vc12\bin\ 
```

インストール環境の設定を確認するスクリプトを提供しています。スクリプトの使い方、確認できる内容について下記ページで解説しています。

- [http://openrtm.org/openrtm/ja/content/rtm-install-check-script]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/windows_install_test_bat)

### インストールされるファイル
ファイルは以下のような構造でインストールされます。<br>
上記のインストール環境の設定を確認する[スクリプト]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/windows_install_test_bat)を実行すると、tree コマンドによる OpenRTM-aist 下のディレクトリー構造をログファイルに保存しますので、詳細を確認することができます。 

```
 <install_dir>
   + OpenRTM-aist
      + 1.x.x  :旧バージョンのランタイム
      + <version>
         + bin: dll, lib, 各種コマンド
         + cmake: OpenRTMConfig.cmake
         + coil: coil ヘッダファイル
         + Components
            + CXX:
               + Examples: C++ サンプルコンポーネント
               + OpenCV: OpenCVのC++ サンプルコンポーネント
            + Java: Java サンプルコンポーネント
            + Python: Python サンプルコンポーネント
         + etc: rtc.confサンプル
         + ext: ComponentObserverConsumer
         + jar:
         + jre: OpenJDK JRE
         + omniORB
         + OpenCV
         + rtm: OpenRTM-aist ヘッダファイル
            + idl: OpenRTM-aist IDLファイル
         + util
            + OpenRTP:
            + RTSystemEditor:
            + rtc-template:
```


