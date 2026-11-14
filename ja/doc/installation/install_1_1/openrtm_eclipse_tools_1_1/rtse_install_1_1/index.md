---
layout: page
title: rtsystemeditor のインストール
---

<!-- Title: RTSystemEditor のインストール -->
#contents
## RTSystemEditor とは
RTSystemEditor は、OpenRTM-aist に含まれる開発ツールの１つであり、RTC をリアルタイムにグラフィカル操作する機能を持っています。また、Eclipse 統合開発環境のプラグインとして作成されており、Eclipse 上にて既存のプラグインとシームレスに操作を行うことができます。

#clear

### 機能概要 
RTSystemEditorは、RTC をリアルタイムにグラフィカル操作する機能を持っています。提供される機能の一覧は以下のとおりです。

<table class="table-alt">
  <tr>
    <th>№</th>
    <th>機能名称</th>
    <th>機能概要</th>
  </tr>
  <tr>
    <td>１</td>
    <td>コンポーネントコンフィグレーション表示/編集機能</td>
    <td>選択したコンポーネントのコンフィギュレーションプロファイル情報をコンフィグレーションビューに表示し編集する。</td>
  </tr>
  <tr>
    <td>２</td>
    <td>コンポーネント動作変更機能</td>
    <td>選択したコンポーネントの動作を変更する。</td>
  </tr>
  <tr>
    <td>３</td>
    <td>コンポーネント組み立て機能</td>
    <td>システムエディタ上でシステムの組み立てやリポジトリおよびファイルシステムのコンポーネント仕様の編集を行う。</td>
  </tr>
  <tr>
    <td>４</td>
    <td>システムセーブ/オープン機能</td>
    <td>システムエディタの内容をセーブ/オープンする。</td>
  </tr>
  <tr>
    <td>５</td>
    <td>システム復元機能</td>
    <td>保存したシステムエディタの内容をシステムに復元する。</td>
  </tr>
</table>

### 動作環境
RTSystemEditor の動作に必要な環境は以下のとおりです。

<table class="table-alt">
  <tr>
    <th>№</th>
    <th>環境</th>
    <th>備考</th>
  </tr>
  <tr>
    <td>１</td>
    <td><a href="http://java.sun.com/javase/ja/6/download.html">Java Development Kit 6</a></td>
    <td><span style="color:Red;">注意：Java1.5(5.0)では動作しません。</span>;</td>
  </tr>
  <tr>
    <td>２</td>
    <td>Eclipse 3.4.2以上 <br> <a href="http://www.eclipse.org/downloads/index.php](http://www.eclipse.org/downloads/index.php">http://www.eclipse.org/downloads/index.php](http://www.eclipse.org/downloads/index.php</a> <br> <a href="http://archive.eclipse.org/eclipse/downloads/index.php">http://archive.eclipse.org/eclipse/downloads/index.php</a></td>
    <td>Eclipse 本体</td>
  </tr>
  <tr>
    <td>３</td>
    <td>Eclipse EMF 2.2.4 <a href="http://www.eclipse.org/downloads/download.php?file=/modeling/emf/emf/downloads/drops/2.2.4/R200710030400/emf-sdo-runtime-2.2.4.zip">EMF＋SDO Runtime</a> および <a href="http://www.eclipse.org/downloads/download.php?file=/modeling/emf/emf/downloads/drops/2.2.4/R200710030400/xsd-runtime-2.2.4.zip">XSD Runtime</a></td>
    <th>RT System Editor が依存する Eclipse プラグイン</th>
  </tr>
  <tr>
    <td>４</td>
    <td><a href="http://www.eclipse.org/downloads/download.php?file=/tools/gef/downloads/drops/R-3.2.2-200702081315/GEF-runtime-3.2.2.zip">Eclipse GEF 3.2.2</a></td>
    <td>RT System Editor が依存する Eclipse プラグイン</td>
  </tr>
  <tr>
    <td>５</td>
    <td><a href="http://www.eclipse.org/projects/project_summary.php?projectid=eclipse.jdt">Eclipse Java development tools(JDT)</a></td>
    <td>※ご使用になられる Eclipse のバージョンに合ったものをご使用ください。</td>
  </tr>
</table>


