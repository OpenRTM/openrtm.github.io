---
layout: page
title: "developer's guide"
---

<!-- Title: デベロッパーズガイド -->
<div align="right"><img src="devguide.png" width="20%;" align="right"></div>

Documentation for RT Component developers. It explains how to create RTCs and how to create systems by combining RTCs, divided into an "Introduction" and an "Advanced" section.
It also explains the more detailed internal structure of OpenRTM-aist.


## Introduction to RTC Programming

- [Data Port (Basics)](./basic_rtc_programming/dataport)
- [Service Port (Basics)](./basic_rtc_programming/servcieport)
- [Configuration (Basics)](./basic_rtc_programming/configuration)
- [Configuration Files and Command-Line Options (Basics)](./basic_rtc_programming/configuration_file_commandlineoption)
- [Manager (Basics) Under Writing](./basic_rtc_programming/manager)
- [List of rtc.conf Setting Items](./basic_rtc_programming/rtc_conf_reference)
- [List of component.conf Setting Items](./basic_rtc_programming/comp_conf_reference)


## [Introduction to RT System Development](./rt_system_development/)(Under Writing)

## RTC Programming (Advanced)

- [Data Port (Advanced)](./advanced_rtc_programming/dataport_advanced)
- [Service Port (Advanced)](./advanced_rtc_programming/serviceport_adavanced)
- [Configuration (Advanced)](./advanced_rtc_programming/configuration_adavanced)
- [SDO Service](./advanced_rtc_programming/sdo_service)


## RT System Development (Advanced)

- [Using DDS Communication Functionality](./advanced_rt_system_programming/dds_comm_use)
- [Using SSM Communication Functionality](./advanced_rt_system_programming/ssm_comm_use)
- [Log Collection with Fluent Logger](./advanced_rt_system_programming/fluent_logger_use)
- [Using ROS2 Communication Functionality](./advanced_rt_system_programming/ros2_comm_use)
- [Using ROS Communication Functionality](./advanced_rt_system_programming/ros_comm_use)
- [Acquiring the State of an RTC (EC)](./advanced_rt_system_programming/acquire_rtc_ec_status)
- [Procedure for Creating a Custom Execution Context](./advanced_rt_system_programming/create_ec)
- [RTC Operation Functions (CORBA_RTCUtil) User Manual](./advanced_rt_system_programming/corba_rtcutil_usersmanual)
- [Procedure for Implementing a Custom Interface Type for Data Ports](./advanced_rt_system_programming/implement_dataport_interface_type)
- [How to Use LocalService](./advanced_rt_system_programming/localservice_use)
- [Accessing RTCs in rtcname Format and rtcloc Format](./advanced_rt_system_programming/rtcname_rtcloc)
- [How to Use HTTPTransport](./advanced_rt_system_programming/httptransport_use)
- [How to Use SSLTransport](./advanced_rt_system_programming/ssltransport_use)
- [How to Use LogicalTimeTriggeredEC](./advanced_rt_system_programming/logicaltimetriggeredec_use)
- [Procedure for Creating an FSM Component](./advanced_rt_system_programming/create_fsm_comp)
- [Order in Which Callback Functions Are Called During Connector Generation and Data Transfer](./advanced_rt_system_programming/callbackfunction_callingorder)
- [How to Use Multi-Level Composite Components](./advanced_rt_system_programming/hierarchy_composite_comp_use)
- [How to Use OpenHRPExecutionContext](./advanced_rt_system_programming/openhrpexecutioncontext_use)
- [How to Use ExtTrigExecutionContext](./advanced_rt_system_programming/exttrigexectuioncontext_use)
- [How to Use SimulatorExecutionContext](./advanced_rt_system_programming/simulatorexecutioncontext_use)
- [How to Implement a Custom Logger](./advanced_rt_system_programming/implement_original_logger)
- [How to Use CSP Ports](./advanced_rt_system_programming/csp_port_use)
- [Using Callback Functions for Component Actions](./advanced_rt_system_programming/callbackfunction_use_by_componentaction)
- [Using Callback Functions for Manager Actions](./advanced_rt_system_programming/callbackfunction_use_by_manageraction)
- [Procedure for Implementing a Custom Serializer](./advanced_rt_system_programming/implement_original_serializer)
- [Manager Functions](./advanced_rt_system_programming/manager_functions)
- [How to Use the Choreonoid OpenRTM Plugin](./advanced_rt_system_programming/choreonoid_openrtm_plugin)
- [Procedure for Building OpenRTM-aist (C++ Version) with CMake](./advanced_rt_system_programming/openrtm_cpp_cmake_build)
- [TAO-Related Settings](./advanced_rt_system_programming/tao_setting)
- [Master Manager and Slave Manager](./advanced_rt_system_programming/mastermanager_slavemanager)

## Inside OpenRTM-aist

- [Overview of Operation When Configuration Parameters Are Updated](./inside_openrtm-aist/operation_overview_at_config_parameter_update)
- [Overview of Component Observers](./inside_openrtm-aist/component_observer_overview)
- [Overview of FSM Components](./inside_openrtm-aist/fsm_component_overview)
- [Overview of Composite Components](./inside_openrtm-aist/composite_component_overview)

