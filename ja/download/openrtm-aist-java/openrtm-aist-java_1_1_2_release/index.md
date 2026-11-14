---
layout: page
title: openrtm-aist-java-1.1.2-release
---

<!-- Title: OpenRTM-aist-Java-1.1.2-RELEASE -->
<div align="right"><a href="java_logo.png"><img src="java_logo.png" width="100;" align="right"></a></div>

#contents
#clear
<br>

<!-- -&color(red){まだリリースしておりません。準備中です。もうしばらくお待ち下さい。}; -->

## パッケージ
### Windows インストーラー

#### 32bit 用

<table class="table-alt">
  <tr>
    <td>Windows 用インストーラー<br> (OpenRTM-aist C++、Python、Java版,<br> および OpenRTP、rtshell (4.1.0) 含む)</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/1.1/OpenRTM-aist-1.1.2-RELEASE_x86.msi">OpenRTM-aist-1.1.2-RELEASE_x86.msi</a> <br>MD5:59be8603f3fc007c2aed4476052886ce</td>
    <td>2016/05/27</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi">python-2.7.10.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python 2.7.10 推奨。2.7.11は PYTHONPATH 等環境変数の設定が必要な場合があります。</span>;
- <span style="color:red;">※ 古い rtshell は事前に削除しておいてください。</span>;

#### 64bit用

<table class="table-alt">
  <tr>
    <td>Windows用インストーラー<br> (OpenRTM-aist C++,Python,Java版,<br> および OpenRTP,rtshell(4.1.0)含む)</td>
    <td><a href="http://openrtm.org/pub/Windows/OpenRTM-aist/1.1/OpenRTM-aist-1.1.2-RELEASE_x86_64.msi">OpenRTM-aist-1.1.2-RELEASE_x86_64.msi</a> <br>MD5:ee8db7c1682cb21dce963207e0484fb3</td>
    <td>2016/05/27</td>
  </tr>
  <tr>
    <td>Python-2.7</td>
    <td><a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.amd64.msi">python-2.7.10.amd64.msi</a></td>
    <td><a href="https://www.python.org">python.org</a></td>
  </tr>
</table>

- <span style="color:red;">※ Python 2.7.10 推奨。2.7.11は PYTHONPATH 等環境変数の設定が必要な場合があります。</span>;
- <span style="color:red;">※ 古い rtshell は事前に削除しておいてください。</span>;

インストールについては、[OpenRTM-aistを10分で始めよう！]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_windows_1_1/quick_start_1_1_2) のページで手順を紹介しています。<br>


### Linux パッケージ

<table class="table-alt">
  <tr>
    <td>jar ファイルおよびサンプル</td>
    <td><a href="https://openrtm.org/pub/OpenRTM-aist/java/1.1.2/OpenRTM-aist-Java-1.1.2-RELEASE-jar.zip">OpenRTM-aist-Java-1.1.2-RELEASE-jar.zip</a> <br>MD5:e89979be5c43c07c3c72c90233b84ad7</td>
    <td>2016.05.27</td>
  </tr>
</table>


<!-- - Windows をご利用の方は msi でのインストールを推奨します。 -->
<!-- - ''jar ファイルおよびサンプル''は Windows と UNIX 両方で利用可能です。 -->





## Java 開発環境

OpenRTM-aist-Java-1.1.2の動作および開発には以下の JDK が必要です。
<!-- - JDK7 (1.7): -->
- JDK8 (1.8): [ダウンロード](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
- 参考: [Java Archive](http://www.oracle.com/technetwork/java/archive-139210.html)

<!-- JDK6 よりも新しいバージョンでも動作する可能性もありますが、配布の msiインストーラでは JDK5 または JDK6 のインストールを確認するため、JDK5、6 のいずれかがインストールされている必要があります。 -->
<!-- JDK6、5 以外の Java をお使いの場合は、zip アーカイブをダウンロードの上、[[手動でインストール:http://openrtm.org/openrtm/ja/content/windows%E3%81%B8%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB-1#toc10]]してください。 -->


## リリースノート: Java-1.1.2-RELEASE
- 雑多なバグフィックス
- Windows インストーラーで Java版、C++版、Python版、rtshell も同時にインストール可能
