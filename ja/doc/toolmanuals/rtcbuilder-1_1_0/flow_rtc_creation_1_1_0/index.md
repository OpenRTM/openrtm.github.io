---
layout: page
title: 概要・rtc作成の流れ
---

init
<!-- Title: 概要・RTC作成の流れ -->
#contents
<!-- **概要 -->
### 動作環境
RTCBuilder の動作に必要な環境は以下のとおりです。
#clear
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
    <td>Eclipse 3.4.2以上 <br> http://www.eclipse.org/downloads/index.php <br> http://archive.eclipse.org/eclipse/downloads/index.php</td>
    <td>Eclipse 本体</td>
  </tr>
  <tr>
    <td>３</td>
    <td><a href="http://www.eclipse.org/modeling/emf/downloads/">Eclipse EMF 2.4以上(SDO,XSD含む)</a></td>
    <td>RTCBuilder が依存する Eclipse プラグイン <br> **※**ご使用になられる Eclipse のバージョンに合ったものをご使用ください。</td>
  </tr>
  <tr>
    <td>４</td>
    <td><a href="http://www.eclipse.org/gef/downloads/">Eclipse GEF 3.4以上(Draw2D含む)</a></td>
    <td>RTCBuilderが依存する Eclipse プラグイン <br> **※**ご使用になられる Eclipse のバージョンに合ったものをご使用ください。</td>
  </tr>
  <tr>
    <td>５</td>
    <td><a href="http://www.eclipse.org/projects/project_summary.php?projectid=eclipse.jdt">Eclipse Java development tools(JDT)</a></td>
    <td>**※**ご使用になられる Eclipse のバージョンに合ったものをご使用ください。</td>
  </tr>
</table>



また以下の開発を行う言語によっては以下の環境をインストールしておくと便利です。
<table class="table-alt">
  <tr>
    <th>№</th>
    <th>環境</th>
    <th>備考</th>
  </tr>
  <tr>
    <td>１</td>
    <td><a href="http://www.eclipse.org/cdt/downloads.php">Eclipse CDT</a></td>
    <td>C++ 用の開発環境</td>
  </tr>
  <tr>
    <td>２</td>
    <td><a href="http://marketplace.eclipse.org/node/114">Pydev for Eclipse</a></td>
    <td>python 用の開発環境</td>
  </tr>
</table>
<!-- |２|[[Pydev for Eclipse:http://sourceforge.net/project/showfiles.php?roup_id=85796]]|python 用の開発環境| -->

### RTC 作成の流れ (C++ 言語の場合)

C++ 言語で RTC を作成する場合、以下のツールが必要となります。
- [CMake](http://www.cmake.org/)
- [Doxygen](http://www.doxygen.jp/)
- [WiX](http://wix.sourceforge.net/)


1. RTCBuilder のコード生成により ソースコードの雛型と CMake の入力に必要なファイルを出力します。
1. RTCBuilder が生成したコードから CMake により、ユーザーの開発環境にあったビルドファイル(Visual Studio ソリューションファイルや GCC の Unix Makefiles など ) を生成します。
1. CMake によって生成されたビルドファイルとソースコードからコンポーネント(dll や so)を生成します。




### 制限
RTCBuilder は、OpenRTM-aist を対象に開発されたものです。その他の RTC プラットフォームに対する動作は想定しておりません。


