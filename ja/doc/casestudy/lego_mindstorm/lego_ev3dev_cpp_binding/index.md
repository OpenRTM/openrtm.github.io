---
layout: page
title: ev3デバイス c++ バインディングの利用
---

<!-- Title: EV3デバイス C++ バインディングの利用 -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * cpp-ev3devの利用 -->
#contents

## ev3dev-lang の利用

ev3dev-lang には C++ や Python、Lua などの EV3 デバイスへのバインディングライブラリが含まれています。
以下では、C++ から利用できる、ev3dev バインディングの導入と使い方について説明します。


## ev3dev-lang の取得

以下の作業は、クロス開発環境にて行います。既に、上述の方法でクロス開発環境が導入済みであるとして進めます。

まず、github から ev3dev-lang をクローニングします。クローニング先は、クロス開発環境内の適当な場所 (ここでは /home/openrtm/work の下) にします。

```
 $ cd ev3-ev3dev-work/home/
 $ mkdir -p openrtm/work
 $ cd openrtm/work
 $ git clone https://github.com/ddemidov/ev3dev-lang-cpp
 Cloning into 'ev3dev-lang-cpp'...
 remote: Counting objects: 1733, done.
 remote: Total 1733 (delta 0), reused 0 (delta 0), pack-reused 1733
 Receiving objects: 100% (1733/1733), 510.41 KiB | 310.00 KiB/s, done.
 Resolving deltas: 100% (1150/1150), done.
 Checking connectivity... done.
 $ ls
 ev3dev-lang-cpp
 $ cd  ev3dev-lang-cpp
 $ git checkout c0829011bf668bb77e55049a7f2f396b0b452f41
```

<!-- C++用のバインディングは、ev3dev-lang/cpp 以下にあります。 -->

<!-- $ cd ev3dev-lang/cpp/ -->
<!-- $ ls -->
<!-- button-test.cpp  ev3dev.h              Makefile -->
<!-- drive-test.cpp   ev3dev-lang-demo.cpp  README.md -->
<!-- ev3dev.cpp       ev3dev-lang-test.cpp  remote_control-test.cpp -->

## ev3dev-lang のビルド

次に、コンパイルを行います。まず、作業ディレクトリー work に入り、brickstrap のクロス開発モードに入ります。

```
 $ cd ~/work
 $ brickstrap -b ev3-ev3dev-jessie -d ev3-ev3dev-work shell
```

先ほど github からクローニングしたディレクトリに移動し、make します。

```
 # cd /home/openrtm/work/ev3dev-lang-cpp/
 # mkdir build
 # cd build
 # cmake .. -DEV3DEV_PLATFORM=EV3
 # make
```
<!-- # make all -->


<!-- mkdir -p obj -->
<!-- g++ -c -o obj/ev3dev.o ev3dev.cpp -O2 -march=armv5 -std=c++11 -D_GLIBCXX_USE_NANOSLEEP -->
<!-- ：中略 -->
<!-- ev3dev-lang-demo.cpp: In function 'void led_action(const char*, ev3dev::led&)': -->
<!-- ev3dev-lang-demo.cpp:523:16: error: no matching function for call to 'ev3dev::led::flash(int)' -->
<!-- l.flash(0); -->
<!-- ^ -->
<!-- ev3dev-lang-demo.cpp:523:16: note: candidate is: -->
<!-- In file included from ev3dev-lang-demo.cpp:22:0: -->
<!-- ev3dev.h:1278:8: note: void ev3dev::led::flash(unsigned int, unsigned int) -->
<!-- void flash(unsigned on_ms, unsigned off_ms); -->
<!-- ^ -->
<!-- ev3dev.h:1278:8: note:   candidate expects 2 arguments, 1 provided -->
<!-- ev3dev-lang-demo.cpp:527:9: error: 'class ev3dev::led' has no member named 'set_on_delay' -->
<!-- l.set_on_delay(interval); l.set_off_delay(interval); -->
<!-- ^ -->
<!-- ev3dev-lang-demo.cpp:527:35: error: 'class ev3dev::led' has no member named 'set_off_delay' -->
<!-- l.set_on_delay(interval); l.set_off_delay(interval); -->
<!-- ^ -->
<!-- Makefile:13: recipe for target 'obj/ev3dev-lang-demo.o' failed -->
<!-- make: *** [obj/ev3dev-lang-demo.o] Error 1 -->

<!-- 2015年8月7日現在、そのままコンパイルするとエラーが出るので、以下の修正を施す必要があります。 -->

