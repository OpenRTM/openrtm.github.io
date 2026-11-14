---
layout: page
title: "comp_conf_reference"
---
#contents(3)

This document explains the setting items of the file used to configure each component.
This file can be given any name, but for convenience it is referred to as component.conf.
component.conf is specified in rtc.conf as follows, using an option whose key is the component category name and component name or instance name.

```
 <コンポーネントカテゴリ名>.<コンポーネント名>.config_file: <任意のファイル名>.conf
 or
 <コンポーネントカテゴリ名>.<コンポーネントインスタンス名>.config_file: <任意のファイル名>.conf
```

Using the ConsoleIn component included in the samples as an example, the actual specification method is shown below.

```
 example.ConsoleIn.config_file: consolein.conf ← ConsoleInコンポーネント全体の設定
 example.ConsoleIn0.config_file: consolein0.conf ← 0番目のインスタンスの設定
 example.ConsoleIn1.config_file: consolein1.conf ← 1番目のインスタンスの設定
 example.ConsoleIn2.config_file: consolein2.conf ← 2番目のインスタンスの設定
```

<!-- ============================================================ -->
## Basic Settings
<!-- ============================================================ -->

### Basic Profile
The following items in the RTC Basic Profile (items set on the Basic tab of RTCBuilder) can be overridden with values in component.conf.

- implementation_id
- type_name
- description
- version
- vendor
- category
- activity_type
- max_instance
- language
- lang_type


<!-- ============================================================ -->
## Execution Context Options
<!-- ============================================================ -->

### exec_cxt.periodic.type

Specifies the Periodic-type ExecutionContext.
Specifies the type of EC to use. The following are available.

- PeriodicExecutionContext: Default. Embedded in the OpenRTM library.
- ExtTrigExecutionContext:   External trigger EC. Embedded in the OpenRTM library.
- SynchExtTriggerEC: Synchronous external trigger EC. Embedded in the OpenRTM library. Usually used with OpenHRP3.
- RTPreemptEC:               Real-time execution context for the Linux RT preemptive patch kernel.

Other ECs

