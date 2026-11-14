---
layout: page
title: "configuration files and command-line options (basics)"
---
<!-- Title: 設定ファイルとコマンドラインオプション (基礎編) -->
#contents

## Configuration File  ( rtc.conf ) 
The component manager reads the configuration file rtc.conf at startup.
The configuration file is usually created with the name rtc.conf, but a configuration file created with any name can also be passed.

### Location of rtc.conf

rtc.conf is usually placed in the same directory as the RTC executable file (standalone component: an RTC in executable format such as xxxComp or xxxComp.exe), so that its settings are loaded automatically.
Alternatively, you can use the <strong>-f</strong> option to load a configuration file with any name.
If rtc.conf is not in the same directory as the executable file or is not specified with the <strong>-f</strong> option, the system-wide rtc.conf is loaded instead.

The loading priority of rtc.conf is set as follows.

#### For Linux/Unix
1. Command-line option "-f"
1. Environment variable "RTC_MANAGER_CONFIG"
1. Default configuration file "./rtc.conf"
1. Default configuration file "/etc/rtc.conf"
1. Default configuration file "/etc/rtc/rtc.conf"
1. Default configuration file "/usr/local/etc/rtc.conf"
1. Default configuration file "/usr/local/etc/rtc/rtc.conf"
1. Embedded configuration values

#### For Windows
1. Command-line option "-f"
1. Environment variable "RTC_MANAGER_CONFIG"
1. Default configuration file "./rtc.conf"
1. Default configuration file "%RTM_ROOT%/%RTM_VC_VERSION%/rtc.conf"

On Windows, rtc.conf placed under the directory specified by the environment variables "RTM_ROOT" and "RTM_VC_VERSION" (usually C:\Program Files\OpenRTM-aist\(version number)\(VC version)) is loaded.

### Main Setting Items
The following are commonly used rtc.conf setting options.
Various options other than the following can also be specified in rtc.conf. For details, see [List of rtc.conf Setting Items]({{ site.baseurl }}/en/doc/developersguide/basic_rtc_programming/rtc_conf_reference).

#### Settings Related to the Name Service 
Items related to naming service settings are as follows.

:<strong>corba.nameservers</strong>|
Specified as host_name:port_number; the default port is 2809 (omniORB default).~
Multiple servers can be specified, and the delimiter between server names is a comma ",".

:<strong>naming.formats</strong>|
%h.host_cxt/%n.rtc →host.host_cxt/MyComp.rtc~
Multiple specifications are possible.~
If you want 0.2.0 compatibility, use:~
%h.host_cxt/%M.mgr_cxt/%c.cat_cxt/%m.mod_cxt/%n.rtc

:<strong>naming.update.enable</strong>|
“YES” or “NO”~
Automatic update setting for registration with the naming service.~
When the name service is started after the component is started, the name is registered again.

:<strong>naming.update.interval</strong>|
Update cycle [s]. The default is 10 seconds.

:<strong>timer.enable</strong>|
“YES” or “NO”~
Enables/disables the manager timer. It must be enabled to use naming.update.

:<strong>timer.tick</strong>|
Timer resolution [s]. The default is 100 ms.

#### Settings Related to Log Output

:<strong>logger.enable</strong>|
“YES” or “NO”~
Enables/disables log output.

:<strong>logger.file_name</strong>|
Log file name.~
%h: host name, %M: manager name, %p: process ID can be used

:<strong>logger.date_format</strong>|
Date format. Conforms to strftime(3) notation.~
Default: %b %d %H:%M:%S → Apr 24 01:02:04|

:<strong>logger.log_level</strong>|
Log level: SILENT, ERROR, WARN, INFO, DEBUG, TRACE, VERBOSE, PARANOID.~
<!-- ログレベル： SILENT, ERROR, WARN, NORMAL, INFO, DEBUG, TRACE, VERBOSE, PARANOID.~ -->
Outputs nothing (SILENT) through outputs everything (PARANOID).~
※Previously this could be used inside RTC, but currently it cannot be used.


#### Settings Related to Execution Contexts 

:<strong>exec_cxt.periodic.type</strong>|
Specifies the execution context to use.~
Currently,
PeriodicExecutionContext and ExtTrigExecutionContext
are available.~
The default is PeriodicExecutionContext.

