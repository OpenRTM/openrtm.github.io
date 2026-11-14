---
layout: page
title: idlコンパイラ
---

<!-- Title: IDLコンパイラ -->
<!-- *IDL コンパイラに関して  -->
#contents
#clear

## MICO IDL 

コンパイラ名 : idl 
/usr/local/bin/idl, /usr/bin/idl など。
<!-- ::そのものの名前を使うのはやめてほしい。 -->
<!-- ::何かprefixをつけてほしいものだ。 -->

オプション: 例 idl --c++-skel --poa --no-boa RTCPackage.idl
<br>
C++ で普通に使うにはこの程度で OK。

```
 > idl -h

 unknown option: -h
 usage: idl [<options>] [<file>]
 possible <options> are:

    --help
    --version
    --config
    --feed-ir
    --feed-included-defs
    --do-not-feed-included-defs
    --no-exceptions
    --codegen-c++
    --no-codegen-c++
    --codegen-idl
    --no-codegen-idl
    --codegen-midl
    --no-codegen-midl
    --cpp < cpp >
    --c++-suffix <filename-suffix>
    --c++-impl
    --c++-skel
    --codegen-wsdl
    --no-codegen-wsdl
    --hh-suffix <filename-suffix>
    --relative-paths
    --emit-repoids
    --do-not-query-server-for-narrow
    --repo-id <repository-id>
    --name <filename-prefix>
    --wsdl-map <filename>
    --ifdef-prefix <prefix>
    --poa
    --no-poa
    --boa    --    (deprecated)
    --no-boa
    --no-poa-ties
    --no-poa-stubs
    --pseudo
    --any
    --typecode
    --windows-dll <dll-prefix>
    --windows-dll-with-export <dll-prefix>
    --mico-core
    --gen-included-defs
    --gen-full-dispatcher
    --missing-nscorba
    --not-missing-nscorba
    --support-id
    --dont-support-id
    --wsi-wsdl
    --no-wsi-wsdl
    --include-prefix <include-prefix>
```
^L を受け付けない<br>
改ページの^LがIDLソース中にあると受け付けない。（omniidl ではそのまま通すことが可能。）
<!-- ::omniidl ではそのまま通すのに…。 -->


<!-- ** omniORB -->


## TAO IDL 

gperf 問題
<br>
gperf は TAO 付属の gperf を使う必要あり。FreeBSD では /usr/bin/gperf (システムに付属か？)と /usr/local/bin/gperf (TAO 付属) がある。
<br>
デフォルトでは $ACE_ROOT/bin/gperf を使うため、環境変数ACE_ROOTを設定するか、オプション -g &lt;gperf_path&gt; を設定する必要がある。
<!-- ::デフォルトでは $ACE_ROOT/bin/gperf を使うため、環境変数ACE_ROOTを設定するか、オプション -g <gperf_path> を設定しなければならない。 -->

TAO_ROOT
<br>
環境変数 TAO_ROOT が設定されていないと TAO が提供する IDL を読み込めない。
<br>
さらに、TAO の ORB の IDL (ex. /usr/local/include/tao/orb.idl) をインクルード

```
 #include <orb.idl>
```
しないと、TypeCodeなどが使えない。
```
 #ifdef TAO_IDL
 #include <orb.idl>
 #endif
```
などとして、他の IDL コンパイラと分ける必要あり。

## ORBit2 idl

コンパイラ名 : orbit-idl-2<br>
ORBit はデフォルトでは C言語でコーディングすることになっている。

- ヘルプ

```
 Usage: orbit-idl-2 [-D|-define STRING] [-I|-include STRING] [--libIDL-version]
        [-v|--version] [-l|--lang STRING] [-d|--debug INT] [--idlwarnlevel=INT]
        [--showcpperrors] [--nostubs] [--noskels] [--nocommon]
        [--noheaders] [--noidata] [-i|--imodule] [--add-imodule]
        [--skeleton-impl] [--backenddir=DIR] [--c-output-formatter=PROGRAM]
        [--onlytop] [--pidl] [--nodefskels] [--deps=FILENAME]
        [--headerguardprefix=STRING] [--output-dir=STRING] [-?|--help]
        [--usage] <IDL files>
```

<!-- : オプション | -l or --lang でcppを指定するとC++のコードを生成する。 -->
ただし、Cのコードを使っているので、Cのコードも生成しておかないといけない。
<br>
<br>

- オプション
  - l or --lang でcppを指定するとC++のコードを生成する。
ただし、Cのコードを使っているので、Cのコードも生成しておく必要がある。

```
 orbit-idl-2 RTCPackage.idl
 orbit-idl-2 -lcpp RTCPackage.idl
```

これにより、
```
 RTCPackage-common.c
 RTCPackage.h
 RTCPackage-cpp-common.cc
 RTCPackage-cpp-common.h
 RTCPackage-cpp-skels.cc
 RTCPackage-cpp-skels.h
 RTCPackage-cpp-stubs.cc
 RTCPackage-cpp-stubs.h
 RTCPackage-cpp.cc
 RTCPackage-cpp.h
```
が生成される。xxx-cpp.cc がすべてのソースを内部で include しているので、スケルトンとスタブの両方が必要ならこのソースのみコンパイルすればよい。

- orbit-idl-2 の問題
struct の中に Object reference のシーケンスを入れるとスケルトンのコンパイルが通らない。
```
 struct ComponentProfile
 {
    PortProfileList inport_profile_list;
    PortProfileList outport_profile_list;
    ServiceProfileList service_profile_list;
    ServiceProfileList consumer_profile_list;
    RTC parent;
    RTCList children; // × typedefしたObject ref のsequenceはだめ
    sequence<RTC> children; // × typedefは関係ない
    sequence<RTC,100> children; // × bounded sequence もだめ
    sequence<short> children; // ○ Object ref でなければOK
 };
```

