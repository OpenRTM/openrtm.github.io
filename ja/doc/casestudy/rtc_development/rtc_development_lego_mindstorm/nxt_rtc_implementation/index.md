---
layout: page
title: nxt rtc の実装
---

<!-- Title: NXT RTC の実装 -->
## NXT RTC の実装

では、上で実装した NXTBrick クラスを組み込むための RTC を作成します。
作成する RTC の仕様は以下のとおりです。

- InPort
  - モーター速度 (TimedFloatSeq)
- Outport
  - モーター位置 (TimedFloatSeq)
  - センサーデータ (TimedFloatSeq)



