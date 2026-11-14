---
layout: page
title: windows_installer_test.batの利用方法
---


<!-- Title: windows_installer_test.batの利用方法 -->
#contents

## windows_installer_test.batとは

OpenRTM-aistをインストールしているWindows環境の設定を調べるスクリプトです。OpenRTM-aist 1.1.2版のインストール環境を調べるために作成しましたが、これ以前のバージョンがインストールされている環境でも使用可能です。<br>
スクリプトをダブルクリックで実行するだけで結果がログファイルに出力され、以下の内容を確認することができます。

- OpenRTM-aistのインストール確認
  - インストールされていれば、treeコマンドによるディレクトリ構造を別ファイルに書き出す

- システム環境変数の確認

- Pathの確認

- OpenRTM-aist-Pythonとrtshellのインストール確認
  - インストールされていれば、treeコマンドによるディレクトリ構造を別ファイルに書き出す

- カスタムインストールリスト確認

## ダウンロード

以下の場所からダウンロードできます。

<table class="table-alt">
  <tr>
    <th>**windows_installer_test.bat**</th>
    <th>http://svn.openrtm.org/openrtm-msi-buildtool/trunk/openrtm_msi/test_scripts/windows_installer_test.bat</th>
  </tr>
</table>

## 実行

ダウンロードした windows_installer_test.bat ファイルをダブルクリックします。　実行中コマンドプロンプト画面が表示されますが、終了すれば消えますので、それまでお待ちください。

### カスタム実行（Cygwin利用）

インストールされているディレクトリ構造をtreeコマンドでログファイルに書き出しています。<br>
Cygwinのtreeコマンドがインストールされている環境ならば、スクリプト冒頭の下記設定を環境に合わせて下さい。%CYGWIN_DIR%\bin\tree.exe が存在しない場合はWindows標準のtreeコマンドを使用します。<br>

Cygwinのtreeコマンドがインストールされていると、OpenRTM-aist-Pythonとrtshellのインストールディレクトリ構造のログ　yymmdd-hhmmss_'Python directory'-dir.tree　がコンパクトになります。出力指定で何階層目までディレクトリを降りるかを指定できるからです。
Windows標準のtreeコマンドは階層指定ができないため、OpenRTM-aist-PythonがインストールされているPythonディレクトリのトップからの構造を全てが対象になってしまいます。そのため、ログにはディレクトリ名だけを出力しています。


```
 set CYGWIN_DIR=C:\Cygwin64
```

## ログファイル

実行結果は全てログファイルに出力されます。出力先は、スクリプトと同じディレクトリのlogフォルダ（無ければ自動で作成される）下です。<br>
本スクリプトをUSBメモリ上で実行し、結果は別のPCで確認するという使い方ができます。

<table class="table-alt">
  <tr>
    <th>**ログファイル名**</th>
    <th>**説明**</th>
  </tr>
  <tr>
    <td>yymmdd-hhmmss.log</td>
    <td>メインのログファイル</td>
  </tr>
  <tr>
    <td>yymmdd-hhmmss_pfile.tree</td>
    <td>C:\Program Files\OpenRTM-aistが存在していた場合に出力されます。treeコマンドによるOpenRTM-aistディレクトリ構造を確認できます。<br> OpenRTM-aistの64bit版は既にアンインストールされている場合でも、rtc`***.log`等のファイルが存在するためにディレクトリが残っている場合は、このログファイルが出力されることになります。</td>
  </tr>
  <tr>
    <td>yymmdd-hhmmss_pfile_x86.tree</td>
    <td>C:\Program Files (x86)\OpenRTM-aistが存在していた場合に出力されます。treeコマンドによるOpenRTM-aistディレクトリ構造を確認できます。<br> OpenRTM-aistの32bit版は既にアンインストールされている場合でも、64bit版と同じ理由でこのログファイルが出力される場合があります。</td>
  </tr>
  <tr>
    <td>yymmdd-hhmmss_'Python directory'-dir.tree</td>
    <td>OpenRTM-aist-Pythonがインストールされている場合に出力されます。treeコマンドによるOpenRTM-aist-PythonとrtshellがインストールされているPythonディレクトリ構造を確認できます。<br>インストール先がC:\Python27だった場合は、ログファイル名がyymmdd-hhmmss_Python27-dir.treeとなります。</td>
  </tr>
</table>

## 出力内容詳細

### メインのログファイル

#### OpenRTM-aistのインストール確認（Program Filesフォルダをチェック）
「C:\Program Files\OpenRTM-aist」と「C:\Program Files (x86)\OpenRTM-aist」のディレクトリ存在確認をしています。OpenRTM-aistを既にアンインストールしていても、インストール後に生成されたファイル（rtc***.log等）が存在しているとディレクトリが残ってしまいます。ディレクトリが「exist!」となっていても、C++, Python, Javaの各Examplesが「not installed」の場合はこのケースが考えられます。treeファイルを確認して下さい。