- SimulatorExecutionContext: Parallel external trigger EC. Built into Choreonoid's OpenRTMPlugin and used automatically within Choreonoid.
- ArtExecutionContext:       Real-time EC for ARTLinux. Scheduled for deprecation. (http://sourceforge.net/projects/art-linux/)

- Setting: (PeriodicExecutionContext|ExTrigExecutionContext|SynchExtTriggerEC|RTPreemptEC)
- Default: PeriodicExecutionContext
- Example:
```
 exec_cxt.periodic.type: PeriodicExecutionContext
```

<!-- ------------------------------------------------------------ -->
### exec_cxt.periodic.rate

ExecutionContext execution cycle
<!-- The execution cycle of ExecutionContext -->

This option specifies the EC cycle specific to the RTC. The execution cycle of this EC overrides the default EC rate of the original RTC.

- Setting: Read/Write, period [Hz]
- Default: 1000 [Hz]
- Example:
```
 exec_cxt.periodic.rate: 1000
```

<!-- ------------------------------------------------------------ -->
### exec_cxt.sync_transition
### exec_cxt.sync_activation
### exec_cxt.sync_deactivation
### exec_cxt.sync_reset

Specifies the state transition mode.
The state of an RTC transitions through activation, deactivation, and reset.
Some execution contexts execute the main logic in a different thread.
If these flags are set to YES, activation, deactivation, and reset are executed synchronously.
In other words, when these flags are YES, the activation/deactivation/reset processing returns after the state transition is complete.

"synchronous_transition" sets the synchronous transition flag for all other synchronous transition flags (synchronous_activation / deactivation / resetting).

- Setting: YES/NO
- Default: YES
- Example:
```
 exec_cxt.sync_transition: YES
 exec_cxt.sync_activation: YES
 exec_cxt.sync_deactivation: YES
 exec_cxt.sync_reset: YES
```

<!-- ------------------------------------------------------------ -->
### exec_cxt.transition_timeout
### exec_cxt.activation_timeout
### exec_cxt.deactivation_timeout
### exec_cxt.reset_timeout

Timeout time during synchronous transitions.
When the synchronous transition flag is set to YES, the timeout settings become available. 
If "transition_timeout" is set, its value is set for all other timeouts for activation/deactivation and reset.

- Setting: timeout time [s]
- Default: 0.5 [s]
- Example:
```
 exec_cxt.transition_timeout: 0.5
 exec_cxt.activation_timeout: 0.5
 exec_cxt.deactivation_timeout: 0.5
 exec_cxt.reset_timeout: 0.5
```

<!-- ------------------------------------------------------------ -->
### exec_cxt.cpu_affinity

Sets the CPU affinity (assignment) of the EC.
This option binds the EC to a specific CPU. The option must be one or more comma-separated numbers used to identify CPU IDs. CPU IDs start from 0, and the maximum number is the number of CPU cores minus 1. If an invalid CPU ID is specified, all CPUs are used for the EC.

- Setting: CPU number
- Default: none
- Example:
```
 exec_cxt.cpu_affinity: 0
```

<!-- ------------------------------------------------------------ -->
### execution_contexts

Specifies execution contexts.
An RTC can be attached to zero or more execution contexts. 
The "execution_contexts" option specifies the ECs to attach specifically to the RTC and their names.
If the option is not specified, the internal global options or rtc.conf options related to ECs are used. 
If None is specified, no EC is created.
The types of ECs that can be specified are the same as those that can be specified with "exec_cxt.type".
In addition, when specifying the EC type, its name can also be specified.
The name is used as the key for options that specify the EC cycle and so on.

- Setting: None or <EC0>,<EC1>,...
  - <EC?>: ECtype(ECname)
- Default: None
- Example:
```
 execution_contexts: PeriodicExecutionContext(pec1000Hz), \
                               PeriodicExecutionContext(pec500Hz)
```

<!-- ------------------------------------------------------------ -->
### ec.<EC name>.rate
### ec.<EC name>.synch_transition
### ec.<EC name>.transition_timeout

EC-specific settings.
Each EC can have its own configuration. 
Individual configurations can be specified using the EC type name or EC instance name. 
An attached EC is specified with the "execution_context" option, such as <EC type name>(<EC instance name>).
EC-specific options can be specified as follows.

- Setting: ec.<EC type name>.<option> or ec.<EC instance name>.<option>
- Default: none
- Example:
```
 ec.PeriodicExecutionContext.sync_transition: NO
 ec.pec1000Hz.rate: 1000
 ec.pec1000Hz.synch_transition: YES
 ec.pec1000Hz.transition_timeout: 0.5
 ec.pec500Hz.rate: 500
 ec.pec500Hz.synch_activation: YES
 ec.pec500Hz.synch_deactivation: NO
 ec.pec500Hz.synch_reset: YES
 ec.pec500Hz.activation_timeout: 0.5
 ec.pec500Hz.reset_timeout: 0.5
```

<!-- End of Execution context settings -->
<!-- ============================================================ -->

<!-- ============================================================ -->
## Port Settings
<!-- Port configurations -->
<!-- ============================================================ -->

### InPort Options

- Format
```
 port.inport.<port_name>.* -> InPortBase.init() の引数に渡される
 port.inport.dataport.*    -> InPortBase.init() の引数に渡される
```

- Example
```
 port.inport.dataport.provider_types: corba_cdr, direct, shm_memory
 port.inport.dataport.consumer_types: corba_cdr, direct, shm_memory
 port.inport.dataport.connection_limit: 1
```


### OutPort Options

- Format
```
 port.outport.<port_name>.* -> OutPortBase.init() の引数に渡される
 port.outport.<port_name>.* -> OutPortBase.init() の引数に渡される
```

- Example
```
 port.inport.dataport.provider_types: corba_cdr, direct, shm_memory
 port.inport.dataport.consumer_types: corba_cdr, direct, shm_memory
 port.inport.dataport.connection_limit: 1
```


### Service Port Options
- Format
```
 port.corbaport.<port_name>.* -> CorbaPortBase.init() の引数に渡される
 port.corba.* -> CorbaPortBase.init() の引数に渡される 
```

<!-- End of Port configurations -->
<!-- ============================================================ -->

<!-- ============================================================ -->
## RTSystemEditor Configuration Set GUI Settings

Configuration parameters can be operated from the GUI widgets in RTSystemEditor's Configuration Set settings dialog.
Usually, when designing an RTC with RTCBuilder, you can specify the type of GUI widget to assign to each parameter, but widget assignments can also be specified from component.conf.

- Example
```
 conf.[configuration_set_name].[parameter_name]:
 conf.__widget__.[parameter_name]: GUI control type for RTSystemEditor
 conf.__constraint__.[parameter_name]: Constraints for the value
```

### List of Available Widgets [<u>widget</u>]

#### Format
```
 conf.__widget__.[widget_name]: [widget_type].[widget_option]
```

#### Format Details
- [widget_name]&#58; widget name = Configuration Set parameter name
  - text:          Text box (default)
  - slider.<step>: Horizontal slider. <step> is the slider step unit. A range constraint option (described later) is required.
  - spin:          Spin button. A range constraint option (described later) is required.
  - radio:         Radio button. An enumeration constraint option (described later) is required.
  - checkbox:      Check box. An enumeration constraint option is required. The parameter must be able to interpret a comma-separated list.
  - ordered_list:   Ordered list. An enumeration constraint option is required. The parameter must be able to interpret a comma-separated list. In this control, one or more enumerated elements appear in the list.
- [widget_type]&#58; type of widget to use, (text, slider, spin, radio, checkbox, ordered_list,)
- [widget_option]&#58; step unit can be specified only for slider

#### Example
```
 conf.__widget__.int_param0: slider.10
 conf.__widget__.int_param1: spin
 conf.__widget__.double_param0: slider.10
 conf.__widget__.double_param1: text
 conf.__widget__.str_param0: radio
 conf.__widget__.vector_param0: checkbox
 conf.__widget__.vector_param1: ordered_list
```

<!-- ------------------------------------------------------------ -->
### List of Available Constraints [<u>constraints</u>]
<!-- GUI control constraint options [__constraints__]: -->

#### Format
```
 conf.__constraints__.[parameter_name]:
```

#### Format Details
- none: (blank)
- literal value: 100 (constraint value)
- range: <, >, <=, >=, and the variable "x" can be used
- enumerated values:  (enum0, enum1, ...)
- array: <constraints0>, <constraints1>, ... for only array value
- hash value: {key0: value0, key1:, value0, ...}

#### Constraint Specification Examples
- No constraint              : (blank)
- Literal value                     : 100 (read only)
- 100 or greater                : x >= 100
- 100 or less                : x <= 100
- Greater than 100       : x > 100
- Less than 100                : x < 0
- 100 or greater and 200 or less: 100 <= x <= 200
- Greater than 100 and less than 200 : 100 < x < 200
- Enumeration constraint                : (9600, 19200, 115200)
- Array                      : x < 1, x < 10, x > 100
- Hash                 : {key0: 100<x<200, key1: x>=100}

- Example
```
 conf.__constraints__.int_param0: 0<=x<=150
 conf.__constraints__.int_param1: 0<=x<=1000
 conf.__constraints__.double_param0: 0<=x<=100
 conf.__constraints__.double_param1:
 conf.__constraints__.str_param0: (default,mode0,mode1)
 conf.__constraints__.vector_param0: (dog,monkey,pheasant,cat)
 conf.__constraints__.vector_param1: (pita,gora,switch)
```

