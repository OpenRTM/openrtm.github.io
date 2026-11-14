---
layout: page
title: "openrtm-aistのビルド、動作確認手順"
---
<br>
<a>No English version available.
</a>
<!-- Title: OpenRTM-aistのビルド、動作確認手順 -->
#contents

## Windows+omniORB

### OpenRTM-aistのビルド、インストール

まず、以下の手順でomniORBをビルドしてください。

- [omniORBのビルド]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/omniorb_build#windows)


次にOpenRTM-aistをビルドします。

```
 set OpenRTM_INSTALL_DIR=C:/work/openrtm_install 
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist
 mkdir build
 cd build
 cmake .. -DCMAKE_INSTALL_PREFIX=%OpenRTM_INSTALL_DIR% -DORB_ROOT=%omniORB_DIR%
 cmake --build . --config Release
 cmake --build . --config Release --target install
```

### OpenRTM-aist-Pythonのビルド、インストール
&aname(pythoninstall);

まずは環境変数**PATH**と**PYTHONPATH**を設定します。

- [環境変数の設定]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/omniorb_build#windows_env)

```
 set OpenRTMPython_INSTALL_DIR=C:/work/python_install
 git clone https://github.com/OpenRTM/OpenRTM-aist-Python
 cd OpenRTM-aist-Python
 python setup.py build
 python setup.py install --prefix %OpenRTMPython_INSTALL_DIR%
```


### rtshell、rtctree、rtsprofileのビルド、インストール

環境変数**PATH**と**PYTHONPATH**を設定します。

- [環境変数の設定]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/omniorb_build#windows_env)

```
 git clone https://github.com/OpenRTM/rtctree
 cd rtctree
 python setup.py build
 python setup.py install_lib --install-dir %OpenRTMPython_INSTALL_DIR%\Lib\site-packages
```

```
 git clone https://github.com/OpenRTM/rtsprofile
 cd rtsprofile
 python setup.py build
 python setup.py install_lib --install-dir %OpenRTMPython_INSTALL_DIR%\Lib\site-packages
```

```
 git clone https://github.com/OpenRTM/rtshell
 cd rtshell
 python setup.py build
 python setup.py install --prefix %OpenRTMPython_INSTALL_DIR%
```


