---
layout: page
title: installation procedure
---
<!-- Title: インストール方法 -->

#contents

Since rtshell is a Python program, installing OpenRTM-aist-Python is required in order to install rtshell.

<!-- よって、インストールはOpenRTM-aist-Pythonとrtshellのインストール、およびPythonの実行環境のインストールが必要になる場合があります。(Linuxの一括インストールはそのスクリプトの中でPythonのインストールを行いますが、Windowsのmsiのケースは前もってインストールをする必要があります。なお対応しているPythonのバージョンは[[ダウンロードページ:/ja/download/openrtm-aist-cpp/openrtm-aist-cpp_1_2_2_release#toc1]]をご確認ください。 -->
<!-- ) -->

## Installation on Windows

Install OpenRTM-aist using the MSI installer. For installation instructions, refer to the following page.<br>

- [Getting Started with OpenRTM-aist in 10 Minutes! - Installing OpenRTM-aist]({{ site.baseurl }}/en/doc/installation/lets_start#toc2)

## Installation on Linux

### Ubuntu

When the all-in-one installation script is executed without arguments, rtshell, the C++ edition, Python edition, Java edition, OpenRTP (amd64 only), and JDK8 are installed.

To install OpenRTM-aist 2.0 series, paste and execute the following command in a shell prompt.

```bash
$ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

To install OpenRTM-aist 1.2 series, execute the following command.

```bash
$ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh)
```

### Raspbian

Move to the directory where the all-in-one installation script was downloaded, and enter the following commands.

```bash
$ sudo sh pkg_install_raspbian.sh -l c++ -l python -l rtshell --yes
$ sudo rtshell_post_install
```

Please note that issues have currently been reported in the Raspbian environment. Use the following workaround.

After executing the commands above, run the following command **without sudo**.

```bash
$ rtshell_post_install
```

For the first two prompts, answer **n** as shown below, and answer **y** only for the final prompt.

```text
Link man pages? n
Link documentation? n
Add shell support to .bashrc? y
```

After completing the execution, close the terminal once.

