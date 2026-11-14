---
layout: page
title: cpack で deb 作成 （linux）
---

<!-- Title: CPack で deb 作成 （Linux） -->
#contents

## はじめに

deb パッケージの作成方法を以下に示します。<br>

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

## deb パッケージの保存場所、ファイル名
正常に作成できた場合は、プロジェクトディレクトリーの  [build] 内に保存されます。 <br>
ファイル名は、「RTCプロジェクト名_RTCのバージョン番号_アーキテクチャ」となります。<br>

(例) Flip_1.2.0_amd64.deb<br>
※アーキテクチャは、[i386] または [amd64] となります。<br>

## deb パッケージの確認方法
- less コマンドで、deb パッケージの確認をする場合

```
 $ cd プロジェクトディレクトリー/build 
 $ less Flip_1.2.0_amd64.deb
 Flip_1.2.0_amd64.deb
 新形式 debian パッケージ、バージョン 2.0。
 サイズ 258304 バイト: コントロールアーカイブ = 2797 バイト。
     162 バイト、    9 行      control              
   10062 バイト、   92 行      md5sums              
 Package: affine
 Version: 1.2.0
 Section: devel
 Priority: optional
 Architecture: amd64
 Installed-Size: 884
 Maintainer: unknown　※パッケージメンテナー情報を定義していないと「unknown」になります
 Description: Flip image component
```

less を終了させるには「q」を押します。

- deb パッケージの内容を抽出して確認する場合<br>
tree コマンドがインストールされていない場合は、インストールします。

```
 $ sudo apt-get install tree
```

```
 $ cd プロジェクトディレクトリー/build 
 $ dpkg -x Flip_1.2.0_amd64.deb .
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

## deb パッケージのインストール・アンインストール
### インストール
インストールは以下のコマンドを実行します。
```
 $ cd プロジェクトディレクトリー/build 
 $ sudo dpkg -i Flip_1.2.0_amd64.deb 
```

### アンインストール
アンインストールは以下のコマンドを実行します。
```
 $ sudo dpkg -ｒ Flip
```

## サービスポートを持つ Python RTC の IDL コンパイル処理 
サービスポートを持つ Python RTC は、パッケージインストール時に IDL コンパイルを実行します。
IDL コンパイル実行時に、プロジェクトディレクトリー内にある postinst.in、prerm.in でこの動作を実現させているため、これらのファイルを削除してしまうと機能しなくなるので注意が必要です。<br><br>
以下、debパッケージからインストールされるファイル一覧です。★マークが IDL コンパイルで生成されるファイルです。 
```
 $ tree /usr/share/openrtm-1.2/components/python/Category/FlipGUI/
 /usr/share/openrtm-1.2/components/python/Category/FlipGUI/
   ├─ BasicDataType_idl.py  ★
   ├─ CalibrationService_idl.py  ★
   ├─ ExtendedDataTypes_idl.py  ★
   ├─ ImageCalibService  ★
   │   └─ __init__.py  ★
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
   │   ├─ CMakeLists.txt
   │   ├─ CalibrationService.idl
   │   ├─ ExtendedDataTypes.idl
   │   └─ InterfaceDataTypes.idl
   ├─ idlcompile.sh
   ├─ rtutil.py
   ├─ setup.py
   └─ flipgui.py
```

