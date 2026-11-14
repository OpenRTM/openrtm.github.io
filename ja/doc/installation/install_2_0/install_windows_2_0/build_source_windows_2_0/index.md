---

layout: page
Title: ソースからのビルド（C++版）

---

<!-- Title: ソースからのビルド（C++版） -->


OpenRTM-aist本体に改修を加えてWindows上で利用したい場合は、OpenRTM-aistのソースコードを取得してビルドできます。　2.0系からはCMakeに対応しましたので、1.2系までの手順とは異なっています。


#contents


<!-- ------------------------------------------------------------ -->
## 必要なソフトウエア・ライブラリ

以下のソフトウエアが必要です。詳細は [OpenRTM-aist 2.0系のWindowsへのインストール]({{ site.baseurl }}/ja/doc/installation/install_2_0/install_windows_2_0/install_2_0) をご覧ください。

- Visual Studio
- Python
- CMake
- Doxygen & Graphviz（ドキュメントビルドも行いたい場合）

また、omniORBライブラリも必要です。
- omniORB 4.2.5 (2022/06現在）

openrtm.org が提供するビルド済みバイナリパッケージを下記リンク先に omniORB-4.2.5-x64-vc14-pyXX.zip という名称で用意してあります。
XXをインストールするpythonのバージョンに読み替えて適切なものをダウンロードし、適当な場所(以下の説明ではC:\workspace\omniORBとしています)に展開してください。

- [openrtm.org提供バイナリパッケージ](https://openrtm.org/pub/omniORB/win32/omniORB-4.2.5/)

他のライブラリを使ってのビルドについては、 [RTシステム開発 (応用編)・OpenRTM-aist(C++版)のCMakeによるビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build) をご覧ください。

## ビルド・インストール時のコマンド手順

ソースコード を入手します。OpenRTM-aist2.0系の最新ソースならばmasterブランチを、2.0.0版のリリースソースでしたらv2.0.0のタグをチェックアウトしてください。 <br>

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist
 git checkout -b v200-src refs/tags/v2.0.0
```


CMakeオプションで以下を指定して実行します。
- -DORB_ROOT : ダウンロード・展開したomniORBのパス
- -G : Visual Studio のバージョン（「Visual Studio 17 2022」「Visual Studio 16 2019」など）
- -DCMAKE_INSTALL_PREFIX : ソースからのインストール先パス


```
 mkdir build
 cd build
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.5-x64-vc14-py310 -G "Visual Studio 17 2022" -DCMAKE_INSTALL_PREFIX=C:/workspace/openrtminstall ..
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

omniORBのダウンロードからソースビルド、インストールまでを一括処理するスクリプト（cxx_src_build.bat）を紹介します。git cloneしたOpenRTM-aistディレクトリ下に置いて実行するものです。

```
 cd OpenRTM-aist
 cxx_src_build.bat > 1.log
```

スクリプト実行時、「Visual Studioのバージョン」「Pythonのバージョン」「インストール先」の3項目だけ環境に合わせて指定してください。

```
 set CMAKE_GENERATOR="Visual Studio 16 2019"
 set PY_VERSION=39　・・・ 37, 38, 39, 310 のいずれかを指定
 set INSTALL_PREFIX=C:\localRTM-test
```

### cxx_src_build.bat

```
 @echo off
 @rem
 @rem ---------- 環境に合わせる  ここから -------
 set CMAKE_GENERATOR="Visual Studio 16 2019"
 set PY_VERSION=39
 set INSTALL_PREFIX=C:\localRTM-test
 @rem ---------- 環境に合わせる  ここまで -------
 set OMNI_VERSION=4.2.5
 set VC_VERSION=vc14
 if exist %INSTALL_PREFIX% rmdir /s/q %INSTALL_PREFIX%
 @rem
 @rem パス中の "\" を "/" に変換する
 set current_dir=%~dp0
 set RTM_ROOT=%current_dir:\=/%
 set INSTALL_PREFIX=%INSTALL_PREFIX:\=/%
 @rem
 @rem omniORB download
 set base_omni_url="https://openrtm.org/pub/omniORB/win32/omniORB-%OMNI_VERSION%/"
 set OMNIORB_DIR=omniORB-%OMNI_VERSION%-x64-%VC_VERSION%-py%PY_VERSION%
 set OMNIORB_ZIP=%OMNIORB_DIR%.zip
 set OMNIORB_URL=%base_omni_url%/%OMNIORB_ZIP%
 if not exist %OMNIORB_ZIP% (
   powershell wget -O %OMNIORB_ZIP% %OMNIORB_URL%
 )
 if exist %OMNIORB_DIR% rmdir /s/q %OMNIORB_DIR%
 powershell Expand-Archive .\%OMNIORB_ZIP% -DestinationPath .\\
 
 set OMNIORB_ROOT=%RTM_ROOT%/%OMNIORB_DIR%
 @rem
 @rem set cmake parameter
 set CMAKE_OPT=-DORB_ROOT=%OMNIORB_ROOT% ^
```
   -DCMAKE_INSTALL_PREFIX=%INSTALL_PREFIX% ^
   -G %CMAKE_GENERATOR% ^
   -A x64 ..
```
 call :CMAKE_Release
 exit /b
 @rem
```
 :CMAKE_Release
```
 if exist build-release rmdir /s/q build-release
 mkdir build-release
 cd build-release
 cmake %CMAKE_OPT% 
 cmake --build . --verbose --config Release
 cmake --install .
 cd ..
 exit /b
```

## 参考：msi生成用ビルドスクリプト

msiに組み込むmsm（vc2019, 2022向け） 作成用ビルドスクリプトです。以下を利用しています。
- Boostライブラリ 1.78.0
- OpenSSL 3.0.1
- Fluent Bit v1.8.9 をソースからビルド

OpenRTM-aistは Release/Debug 両ビルドをしています。omniORBのバイナリはvc14でビルドしたバイナリを使用して問題ないが、vc16用バイナリを用意して使用しています。

```
 @echo off
 @rem
 set CMAKE_GENERATOR="Visual Studio 16 2019"
 set VC_VERSION=vc16
 set SSL_VC_VERSION=vc14
 set PY_VERSION=39
 set INSTALL_PREFIX=C:\localRTM
 set OMNI_VERSION=4.2.5
 set SSL_VERSION=3.0.1
 set BOOST_PATH=C:\local\boost_1_78_0
 set FLB_ROOT=C:\localFLB
 @rem
 if exist %INSTALL_PREFIX% rmdir /s/q %INSTALL_PREFIX%
 @rem ------------
 @rem パス中の "\" を "/" に変換する
 set current_dir=%~dp0
 set RTM_ROOT=%current_dir:\=/%
 set BOOST_PATH=%BOOST_PATH:\=/%
 set INSTALL_PREFIX=%INSTALL_PREFIX:\=/%
 set FLB_ROOT=%FLB_ROOT:\=/%
 @rem ------------
 @rem omniORB download
 set base_omni_url="https://openrtm.org/pub/omniORB/win32/omniORB-%OMNI_VERSION%/"
 set OMNIORB_DIR=omniORB-%OMNI_VERSION%-x64-%VC_VERSION%-py%PY_VERSION%
 set OMNIORB_ZIP=%OMNIORB_DIR%.zip
 set OMNIORB_URL=%base_omni_url%/%OMNIORB_ZIP%
 if not exist %OMNIORB_ZIP% (
   powershell wget -O %OMNIORB_ZIP% %OMNIORB_URL%
 )
 if exist %OMNIORB_DIR% rmdir /s/q %OMNIORB_DIR%
 powershell Expand-Archive .\%OMNIORB_ZIP% -DestinationPath .\\
```

```
 set OMNIORB_ROOT=%RTM_ROOT%/%OMNIORB_DIR%
 @rem ------------
 @rem OpenSSL download
 set base_ssl_url="https://openrtm.org/pub/OpenSSL/%SSL_VERSION%"
 set OPENSSL_ZIP=openssl-%SSL_VERSION%-win64-%SSL_VC_VERSION%.zip
 set OPENSSL_URL=%base_ssl_url%/%OPENSSL_ZIP%
 if not exist %OPENSSL_ZIP% (
   powershell wget -O %OPENSSL_ZIP% %OPENSSL_URL%
 )
 if exist OpenSSL rmdir /s/q OpenSSL
 powershell Expand-Archive .\%OPENSSL_ZIP% -DestinationPath .\\
```

```
 set SSL_ROOT=%RTM_ROOT%OpenSSL/build
 @rem ------------
 @rem set cmake parameter
 set CMAKE_OPT=-DRTM_VC_VER=%VC_VERSION% ^
```
   -DORB_ROOT=%OMNIORB_ROOT% ^
   -DCORBA=omniORB ^
   -DSSL_ENABLE=ON ^
   -DOPENSSL_ROOT=%SSL_ROOT% ^
   -DCMAKE_INSTALL_PREFIX=%INSTALL_PREFIX% ^
   -DWINDOWS_MSM_BUILD=ON ^
   -DBOOST_ROOT=%BOOST_PATH% ^
   -DFLUENTBIT_ENABLE=ON ^
   -DFLUENTBIT_ROOT=%FLB_ROOT% ^
   -G %CMAKE_GENERATOR% ^
   -A x64 ..
```
 call :CMAKE_Debug
 call :CMAKE_Release
 exit /b
 @rem ------------
```
 :CMAKE_Release
```
 if exist build-release rmdir /s/q build-release
 mkdir build-release
 cd build-release
 cmake %CMAKE_OPT% 
 cmake --build . --verbose --config Release
 cmake --install .
 cd ..
 exit /b
 @rem ------------
```
 :CMAKE_Debug
```
 if exist build-debug rmdir /s/q build-debug
 mkdir build-debug
 cd build-debug
 cmake %CMAKE_OPT%
 cmake --build . --verbose --config Debug
 cmake --install . --config Debug
 cd ..
 exit /b
```





