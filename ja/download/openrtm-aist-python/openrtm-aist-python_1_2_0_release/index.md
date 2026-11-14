---
layout: page
title: openrtm-aist-python-1.2.0-release
---

<!-- Title: OpenRTM-aist-Python-1.2.0-RELEASE -->
<div align="right"><a href="python-logo.png"><img src="python-logo.png" width="20%;" align="right"></a></div>
#contents(4)
<br>
<br>
<br>

<!-- ** &color(blue){まだリリースしておりません。準備中です。もうしばらくお待ち下さい。}; -->

<br>
インストール手順については以下のページを参照してください。

- [OpenRTM-aist (Python版) 1.2系のインストール]({{ site.baseurl }}/ja/doc/installation/install_1_2/python_1_2)
## パッケージ
### Windows インストーラー

#### 32bit用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist、C++、Python、<br>Java版、および OpenRTP、<br>rtshell(4.2.2) 含む)<br>(Visual Studio 2008、2010、<br>2012、2013、2015、2017 共通)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86.msi">OpenRTM-aist-1.2.0-RELEASE_x86.msi</a> <br>MD5:abef26d7b3fa89f1ed8c7b96ea1a452b</td>
    <td>2019/03/15</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi">python-2.7.16.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe">python-3.6.8.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe">python-3.7.3.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python は、"2.7"  "3.6"  "3.7" のいずれかのバージョンをインストールして下さい。</span>;
- <span style="color:red;">※ 古い rtshell は事前に削除しておいてください。ただし、OpenRTM-aist 1.1.2版をmsiでインストールしている場合は対応不要です。</span>;

#### 64bit用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist、C++、Python、<br>Java版、および OpenRTP、<br> rtshell (4.2.2) 含む)<br>(Visual Studio 2010、2012、<br> 2013、2015、2017 共通)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist/releases/download/v1.2.0/OpenRTM-aist-1.2.0-RELEASE_x86_64.msi">OpenRTM-aist-1.2.0-RELEASE_x86_64.msi</a> <br>MD5:7a2670eb70a3e53abc819fa722be690a</td>
    <td>2019/03/15</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi">python-2.7.16.amd64.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.6</td>
    <td><a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe">python-3.6.8-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
  <tr>
    <td>Python-3.7</td>
    <td><a href="https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe">python-3.7.3-amd64.exe</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python は、"2.7"  "3.6"  "3.7" のいずれかのバージョンをインストールして下さい。</span>;
- <span style="color:red;">※ 古い rtshell は事前に削除しておいてください。ただし、OpenRTM-aist 1.1.2版をmsiでインストールしている場合は対応不要です。</span>;

インストールについては、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/lets_start121) のページで手順を紹介しています。<br>

### （重要なお知らせ）OpenRTM-aistインストール後の設定

- Pythonのインストール先によっては、rtshellのexeコマンド実行時にエラーとなることが判明しました
- 下記手順で更新して頂ければ改善します

```
  pip uninstall rtshell rtctree rtsprofile
  pip install rtshell-aist
```

### Linux パッケージ

現在のところ、以下のディストリビューション・バージョンでパッケージを提供しています。<br>
以下で配布しているインストールスクリプトを利用すれば、必要なパッケージを一括でインストールすることができます。

<table class="table-alt">
  <tr>
    <th>ディストリビューション・バージョン</th>
    <th>一括インストールスクリプト</th>
  </tr>
  <tr>
    <td>Ubuntu 14.04 (trusty) i386/amd64 <br>  Ubuntu 16.04 (xenial) i386/amd64 <br> Ubuntu 18.04 (bionic) amd64 <br> Ubuntu 18.10 (cosmic) amd64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh">pkg_install_ubuntu.sh </a></td>
  </tr>
  <tr>
    <td>Debian  8.0  (jessie) i386/amd64 <br> Debian  9.0  (stretch) i386/amd64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_debian.sh">pkg_install_debian.sh </a></td>
  </tr>
  <tr>
    <td>Fedora 27 i686/x86_64 <br> Fedora 28 i686/x86_64 <br> Fedora 29 i686/x86_64</td>
    <td><a href="https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_fedora.sh">pkg_install_fedora.sh </a></td>
  </tr>
</table>

オプションを指定することで、目的に合わせたパッケージをインストールすることができるようになりました。インストール方法やオプション、パッケージの種類につきましては、[一括インストール・スクリプト]({{ site.baseurl }}/ja/doc/appendix/bulk_installation_script) をご確認ください。

## ソースコード

<table class="table-alt">
  <tr>
    <td>Python版ソースコード</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python-1.2.0.tar.gz">OpenRTM-aist-Python-1.2.0.tar.gz</a> <br>MD5:6ef5853259aebd07e8d7985b93b0090c</td>
    <td>2019/03/15</td>
  </tr>
  <tr>
    <td>Python版ソースコード(Win32)</td>
    <td><a href="https://github.com/OpenRTM/OpenRTM-aist-Python/releases/download/v1.2.0/OpenRTM-aist-Python-1.2.0.zip">OpenRTM-aist-Python-1.2.0.zip</a> <br>MD5:bafe866f294064f2eb1894b5e79c425e</td>
    <td>2019/03/15</td>
  </tr>
</table>

<br>

## リリースノート: 1.2.0-RELEASE

RTミドルウエア：OpenRTM-aist の Python言語版最新バージョン 1.2.0-RELEASE をリリースいたしました。

OpenRTM-aist Official Website からソースコード、Windows インストーラー、Linux 用パッケージ等が LGPL ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

### 機能に関する変更
- 雑多なバグフィックス
- マネージャ起動時にポートを接続する機能
- マネージャ起動時にコンポーネントをアクティベーションする機能
- CORBA_RTCUtil：コンポーネント操作関数群の導入
- トピックベースのポート接続機能
- 共有メモリ通信データポート(shared_memory型インターフェース)
- 同一プロセス内通信のデータ転送を変数で渡すダイレクト接続データポート(direct型インターフェース)
- OpenSSLによるセキュアな通信機能
- 名前付けポリシー機能の拡張(同一ネームサーバー、同一ノードで独自のインスタンス名を設定する)
- rtcloc形式のコンポーネント指定方法(マスターマネージャに登録されたスレーブマネージャからコンポーネントを名前で検索)
- rtcname形式のコンポーネント指定方法(ネームサーバーに登録されたコンポーネントを名前で検索)
- デフォルトでデータポートの二重接続を許可しない機能
- LogstreamBase：ロガー機能の拡張
- Fluent Bitによるログ収集機能
- コンポーネントオブザーバのデータ入出力検知機能
- モジュール探索パスのサブディレクトリのモジュールを探索する機能

### ユーザービリティに関する変更
- Windows インストーラーで omniORBpy を 4.2.3 に更新

### 動作条件
- サポートする Python バージョン： 2.7、3.6、3.7
- 動作確認済みOS
  - Debian 8.0 i386, amd64
  - Debian 9.0 i386, amd64
  - Ubuntu 14.04 i386, amd64
  - Ubuntu 16.04 i386, amd64
  - Ubuntu 18.04 amd64
  - Ubuntu 18.10 amd64
  - Fedora release 27 i686, x86_64
  - Fedora release 28 i686, x86_64
  - Fedora release 29 i686, x86_64
  - Windows-7 (32/64bit)
  - Windows-8.1 (32/64bit)
  - Windows-10 (32/64bit)