- 1.1.2版がインストールされている環境での出力例
  - 下記の結果は32bit版のみがインストールされていることを示しています
  - C:\Program Files (x86)\OpenRTM-aistのディレクトリ構造の保存先ファイルは、log\20160906-141617_pfile_x86.tree 
  - 1.1.2 のバージョン番号は、RTM_ROOT の設定から取得したもの

```
 *-*-*-*-*-*-* check OpenRTM-aist installed directory *-*-*-*-*-*-* 
 [[check]] "C:\Program Files\OpenRTM-aist" directory 
 --- not exist! 
 
 [[check]] "C:\Program Files (x86)\OpenRTM-aist" directory 
 --- exist! 
 --- RTM_VERSION = 1.1.2 
 
 Result ⇒ log\20160906-141617_pfile_x86.tree 
 --- C++ Examples (1.1.2) ⇒  installed 
 --- Python Examples (1.1.2) ⇒  installed 
 --- Java Examples (1.1.2) ⇒  installed 
```

- 1.1.1版のみがインストールされている環境での出力例

```
 *-*-*-*-*-*-* check OpenRTM-aist installed directory *-*-*-*-*-*-* 
 [[check]] "C:\Program Files\OpenRTM-aist" directory 
 --- not exist! 
 
 [[check]] "C:\Program Files (x86)\OpenRTM-aist" directory 
 --- exist! 
 --- RTM_VERSION = 1.1 
 
 Result ⇒ log\20160906-133745_pfile_x86.tree 
 --- C++ Examples (1.1) ⇒  installed 
 --- Python Examples (1.1) ⇒  installed 
 --- Java Examples (1.1) ⇒  not installed 
```

- 32bit OS環境での出力例
  - この環境は「C:\Program Files (x86)」のパスは存在しないため、「This PC is 32bit OS.」と表示させています

```
 *-*-*-*-*-*-* check OpenRTM-aist installed directory *-*-*-*-*-*-* 
 [[check]] "C:\Program Files\OpenRTM-aist" directory 
 --- exist! 
 --- RTM_VERSION = 1.1.2 
 
 Result ⇒ log\20160907-104846_pfile.tree 
 --- C++ Examples (1.1.2) ⇒  installed 
 --- Python Examples (1.1.2) ⇒  installed 
 --- Java Examples (1.1.2) ⇒  installed 
 
 --- This PC is 32bit OS. 
```

#### システム環境変数の確認
- 1.1.2版がインストールされている環境での出力例

```
 *-*-*-*-*-*-* check system environment variables *-*-*-*-*-*-* 
 RTM_BASE=C:\Program Files (x86)\OpenRTM-aist\\
 RTM_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\\
 RTM_VC_VERSION=vc12
 RTM_JAVA_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\\
 OMNI_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1.2\omniORB\4.2.1_vc12\\
 OpenCV_DIR=C:\Program Files (x86)\OpenRTM-aist\1.1.2\OpenCV2.4.11\\
 OpenRTM_DIR=C:\Program Files (x86)\OpenRTM-aist\1.1.2\cmake\\
```

- 1.1.1版のみがインストールされている環境での出力例
  - 1.1.2版で追加された環境変数は1.1.1版では設定されていないことを確認できる

```
 *-*-*-*-*-*-* check system environment variables *-*-*-*-*-*-*  
 環境変数 RTM_BASE  が定義されていません
 RTM_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1\\
 環境変数 RTM_VC_VERSION  が定義されていません
 RTM_JAVA_ROOT=C:\Program Files\OpenRTM-aist\1.1\\
 OMNI_ROOT=C:\Program Files (x86)\OpenRTM-aist\1.1\omniORB\4.1.7_vc10\\
 OpenCV_DIR=C:\Program Files (x86)\OpenRTM-aist\1.1\OpenCV2.4.9\\
 環境変数 OpenRTM_DIR  が定義されていません
```


#### Pathの確認

- OpenRTM-aistが設定しているパスとOpenCVの設定を抜き出しています
- 1.1.2版がインストールされている環境での出力例


```
 *-*-*-*-*-*-* check Path *-*-*-*-*-*-* 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\bin\vc12\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\omniORB\4.2.1_vc12\bin\x86_win32\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1.2\OpenCV2.4.11\x86\vc12\bin\ 
```

- 別途OpenCVがインストールされている環境での出力例
  - OpenRTM-aistに先立ってOpenCVがインストールされている（Pathに追加されている）環境を確認できます

