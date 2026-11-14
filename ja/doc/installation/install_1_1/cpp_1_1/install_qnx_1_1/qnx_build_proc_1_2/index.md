---
layout: page
title: qnxでのビルド手順(openrtm-aist 1.2)
---

<!-- Title: QNXでのビルド手順(OpenRTM-aist 1.2) -->
#contents

このページではQNX 6.5でOpenRTM-aist 1.2をビルドする手順を説明します。
以下からソースコードを入手してください。

- https://github.com/OpenRTM/OpenRTM-aist/tree/svn/RELENG_1_2

pkg_src、omniORB、libuuidのビルド手順については以下のページを参考にしてください。


- [OpenRTM-aist(C++版)のCMakeによるビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build) 



OpenRTM-aistのビルドのために以下のソフトウェアをインストールします。

```
 /usr/pkg/sbin/pkg_add -v autoconf-2.68
 /usr/pkg/sbin/pkg_add -v automake-1.11.1nb1
 /usr/pkg/sbin/pkg_add -v libtool-2.2.6b
```






configure.ac、src/ext/Makefile.am、src/ext/local_service/Makefile.amを編集します。

configure.acから-lomnisslTP4を削除してください。
```
        #LIBS="$LIBS -lomniORB4 -lomnithread -lomniDynamic4 -lomnisslTP4" <-削除
        #LDSOLIBS="$LDSOLIBS -lomniORB4 -lomnithread -lomniDynamic4 -lomnisslTP4" <-削除
        LIBS="$LIBS -lomniORB4 -lomnithread -lomniDynamic4" <-追加
        LDSOLIBS="$LDSOLIBS -lomniORB4 -lomnithread -lomniDynamic4" <-追加
```

src/ext/Makefile.amは以下のようにsslを削除します。


```
 #SUBDIRS = local_service ec sdo <-削除
 #DIST_SUBDIRS = local_service ec sdo logger <-削除
 SUBDIRS = local_service ec sdo ssl <-追加
 DIST_SUBDIRS = local_service ec sdo logger ssl <-追加
```


src/ext/local_service/Makefile.amは以下のようにサブディレクトリの設定を削除します。

```
 #SUBDIRS = nameservice_file <-削除
```


以下のコマンドでビルドします。

```
 ./autogen.sh
 ./configure --without-doxygen
 make
 make install
```
