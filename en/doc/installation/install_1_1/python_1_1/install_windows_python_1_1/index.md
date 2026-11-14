---
layout: page
title: windowsへのインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: Windowsへのインストール -->
#contents

openrtm.org では Windows 用の msi (Microsoft Windows インストーラー)パッケージを提供しています。
msi パッケージを利用することで、依存ライブラリである omniORBpy や RTSystemEditor といったツールも同時にインストールすることができます。


## msi パッケージによるインストール

openrtm.org の[ダウンロードサイト]({{ site.baseurl }}/en/download/openrtm-aist-python/openrtm-aist-python_1_1_2_release)から、msi パッケージをダウンロードします。msi パッケージには、必要な omniORBpy や RTSystemEditor といったツールは含まれていますが、Python は予めインストールしておく必要があります。

1.1.2 版からは一つの Windows 用インストーラーに3言語（C++、Java、Python）＋ツール（Eclipse＋rtshell）すべてが同梱されています。古いバージョンは予めアンインストールすることをお勧めします。　また、[ダウンロードサイト]({{ site.baseurl }}/en/download/openrtm-aist-python/openrtm-aist-python_1_1_2_release)での赤字表記の注意書きをご覧下さい。

### インストーラーの起動

手順については、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/quick_start_1_1_2/) のページをご覧下さい。


## インストールの詳細
### インストーラーの作業内容
インストーラーは以下の作業を行います。

- インストールディレクトリー (デフォルトは C:\Python<version>) 以下に各種ファイルをコピー
- インストールディレクトリー (デフォルトは C:\Program Files) 以下に各種ファイルをコピー
- スタートメニュー以下に OpenRTM-aist フォルダーを作成し各種ショートカットを設定
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
  - 32 bit 用 msi 利用時の設定

```
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\bin\vc12\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\omniORB\4.2.1_vc12\bin\x86_win32\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\OpenCV2.4.11\x86\vc12\bin\ 
```

インストール環境の設定を確認するスクリプトを提供しています。スクリプトの使い方、確認できる内容について下記ページで解説しています。

- http://openrtm.org/openrtm/ja/content/rtm-install-check-script

### インストールされるファイル
ファイルは以下のような構造でインストールされます。<br>
上記のインストール環境の設定を確認する[スクリプト]({{ site.baseurl }}/en/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/windows_install_test_bat)を実行すると、tree コマンドによる Python がインストールされているディレクトリーと Program Files 下の OpenRTM-aist ディレクトリー構造をログファイルに保存しますので、詳細を確認することができます。 

```
<python_install_dir>
   + omniORBのdll, 各種コマンド
   + rtcd, rtcprofileなどOpenRTM-aist 関連の各種コマンド
   |
   + Lib
   |  + site-packages
   |     + OpenRTM_aist: OpenRTM-aist の Python モジュール
   |        + RTM_IDL: IDLファイル
   |
   |     + omniORB 関連の Python モジュール
```
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
               + OpenCV: OpenCV の C++ サンプルコンポーネント
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


以上、インストールが終了しましたら、[動作確認]({{ site.baseurl }}/en/doc/installation/install_1_1/python_1_1/test_windows_python_1_1) へ進みましょう。