<!-- --- a/cpp/ev3dev-lang-demo.cpp -->
<!-- +++ b/cpp/ev3dev-lang-demo.cpp -->
<!-- @@ -520,11 +520,11 @@ void led_action(const char *name, led &l) -->
<!-- l.on(); -->
<!-- break; -->
<!-- case 'f': -->
<!-- -      l.flash(0); -->
<!-- +      l.flash(0, 0); -->
<!-- break; -->
<!-- case 'i': -->
<!-- cout << "interval: "; cin >> interval; cout << endl; -->
<!-- -      l.set_on_delay(interval); l.set_off_delay(interval); -->
<!-- +      l.set_delay_on(interval); l.set_delay_off(interval); -->
<!-- break; -->
<!-- case 't': -->
<!-- { -->

<!-- パッチをあててもよいですが、修正は2か所ですので、直接編集してもよいでしょう。 -->
<!--  -->
<!--  -->
<!-- (brickstrap)root@ev3buntu:/home/openrtm/work/ev3dev-lang/cpp# vi ev3dev-lang-demo.cpp -->
<!-- (brickstrap)root@ev3buntu:/home/openrtm/work/ev3dev-lang/cpp# make all -->

<!-- コンパイルが終了すると、lib の下にはスタティックリンクライブラリ、bin の下には、いくつかのサンプルアプリケーションが生成されます。 -->

<!-- (brickstrap)root@ev3buntu:/home/openrtm/work/ev3dev-lang/cpp# ls lib/ -->
<!-- libev3dev.a -->
<!-- (brickstrap)root@ev3buntu:/home/openrtm/work/ev3dev-lang/cpp# ls bin -->
<!-- button-test  ev3dev-lang-demo  remote_control-test -->
<!-- drive-test   ev3dev-lang-test -->

コンパイルが終了すると build の下にスタティックリンクライブラリ (libev3dev.a)、demos の下にはいくつかのサンプルアプリケーションが生成されます。


## サンプルプログラム 

サンプルプログラムの内容は以下の通りです。
標準セットの構成で使用できる産プロプログラムは、button-test、ev3dev-lang-demo、ev3dev-lang-test で drive-test、remote_control-test には IRセンサーと IRビーコンが必要になります。

<table class="table-alt">
  <tr>
    <td>button-test</td>
    <td>EV3 インテリジェントブロック（本体）のボタン（十字、中央、キャンセル）の ON/OFF を表示するサンプル。</td>
  </tr>
  <tr>
    <td>drive-test</td>
    <td>モード1: IRセンサーを距離センサーとして利用し、障害物がなければ直進、障害物があればターンする自動動作を繰り返す。モード2: IRビーコンを用いた赤外線による遠隔操作モード。(標準セットにはIRセンサー、IRビーコンが付属していません。)</td>
  </tr>
  <tr>
    <td>ev3dev-lang-demo</td>
    <td>メニュー形式で、センサー、モーター、LED、ボタン、サウンド、バッテリー、LCD等のデバイスの様々な機能にアクセスできるでもプログラム。</td>
  </tr>
  <tr>
    <td>ev3dev-lang-test</td>
    <td>libev3dev のテスト用プログラム。センサー、モーター、LEDなどの機能を一通りアクセスし、libev3dev の機能をテストするプログラム。</td>
  </tr>
  <tr>
    <td>remote_control-test</td>
    <td>IRセンサーと IRビーコンを用いたリモートコントロールのでもプログラム。</td>
  </tr>
</table>

## サンプルロプログラムの EV3 へのコピー

実際に EV3 で動作させるために、サンプルプログラムを EV3 にコピーします。EV3 で ev3dev が起動してネットワークにつながっていることを確認してください。クロス開発環境側から以下のようにしてコピーします。

```
 # cd demos ← ev3dev-lang-cpp/demos に移動
 # scp * ev3dev.local:/tmp/ ← ファイルを ev3.local (EV3) の /tmp/ にコピー
```

## サンプルプログラムの実行

そのままターミナルから ev3dev.local にログインしてサンプルプログラムを実行します。

```
 # ssh ev3dev.local
 login: root
 password: r00tme
 # cd /tmp
 # ./ev3dev-lang-demo
 *** main menu ***
 
 (s)ensors
 (m)otors
 (l)eds
 (b)uttons
 s(o)und
 b(a)ttery
 l(c)d
 (q)uit
 
 Choice: 
```


## 自作のプログラムのビルド
自作のプログラムをビルドする際は ev3dev.h のインクルードと libev3dev.a とのリンクする必要があります。
以下は CMakeLists.txt の一例です。


```
 cmake_minimum_required(VERSION 2.8)
 
 set(ev3dev_dir /home/ev3dev-lang-cpp)
 set(ev3dev_lib ${ev3dev_dir}/build/libev3dev.a)
 
 set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11")
 
 project( testEV3 )
 add_executable(testEV3 main.cpp)
 include_directories(${ev3dev_dir})
 target_link_libraries(testEV3 ${ev3dev_lib} pthread)
```
