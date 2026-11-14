---
layout: page
title: ソースからのビルド（c++版）
---

<!-- Title: ソースからのビルド（C++版） -->


OpenRTM-aist本体に改修を加えてWindows上で利用したい場合は、OpenRTM-aistのソースコードを取得してビルドできます。　2.0系からはCMakeに対応しましたので、1.2系までの手順とは異なっています。


#contents


<!-- ------------------------------------------------------------ -->
## 必要なソフトウエア・ライブラリ

以下のソフトウエアが必要です。詳細は [OpenRTM-aist 2.1系のWindowsへのインストール]({{ site.baseurl }}/ja/doc/installation/install_2_1/install_windows_2_1/install_2_1) をご覧ください。

- Visual Studio
- Python
- CMake
- Doxygen & Graphviz（ドキュメントビルドも行いたい場合）

また、omniORBライブラリも必要です。
- omniORB 4.3.4

openrtm.org が提供するビルド済みバイナリパッケージを下記リンク先に omniORB-4.3.4-x64-vc16-pyXX.zip という名称で用意してあります。
XXをインストールするpythonのバージョンに読み替えて適切なものをダウンロードし、適当な場所(以下の説明ではC:\workspace\omniORBとしています)に展開してください。

- [openrtm.org提供バイナリパッケージ](https://openrtm.org/pub/omniORB/win32/omniORB-4.3.4/)

他のライブラリを使ってのビルドについては、 [RTシステム開発 (応用編)・OpenRTM-aist(C++版)のCMakeによるビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build) をご覧ください。

## ビルド・インストール時のコマンド手順

ソースコード を入手します。OpenRTM-aist2.1系の最新ソースならばmasterブランチを、2.1.0版のリリースソースでしたらv2.1.0のタグをチェックアウトしてください。 <br>

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist
 git checkout -b v210-src refs/tags/v2.1.0
```


CMakeオプションで以下を指定して実行します。
- -DORB_ROOT : ダウンロード・展開したomniORBのパス
- -G : Visual Studio のバージョン（「Visual Studio 18 2026」「Visual Studio 17 2022」「Visual Studio 16 2019」など）
- -DCMAKE_INSTALL_PREFIX : ソースからのインストール先パス


```
 mkdir build
 cd build
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.5-x64-vc16-py314 -G "Visual Studio 18 2026" -DCMAKE_INSTALL_PREFIX=C:/workspace/openrtminstall ..
```

次に以下のコマンドを実行します。 最後に以下のように表示したらビルドは成功です。
```
 cmake --build . --verbose --config Release 
 ビルドに成功しました。
     0 個の警告
     0 エラー
```

ビルドが成功したら、次のコマンドでインストールを完了させます。
```
 cmake --build . --config Release --target install
```

## スクリプトでの一括処理

omniORBのダウンロードからソースビルド、インストールまでを一括処理するスクリプト（OpenRTM-build-Windows.bat）を紹介します。git cloneしたOpenRTM-aistディレクトリ下に置いて実行するものです。

```
 cd OpenRTM-aist
 copy scripts\OpenRTM-build-Windows.bat . 
 OpenRTM-build-Windows.bat > build.log
```

このOpenRTM-build-Windows.batは、Windowsインストーラmsiに組み込むためのビルド時に使用しているものです。
cmake時のオプションで必要なものに絞ってお使い下さい。
