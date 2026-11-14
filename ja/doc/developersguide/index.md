---
layout: page
title: " デベロッパーズガイド"
---

<!-- Title: デベロッパーズガイド -->
<div align="right"><img src="devguide.png" width="20%;" align="right"></div>

RTコンポーネント開発者向けのドキュメント。RTCを作る方法および、RTCを組み合わせてシステムを作る方法について、「入門編」と「応用編」に分けて解説します。
また、OpenRTM-aistのより詳細な内部構造についても解説します。


## RTCプログラミング入門

- [データポート (基礎編)](./basic_rtc_programming/dataport)
- [サービスポート (基礎編)](./basic_rtc_programming/servcieport)
- [コンフィギュレーション(基礎編)](./basic_rtc_programming/configuration)
- [設定ファイルとコマンドラインオプション (基礎編)](./basic_rtc_programming/configuration_file_commandlineoption)
- [マネージャ (基礎編)執筆中](./basic_rtc_programming/manager)
- [rtc.conf設定項目一覧](./basic_rtc_programming/rtc_conf_reference)
- [component.conf 設定項目一覧](./basic_rtc_programming/comp_conf_reference)


## [RTシステム開発入門](./rt_system_development/)(執筆中)

## RTCプログラミング (応用編)

- [データポート (応用編)](./advanced_rtc_programming/dataport_advanced)
- [サービスポート (応用編)](./advanced_rtc_programming/serviceport_adavanced)
- [コンフィギュレーション (応用編)](./advanced_rtc_programming/configuration_adavanced)
- [SDO サービス](./advanced_rtc_programming/sdo_service)


## RTシステム開発 (応用編)

- [DDS通信機能の利用](./advanced_rt_system_programming/dds_comm_use)
- [SSM通信機能の利用](./advanced_rt_system_programming/ssm_comm_use)
- [Fluent Loggerによるログ収集](./advanced_rt_system_programming/fluent_logger_use)
- [ROS2通信機能の利用](./advanced_rt_system_programming/ros2_comm_use)
- [ROS通信機能の利用](./advanced_rt_system_programming/ros_comm_use)
- [RTC（EC）の状態を取得する](./advanced_rt_system_programming/acquire_rtc_ec_status)
- [独自実行コンテキストの作成手順](./advanced_rt_system_programming/create_ec)
- [RTC操作関数(CORBA_RTCUtil)利用マニュアル](./advanced_rt_system_programming/corba_rtcutil_usersmanual)
- [データポートの独自インターフェース型の実装手順](./advanced_rt_system_programming/implement_dataport_interface_type)
- [LocalServiceの利用方法](./advanced_rt_system_programming/localservice_use)
- [rtcname形式、rtcloc形式でのRTCへのアクセス](./advanced_rt_system_programming/rtcname_rtcloc)
- [HTTPTransportの使用方法](./advanced_rt_system_programming/httptransport_use)
- [SSLTransportの使用方法](./advanced_rt_system_programming/ssltransport_use)
- [LogicalTimeTriggeredECの使用方法](./advanced_rt_system_programming/logicaltimetriggeredec_use)
- [FSMコンポーネント作成手順](./advanced_rt_system_programming/create_fsm_comp)
- [コネクタ生成時、データ転送時にコールバック関数が呼ばれる順序について](./advanced_rt_system_programming/callbackfunction_callingorder)
- [多階層複合コンポーネントの利用方法](./advanced_rt_system_programming/hierarchy_composite_comp_use)
- [OpenHRPExecutionContextの使用方法](./advanced_rt_system_programming/openhrpexecutioncontext_use)
- [ExtTrigExecutionContextの使用方法](./advanced_rt_system_programming/exttrigexectuioncontext_use)
- [SimulatorExecutionContextの使用方法](./advanced_rt_system_programming/simulatorexecutioncontext_use)
- [独自ロガーの実装方法](./advanced_rt_system_programming/implement_original_logger)
- [CSPポートの使用方法](./advanced_rt_system_programming/csp_port_use)
- [コンポーネントアクションのコールバック関数の利用](./advanced_rt_system_programming/callbackfunction_use_by_componentaction)
- [マネージャアクションのコールバック関数の利用](./advanced_rt_system_programming/callbackfunction_use_by_manageraction)
- [独自シリアライザの実装手順](./advanced_rt_system_programming/implement_original_serializer)
- [マネージャの機能](./advanced_rt_system_programming/manager_functions)
- [Choreonoid OpenRTMプラグインの利用方法](./advanced_rt_system_programming/choreonoid_openrtm_plugin)
  - [Choreonoid入門](./advanced_rt_system_programming/choreonoid_openrtm_plugin/tutorial)
  - [myCobot280の制御](./advanced_rt_system_programming/choreonoid_openrtm_plugin/tutorial_serviceport)
- [OpenRTM-aist(C++版)のCMakeによるビルド手順](./advanced_rt_system_programming/openrtm_cpp_cmake_build)
- [TAO関連の設定](./advanced_rt_system_programming/tao_setting)
- [マスターマネージャ、スレーブマネージャ](./advanced_rt_system_programming/mastermanager_slavemanager)

## インサイドOpenRTM-aist

- [コンフィギュレーションパラメータ更新時の動作概要](./inside_openrtm-aist/operation_overview_at_config_parameter_update)
- [コンポーネントオブザーバーの概要](./inside_openrtm-aist/component_observer_overview)
- [FSMコンポーネントの概要](./inside_openrtm-aist/fsm_component_overview)
- [複合コンポーネントの概要](./inside_openrtm-aist/composite_component_overview)


