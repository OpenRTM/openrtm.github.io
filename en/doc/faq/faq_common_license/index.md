---
layout: page
title: faq on general matters and licenses
---

<!-- Title: 一般・ライセンスに関する FAQ -->
#contents


## About Using OpenRTM

### What is the difference between RT Middleware and OpenRTM-aist?

RT Middleware means middleware for Robot Technology (robot technology elements). This is not something limited to AIST; it is a general term that broadly refers to middleware for robots. Therefore, other robot platforms and middleware such as ROS, OROCOS, and OPRoS can also be called RT Middleware in a broad sense.
On the other hand, in general, implementations of the [OMG RTC standard specification](http://www.omg.org/spec/RTC) are often called RT Middleware.

The RT Middleware developed and distributed as open source by AIST is called OpenRTM-aist as a proper noun. In addition, there are several compatible implementations of RT Middleware conforming to the OMG RTC standard, such as OpenRTM.NET by SEC Co., Ltd., RT-Middleware on Android, and RT Middleware by Honda R&D Co., Ltd.


### Does it cost money to use OpenRTM-aist?

OpenRTM-aist is so-called open-source software whose source code is released under the LGPL license.
No money is required at all to use it.

For details, please refer to the FAQ on "Licenses" below.


### Do I need to apply to AIST to use OpenRTM-aist?

OpenRTM-aist is an LGPL open-source product, so you do not need to obtain permission from AIST at all in order to use it.
You are free to download and use it.
Also, as long as you comply with the LGPL license, you are free to incorporate it into products and sell them. You do not need to obtain permission from AIST.
However, if you would like to use it in a product, we would appreciate it if you could let us know via the mailing list or the [contact form on the Web page]()(No corresponding page available.).


### Is support provided? Is there any warranty?

OpenRTM-aist is an open-source product without warranty. OpenRTM-aist is provided As-Is, and AIST and its developers make no warranty of any kind regarding its use or performance.
In addition, AIST and the developers do not guarantee the achievements or results obtained by using OpenRTM-aist, and AIST and the developers have no obligation to fix bugs or other defects.
This is equivalent to the no-warranty clauses commonly included in software licenses in general, not only open-source software.

However, AIST provides the following for information sharing among users:

- [Mailing list]()(No corresponding page (mailinglist) available.)
- [Web forum]()(No corresponding page (forum) available.)

Through questions posted there, we make efforts to answer questions as much as possible.
Furthermore, we hold training courses, summer camps, contests, and other events to promote the acquisition of RT component development and system development skills, and we make efforts to respond to questions and feedback as much as possible through those opportunities.

For details, please refer to "About the Community."



## Licenses, etc.

### What is the license of OpenRTM-aist?

OpenRTM-aist (C++, Python, Java versions) adopts a dual licensing system consisting of the LGPL (GNU Lesser General Public License) and individual contracts with AIST.
The tools (RTCBUilder, RTSystemEditor) adopt a dual licensing system consisting of the EPL (Eclipse Public License) and individual contracts with AIST.

### What is dual licensing?

The method of distributing a single piece of software under two or more different licenses is called dual licensing.
When software is distributed under dual licenses, users can choose one of the licenses in order to use or redistribute the software. For details, please see Wikipedia and other sources.

- [Dual licensing (wikipedia)](http://ja.wikipedia.org/wiki/%E3%83%87%E3%83%A5%E3%82%A2%E3%83%AB%E3%83%A9%E3%82%A4%E3%82%BB%E3%83%B3%E3%82%B9)


### Why is it dual licensed?

We want to spread OpenRTM-aist and the concepts of RT Middleware and RT components, and for that reason we distribute the software as open source.
On the other hand, we at AIST also have a mission to support companies that want to use RT Middleware in practice to commercialize and put robots and other systems into practical use.
In such cases, distributing only under an open-source license imposes several restrictions that may be inconvenient for companies, so we adopt a dual licensing system that also allows individual contracts separate from open source.

### In what cases is an individual contract required?

For example, if you want to modify the OpenRTM-aist core itself and incorporate it into a system, but do not want to publish the modified portions, you cannot use OpenRTM-aist under the LGPL license, so you need to enter into an individual contract with AIST.
In that case, we will charge a small implementation fee, but please rest assured that, given our position of promoting RT Middleware, we will never charge an exorbitant implementation fee.

### Why are the licenses for OpenRTM-aist and the tools different?

OpenRTM-aist adopts the LGPL, while the tools adopt the EPL. There are differences between the LGPL and the EPL, such as patent clauses and whether they can be used together with GPL-licensed libraries.

The EPL has patent clauses, and patents held by contributors to the software do not affect the software (users are granted a royalty-free patent license), making it a safer license for users. However, because it is incompatible with the GPL, it cannot be used together with GPL software.
Therefore, in Eclipse, which is licensed under the EPL, it is customary for plugins (RTCBuilder, RTSystemEditor, etc. are also plugins) to also be under the EPL. (It is possible to apply the GPL to plugins by adding an exception clause, however.)

On the other hand, when creating RT components in C++ or Python using OpenRTM-aist, linking with GPL-licensed libraries can easily occur. Therefore, if OpenRTM-aist itself were made EPL, linking with such GPL libraries would effectively become impossible, so the LGPL, which is compatible with the GPL, is adopted.



## About the Community

### How can I participate in the OpenRTM-aist community?

By participating in the OpenRTM-aist community, you can obtain information necessary for using OpenRTM-aist and exchange information with other users.
There are several ways to do this, including the following.

- Join the mailing list
- Join the forum
- Join Facebook
- Attend a training course
- Join the summer camp
- Publish RT components you have created
- Participate in the RT Middleware Contest
- Present at academic conferences, etc.

Please see the following FAQ for details.


### How can I join the mailing list?

The easiest way to participate in the community is to join the mailing list.
There is a mailing list for discussing topics related to OpenRTM-aist and RT Middleware in general. It is a place to consult about problems such as being unable to install OpenRTM-aist or components not connecting properly, and it is also used to announce information about training courses, events, and so on.

Joining is very easy: submit the required information on this page, then click the link in the automatically sent email to complete the process.

- http://www.openrtm.org/mailman/listinfo/openrtm-users

### How can I participate in the forum?

A forum is a bulletin board provided on a Web page. A forum is provided on OpenRTM.org.

- http://openrtm.org/openrtm/ja/community/forum_ja

This forum is linked with the mailing list. Mailing list content is automatically posted to the forum as well, and conversely, content posted to the forum is also posted to the mailing list.


### How can I join Facebook?

Information about OpenRTM-aist is also posted on Facebook. Announcements related to RT Middleware are posted about once or twice a week, so if you use Facebook, the announcements will appear in your timeline.
In addition, topics related to RT Middleware may also be provided by users.

If you use Facebook, please access the following page and click "Like":

- https://www.facebook.com/openrtm

Alternatively, access the following OpenRTM-aist Web page and click the "Like" button at the upper right to complete registration.

- http://openrtm.org/


### How can I attend a training course?

AIST holds RT Middleware training courses on a regular or irregular basis.

Usually, we hold RT Middleware training courses as tutorials at the JSME Robotics and Mechatronics Conference.
They may also be held irregularly for events or upon request. In such cases, announcements will be made through NEWS on http://openrtm.org, Facebook, and the mailing list.


### How can I participate in the summer camp?

AIST holds a residential training course called the RT Middleware Summer Camp every summer.
At the summer camp, participants usually stay from Monday to Friday at AIST's lodging facility (Sakura-kan) and learn how to build robot systems using RT Middleware through lectures, practical exercises, and result presentations.

Eligibility requires that participants have attended at least one of the training courses mentioned above, and the training course is primarily focused on learning more practical system construction.

### What is the project page?

The project page is a site on openrtm.org for publishing RT components. Anyone can publish RT components they have created.
You can also search for and download components you need from there.

- Project page: http://openrtm.org/openrtm/ja/project/projects_ja

To register your own components on the project page, you need to elevate your user privileges.
For details, please see:

- [Project creation manual](http://openrtm.org/openrtm/ja/node/1554)(No corresponding English project page (How to Register) available.)(No corresponding English project page (How to Register) available.)

### How can I participate in the RT Middleware Contest?

The RT Middleware Contest is held every December at the conference of the Society of Instrument and Control Engineers, System Integration Division.
The contest is held as an organized session of the conference, and participants register in advance on the OpenRTM Web page some software work using RT Middleware, in addition to the paper submitted to the conference, and receive evaluations from judges and volunteer general judges.
After the final presentation at the conference, the judging committee is held and various awards are presented.

One feature of the RT Middleware Contest is the large number of awards. Individuals or companies can provide sponsorship awards with contributions of 10,000 to 20,000 yen per award and establish their own awards.
Each award can be given based on the criteria of the sponsoring individual or company. The best work is determined by the judging committee, and the Best Award is presented by the System Integration Division of the Society of Instrument and Control Engineers.

### How can I present at academic conferences, etc.?

Organized sessions titled "RT Systems and Openness" and "RT Middleware and Openness" are held every year at the JSME Robotics and Mechatronics Conference (ROBOMECH), the Annual Conference of the Robotics Society of Japan, and the conference of the Society of Instrument and Control Engineers, System Integration Division.
These organized sessions are for discussing examples of system construction using RT Middleware or other robot middleware, problems encountered when building software, and related topics.
We especially hope that students who are interested in robot software will give presentations.
Announcements for organized sessions are also made through the Web page, Facebook, and the mailing list.