## RTSystemEditor のインストール
RTSystemEditor は Eclipse プラグインであるため、 Eclipse 本体をインストールする必要があります。さらに、 Eclipse は Java アプリケーションなので、Eclipse 本体をインストールする前に Java 実行環境（あるいは JDK：Java 開発環境でもよい）をインストールする必要があります。
- Java 実行環境のインストールについては、[Eclipseについて の Java 実行環境 (JRE) のインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/openrtm_eclipse_tools_1_1/about_eclipse_1_1#jre_install) を参照願います。
- Eclipse のインストールについては、[Eclipse について の Eclipse のインストール]({{ site.baseurl }}/ja/doc/installation/install_1_1/openrtm_eclipse_tools_1_1/about_eclipse_1_1#eclipse_install) を参照願います。

<!-- *** Java実行環境(JRE)のインストール -->
<!-- Eclipse は Java アプリケーションなので、SunのJava実行環境[[(JRE: Java Runtime Environment):http://www.java.com/ja/download/manual.jsp]] をインストールする必要があります。すでに、JDK（Java 開発環境、ただし、''1.6以上''）がインストールされている環境では JRE のインストールは必要ありません。（RTCBuilder で、Java のコードを生成させる場合には JRE でなく JDK が必要となります。） -->
<!-- -[[JRE ダウンロード:http://www.java.com/ja/download/manual.jsp]] -->
<!-- -[[JRE (Windows) オンラインインストーラー:http://javadl.sun.com/webapps/download/AutoDL?BundleId=11145]] -->
<!-- -[[JRE (Windows) オフラインインストーラー:http://javadl.sun.com/webapps/download/AutoDL?BundleId=11193]] -->
<!--  -->
<!-- ダウンロード後はインストーラーの指示に従ってインストールしてください。 -->
<!--  -->
<!--  -->
<!-- &br; -->
<!-- '' JDK インストール：''~ -->
<!-- ⇒　[[Java Development Kit 6:http://java.sun.com/javase/ja/6/download.html]]~ -->
<!-- ⇒　以下に''旧バージョンのJava Development Kit 5(JDK1.5)''のインストール方法が記載してあります。 -->
<!-- -[[JDKインストール方法>node/661#instjavaunixjdk]] -->
<!--  -->
<!-- &br; -->
<!--  -->
<!-- ~ -->
<!-- ''参考：'' -->
<!-- →　&color(red){''cool!''}; [[UNIX系環境で簡易にSunのJava(JRE)をEclipseに適用する方法 >/ja/node/248#rtclinksunjava]] -->
<!--  -->
<!-- #br -->
<!--  -->
<!-- *** Eclipseのインストール -->
<!-- Eclipseの[[ダウンロードサイト>http://www.eclipse.org/downloads/index.php]] からそれぞれのプラットフォームに対応したEclipseのアーカイブを&color(default){ダウンロード};、インストールしてください。 -->
<!-- なお、RTSystemEditor の推奨環境は Eclipse3.4.2 です。 -->
<!--  -->
<!-- -[[Eclipse 3.4.2 (Windows版)>http://archive.eclipse.org/eclipse/downloads/drops/R-3.4.2-200902111700/eclipse-SDK-3.4.2-win32.zip]] -->
<!-- -[[Eclipse 3.4.2 (Linux版 x86/GTK 2)>http://archive.eclipse.org/eclipse/downloads/drops/R-3.4.2-200902111700/download.php?dropFile=eclipse-SDK-3.4.2-linux-gtk.tar.gz]] -->
<!-- -[[Eclipse 3.4.2 (Linux版 x86/Motif Test版)>http://archive.eclipse.org/eclipse/downloads/drops/R-3.4.2-200902111700/download.php?dropFile=eclipse-SDK-3.4.2-linux-motif.tar.gz]] -->
<!--  -->
<!-- Eclipseは以下のRingサーバでもミラーされていますので、こちらからも[[ダウンロード>http://www.ring.gr.jp/pub/misc/eclipse/downloads/drops/]]できるでしょう。 -->
<!--  -->
<!-- -[[Ring Server Project>http://www.ring.gr.jp/pub/misc/eclipse/downloads/drops/]] -->
<!-- -[[AIST Ring Server>http://ring.aist.go.jp/pub/misc/eclipse/downloads/drops/]] -->
<!-- -[[RIKEN Ring Server>http://ring.riken.go.jp/pub/misc/eclipse/downloads/drops/]] -->
<!-- -[[参考 eclipse project archived downloads  >http://archive.eclipse.org/eclipse/downloads/]](過去のバージョンのアーカイブ) -->
<!--  -->
<!-- #br -->
<!--  -->
<!-- ''新着情報！'';~ -->
<!-- ''[[こちら >/ja/node/75]]にUNIX用とWindows用 new!; のインストールパッケージを用意しました。'';RT System Editor とRTC Builder（後述）を含め、全て（ Eclipse3.4.2 ＋ 日本語化 + RT System Editor ＋ GEF ＋ EMF ＋ XSD  +RTC Builder ）が入ったUNIX用とWindows用のパッケージを用意しました。「とりいそぎ」動かしてみたい方はぜひご利用ください。 -->
<!--  -->
<!--  -->
<!-- 次の[[インストールの仕方 >#howtoinstall]]に従うだけで、とても簡単にインストールできます。 -->
<!--  -->
<!-- ****インストールの仕方 &aname(howtoinstall); -->
<!-- Eclipseのアーカイブ（圧縮された状態のパッケージファイル）は100MB以上あります. ダウンロードしたら、アーカイブをインストールしたいディレクトリに展開してください。 -->
<!-- Eclipseには特にインストーラは無く、アーカイブを展開するだけでそのまま使用できます。 -->
<!-- #br -->
<!--  -->
<!-- 参考： -->
<!--  -->
<!-- → [[''FAQ:'' Eclipseの起動方法 >/ja/node/158#eclipse]] -->
<!-- #br -->
<!--  -->
<!-- -Ubuntu8.04, Ubuntu9.10でLinux用Eclipse3.4.2が動作しない不具合が報告されています。 -->
<!-- --Ubuntu8.04では、''apt-get install xulrunner-1.9'' として xulrunninerをアップデートしてください。 -->
<!-- --Ubuntu9.10では、以下の方法を利用するか、Eclipse3.3もしくは3.5をご利用ください。 -->
<!-- $ su -->
<!-- # vi /etc/apt/source.list -->
<!-- 1行追加 → deb http://jp.archive.ubuntu.com/ubuntu/ jaunty main restricted -->
<!-- # apt-get update -->
<!-- # apt-get install xulrunner-1.9 -->
<!-- # dpkg -l |grep xulrunner-1.9 -->
<!-- ii  xulrunner-1.9                        1.9.0.8+nobinonly-0ubuntu2                 XUL +  XPCOM application runner -->
<!-- ii  xulrunner-1.9.1                      1.9.1.7+nobinonly-0ubuntu0.9.10.1          XUL + XPCOM application runner -->
<!-- ii  xulrunner-1.9.1-gnome-support        1.9.1.7+nobinonly-0ubuntu0.9.10.1          Support for GNOME in xulrunner-1.9.1 applica -->
<!-- 一応、1.9.1と1.9 が共存 -->
<!-- # exit -->
<!-- $ export GDK_NATIVE_WINDOWS=1 -->
<!-- $ ./eclipse -->
<!-- また、xulrunner-1.9.1.8 で動作するという報告もあります。1.9.1.8にアップデートして、以下のようなシェルスクリプトを用意して起動するとよいでしょう。 -->
<!-- #/bin/sh -->
<!-- export GDK_NATIVE_WINDOWS=1 -->
<!-- ./eclipse -vmargs -Dorg.eclipse.swt.browser.XULRunnerPath=/usr/lib/xulrunner-1.9.1.8/xulrunner -->
<!--  -->
<!--  -->
<!--  -->
<!-- ***Eclipseの日本語化 -->
<!-- この時点ではEclipseは日本語化されていません。もし、 日本語化したい場合は以下のEclipseの日本語化のページを参考にしてください。 -->
<!-- // -[[Eclipse日本語化:http://eclipsewiki.net/eclipse/?%C6%FC%CB%DC%B8%EC%B2%BD]] -->
<!-- -[[Eclipse日本語化>http://sourceforge.jp/magazine/08/10/20/0936240]] -->
<!-- 簡単な手順は, 以下の通りです. -->
<!--  -->
<!-- -Eclipseのバージョンに合ったファイルを下記サイトからダウンロードします。 -->
<!-- --[[Eclipse 日本語化言語パック (サードパーティ版)>http://www.igapyon.jp/blanco/nlpack/eclipse/]] -->
<!-- --[[NLpack1-eclipse-SDK-3.1.1-win32.zip:http://www.ring.gr.jp/pub/misc/eclipse/downloads/drops/L-3.1.1_Language_Packs-200510051300/NLpack1-eclipse-SDK-3.1.1-win32.zip]] -->
<!-- --[[NLpack1-eclipse-SDK-3.2-win32.zip:http://www.ring.gr.jp/pub/misc/eclipse/downloads/drops/L-3.2_Language_Packs-200607121700/NLpack1-eclipse-SDK-3.2-win32.zip]] -->
<!-- -解凍して出来た eclipse フォルダ内の features、 plugins をeclipse本体があるフォルダにコピーします。 -->
<!-- -eclipse を再起動します。 -->
<!-- #br -->
<!--  -->
<!-- 参考： -->
<!-- → [[''FAQ:'' Eclipseの起動方法 >/ja/node/158#eclipse]] -->
<!-- #br -->

### RTSystemEditor のインストールと起動
<!-- RTSystemEditor は下記の Eclipse プラグインを使用しています。 -->
<!-- -[[EMF (Eclipse Modeling Framework):http://www.eclipse.org/modeling/emf/]] -->
<!-- -[[GEF (Graphical Editing Framework):http://www.eclipse.org/gef/]]  -->
<!-- -[[XSD (XML Schema Infoset Model):http://www.eclipse.org/modeling/mdt/?project=xsd#xsd]]  -->
<!-- -[[SDO (EMF Service Data Objects):http://www.eclipse.org/modeling/emf/?project=sdo]] -->
<!-- -[[JDT (Eclipse Java development tools):http://www.eclipse.org/projects/project_summary.php?projectid=eclipse.jdt]] -->
<!--  -->
<!-- RTSystemEditor プラグインをインストールする前に、 これらのプラグインをインストールしてください。 -->
<!--  -->
<!-- まず、  Eclipse のメニューから''ヘルプ(H)→ソフトウエア更新...''を選択します。 -->
<!-- このような ソフトウェア更新およびアドイン ウィンドウ が表示されますので、''使用可能なソフトウェア(V)''タブを選択します。 -->
<!-- #br -->
<!--  -->
<!-- #ref(EclipsePluginInstall0.png,nolink,center) -->
<!-- #br -->
<!-- ''Genymede Update Site'' を展開して、プラグインを選択します。 -->
<!-- #br -->
<!--  -->
<!-- #ref(EclipsePluginInstall1.png,nolink,center) -->
<!-- #br -->
<!-- ''Callisto Discovery Site''をチェックして''終了(F)''を押します。 -->
<!-- #br -->
<!--  -->
<!-- #ref(EclipsePluginInstall2.png,nolink,center) -->
<!-- #br -->
<!-- ''Callisto Discovery Site''をクリックして''OK''を押します。 -->
<!-- #br -->
<!--  -->
<!-- #ref(EclipsePluginInstall3.png,nolink,center) -->
<!--  -->
<!-- -Graphical Editing Framework -->
<!-- -Eclipse Modling Framework Runtime -->
<!-- -XML Schema Infoset Model(XSD) Runtime -->
<!-- -EMF Service Data Objects(SDO) Runtime -->
<!--  -->
<!-- を選択して''次へ(N)''を押します。 -->
<!-- これで, これらのプラグインが自動的にダウンロードされて, インストールされます。 -->
<!-- インストール後Eclipseを一旦終了します。 -->
<!--  -->
<!-- +Software Updates の Available Software タブの Managed Sites... を開き、Export で Site 一覧を保存する -->
<!-- +Eclipse を終了し、<eclipse_home>\configuration\.settings フォルダを開き以下の2ファイルを削除 -->
<!-- --org.eclipse.equinox.p2.artifact.repository.prefs -->
<!-- --org.eclipse.equinox.p2.metadata.repository.prefs -->
<!-- +Eclipse を起動し Site 一覧を Import -->
<!-- +Reflesh -->


[バイナリ(日本語版 jar ファイル(RTSE+RTCB)) ]()（リンク切れです） をダウンロードして、  Eclipse の plugin ディレクトリー( Eclipse のアーカイブを展開すると通常 eclipse というディレクトリーが作成されますが、 その中の plugin というディレクトリー)にダウンロードした jar ファイルをそのままコピーします。

Eclipse を起動し、 メニューから [ウインドウ] > [パースペクティブを開く] > [その他] を選択すると、 次のようなパースペクティブ選択画面が表示されます。

<div align="center"><a href="fig4PerspectiveSelection_ja.png"><img src="fig4PerspectiveSelection_ja.png" width="40%;"></a></div>
<br>
パースペクティブ一覧にある RT System Editor を選択すると、 次のような画面が表示されて RTSystemEditor が起動されます。

<div align="center"><a href="fig5InitialOfRTSystemEditorStarts_ja.png"><img src="fig5InitialOfRTSystemEditorStarts_ja.png" width="60%;"></a></div>
<br>

もし、 パースペクティブの一覧に RT System Editor が表示されない場合は、EMF や GEF や XSD や JDT が正しくインストールできているか、 RT System Editorがplugin ディレクトリーに正しくコピーされているかを再度チェックしてください。
### Eclipse の再起動
RTSystemEditor の起動が確認できましたら、一旦、Eclipse を終了してください。再度、同じワークスペースを指定して Eclipse を起動すると、RTSystemEditor が起動された状態から始まります。

<br>
<br>
参考：
　→ [**FAQ:** Eclipseの起動方法 ]({{ site.baseurl }}/ja/doc/faq/faq_rtp_tools#toc9)
<br>
<br>



