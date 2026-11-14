---
layout: page
title: 動作確認(linux編)
---

<!-- Titile: 動作確認(Linux編) -->

#contents

## サンプルコンポーネントを実行する

インストールが正常に終了したら、付属のサンプルコンポーネントで動作を確認できます。 サンプルコンポーネントのインストール先は以下です。

```
 /usr/share/openrtm-2.1/components/c++/examples
 /usr/share/openrtm-2.1/components/python3/
 /usr/share/openrtm-2.1/components/java
```

RTCの操作、RTシステムの構築を行うためのツールOpenRTPを起動します。

- OpenRTM-aist 2.x系は、openrtp2 コマンドで起動します

```
 $ openrtp2
```

<!-- OpenRTM-aist 1.2系では openrtp コマンドで起動します。コマンド名は異なりますが、起動手順、使い方は 1.2系と変更ありませんので、詳細は以下のページをご覧ください。 -->
<!-- - [[OpenRTPの起動手順(1.2系、Linux):/node/6654]] -->
<!--  -->
<!-- ※OpenRTPは1.2系と2.0系の共存が可能です。このため、openrtp と openrtp2 の両方を実行することは可能です。  -->

付属のサンプルコンポーネントについては、以下のページでWindows版の一覧を記載しています。コンポーネントの動作についてはWindows版・Linux版に違いはございません。
- [サンプルコンポーネント一覧]({{ site.baseurl }}/ja/doc/installation/install_2_0/install_windows_2_0/check_windows_2_0#toc1)

Linux環境でのサンプルコンポーネントの実行手順について、もう少し詳しく知りたい場合は、以下の1.2系の解説ページをご覧ください。コンポーネントのパスを読み替えていただければ実行手順は2.x系も同じです。
- [OpenRTM-aist(C++版)1.2系・動作確認(Linux編)]({{ site.baseurl }}/ja/doc/installation/install_1_2/cpp_1_2/check_linux_1_2)
- [OpenRTM-aist(Python版)1.2系・動作確認(Linux編)]({{ site.baseurl }}/ja/doc/installation/install_1_2/python_1_2/check_python_linux_1_2)
- [OpenRTM-aist(Java版)1.2系・動作確認(Linux編)]({{ site.baseurl }}/ja/doc/installation/install_1_2/java_1_2/check_linux_java_1_2)

## OpenCVサンプルコンポーネントのインストール

OpenCVのC++サンプルコンポーネントはインストール用debパッケージを提供しておりません。ソースからdebパッケージを生成するスクリプトを提供しておりますのでビルド・インストールしてください。

### OpenCV4.5.4のインストール例

バージョン4.5.4のOpenCV本体と拡張モジュール群（opencv_contrib）を合わせてビルド・インストールする例です。

- まず、/etc/apt/sources.listの以下の deb-src 行をコメントインしておきます。

```
 $ sudo vi /etc/apt/sources.list
      :
 deb-src http://jp.archive.ubuntu.com/ubuntu/ *** universe
    or
 deb-src http://us.archive.ubuntu.com/ubuntu/ *** universe
```

- 下記コマンドの実行でOpenCVのインストールが完了します。

```
 sudo apt build-dep opencv
 wget https://github.com/opencv/opencv/archive/refs/tags/4.5.4.tar.gz -O opencv-4.5.4.tar.gz
 tar xvzf opencv-4.5.4.tar.gz
 wget https://github.com/opencv/opencv_contrib/archive/refs/tags/4.5.4.tar.gz -O opencv_contrib-4.5.4.tar.gz
 tar xvzf opencv_contrib-4.5.4.tar.gz
 cd opencv-4.5.4
 mkdir build
 cd build
 cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.5.4/modules -DBUILD_opencv_java=OFF ..
 make -j$(nproc)
 sudo make install
 sudo ldconfig
```

### OpenCVサンプルコンポーネントのビルド手順

ソースのImageProcessingを取得してビルドし、debパッケージを生成します。

```
 git clone https://github.com/OpenRTM/ImageProcessing
 cd ImageProcessing/opencv
 mkdir build
 cd build
 cmake ..
 ./build_linux_package.sh
```

これで、imageprocessing_2.x.x_amd64.deb が生成されますのでインストールします。

```
 sudo dpkg -i imageprocessing_2.x.x_amd64.deb
 ls /usr/share/openrtm-2.0/components/c++/opencv-rtcs/
 Affine                       CameraViewer     Edge         Histogram         ImageSubtraction  Perspective        Scale                 Template
 BackGroundSubtractionSimple  Chromakey        Findcontour  Hough             ObjectTracking    RockPaperScissors  Sepia                 Translate
 Binarization                 DilationErosion  Flip         ImageCalibration  OpenCVCamera      Rotate             SubtractCaptureImage  rtc.conf
```

各サンプルディレクトリ下に実行ファイル（`***Comp`）がインストールされていますので、実行してみてください。 





