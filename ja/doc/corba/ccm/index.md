---
layout: page
title: ccm
---

<!-- Title: CCM -->
#contents
## CCM (CORBA Component Model)

CCM は CORBA のサーバーサイドのコンポーネントモデルを提供するとともに、CORBA 環境上に EJB のようなコンポーネント環境を構築するためのフレームワークを提供する。

### コンポーネント 
コンポーネントの定義には様々あり、一般的に「再利用可能なソフトウェアの単位」であると言われている。
M.Collins-Cope らにある定義では、以下の４つの要件を満たすものをコンポーネントと呼び、この定義が広く用いられているようである。

<table class="table-alt">
  <tr>
    <td>自己完備性／自己記述性</td>
    <td>独立した機能単体として存在し、 宣言的にインターフェースが定義されている。また、動作や操作に 標準的な方法が定められており、そのためのメカニズムが明確に定義されている。</td>
  </tr>
  <tr>
    <td>動的な機能追加、変更が可能</td>
    <td>コンポーネントの外部からプロパティやイベントなどの設定、変更ができる。また、そのための標準的な方法が与えられている。</td>
  </tr>
  <tr>
    <td>インターフェースの透明性</td>
    <td>インターフェース定義に基づいて、バイナリレベルでの連携方法が与えられている。</td>
  </tr>
  <tr>
    <td>他のコンポーネントとの疎結合の支援</td>
    <td>他のコンポーネント との直接的な通信経路を持たず、コンテナやアセンブリ環境などのフレームワークを介して接続される。</td>
  </tr>
</table>

『 CORBA components が開く新しい分散環境 』 鈴木 純一／著, ドクター・ドブズ・ジャーナル日本語版 1999 年 4 月号、pp.150-158．


### コンポーネントモデル 
<table class="table-alt">
  <tr>
    <td>Facet</td>
    <td>コンポーネントのインターフェースを外部に公開することを示します。クライアントは、公開されたインターフェースをイントロスペクションによって獲得し、インターフェースがもつメソッドを呼び出すことができます。</td>
  </tr>
  <tr>
    <td>Receptacle</td>
    <td>他のコンポーネントがもつインターフェースを接続できることを示します。Receptacle のタイプとしては、一つのインターフェースを接続できる Simplex Receptacle と複数のインターフェースを同じ Receptacle に接続できる Multiplex Receptacle が存在します。</td>
  </tr>
  <tr>
    <td>Event Source</td>
    <td>特定のイベントを発行することを示します。イベント通知のタイプとしては、１対多の通知ができる Publisher と同時にひとつしか通知できない Emitter が存在します。</td>
  </tr>
  <tr>
    <td>Event Sink</td>
    <td>特定のイベントを受け取ることを示します。</td>
  </tr>
  <tr>
    <td>Attribute</td>
    <td>コンポーネントが持つ属性を示します。通常の CORBA オブジェクトの属性と同じ意味を持っています。</td>
  </tr>
</table>


### CIDL のための追加されたキーワード 
- component
- consumes
- emits
- eventtype
- finder
- getraises
- home
- import 
- multiple
- primarykey
- provides
- publishes
- setraises
- typeid
- typeprefix
- uses


### Deployment と Configuration のための XMLファイル
<table class="table-alt">
  <tr>
    <th>Descriptor</th>
    <th>拡張子</th>
  </tr>
  <tr>
    <td>Component Package Descriptor:</td>
    <td>.cpd</td>
  </tr>
  <tr>
    <td>Component Implementation Descriptor:</td>
    <td>.cid</td>
  </tr>
  <tr>
    <td>Implementation Artifact Descriptor:</td>
    <td>.iad</td>
  </tr>
  <tr>
    <td>Component Interface Descriptor (CORBA Component Descriptor):</td>
    <td>.ccd</td>
  </tr>
  <tr>
    <td>Component Domain Descriptor</td>
    <td>.cdd</td>
  </tr>
  <tr>
    <td>Deployment Plan Descriptor (Component Deployment Plan):</td>
    <td>.cdp</td>
  </tr>
  <tr>
    <td>Top Level Package Descriptor</td>
    <td>package.pcd</td>
  </tr>
  <tr>
    <td>ZIP file containing all of above + binaries</td>
    <td>.cpk</td>
  </tr>
</table>


### コンポーネントの宣言 
CCM のコンポーネントは、拡張 IDL に基づき component 宣言子を用いて以下の構文に従って宣言される。

```
 component <component_name> [ : <base_name> ]
     [ supports <interface_name> [, <interface_name>] * ]
 {
      <attribute declaration> *;
      <port declaration> *;
 };  
```

component に続く &lt;component_name&gt; は宣言するコンポーネントの名前を記述する。
オプション的な宣言として、コンポーネントは一つのコンポーネント( &lt;base_name&gt; )を継承することがでる。
また、support 宣言子により同時にいくつかの IDL で定義したインターフェース( &lt;interface_name&gt; )を持つこともでき、これらは supported interface と呼ばれる。
コンポーネントの本体には、コンポーネントの属性( &lt;attribute declaration&gt; ) や Ports ( &lt;port declaration&gt; )を宣言することができる。

この宣言は IDL2 と等価なインターフェース equivalent interface として以下のように宣言するのと等価である。

```
 interface <component_name>
     : Components::CCMObject, [<base_name>, <interface_name>, <interface_name>] * ]
 {
 };  
```


したがって、&lt;base_name&gt; はコンポーネント名であり、&lt;interface_name&gt; はインターフェース名として区別されるが、equivalent interface においてこれらはすべて interface となり、これらの継承に帰着される。

例えば、以下のように Hello インターフェースをもった HelloWorld コンポーネントを宣言することができます。 




### 参考文献 
1. [CORBA Component Model 入門 (第一回)](http://www.ogis-ri.co.jp/otc/hiroba/technical/CCM/step1/index.html)
1. [CORBA Component Model 入門 (第ニ回)](http://www.ogis-ri.co.jp/otc/hiroba/technical/CCM/step2/index.html)
1. [『 CORBA Component Model Tutorial 』 OMG Document ccm/02-04-01](http://www.omg.org/cgi-bin/doc?ccm/2002-04-01)
<!-- + [[Lightweight CORBA Component Model ptc/04-06-10>http://www.omg.org/docs/ptc/04-06-10.pdf]](リンク切れ) -->

