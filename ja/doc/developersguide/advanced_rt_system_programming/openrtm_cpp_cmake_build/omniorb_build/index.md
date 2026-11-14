---
layout: page
title: "omniorbのビルド"
---
<!-- Title: omniORBのビルド -->
#contents

## Windows

### omniORBのビルド

&aname(windows);

ビルドにはPython、Cygwinのインストールが必要です。

- [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
- [https://www.cygwin.com/](https://www.cygwin.com/)

sslTp、httpTp機能を使う場合はOpenSSLのビルドが必要です。

- [https://github.com/openssl/openssl/tags](https://github.com/openssl/openssl/tags)

Strawberry Perlをインストールして以下のコマンドを実行する。

```
 set OPENSSL_INSTALL_DIR=C:/work/openssl_install
 call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
 perl Configure VC-WIN64A --prefix=%OPENSSL_INSTALL_DIR% no-asm shared
 nmake install
```

omniORBのソースコードを入手します。

- [https://sourceforge.net/projects/omniorb/files/omniORB/](https://sourceforge.net/projects/omniorb/files/omniORB/)

**mk/platforms/x86_win32_vs_16.mk**でPython、OpenSSLのパスを設定します。**OPEN_SSL_ROOT**を設定しなかった場合でもビルドは可能ですが、sslTp、httpTp機能は使えません。

```
 PYTHON = /cygdrive/c/Python310/python
```

```
 OPEN_SSL_ROOT = /cygdrive/c/work/openssl_install
```

**config/config.mk**でビルドする環境を指定してください。

```
 platform = x86_win32_vs_16
```

omniORBを展開したフォルダに移動して以下のコマンドを実行してください。

```
 set PATH=C:\cygwin64\bin;%PATH%;
 call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
 cd src
 make export
```

次にomniORBpyのビルドを実行します。
まずomniORBpyのソースコードを入手してください。

- [https://sourceforge.net/projects/omniorb/files/omniORBpy/](https://sourceforge.net/projects/omniorb/files/omniORBpy/)

omniORBpyをomniORBの**src/lib**以下にコピーします。

```
 omniORB-4.x.y
    |--src
    |  |--lib
    |    |--omniORBpy
    |--mk
    |  |--platforms
    |    |--x86_win32_vs_16
    |--config
      |--config.mk
```
omniORBpyフォルダに移動してmakeコマンドを実行します。

```
 cd lib\omniORBpy
 make export
```

### 環境変数の設定

&aname(windows_env);

omniORB、omniORBpyの動作確認をするためには環境変数**PATH**、**PYTHONPATH**の設定が必要です。

```
 set omniORB_DIR=C:/workspace/omniORB-4.3.0
 set PATH=%omniORB_DIR%\bin\x86_win32;%PATH%
 set PYTHONPATH=%omniORB_DIR%\lib\x86_win32;%omniORB_DIR%\lib\python;%PYTHONPATH%
```

## Ubuntu

### omniORBのビルド

&aname(ubuntu);

sslTp、httpTp機能を使う場合はOpenSSLのインストールが必要です。

```
 sudo apt install libssl-dev
```

次にomniORBのソースコードを入手してビルドします。

```
 export PYTHON=/usr/bin/python3
 export OMNIORB_INSTALL_DIR=~/work/omniorb_install
 wget https://jaist.dl.sourceforge.net/project/omniorb/omniORB/omniORB-4.3.0/omniORB-4.3.0.tar.bz2
 tar xf omniORB-4.3.0.tar.bz2
 cd omniORB-4.3.0
 ./configure --prefix=${OMNIORB_INSTALL_DIR} --with-openssl
 make
 make install
```

omniORBpyのビルドを実行します。

```
 export PYTHON=/usr/bin/python3
 wget https://jaist.dl.sourceforge.net/project/omniorb/omniORBpy/omniORBpy-4.3.0/omniORBpy-4.3.0.tar.bz2
 tar xf omniORBpy-4.3.0.tar.bz2
 cd omniORBpy-4.3.0
 ./configure --with-omniorb=${OMNIORB_INSTALL_DIR} --prefix=${OMNIORB_INSTALL_DIR} --with-openssl
 make
 make install
```


### 環境変数の設定

&aname(ubuntu_env);

omniORB、omniORBpyの動作確認をするためには環境変数**PATH**、**LD_LIBRARY_PATH**、**PYTHONPATH**の設定が必要です。

```
 export PATH=${OMNIORB_INSTALL_DIR}/bin:$PATH
 export LD_LIBRARY_PATH=${OMNIORB_INSTALL_DIR}/lib:${LD_LIBRARY_PATH}
 export PYTHONPATH=${OMNIORB_INSTALL_DIR}/lib/python3.6/site-packages:$PYTHONPATH
```

また、pkg-configでomniORBを検出するには以下のように環境変数**PKG_CONFIG**を設定する。

```
 export PKG_CONFIG_PATH=${OMNIORB_INSTALL_DIR}/lib/pkgconfig:$PKG_CONFIG_PATH
```