:<strong>exec_cxt.periodic.rate</strong>|
Specifies the execution context frequency [Hz].~
Valid range: (0, 1000000].~
Default: 1000.~


#### Other Settings 

:<strong>corba.endpoint</strong>|
Specified as IP_Addr:Port. When there are multiple NICs, this specifies which one the ORB should listen on.~
Even when Port is not specified, <strong>:</strong> is required.~
Example:  corba.endpoint: 192.168.0.12~
If there are two NICs, be sure to specify this.
(It may work correctly by chance even if it is not specified.)

:<strong>corba.args</strong>|
Arguments for CORBA. For details, refer to the omniORB manual.

<strong>[category name].[component name].config_file</strong>|
<strong>[category name].[instance name]. config_file</strong>|
Component configuration file
If the category name is manipulator, the component name is myarm, and the instance names are myarm 0, 1, 2, ...
```
 manipulator.myarm.config_file: arm.conf
 または
 manipulator.myarm0.config.file: arm0.conf
```
can be specified as shown above.

## Command-Line Options


For standalone components or the RTC daemon (rtcd), several options can be specified on the command line.
The following table shows the command-line options that can be specified.

hogehogehoge

<table class="table-alt">
  <tr>
    <th>Option</th>
    <th>Meaning</th>
  </tr>
  <tr>
    <td>-a</td>
    <td>Manager service OFF</td>
  </tr>
  <tr>
    <td>-f file name</td>
    <td>Specifies the configuration file</td>
  </tr>
  <tr>
    <td>-o option</td>
    <td>Specifies an option</td>
  </tr>
  <tr>
    <td>-p port number</td>
    <td>Specifies the port number</td>
  </tr>
  <tr>
    <td>-d</td>
    <td>Specifies the master manager</td>
  </tr>
</table>


The detailed meanings of these options are shown below.

### -a: Manager Service OFF

Normally, to start an RTC, the internal component manager instantiates and deletes RTCs. (This is called lifecycle management.)
By default, a server (servant) is started so that this manager can be controlled remotely.
However, if there is no need after startup to start the same RTC in the same process, load another RTC module and start an RTC, or perform similar operations, the servant is unnecessary, so startup of the servant can be suppressed by specifying the <strong>-a</strong> option.

### -f: Specify Configuration File

By using the <strong>-f</strong> option, you can give a file with any name to a standalone component or rtcd instead of rtc.conf.

```
 <利用例>
 ConsoleInComp -f consin.conf
```


### -o: Specify Option

By using the <strong>-o</strong> option, you can provide options that can be specified in rtc.conf from the command line. Options given with the <strong>-o</strong> option take precedence over those specified in rtc.conf, so it is useful to use the <strong>-o</strong> option when you want to temporarily override and change options specified in rtc.conf.
However, because they are passed as command-line options, spaces are recognized as argument separators, so when specifying them, you must either not include spaces or enclose the option in single quotes or double quotes.

```
 <利用例>
 ConsoleInComp -o corba.nameservers:localhost,openrtm.org
 ConsoleInComp -o "corba.nameservers:localhost, openrtm.org"
 <正しく認識されない例>
 ConsoleInComp -o corba.nameservers:localhost, openrtm.org
 '',(カンマ)''の後に空白があるため、openrtm.org が別の引数として認識される。
```


### -p: Specify Port Number

By using <strong>-p</strong>, you can specify the port number used by the RTC being started.
If you want to start the RTC with a specific port number, use this option.
This option behaves the same as specifying only the port number without a host name in the <strong>corba.endpoints:</strong> option.

```
 <利用例>
 ConsoleInComp -p 2810
 以下と同じ
 ConsoleInComp -o "corba.endpoints: :2810" 
```

### -d: Specify Master Manager

By using the <strong>-d</strong> option, you can start the standalone component or rtcd as a daemon and as the master manager.
Managers include master and slave managers. The master normally waits for requests on the fixed port number 2810 and delegates RTC startup and other operations to slaves.
When started with the <strong>-d</strong> option specified, the port number is fixed to 2810 by default, the manager servant is started in master mode, and a reference to the manager is registered with the name service.
