---
layout: page
title: インストール方法
---
<!-- Title: インストール方法 -->

#contents

rtshellのインストールにはrtshellがPythonのプログラムであるため、OpenRTM-aist-Pythonのインストールが必要になります。
<!-- よって、インストールはOpenRTM-aist-Pythonとrtshellのインストール、およびPythonの実行環境のインストールが必要になる場合があります。(Linuxの一括インストールはそのスクリプトの中でPythonのインストールを行いますが、Windowsのmsiのケースは前もってインストールをする必要があります。なお対応しているPythonのバージョンは[[ダウンロードページ:/ja/download/openrtm-aist-cpp/openrtm-aist-cpp_1_2_2_release#toc1]]をご確認ください。 -->
<!-- ) -->

## Windowsへのインストール
msiインストーラーによるOpenRTM-aistをインストールしてください。手順については下記のページを参照してください。<br>
    - [OpenRTM-aistを10分で始めよう！・OpenRTM-aistのインストール]({{ site.baseurl }}/ja/doc/installation/lets_start#toc2) 


## Linux環境へのインストール

### Ubuntuの場合

一括インストールスクリプトを引数無しで実行すると、rtshell も含めて、C++版、 Python版、 Java版、 OpenRTP(amd64のみ)、 JDK8 がインストールされます。　

OpenRTM-aist 2.0系のインストール時は、下記をシェルプロンプトに貼り付けて実行してください。　
```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh)
```

OpenRTM-aist 1.2系のインストール時は、下記を実行して下さい。
```
 $ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh)
```


### Raspbianの場合
一括インストールスクリプトをダウンロードしたディレクトリに移動し、以下のように入力します。
```
 $ sudo sh pkg_install_raspbian.sh -l c++ -l python -l rtshell --yes
 $ sudo rtshell_post_install
```

なおRaspbianの環境では現状問題が報告されており下記の方法で対処してください。

上記の実行後、sudoをつけないで
```
 $ rtshell_post_install
```

と実行し、最初の２つの問い合わせには下記のように’’n’’と答え、最後の問い合わせのみに**y**と答えてください。
```
 Link man pages? n
 Link documentation? n
 Add shell support to .bashrc? y
```

実行を完了したら、一度ターミナルを閉じてください。

