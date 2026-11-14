---
layout: page
title: "コンフィギュレーション (応用編)"
---
<!-- Title: コンフィギュレーション (応用編) -->
#contents

コンフィギュレーション(基本編)では、コンフィギュレーションの基本的な使い方について説明しました。応用編では、もう少し踏み込んだ使い方について解説します。

## コールバックの利用
コンフィギュレーションパラメータのコールバックの利用について説明します。<br>
コンフィギュレーションには、以下のコールバックがあります。

- OnUpdateCallback
- OnUpdateParamCallback
- OnSetConfigurationSetCallback
- OnAddConfigurationAddCallback
- OnRemoveConfigurationSetCallback
- OnActivateSetCallback

以下のようにしてコールバックを設定します。

### OnUpdateCallback
```
 class MyOnUpdate
 	: public RTC::OnUpdateCallback
 {
 public:
 	MyOnUpdate(ConfigurationTest *obj)
 	{
 		myobj = obj;
	}
	virtual void operator()(const char* config_set)
	{
		RTC::ExecutionContextList_var ecs;
		ecs = myobj->get_owned_contexts();
		ecs[(CORBA::ULong)0]->set_rate(myobj->m_interval);
		std::cout << "OnUpdateCallback\t" << config_set << std::endl;
	}
 private:
 	ConfigurationTest *myobj;
 };
```

### OnUpdateParamCallback
```
 class MyOnUpdateParam
	: public RTC::OnUpdateParamCallback
 {
 public:
	MyOnUpdateParam(ConfigurationTest *obj)
	{
		myobj = obj;
	}
	virtual void operator()(const char* config_set, const char* config_param)
	{
		RTC::ExecutionContextList_var ecs;
		ecs = myobj->get_owned_contexts();
		ecs[(CORBA::ULong)0]->set_rate(myobj->m_interval);
		std::cout << "OnUpdateParamCallback\t" << config_set << "\t" << config_param <<  std::endl;
	}

 private:
	ConfigurationTest *myobj;
 };
```

### OnSetConfigurationSetCallback

```
 class MyOnSetConfigurationSet
	: public RTC::OnSetConfigurationSetCallback
 {
 public:
	MyOnSetConfigurationSet(ConfigurationTest *obj)
	{
		myobj = obj;
	}
	virtual void operator()(const coil::Properties& config_set)
	{
		RTC::ExecutionContextList_var ecs;
		ecs = myobj->get_owned_contexts();
		ecs[(CORBA::ULong)0]->set_rate(myobj->m_interval);
		std::cout << "OnSetConfiguration\t" << config_set.getName() << "\t" << config_set.getValue() << std::endl;
	}

 private:
	ConfigurationTest *myobj;
 };
```

### OnAddConfigurationAddCallback

```
 class MyOnAddConfigurationAdd
	: public RTC::OnAddConfigurationAddCallback
 {
 public:
	MyOnAddConfigurationAdd(ConfigurationTest *obj)
	{
		myobj = obj;
	}
	virtual void operator()(const coil::Properties& config_set)
	{
		RTC::ExecutionContextList_var ecs;
		ecs = myobj->get_owned_contexts();
		ecs[(CORBA::ULong)0]->set_rate(myobj->m_interval);
		std::cout << "OnAddConfigurationAdd\t" << config_set.getName() << "\t" << config_set.getValue() << std::endl;
	}

 private:
	ConfigurationTest *myobj;
 };
```

### OnRemoveConfigurationSetCallback
```
 class MyOnRemoveConfigurationSet
	: public RTC::OnRemoveConfigurationSetCallback
 {
 public:
	MyOnRemoveConfigurationSet(ConfigurationTest *obj)
	{
		myobj = obj;
	}
	virtual void operator()(const char* config_set)
	{
		RTC::ExecutionContextList_var ecs;
		ecs = myobj->get_owned_contexts();
		ecs[(CORBA::ULong)0]->set_rate(myobj->m_interval);
		std::cout << "OnRemoveConfigurationSet\t" << config_set << std::endl;
	}

 private:

	ConfigurationTest *myobj;

 };
```

