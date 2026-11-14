---
layout: page
title: "独自ロガーの実装方法"
---
<!-- Title: 独自ロガーの実装方法 -->
#contents

OpenRTM-aistは[Fluent Bitプラグイン]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/fluent_logger_use)のように、OpenRTM-aistデフォルトのロガー以外のロギング機能を拡張することができます。

このページでは独自ロガーの作成方法、使用手順を説明します。

今回作成したソースコードは以下から入手できます。

- [https://github.com/Nobu19800/testlopenrtmlogger](https://github.com/Nobu19800/testlopenrtmlogger)

## 独自ロガーの作成方法

### C++

#### 独自ロガー作成

C++の場合はビルドのためのCMakeLists.txtを用意してください。今回はTestLoggerという名前で作成します。

```
 cmake_minimum_required(VERSION 3.1)
 
 set(target TestLogger)
 project(${target} CXX)
 
 find_package(OpenRTM REQUIRED)
 
 
 
 add_definitions(${OPENRTM_CFLAGS})
 link_directories(${OPENRTM_LIBRARY_DIRS})
 
 add_library(${target} SHARED ${target}.cpp ${target}.h)
 target_link_libraries(${target} ${OPENRTM_LIBRARIES})
 target_include_directories(${target} SYSTEM PRIVATE ${OPENRTM_INCLUDE_DIRS})
 set_target_properties(${target} PROPERTIES PREFIX "")
```


ヘッダーファイル(TestLogger.h)、ソースファイル(TestLogger.cpp)を用意します。
**coil::LogStreamBuffer**クラスを継承したTestLoggerStreamクラス、**RTC::LogstreamBase**クラスを継承したTestLoggerクラスを実装します。
TestLoggerStreamはロギングの処理を実装するクラスで、TestLoggerはTestLoggerStreamを生成して外部から取得可能にするクラスです。

```
 #ifndef TESTLOGGER_H
 #define TESTLOGGER_H
 
 
 #include <rtm/LogstreamBase.h>
 
 
 class TestLoggerStream
```
  : public coil::LogStreamBuffer
```
 {
 public:
   TestLoggerStream();
   ~TestLoggerStream() override;
   bool init(const coil::Properties& prop);
    void write(int level, const std::string& name, const std::string& date, const std::string& mes) override;
 private:
   std::string header;
 };
 
 class TestLogger
```
  : public RTC::LogstreamBase
```
 {
 public:
   TestLogger();
   ~TestLogger() override;
   bool init(const coil::Properties& prop) override;
   coil::LogStreamBuffer* getStreamBuffer() override;
 private:
   TestLoggerStream m_logstream;
 };
 
 extern "C"
 {
   void DLL_EXPORT TestLoggerInit();
 }
 
 #endif
```



```
 #include "TestLogger.h"
 #include <iostream>
 
 
 TestLoggerStream::TestLoggerStream()
 {
 }
 
 TestLoggerStream::~TestLoggerStream()
 {
 }
 
 bool TestLoggerStream::init(const coil::Properties& prop)
 {
   header = prop["header"];
   return true;
 }
 
 void TestLoggerStream::write(int level, const std::string& name, const std::string& date, const std::string& mes)
 {
   std::cout << header << ":" << mes << std::endl;
 }
 
 
 TestLogger::TestLogger()
 {
 }
 
 TestLogger::~TestLogger()
 {
 }
 
 bool TestLogger::init(const coil::Properties& prop)
 {
   m_logstream.init(prop);
   return true;
 }
 
 coil::LogStreamBuffer* TestLogger::getStreamBuffer()
 {
   return &m_logstream;
 }
 
 
 extern "C"
 {
   void TestLoggerInit()
   {
```
     ::RTC::LogstreamFactory::
```
       instance().addFactory("testlogger",
```
                            ::coil::Creator< ::RTC::LogstreamBase,
```
                                             TestLogger>,
```
                            ::coil::Destructor< ::RTC::LogstreamBase,
```
                                                TestLogger>);
   }
 }
```


TestLoggerクラスの**init**関数で初期化、**getStreamBuffer**関数でLogStreamBufferオブジェクトを取得することができます。
TestLoggerクラスは特に理由が無ければ変更の必要はないです。

TestLoggerStreamクラスの**write**関数でログの出力を行います。
この例では、プロパティのheaderオプションに設定した文字列をログメッセージの先頭に追加して標準出力しています。

TestLoggerInit関数は動的ライブラリをロードする時に呼び出す関数です。〇〇.dllであれば**〇〇Init**というように、初期化関数は動的ライブラリの名前+Initにしてください。
TestLoggerInit関数内でLogstreamFactoryのaddFactory関数を呼ぶことでロガーを追加できます。

#### 動作確認

ビルドしてTestLogger.dll、TestLogger.soを生成後に動作確認を行います。

以下のrtc.confを作成してください。

```
 logger.enable: YES
 logger.log_level: VERBOSE
 
 logger.plugins: TestLogger.dll
 
 logger.logstream.testlogger.enable: ON
 logger.logstream.testlogger.header: example
```

まず**logger.plugins**オプションを設定してTestLoggerをロードするようにします。
ただロードするだけでは有効にはならないため、**logger.logstream.testlogger.enable**オプションを設定します。

※OpenRTM-aistの動作としては**logger.logstream.${モジュール名}**以下のオプションが設定されている場合にロガーが有効になるため、必ずしもenableオプションである必要はありません。

**logger.logstream.testlogger.header**オプションでログメッセージの先頭に追加する文字列を指定しています。

このrtc.confを指定してRTCを起動するとログが標準出力されることが確認できます。

### Python

Pythonファイル(TestLogger.py)を用意します。
**OpenRTM_aist.LogstreamBase**を継承したTestLoggerクラスを実装します。


```
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-
 
 
 import OpenRTM_aist
 
 
 class TestLogger(OpenRTM_aist.LogstreamBase):
 
    def __init__(self):
        OpenRTM_aist.LogstreamBase.__init__(self)
        self._header = ""
 
    def __del__(self):
        pass
 
    def init(self, prop):
        self._header = prop.getProperty("header")
        return True
 
    def log(self, msg, level, name):
        print(self._header+":"+msg)
        return True
 
    def setLogLevel(self, level):
        pass
 
    def shutdown(self):
        return True
 
 
 def TestLoggerInit(mgr):
    OpenRTM_aist.LogstreamFactory.instance().addFactory("testlogger",
                                                        TestLogger)
```

TestLoggerクラスの**init**関数で初期化、**log**関数でログの出力、**setLogLevel**関数でログレベルの設定、**shutdown**関数で終了処理を行います。
この例では、プロパティのheaderオプションに設定した文字列をログメッセージの先頭に追加して標準出力しています。


TestLoggerInit関数はPythonモジュールをロードする時に呼び出す関数です。〇〇.pyであれば**〇〇Init**というように、初期化関数はPythonファイルの名前+Initにしてください。
TestLoggerInit関数内でLogstreamFactoryのaddFactory関数を呼ぶことでロガーを追加できます。

#### 動作確認

以下のrtc.confを作成してください。

```
 logger.enable: YES
 logger.log_level: VERBOSE
 
 logger.plugins: TestLogger.py
 
 logger.logstream.testlogger.enable: ON
 logger.logstream.testlogger.header: example
```

まず**logger.plugins**オプションを設定してTestLoggerをロードするようにします。
ただロードするだけでは有効にはならないため、**logger.logstream.testlogger.enable**オプションを設定します。

**logger.logstream.testlogger.header**オプションでログメッセージの先頭に追加する文字列を指定しています。

このrtc.confを指定してRTCを起動するとログが標準出力されることが確認できます。



