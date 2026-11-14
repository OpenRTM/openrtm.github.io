---
layout: page
title: ccm
---

<!-- Title: CCM -->
#contents
## CCM (CORBA Component Model)

CCM provides a server-side component model for CORBA, as well as a framework for building an EJB-like component environment on a CORBA environment.

### Components 
There are various definitions of a component, but it is generally said to be a "reusable unit of software."
According to a definition by M. Collins-Cope and others, something that satisfies the following four requirements is called a component, and this definition appears to be widely used.

<table class="table-alt">
  <tr>
    <td>Self-contained / self-describing</td>
    <td>It exists as an independent functional unit, and its interface is defined declaratively. In addition, standard methods are defined for its operation and manipulation, and the mechanisms for them are clearly defined.</td>
  </tr>
  <tr>
    <td>Dynamic function addition and modification are possible</td>
    <td>Properties, events, and other settings can be configured and changed from outside the component. A standard method for doing so is also provided.</td>
  </tr>
  <tr>
    <td>Interface transparency</td>
    <td>Based on the interface definition, a method for cooperation at the binary level is provided.</td>
  </tr>
  <tr>
    <td>Support for loose coupling with other components</td>
    <td>It does not have a direct communication path with other components, and is connected through a framework such as a container or assembly environment.</td>
  </tr>
</table>

"New Distributed Environments Opened by CORBA Components," Junichi Suzuki, Doctor Dobb's Journal Japanese Edition, April 1999 issue, pp.150-158.


### Component Model 
<table class="table-alt">
  <tr>
    <td>Facet</td>
    <td>Indicates that the component's interface is exposed externally. Clients can obtain the exposed interface through introspection and call the methods provided by the interface.</td>
  </tr>
  <tr>
    <td>Receptacle</td>
    <td>Indicates that interfaces provided by other components can be connected. Receptacle types include Simplex Receptacle, to which one interface can be connected, and Multiplex Receptacle, to which multiple interfaces can be connected to the same Receptacle.</td>
  </tr>
  <tr>
    <td>Event Source</td>
    <td>Indicates that a specific event is issued. Event notification types include Publisher, which can notify one-to-many, and Emitter, which can notify only one at a time.</td>
  </tr>
  <tr>
    <td>Event Sink</td>
    <td>Indicates that a specific event is received.</td>
  </tr>
  <tr>
    <td>Attribute</td>
    <td>Indicates an attribute possessed by the component. It has the same meaning as an attribute of a normal CORBA object.</td>
  </tr>
</table>


### Keywords Added for CIDL 
- component
- consumes
- emits
- eventtype
- finder
- getraises
- home
- import 
- multiple
- primarykey
- provides
- publishes
- setraises
- typeid
- typeprefix
- uses


### XML Files for Deployment and Configuration
<table class="table-alt">
  <tr>
    <th>Descriptor</th>
    <th>Extension</th>
  </tr>
  <tr>
    <td>Component Package Descriptor:</td>
    <td>.cpd</td>
  </tr>
  <tr>
    <td>Component Implementation Descriptor:</td>
    <td>.cid</td>
  </tr>
  <tr>
    <td>Implementation Artifact Descriptor:</td>
    <td>.iad</td>
  </tr>
  <tr>
    <td>Component Interface Descriptor (CORBA Component Descriptor):</td>
    <td>.ccd</td>
  </tr>
  <tr>
    <td>Component Domain Descriptor</td>
    <td>.cdd</td>
  </tr>
  <tr>
    <td>Deployment Plan Descriptor (Component Deployment Plan):</td>
    <td>.cdp</td>
  </tr>
  <tr>
    <td>Top Level Package Descriptor</td>
    <td>package.pcd</td>
  </tr>
  <tr>
    <td>ZIP file containing all of above + binaries</td>
    <td>.cpk</td>
  </tr>
</table>


### Component Declaration 
CCM components are declared according to the following syntax using the component declarator based on extended IDL.

```
 component <component_name> [ : <base_name> ]
     [ supports <interface_name> [, <interface_name>] * ]
 {
      <attribute declaration> *;
      <port declaration> *;
 };  
```

The &lt;component_name&gt; following component describes the name of the component to be declared.
As an optional declaration, a component can inherit from one component ( &lt;base_name&gt; ).
Also, by using the support declarator, it can have several interfaces ( &lt;interface_name&gt; ) defined in IDL at the same time, and these are called supported interfaces.
In the body of the component, component attributes ( &lt;attribute declaration&gt; ) and Ports ( &lt;port declaration&gt; ) can be declared.

This declaration is equivalent to declaring it as an equivalent interface equivalent to IDL2 as follows.

```
 interface <component_name>
     : Components::CCMObject, [<base_name>, <interface_name>, <interface_name>] * ]
 {
 };  
```


Therefore, &lt;base_name&gt; is distinguished as a component name and &lt;interface_name&gt; as an interface name, but in the equivalent interface, all of these become interfaces and are reduced to inheritance from these interfaces.

For example, a HelloWorld component with a Hello interface can be declared as follows. 




### References 
1. [Introduction to the CORBA Component Model (Part 1)](http://www.ogis-ri.co.jp/otc/hiroba/technical/CCM/step1/index.html)
1. [Introduction to the CORBA Component Model (Part 2)](http://www.ogis-ri.co.jp/otc/hiroba/technical/CCM/step2/index.html)
1. ["CORBA Component Model Tutorial" OMG Document ccm/02-04-01](http://www.omg.org/cgi-bin/doc?ccm/2002-04-01)
<!-- + [[Lightweight CORBA Component Model ptc/04-06-10>http://www.omg.org/docs/ptc/04-06-10.pdf]](リンク切れ) -->

