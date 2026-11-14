---
layout: page
title: "rtc（ec）の状態を取得する"
---

<!-- Title: RTC（EC）の状態を取得する -->
エラーを取得する方法として2つの方法があります。
rtctree （rtshell のもととなっているライブラリ）ですと簡単に実現できますが、
まずは原理的なところから説明させていただきます。

1) ECに対してポーリングをする
あるRTCにアタッチされている実行コンテキスト（EC）に対して get_component_state() で
現在の状態を問い合わせる。
この方法はポーリングですので多用するとシステムの速度低下を招きます。

疑似コードで説明いたします。

```
rtc = <何らかの方法でRTCのオブジェクトリファレンスを取得>
ec_list = rtc.get_owned_contexts();
<!-- ec_list には RTCが持つ自身のECが入る。通常[0]にデフォルトコンテキストが -->
<!-- 入っており、OpenRTM-aistでは[1]以降にECが入ることはない。 -->
switch (ec_list[0].get_component_state(rtc)) {
  case CREATED_STATE:
    printf("Created state.");
    break;
  case INACTIVE_STATE:
    printf("Inactive state.");
    break;
  case ACTIVE_STATE:
    printf("Active state.");
    break;
  case ERROR_STATE:
    printf("Error state.");
   break;
  default:
     printf("Unknown state");
     break;
}
```


まずRTCからECを取得して、そのECに対してRTCを引数にして状態を取得しています。
このような呼び出し方をしているのは、以下の様な考え方からです。

RTCのステータスとして Inactive-Active-Error とされているのは、実際にはRTC の状態
ではなく、ある実行コンテキスト(EC)があるRTCと結びついたときの状態です。
（すなわち、状態はEC側にある、という考え方です。）
http://www.omg.org/spec/RTC/ のFigure5.6 がそれに当たります。

通常は自身のECしかないため、ECの状態とRTCの状態を同一視しても問題ないのですが、
実際には一つのRTCは複数のECにアタッチされる可能性があることをご理解ください。

2) ComponentObserver を利用する
もう一つはComponentObserver （1.1.0以降で導入） を利用する方法です。
ComponentObserverは以下の様なインターフェースを持っており、問い合わせをしたい側で
サーバントを実装し、このオブジェクトをRTCにアタッチすることで状態が変わったとき
などにコールバックさせます。

[ext/sdo/observer/ComponentObserver.idl](http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_0/OpenRTM-aist/src/ext/sdo/observer/ComponentObserver.idl)

@interface ComponentObserver の項をご覧ください。


```
obs_svt = new ComponentOberver_impl(); // サーバント
OpenRTM::ComponentObserver obs_ref = obs_svt._this(); // オブジェクト参照
SDO::ServiceProfile profile;
profile.id = UUID();
profile.interface_type = CORBA_Util::toRepositoryId<OpenRTM::ComponentObserver>(); // rtm/Typename.h
CORBA_SeqUtil.push_back(profile.properties, NVUtil::newNV("observed_status", "RTC_STATUS"));
CORBA_SeqUtil.push_back(profile.properties, NVUtil::newNV("heartbeat.enable", "YES"));
CORBA_SeqUtil.push_back(profile.properties, NVUtil::newNV("heartbeat.interval", "1.0"));
profile.service = obs_ref;

rtc = <何らかの方法でRTCのオブジェクトリファレンスを取得>
SDO::Configuration conf = rtc.get_configuration(); // SDO::get_configuration()
conf.add_service_profile(profile);

```

状態がACTIVEに変わったら、上記 ovs_svt の
ComponentOberver_impl::update_status("RTC_STATUS", "ACTIVE:0");
状態がINACTIVEに変わったら、
ComponentOberver_impl::update_status("RTC_STATUS", "INACTIVE:0");
状態がERRORに変わったら、
ComponentOberver_impl::update_status("RTC_STATUS", "ERROR:0");
が呼び出される。

<!-- > もしないのでしたらどのタイミングでリセットするかをどのように判断するのか -->
<!-- > 教えて頂けないでしょうか。 -->
<!-- > -->
<!-- > rtshellなどの方法で適切なタイミングでリセットを掛けるタイミングがわから -->
<!-- > ず、OpenRTMでは一般的な方法がないのか気になっております。 -->

ちなみに、rtshellのもととなっているrtctreeでは、たとえば RTCTree のコンストラクタに
dynamic = True をセットするとツリーオブジェクトがRTCの状態を取得する際に
ComponentObserverを利用して状態を取得するようになります。

- [tree.py](https://github.com/gbiggs/rtctree/blob/master/rtctree/tree.py)

また TreeNode::add_callback() を利用すると、イベントをフックできるようです。

- [node.py](https://github.com/gbiggs/rtctree/blob/master/rtctree/node.py)

このファイルの一番下にイベント名が定義されています。

- [component.py](https://github.com/gbiggs/rtctree/blob/master/rtctree/component.py)