インストールが完了したら[環境変数の設定](#windows_env)を行ってください。

## Windows+TAO

### OpenRTM-aistのビルド、インストール

まず、以下の手順でTAOをビルドしてください。

- [TAOのビルド]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/tao_build#windows)


次にOpenRTM-aistをビルドします。

```
 set OpenRTM_INSTALL_DIR=C:/work/openrtm_install
 set PATH=%PATH%;%ACE_ROOT%\lib;
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist
 mkdir build
 cd build
 cmake .. -DCMAKE_INSTALL_PREFIX=%OpenRTM_INSTALL_DIR% -DORB_ROOT=%ACE_ROOT%  -DCORBA=TAO
 cmake --build . --config Release
 cmake --build . --config Release --target install
```

インストールが完了したら[環境変数の設定](#windows_env)を行ってください。

OpenRTM-aist-Python、rtshell、rtctree、rtsprofileはTAOには対応していません。

## Windows共通
### 環境変数の設定
&aname(windows_env);
OpenRTM-aist C++のRTC等を実行するためには環境変数%PATH%を設定する必要があります。

```
 set PATH=%OpenRTM_INSTALL_DIR%\2.0.0\bin\vc16;%OpenRTM_INSTALL_DIR%\2.0.0\omniORB\4.3.0_vc16\bin\x86_win32;%PATH%
```

OpenRTM-aist Python、rtctree、rtsprofileを使うためには環境変数**PYTHONPATH**を設定する必要があります。

```
 set PYTHONPATH=%OpenRTMPython_INSTALL_DIR%\Lib\site-packages;%OpenRTMPython_INSTALL_DIR%\Lib\site-packages\OpenRTM_aist;%OpenRTMPython_INSTALL_DIR%\Lib\site-packages\OpenRTM_aist\RTM_IDL;%PYTHONPATH%
```

rtshellを使うためには環境変数**PATH**の設定が必要です。

```
 set PATH=%OpenRTMPython_INSTALL_DIR%\Scripts;%PATH%
```

### RTCのビルド

外部のRTCをビルドするためには、CMake実行時にOpenRTMConfig.cmakeをインストールしたパスを指定する必要があります。

```
 cmake .. -DOpenRTM_DIR=%OpenRTM_INSTALL_DIR%/2.0.0/cmake
```

#### 環境変数設定スクリプト

OpenRTM-aist C++をインストールすると、環境変数を設定するバッチファイルがインストールされます。

```
 %OpenRTM_INSTALL_DIR%\2.0.0\ext\environment-setup.omniorb.vc16.bat
```

このバッチファイルを実行することで以下の環境変数が設定されます。

<table class="table-alt">
  <tr>
    <th>変数名</th>
    <th>設定値</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>OMNI_ROOT</td>
    <td>%RTM_ROOT%/omniORB/4.3.0_%RTM_VC_VERSION%/</td>
    <td>omniORBをインストールしたフォルダ</td>
  </tr>
  <tr>
    <td>OpenRTM_DIR</td>
    <td>%RTM_ROOT%/cmake</td>
    <td>OpenRTM-aistのCMake設定ファイルをインストールしたフォルダ</td>
  </tr>
  <tr>
    <td>RTM_BASE</td>
    <td>%OpenRTM_INSTALL_DIR%</td>
    <td>OpenRTM-aistをインストールしたフォルダ</td>
  </tr>
  <tr>
    <td>RTM_IDL_DIR</td>
    <td>%RTM_ROOT%/rtm/idl</td>
    <td>OpenRTM-aistのIDLファイルをインストールしたフォルダ</td>
  </tr>
  <tr>
    <td>RTM_ROOT</td>
    <td>%OpenRTM_INSTALL_DIR%/2.0.0</td>
    <td>OpenRTM-aistの2.0.0をインストールしたフォルダ</td>
  </tr>
  <tr>
    <td>RTM_VC_VERSION</td>
    <td>vc**</td>
    <td>ビルドしたVisual Studioのバージョン</td>
  </tr>
  <tr>
    <td>PATH</td>
    <td>%RTM_ROOT%/bin/%RTM_VC_VERSION%;%OMNI_ROOT%/bin/x86_win32;%PATH%</td>
    <td>PATHにOpenRTM-aist、omniORBの実行ファイルのパスを追加</td>
  </tr>
</table>

OpenRTM-aist Python、rtshellの環境変数は設定されません。
Pythonのホームフォルダ(**C:\Python37**等)にインストールした場合は環境変数の設定は不要ですが、それ以外は手動で設定する必要があります。


## Ubuntu+omniORB

まず、以下の手順でomniORBをビルドしてください。

- [omniORBのビルド]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/omniorb_build#ubuntu)

以下の手順で環境変数**PKG_CONFIG**を設定します。

- [環境変数の設定]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/omniorb_build#ubuntu_env)

次にOpenRTM-aistをビルドします。

```
 export OPENRTM_INSTALL_DIR=$OMNIORB_INSTALL_DIR
 export PATH=$OMNIORB_INSTALL_DIR/bin:$PATH
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist
 mkdir build
 cd build
 cmake .. -DCMAKE_INSTALL_PREFIX=$OPENRTM_INSTALL_DIR
 cmake --build . --config Release -- -j$(nproc)
 cmake --build . --config Release --target install
```

### OpenRTM-aist-Pythonのビルド、インストール

まずは環境変数**PATH**と**LD_LIBRARY_PATH**、**PYTHONPATH**を設定します。

- [環境変数の設定]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/omniorb_build#ubuntu_env)

```
 export OPENRTMPYTHON_INSTALL_DIR=$OMNIORB_INSTALL_DIR
 git clone https://github.com/OpenRTM/OpenRTM-aist-Python
 cd OpenRTM-aist-Python
 python3 setup.py build
 python3 setup.py install --prefix $OPENRTMPYTHON_INSTALL_DIR
```

### rtshell、rtctree、rtsprofileのビルド、インストール

環境変数**PATH**と**LD_LIBRARY_PATH**、**PYTHONPATH**を設定します。

- [環境変数の設定]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/omniorb_build#ubuntu_env)

```
 git clone https://github.com/OpenRTM/rtctree
 cd rtctree
 python3 setup.py build
 python3 setup.py install_lib --install-dir $OPENRTMPYTHON_INSTALL_DIR/lib/python3.6/site-packages
```

```
 git clone https://github.com/OpenRTM/rtsprofile
 cd rtsprofile
 python3 setup.py build
 python3 setup.py install_lib --install-dir $OPENRTMPYTHON_INSTALL_DIR/lib/python3.6/site-packages
```

```
 git clone https://github.com/OpenRTM/rtshell
 cd rtshell
 python3 setup.py build
 python3 setup.py install --prefix $OPENRTMPYTHON_INSTALL_DIR
```

インストールが完了したら[環境変数の設定](#ubuntu_env)を行ってください。

## Ubuntu+TAO

### OpenRTM-aistのビルド、インストール

まず、以下の手順でTAOをビルドしてください。

- [TAOのビルド]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/tao_build#ubuntu)


以下の手順で環境変数**PKG_CONFIG**を設定します。

- [環境変数の設定]({{ site.baseurl }}/en/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build/tao_build#ubuntu_env)

次にOpenRTM-aistをビルドします。

```
 export OPENRTM_INSTALL_DIR=$ACE_INSTALL_DIR
 export LD_LIBRARY_PATH=ACE_INSTALL_DIR/lib:$LD_LIBRARY_PATH
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist
 mkdir build
 cd build
 cmake .. -DCMAKE_INSTALL_PREFIX=$OPENRTM_INSTALL_DIR -DCORBA=TAO
 cmake --build . --config Release -- -j$(nproc)
 cmake --build . --config Release --target install
```

インストールが完了したら[環境変数の設定](#ubuntu_env)を行ってください。

OpenRTM-aist-Python、rtshell、rtctree、rtsprofileはTAOには対応していません。

## Ubuntu共通
### 環境変数の設定
&aname(ubuntu_env);
OpenRTM-aist C++のRTC等を実行するためには環境変数**PATH**、**LD_LIBRARY_PATH**を設定する必要があります。

```
 export PATH=$OPENRTM_INSTALL_DIR/bin:$PATH
 export LD_LIBRARY_PATH=$OPENRTM_INSTALL_DIR/lib:$LD_LIBRARY_PATH
```


OpenRTM-aist Python、rtctree、rtsprofileを使うためには環境変数**PYTHONPATH**を設定する必要があります。

```
 export PYTHONPATH=$OPENRTM_INSTALL_DIR/lib/python3.6/site-packages:$OPENRTM_INSTALL_DIR/lib/python3.6/site-packages/OpenRTM_aist:$OPENRTM_INSTALL_DIR/lib/python3.6/site-packages/OpenRTM_aist/RTM_IDL:$PYTHONPATH
```

rtshellを使うためには環境変数**PATH**の設定が必要です。

```
 export PATH=$OPENRTMPYTHON_INSTALL_DIR/bin:$PATH
```

omniORBやOpenRTM-aist等をインストールしたパスが同じ場合は以下のコマンドだけ実行します。

```
 export PATH=$OPENRTM_INSTALL_DIR/bin:$PATH
 export LD_LIBRARY_PATH=$OPENRTM_INSTALL_DIR/lib:$LD_LIBRARY_PATH
 export PYTHONPATH=$OPENRTM_INSTALL_DIR/lib/python3.6/site-packages:$OPENRTM_INSTALL_DIR/lib/python3.6/site-packages/OpenRTM_aist:$OPENRTM_INSTALL_DIR/lib/python3.6/site-packages/OpenRTM_aist/RTM_IDL:$PYTHONPATH
```

#### 環境変数設定スクリプト

OpenRTM-aist C++をインストールすると、環境変数を設定するバッチファイルがインストールされます。

```
 source ${OpenRTM_INSTALL_DIR}/etc/environment-setup.sh
```

このバッチファイルを実行することで以下の環境変数が設定されます。

<table class="table-alt">
  <tr>
    <th>変数名</th>
    <th>設定値</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>OpenRTM_DIR</td>
    <td>${OpenRTM_INSTALL_DIR}/lib/openrtm-2.0/cmake</td>
    <td>OpenRTM-aistのCMake設定ファイルをインストールしたフォルダ</td>
  </tr>
  <tr>
    <td>RTM_IDL_DIR</td>
    <td>${OpenRTM_INSTALL_DIR}/include/openrtm-2.0/rtm/idl</td>
    <td>OpenRTM-aistのIDLファイルをインストールしたフォルダ</td>
  </tr>
  <tr>
    <td>PATH</td>
    <td>${OpenRTM_INSTALL_DIR}/bin:$PATH</td>
    <td>PATHにOpenRTM-aist、omniORBの実行ファイルのパスを追加</td>
    <td>]</td>
  </tr>
  <tr>
    <td>LD_LIBRARY_PATH</td>
    <td>${OpenRTM_INSTALL_DIR}/lib:$LD_LIBRARY_PATH</td>
    <td>PATHにOpenRTM-aist、omniORBの実行ファイルのパスを追加</td>
  </tr>
</table>

OpenRTM-aist Python、rtshellの環境変数は設定されません。
Pythonのホームフォルダ(**C:\Python37**等)にインストールした場合は環境変数の設定は不要ですが、それ以外は手動で設定する必要があります。


### RTCのビルド

外部のRTCをビルドするためには、CMake実行時にOpenRTMConfig.cmakeをインストールしたパスを指定する必要があります。

```
 cmake .. -DOpenRTM_DIR=${OPENRTM_INSTALL_DIR}/lib/openrtm-2.0/cmake
```




