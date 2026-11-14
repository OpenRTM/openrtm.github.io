---
layout: page
title: "独自インターフェース型の実装手順(c++)"
---
<!-- Title: 独自インターフェース型の実装手順(C++) -->
#contents

このページではC++で独自インターフェースを作成する手順を説明します。

以下のソースコードのサンプルでは重要でない部分は省略しているため、詳細なソースコードは以下から取得してください。

- [https://github.com/Nobu19800/openrtm_testinterface](https://github.com/Nobu19800/openrtm_testinterface)

## CMakeLists.txtの作成

ビルドのために以下のCMakeLists.txtを作成してください。
OpenRTM-aistのライブラリの検出の設定が必要です。
また、生成する動的ライブラリの名前を**${target}.dll**、**${target}.so**にする必要があります。
Linux環境では先頭にlibを付けるので(libTestIF.so)、以下の例では先頭のlibを削除しています。

```
 cmake_minimum_required(VERSION 3.1)
 
 set(target TestIF)
 project(${target} CXX)
 
 find_package(OpenRTM REQUIRED)
 
 
 
 add_definitions(${OPENRTM_CFLAGS})
 link_directories(${OPENRTM_LIBRARY_DIRS})
 
 add_library(${target} SHARED ${target}.cpp TestInPortConsumer.cpp TestInPortConsumer.h TestInPortProvider.cpp TestInPortProvider.h TestOutPortConsumer.cpp TestOutPortConsumer.h 
 TestOutPortProvider.cpp TestOutPortProvider.h)
 target_link_libraries(${target} ${OPENRTM_LIBRARIES})
 target_include_directories(${target} SYSTEM PRIVATE ${OPENRTM_INCLUDE_DIRS})
 set_target_properties(${target} PROPERTIES PREFIX "")
```

ただし、Push型通信を実装する場合はTestInPortConsumer、TestInPortProviderが必要で、Pull型通信を実装する場合はTestOutPortConsumer、TestOutPortConsumerが必要なため、どちらかしか実装しない場合は不要なファイルの作成は不要です。

### Push型通信
Push型通信実装のためにTestInPortConsumer(InPortConsumer)、TestInPortProvider(InPortProvider)を実装します。

#### InPortConsumerの実装
まず以下のようなヘッダーファイル(TestInPortConsumer.h)、ソースファイル(TestInPortConsumer.cpp)を用意します。


```
 #ifndef TESTINPORTCONSUMER_H
 #define TESTINPORTCONSUMER_H
 
 #include <rtm/InPortConsumer.h>
 
 class TestInPortConsumer

    : public RTC::InPortConsumer

 {
 public:
   TestInPortConsumer();
   ~TestInPortConsumer() override;
   void init(coil::Properties& prop) override;
   RTC::DataPortStatus put(RTC::ByteData& data) override;
   void publishInterfaceProfile(SDOPackage::NVList& properties) override;
   bool subscribeInterface(const SDOPackage::NVList& properties) override;
   void unsubscribeInterface(const SDOPackage::NVList& properties) override;
 };
 
 #endif
```


```
 #include "TestInPortConsumer.h"
 
 TestInPortConsumer::TestInPortConsumer()
 {
 }
 
 TestInPortConsumer::~TestInPortConsumer()
 {
 }
 
 void TestInPortConsumer::init(coil::Properties& prop)
 {
 }
 
 RTC::DataPortStatus TestInPortConsumer::put(RTC::ByteData& data)
 {

	return RTC::DataPortStatus::PORT_OK;

 }
 
 void TestInPortConsumer::publishInterfaceProfile(SDOPackage::NVList& properties)
 {
 }
 
 bool TestInPortConsumer::subscribeInterface(const SDOPackage::NVList& properties)
 {
 
	return true;

 }
 
 void TestInPortConsumer::unsubscribeInterface(const SDOPackage::NVList& properties)
 {
 }
```


今回はここにファイルの読み書きでデータを転送する独自インターフェースを実装します。

まずコネクタの初期化時に**init**関数が呼ばれます。
変数**prop**にはRTSystemEditor等で設定したコネクタの接続情報が格納されています。
以下の例ではpropからtestif.filenameのパラメータを取得してファイル名に設定しています。
init関数は複数回呼ばれる可能性があるので、その点は注意する必要があります。

```
 void TestInPortConsumer::init(coil::Properties& prop)
 {

	if (prop.propertyNames().size() == 0)
	{
		return;
	}

	m_filename = prop.getProperty("testif.filename", "test.dat");

 }
```


データの書き込み時には**put**関数が呼ばれます。
変数**data**にはバイト列にシリアライズしたデータが格納されています。

```
 RTC::DataPortStatus TestInPortConsumer::put(RTC::ByteData& data)
 {
 
   std::ofstream fout;
   fout.open(m_filename, std::ios::out | std::ios::binary | std::ios::trunc);
 
   if (fout.fail())
   {
     return RTC::DataPortStatus::PORT_ERROR;
   }
   else
   {
     m_dataid += 1;
     fout.write((const char*)&m_dataid, sizeof(unsigned long));
 
     const unsigned long size = data.getDataLength();
     fout.write((const char*)&size, sizeof(unsigned long));
 
     if (size > 0)
     {
       fout.write((const char*)data.getBuffer(), size);
     }
   }
 
 
   return RTC::DataPortStatus::PORT_OK;
 }
```

この例ではファイルにデータのID、データサイズ、バイト列データを書き込んでいます。
変数dataの**getDataLength**関数でデータサイズ、**getBuffer**関数でバイト列データを取得して、取得したデータを何らかの方法でInPortProviderへ送信します。
データの読み込みには他に**readData**関数を使う事ができます。

その他の関数は基本的に実装の必要はありませんが、InPortProvider側で追加の情報を設定する場合は**subscribeInterface**関数でその情報の取得をする必要があります。
**unsubscribeInterface**はコネクタ切断時に呼ばれるので、subscribeInterface関数での処理に関して何らかの終了処理が必要な場合は記述します。

#### InPortProviderの実装

まず以下のようなヘッダーファイル(TestInPortProvider.h)、ソースファイル(TestInPortProvider.cpp)を用意します。

```
 #ifndef TESTINPORTPROVIDER_H
 #define TESTINPORTPROVIDER_H
 
 #include <rtm/InPortProvider.h>
 #include <thread>
 
 class TestInPortProvider
 
    : public RTC::InPortProvider

 {
 public:
   TestInPortProvider();
   ~TestInPortProvider() override;
   void init(coil::Properties& prop) override;
   void setBuffer(RTC::BufferBase<RTC::ByteData>* buffer) override;
   void setListener(RTC::ConnectorInfo& info,
                             RTC::ConnectorListenersBase* listeners) override;
   void setConnector(RTC::InPortConnector* connector) override;
 private:
   RTC::InPortConnector* m_connector;
 };
 
 #endif
```

```
 #include "TestInPortProvider.h"
 #include <fstream>
 
 TestInPortProvider::TestInPortProvider() : m_connector(nullptr)
 {
   setInterfaceType("testif");
 }
 
 TestInPortProvider::~TestInPortProvider()
 {
 }
 
 void TestInPortProvider::init(coil::Properties& prop)
 {
 }
 
 void TestInPortProvider::setBuffer(RTC::BufferBase<RTC::ByteData>* buffer)
 {
 }
 
 void TestInPortProvider::setListener(RTC::ConnectorInfo& info,
   RTC::ConnectorListenersBase* listeners)
 {
 }
 
 void TestInPortProvider::setConnector(RTC::InPortConnector* connector)
 {
   m_connector = connector;
 }
```

ここに処理を追加していきます。
今回の例では、**init**関数で指定ファイルが変更されているかをポーリングするスレッドを作成しています。



```
 void TestInPortProvider::init(coil::Properties& prop)
 {
   if (prop.propertyNames().size() == 0)
   {
     return;
   }
 
   const std::string filename = prop.getProperty("testif.filename", "test.dat");
 
   if (!m_running)
   {
     m_thread = std::thread([this, filename] {
       this->m_running = true;
       unsigned long lastid = 0;
       while (this->m_running)
       {
         if (this->m_connector != nullptr)
         {
           std::ifstream fin(filename, std::ios::in | std::ios::binary);
           if (!fin.fail())
           {
             unsigned long id = 0;
             fin.read((char*)&id, sizeof(unsigned long));
 
             if (id != lastid)
             {
               lastid = id;
               unsigned long size = 0;
               fin.read((char*)&size, sizeof(unsigned long));
               if (size > 0)
               {
                 RTC::ByteData data;
                 data.setDataLength(size);
                 fin.read((char*)data.getBuffer(), size);
                 this->m_connector->write(data);
               }
             }
           }
         }
       }
       });
   }
 }
```

ファイルからデータを取得後に、m_connectorの**write**関数を呼び出してデータをInPortConnectorに渡しています。
InPortConsumerのデータをファイルに書き込んで、InPortProviderでファイルからデータを読み込むというデータ転送を実装できました。

### Pull型通信
Pull型通信実装のためにTestInPortConsumer(OutPortConsumer)、TestInPortProvider(OutPortProvider)を実装します。
ただし、Push型通信のみを実装する場合はここは飛ばしてください。

#### InPortConsumerの実装
まず以下のようなヘッダーファイル(TestOutPortConsumer.h)、ソースファイル(TestOutPortConsumer.cpp)を用意します。


```
 #ifndef TESTOUTPORTCONSUMER_H
 #define TESTOUTPORTCONSUMER_H
 
 #include <rtm/SystemLogger.h>
 #include <rtm/OutPortConsumer.h>
 
 class TestOutPortConsumer
  : public RTC::OutPortConsumer
 {
 public:
   TestOutPortConsumer();
   ~TestOutPortConsumer() override;
   void init(coil::Properties& prop) override;
   void setBuffer(RTC::CdrBufferBase* buffer) override;
   void setListener(RTC::ConnectorInfo& info,
     RTC::ConnectorListenersBase* listeners) override;
   RTC::DataPortStatus get(RTC::ByteData& data) override;
   bool subscribeInterface(const SDOPackage::NVList& properties) override;
   void unsubscribeInterface(const SDOPackage::NVList& properties) override;
 };
 
 #endif
```

```
 #include "TestOutPortConsumer.h"
 
 
 TestOutPortConsumer::TestOutPortConsumer()
 {
 }
 
 TestOutPortConsumer::~TestOutPortConsumer()
 {
 }
 
 void TestOutPortConsumer::init(coil::Properties& prop)
 {
 }
 
 void TestOutPortConsumer::setBuffer(RTC::CdrBufferBase* buffer)
 {
 }
 
 void TestOutPortConsumer::setListener(RTC::ConnectorInfo& info,
   RTC::ConnectorListenersBase* listeners)
 {
 }
 
 RTC::DataPortStatus TestOutPortConsumer::get(RTC::ByteData& data)
 {
   return RTC::DataPortStatus::PORT_OK;
 }
 
 bool TestOutPortConsumer::subscribeInterface(const SDOPackage::NVList& properties)
 {
   return true;
 }
 
 void TestOutPortConsumer::unsubscribeInterface(const SDOPackage::NVList& properties)
 {
 }
```

今回の例では**init**関数で読み書きするファイル名を指定します。

```
 void TestOutPortConsumer::init(coil::Properties& prop)
 {
   if (prop.propertyNames().size() == 0)
   {
     return;
   }
 
   m_filename_in = prop.getProperty("testif.filename_in", "test_in.dat");
   m_filename_out = prop.getProperty("testif.filename_out", "test_out.dat");
 }
```

ここに処理を追加していきます。
Pull型通信ではデータ読み込み時に**get**関数を呼びますが、以下の例ではファイルAに呼び出しのIDを書き込みます。
次にファイルBからデータサイズとバイト列データを読み込んで変数dataに格納しています。
データサイズを設定するには**setDataLength**関数を使用します。
データの格納には**getBuffer**関数で取得したポインタのアドレスに書き込むか、**writeData**関数を使用します。

```
 RTC::DataPortStatus TestOutPortConsumer::get(RTC::ByteData& data)
 {
   std::ofstream fout;
   fout.open(m_filename_out, std::ios::out | std::ios::binary | std::ios::trunc);
 
   if (fout.fail())
   {
     return RTC::DataPortStatus::PORT_ERROR;
   }
   else
   {
     m_dataid += 1;
     fout.write((const char*)&m_dataid, sizeof(unsigned long));
     fout.close();
 
     for (int i = 0; i < 100; i++)
     {
       std::ifstream fin(m_filename_in, std::ios::in | std::ios::binary);
       if (!fin.fail())
       {
         unsigned long id = 0;
         fin.read((char*)&id, sizeof(unsigned long));
 
         if (id == m_dataid)
         {
           unsigned long size = 0;
           fin.read((char*)&size, sizeof(unsigned long));
           if (size > 0)
           {
             data.setDataLength(size);
             fin.read((char*)data.getBuffer(), size);
             return RTC::DataPortStatus::PORT_OK;
           }
 
         }
       }
     }
   }
 
   return RTC::DataPortStatus::PORT_ERROR;
 }
```

#### OutPortProviderの実装
まず以下のようなヘッダーファイル(TestOutPortProvider.h)、ソースファイル(TestOutPortProvider.cpp)を用意します。

```
 #ifndef TESTOUTPORTPROVIDER_H
 #define TESTOUTPORTPROVIDER_H
 
 #include <rtm/OutPortProvider.h>
 
 class TestOutPortProvider
  : public RTC::OutPortProvider
 {
 public:
   TestOutPortProvider();
   ~TestOutPortProvider() override;
   void init(coil::Properties& prop) override;
   void setBuffer(RTC::CdrBufferBase* buffer) override;
   void setListener(RTC::ConnectorInfo& info,
     RTC::ConnectorListenersBase* listeners) override;
   void setConnector(RTC::OutPortConnector* connector) override;
 private:
   RTC::OutPortConnector* m_connector;
 };
 
 #endif
```

```
 #include "TestOutPortProvider.h"
 
 
 TestOutPortProvider::TestOutPortProvider() : m_connector(nullptr)
 {
   setInterfaceType("testif");
 }
 
 TestOutPortProvider::~TestOutPortProvider()
 {
 }
 
 void TestOutPortProvider::init(coil::Properties& prop)
 {
 }
 
 void TestOutPortProvider::setBuffer(RTC::CdrBufferBase* buffer)
 {
 }
 
 void TestOutPortProvider::setListener(RTC::ConnectorInfo& info,
   RTC::ConnectorListenersBase* listeners)
 {
 }
 
 void TestOutPortProvider::setConnector(RTC::OutPortConnector* connector)
 {
   m_connector = connector;
 }
```

ここに処理を追加していきます。
以下の例では**init**関数でファイルが変更されたかをポーリングして、変更時に別のファイルにデータを書き込むスレッドを起動しています。

```
 void TestOutPortProvider::init(coil::Properties& prop)
 {
   if (prop.propertyNames().size() == 0)
   {
     return;
   }
 
   const std::string filename_in = prop.getProperty("testif.filename_in", "test_in.dat");
   const std::string filename_out = prop.getProperty("testif.filename_out", "test_out.dat");
 
   if (!m_running)
   {
     m_thread = std::thread([this, filename_in, filename_out] {
       this->m_running = true;
       unsigned long lastid = 0;
       while (this->m_running)
       {
         if (this->m_connector != nullptr)
         {
           std::ifstream fin(filename_out, std::ios::in | std::ios::binary);
           if (!fin.fail())
           {
             unsigned long id = 0;
             fin.read((char*)&id, sizeof(unsigned long));
             fin.close();
 
             if (lastid != id)
             {
               std::ofstream fout;
               fout.open(filename_in, std::ios::out | std::ios::binary | std::ios::trunc);
               if (!fout.fail())
               {
                 fout.write((const char*)&id, sizeof(unsigned long));
 
                 RTC::ByteData data;
                 m_connector->read(data);
 
                 const unsigned long size = data.getDataLength();
                 fout.write((const char*)&size, sizeof(unsigned long));
 
                 if (size > 0)
                 {
                   fout.write((const char*)data.getBuffer(), size);
                 }
               }
 
               lastid = id;
             }
           }
         }
       }
     });
   }
 }
```

まずm_connectorの**read**関数を呼んでOutPortConnectorから転送するデータを取得します。
getDataLength関数でデータサイズを取得、getBuffer関数でバイト列データを取得してファイルに書き込んでいます。

これにより、OutPortConsumerでファイルAにデータのIDを書き込み後にOutPortProviderでファイルAからIDを読み込んで前回読み込んだデータのIDと一致しているかを判定します。
新しいデータだと判定したらファイルBにデータを書き込んで、OutPortConsumerでファイルBが新しいデータかを判定してOutPortConnectorにデータを渡します。

### 独自インターフェースの登録
ここまでに実装した独自インターフェースを使用可能にするためファクトリに登録します。
以下の内容の**TestIF.cpp**を作成してください。

```
 #include "TestInPortConsumer.h"
 #include "TestInPortProvider.h"
 #include "TestOutPortConsumer.h"
 #include "TestOutPortProvider.h"
 #include <rtm/Manager.h>
 
 extern "C"
 {
   DLL_EXPORT void TestIFInit(RTC::Manager* manager)
   {
      {
        RTC::InPortProviderFactory& factory(RTC::InPortProviderFactory::instance());
        factory.addFactory("testif",
                       ::coil::Creator< ::RTC::InPortProvider,
                                         TestInPortProvider>,
                       ::coil::Destructor< ::RTC::InPortProvider,
                                         TestInPortProvider>);
      }
 
      {
        RTC::InPortConsumerFactory& factory(RTC::InPortConsumerFactory::instance());
        factory.addFactory("testif",
                       ::coil::Creator< ::RTC::InPortConsumer,
                                         TestInPortConsumer>,
                       ::coil::Destructor< ::RTC::InPortConsumer,
                                         TestInPortConsumer>);
      }
 
      {
        RTC::OutPortProviderFactory& factory(RTC::OutPortProviderFactory::instance());
        factory.addFactory("testif",
                       ::coil::Creator< ::RTC::OutPortProvider,
                                         TestOutPortProvider>,
                       ::coil::Destructor< ::RTC::OutPortProvider,
                                         TestOutPortProvider>);
      }
 
      {
        RTC::OutPortConsumerFactory& factory(RTC::OutPortConsumerFactory::instance());
        factory.addFactory("testif",
                       ::coil::Creator< ::RTC::OutPortConsumer,
                                        TestOutPortConsumer>,
                       ::coil::Destructor< ::RTC::OutPortConsumer,
                                         TestOutPortConsumer>);
      }
   }
 }
```

**InPortProviderFactory**、**InPortConsumerFactory**、**OutPortProviderFactory**、**OutPortConsumerFactory**の**addFactory**関数で実装した独自インターフェースを登録しています。
この例の場合、**testif**という名前をポート接続時に指定することで使用できます。
Push型のみ、もしくはPull型通信のみの実装の場合は、必要なモジュールだけを登録してください。
TestIFInit関数は動的ライブラリをロードする時に呼び出す関数です。〇〇.dllであれば**〇〇Init**というように、初期化関数は動的ライブラリの名前+Initにしてください。
### 動作確認
ビルドして**TestIF.dll**、**TestIF.so**生成後に、以下のrtc.confを作成してください。
${TestIF_DIR}にはTestIF.dll、TestIF.soのフォルダのパスを指定してください。

```
 manager.modules.load_path: ${TestIF_DIR}
 manager.preload.modules: TestIF.dll
```

作成したrtc.confを指定してConsoleIn、ConsoleOutのサンプルコンポーネントを起動します。これでOpenRTM-aistがTestIF.dllをロードします。

```
 ConsoleIn -f rtc.conf
```

```
 ConsoleOut -f rtc.conf
```

RTSystemEditorでデータポートを接続しようとすると、以下のようにInterface Typeでtestifが選択可能になっています。

<br>

<div align="center"><a href="if4.png"><img src="if4.png" width="70%;"></a></div>

<br>

Interface Typeにtestifを選択して接続すると、実装したファイル読み書きによるデータ転送ができることが確認できます。

Pull型通信を動作確認する場合について、Pull型通信ではInPortのisNew関数が使えず新規のデータが存在するかは確認できません。
このため、ConsoleOutコンポーネントのisNew関数を実行している部分をコメントアウトして再ビルドする必要があります。

```
   //if (m_inIn.isNew())
```

### 接続時のオプションを設定
今回の例ではtestif.filename、testif.filename_in、testif.filename_outというオプションで読み書きするファイル名を指定できるようにしましたが、これらをデータポートのプロファイルからオプションの情報を取得するように設定を追加できます。ただし、リリース版のOpenRTM-aist 2.0では使えない場合があるので、OpenRTM-aistをソースコードからビルドしてください。

```
 static const char* const testifpush_option[] =
 {
   "filename.__value__", "test.dat",
   "filename.__widget__", "text",
   "filename.__constraint__", "none",
   ""
 };
 
 extern "C"
 {
   DLL_EXPORT void TestIFInit(RTC::Manager* manager)
   {
      {
        coil::Properties prop(testifpush_option);
        RTC::InPortProviderFactory& factory(RTC::InPortProviderFactory::instance());
        factory.addFactory("testif",
                      ::coil::Creator< ::RTC::InPortProvider,
                                        TestInPortProvider>,
                      ::coil::Destructor< ::RTC::InPortProvider,
                                        TestInPortProvider>,
                      prop);
      }
```



