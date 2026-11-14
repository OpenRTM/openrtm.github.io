---
layout: page
title: openrtm-aist-java-1.1.0-rc1
---

<!-- Title: OpenRTM-aist-Java-1.1.0-RC1 -->
<div align="right"><a href="java_logo.png"><img src="java_logo.png" width="10%;" align="right"></a></div>

#contents
#clear
<br>

## ビルド済みパッケージ
<table class="table-alt">
  <tr>
    <td>jarファイルおよびサンプル</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/java/1.1.0/OpenRTM-aist-Java-1.1.0-RC1-jar.zip">OpenRTM-aist-Java-1.1.0-RC1-jar.zip </a><br>MD5:9AB2440D42C66042ACB5B36226839168</td>
    <td>2011.10.05</td>
  </tr>
  <tr>
    <td>Windows用インストーラ</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/java/OpenRTM-aist-Java-1.1.0-RC1.msi">OpenRTM-aist-Java-1.1.0-RC1.msi </a><br>MD5:6C89B80A9BF96F73393D4D2E583AAB92</td>
    <td>2011.10.05</td>
  </tr>
</table>

- Windowsをご利用の方はmsiでのインストールを推奨します。[インストール方法]({{ site.baseurl }}/ja/doc/installation/install_1_1/java_1_1/install_windows_java_1_1)
- **jarファイルおよびサンプル**はWindowsとUNIX両方で利用可能です。

## Java開発環境

OpenRTM-aist-Java-1.1.0の動作および開発には以下のいずれかのJDKが必要です。
- JDK5 (1.5): [ダウンロード](http://www.oracle.com/technetwork/java/javasebusiness/downloads/java-archive-downloads-javase5-419410.html)
- JDK6 (1.6): [ダウンロード](http://www.oracle.com/technetwork/java/javase/downloads/jdk-6u32-downloads-1594644.html)
- 参考: [Java Archive](http://www.oracle.com/technetwork/java/archive-139210.html)

JDK6よりも新しいバージョンでも動作する可能性もありますが、配布のmsiインストーラではJDK5またはJDK6のインストールを確認するため、JDK5,6のいずれかがインストールされている必要があります。
JDK6,5以外のJavaをお使いの場合は、zipアーカイブをダウンロードの上、[手動でインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/java_1_1/install_windows_java_1_1#toc10)してください。


## リリースノート: Java-1.1.0-RC1
- APIの追加
  - コールバックAPI
  - 実行コンテキストに関するコールバック
- rtc.conf新オプション(-o)の導入
- ECのrateをrtc.confで与えられるよう変更
- SDOサービスフレームワーク
- オブザーバSDOサービスの導入(実験的)
- 雑多なバグフィックス

<!-- 
## 過去のバージョン
- [1.0.0-RELEASE]()（リンク切れです）
- [1.0.0-RC1]()（リンク切れです）
- [Java-0.4.2-RELEASE]()（リンク切れです）
- [Java-0.4.1-RELEASE]()（リンク切れです）
- [0.4.1-RC1]()（リンク切れです）
-->
