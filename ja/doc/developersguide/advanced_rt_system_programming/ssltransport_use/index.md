---
layout: page
title: "ssltransportの使用方法"
---

<!-- Title: SSLTransportの使用方法 -->
#contents

## 概要
オブジェクトの[CORBA Security Service](https://www.omg.org/spec/SEC/About-SEC/)仕様のセキュリティ機能を一部使用可能になっています。
CORBA Security Serviceではセキュリティポリシーのモデル、認証、アクセス制御、メッセージ保護、委譲、監査、否認不可の機能を定義していますが、omniORBではGIOPメッセージをSSL/TLSによるサーバー・クライアント認証と暗号化で保護するSSLIOP通信をサポートしています。
このページではOpenRTM-aistでomniORBのSSLIOP通信を使用する手順を説明します。




## C++
### Windows
#### OpenRTM-aistのビルドとインストール

まず、OpenSSLのヘッダーファイル、ライブラリを適当な場所に展開してください。

- https://openrtm.org/pub/OpenSSL/

OpenRTM-aist+omniORBを以下の手順でビルド、インストールします。

- [OpenRTM-aist(C++版)のCMakeによるビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build#windowsomniorb)

ただし、CMake実行時に**SSL_ENABLE**、**OPENSSL_ROOT_DIR**のオプションを設定する必要があります。

<table class="table-alt">
  <tr>
    <th>設定項目</th>
    <th>内容</th>
    <th>設定例</th>
  </tr>
  <tr>
    <td>SSL_ENABLE</td>
    <td>SSLTransportプラグインの生成の有無</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>OPENSSL_ROOT_DIR</td>
    <td>OpenSSLの各種ファイルを配置したパス</td>
    <td>C:/work/OpenSSL/x64</td>
  </tr>
</table>

また、CMake実行時にOpenRTM-aistのインストールフォルダは指定してそこにインストールするようにしてください。

```
 set OPENRTM_INSTALL_DIR=C:/work/openrtm_install
 set OMNIORB_SOURCE_DIR=C:/workspace/omniORB-4.2.5-x64-vc14-py310
 set OPENSSL_ROOT_DIR=C:/work/OpenSSL/x64
 cmake .. -DORB_ROOT=%OMNIORB_SOURCE_DIR% -DSSL_ENABLE=ON -DOPENSSL_ROOT_DIR=%OPENSSL_ROOT_DIR% -DCMAKE_INSTALL_PREFIX=%OPENRTM_INSTALL_DIR%
 cmake --build . --config Release
 cmake --build . --config Release --target install
```

### Ubuntu
#### OpenRTM-aistのビルドとインストール
OpenSSLのヘッダとライブラリをインストールします。

```
 sudo apt install libssl-dev
```

OpenRTM-aist+omniORBを以下の手順でビルド、インストールします。

- [OpenRTM-aist(C++版)のCMakeによるビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build#ubuntuomniorb)

ただし、**SSL_ENABLE**のオプションを設定する必要があります。

<table class="table-alt">
  <tr>
    <th>設定項目</th>
    <th>内容</th>
    <th>設定例</th>
  </tr>
  <tr>
    <td>SSL_ENABLE</td>
    <td>SSLTransportプラグインの生成の有無</td>
    <td>ON</td>
  </tr>
</table>

```
 set OPENRTM_INSTALL_DIR=~/work/openrtm_install
 cmake .. -DSSL_ENABLE=ON -DCMAKE_INSTALL_PREFIX=$OPENRTM_INSTALL_DIR
 cmake --build . --config Release -- -j$(nproc)
 cmake --build . --config Release --target install
```

## Python
### OpenRTM-aistのビルドとインストール
以下の手順でOpenRTM-aist Python版をインストールしてださい。

- [OpenRTM-aistのビルド、動作確認手順]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_qnx_1_1/qnx_build_proc_1_2/openrtm_cpp_cmake_run#pythoninstall)

ただし、動作確認でOpenRTM-aist C++版付属のネームサーバーを使用するため、C++版のビルドも実行してください。

## 動作確認

### ネームサーバー起動

SSLTransportの動作確認のためにはネームサーバーがSSLIOP通信に対応している必要があります。
OpenRTM-aist付属の**openrtmNames**を起動します。

以下のコマンドを実行してください。パスは確認して変更してください。

```
 %OPENRTM_INSTALL_DIR%\2.0.0\bin\vc16\openrtmNames.exe -f %OPENRTM_INSTALL_DIR%\2.0.0\ext\rtc.names.ssl.conf
```

```
 $OPENRTM_INSTALL_DIR/bin/openrtmNames -f $OPENRTM_INSTALL_DIR/etc/rtc.names.ssl.conf
```

**rtc.names.ssl.conf**では生成済みのルート証明書root.crtと秘密鍵とサーバー証明書を連結したファイルserver.pemを使用するため、動作確認に使用するRTCもこれらの証明書ファイルを使います。
実際にシステムを開発する際は証明書と秘密鍵を変更してください。

### RTC起動

以下のようなrtc.confを作成します。OpenRTM-aistをインストールしたパスは適宜変更してください。

C++では以下のファイルを作成します。

```
 manager.modules.load_path: C:/work/openrtm_install/2.0.0/ext/ssl
 manager.preload.modules: SSLTransport.dll
 
 corba.ssl.certificate_authority_file:C:/work/openrtm_install/2.0.0/ext/ssl/root.crt
 corba.ssl.key_file:C:/work/openrtm_install/2.0.0/ext/ssl/server.pem
 corba.ssl.key_file_password:password
 corba.args:-ORBserverTransportRule "* ssl" -ORBclientTransportRule "* ssl" -ORBendPoint giop:ssl::
 corba.nameservers: corbaloc:ssliop:localhost:2809
 corba.master_manager: giop:ssl:localhost:2810
```

Pythonでは以下のファイルを作成します。

```
 manager.modules.load_path: C:/Python37/Lib/site-packages/OpenRTM_aist/ext/vc16/ssl
 manager.preload.modules: SSLTransport.py
 
 corba.ssl.certificate_authority_file:C:/Python37/Lib/site-packages/OpenRTM_aist/ext/ssl/root.crt
 corba.ssl.key_file:C:/Python37/Lib/site-packages/OpenRTM_aist/ext/ssl/server.pem
 corba.ssl.key_file_password:password
 corba.args:-ORBserverTransportRule "* ssl" -ORBclientTransportRule "* ssl" -ORBendPoint giop:ssl::
 corba.nameservers: corbaloc:ssliop:localhost:2809
 corba.master_manager: giop:ssl:localhost:2810
```

各設定項目の内容は以下のようになっています。


<table class="table-alt">
  <tr>
    <th>項目名</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>corba.ssl.certificate_authority_file</td>
    <td>ルート証明書</td>
  </tr>
  <tr>
    <td>corba.ssl.key_file</td>
    <td>秘密鍵+サーバー証明書兼クライアント証明書の連結ファイル</td>
  </tr>
  <tr>
    <td>corba.ssl.key_file_password</td>
    <td>秘密鍵のパスフレーズ</td>
  </tr>
  <tr>
    <td>corba.args</td>
    <td>CORBAライブラリの初期化関数に渡す引数。ここでSSLIOP通信のエンドポイントを設定する必要がある。</td>
  </tr>
  <tr>
    <td>corba.nameservers</td>
    <td>ネームサーバーのアドレス。ここでSSLIOP通信でネームサーバーに接続するように設定する。</td>
  </tr>
  <tr>
    <td>corba.master_manager</td>
    <td>マスターマネージャのエンドポイント。マスターマネージャの場合は自身のエンドポイントを設定し、スレーブマネージャの場合は接続先のマスターマネージャのアドレスを設定する。</td>
  </tr>
</table>

このrtc.confを指定してConsoleIn、ConsoleOutのRTCを起動します。

```
 %OPENRTM_INSTALL_DIR%\2.0.0\Components\C++\Examples\vc16\ConsoleInComp.exe -f rtc.conf
```

```
 %OPENRTM_INSTALL_DIR%\2.0.0\Components\C++\Examples\vc16\ConsoleOutComp.exe -f rtc.conf
```

```
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f rtc.conf
```

```
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleInComp -f rtc.conf
```

```
 python %OpenRTMPython_INSTALL_DIR%\Lib\site-packages\ConsoleIn.py -f rtc.conf
```

```
 python %OpenRTMPython_INSTALL_DIR%\Lib\site-packages\ConsoleOut.py -f rtc.conf
```

```
 python3 ${OpenRTMPython_INSTALL_DIR}/share/openrtm-2.0/components/python3/SimpleIO/ConsoleOut.py -f rtc.conf
```

```
 python3 ${OpenRTMPython_INSTALL_DIR}/share/openrtm-2.0/components/python3/SimpleIO/ConsoleIn.py -f rtc.conf
```

これでネームサーバーに登録されますが、RTシステムエディタにSSLIOP通信機能はないため、OpenRTM-aistの機能かrtshellによりポートの接続やRTCのアクティブ化を実行する必要があります。

## マネージャ起動時のポート接続、RTCのアクティブ化

rtc.confの[manager.components.preconnect]({{ site.baseurl }}/ja/doc/developersguide/basic_rtc_programming/rtc_conf_reference#preconnect)、[manager.components.preactivation]({{ site.baseurl }}/ja/doc/developersguide/basic_rtc_programming/rtc_conf_reference)でrtcname形式、rtcloc形式を指定することでポートの接続、RTCのアクティブ化ができます。
SSLIOP通信の場合は以下のようにプロトコルに**ssliop**を指定することで使用可能になります。

```
 manager.components.preconnect: ConsoleIn0.out?port=rtcname.ssliop://localhost:2809/*/ConsoleOut0.in
 manager.components.preactivation: ConsoleIn0, rtcname.ssliop://localhost:2809/*/ConsoleOut0
```

```
 naming.type: corba, manager
 manager.components.preconnect: ConsoleIn0.out?port=rtcloc.ssliop://localhost:2810/*/ConsoleOut0.in
 manager.components.preactivation: ConsoleIn0, rtcloc.ssliop://localhost:2810/*/ConsoleOut0
```

## rtshellによる操作
&aname(rtshell);

まず、現在インストールされるrtshellでは対応していないため、最新版のrtctree、rtshell、rtsprofileが必要です。

- https://github.com/OpenRTM/rtctree
- https://github.com/OpenRTM/rtshell
- https://github.com/OpenRTM/rtsprofile

rtshellでSSLIOP通信機能を使用するためには以下の環境変数を設定する必要があります。

<table class="table-alt">
  <tr>
    <th>環境変数名</th>
    <th>設定例</th>
    <th>意味</th>
  </tr>
  <tr>
    <td>RTCTREE_SSL_ENABLE</td>
    <td>YES</td>
    <td>YES：rtctreeでSSLIOP通信機能を有効にする。</td>
  </tr>
  <tr>
    <td>RTCTREE_NAMESERVERS</td>
    <td>ssliop:localhost:2809</td>
    <td>接続するネームサーバー</td>
  </tr>
  <tr>
    <td>ORBsslCAFile</td>
    <td>root.crt</td>
    <td>ルート証明書</td>
  </tr>
  <tr>
    <td>ORBsslKeyFile</td>
    <td>server.pem</td>
    <td>秘密鍵+サーバー証明書兼クライアント証明書の連結ファイル</td>
  </tr>
  <tr>
    <td>ORBsslKeyPassword</td>
    <td>password</td>
    <td>秘密鍵のパスフレーズ</td>
  </tr>
  <tr>
    <td>ORBserverTransportRule</td>
    <td>"* ssl"</td>
    <td>サーバー側の通信プロトコル選択のルール</td>
  </tr>
  <tr>
    <td>ORBclientTransportRule</td>
    <td>"* ssl"</td>
    <td>クライアント側の通信プロトコル選択のルール</td>
  </tr>
  <tr>
    <td>ORBendPoint</td>
    <td>giop:ssl::</td>
    <td>omniORBのエンドポイント</td>
  </tr>
</table>

```
 set RTCTREE_SSL_ENABLE=YES
 set ORBsslCAFile=%RTM_ROOT%/ext/ssl/root.crt
 set ORBsslKeyFile=%RTM_ROOT%/ext/ssl/server.pem
 set ORBsslKeyPassword=password
 set RTCTREE_NAMESERVERS=ssliop:localhost:2809
 set ORBserverTransportRule=* ssl
 set ORBclientTransportRule=* ssl
 set ORBendPoint=giop:ssl::
```

以下のように接続するネームサーバーのアドレスの前に**ssliop:**を付けることでSSLIOP通信でネームサーバーに接続できるようになります。

```
 rtcon /ssliop:localhost:2809/test.host_cxt/ConsoleIn0.rtc:out /ssliop:localhost:2809/test.host_cxt/ConsoleOut0.rtc:in
 rtact /ssliop:localhost:2809/test.host_cxt/ConsoleIn0.rtc /ssliop:localhost:2809/test.host_cxt/ConsoleOut0.rtc
 rtdeact /ssliop:localhost:2809/test.host_cxt/ConsoleIn0.rtc /ssliop:localhost:2809/test.host_cxt/ConsoleOut0.rtc
 rtexit /ssliop:localhost:2809/test.host_cxt/ConsoleOut0.rtc
 rtcryo ssliop:localhost:2809 -o sys.rtsys
```


## 秘密鍵、証明書の生成

まずは秘密鍵、証明書の生成が必要です。

証明書にはルート証明書、中間証明書、サーバー証明書、クライアント証明書があります。
以下はサーバー証明書によるサーバー認証を行う場合の概要図です。

<div align="center"><a href="ssl1.png"><img src="ssl1.png" width="80%;"></a></div>

通信するサーバー、クライアントPC以外に公開鍵証明書認証局(CA、Certificate Authority)が必要です。
認証局はルート証明書と対応する秘密鍵(秘密鍵1)を持っています。
サーバーは秘密鍵を生成後、生成した秘密鍵(秘密鍵a)でCSR(Certificate Signing Request：公開鍵情報、ウェブサイトの所有者情報)を認証局に送信します。
認証局はCSRに秘密鍵1で署名したサーバー証明書を発行します。
サーバーとクライアントのSSL/TLS通信のハンドシェイク処理でサーバー証明書を送信します。この時に他にも鍵交換アルゴリズムの処理などもありますが説明は省略します。
クライアントは予め入手しておいたルート証明書の公開鍵でサーバー証明書の署名の検証を行い、証明書の検証が完了したら暗号化通信(秘密鍵aで符号化、サーバー証明書の公開鍵で復号)を開始します。

この他に中間認証局がルート認証局から中間証明書を取得し、中間認証局がサーバー証明書を発行する場合があります。
説明は以下のサイトの図が分かりやすいので参考になると思います。

- [OpenSSLでプライベート認証局の構築（ルートCA、中間CA）](https://qiita.com/bashaway/items/ac5ece9618a613f37ce5)

ここまでの説明ではクライアント側がサーバーの認証をしていましたが、サーバーがクライアントの認証をする場合があります。
omniORBでは引数`-ORBsslVerifyMode`や環境変数`ORBsslVerifyMode`で以下のパラメータを設定することで認証方法を変更可能です。

<table class="table-alt">
  <tr>
    <th>パラメータ</th>
    <th>意味</th>
  </tr>
  <tr>
    <td>none</td>
    <td>サーバー証明書の検証に失敗してもハンドシェイクを継続する。クライアント証明書の要求は実行しない。</td>
  </tr>
  <tr>
    <td>peer(デフォルト値)</td>
    <td>サーバーがクライアント証明書を要求する。サーバー認証、クライアント認証(クライアント証明書が送信されてきた場合)で失敗したらハンドシェイクを終了する。</td>
  </tr>
  <tr>
    <td>peer, fail</td>
    <td>クライアント証明書が送信されなかったらハンドシェイクを終了する。</td>
  </tr>
  <tr>
    <td>peer, once</td>
    <td>クライアント認証を最初のハンドシェイクでのみ実行する。</td>
  </tr>
  <tr>
    <td>peer, fail, once</td>
    <td>上記の組み合わせ。</td>
  </tr>
</table>

omniORBはサーバー証明書、クライアント証明書のルート証明書ファイルを個別に指定できないため、どちらも`corba.ssl.certificate_authority_file`オプションで指定してください。

まとめると、OpenRTM-aistのSSL/TLS通信にはルート証明書、サーバー証明書、クライアント証明書、中間証明書、秘密鍵を以下のように配置する必要があります。

<div align="center"><a href="ssl2.png"><img src="ssl2.png" width="80%;"></a></div>

以降ではOpenSSLのコマンドを使って自己認証局と自己署名証明書(いわゆるオレオレ証明書)を作成してみます。
cnfファイルは上記のリンク先のサイトのものを使用します。

まず適当な作業フォルダにroot、inter、serverフォルダを作成します。

ルート認証局の秘密鍵、ルート証明書を作成します。

```
 mkdir root
 cd root
 mkdir newcerts
 type nul > index.txt
 echo 01 > serial
 echo 00 > crlnumberl
 openssl genrsa -out RootCA_key.pem -passout pass:rootpass 2048
 openssl req -new -subj "/C=JP/ST=Tokyo/O=EXAMPLE/CN=EXAMPLE Root CA" -out RootCA_csr.pem  -key RootCA_key.pem  -passin pass:rootpass -config ../conf/openssl_sign.cnf
 openssl ca  -batch -extensions v3_ca -out RootCA_crt.pem -in RootCA_csr.pem -selfsign -keyfile RootCA_key.pem -passin pass:rootpass -config ../conf/openssl_sign.cnf
 openssl x509 -in RootCA_crt.pem -out RootCA_crt.pem
 cd ..
```

次に中間認証局の秘密鍵、中間証明書のCSRを作成します。

```
 mkdir inter
 cd inter
 mkdir newcerts
 type nul > index.txt
 echo 01 > serial
 echo 00 > crlnumberl
 openssl genrsa -out InterCA_key.pem -passout pass:interpass 2048
 openssl req -new -subj "/C=JP/ST=Tokyo/O=EXAMPLE/CN=EXAMPLE Intermediate CA" -out InterCA_csr.pem -key InterCA_key.pem -passin pass:interpass -config ../conf/openssl_sign.cnf
 cd ..
```

ルート認証局で中間証明書を発行します。

```
 cd root
 openssl ca -batch -extensions v3_ca -out ..\inter\InterCA_crt.pem -in  ..\inter\InterCA_csr.pem -cert RootCA_crt.pem -keyfile RootCA_key.pem -passin pass:interpass -config ../conf/openssl_sign.cnf
 cd ..
```


サーバーで秘密鍵とサーバー証明書のCSRを作成します。

```
 mkdir server
 cd server
 mkdir newcerts
 type nul > index.txt
 echo 01 > serial
 echo 00 > crlnumberl
 openssl genrsa -out Server_key.pem -passout pass:serverpass 2048
 openssl req -new -subj "/C=JP/ST=Tokyo/O=EXAMPLE/CN=EXAMPLE Server" -out Server_csr.pem -key Server_key.pem -passin pass:serverpass -config ../conf/openssl_sign.cnf
 cd ..
```

中間認証局でサーバー証明書を発行します。

```
 cd inter
 openssl x509 -req -in ..\server\Server_csr.pem -sha256 -CA InterCA_crt.pem -CAkey InterCA_key.pem -set_serial 01 -days 730 -out ..\server\Server_crt.pem -passin pass:serverpass
 cd ..
```

秘密鍵、サーバー証明書、中間証明書を連結します。

```
 cd server
 openssl x509 -in Server_crt.pem -out Server_crt.pem
 openssl x509 -in ..\inter\InterCA_crt.pem -out InterCA_crt.pem
 copy /b Server_key.pem + Server_crt.pem + InterCA_crt.pem server.pem
```


今回使用するのは連結したファイル(server.pem)とルート証明書(RootCA_crt.pem)です。

## 簡単な動作確認
OpenRTM-aistをビルド、インストールすると、SSLTransportの簡単な動作確認用の設定ファイルがインストールされます。

```
 %RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
 %RTM_ROOT%\bin\vc16\openrtmNames.exe -f %RTM_ROOT%\ext\rtc.names.ssl.conf
```

```
 %RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
 %RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\ssl\rtc.ssl.conf
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/bin/openrtmNames -f ${OPENRTM_INSTALL_DIR}/etc/rtc.names.ssl.conf
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh 
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/ssl/rtc.ssl.conf
```

