---
layout: page
title: windowsへのインストール
---

<!-- Title Windowsへのインストール -->
#contents

## OpenRTM-aistのインストール
MSIインストーラーによるOpenRTM-aistのインストール手順については下記のページに記載。

- [OpenRTM-aist 1.2系のインストール(Windows、MSIインストーラー使用)]({{ site.baseurl }}/ja/doc/appendix/openrtm-aist_1_2_windows_msi)


## 開発に必要なソフトウエアのインストール
RTCの開発にはCMake、Doxygen、Visual Studioのインストールが必要です。

- [CMake(3.11以上推奨)](https://cmake.org/download/)
インストールの途中で[Install Options]としてsystem PATHをどうするかを聞かれますが、Add CMake to the system PATH for all usersを選択することを推奨します。(チェックはそれで行っています。)
- [Doxygen](http://www.doxygen.nl/download.html)
のWebページからWindows版のバイナリ実行形式ファイルをダウンロードして実行してインストールしてください。
- [Visual Studio]({{ site.baseurl }}/ja/doc/installation/install_1_2/cpp_1_2/install_windows_1_2/visual_studio_1_2/visual_studio_2022)
からダウンロード版をインストールするか、別途Visual Studio 2010/2012/2013/2015/2017/2019を入手してインストールしてください。Visual StudioはPythonベースのRTC開発自体には直接必要なものではないですが、開発したRTCの配布にあたってOpenRTM-aistの環境と共にMSI配布パッケージを作りたい場合は必要となります。

## インストーラーの作業内容
インストーラーは以下の作業を行います。

- インストールディレクトリ(デフォルトはC:\Program Files)下に各種ファイルをコピー
- スタートメニュー以下にOpenRTM-aistフォルダーを作成し各種ショートカットを設定

  - 環境変数とPATHの設定
    - 64bit用MSI利用時の環境変数

```
 RTM_BASE=C:\Program Files\OpenRTM-aist\\
 RTM_ROOT=C:\Program Files\OpenRTM-aist\1.2.1\\
 RTM_VC_VERSION= //ここにはユーザーが指定したVisual StudioにのっとったVCのバージョンを指定するテキストが入ります
 RTM_JAVA_ROOT=C:\Program Files\OpenRTM-aist\1.2.1\\
 OMNI_ROOT=C:\Program Files\OpenRTM-aist\1.2.1\omniORB\4.2.3_%RTM_VC_VERSION%\\
 OpenCV_DIR=C:\Program Files\OpenRTM-aist\1.2.1\OpenCV3.4\\
 OpenRTM_DIR=C:\Program Files\OpenRTM-aist\1.2.1\cmake\\
```

   - 64bit用MSI利用時のPATHへの追加設定

```
 C:\Program Files\OpenRTM-aist\1.2.1\bin\%RTM_VC_VERSION%\\
 C:\Program Files\OpenRTM-aist\1.2.1\omniORB\4.2.1_%RTM_VC_VERSION%\bin\x86_win32\\
 C:\Program Files\OpenRTM-aist\1.2.1\OpenCV3.4\%RTM_VC_VERSION%\bin\\
```

   - 32bit用MSI利用時の環境変数

(64bit版Windows 10での場合で、32bit版の場合は「Program Files (x86)」の部分が「Program Files」になります。)

```
 RTM_BASE=C:\Program Files (x86)\OpenRTM-aist\\
 RTM_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.2.1\\
 RTM_VC_VERSION= //ここにはユーザーが指定したVisual StudioにのっとったVCのバージョンを指定するテキストが入ります
 RTM_JAVA_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.2.1\\
 OMNI_ROOT=C:\Program Files\OpenRTM-aist\1.2.1\omniORB\4.2.3_%RTM_VC_VERSION%\\
 OpenCV_DIR=C:\Program Files\OpenRTM-aist\1.2.1\OpenCV3.4\\
 OpenRTM_DIR=C:\Program Files\OpenRTM-aist\1.2.1\cmake\\
```

   - 32bit用MSI利用時の PATHへの追加設定
(64bit版Windows 10での場合で、32bit版の場合は「Program Files (x86)」の部分が「Program Files」になります。)

```
 C:\Program Files(x86)\OpenRTM-aist\1.2.1\bin\%RTM_VC_VERSION%\\
 C:\Program Files(x86)\OpenRTM-aist\1.2.1\omniORB\4.2.3_%RTM_VC_VERSION%\bin\x86_win32\\
 C:\Program Files(x86)\OpenRTM-aist\1.2.1\OpenCV3.4\x86\%RTM_VC_VERSION%\bin\\
```

<!--  -->
<!-- インストール環境の設定を確認するスクリプトを提供しています。スクリプトの使い方、確認できる内容について下記ページで解説しています。 -->
<!--  -->
<!-- - http://openrtm.org/openrtm/ja/content/rtm-install-check-script -->
<!--  -->

## インストールされるファイル
ファイルは以下のような構造でインストールされます。<br>
<!-- 上記のインストール環境の設定を確認する[[スクリプト:/ja/node/6092]]を実行すると、treeコマンドによるOpenRTM-aist下のディレクトリ構造をログファイルに保存しますので、詳細を確認できます。  -->

```
 <install_dir>
   + OpenRTM-aist
      + 1.x.x  :旧バージョンのランタイム
      + 1.2.1
         + bin: dll、lib各種コマンド
         + cmake: OpenRTMConfig.cmake
         + coil: coilヘッダファイル
         + Components
            + C++
               + Examples: C++サンプルコンポーネント
               + OpenCV: OpenCVのC++サンプルコンポーネント
            + Java: Java サンプルコンポーネント
            + Python: Python サンプルコンポーネント
         + etc: rtc.confサンプル
         + jar: jarファイル
         + jre: OpenJDK JRE
         + omniORB
         + OpenCV3.4
         + rtm: OpenRTM-aistヘッダファイル
            + ext: 拡張モジュール用ファイル 
            + idl: OpenRTM-aistIDLファイル
         + util
            + ExcelControlpy: PythonベースのMicrosoft Office用RTC
            + OpenRTP: RTCBuilderとRTSystemEditorツール
            + PowerPointControlpy: Microsoft Office PowerPoint用RTC
            + python_dist: pythonベースツール共通ライブラリ
            + RTCDT: PythonベースRTCの開発を支援するツール
            + rtc-template: RTCBuilderと似た機能を提供する古いツール
            + RTSystemEditor: RTSystem Editorのみのファイル
            + VCVerChanger: 使用しているVisual Studioのバージョンを指定するツール
            + WordContrlpy: PythonベースMicrosoft Office Word用RTC

```