### OnActivateSetCallback
```
 class MyOnActivateSet
	: public RTC::OnActivateSetCallback
 {

 public:
	MyOnActivateSet(ConfigurationTest *obj)
	{
		myobj = obj;
	}
	virtual void operator()(const char* config_id)
	{
		RTC::ExecutionContextList_var ecs;
		ecs = myobj->get_owned_contexts();
		ecs[(CORBA::ULong)0]->set_rate(myobj->m_interval);
		std::cout << "OnActivateSet\t" << config_id << std::endl;
	}

 private:

	ConfigurationTest *myobj;

 };
```

### サンプル
参考までに、コールバックが呼ばれると実行周期がコンフィギュレーションパラメーター Interval に設定されるという例を示します。
アクティブ、非アクティブに遷移したときにコールバックにより、コンフィギュレーションパラメーターが変更されることを確認します。

コンフィギュレーション(初期編) を参照して、初期パラメーターを設定します。
```
 static const char* configurationtest_spec[] =
  {
    "implementation_id", "ConfigurationTest",
    "type_name",            "ConfigurationTest",
    "description",            "Configuration Test Component",
    "version",                  "1.0.0",
    "vendor",                  "hogehoge",
    "category",               "TEST",
    "activity_type",         "PERIODIC",
    "kind",                     "DataFlowComponent",
    "max_instance",       "1",
    "language",              "C++",
    "lang_type",             "compile",
    // Configuration variables
    "conf.default.Interval",   "1000",
    "conf.default.Test",        "0",
    // Widget
    "conf.__widget__.Interval",   "text",
    "conf.__widget__.Test",        "text",
    // Constraints
    "conf.__constraints__.Interval",    "0 < x < 10000",
    ""
  };
```

```
 RTC::ReturnCode_t ConfigurationTest::onInitialize()
 {
   this->m_configsets.setOnUpdate(new MyOnUpdate(this));
   this->m_configsets.setOnUpdateParam(new MyOnUpdateParam(this));
   this->m_configsets.setOnSetConfigurationSet(new MyOnSetConfigurationSet(this));
   this->m_configsets.setOnRemoveConfigurationSet(new MyOnRemoveConfigurationSet(this));
   this->m_configsets.setOnAddConfigurationSet(new MyOnAddConfigurationAdd(this));
   this->m_configsets.setOnActivateSet(new MyOnActivateSet(this));
 
   bindParameter("Interval", m_interval, "1000");
   bindParameter("Test", m_test, "0");
  
   return RTC::RTC_OK;
 }
```

m_configsets は ConfigAdminクラス (コンフィギュレーション情報管理オブジェクト)で、ConfigAdmin.h にコールバックの定義があります。

まず、RTC を起動して、RTC を配置します。コンソールには以下のように表示されます。
<div align="center"><a href="ConfigurationCallback01.png"><img src="ConfigurationCallback01.png" width="70%;"></a></div>
<br>
<div align="center"><a href="ConfigurationCallback01-1.png"><img src="ConfigurationCallback01-1.png" width="70%;"></a></div>
<br>
<br>

次に、RTC をアクティブにします。コンソールには以下のように表示されます。
<div align="center"><a href="ConfigurationCallback05.png"><img src="ConfigurationCallback05.png" width="70%;"></a></div>
<br>
<div align="center"><a href="ConfigurationCallback02-1.png"><img src="ConfigurationCallback02-1.png" width="70%;"></a></div>
<br>

```
 RTC::ReturnCode_t ConfigurationTest::onActivated(RTC::UniqueId ec_id)
 {
    coil::Properties cproperties("default");
    cproperties.setProperty("Interval", "1");
    this->m_configsets.setConfigurationSetValues(cproperties);
    this->m_configsets.activateConfigurationSet("default");
    std::cout << "Interval:\t" << m_interval << std::endl;
    this->m_configsets.update("default","Test");
    std::cout << "Interval:\t" << m_interval << std::endl;
    this->m_configsets.update("default");
    std::cout << "Interval:\t" << m_interval << std::endl;
 
    return RTC::RTC_OK;
 }
```

