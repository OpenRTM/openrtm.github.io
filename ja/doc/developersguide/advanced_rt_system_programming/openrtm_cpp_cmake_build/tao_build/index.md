---
layout: page
title: "taoのビルド"
---
<!-- Title: TAOのビルド -->
#contents

## Windows
&aname(windows);
### ACE+TAOのビルド

以下から ACE+TAO.zip をダウンロードしてください。

- [http://download.dre.vanderbilt.edu](http://download.dre.vanderbilt.edu)
- [https://github.com/DOCGroup/ACE_TAO/releases](https://github.com/DOCGroup/ACE_TAO/releases)

Visual Studio で ACE と TAO のビルドをします。

ACE+TAO.zip を展開したフォルダーの **ace/config-win32.h** を **ace/config.h** に変更してください。

ACE_vs2019.sln (もしくは ACE_vs2017.sln)を Visual Studio で開いてビルドしてください。
64bitの場合はソリューションプラットフォームがWin32となっている部分をx64に変更してください。

次に以下の環境変数を設定した状態でTAO_vs2019.sln (もしくは TAO_vs2017.sln)を Visual Studio で開いてビルドしてください。

<table class="table-alt">
  <tr>
    <th>環境変数</th>
    <th>内容</th>
    <th>設定例</th>
  </tr>
  <tr>
    <td>ACE_ROOT</td>
    <td>ACE_wrappersを展開したフォルダのパス</td>
    <td>C:/work/ACE_wrappers</td>
  </tr>
</table>

```
 cd TAO
 set ACE_ROOT=C:/work/ACE_wrappers
 TAO_vs2019.sln
```


## Ubuntu
&aname(ubuntu);
### ACE+TAOのビルド

ACE+TAO.tar.gzを入手して以下のコマンドでビルドします。

```
 export ACE_INSTALL_DIR=~/work/ace_install
 sudo apt-get install gperf
 export ACE_ROOT=${PWD}/ACE_wrappers/build/linux
 export TAO_ROOT=${ACE_ROOT}/TAO
 export LD_LIBRARY_PATH=$ACE_ROOT/ace:$ACE_ROOT/lib
 export INSTALL_PREFIX=$ACE_INSTALL_DIR
 wget https://github.com/DOCGroup/ACE_TAO/releases/download/ACE%2BTAO-7_0_6/ACE+TAO-7.0.6.tar.gz
 tar xf ACE+TAO-7.0.6.tar.gz
 cd ACE_wrappers
 mkdir -p build/linux
 ./bin/create_ace_build build/linux
 echo '#include "ace/config-linux.h"' > build/linux/ace/config.h
 echo 'include $(ACE_ROOT)/include/makeinclude/platform_linux.GNU' > build/linux/include/makeinclude/platform_macros.GNU
 cd build/linux
 make
 make install
 cd TAO
 make
 make install
```

SSLIOPを有効にする場合は、以下のように**ssl**オプションを有効にして**SSLIOP**をビルドする必要があります。

```
 cd build/linux
 make ssl=1
 make install ssl=1
 cd TAO
 make SSLIOP ssl=1
 make install ssl=1
```

### 環境変数の設定
&aname(ubuntu_env);
また、pkg-configでACE+TAOを検出するには以下のように環境変数**PKG_CONFIG**を設定する。

```
 export PKG_CONFIG_PATH=${ACE_INSTALL_DIR}/lib/pkgconfig:$PKG_CONFIG_PATH
```

## ネームサーバー起動手順(SSLIOP)

ネームサーバーをSSLIOP通信可能な状態で起動するためには以下のコマンドを実行する。

```
 ${ACE_INSTALL_DIR}bin/tao_cosnaming -ORBSvcConf server.conf -ORBEndpoint iiop://localhost:/ssl_port=2809
```

エンドポイントを**ssliop://localhost:2809**のように設定するとcorbaloc形式でのアクセスが上手くいかないため、上記のように**iiop://localhost:/ssl_port=2809**と指定する。

**server.conf**は例えば以下のようなファイルを用意する。

```
 dynamic SSLIOP_Factory Service_Object *
         TAO_SSLIOP:_make_TAO_SSLIOP_Protocol_Factory()
         "-SSLAuthenticate SERVER_AND_CLIENT -SSLPrivateKey PEM:server_key.pem -SSLCertificate PEM:server_cert.pem -SSLCAfile PEM:cacert.pem"
 static Resource_Factory "-ORBProtocolFactory SSLIOP_Factory"
```

