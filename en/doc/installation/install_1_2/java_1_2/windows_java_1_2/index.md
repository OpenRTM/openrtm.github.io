---
layout: page
title:  windowsへのインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: Windowsへのインストール -->
#contents

## OpenRTM-aistのインストール
MSIインストーラーによるOpenRTM-aistのインストール手順については下記のページに記載。
- [OpenRTM-aist1.2系のインストール(Windows、MSIインストーラー使用)]({{ site.baseurl }}/en/doc/appendix/openrtm-aist_1_2_windows_msi)
より、.msiファイルをダウンロードしてください。ファイル名は、64ビット版なら"x86_64.msi"で、32bit版なら"64.msi"で終端された名前となります。ダウンロードした後は、拡張子.msiのファイルをダブルクリックすればインストールプログラムが起動されます。インストール途中で[標準]を選択するとこの.msiファイルが対応している全ての構成がインストールされます。一部の構成のみをインストールしたい場合は[カスタム]を選択してください。(一部の構成のみの検証は十分にはなされていないので、[標準]でインストールすることを推奨します。）

## JDK8のインストール
OpenRTM-aist-Java-1.２.ｘの動作にはJDK8相当のJDK(JDK11では正常動作しません)が前もってインストールされている必要があります。JDK8の入手やインストールについては以下を参照してください。
- [JDK8のインストール]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

### JDKのインストール確認
コマンドプロンプトを開き、
```
 C:\>java -version
```
と入力します。インストールしたJavaのバージョンが表示されればインストールは完了です。例えば以下のように表示されます。
```
 openjdk version "1.8.0_232"
 OpenJDK Runtime Environment (build 1.8.0_232-b09)
 OpenJDK 64-Bit Server VM (build 25.232-b09, mixed mode)
```

## インストーラーの作業内容
インストーラーは以下の作業を行います。
- インストールディレクトリ(デフォルトはC:\Program Files)以下に各種ファイルをコピー
- スタートメニュー以下にOpenRTM-aistフォルダーを作成し各種ショートカットを設定
- 環境変数の設定
  - 64bit版MSIファイルの場合
```
 RTM_BASE=C:\Program Files\OpenRTM-aist\\
 RTM_IDL_DIR=C:\Program Files\OpenrRTM-aist\1.2.1\rtm\idl\\
 RTM_JAVA_ROOT=C:\Program Files\OpenRTM-aist\1.2.1\\
 RTM_ROOT=C:\Program Files\OpenRTM-aist\1.２.1\\
 RTM_VC_VERSION=vc14
 OMNI_ROOT=C:\Program Files\OpenRTM-aist\1.2.1\omniORB\4.2.1_%RTM_VC_VERSION%\\
 OpenCV_DIR=C:\Program Files\OpenRTM-aist\1.2.1\OpenCV3.4\\
 OpenRTM_DIR=C:\Program Files\OpenRTM-aist\1.2.1\cmake\\
```

  - 32bit版MSIファイルの場合
```
 RTM_BASE=C:\Program Files (x86)\OpenRTM-aist\\
 RTM_IDL_DIR=C:\Program Files (x86)\OpenrRTM-aist\1.2.1\rtm\idl\\
 RTM_JAVA_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.2.1\\
 RTM_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.２.1\\
 RTM_VC_VERSION=vc14
 OMNI_ROOT=C:\Program Files\OpenRTM-aist\1.2.1\omniORB\4.2.3_%RTM_VC_VERSION%\\
 OpenCV_DIR=C:\Program Files\OpenRTM-aist\1.2.1\OpenCV3.4\\
 OpenRTM_DIR=C:\Program FilessOpenRTM-aist\1.2.1\cmake\\
```

  - 64bit版MSIファイルの場合に追加されるパス
```
 C:\Program Files\OpenRTM-aist\1.2.1\bin\%RTM_VC_VERSION%\\
 C:\Program Files\OpenRTM-aist\1.2.1\omniORB\4.2.3_%RTM_VC_VERSION%\bin\x86_win32\\
 C:\Program Files\OpenRTM-aist\1.2.1\OpenCV3.4\x64\%RTM_VC_VERSION%\bin\\
```

  - 32bit版MSIファイルの場合に追加されるパス
```
 C:\Program Files (x86)\OpenRTM-aist\1.2.1\bin\%RTM_VC_VERSION%\\
 C:\Program Files (x86)\OpenRTM-aist\1.2.1\omniORB\4.2.3_%RTM_VC_VERSION%\bin\x86_win32\\
 C:\Program Files (x86)\OpenRTM-aist\1.2.1\OpenCV3.4\x86\%RTM_VC_VERSION%\bin\\
```

### インストールされるファイル
ファイルは以下のような構造でインストールされます。
```
 <install_dir>
   + OpenRTM-aist
      + 1.x.x: 旧バージョンのランタイム
      + 1.2.1
         + bin: dll、lib各種コマンド
         + cmake: OpenRTMConfig.cmake
         + coil: coilヘッダファイル
         + Components
            + C++
               + Examples: C++サンプルコンポーネント
               + OpenCV: OpenCVのC++サンプルコンポーネント
            + Java: Javaサンプルコンポーネント
            + Python: Pythonサンプルコンポーネント
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

