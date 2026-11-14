---
layout: page
title: "getting the state of an rtc (ec)"
---

<!-- Title: RTC（EC）の状態を取得する -->
There are two ways to get errors.
This can be done easily with rtctree (the library on which rtshell is based),
but first, let me explain the underlying principle.

1) Poll the EC
For the execution context (EC) attached to an RTC, query the current state using get_component_state().
Since this method uses polling, using it frequently may slow down the system.

This is explained with pseudocode below.

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


First, the EC is obtained from the RTC, and then the state is obtained from that EC with the RTC passed as an argument.
This type of call is used based on the following idea.

What is referred to as the RTC status, Inactive-Active-Error, is actually not the state of the RTC itself,
but the state when a certain execution context (EC) is associated with an RTC.
(In other words, the state is considered to belong to the EC side.)
Figure 5.6 at http://www.omg.org/spec/RTC/ corresponds to this.

Normally, an RTC only has its own EC, so it is not a problem to regard the EC state and the RTC state as the same.
However, please understand that one RTC can actually be attached to multiple ECs.

2) Use ComponentObserver
Another method is to use ComponentObserver (introduced in 1.1.0 and later).
ComponentObserver has an interface like the following. The side that wants to make inquiries implements a servant,
and by attaching this object to the RTC, callbacks are made when the state changes, etc.

[ext/sdo/observer/ComponentObserver.idl](http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_0/OpenRTM-aist/src/ext/sdo/observer/ComponentObserver.idl)

See the @interface ComponentObserver section.


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

When the state changes to ACTIVE,
ComponentOberver_impl::update_status("RTC_STATUS", "ACTIVE:0");
of the above ovs_svt is called.
When the state changes to INACTIVE,
ComponentOberver_impl::update_status("RTC_STATUS", "INACTIVE:0");
is called.
When the state changes to ERROR,
ComponentOberver_impl::update_status("RTC_STATUS", "ERROR:0");
is called.

<!-- > もしないのでしたらどのタイミングでリセットするかをどのように判断するのか -->
<!-- > 教えて頂けないでしょうか。 -->
<!-- > -->
<!-- > rtshellなどの方法で適切なタイミングでリセットを掛けるタイミングがわから -->
<!-- > ず、OpenRTMでは一般的な方法がないのか気になっております。 -->

Incidentally, in rtctree, which is the basis of rtshell, for example, if dynamic = True is set in the RTCTree constructor,
the tree object will use ComponentObserver to obtain the RTC state when obtaining the state of an RTC.

- [tree.py](https://github.com/gbiggs/rtctree/blob/master/rtctree/tree.py)

Also, it seems that events can be hooked by using TreeNode::add_callback().

- [node.py](https://github.com/gbiggs/rtctree/blob/master/rtctree/node.py)

Event names are defined at the bottom of this file.

- [component.py](https://github.com/gbiggs/rtctree/blob/master/rtctree/component.py)

