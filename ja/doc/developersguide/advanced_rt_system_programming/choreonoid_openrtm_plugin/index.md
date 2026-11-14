---
layout: page
title: "choreonoid openrtmプラグインの利用方法"
---

<!-- Choreonoid OpenRTMプラグインの利用方法 -->
#contents
Choreonoidはオープンソースのロボット用シミュレーションソフトウェアです。
拡張性が高く、物理エンジン、通信機能、スクリプティング機能、制御アルゴリズム等をC++プラグインとして追加できます。

- [Choreonoid ホームページ](https://choreonoid.org/ja/)

Choreonoid用OpenRTMプラグインはChoreonoid上でRTCを起動し、シミュレータ上のオブジェクトのトルクや速度、ビジョンセンサやレーザーレンジセンサ等の入出力をポートの入出力と関連付けたRTCを作成できます。
これにより外部のRTCとChoreonoidの入出力が連携し、RTCの再利用によるシミュレータ実行の効率化、シミュレータ環境から実機環境へシームレスに移行できます。

<div align="center"><a href="choreonoid1_1.png"><img src="choreonoid1_1.png" width="80%;"></a></div>

このページではOpenRTMプラグインのインストール手順について説明します。




## ビルド手順
OpenRTMプラグインは現在OpenRTM-aist 1.2.2以前のバージョンのサポートを終了しています。
OpenRTM-aist 2.0.0以上のバージョンのインストールが必要です。

### Windows
#### OpenRTM-aistのビルドとインストール

OpenRTM-aist+omniORBを以下の手順でビルド、インストールしてください。
※インストーラーでOpenRTM-aistをインストールしている場合は不要。

- [OpenRTM-aist(C++版)のCMakeによるビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build#windowsomniorb)

ただし、CMake実行時にOpenRTM-aistのインストールフォルダは指定してそこにインストールするようにしてください。

```
 set OPENRTM_INSTALL_DIR=C:/work/openrtm_install
 set OMNIORB_SOURCE_DIR=C:/workspace/omniORB-4.2.5-x64-vc14-py310
 cmake .. -DORB_ROOT=%OMNIORB_SOURCE_DIR% -DCMAKE_INSTALL_PREFIX=%OPENRTM_INSTALL_DIR%
 cmake --build . --config Release
 cmake --build . --config Release --target install
```

またOpenSSLのヘッダーファイル、ライブラリを適当な場所に展開してください。

- https://openrtm.org/pub/OpenSSL/1.1.0/

#### Choreonoidのビルドとインストール

Choreonoidを以下の手順でビルド、インストールしてください。

- [ソースコードからのビルドとインストール (Windows編)](https://choreonoid.org/ja/documents/latest/install/build-windows.html)

CMake、Boost、Qtのバージョンには注意してください。

- CMakeのバージョンが古い場合、Boostをライブラリを検出できない場合があります。できるだけ最新版をインストールしてください。
- Boostはデフォルトの設定で**C:\local\boost_1_77_0**のようなフォルダにインストールされますが、CMakeは**C:\local\boost_{バージョン番号}**からBoostを探すため、古いバージョンがすでに**C:\local\**以下にインストールされている場合にそちらを検出する事があるので注意してください。

OpenRTMプラグインの使用のためにはCORBAプラグインのビルドに、ヘッダーファイルなどの各種ファイルをインストールが必要です。
また、OpenRTM Pythonプラグインの使用のためにはPythonプラグインのビルドが必要です。

<table class="table-alt">
  <tr>
    <th>設定項目</th>
    <th>内容</th>
    <th>設定例</th>
  </tr>
  <tr>
    <td>ENABLE_CORBA</td>
    <td>CORBA通信機能の有効化、無効化</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>BUILD_CORBA_PLUGIN</td>
    <td>CORBAプラグインのビルドの有無</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>CHOREONOID_OMNIORB_DIR</td>
    <td>omniORBのインストールフォルダのパス</td>
    <td>**'C:/work/openrtm_install/2.0.0/omniORB/4.2.5_vc16**'</td>
  </tr>
  <tr>
    <td>INSTALL_SDK</td>
    <td>ヘッダーファイルなどの各種ファイルをインストールするか</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>ENABLE_PYTHON</td>
    <td>Pythonスクリプティング機能、およびPythonプラグインのビルドの有無</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>CMAKE_INSTALL_PREFIX</td>
    <td>Choreonoidのインストールフォルダ</td>
    <td>**'C:/work/choreonoid_install**'</td>
  </tr>
</table>


**CHOREONOID_OMNIORB_DIR**については環境変数OMNI_ROOTを設定していると自動でomniORBを検出しますが、Choreonoidが生成するCMakeコンフィグファイルの問題でOpenRTMプラグインのビルドでエラーが発生することがあるので必ず手動でパスを設定してください。
またPythonプラグインのビルドのため、Pythonをインストールしてください。

コマンドでは以下のように入力できます。

```
 set CHOREONOID_INSTALL_DIR=C:/work/choreonoid_install
 Invoke-WebRequest -Uri https://github.com/choreonoid/choreonoid/archive/refs/tags/v1.7.0.zip -OutFile choreonoid-1.7.0.zip
 Expand-Archive -Path choreonoid-1.7.0.zip -DestinationPath .
 Rename-Item choreonoid-1.7.0 choreonoid
 cd choreonoid
 mkdir build
 cd build
 cmake .. -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DINSTALL_SDK=ON -DCHOREONOID_OMNIORB_DIR=%OPENRTM_INSTALL_DIR%/2.0.0/omniORB/4.2.5_vc16 -DENABLE_PYTHON=ON -DCMAKE_INSTALL_PREFIX=%CHOREONOID_INSTALL_DIR%
 cmake --build . --config Release
 cmake --build . --config Release --target install
```

※[choreonoidのリポジトリ](https://github.com/choreonoid/choreonoid)のmasterブランチのソースコードに不具合があり、WindowsでのCorbaPluginのビルドでエラーが発生します。masterブランチのソースコードを使う場合、**src/CorbaPlugin/CorbaPlugin.cpp**の以下の部分を修正してください。

```
 nameServerProcess.start(QString("\"") + command.c_str() + "\""); //修正前
 
 nameServerProcess.start(QString("\"") + command.c_str() + "\"", QStringList()); //修正後
```

※OpenRTM-aistをインストーラーでインストールした場合はCHOREONOID_OMNIORB_DIRオプションの設定は不要です。

#### OpenRTMプラグインのビルドとインストール

OpenRTMプラグインのソースコードは以下から入手できます。

- [choreonoid-openrtm](https://github.com/OpenRTM/choreonoid-openrtm)

Choreonoidと同様、CMake実行後にVisual Studioでビルドします。

CMakeでは以下の項目を設定します。

<table class="table-alt">
  <tr>
    <th>設定項目</th>
    <th>内容</th>
    <th>設定例</th>
  </tr>
  <tr>
    <td>Choreonoid_DIR</td>
    <td>ChoreonoidのCMakeコンフィグファイルがインストールされたフォルダ</td>
    <td>**'C:/work/choreonoid_install/share/choreonoid/cmake**'</td>
  </tr>
  <tr>
    <td>OpenRTM_DIR</td>
    <td>OpenRTM-aistのCMakeコンフィグファイルがインストールされたフォルダ</td>
    <td>**'C:/work/openrtm_install/2.0.0/cmake**'</td>
  </tr>
</table>

以下のコマンドを実行することでビルド、インストールができます。
生成したOpenRTMプラグインはChoreonoidのインストールフォルダにコピーされます。

```
 git clone https://github.com/OpenRTM/choreonoid-openrtm
 cd choreonoid-openrtm
 mkdir build
 cd build
 cmake .. -DChoreonoid_DIR=%CHOREONOID_INSTALL_DIR%/share/choreonoid/cmake -DOpenRTM_DIR=%OPENRTM_INSTALL_DIR%/2.0.0/cmake
 cmake --build . --config Release
 cmake --build . --config Release --target install
```

※OpenRTM-aistをインストーラーでインストールした場合はOpenRTM_DIRオプションの設定は不要です。

#### OpenRTM Pythonプラグインのビルドとインストール

OpenRTMプラグインのソースコードは以下から入手できます。

- [OpenRTMPythonPlugin](https://github.com/Nobu19800/OpenRTMPythonPlugin)

CMakeの設定項目はOpenRTMプラグインと同じです。

以下のコマンドを実行することでビルド、インストールができます。

```
 git clone https://github.com/Nobu19800/OpenRTMPythonPlugin
 cd OpenRTMPythonPlugin
 mkdir build
 cd build
 cmake .. -DChoreonoid_DIR=%CHOREONOID_INSTALL_DIR%/share/choreonoid/cmake -DOpenRTM_DIR=%OPENRTM_INSTALL_DIR%/2.0.0/cmake
 cmake --build . --config Release
 cmake --build . --config Release --target install
```

※OpenRTM-aistをインストーラーでインストールした場合はOpenRTM_DIRオプションの設定は不要です。

#### 必要なファイル一式をまとめる

Choreonoidをビルド、インストールすると、基本的には必要なファイルはインストール先にコピーされます。
ただし、Pythonプラグインをビルドする場合は、対応するバージョンのPythonがインストールされている必要があります。

このため、対応するバージョンのPythonがインストールされていない場合は、以下のページのように組み込み用Pythonを同梱する必要があります。

- [WindowsでPython3.7の実行環境を手早く作る方法](https://qiita.com/hirohiro77/items/377dfc0a264acb3db222)


まずは、対応するバージョンの**python-3.x.y-embed-amd64**をダウンロードしてください。

- https://www.python.org/ftp/python/

次に必要なライブラリをインストールします。
Choreonoidはnumpyが必要なためインストールします。

```
 python -m pip install numpy
```

また、Choreonoid Pythonプラグインのサンプルプログラムを実行するためにPySDL2が必要なためインストールします。

```
 python -m pip install pysdl2 pysdl2-dll
```

omniORB、OpenRTM-aistをインストールする必要があるため、以下のファイル、フォルダを**python-3.x.y-embed-amd64/Lib/site-packages**以下のコピーしてください。

- CosNaming
- omniidl
- omniidl_be
- omniORB
- OpenRTM_aist
- OpenRTM-aist.pth
- CORBA.py
- CosNaming_idl.py
- CosNaming__POA
- PortableServer.py
- PortableServer__POA.py
- _omnicodesets.pyd
- _omniConnMgmt.pyd
- _omnihttpCrypto.pyd
- _omnihttpTP.pyd
- _omnipy.pyd
- _omnisslTP.pyd


### Ubuntu
#### OpenRTM-aistのビルドとインストール

OpenRTM-aist+omniORBを以下の手順でビルド、インストールしてください。

- [OpenRTM-aist(C++版)のCMakeによるビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build#ubuntuomniorb)

```
 export OPENRTM_INSTALL_PATH=~/work/openrtm_install
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist/
 mkdir build
 cd build/
 git clone 
 cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$OPENRTM_INSTALL_PATH
 cmake --build . --config Release
 sudo cmake --build . --config Release --target install
```


#### Choreonoidのビルドとインストール

Choreonoidを以下の手順でビルド、インストールしてください。

- [ソースコードからのビルドとインストール (Windows編)](https://choreonoid.org/ja/documents/latest/install/build-windows.html)

CMake、Boost、Qtのバージョンには注意してください。

- CMakeのバージョンが古い場合、Boostをライブラリを検出できない場合があります。できるだけ最新版をインストールしてください。
- Boostはデフォルトの設定で**C:\local\boost_1_77_0**のようなフォルダにインストールされますが、CMakeは**C:\local\boost_{バージョン番号}**からBoostを探すため、古いバージョンがすでに**C:\local\**以下にインストールされている場合にそちらを検出する事があるので注意してください。

OpenRTMプラグインの使用のためにはCORBAプラグインのビルドに、ヘッダーファイルなどの各種ファイルをインストールが必要です。
また、OpenRTM Pythonプラグインの使用のためにはPythonプラグインのビルドが必要です。

<table class="table-alt">
  <tr>
    <th>設定項目</th>
    <th>内容</th>
    <th>設定例</th>
  </tr>
  <tr>
    <td>ENABLE_CORBA</td>
    <td>CORBA通信機能の有効化、無効化</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>BUILD_CORBA_PLUGIN</td>
    <td>CORBAプラグインのビルドの有無</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>INSTALL_SDK</td>
    <td>ヘッダーファイルなどの各種ファイルをインストールするか</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>ENABLE_PYTHON</td>
    <td>Pythonスクリプティング機能、およびPythonプラグインのビルドの有無</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>CMAKE_INSTALL_PREFIX</td>
    <td>Choreonoidのインストールフォルダ</td>
    <td>'/work/choreonoid_install'</td>
  </tr>
</table>

```
 export CHOREONOID_INSTALL_DIR=~/work/choreonoid_install
 git clone https://github.com/choreonoid/choreonoid
 cd choreonoid
 mkdir build
 cd build
 cmake .. -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DINSTALL_SDK=ON  -DENABLE_PYTHON=ON -DCMAKE_INSTALL_PREFIX=$CHOREONOID_INSTALL_DIR
 cmake --build . --config Release
 cmake --build . --config Release --target install
```



#### OpenRTMプラグインのビルドとインストール

OpenRTMプラグインのソースコードは以下から入手できます。

- [choreonoid-openrtm](https://github.com/OpenRTM/choreonoid-openrtm)


CMakeでは以下の項目を設定します。

<table class="table-alt">
  <tr>
    <th>設定項目</th>
    <th>内容</th>
    <th>設定例</th>
  </tr>
  <tr>
    <td>Choreonoid_DIR</td>
    <td>ChoreonoidのCMakeコンフィグファイルがインストールされたフォルダ</td>
    <td>`/work/choreonoid_install/share/choreonoid/cmake`</td>
  </tr>
  <tr>
    <td>OpenRTM_DIR</td>
    <td>OpenRTM-aistのCMakeコンフィグファイルがインストールされたフォルダ</td>
    <td>`/work/openrtm_install/lib/openrtm-2.0/cmake`</td>
  </tr>
</table>

以下のコマンドを実行することでビルド、インストールができます。
生成したOpenRTMプラグインはChoreonoidのインストールフォルダにコピーされます。

```
 git clone https://github.com/OpenRTM/choreonoid-openrtm
 cd choreonoid-openrtm
 mkdir build
 cd build
 cmake .. -DChoreonoid_DIR=$CHOREONOID_INSTALL_DIR/share/choreonoid/cmake -DOpenRTM_DIR=$OPENRTM_INSTALL_PATH/lib/openrtm-2.0/cmake
 cmake --build . --config Release
 cmake --build . --config Release --target install
```


#### OpenRTM Pythonプラグインのビルドとインストール

OpenRTMプラグインのソースコードは以下から入手できます。

- [OpenRTMPythonPlugin](https://github.com/Nobu19800/OpenRTMPythonPlugin)

CMakeの設定項目はOpenRTMプラグインと同じです。

以下のコマンドを実行することでビルド、インストールができます。

```
 git clone https://github.com/Nobu19800/OpenRTMPythonPlugin
 cd OpenRTMPythonPlugin
 mkdir build
 cd build
 cmake .. -DChoreonoid_DIR=$CHOREONOID_INSTALL_DIR/share/choreonoid/cmake -DOpenRTM_DIR=$OPENRTM_INSTALL_PATH/lib/openrtm-2.0/cmake
 cmake --build . --config Release
 cmake --build . --config Release --target install
```

## 使用方法

使用方法については以下のページを参考にしてください。

- [OpenRTMプラグイン](https://choreonoid.org/ja/documents/1.7/openrtm/index.html)
- [Choreonoid用OpenRTM連携プラグイン Python版 マニュアル]({{ site.baseurl }}/ja/content/choreonoid_openrtm_python_manual)

<hr>
- [Choreonoid入門](./tutorial)
- [myCobot280の制御](./tutorial_serviceport)

