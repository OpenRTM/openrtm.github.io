---
layout: page
title: other faqs
---

<!-- Title: その他 FAQ -->

### Documents and materials for understanding the structure of each data type included in the installed OpenRTM
Please refer to the following pages.
<br>
<br>
- [http://openrtm.org/doc/idl/1.1/idlreference_ja/index.html](http://openrtm.org/doc/idl/1.1/idlreference_ja/index.html)
- [https://github.com/Nobu19800/DataTypeManual/wiki](https://github.com/Nobu19800/DataTypeManual/wiki)
<br>
<br>

### I want to check the data between ports, but I do not know how to debug it
Debugging is performed using rtprint, rtinject, and other rtshell commands. Please refer to the following page.
<br>
<br>
[http://www.openrtm.org/pub/OpenRTM-aist/tools/rtshell/3.0/ja/rtprint.html](http://www.openrtm.org/pub/OpenRTM-aist/tools/rtshell/3.0/ja/rtprint.html)
<br>
<br>

### Is real-time performance guaranteed even when communicating between different OSes?
If the OS supports real-time operation, it is possible to create an RTC with real-time performance, but when communication is involved, it is difficult as long as TCP/IP is used.
<br>
<br>
