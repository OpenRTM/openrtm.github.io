---
layout: page
title: "ライセンス"
---

<!-- Title: ライセンス -->

OpenRTM-aistは、各言語版(C++、Java、Python)のミドルウエアライブラリと、RTCBuilder、RTSystemEditorなどツールから構成されており、それぞれ

- OpenRTM-aist (C++、Java、Python版)は **LGPLと個別契約のデュアルライセンス**
- RTSystemEditor、RTCBuilderは **EPLと個別契約のデュアルライセンス**

のもとでオープンソース形式で配布しています。

LGPL(GNU Lesser General Public License)はフリーソフトウェア財団(Free Software Foundation、以下FSFと略称)が提唱しているコピーレフト型のフリーソフトウェアライセンスです。

EPL(Eclipse Public License)はFSFによって認められている「フリーソフトウェアライセンス」の1つであり、CPL(一部はLGPL)等と似たライセンス形態であり、より商業利用を促進するものとなっています。

これらのライセンスは、(i) 別モジュールとして頒布されるソフトウエアや、(ii) 許諾プログラムの派生物でないもの　には及びません。またEPLライセンスは、特許に関する条項が含まれており、コントリビューターが持つ特許が当該ソフトウエアの使用に影響しない(使用者には使用料無料の特許ライセンスが付与される)形態となっています。

なお、LGPLライセンスの詳細については、
- http://www.gnu.org/copyleft/lesser.html
を、EPLライセンスの詳細については、
- http://opensource.org/licenses/eclipse-1.0.php
- http://sourceforge.jp/projects/opensource/wiki/licenses/Eclipse_Public_License (日本語訳)
を参照してください。

以下、OpenRTM-aistを用いた生成物の例に関連するライセンスと制約条件を説明します。

## RTコンポーネント開発・配布

OpenRTM-aisのライセンスは、個々のRTコンポーネントには及びません。したがって、**RTコンポーネントの作成者は、自由なライセンスで配布・販売することができます**。

RTコンポーネントは、OpenRTM-aist の libRTC.so (またはRTC.DLL) と動的リンクされており、また、RTコンポーネント自体も共有オブジェクト(またはダイナミックリンクライブラリ)として配布可能です。したがって、RTコンポーネント自体はライセンスが定める派生物とはみなされず、LGPLは及びません。

<div align="center"><a href="license_for_rtcs_ja.png"><img src="./license_for_rtcs_ja.png" style="width:50%;"></a></div>
<div align="center"><strong>RTコンポーネントのライセンス</strong></div>

RTコンポーネントを作成して配布する場合、任意のライセンスの元でRTコンポーネントを配布または販売することができ、ソースコードをオープンにするかクローズにするかを自由に選ぶことができます。

## LGPLに基づくOpenRTM-aist の改編と再配布

産総研が公開するOpenRTM-aistをLGPLに基づき利用する場合、産総研は利用者に対して、OpenRTM-aistを実行、改編、再配布、無料使用するライセンスを付与します。
ただし、LGPLでは再配布する場合に、再配布するプログラムについて、LGPLと矛盾しないことを要求しており、その中には改編されたソースコードを第三者が入手可能であることも含まれています。
したがって、LGPL のもとに OpenRTM-aist を改編して再配布したり販売する場合には、ソースコードを開示することが要求されます。

組込みシステムなどにおいては、ソースコードを改編せずにターゲットに適用することが困難で、改変したソースを開示することに抵抗がある場合が数多くあり、これはロボットを事業化したい会社等にとっては不都合であると言えます。
こうした場合を考慮して、OpenRTM-aist は次に説明する、個別契約に基づくライセンス付与の形態もとれるよう、デュアルライセンス形式となっています。


## 個別契約に基づくOpenRTM-aist の改編と再配布

上記の場合のように、ロボットシステムを商業化する際に、ソースコードを改編しつつ、技術の流出を防ぐためにソースコードをクローズにしたい場合、LGPLやEPLではなく、個別契約のライセンスを用いることができます。

OpenRTM-aistを改編、再配布する場合、産総研の知的財産部門と個別に協議のうえ、個別契約として産総研から利用者に対して非LGPL・非EPLのライセンスを付与することができます。
その場合のソースコードの利用料(実施料)やライセンスの範囲等の条件については、利用形態、ソースコードの改編の度合いや両者の知的財産の割合等に応じて、詳細を決定します。ただし、産総研は産業振興を目的とする非営利法人であり、その実施料は高価なものにはならないはずです。

<div align="center"><a href="./license_for_rtms_ja.png"><img src="./license_for_rtms_ja.png" style="width:50%;"></a></div>
<div align="center"><strong>RTミドルウエアのライセンス</strong></div>

RtcLink、RtcTemplate(RTSystemEditor、RTCBuilderの以前のバージョン)およびOpenRTM-aist(Java版)については、ソースコードの開示および実施(製品への利用)について個別契約によるライセンス提供の実績があります。


