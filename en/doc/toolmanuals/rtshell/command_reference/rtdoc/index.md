---
layout: page
title: rtdoc
---

<!-- Title: rtdoc -->

## Format
```
 rtdoc [OPTION ...] PATH
```

## Note
In this section, due to limitations of the system used for this website, there are places where consecutive underscores cannot be written properly. In such places, they are written with a space in between as "_ _", but this means "__", so please read it by replacing it accordingly.

## Overview
Displays embedded documentation of an RT Component.

Some RT Components can embed documentation, which is implemented as a hidden configuration set. This command can display that embedded documentation in multiple formats. The supported formats are reStructuredText, HTML, and LaTeX (for conversion to PDF).

## Options
```
 -f FORMAT, --format=FORMAT
 　　　　　　Selects the format. Choose from rst, html, and latex.
 -g, --graph 　Displays a graph of the component.
 --version　　　Displays the program version number and exits.
 -h, --help　 　Displays help and exits.
 -v, --verbose Outputs more detailed information.
```

### RT Component Documentation
The embedded documentation handled by this command is written in the _ _doc_ _ configuration set. Parameters in this set (those that are not hidden) are added as sections.

Common sections are:

- **intro**
  - Introduction to the component. Describes an overview such as the purpose of its operation. (Title:  Introduction.)
- **reqs**
  - Describes items that require advance preparation, such as software that must be installed in advance in order to use the component. (Title:  Pre-requisites.)
- **install**
  - Describes how to install the component. (Title:  Installation.)
- **usage**
  - Describes how to start and use the component. (Title:  Usage.)
- **misc**
  - Describes other important information that is useful to know when using the component. (Title:  Miscellaneous.)
- **changelog**
  - |Describes the change history of the component. (Title:  Changelog.)

Also, if the component has ports or configurations, port and config sections are automatically created in its default configuration set. All other sections in the _ _doc_ _ set are added as this embedded documentation.

The following three parameters can also be added to the beginning of the documentation as additional information.

- _ _license_ _
  - License information such as GPL or BSD
- _ _contact_ _
  - Contact information such as the author's email address
- _ _url_ _
  - URL of the homepage related to the component

Parameters can be written either in the component source or in the configuration file loaded when the component starts. For documentation embedded in the source, except for short information such as usage and contact information, it is recommended to write it in a configuration file because it consumes the component binary data size.

For example, write the following in the source code:

```
 'conf.__doc__.__license__', 'LGPL',
 'conf.__doc__.__contact__', 'a@example.com',
 'conf.__doc__.__url__', 'http://www.openrtm.org',
 'conf.__doc__.intro', 'This is the introduction.',
 'conf.__doc__.reqs', 'This component requires nothing.',
 'conf.__doc__.install', 'Type "make install"',
 'conf.__doc__.usage', 'Run comp_standalone.',
 'conf.__doc__.misc', 'Extra information.',
 'conf.__doc__.changelog', 'No changes.',
 'conf.__doc__.Another', 'A non-standard section.',
```

By default, sections are included in the following order.
```
 intro, reqs, usage, ports, config, misc, changelog, [other sections]
```

This order can be changed with the _ _order_ _ parameter in the ＿ ＿doc_ _ set. Specify a comma-separated list of the names of each parameter in the documentation sections, for example as follows:
```
 'conf.__doc__.__order__', 'intro,ports,config,reqs,Another'
```

Sections not specified there will come after the specified sections, and their order is not defined.

Documentation for ports is added by adding a description property to the port, for example as follows:
```
 self._inport.addProperty('description', 'This port receives stuff.')
```

Documentation for configuration parameters is set by configuring parameters in the _ _description_ _ set, for example as follows:,
```
 'conf.default.param', '0',
 'conf.__description__.param', 'A test parameter.',
```

## Paths
rtshell indicates objects in the RTC tree using paths. Name servers and name contexts are specified as directory names, and managers and RT Components are specified as file names. Paths passed to commands are specified based on the current working directory of rtshell (for relative paths). The current working directory of rtshell is stored in an environment variable named RTCSH_CWD, and can be changed with the rtcwd command. (At present, the rtcwd command does not work in Linux environments.)

Available paths depend on the name servers referenced when commands are executed. The host name where a name server is running can be specified with the RTCTREE_NAMESERVERS environment variable. You can also specify the host where a name server is running directly as a path under the root, such as /<host name>/....

For example, /localhost/comp0.rtc indicates an RT Component named comp0.rtc registered with the name server on localhost. /localhost/manager/comp0.rtc indicates an RT Component named comp0.rtc registered in a directory named manager under the name server on localhost. ./comp0.rtc indicates an RT Component named comp0.rtc in the current working directory.

To indicate a port of an RT Component, specify it after the path separated by a colon (":"). For example, /localhost/comp0.rtc:data means the port named data of the RT Component named comp0.rtc.

Some commands can create new ports. In this case, you can add them to the path with options. The available options are the name of the created port and the formatter. Specify them as follows:

```
 <path>:<port>.<new_port_name>#<formatter>
```

### Example:
```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff#a_printer
```

This specifies that the name of the newly created port is stuff, and that the data is displayed on the terminal using a function (formatter) named a_printer. (The a_printer function must exist somewhere Python can use it. Normally, the user provides it in a module.) The created port is connected to the input port of comp0.rtc.

The `<new_port_name>` part is not required. If it is not specified, do not specify "." either. Example:

```
 /localhost/blurg.host_cxt/comp0.rtc:input#a_printer
```

The `<formatter>` part is not required. If it is not written, do not specify "." either. Example:

```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff
```

## Environment Variables
- **RTCTREE_ORB_ARGS**
  - Variables passed when creating the ORB. Separate them with semicolons. This is not required.
- **RTCTREE_NAMESERVERS**
  - Addresses of name servers referenced when creating the RTC tree. Separate addresses with semicolons. The listed addresses are added to the RTC tree and can be referenced by rtshell. This is not required because they can also be specified as directory names under the root in paths.
- **RTSH_CWD**
  - The current working directory of rtshell. rtshell sets it automatically. Do not set it manually.

In typical use, the only variable that users set is RTCTREE_NAMESERVERS. It is convenient to set frequently used name servers. For example, in the Bash shell, the following command allows rtshell to reference name servers on localhost, port 192.168.0.1:65346, and host example.com.

```
 $ export RTCTREE_NAMESERVERS=localhost;192.168.0.1:65346;example.com
```


## Return Values
Returns zero on success. Returns a non-zero value on failure.

Debug information and errors are output to stderr.

## Examples
- Displays the documentation of ConsoleOut0.rtc to standard output.
```
 $ rtdoc /localhost/ConsoleOut0.rtc
```

- Saves the documentation of ConsoleOut0.rtc to a file named doc.html.
```
 $ rtdoc /localhost/ConsoleOut0.rtc > doc.html
```

- Displays the documentation of ConsoleOut0.rtc in reStructuredText format.
```
 $ rtdoc /localhost/ConsoleOut0.rtc -f rst
```

- Saves the documentation of ConsoleOut0.rtc in PDF format using the rubber tool.
```
 $ rtdoc /localhost/ConsoleOut0.rtc -f latex > doc.tex && rubber -d doc.tex
```
