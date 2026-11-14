---
layout: page
title: "openrtm-aist(c++版)のcmakeによるビルド手順"
---

<!-- Title: OpenRTM-aist(C++版)のCMakeによるビルド手順 -->
#contents

## Windows + omniORB

&aname(windowsomniorb);

以下から OpenRTM-aist のソースコードを入手してください。

- [https://github.com/OpenRTM/OpenRTM-aist](https://github.com/OpenRTM/OpenRTM-aist)

以下からビルド済みの omniORB を入手してください。

- [https://openrtm.org/pub/omniORB/win32/](https://openrtm.org/pub/omniORB/win32/)

チェックアウトしたフォルダー(OpenRTM-aist)に移動して以下のコマンドを実行してください。


```
 mkdir build
 cd build
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc141 -G "Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=C:/workspace/openrtminstall ..
 cmake --build . --config Release
 cmake --build . --config Release --target install
```


<table class="table-alt">
  <tr>
    <th>変数名</th>
    <th>意味</th>
    <th>設定できる値</th>
  </tr>
  <tr>
    <td>CORBA</td>
    <td>CORBA のライブラリー</td>
    <td>omniORB</td>
  </tr>
</table>

## Windows + TAO

以下から OpenRTM-aist のソースコードを入手してください。

- [https://github.com/OpenRTM/OpenRTM-aist](https://github.com/OpenRTM/OpenRTM-aist)

以下の手順でTAOをビルドします。

- [TAOのビルド]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_qnx_1_1/qnx_build_proc_1_2/tao_buildn#windows)


チェックアウトしたフォルダー(OpenRTM-aist)に移動して以下のコマンドを実行してください。



```
 mkdir build
 cd build
 cmake -DORB_ROOT=C:/workspace/ACE_wrappers -DCORBA=TAO -G "Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=C:/workspace/openrtminstall ..
 set PATH=%PATH%;C:\workspace\ACE_wrappers\lib;
 cmake --build . --config Release
 cmake --build . --config Release --target install
```


## Windows 10 IoT + omniORB
omniORBのWindows 10 IoT用のビルド済みバイナリファイルは現在のところ配布していないため、自力でビルドする必要があります。
Cygwinのインストールが必要です。

- [https://www.cygwin.com/](https://www.cygwin.com/)


omniORBのソースコードを入手してください。

- [https://sourceforge.net/projects/omniorb/files/omniORB/omniORB-4.2.2/](https://sourceforge.net/projects/omniorb/files/omniORB/omniORB-4.2.2/)


omniORB-4.2.2.tar.bz2を適当な場所に展開してください。

最初にARM+Windows用の修正パッチを適用します。
以下から修正パッチを入手してください。

- [http://svn.openrtm.org/omniORB/trunk/windows/omniORB-4.2.2-windows-iot.patch](http://svn.openrtm.org/omniORB/trunk/windows/omniORB-4.2.2-windows-iot.patch)

Cygwin上で以下のコマンドを実行してください。


```
 patch -p1 -d omniORB-4.2.2 < omniORB-4.2.2-windows-iot.patch
```



omniORB-4.2.2.tar.bz2を展開したフォルダの**mk/platforms/arm_win32_vs_14.mk**を編集します。
使用するVisual Studioのバージョンが違う場合は合ったものを選択してください。
以下のようにPythonのディレクトリを指定します。


```
 PYTHON = /cygdrive/c/Python27/python
```


次に**config/config.mk**を編集します。
以下のように対応したmkファイルを指定します。
Visual Studioのバージョンが違う場合は適宜対応してください。


```
 platform = arm_win32_vs_14
```



クロスコンパイルを行うため、idlコンパイラなどの実行ファイルは開発環境で動作可能なものを用意します。

以下からx86用にビルドした omniORB のバイナリを入手してください。

- [http://openrtm.org/pub/omniORB/win32/omniORB-4.2.2/](http://openrtm.org/pub/omniORB/win32/omniORB-4.2.2/)

zipファイルを展開したフォルダの**bin/x86_win32**の中身を、omniORB-4.2.2.tar.bz2を展開したフォルダの**bin/x86_win32**にコピーしてください。




omniORB-4.2.2.tar.bz2を展開したディレクトリに移動して、以下のコマンドを実行してください。

```
 set PATH=C:\cygwin64\bin;%PATH%;
 call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x86_arm
 cd src
 make export
```


これで**bin/ARM_win32**に実行ファイルが、**lib/ARM_win32**にライブラリが生成されます。
vcvarsall.batについてはVisual Studioのバージョンにあったものを使用してください。
Visual Studio 2017の場合は**C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat**となります。



OpenRTM-aistのビルドは通常とほとんど同じです。
cmakeのオプションとして**Visual Studio 14 2015 ARM**というようにARM用のコンパイラを指定してください。



```
 mkdir build
 cd build
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.2 -G "Visual Studio 14 2015" -A ARM -DCMAKE_INSTALL_PREFIX=C:/workspace/openrtminstall ..
 cmake --build . --config Release
 cmake --build . --config Release --target install
```


Visual StudioにARM用コンパイラがインストールされていないとビルドできません。
ARM用コンパイラをインストールしていない場合は、**Visual Studio Installer**を起動して**ARM用Visual Studio C++コンパイラとライブラリ**'をインストールしてください。


<br>
<br>

<div align="center"><a href="arm1.png"><img src="arm1.png" width="50%;"></a></div>
<br>
<br>

## Ubuntu + omniORB

&aname(ubuntuomniorb);

```
 sudo apt install libomniorb4-dev omniidl omniorb-nameserver
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist/
 mkdir build
 cd build/
 cmake -DCMAKE_BUILD_TYPE=Release ..
 cmake --build . --config Release -- -j$(nproc)
 sudo cmake --build . --config Release --target install
```



<table class="table-alt">
  <tr>
    <td>変数名</td>
    <td>意味</td>
    <td>設定できる値</td>
  </tr>
  <tr>
    <td>CORBA</td>
    <td>CORBA のライブラリー</td>
    <td>omniORB</td>
  </tr>
</table>

## Ubuntu + TAO

以下の手順でTAOをビルドします。

- [TAOのビルド]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_qnx_1_1/qnx_build_proc_1_2/tao_buildn#ubuntu)

以下のコマンドでOpenRTM-aistをビルドしてください。

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist/
 mkdir build
 cd build
 cmake -DCORBA=TAO -DCMAKE_BUILD_TYPE=Release ..
 cmake --build . --config Release -- -j$(nproc)
 sudo cmake --build . --config Release --target install
```

## VxWorks + omniORB
事前にWind River Workbenchのホームディレクトリを指定する必要があります。
Wind River Workbenchをインストールしたディレクトリを**WIND_HOME**という変数に設定してください。

```
 export WIND_HOME=/home/openrtm/WindRiver
```

OpenRTM-aistのビルドの前に、omniORBのビルドを行う必要があります。

### omniORB
omniORBのソースコードを入手してください。

- [http://omniorb.sourceforge.net/](http://omniorb.sourceforge.net/)

omniORBのVxWorks対応パッチを入手してください。

- [http://svn.openrtm.org/omniORB/trunk/vxworks/omniORB-4.2.2-vxworks.patch](http://svn.openrtm.org/omniORB/trunk/vxworks/omniORB-4.2.2-vxworks.patch)


以下のコマンドでビルドを実行します。

```
 wget https://jaist.dl.sourceforge.net/project/omniorb/omniORB/omniORB-4.2.2/omniORB-4.2.2.tar.bz2
 tar xf omniORB-4.2.2.tar.bz2
 wget http://svn.openrtm.org/omniORB/trunk/vxworks/omniORB-4.2.2-vxworks.patch
 patch -p1 -d omniORB-4.2.2 < omniORB-4.2.2-vxworks.patch
 cd omniORB-4.2.2
 mkdir build
 cd build
 ../configure
 make
 cd ..
 sed -i '1s/^/platform = ${VXWORKS_PLATFORM}\n/' config/config.mk
 cd src
 make export
```

ただし、VXWORKS_PLATFORMには動作環境に合ったものを入力するようにしてください。
<table class="table-alt">
  <tr>
    <th>VXWORKS_PLATFORM</th>
    <th>CPU</th>
    <th>VxWorksのバージョン</th>
    <th>実装方法</th>
  </tr>
  <tr>
    <td>powerpc_vxWorks_kernel_6.6</td>
    <td>PowerPC</td>
    <td>6.6</td>
    <td>カーネルモジュール</td>
  </tr>
  <tr>
    <td>powerpc_vxWorks_RTP_6.6</td>
    <td>PowerPC</td>
    <td>6.6</td>
    <td>RTP</td>
  </tr>
  <tr>
    <td>powerpc_vxWorks_kernel_6.9</td>
    <td>PowerPC</td>
    <td>6.9</td>
    <td>カーネルモジュール</td>
  </tr>
  <tr>
    <td>powerpc_vxWorks_RTP_6.9</td>
    <td>PowerPC</td>
    <td>6.9</td>
    <td>RTP</td>
  </tr>
  <tr>
    <td>simlinux_vxWorks_kernel_6.6</td>
    <td>Linux上のシミュレータ</td>
    <td>6.6</td>
    <td>カーネルモジュール</td>
  </tr>
  <tr>
    <td>simpentium_vxWorks_RTP_6.6</td>
    <td>Linux上のシミュレータ</td>
    <td>6.6</td>
    <td>RTP</td>
  </tr>
  <tr>
    <td>simlinux_vxWorks_kernel_6.9</td>
    <td>Linux上のシミュレータ</td>
    <td>6.9</td>
    <td>カーネルモジュール</td>
  </tr>
  <tr>
    <td>simpentium_vxWorks_RTP_6.9</td>
    <td>Linux上のシミュレータ</td>
    <td>6.9</td>
    <td>RTP</td>
  </tr>
</table>

### OpenRTM-aist

以下のコマンドを入力してください。

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist/
 mkdir build
 cd build/
 cmake -DCMAKE_TOOLCHAIN_FILE=${TOOLCHAIN_FILE} -DVX_VERSION=${VX_VERSION} -DORB_ROOT=${ORB_ROOT} -DOMNI_VERSION=42 -DCORBA=omniORB -DVX_CPU_FAMILY=${ARCH} ..
 make
```

ただし、TOOLCHAIN_FILE、VX_VERSION 、ORB_ROOT、ARCHには以下の設定をしてください。

<table class="table-alt">
  <tr>
    <th>TOOLCHAIN_FILE</th>
    <th>VxWorks 6.6(カーネルモジュール、PowerPC)の場合は**../Toolchain-vxworks6.6-Linux.cmake**、それ以外の場合は**../Toolchain-vxworks6.cmake**</th>
  </tr>
  <tr>
    <td>VX_VERSION</td>
    <td>**vxworks-6.6**か**vxworks-6.9**</td>
  </tr>
  <tr>
    <td>ORB_ROOT</td>
    <td>omniORBのディレクトリ(例：/home/openrtm/omniORB-4.2.2)</td>
  </tr>
  <tr>
    <td>VX_CPU_FAMILY</td>
    <td>**ppc**(PowerPC)、**simlinux**(カーネルモジュール、シミュレータ)、**simpentium**(RTP、シミュレータ)</td>
  </tr>
</table>

RTPの場合はcmakeコマンドに**-DRTP=ON**を追加する必要があります。

```
 cmake -DCMAKE_TOOLCHAIN_FILE=${TOOLCHAIN_FILE} -DVX_VERSION=${VX_VERSION} -DORB_ROOT=${ORB_ROOT} -DOMNI_VERSION=42 -DCORBA=omniORB -DVX_CPU_FAMILY=${ARCH} -DRTP=ON ..
 cmake --build . --config Release
```


## VxWorks + ORBexpress
※現在のところ対応環境はVxWorks 6.6、PowerPCのみです。

以下のコマンドを入力してください。


```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist/
 mkdir build
 cd build/
 cmake -DCMAKE_TOOLCHAIN_FILE=${TOOLCHAIN_FILE} -DORB_ROOT=${ORB_ROOT} -DCORBA=ORBexpress ..
 make
```

TOOLCHAIN_FILE、ORB_ROOTには以下の設定をしてください。

<table class="table-alt">
  <tr>
    <th>TOOLCHAIN_FILE</th>
    <th>カーネルモジュールの場合は**../Toolchain-vxworks6.6-Linux.cmake**、RTPの場合は**../Toolchain-vxworks6.cmake**</th>
  </tr>
  <tr>
    <td>ORB_ROOT</td>
    <td>ORBexpressのディレクトリ(例：/home/openrtm/OIS/ORBexpress/RT_2.8.4_PATCH_KC1)</td>
  </tr>
</table>



## QNX 6.5 + omniORB
VMWare上のQNX 6.5でビルドします。
以下のページからISOイメージを入手してください。

- [http://www.qnx.com/download/group.html?programid=16780](http://www.qnx.com/download/group.html?programid=16780)

### pkgsrc
まずはパッケージ管理システムpkgsrcをインストールします。
以下のコマンドでソースコードを入手してください。

```
 svn checkout --username ユーザ名 --password パスワード http://community.qnx.com/svn/repos/pkgsrc/HEAD_650/pkgsrc
```

ユーザー名、パスワードはQNXのアカウントのメールアドレス、パスワードを設定してください。

次に以下のコマンドでインストールします。
コマンドはsuで実行してください。

```
 (cd pkgsrc/bootstrap && ./bootstrap)
 (cd pkgsrc/misc/figlet && ../../bootstrap/work/bin/bmake install)
```

環境変数PKG_PATHを設定しておいてください。

```
 export PKG_PATH=ftp://ftp.netbsd.org/pub/pkgsrc/packages/QNX/i386/6.5.0_head_20110826/All/
```

### libuuid
まずはlibuuidのビルドをします。
libuuid-1.0.3.tar.gzをダウンロードしてQNXに転送してください。

- [https://sourceforge.net/projects/libuuid/files/](https://sourceforge.net/projects/libuuid/files/)

ファイルを展開してください。

```
 tar xf libuuid-1.0.3.tar.gz
```


libuuidのビルドにはsys/syscall.h、bits/syscall.h、asm/unistd.h、asm/unistd_32.h(もしくはasm/unistd_64.h)が必要になります。
ファイルを入手してlibuuid-1.0.3の下にコピーしてください。

```
 libuuid-1.0.3
    |-sys
    | |-syscall.h
    |-bits
    | |-syscall.h
    |-asm
    | |-unistd.h
    | |-unistd_32.h(もしくはunistd_64.h)
    |-(省略)
```

以下のコマンドでビルド、インストールしてください。

```
 cd libuuid-1.0.3
 ./configure
 make
 make install
 cd ..
```



### omniORB
まずはomniORB-4.2.3.tar.bz2を入手してQNXに転送してください。

- [https://sourceforge.net/projects/omniorb/files/omniORB/](https://sourceforge.net/projects/omniorb/files/omniORB/)

ファイルを展開してください。

```
 tar xf omniORB-4.2.3.tar.bz2
```

以下のファイルについて変更が必要です。

- configure
- /beforeauto.mk.in

まずconfigureについては2箇所の変更が必要です。
以下の*-*-nto-qnx)の行を追加してください。

```
 case "$host" in
   *-*-linux-*)   plat_name="Linux";    plat_def="<u>linux</u>";    os_v="2";;
   *-*-nto-qnx)   plat_name="Linux";    plat_def="<u>linux</u>";    os_v="2";;
```

以下のx86-pc-*)の部分を追加してください。

```
 case "$host" in
   i?86-*)   proc_name="x86Processor";     proc_def="__x86__";;
   x86-pc-*) proc_name="x86Processor"; proc_def="__x86__";;
```

mk/beforeauto.mk.inは以下の部分を変更してください。

```
 #OMNITHREAD_LIB += -lpthread #削除
 OMNITHREAD_LIB += -lsocket #追加
```

以下のコマンドでビルドします。

```
 ./configure
 make
 make install
 cd ..
```


### OpenRTM-aist
OpenRTM-aistのビルドにはcmake、pkg-config、Python 2.7が必要です。

```
 /usr/pkg/sbin/pkg_add -v pkg-config-0.25nb1
 /usr/pkg/sbin/pkg_add -v cmake-2.8.5
 /usr/pkg/sbin/pkg_add -v python27-2.7.2
```

環境変数PKG_CONFIG_PATHを設定してください。

```
 export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig/
```

OpenRTM-aistのソースコードを入手してQNXに転送してください。

OpenRTM-aistのディレクトリに移動して以下のコマンドを実行します。

```
 mkdir build
 cd build/
 ln -s /usr/pkg/bin/python2.7 ./python
 export PATH=$PWD:$PATH
 cmake -DCORBA=omniORB ..
 cmake --build . --config Release -- -j$(nproc)
 cmake --build . --target install
```


## QNX 7.0 + omniORB
Ubuntu上にQNX Software Development Platform 7.0をインストールしてビルドします。
まずはQNX Software Centerをインストールしてください。

- [http://www.qnx.com/download/group.html?programid=29178](http://www.qnx.com/download/group.html?programid=29178)

```
 sudo apt-get install libgtk2.0-0:i386
 chmod a+x qnx-setup-201808201144-lin.run
 ./qnx-setup-201808201144-lin.run
```

QNX Software Centerを起動してAdd InstallationからQNX Software Development Platformをインストールしてください。

```
 /home/openrtm/qnx/qnxsoftwarecenter/qnxsoftwarecenter
```

<div align="center"><a href="qnx9.png"><img src="qnx9.png" width="80%;"></a></div>


### libuuid
まずはlibuuidのビルドをします。

```
 wget https://jaist.dl.sourceforge.net/project/libuuid/libuuid-1.0.3.tar.gz
 tar xf libuuid-1.0.3.tar.gz
```


libuuidのビルドにはsys/syscall.h、bits/syscall.h、asm/unistd.h、asm/unistd_32.h(もしくはasm/unistd_64.h)が必要になります。
ファイルを入手してlibuuid-1.0.3の下にコピーしてください。

```
 cd libuuid-1.0.3
 mkdir sys
 cp /usr/include/x86_64-linux-gnu/sys/syscall.h sys
 mkdir asm
 cp /usr/include/x86_64-linux-gnu/asm/unistd.h asm
 cp /usr/include/x86_64-linux-gnu/asm/unistd_64.h asm
 mkdir bits
 cp /usr/include/x86_64-linux-gnu/bits/syscall.h bits
```


QNXクロスコンパイル環境設定のためにスクリプトを実行します。

```
 source ~/qnx700/qnxsdp-env.sh
```

以下のコマンドでビルドします。
qnx700のパスは適宜変更してください。

```
 ./configure --prefix=/home/openrtm/qnx700/target/qnx7/usr/ CC="qcc -V5.4.0,gcc_ntox86_64_gpp" CXX="q++ -V5.4.0,gcc_ntox86_64_gpp" AR=ntox86_64-ar RANLIB=ntox86_64-ranlib --host=x86_64-unknown-linux-gnu
 make
 make install
 cd ..
```

### omniORB
まずはomniORBのソースコードを入手してください。

```
 wget https://jaist.dl.sourceforge.net/project/omniorb/omniORB/omniORB-4.2.3/omniORB-4.2.3.tar.bz2
 tar xf omniORB-4.2.3.tar.bz2 
 cd omniORB-4.2.3
```


Ubuntu上でomniidlをビルドする必要があります。
qnxsdp-env.shを実行していない環境でomniORBのビルドを行いインストールしてください。

```
 ./configure
 make
 make install
```

QNXでビルドするために

```
 #OMNITHREAD_LIB += -lpthread
 OMNITHREAD_LIB += -lsocket
```

以下のコマンドでビルドしてください。

```
 make clean
 ./configure --prefix=/home/openrtm/qnx700/target/qnx7/usr/  CC="qcc -V5.4.0,gcc_ntox86_64_gpp" CXX="q++ -V5.4.0,gcc_ntox86_64_gpp" AR=ntox86_64-ar RANLIB=ntox86_64-ranlib --host=x86_64-unknown-linux-gnu
 make
 make install
```

### OpenRTM-aist

omniORB、uuidをpkg-configで検出するために環境変数PKG_CONFIG_PATHを設定してください。

```
 export PKG_CONFIG_PATH=/home/openrtm/qnx700/target/qnx7/usr/lib/pkgconfig
```

以下のコマンドでビルドします。

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 cd OpenRTM-aist/
 mkdir build
 cd build
 cmake -DCORBA=omniORB -DCMAKE_TOOLCHAIN_FILE=../Toolchain-QNX7.cmake -DCMAKE_INSTALL_PREFIX=/home/openrtm/qnx700/target/qnx7/usr/ ..
 cmake --build . --config Release -- -j$(nproc)
```


### VMWareイメージの入手
VMWare用のイメージを入手するためには、QNX Software Centerでファイルをダウンロードします。

<div align="center"><a href="qnx10.png"><img src="qnx10.png" width="80%;"></a></div>

QNX Software Development Platform->Reference Images->QNX SDP 7.0 x86-64 virtual machine for VMWareをインストールしてください。

<div align="center"><a href="qnx.png"><img src="qnx.png" width="80%;"></a></div>

インストールしたQNX_SDP.vmxをVMwareで開くと仮想マシンが起動します。

<hr>

- [CMakeのオプション一覧](./cmake_option/)
- [omniORBのビルド](./omniorb_build/)
- [TAOのビルド](./tao_build)
- [OpenRTM-aistのビルド、動作確認手順]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_qnx_1_1/qnx_build_proc_1_2/openrtm_cpp_cmake_run/)


