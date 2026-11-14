---
layout: page
title: openrtm-aist-java-1.0.0-release
---

<!-- Title: OpenRTM-aist-Java-1.0.0-RELEASE  -->
<div align="right"><a href="java_logo.png"><img src="java_logo.png" width="10%;" align="right"></a></div>

#contents
#clear
<br>

## ビルド済みパッケージ

<table class="table-alt">
  <tr>
    <td>jarファイルおよびサンプル</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/java/1.0.0/OpenRTM-aist-Java-1.0.0-jar.zip">OpenRTM-aist-Java-1.0.0-jar.zip </a><br>MD5:B1C538B3BAA390A895E90E033E6D0D87</td>
    <td>2010.05.11</td>
  </tr>
  <tr>
    <td>Windows用インストーラ</td>
    <td><a href="http://www.openrtm.org/pub/Windows/OpenRTM-aist/java/OpenRTM-aist-Java-1.0.0.msi">OpenRTM-aist-Java-1.0.0.msi </a><br>MD5:1EB7EE0241A59B6FCEABE0EE7ADE50B3</td>
    <td>2010.05.11</td>
  </tr>
</table>

- Windowsをご利用の方はmsiでのインストールを推奨します。
- **jarファイルおよびサンプル**はWindowsとUNIX両方で利用可能です。

## ソースコード&aname(source);
<table class="table-alt">
  <tr>
    <td>ソースコード</td>
    <td><a href="http://www.openrtm.org/pub/OpenRTM-aist/java/1.0.0/OpenRTM-aist-Java-1.0.0-RELEASE.tar.gz">OpenRTM-aist-Java-1.0.0-RELEASE.tar.gz </a><br>MD5:5A0FD25EB9CE87D72F0B377B3D24A43A</td>
    <td>2010.05.11</td>
  </tr>
</table>



<br>
## Java開発環境
OpenRTM-aist-Java-1.0.0は動作および開発に以下のJDKを必要とします。利用する際は予めJDKをインストールしてください。
- [JDK5.0: Java SE Development Kit Webページ](http://java.sun.com/javase/downloads/index_jdk5.jsp)


<br>

&aname(note);
## リリースノート: Java-1.0.0-RELEASE
RTミドルウエア：OpenRTM-aist のJava言語版最新バージョン 1.0.0 をリリースいたしました。今回のリリースでは、2008年4月に公式な国際標準となった OMG RTC Specification version 1.0 へ正式に準拠いたしました。

OpenRTM-aist Official Website からソースコード、Windowsインストーラ等が EPL (Eclipse Public License) ライセンスもしくは産総研との個別契約のうち一つから選択するデュアルライセンス方式で利用可能です。

どなたでもすぐにサンプルを実行して試用可能となっております。ぜひお試しください。

- [OpenRTM-aist-Java-1.0.0-RELESE.tar.gz](http://www.openrtm.org/pub/OpenRTM-aist/java/1.0.0/OpenRTM-aist-Java-1.0.0-RELEASE.tar.gz) -- 2010.05.11リリース 
  - OMG RTC Specification v1.0 準拠
  - 新データポート導入 (corba_cdrインターフェース型)
    - push型・pull型データフローの導入
    - サブスクリプション型の導入
    - 送信ポリシの導入
    - バッファリングポリシとタイムアウトの導入
  - 雑多なバグフィックス
  - コンフィギュレーション機能の充実
    - rtc.conf新オプションの導入 
    - より多くの項目を設定可能に
  - ManagerのCORBAサービス化(試験的) 
    - マスタ、スレーブマネージャ方式 
    - マスタマネージャのINS(Interoperable naming service)対応
    - コンポーネントのリモート管理機能の導入


