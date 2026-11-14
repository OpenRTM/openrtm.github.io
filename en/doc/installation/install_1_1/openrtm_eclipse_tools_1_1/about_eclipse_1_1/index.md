---
layout: page
title: eclipse について
---
<br>
<a>No English version available.
</a>

<!-- Title: Eclipse について -->
<div align="left"><a href="eclipse_logo.png"><img src="eclipse_logo.png" width="15%;" align="left"></a></div>
#contents
[Eclipse](http://www.eclipse.org/) は Eclipse Foundation が開発するオープンソースのJava 言語およびその他の言語のための統合開発環境を構築するためのフレームワークです。
Eclipse の基本部分は plug-in を実行するためのプラットフォームで、 様々な開発環境は多くのplug-in の集合体として構築されます。
デフォルトで付属するJava の開発環境自体もplug-inとして実現され、 plug-in を追加することで様々な言語の開発環境として容易に拡張することができます。
#clear
Eclipse の特徴として、
- plug-in 機構により容易に拡張可能であり、plug-in 同士の連携も可能である。
- Rich Client Platform (RCP) と呼ばれる仕組みにより、 plug-in をスタンドアロン化することが容易にできる。
- Java で実装されているため、多くのプラットフォームで動作する。

等が挙げられます。
こうした Eclipse の特徴が、ロボット用統合開発環境を構築する上で有用であると判断し、Eclipse を RTミドルウエアのツールのためのプラットフォームとして選択しました。

RTCBuilder と RTSystemEditor を利用するには Eclipse をインストールする必要があります。
Eclipse のインストール方法に関しては、
- [http://eclipsewiki.net/eclipse/:http://eclipsewiki.net/eclipse/](http://eclipsewiki.net/eclipse/:http://eclipsewiki.net/eclipse/)

などが参考になります。

&aname(jre_install);
### Java 実行環境 (JRE) のインストール
Eclipse は Java アプリケーションですので、Oracle の Java 実行環境[(JRE: Java Runtime Environment)](https://www.java.com/ja/download/manual.jsp) をインストールする必要があります。
すでに、JDK（Java 開発環境、ただし、**1.6以上**）がインストールされている環境では JRE のインストールは必要ありません。（RTCBuilder で、Java のコードを生成させる場合には JRE でなく JDK が必要となります。）
- [JRE ダウンロード](https://www.java.com/ja/download/manual.jsp)
<!-- -[[JRE (Windows) オンラインインストーラ:http://javadl.sun.com/webapps/download/AutoDL?BundleId=11145]] -->
<!-- -[[JRE (Windows) オフラインインストーラー:http://javadl.sun.com/webapps/download/AutoDL?BundleId=11193]] -->

ダウンロード後はインストーラーの指示に従ってインストールしてください。


<br>
** JDK インストール**
⇒　[Java Development Kit 7](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)
<!-- ⇒　[[Java Development Kit 6:http://www.oracle.com/technetwork/java/javase/downloads/jdk-6u30-download-1377139.html]]~ -->

<br>


**参考：**
→　<span style="color:red;">**cool!**</span>; [UNIX系環境で簡易に Oracle の Java(JRE) を Eclipse に適用する方法 ]({{ site.baseurl }}/en/doc/faq/faq_rtp_tools#rtclinksunjava)



&aname(eclipse_install);
### Eclipse のインストール
Eclipse の[ダウンロードサイト](http://www.eclipse.org/downloads/index.php) からそれぞれのプラットフォームに対応した Eclipse のアーカイブを<span style="color:default;">ダウンロード</span>;、インストールしてください。
なお、RTCBuilder と RTSystemEditor の推奨環境は Eclipse3.4.2 です。

- [Eclipse 3.4.2 (Windows版)](http://archive.eclipse.org/eclipse/downloads/drops/R-3.4.2-200902111700/eclipse-SDK-3.4.2-win32.zip)
- [Eclipse 3.4.2 (Linux版 x86/GTK 2)](http://archive.eclipse.org/eclipse/downloads/drops/R-3.4.2-200902111700/download.php?dropFile=eclipse-SDK-3.4.2-linux-gtk.tar.gz)
- [Eclipse 3.4.2 (Linux版 x86/Motif Test版)](http://archive.eclipse.org/eclipse/downloads/drops/R-3.4.2-200902111700/download.php?dropFile=eclipse-SDK-3.4.2-linux-motif.tar.gz)

<!-- Eclipse は以下の Ring サーバーでもミラーされていますので、こちらからも[[ダウンロード>http://www.ring.gr.jp/pub/misc/eclipse/downloads/drops/]]できるでしょう。 -->
<!-- -[[Ring Server Project>http://www.ring.gr.jp/pub/misc/eclipse/downloads/drops/]] -->
<!-- -[[AIST Ring Server>http://ring.aist.go.jp/pub/misc/eclipse/downloads/drops/]] -->
<!-- -[[RIKEN Ring Server>http://ring.riken.go.jp/pub/misc/eclipse/downloads/drops/]] -->
- [参考 eclipse project archived downloads  ](http://archive.eclipse.org/eclipse/downloads/)(過去のバージョンのアーカイブ)

<br>

**参考**
→ [**FAQ:** Eclipse の起動方法 ]({{ site.baseurl }}/en/doc/faq/faq_rtp_tools#eclipse)

- Ubuntu8.04、Ubuntu9.10 で Linux 用 Eclipse3.4.2 が動作しない不具合が報告されています。
  - Ubuntu8.04では、**apt-get install xulrunner-1.9** として xulrunninerをアップデートしてください。
  - Ubuntu9.10では、以下の方法を利用するか、Eclipse3.3 もしくは 3.5 をご利用ください。
```
 $ su
 # vi /etc/apt/source.list
  1行追加 → deb http://jp.archive.ubuntu.com/ubuntu/ jaunty main restricted
 # apt-get update
 # apt-get install xulrunner-1.9
 # dpkg -l |grep xulrunner-1.9
 ii  xulrunner-1.9                        1.9.0.8+nobinonly-0ubuntu2                 XUL +  XPCOM application runner
 ii  xulrunner-1.9.1                      1.9.1.7+nobinonly-0ubuntu0.9.10.1          XUL + XPCOM application runner
 ii  xulrunner-1.9.1-gnome-support        1.9.1.7+nobinonly-0ubuntu0.9.10.1          Support for GNOME in xulrunner-1.9.1 applica
 一応、1.9.1と1.9 が共存
 # exit
 $ export GDK_NATIVE_WINDOWS=1
 $ ./eclipse
```
また、xulrunner-1.9.1.8 で動作するという報告もあります。1.9.1.8 にアップデートして、以下のようなシェルスクリプトを用意して起動するとよいでしょう。
```
 #/bin/sh
 export GDK_NATIVE_WINDOWS=1
 ./eclipse -vmargs -Dorg.eclipse.swt.browser.XULRunnerPath=/usr/lib/xulrunner-1.9.1.8/xulrunner
```



### Eclipse の日本語化
この時点では Eclipse は日本語化されていません。もし、 日本語化したい場合は以下の Eclipse の日本語化のページを参考にしてください。
<!-- -[[Eclipse日本語化:http://eclipsewiki.net/eclipse/?%C6%FC%CB%DC%B8%EC%B2%BD]] -->
- [Eclipse日本語化](https://mag.osdn.jp/08/10/20/0936240)

簡単な手順は, 以下の通りです.

1. Eclipse のバージョンに合ったファイルを下記サイトからダウンロードします。~
[Eclipse 日本語化言語パック (サードパーティ版)](http://www.igapyon.jp/blanco/nlpack/eclipse/)
<!-- --[[NLpack1-eclipse-SDK-3.1.1-win32.zip:http://www.ring.gr.jp/pub/misc/eclipse/downloads/drops/L-3.1.1_Language_Packs-200510051300/NLpack1-eclipse-SDK-3.1.1-win32.zip]] -->
<!-- --[[NLpack1-eclipse-SDK-3.2-win32.zip:http://www.ring.gr.jp/pub/misc/eclipse/downloads/drops/L-3.2_Language_Packs-200607121700/NLpack1-eclipse-SDK-3.2-win32.zip]] -->
1. 解凍してできた eclipse フォルダー内の features、 plugins をeclipse本体があるフォルダーにコピーします。
1. eclipse を再起動します。
<br>

参考：
　→ [**FAQ:** Eclipseの起動方法 ]({{ site.baseurl }}/en/doc/faq/faq_rtp_tools#eclipse)

### プラグインのインストール
RTCBuilder と RTSystemEditor  は下記の Eclipse プラグインを使用しています。
- [EMF (Eclipse Modeling Framework)](http://www.eclipse.org/modeling/emf/)
- [GEF (Graphical Editing Framework)](http://www.eclipse.org/gef/) 
- [XSD (XML Schema Infoset Model)](http://www.eclipse.org/modeling/mdt/?project=xsd#xsd) 
- [SDO (EMF Service Data Objects)](http://www.eclipse.org/modeling/emf/?project=sdo)
- [JDT (Eclipse Java development tools)](http://www.eclipse.org/projects/project_summary.php?projectid=eclipse.jdt)

以下の手順で、これらのプラグインをインストールしてください。

1. Eclipse のメニューから [ヘルプ] > [ソフトウエア更新] を選択します。
1. このような ソフトウェア更新およびアドイン ウィンドウ が表示されますので、「使用可能なソフトウェア」タブを選択します。
<div align="center"><a href="eclipse_update_ja.png"><img src="eclipse_update_ja.png" width="60%;"></a></div>
1. Genymede Update Site を展開してプラグインを選択します。
<div align="center"><a href="eclipse_plugin_GEF_JDT_ja.png"><img src="eclipse_plugin_GEF_JDT_ja.png" width="60%;"></a></div>
<div align="center"><a href="eclipse_plugin_EMF_SDO_ja.png"><img src="eclipse_plugin_EMF_SDO_ja.png" width="60%;"></a></div>
1. [インストール]をクリックします。
<div align="center"><a href="eclipse_plugin2_ja.png"><img src="eclipse_plugin2_ja.png" width="60%;"></a></div>
1. これで、これらのプラグインが自動的にダウンロードされて、インストールされます。

インストール後 Eclipse を一旦終了します。

<!-- +Software Updates の Available Software タブの Managed Sites... を開き、Export で Site 一覧を保存する -->
<!-- +Eclipse を終了し、<eclipse_home>\configuration\.settings フォルダーを開き以下の2ファイルを削除 -->
<!-- --org.eclipse.equinox.p2.artifact.repository.prefs -->
<!-- --org.eclipse.equinox.p2.metadata.repository.prefs -->
<!-- +Eclipse を起動し Site 一覧を Import -->
<!-- +Reflesh -->


