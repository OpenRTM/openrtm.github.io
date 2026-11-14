---
layout: page
title: "sdo service section"
---
<!-- Title: SDO サービス編 -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * SDO サービス編 -->

#contents

In addition to service ports, service interfaces called SDO services can be added to RTCs.

SDO stands for Super Distributed Object, and it is one of the distributed component standards standardized by OMG.
RTObject, which is the actual entity of an RTC, actually inherits from an SDO object, so an RTC can be said to be a kind of SDO object.
SDO defines the basic interfaces of components.
A service interface owned by an SDO component is called an SDOService interface, and it inherits the interface definition.
In fact, RTC ports and execution contexts also inherit SDOService and are a type of SDO service.

What is the difference between a service port and an SDO service?

Both provide services (Provided) to the outside of an RTC or use external services (Required).
The major difference is that service ports provide interfaces for accessing details of the internal logic of an RTC (the core logic implemented by the RTC developer), or for accessing external services from the core logic, whereas SDO services provide interfaces for accessing details of the functionality of the RTC itself, that is, the component that contains the core logic (or for accessing external services from the component's functionality).

- **Service port**: A service for (or used by) the core logic inside an RTC
- **SDO service**: A service for (or used by) the functionality of the RTC as a component

Specific uses of SDO services are as follows.

## Example of ComponentObserver

For example, OpenRTM has an extension function called ComponentObserver. This is a mechanism that allows external tools and similar applications to receive notifications without polling when some kind of state change occurs in the component (RTC) itself.

Tools and similar applications can receive notifications when there are changes in RTC states, profiles, EC states, state changes including port connection and disconnection, configuration changes, and so on.

It is possible to know these state changes externally by periodically calling (polling) functions such as the RTC's get_component_profile() and the EC's get_profile(). However, periodically calling many functions such as get_xxx() from multiple tools or external RTCs in order to know various changes in an RTC is inefficient, and in the worst case, detecting changes incurs a delay equal to the polling cycle.

If tools and similar applications give callback objects to the RTC in advance, and the RTC side immediately calls functions of those objects only when changes occur, there is no delay, and functions are called only when changes occur, making this efficient.

Also, such functionality is unrelated to the RTC core logic and is a service function related to the RTC framework itself. Therefore, it is appropriate to implement such service interfaces as SDO services.

In the case of ComponentObserver, the RTC side realizes this functionality by calling functions of a service object provided by the tool. In other words, the service implementation exists on the tool side, and the RTC side uses the tool's service. Therefore, in this case, the RTC side implements an SDO service consumer (Required interface).

Conversely, there may also be cases where the RTC side provides a service and tools or other external entities use that service. In this case, an SDO service provider (Provided interface) is implemented.


## Implementation Method

Both SDO service providers and SDO service consumers are normally provided in the form of shared objects. They are loaded from the RTC process by a prescribed method, registered with a factory, instantiated, and then service provision or use begins.

For one RTC, one SDO service of each type is instantiated and associated with it. Services predefined on a per-process basis are instantiated.

The SDO service-related options that can be set in rtc.conf are as follows.

<table class="table-alt">
  <tr>
    <th colspan="2">Settings Related to SDO Service Providers</th>
  </tr>
  <tr>
    <td>sdo.service.provider.available_services</td>
    <td>Read-only. List of available services</td>
  </tr>
  <tr>
    <td>sdo.service.provider.enabled_services</td>
    <td>Among the loaded SDO service providers, those to enable. Specify ALL to enable all.</td>
  </tr>
  <tr>
    <td>sdo.service.provider.providing_services</td>
    <td>Read-only. List of SDO services being used.</td>
  </tr>
  <tr>
    <th colspan="3">Settings Related to SDO Service Consumers</th>
  </tr>
  <tr>
    <td>sdo.service.consumer.available_services</td>
    <td>Read-only. List of available SDO service consumers.</td>
  </tr>
  <tr>
    <td>sdo.service.consumer.enabled_services</td>
    <td>Among the loaded SDO service consumers, those to enable. Specify ALL to enable all.</td>
  </tr>
</table>


From the next section, we explain how to implement providers and consumers on the RTC side for SDO services.

