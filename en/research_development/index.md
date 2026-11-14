---

layout: page
title: "research_development"

---
<!-- Title: Research and Development -->
#contents

<!-- ** 開発の経緯 -->
## History of development

<!-- RTミドルウエアは、(独)新エネルギー・産業技術総合開発機構(NEDO)の21世紀ロボットチャレンジプログラム(2002～2004年度)のプロジェクトにおいて、そのコンセプトが提唱され、(独)産業技術総合研究所(産総研)、松下電工(現パナソニック電工株式会社), (社)日本ロボット工業会により研究・開発・標準化が行われました。 -->
The concept of RT-Middleware was proposed at the 21st-century Robot challenge program (2002-2004 fiscal year) bu New Energy and Industrial Technology Development Organization (NEDO). National Institute of Advanced Industrial Science and Technology (AIST), Matsushita Electric Works (now Life Solutions Company in Panasonic Cooperation), and Japan Robot Association (JARA) conducted the research, the development, and the standardization.

<!-- プロジェクトの成果として、RTミドルウエアの参照実装: OpenRTM-aist-0.2およびそのインターフェース仕様が公開されました。その後、国際標準化団体OMG (Object Management Group: https://www.omg.org )においてRTCインターフェース仕様の標準化が進められ、2008年4月にOMG公式標準仕様となりました。この標準に準拠したRTミドルウエア実装の一つが2010年1月に公開されたOpenRTM-aist-1.0です。 -->
As a result of the project, a reference implementation of RT-Middleware: OpenRTM-aist-0.2 and its interface specification were released. After that, standardization of the RTC interface specification was being made in an international standards organization: OMG (Object Management Group: http://www.omg.org), and became OMG official standard specification in April 2008.
One of RT-Middleware implementations conforming to the standard is OpenRTM-aist-1.0 released in January 2010.

<!-- 図に現在の研究/開発/標準化体制を示します。 -->
The figure shows the current research/development/standardization system.

<div align="center"><a href="rtm_randd_en.png"><img src="rtm_randd_en.png" width="30%;"></a></div>
<!-- CENTER: ''OpenRTM-aistの研究/開発/標準化体制'' -->
<div align="center"><strong>OpenRTM-aist research/development/standardization system</strong></div>

<!-- RTミドルウエアに関する研究開発は、2002年のRTミドルウエアプロジェクトに始まり、様々なプロジェクトで周辺技術の充実を図りながら、2007年からのNEDO知能化プロジェクトへと継続的に行われてきました(下図)。 -->
Research and development for RT-Middleware started as the RT-Middleware project in 2002 and then it was continued as various projects (the following figure) including NEDO's daily life support robot realizing project.

<div align="center"><a href="rtm_projects_en.png"><img src="rtm_projects_en.png" width="30%;"></a></div>
<!-- CENTER: ''OpenRTM-aistに関連した様々なプロジェクト'' -->
<div align="center"><strong>Various projects related to OpenRTM-aist </strong></div>

<!-- 以下ではこれまでの主なプロジェクトの概要を説明します。 -->
The following shows the overview of our major projects so far.

<!-- ** RTミドルウエア関連プロジェクト -->
## RT Middleware related project

<!-- *** RTミドルウエアプロジェクト -->
### RT middleware project

<!-- 独立行政法人新エネルギー・産業技術統合開発機構(NEDO)21世紀ロボットチャレンジプログラム(2002～2004年度)において「ロボット機能発現のために必要な要素技術開発」プロジェクト(通称:RTミドルウエアプロジェクト)が行われました。このプロジェクトでは、ロボット用分散ミドルウェア(RTミドルウエア)の研究開発が行われました。その成果として、ミドルウエアのインターフェース仕様が策定され、その仕様に基づいた実装OpenRTM-aist-0.2.0がリリースされました。 -->
"Development for required underlying technology for Robot function discovery" project (common name: RT middleware project) is conducted in the 21st Century Robot Challenge Program by  New Energy and Industrial Technology Development Organization (NEDO). In this project, the research and the development of Distributed Middleware for robots (RT middleware) were conducted. As a result, a middleware interface specification was developed, and an implementation based on the specification OpenRTM-aist-0.2.0 was released.

<!-- *** 分散コンポーネント型ロボットシミュレーター -->
### Distributed component type robot simulator

<!-- 科学振興調整費により 2005～2007年度 にかけて行われたこのプロジェクトは、ロボットソフトウェアの蓄積に適した分散コンポーネントフレームワークと、この上に構築されたロボットワールドシミュレーターを開発することにより、基盤ソフトウェアの再利用を促進し、次世代ロボットの開発を効率化することを目的としています。 -->
The purpose of the project, which was carried out from 2005 to 2007 fiscal year by using the Special Coordination Funds for Promoting Science and Technology, was developing a more effective way to develop next-generation robots by developing a distributed component framework which enables to increase software property for robot and a robot simulator made on the framework. 

<div align="center"><a href="openhrp_openrtm_en.png"><img src="openhrp_openrtm_en.png" width="60%;"></a></div>
<!-- CENTER: ''分散コンポーネント型ロボットシミュレーター'' -->
<div align="center"><strong>Distributed Component based Robot Simulator</strong></div>

<!-- このプロジェクトにより、これまで産総研において別々に開発されていた、ロボット用動力学シミュレータであるOpenHRP3と、OpenRTM-aistが統合されることになりました。 -->
As a result of the project, we integrated OpenRTM-aist and OpenHRP3 which is a robot dynamics simulator. Those were developed separately at AIST.

<!-- シミュレーター内の対象システムおよび、外部のコントローラーモジュール等を、RTコンポーネントとして開発し、かつ、コントローラーコンポーネントをシミュレーター/実機ともに再コンパイルすることなしに再利用できるよう、RTコンポーネントのロジック駆動主体である実行コンテキストが拡張されました。 -->
We developed a target system in the simulator, external controller module, etc as RT components. And we enhanced Execution Context function which is the main logic driving entity of RT component to be usable without the re-compilation of the controller components both on the real system and the simulator. 

<!-- *** 次世代ロボット知能化技術開発プロジェクト -->
### Next-generation Robot Intelligent RT Software Project

<!-- 経済産業省およびNEDOによる「次世代ロボット知能化技術開発プロジェクト」(2007～2011年度)は、5年間で総額70億(予想)の大規模プロジェクトです。次世代ロボットシステムのための要素技術を、RTコンポーネントとして作成・蓄積し、再利用の方法やインターフェースの共通化に関する議論を通して、次世代ロボットの設計・実装するための方法論を確立するとともに、実際に使える多くのRTコンポーネント群を蓄積することを目的としています。 -->
"Next-Generation Robot Intelligent RT Software Project" (2007 - 2011 fiscal year) by the Ministry of Economy, Trade and Industry and NEDO is a large-scale project that cost a totally of 7 billion yen (forecast) over 5 years. The purpose of the project was making methodology to design/implementation of the next-generation robot and accumulating RT components which can be used in an actual robot system. The components would be developed through the discussion about the re-use method, interface unifying. 

<!-- また、ロボットシステム開発の様々なフェーズで利用できる各種ツール群、ミドルウエア、ライブラリを含むRTシステム開発のためのプラットフォーム(OpenRT プラットフォーム(OpenRTP)と呼ぶ)をOpenRTM-aistの上に構築しました。開発ツール群は、Eclipseのプラグインとして実装され、一連の作業を同一の開発環境で行うことのできるツールチェーンとなっています。 -->
Also, a platform called "OpenRTP" was constructed on OpenRTM-aist. The platform is including various tools which can be used in the various development phase for a robot system, a middleware, libraries. The tools were implemented as Eclipse plug-in and it is a toolchain that can allow the user to do a series of work in a single development environment.

<div align="center"><a href="openrtp_en.png"><img src="openrtp_en.png" width="50%;"></a></div>
<!-- CENTER: ''OpenRT プラットフォーム (OpenRTP)'' -->
<div align="center"><strong>OpenRT platform (OpenRTP)</strong></div>

<!-- ツール間のデータは、RTコンポーネントを基盤としたモジュール仕様記述方式やシステム仕様記述方式 (UMLモデルとXMLスキーマから成る。) に基づいたフォーマットで記述され、ツール間の連携をより確かなものにするとともに、将来的には標準化も目指しています。プロジェクトの最終成果として、作成した多くのRTコンポーネント群やツール群をソースコード公開の上オープン化、あるいは事業化についても検討されています。 -->
Data between the tools are written with the format which is defined based on the module and system specification description method (defined by UML model and XML schema). This provides better co-working between tools. We also considering to standardize it in the future. Also, we are considering to make the big collection of RT components and the tools open-source and do business with them.   

<!-- *** オープンイノベーション促進プロジェクト -->
### Open Innovation Promotion Project

<!-- NEDOにより2008年から3年間実施された「基盤ロボット技術活用型オープンイノベーション促進プロジェクト」です。このプロジェクトでは、既存の要素部品を容易に RTコンポーネント化するため、安価で小型な基盤通信モジュールを開発することを目指しています。さらに、この基盤通信モジュールを利用して、実際に家屋の様々な部分に、センサーやアクチュエーターを配置し、多様なデバイスが連携して安心・安全・快適な居住空間を作り出す知能化住宅を実証システムとして構築しました。 -->
Fundamental Robot Technology-based Open Innovation Promotion Project were funded by NEDO for 3 years from 2008. In the project, to make existing elementally function parts to RT components, the development of cheap and compact base communication module was targeted. Also using the base communication module, an intelligent house in which various sensors and actuators are installed on various parts of the house and the devices are co-worked were built as a POC system.

<!-- ** その他 -->
## Other

<!-- プロジェクト以外においても、OpenRTM-aistの研究/開発/普及のための活動を行っています。 -->
We are also doing OpenRTM-aist research/development/promotion activity other than the projects. 

<!-- *** 講習会 -->
### Training session

<!-- 不定期ですが、年に数回のペースで実習形式の講習会を様々な場所で行っています。特に、機械学会ロボティクス・メカトロニクス講演会においては、チュートリアルとして毎年講習会を実施しています。 -->
In The Robotics and Mechatronics Conference (by the Japan Society of Mechanical Engineers) we are holding a lecture yearly base as a tutorial session. Also, several workshop style lectures are being held in various place in indeterminate matter.  

<!-- *** RTMコンテスト -->
### RTM Contest
<!-- ロボットビジネス推進協議会の主催、SICEシステムインテグレーション部門講演会の併設行事として、RTミドルウエアやRTコンポーネントの作品を募集しコンペティションを行うRTミドルウエアコンテストを行っています。 -->
The Robot Business Promotion Council is holding RT-Middleware contest as an event in SICE system integration division conference. In the contest, competitions of RT-Middleware based products are being performed.  

