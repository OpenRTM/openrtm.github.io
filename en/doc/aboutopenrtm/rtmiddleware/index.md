---
layout: page
title: "what is openrtm-aist?"
---
<!-- Title: What is OpenRTM-aist? -->
<div align="right"><img src="piping_rtm_logo2.png" width="15%;" align="right"></div>

OpenRTM-aist is a software platform for component-oriented development of robotic systems.
<!--break-->
In OpenRTM-aist, when building a robotic system, software modules called RT Components (RTCs) are created for each functional element, and the system is constructed by connecting these components together. RT Components can be developed in **C++**, **Python**, and **Java**, and support major operating systems such as Linux/Unix, Windows, and Mac OS X.

For component development and system development using components, both **Eclipse**-based tools and command-line tools are available.

RT Components provide features such as ports for exchanging data and commands between components, activities that define standardized state transitions and behavior, and configurations that allow parameters to be manipulated externally.

By utilizing these features, it is easy to create highly independent and reusable modules. By reusing existing components, systems can be built with minimal programming effort.

OpenRTM-aist is implemented using CORBA, a distributed object standard, with an emphasis on network transparency and independence from operating systems and programming languages. Currently, OpenRTM-aist implementations are available in C++, Python, and Java.

- [RT Middleware]({{ site.baseurl }}/en/doc/aboutopenrtm/rtmiddleware/)
- [License]({{ site.baseurl }}/en/doc/aboutopenrtm/license/)
- [OpenRTM-aist Specifications]({{ site.baseurl }}/en/doc/aboutopenrtm/specification/)
- [RT Component Architecture]({{ site.baseurl }}/en/doc/aboutopenrtm/rtc_architecture)
- [RTC Development Flow]({{ site.baseurl }}/en/doc/aboutopenrtm/rtc_developmentflow/)
- [RT System Development Flow]({{ site.baseurl }}/en/doc/aboutopenrtm/rts_developmentflow/)
- [Research and Development]({{ site.baseurl }}/en/doc/aboutopenrtm/researchanddevel/)