<br>

Interval を「1000」から「1」に設定します。
```
 cproperties.setProperty("Interval", "1");
```

<br>

コンフィギュレーションセットを取得し追加します。このときに OnSetConfiguration が呼ばれます。
```
 this->m_configsets.setConfigurationSetValues(cproperties);
```

<br>

コンフィギュレーションセットをアクティブ化します。このときに OnSetActivateSet が呼ばれますが、まだコンフィギュレーションパラメーターは変更されていません。
```
 this->m_configsets.activateConfigurationSet("default");
```

<br>

もう一つのコンフィギュレーションパラメーター Test のみをアップデートします。Interval は「1000」のままです。
```
 this->m_configsets.update("default","Test");
```

<br>

コンフィギュレーションセットを更新し Interval に「1」を設定します。
```
 this->m_configsets.update("default");
```

<br>
<br>

次に、アクティブ化したまま RTSystemEditor で Interval を「2」に変更します。コンソールには以下のように表示されます。


<div align="center"><div align="center"><a href="ConfigurationCallback03.png"><img src="ConfigurationCallback03.png" width="70%;"></a></div>;  <div align="center"><a href="ConfigurationCallback04.png"><img src="ConfigurationCallback04.png" width="70%;"></a></div>;</div>
<br>
<div align="center"><a href="ConfigurationCallback03-1.png"><img src="ConfigurationCallback03-1.png" width="70%;"></a></div>
<br>
まず、上述同様、コンフィギュレーションセットへの更新パラメータの追加とアクティブ化が行われます。
onExecute の後 または onStateUpdate() の直後に更新が行われます。

<br>
<br>

続いて、RTC を非アクティブにします。コンソールには以下のように表示されます。

<div align="center"><a href="ConfigurationCallback06.png"><img src="ConfigurationCallback06.png" width="70%;"></a></div>
<br>
<div align="center"><a href="ConfigurationCallback06-1.png"><img src="ConfigurationCallback06-1.png" width="70%;"></a></div>
<br>

```
 RTC::ReturnCode_t ConfigurationTest::onDeactivated(RTC::UniqueId ec_id)
 {
    coil::Properties cproperties("default");
    cproperties.setProperty("Interval", "800");
    this->m_configsets.setConfigurationSetValues(cproperties);
    this->m_configsets.activateConfigurationSet("default");
    std::cout << "Interval:\t" << m_interval << std::endl;
    this->m_configsets.update("default","Interval");
    std::cout << "Interval:\t" << m_interval << std::endl;
    this->m_configsets.update("default");
    std::cout << "Interval:\t" << m_interval << std::endl;
 
   return RTC::RTC_OK;
 }
```

アクティブにしたときと異なるのは、Interval を 800 にした箇所と、m_configsets.update("default","Interval") として Interval のみ更新しているところです。
今回は、m_configsets.update("default","Interval") で値が更新されているか確認できます。

<br>
<br>

続いて、RTSyetemEditor でコンフィギュレーションセットを追加します。
図で [追加] ボタンをクリックした後に、[適用] ボタンをクリックすると OnAddConfigurationAddCallback を呼ぶことができます。
コンソールには以下のように表示されます。

<div align="center"><a href="ConfigurationCallback07.png"><img src="ConfigurationCallback07.png" width="70%;"></a></div>
<br>
<div align="center"><a href="ConfigurationCallback07-1.png"><img src="ConfigurationCallback07-1.png" width="70%;"></a></div>
<br>

同様に、コンフィギュレーションセットを削除することで OnRemoveConfigurationSetCallback を呼ぶことができます。

<br>

基本的に、パラメーターの変更は RTC のアクティビティが呼び出されるまではコンフィギュレーションパラメーターが外部で変更されても反映されませんが、コールバックを使うことでいろいろな設定ができるようになります。


