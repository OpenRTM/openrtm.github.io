---
layout: page
title: cpack で rpm 作成 （linux）
---

<!-- title: CPack で rpm 作成 （Linux）-->
#contents

## はじめに

rpm パッケージの作成方法を以下に示します。<br>

## doxygen ドキュメントを含めない場合の作成手順
※デフォルトでは、ドキュメントビルドは OFF になっているため生成されません。

- C++ RTC の場合

```
 $ cd プロジェクトディレクトリー
 $ mkdir build
 $ cd build
 $ cmake ..
 $ make
 $ cpack
```

- Pyrhon RTC での場合

```
 $ cd プロジェクトディレクトリー
 $ mkdir build
 $ cd build
 $ cmake ..
 $ cpack
```

## doxygen ドキュメントを含める場合の作成手順
プロジェクトディレクトリー直下にある CMakeLists.txt の下記の行を、OFF → ON に書き換えます。<br>
C++ RTC の場合は 86行目あたり、Python RTC の場合は 77行目あたりです。

```
 option(BUILD_DOCUMENTATION "Build the documentation" ON) ※この行の OFF を ON に書き換えます。(デフォルトは OFF)
```

- C++ RTC の場合

```
 $ cd プロジェクトディレクトリー
 $ mkdir build
 $ cd build
 $ cmake ..
 $ make
 $ make doc
 $ cpack
```

- Pyrhon RTC での場合

```
 $ cd プロジェクトディレクトリー
 $ mkdir build
 $ cd build
 $ cmake ..
 $ make doc
 $ cpack
```

【注意事項】<br>
ドキュメントビルドを ON にして、「make doc」 をせずに 「cpack」 を実行すると以下のようなエラーになります。

```
 CMake Error at /home/プロジェクトディレクトリー/build/doc/cmake_install.cmake:36 (file):
 file INSTALL cannot find
 "/home/プロジェクトディレクトリー/build/doc/html/doxygen/html".
```

## rpm パッケージの保存場所、ファイル名
正常に作成できた場合は、プロジェクトディレクトリー内の [build] に保存されます。 <br>
ファイル名は、「RTCプロジェクト名-RTCのバージョン番号-アーキテクチャ」となります。<br>

(例) Flip-1.2.0-x86_64.rpm<br>
※アーキテクチャは、[i686] または [x86_64] となります。<br>

## rpm パッケージの確認方法
- less コマンドで、rpm パッケージの確認をする場合

```
 $ cd プロジェクトディレクトリー/build 
 $ less Flip-1.2.0-x86_64.rpm
 Name        : Flip
 Version     : 1.2.0
 Release     : 1
 Architecture: x86_64
 Install Date: (not installed)
 Group       : unknown
 Size        : 506080
 License     : unknown
 Signature   : (none)
 Source RPM  : Flip-1.2.0-1.src.rpm
 Build Date  : 2017年xx月xx日 xx時xx分x秒
 Build Host  : localhost
 Relocations : /usr 
 Vendor      : AIST
 Summary     : Flip image component
 Description :
 DESCRIPTION
```

less を終了させるには「q」を押します。

- rpm パッケージの内容を抽出して確認する場合<br>
tree コマンドがインストールされていない場合は、インストールします。

```
 $ sudo apt-get install tree
```

```
 $ cd プロジェクトディレクトリー/build 
 $ dpkg -x Flip-1.2.0-x86_64.rpm .
 $ tree usr
 usr
 └─ share
    　└─ openrtm-1.2
        　　└─ components
            　　　└─ python
               　　　 　└─ Category　※指定したインストール先ディレクトリー
                    　　　　　└─ FlipGUI
                        　　　　　　├─ RTC.xml
                        　　　　　　├─ FlipGUIComp.py
                        　　　　　　├─ idl
                        　　　　　　│    ├─ BasicDataType.idl
                        　　　　　　│    ├─ CMakeLists.txt
                     　　　　　　   │    ├─ CalibrationService.idl
                  　　　　　　      │    ├─ ExtendedDataTypes.idl
                        　　　　　　│    └─ InterfaceDataTypes.idl
                        　　　　　　├─ idlcompile.sh
                      　　　　　　  ├─ rtutil.py
                        　　　　　　├─ setup.py
                        　　　　　　└─ flipgui.py
```


## rpm パッケージのインストール・アンインストール
### インストール
インストールは以下のコマンドを実行します。
```
 $ cd プロジェクトディレクトリー/build 
 $ sudo rpm -i Flip-1.2.0-x86_64.rpm
```

### アンインストール
アンインストールは以下のコマンドを実行します。
```
 $ sudo rpm -e Flip
```

## サービスポートを持つ Python RTC の IDL コンパイル処理 
サービスポートを持つ Python RTC は、パッケージインストール時に IDL コンパイルを実行します。
IDL コンパイル実行時に、プロジェクトディレクトリー内にある postinst.in、prerm.in でこの動作を実現させているため、これらのファイルを削除してしまうと機能しなくなるので注意が必要です。<br><br>
以下、rpm パッケージからインストールされるファイル一覧です。★マークが IDL コンパイルで生成されるファイルです。 

```
 $ tree /usr/share/openrtm-1.2/components/python/Category/FlipGUI/
 /usr/share/openrtm-1.2/components/python/Category/FlipGUI/
  ├─ BasicDataType_idl.py  ★
  ├─ CalibrationService_idl.py  ★
  ├─ ExtendedDataTypes_idl.py  ★
  ├─ ImageCalibService  ★
  │   └─ __init__.py  ★
  ├─ ImageCalibService__POA  ★
  │   └─ __init__.py  ★
  ├─ InterfaceDataTypes_idl.py  ★
  ├─ RTC  ★
  │   └─ __init__.py  ★
  ├─ RTC.xml
  ├─ RTC__POA  ★
  │   └─ __init__.py  ★
  ├─ FlipGUIComp.py
  ├─ idl
  │   ├─ BasicDataType.idl
  │   ├─ CMakeLists.txt
  │   ├─ CalibrationService.idl
  │   ├─ ExtendedDataTypes.idl
  │   └─ InterfaceDataTypes.idl
  ├─ idlcompile.sh
  ├─ rtutil.py
  ├─ setup.py
  └─ flipgui.py
```