```
 *-*-*-*-*-*-* check Path *-*-*-*-*-*-*
 C:\distribution\opencv3.0.0\build\x86\vc10\bin 
 C:\Program Files (x86)\OpenRTM-aist\1.1\bin\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1\omniORB\4.1.7_vc10\bin\x86_win32\ 
 C:\Program Files (x86)\OpenRTM-aist\1.1\OpenCV2.4.9\x86\vc10\bin\
```

#### PythonとOpenRTM-aist-Pythonとrtshellのインストール確認

- Pythonがインストールされているパスをレジストリから取得し、OpenRTM-aist-Pythonとrtshellがインストールされているかどうかを確認できます
- Pythonの複数バージョンをインストールしている環境も対応しています
- 1.1.2版がインストールされている環境での出力例
  - PYTHON_DIR\omniidl.exe が存在すればOpenRTM-aist-Pythonはインストールされていると判断
  - PYTHON_DIR\Lib\site-packages\rtshellが存在すればrtshellはインストールされていると判断

```
 *-*-*-*-*-*-* check Python installed directory *-*-*-*-*-*-* 
 C:\Python27\ ----OpenRTM-aist-Python installed.  
 C:\Python27\ ----rtshell installed.  
 C:\Python27_x64\ ----OpenRTM-aist-Python not installed.  
 C:\Python27_x64\ ----rtshell installed.  
 C:\Python35_x64\ ----OpenRTM-aist-Python not installed.  
 C:\Python35_x64\ ----rtshell not installed.  
 C:\Python35\ ----OpenRTM-aist-Python not installed.  
 C:\Python35\ ----rtshell not installed.  
```

#### OpenRTM-aist-Pythonとrtshellのインストールディレクトリ確認

- OpenRTM-aist-PythonがインストールされているPythonディレクトリ構造を出力します。
- 1.1.2版がインストールされている環境での出力例
  - 上記の結果で、C:\Python27_x64\にはOpenRTM-aist-Pythonはインストールされていないが、rtshellはインストールされているとありますが、
この環境は対象外と判断しています。

```
 *-*-*-*-*-*-* check OpenRTM-aist-Python installed directory *-*-*-*-*-*-* 
 Result ⇒ log\20160906-141617_Python27-dir.tree
```

- OpenRTM-aist-Python 1.1.0版がインストールされている環境での出力例
  - このバージョンはPython2.6と2.7に対応していたので、両方インストールされている場合はそれぞれのログファイルが出力されます

```
 *-*-*-*-*-*-* check OpenRTM-aist-Python installed directory *-*-*-*-*-*-* 
 Result ⇒ log\20160906-171616_Python26-dir.tree  
 Result ⇒ log\20160906-171616_Python27-dir.tree 
```

#### カスタムインストールの確認

- インストーラ実行時、カスタムインストールを選択された場合のインストール状況を確認できます
- 1.1.2版以降のバージョンを対象にしているので、1.1.1版のみがインストールされている環境ではログに出力されません
- 1.1.2版がインストールされている環境での出力例
  - インストーラ実行時にデフォルトの標準を選択していれば、[1]から[15]までの全てのモジュールがインストールされます。
ただし、64bit版のインストーラを実行時は、[12]はインストールされません。
  - カスタムインストール行った場合、選択しなかったモジュールはログに出力されません
  - カスタムインストールで選択しなかったモジュールでも、依存関係があるものはインストールされます

```
 *-*-*-*-*-*-* check Custom installed lists *-*-*-*-*-*-* 
 [1] C++ : Runtime Environment 
 [2] C++ : Development Environment 
 [3] C++ : Examples RTC 
 [4] C++ : OpenCV RTC 
 [5] OpenCV 
 [6] Python : Examples RTC 
 [7] Java : Runtime Environment 
 [8] Java : Examples RTC 
 [9] Tools : OpenRTP 
 [10] Tools : RTSystemEditorRCP 
 [11] Tools : JRE 
 [12] OpenRTM-aist old Runtime : 1.0.0 [x86 only] 
 [13] OpenRTM-aist old Runtime : 1.1.0 
 [14] OpenRTM-aist old Runtime : 1.1.1 
 [15] IDL 
```


### treeファイル

- treeコマンドの実行結果をそのまま保存したファイルです
- メインのログファイルと区別しやすいように拡張子をtreeとしているだけですので、テキストエディタで内容を確認して下さい
- 1.1.2版がインストールされている環境での出力例

```
 フォルダー パスの一覧
 ボリューム シリアル番号は 9CF9-3755 です
 C:\PROGRAM FILES (X86)\OPENRTM-AIST
 ├─1.0.0
 │  └─vc9
 │      └─bin
 │              coil.dll
   :
 └─1.1.2
     ├─bin
     │  │  cmakeconfgen.py
```

