---
layout: page
title: ubuntu/debianへのインストール
---

<!-- Ubuntu/Debianへのインストール -->

#contents

<div align="right"><a href="ubuntu_logo2.png"><img src="ubuntu_logo2.png" width="15%;" align="right"></a></div>



Python 版 OpenRTM-aist は Ubuntu や Debian GNU Linuxで利用可能な deb パッケージが提供されています。
対応しているディストリビューションのバージョンは、ダウンロードページから確認できます。
Ubuntu/Debian GNU Linux への対応およびそのバージョンは、予告なしに変更または停止されることがありますので、予めご了承ください。

インストールの方法には大きく分けて以下の二種類のインストール方法があります。

- openrtm.org が提供する一括インストールスクリプトを使用
- apt-get や synaptic パッケージマネージャを使用

好みの方法でインストールしてください。

## 一括インストール・スクリプトを使う方法

openrtm.org が提供するインストール・スクリプト **pkg_install_ubuntu.sh** または **pkg_install_debian.sh** をダウンロードページからダウンロードし、root 権限で実行します。
このスクリプトは、必要なパッケージを順次 apt-get でインストールしていきます。

<!-- -[[パッケージインストールスクリプト:http://www.openrtm.org/OpenRTM-aist/download/install_scripts/]] -->
<!-- -[[パッケージインストールスクリプト:http://www.openrtm.org/openrtm/ja/node/932#linuxpkg]] -->
<!-- -[[ソースコードリポジトリ上の最新スクリプト:http://svn.openrtm.org/OpenRTM-aist-Python/trunk/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh]] -->
<!-- -[[一括インストールスクリプト(Ubuntu):http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh]] -->
<!-- -[[一括インストールスクリプト(Debian):http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_0/OpenRTM-aist-Python/installer/install_scripts/pkg_install_python_debian.sh]] -->

- [一括インストールスクリプト(Ubuntu)](http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_ubuntu.sh)
- [一括インストールスクリプト(Debian)](http://svn.openrtm.org/OpenRTM-aist/trunk/OpenRTM-aist/build/pkg_install_debian.sh)

OpenRTM-aist を開発・実行するために必要なパッケージをもれなくインストールしてくれるので大変便利です。
<!-- 初めて OpenRTM-aist をインストールしてみる方にお勧めします。 -->
オプションを指定することで、目的に合わせたパッケージをインストールできるようになったので、
初めて OpenRTM-aist をインストールしてみる方にもソースをコンパイルしてみる方にもお勧めします。

ただし、OpenRTM-aist 関係のすべてのパッケージをインストールするので、必要ないものもインストールされる可能性があります。
詳しく理解している人は、手動でインストールした方がよいでしょう。

詳しいインストール方法や、オプション・パッケージの種類につきましては、[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script) をご確認ください。

<!-- 以下、一括インストールスクリプトを使用したインストールの手順です。 -->
<!-- （pkg_install_debian.sh のオプション設定も同じ） -->

<!-- > wget [pkg_install_ubuntu.sh のダウンロードURL] -->
<!-- > su -->
<!-- # sh pkg_install_ubuntu.sh -l python -d -->
<!-- //途中、いくつかの質問をたずねられるので、''y'' あるいは ''Y'' を入力しながら完了させる。 -->
<!-- //オプション "--yes" を追加することで省略も可能。 -->

## apt-get を使う方法&aname(apt_get);

### source.list の編集

openrtm.org では apt-get から利用可能なパッケージリポジトリを提供しています。
ただし、デフォルトのパッケージリポジトリには含まれていませんので、apt-get の設定を変更する必要があります。

/etc/apt/sources.list に以下の行を追加します。

 > su
```
 # vi /etc/apt/sources.list # "sources.list" を編集
```

```
  deb http://openrtm.org/pub/Linux/ubuntu/ (code name) main
  または
  deb http://openrtm.org/pub/Linux/debian/ (code name) main
```

の1行を追加。"(code name)" の部分には以下の debian/ubuntu のバージョンに対応したコードネームを指定します。

<table class="table-alt">
  <tr>
    <th>バージョン</th>
    <th>code name</th>
  </tr>
  <tr>
    <td>></td>
    <td>Debian GNU Linux</td>
  </tr>
  <tr>
    <td>Debian 7.0</td>
    <td>wheezy</td>
  </tr>
  <tr>
    <td>Debian 8.0</td>
    <td>jessie</td>
  </tr>
  <tr>
    <td>Debian 9.0</td>
    <td>stretch</td>
  </tr>
  <tr>
    <td>></td>
    <td>Ubuntu</td>
  </tr>
  <tr>
    <td>Ubuntu 14.04</td>
    <td>trusty</td>
  </tr>
  <tr>
    <td>Ubuntu 16.04</td>
    <td>xenial</td>
  </tr>
  <tr>
    <td>Ubuntu 16.10</td>
    <td>yakkety</td>
  </tr>
  <tr>
    <td>Ubuntu 17.04</td>
    <td>zesty</td>
  </tr>
</table>

### apt-get によるインストール

次の手順でインストールを行います。途中、いくつかの応答を求められるので、**y** を入力しながら完了させてください。

```
 # apt-get update
 # apt-get install python
 # apt-get install python-omniorb-omg omniidl-python
 # apt-get install openrtm-aist-python openrtm-aist-python-example
```

なお、インストール済みの OpenRTM-aist を特定バージョンのまま保持したい場合には、**/etc/apt/preferences**を編集して以下の行を追加します。
（この例では1.0系列にバージョンを固定します。）

```
 Package: OpenRTM-aist-Python
 Pin: version 1.0.*
```

詳しくは
http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.ja.html#s-pin
を参照してください。

### インストールの確認

インストールを確認します。

```
 $ dpkg -l 'openrtm*'
 要望=(U)不明/(I)インストール/(R)削除/(P)完全削除/(H)保持
```
<table class="table-alt">
  <tr>
    <th>状態=(N)無/(I)インストール済/(C)設定/(U)展開/(F)設定失敗/(H)半インストール/(W)トリガ待ち/(T)トリガ保留</th>
  </tr>
  <tr>
    <td>/ エラー?=(空欄)無/(R)要再インストール (状態,エラーの大文字=異常)</td>
  </tr>
  <tr>
    <td>/ 名前                         バージョン          アーキテクチャ      説明</td>
  </tr>
</table>
 +++-============================-===================-===================-=============================================================
```
 ii  openrtm-aist-python          1.1.0-2             i386                OpenRTM-aist is a reference implementation of RT-Middleware
 ii  openrtm-aist-python-example  1.1.0-2             i386                OpenRTM-aist-Python examples
```

## パッケージの詳細
各パッケージの内容は以下の通りです。

### openrtm-aist-python
openrtm-aist-python には Python モジュールとコマンド群が含まれています。

- コマンド
```
 /usr/bin/rtcprof_python
 /usr/bin/rtcd_python
```

- 設定ファイルサンプル
<!-- /usr/lib/python<version>/dist-packages/OpenRTM_aist/examples/rtc.conf.sample -->
```
 /usr/etc/rtc.conf.sample
```

- OpenRTM-aist 本体の Python モジュール
```
 /usr/lib/python<version>/dist-packages/OpenRTM_aist/*
```

- OpenRTM-aist のユーティリティモジュール
```
 /usr/lib/python<version>/dist-packages/OpenRTM_aist/utils/rtcprof
 /usr/lib/python<version>/dist-packages/OpenRTM_aist/utils/rtcd
 /usr/lib/python<version>/dist-packages/OpenRTM_aist/utils/rtc-template
 /usr/lib/python<version>/dist-packages/OpenRTM_aist/utils/rtm-naming
```

### openrtm-aist-python-example
openrtm-aist-python-exampleには RTC のサンプルが含まれています。

- サンプル
```
 /usr/share/openrtm-1.1/example/python/SimpleIO/
 /usr/share/openrtm-1.1/example/python/SimpleService/
 中略
```

以上、インストールが終了しましたら、[動作確認]({{ site.baseurl }}/ja/doc/installation/install_1_1/python_1_1/test_linux_python_1_1)へ進みましょう。
