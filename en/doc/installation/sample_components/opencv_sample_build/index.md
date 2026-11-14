---
layout: page
title: LinuxにおけるOpenCVサンプルのビルド手順
---

<!-- Title: LinuxにおけるOpenCVサンプルのビルド手順 -->

Linuxにおいては一括インストールスクリプトの実行ではOpenCVサンプルコードはインストールされません。サンプルコードのインストールのためには、githubリポジトリよりソースコードを入手してビルドする必要があります。手順は以下のようになります。

- OpenRTM-aistを[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)を用いてインストールしてください。(以下の手順の実行にはC++版とPython版が必要になります。また、実際に動作させる場合にはOpenrtpが必要になることが多いかと思われます。それに合わせてオプションを指定してください。)  例えば
```
 $ sudo sh pkg_install_ubuntu.sh -l all --yes
```
- OpenCV3.4以降をインストールする。(現状では3.4.5のみがテストされています。インストールにはソースコードビルドが必要なこともあります。)
- 以下の手順でソースコードを入手してビルドしてください。
```
 $ sudo apt-get install git
 $ git clone https://github.com/OpenRTM/ImageProcessing.git
 $ cd ImageProcessing/opencv
 $ mkdir build
 $ cd build
 $ cmake ..
 $ make
 $ ./build_linux_package.sh
 $ sudo dpkg -i imageprocessing_1.2.1_amd64.deb
```



