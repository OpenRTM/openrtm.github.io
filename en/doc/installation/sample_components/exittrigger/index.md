---
layout: page
title: "exttrigger"
---
<!-- Title: ExtTrigger -->

### Overview

This sample demonstrates an ExecutionContext in which processing is executed in response to external input (events).

- Run ExtConsoleIn.bat and ExtConsoleOut.bat to start the two sample components.
- After both components have been started, run ExtConnector.bat to connect the ports of the two components.

### Startup Screens

<div align="center"><a href="java_exttrigsample0.png"><img src="java_exttrigsample0.png" width="80%;"></a></div>
<div align="center"><strong>ExtTrigger Execution Example (ExtConsoleIn)</strong></div>

<div align="center"><a href="java_exttrigsample1.png"><img src="java_exttrigsample1.png" width="80%;"></a></div>
<div align="center"><strong>ExtTrigger Execution Example (ExtConsoleOut)</strong></div>

<div align="center"><a href="java_exttrigsample2.png"><img src="java_exttrigsample2.png" width="80%;"></a></div>
<div align="center"><strong>ExtTrigger Execution Example (ExtConnector)</strong></div>

When the port connection is successfully established, a menu is displayed in the console where ExtConnector was executed, allowing you to select which component should proceed with processing.

Based on the selected input value, each component advances its processing by one execution cycle at a time.

