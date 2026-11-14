---
layout: page
title: "download"
---

<!-- Title: ダウンロード -->

### 現在の最新RELEASEバージョン: 2.1.0-RELEASE

現在の最新RELEASEバージョンは OpenRTM-aist-2.1.0-RELEASE です。

- **リリースノート**
  - **[C++ ](https://github.com/OpenRTM/OpenRTM-aist/releases/tag/v2.1.0)**
  - **[Python ](https://github.com/OpenRTM/OpenRTM-aist-Python/releases/tag/v2.1.0)**
  - **[Java ](https://github.com/OpenRTM/OpenRTM-aist-Java/releases/tag/v2.1.0)**
  - **[tools (OpenRTP) ](https://github.com/OpenRTM/OpenRTP-aist/releases/tag/v2.1.0)**

### Windowsインストーラ

64bit版のみの提供です。ダウンロードしたmsiを実行すると、C++版、 Python版、 Java版、 OpenRTP、 rtshell、OpenCV4.13.0、omniORB4.3.4、JRE8 がインストールされます。 

<table class="table-alt">
  <tr>
    <th><a href="https://openrtm.org/pub/Windows/OpenRTM-aist/2.1/OpenRTM-aist-2.1.0-RELEASE_x86_64.msi">OpenRTM-aist-2.1.0-RELEASE_x86_64.msi </a></th>
    <th>MD5:e1804a5aaa4fab85a5cdc777bd9c48c1</th>
    <th>2026/06/02</th>
  </tr>
</table>

Microsoft Edge をお使いでダウンロードできない場合は、下記ページの解説をご覧ください。
- [OpenRTM-aistを10分で始めよう！・OpenRTM-aistのダウンロード]({{ site.baseurl }}/ja/doc/installation/lets_start#toc2)  

必要なソフトウエアである Visual Studio と Python は下記バージョンに対応しています。
- Visual Studio（2019, 2022, 2026）
- Python （3.10, 3.11, 3.12, 3.13, 3.14）

Windowsの場合、コマンドプロンプトでPythonのバージョン番号が表示されることを確認して下さい。 <br>
表示されない場合は、[WindowsでPythonをインストールしてもバージョン番号が表示されない]({{ site.baseurl }}/ja/doc/faq/faq_install#toc1) をご覧ください。

インストールに関しては、[2.1系のWindowsへのインストール]({{ site.baseurl }}/ja/doc/installation/install_2_1/install_win_2_1) をご覧ください。　<br>
初めてインストールされる場合は、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/lets_start) をご覧ください。

### Linuxパッケージ

<!-- 既に1.2系をご利用されている場合は、インストール前に [[2.1系での変更点:/ja/doc/installation/install_2_1/install_linux_2_1/install_2_1#toc0]] をご覧ください。　&br; -->

Ubuntu22.04、24.04（各amd64、arm64環境）では、下記をシェルプロンプトに貼り付けて実行すると、C++版、 Python版、 Java版、 OpenRTP(amd64のみ)、 rtshell、JDK8 がインストールされます。 

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

インストールに関しては、[2.1系のLinuxへのインストール]({{ site.baseurl }}/ja/doc/installation/install_2_1/install_linux_2_1)をご覧ください。

### Raspberry Pi OSパッケージ

<!-- 既に1.2系をご利用されている場合は、インストール前に [[2.1系での変更点:/ja/doc/installation/install_2_1/install_raspbian_2_1#toc0]] をご覧ください。　&br; -->

Bookworm（64bit環境）では、下記をシェルプロンプトに貼り付けて実行すると、C++版、 Python版、 Java版、 rtshell がインストールされます。 

```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh)
```

インストールに関しては、[2.1系のRaspberry Pi OSへのインストール]({{ site.baseurl }}/ja/doc/installation/install_2_1/install_raspbian_2_1)をご覧ください。

### Macパッケージ

Mac環境へはC++版、 Python版、 OpenRTPをインストールできます。手順は下記ページのREADMEをご覧ください。　<br>
https://github.com/OpenRTM/homebrew-openrtm2

### 旧バージョン
#### 2.0.2
- [OpenRTM 2.0.2]({{ site.baseurl }}/ja/download/download_202_release) 
#### 1.2.2
- [OpenRTM-aist C++ 1.2.2-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-cpp/openrtm-aist-cpp_1_2_2_release)
- [OpenRTM-aist Python 1.2.2-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-python/openrtm-aist-python_1_2_2_release)
- [OpenRTM-aist Java 1.2.2-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-java/openrtm-aist-java_1_2_2_release)
- [OpenRTP 1.2.2]({{ site.baseurl }}/ja/download/tools/openrtp_1_2_2)

#### 1.2.1
- [OpenRTM-aist C++ 1.2.1-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-cpp/openrtm-aist-cpp_1_2_1_release)
- [OpenRTM-aist Python 1.2.1-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-python/openrtm-aist-python_1_2_1_release)
- [OpenRTM-aist Java 1.2.1-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-java/openrtm-aist-java_1_2_1_release)
- [OpenRTP 1.2.1]({{ site.baseurl }}/ja/download/tools/openrtp_1_2_1)

#### 1.1.2
- [OpenRTM-aist C++ 1.1.2-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-cpp/openrtm-aist-cpp_1_1_2_release)
- [OpenRTM-aist Python 1.1.2-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-python/openrtm-aist-python_1_1_2_release)
- [OpenRTM-aist Java 1.1.2-RELEASE]({{ site.baseurl }}/ja/download/openrtm-aist-java/openrtm-aist-java_1_1_2_release)
- [OpenRTP 1.1.2]({{ site.baseurl }}/ja/download/tools/openrtp_1_1_2)

#### [各種仕様]({{ site.baseurl }}/ja/download/various_specs)
