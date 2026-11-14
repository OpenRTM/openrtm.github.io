---
layout: page
Title: OpenRTM-aistインストーラ作業内容
---

<!-- Title: OpenRTM-aistインストーラ作業内容 -->

<br>

## インストーラーの作業内容

インストーラーは以下の作業内容に従ってファイルのコピー、システム設定を行います。
インストール、アンインストールが正しく行われているかの確認する際の参考のために以下に記しておきます。

- インストールディレクトリ(C:\Program Files)下に各種ファイルをコピー
- スタートメニュー以下にOpenRTM-aistフォルダーを作成し各種ショートカットを設定
- 環境変数の設定（OpenRTM-aist 2.0.0版をデフォルト設定でインストールした場合）
```
 RTM_BASE=C:\Program Files\OpenRTM-aist\\
 RTM_ROOT=C:\Program Files\OpenRTM-aist\2.0.0\\
 RTM_VC_VERSION=vc16  (※インストール時Visual Studioのバージョン2015、2017を選択した場合は、vc14)
 RTM_JAVA_ROOT=C:\Program Files\OpenRTM-aist\2.0.0\\
 RTM_IDL_DIR=C:\Program Files\OpenRTM-aist\2.0.0\rtm\idl\\
 OMNI_ROOT=C:\Program Files\OpenRTM-aist\2.0.0\omniORB\4.2.5_vc16\\
 OpenCV_DIR=C:\Program Files\OpenRTM-aist\2.0.0\OpenCV4.4\\
 OpenRTM_DIR=C:\Program Files\OpenRTM-aist\2.0.0\cmake\\
```

- PATHへの追加設定（OpenRTM-aist 2.0.0版をデフォルト設定でインストールした場合）
```
 C:\Program Files\OpenRTM-aist\2.0.0\bin\vc16\\
 C:\Program Files\OpenRTM-aist\2.0.0\omniORB\4.2.5_vc16\bin\x86_win32\\
 C:\Program Files\OpenRTM-aist\2.0.0\OpenCV4.4\x64\vc16\bin\\
```


## インストールされるファイル
ファイルは以下のような構造でインストールされます。<br>
<!-- 上記のインストール環境の設定を確認する[[スクリプト:/ja/node/6092]]を実行すると、treeコマンドによるOpenRTM-aist下のディレクトリ構造をログファイルに保存しますので、詳細を確認できます。  -->

```
 <install_dir>
   + OpenRTM-aist
      + 1.x.x  :旧バージョンのランタイム
      + 2.0.x
         + bin: dll、lib各種コマンド
         + cmake: OpenRTMConfig.cmake
         + coil: coilヘッダファイル
         + Components
            + C++
               + Examples: C++サンプルコンポーネント
               + OpenCV: OpenCVのC++サンプルコンポーネント
            + Java: Java サンプルコンポーネント
            + Python: Python サンプルコンポーネント
         + ext: 拡張モジュール用ファイル
         + hrtm: HRTMのラッパーライブラリ
         + jar: jarファイル
         + jre: AdoptOpenJDK JRE
         + omniORB 4.2.5
         + OpenCV 4.4
         + rtm: OpenRTM-aistヘッダファイル
            + idl: OpenRTM-aistIDLファイル
         + util
            + OpenRTP: RTCBuilderとRTSystemEditorツール
            + RTSystemEditor: RTSystem Editorのみのファイル
            + VCVerChanger: 使用しているVisual Studioのバージョンを指定するツール
```


