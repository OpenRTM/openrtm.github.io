---
layout: page
title: rtctree module
---

<!-- Title: rtctreeモジュール -->
#contents

rtctree is a library for managing RT Components in Python.

## Overview 

rtctree is a Python library for managing RT Components with a simple API. Developers can manage RT Component systems from other programs without knowing the CORBA API.
It is possible to activate and deactivate components, and to connect components to each other.

This software is developed by the National Institute of Advanced Industrial Science and Technology with support from NEDO (New Energy and Industrial Technology Development Organization) under the Next-Generation Robot Intelligence Technology Development Project.

## Requirements

- ominorb-py, omniidl, and the Python module for omniidl are required.
- Python 2.6 or later is required because features that do not exist in Python 2.5 or earlier are used.
- If you are using Ubuntu 9.04, you need to manually install Python 2.6. Therefore, Ubuntu 9.04 or later is recommended.

## Installation

Several installation methods are available.

- Download from the repository (see [Repository](#repo) below) or from the source archive, extract it in an appropriate directory, and install it:
  1. Extract the source.
```
 $ cd /home/blurgle/src/
 $ tar -xvzf rtctree-2.0.0.tar.gz
```
  1. Run setup.py.
```
 $ python setup.py install
```
  1. Set environment variables as needed. These are set by default, but if they are not set, you need to set them yourself. On Windows, make sure that the Python site-packages directory is set in the **PYTHONPATH** environment variable, and that the Python script directory is set in the **PATH** environment variable. Normally, these are **C:\\Python26\\Lib\\site-packages\\** and **C:\\Python26\\Scripts\\** (if Python is installed in **C:\\Python26\\**).

- On Windows, using the installer is recommended. Using setup.py makes the result easier to configure. However, depending on the environment, additional environment variable settings may be required.


## Environment Variables

The following environment variables are used.

<table class="table-alt">
  <tr>
    <td><strong>RTCTREE_ORB_ARGS</strong></td>
    <td>A semicolon-separated list of arguments given when creating the ORB. This does not need to be set.</td>
  </tr>
  <tr>
    <td><strong>RTCTREE_NAMESERVERS</strong></td>
    <td>A semicolon-separated list of name server addresses for the RTC tree. The servers written in this variable are added to the tree. This does not need to be set.</td>
  </tr>
</table>

Normally, RTCTREE_ORB_ARGS does not need to be set. Setting RTCTREE_NAMESERVERS makes using rtctree more convenient. For example, in a Bash shell:

```
 $ export RTCTREE_NAMESERVERS=localhost;192.168.0.1:65346;example.com
```

## RTC Tree

The main part of the library is the RTC tree.
```
 import rtctree.tree
 tree = rtctree.tree.RTCTree()
```
This is a file-system-like tree created by searching name servers to obtain naming contexts, components, and managers. It can be handled exactly like a normal file system. The tree represents naming contexts, managers, and components registered with all known name servers in a tree structure.

```
 \  
 |-+localhost
 | |-+naming_context
 | | |--ConsoleIn0.rtc</td>
 | | |--ConsoleOut0.rtc</td>
 | |
 | |--another_naming_context</td>
 | |--Sensor0.rtc</td>
 | 
 |-+192.168.0.5</td>
   |--Motor0.rtc</td>
   |--Controller0.rtc</td>
```

Each directory in the tree is either a normal naming context or the root context of a name server. The root context of a name server is represented by the **NameServer** class. A naming context is represented by the **'Directory'** class, and a manager is represented by the **Manager** class.

Name servers are treated as directories from the root directory. Under them are files and subdirectories. Subdirectories represent naming contexts and managers under the root context.

Files are components and managers. Components are represented by the Component class.

A component object stores various information about the component it represents. You can activate and deactivate components, manage component ports, connect ports, and set configuration settings.

Managers can create new component instances and delete components.

All nodes in the tree also store references to the CORBA objects represented by those nodes. By accessing these objects, you can call IDL methods. Even if there is a function that is currently not available in rtctree, you can use this CORBA object to call IDL methods directly.


### Building the Tree

The arguments of the tree factory function (**create_tree()**) specify the name servers to be parsed in order to build the tree. For details, refer to the documentation for that function. In general, you can build a tree by passing a list of name server addresses or a list of paths. The environment variable **RTCTREE_NAMESERVERS** is also checked.

### Paths 

Nodes in the tree are specified by paths. A path is a list of strings. Each level to the right is one level deeper than the one to the left. An absolute path is required to specify a tree object. If the path exists under a node, a relative path from that node can also be specified.

These path strings are similar to file system path specifications. The root of the tree is indicated by `/` (or `\` on Windows). The first level is the name server address. The levels below it are components, managers, and naming contexts (shown as directories). The function **parse_path** converts a string path into a path for the RTC tree.

For example, the following path:
```
 /localhost/naming_context/ConsoleIn0.rtc
```
indicates a component named **ConsoleIn0.rtc** registered under **naming_context** of the name server running on **localhost**. When you want to obtain the object of that component from the tree, you need to convert the path into a Python list using **parse_path**.
```
 ['/', 'localhost', 'naming_context', 'ConsoleIn0.rtc']
```

### Helper Functions

The following are helper functions for the RTCTree class and various node classes. This does not show all APIs. Refer to the API documentation written with Doxygen. For examples, refer to the rtcshell source.

<table class="table-alt">
  <tr>
    <td><strong>RTCTree.has_path</strong></td>
    <td>Checks whether a path exists in the tree. This function is useful for checking the existence of a component.</td>
  </tr>
  <tr>
    <td><strong>RTCTree.get_node</strong></td>
    <td>Gets a node from the tree. Use this function to obtain a component, directory, or other object.</td>
  </tr>
  <tr>
    <td><strong>RTCTree.is_component</strong></td>
    <td>Checks whether the path points to a component. Node classes have a property with the same function named <strong>is_component</strong>. There are also functions and properties named <strong>is_directory</strong>, <strong>is_manager</strong>, and <strong>is_nameserver</strong>.</td>
  </tr>
  <tr>
    <td><strong>RTCTree.iterate()</strong></td>
    <td>Executes the same function on all nodes in the tree. All results are returned as a list. For an example, refer to <strong>rtls</strong> in rtcshell.</td>
  </tr>
</table>

<br>
<table class="table-alt">
  <tr>
    <td><strong>Node.children</strong></td>
    <td>All child nodes of the node. For example, it can be used to obtain a list of components under a directory.</td>
  </tr>
  <tr>
    <td><strong>Node.full_path</strong></td>
    <td>The path from the root of the tree to this node.</td>
  </tr>
  <tr>
    <td><strong>Node.name</strong></td>
    <td>The name of the node. For example, the name of a directory.</td>
  </tr>
  <tr>
    <td><strong>Node.parent_name</strong></td>
    <td>The name of the parent of the node.</td>
  </tr>
  <tr>
    <td><strong>Node.root</strong></td>
    <td>The root node of the tree for this node. The returned object can perform almost all functions of the tree.</td>
  </tr>
</table>

<br>

<table class="table-alt">
  <tr>
    <td><strong>Component.activate_in_ec()</strong></td>
    <td>Activates the component. Usually, ec_index can be 0.</td>
  </tr>
  <tr>
    <td><strong>Component.deactivate_in_ec()</strong></td>
    <td>Deactivates the component.</td>
  </tr>
  <tr>
    <td><strong>Component.reset_in_ec()</strong></td>
    <td>Resets the component.</td>
  </tr>
  <tr>
    <td><strong>Component.state_in_ec()</strong></td>
    <td>Gets the state of the component in a certain execution context.</td>
  </tr>
  <tr>
    <td><strong>Component.alive</strong></td>
    <td>Checks whether the component is alive.</td>
  </tr>
  <tr>
    <td><strong>Component.owned_ecs</strong></td>
    <td>A list of execution contexts owned by the component.</td>
  </tr>
  <tr>
    <td><strong>Component.participating_ecs</strong></td>
    <td>A list of execution contexts used by the component.</td>
  </tr>
  <tr>
    <td><strong>Component.state</strong></td>
    <td>The state of the component.</td>
  </tr>
  <tr>
    <td><strong>Component.state_string</strong></td>
    <td>The state of the component as a string.</td>
  </tr>
  <tr>
    <td><strong>Component.disconnect_all()</strong></td>
    <td>Disconnects all connections of all ports of the component.</td>
  </tr>
  <tr>
    <td><strong>Component.get_port_by_name()</strong></td>
    <td>Finds a component port by name.</td>
  </tr>
  <tr>
    <td><strong>Component.ports</strong></td>
    <td>A list of component ports. It includes lists of input ports, output ports, and service ports, and can also obtain a list of currently connected ports.</td>
  </tr>
  <tr>
    <td><strong>Component.object</strong></td>
    <td>The CORBA <strong>LightweightRTObject</strong> object of the component.</td>
  </tr>
  <tr>
    <td><strong>Component.activate_conf_set</strong></td>
    <td>Activates a configuration set.</td>
  </tr>
  <tr>
    <td><strong>Component.set_conf_set_value</strong></td>
    <td>Sets a variable in a configuration set.</td>
  </tr>
  <tr>
    <td><strong>Component.active_conf_set</strong></td>
    <td>The currently active configuration set.</td>
  </tr>
  <tr>
    <td><strong>Component.active_conf_set_name</strong></td>
    <td>The name of the currently active configuration set.</td>
  </tr>
  <tr>
    <td><strong>Component.conf_sets</strong></td>
    <td>A list of configuration sets.</td>
  </tr>
</table>

<br>
<table class="table-alt">
  <tr>
    <td><strong>Port.connect()</strong></td>
    <td>Connects this port to another port.</td>
  </tr>
  <tr>
    <td><strong>Port.disconnect_all()</strong></td>
    <td>Disconnects all connections of this port.</td>
  </tr>
  <tr>
    <td><strong>Port.get_connection_by_dest()</strong></td>
    <td>Finds a connection of this port by another port.</td>
  </tr>
  <tr>
    <td><strong>Port.get_connection_by_name()</strong></td>
    <td>Finds a connection of this port by name.</td>
  </tr>
  <tr>
    <td><strong>Port.connections</strong></td>
    <td>A list of connections of this port.</td>
  </tr>
  <tr>
    <td><strong>Port.is_connected</strong></td>
    <td>Checks whether this port is connected.</td>
  </tr>
  <tr>
    <td><strong>Port.name</strong></td>
    <td>The name of the port.</td>
  </tr>
  <tr>
    <td><strong>Port.objecti</strong></td>
    <td>The CORBA <strong>PortService</strong> object of this port.</td>
  </tr>
  <tr>
    <td><strong>Port.name</strong></td>
    <td>The owner of the port (usually a <strong>Component</strong> object).</td>
  </tr>
  <tr>
    <td><strong>Port.porttype</strong></td>
    <td>The type of the port (<strong>DataInPort</strong>, <strong>DataOutPort</strong>, or <strong>CorbaPort</strong>).</td>
  </tr>
</table>

<table class="table-alt">
  <tr>
    <td><strong>Connection.disconnect()</strong></td>
    <td>Disconnects this connection.</td>
  </tr>
  <tr>
    <td><strong>Connection.ports</strong></td>
    <td>A list of the source and destination ports of this connection.</td>
  </tr>
</table>
<br>
<table class="table-alt">
  <tr>
    <td><strong>ConfigurationSet.has_param()</strong></td>
    <td>Checks whether this set has a variable.</td>
  </tr>
  <tr>
    <td><strong>ConfigurationSet.set_param()</strong></td>
    <td>Sets a variable in this set.</td>
  </tr>
</table>
<br>
<table class="table-alt">
  <tr>
    <td><strong>ExecutionContext.activate_component()</strong></td>
    <td>Activates a component in this execution context.</td>
  </tr>
  <tr>
    <td><strong>ExecutionContext.deactivate_component()</strong></td>
    <td>Deactivates a component in this execution context.</td>
  </tr>
  <tr>
    <td><strong>ExecutionContext.reset_component()</strong></td>
    <td>Resets a component in this execution context.</td>
  </tr>
  <tr>
    <td><strong>ExecutionContext.get_component_state()</strong></td>
    <td>Gets the state of a component in this execution context.</td>
  </tr>
  <tr>
    <td><strong>ExecutionContext.running</strong></td>
    <td>Checks whether this execution context is running.</td>
  </tr>
</table>
<br>
<table class="table-alt">
  <tr>
    <td><strong>Manager.create_component()</strong></td>
    <td>Creates a new component instance.</td>
  </tr>
  <tr>
    <td><strong>Manager.delete_component()</strong></td>
    <td>Deletes a component instance.</td>
  </tr>
</table>

<br>
<table class="table-alt">
  <tr>
    <td><strong>dict_to_nvlist()</strong></td>
    <td>Converts a Python dict to a CORBA namevalue list.</td>
  </tr>
  <tr>
    <td><strong>nvlist_to_dict()</strong></td>
    <td>Converts a CORBA namevalue list to a Python dict.</td>
  </tr>
</table>

## API Style

rtctree follows the standard Python style. Refer to [PEP8](http://www.python.org/dev/peps/pep-0008/).

The most important point is that private internal API functions begin with an underscore ("_"). Functions that begin with an underscore should not be accessed from outside the class. If they are used, undefined behavior may occur. Use only functions that do not begin with an underscore and that have docstrings.

&aname(repo);
<a name="repo">
## Repository

The latest source is available in the [Git repository on github](http://github.com/gbiggs/rtctree). You can download it by clicking "Download source". You can also use "git clone". If you want to send patches, this method is recommended.

```
 $ git clone git://github.com/gbiggs/rtctree.git
```

## More Detailed Documentation and Samples

For more detailed documentation, refer to the documentation written with Doxygen.

For samples, refer to the [rtshell source](https://github.com/OpenRTM/rtshell). These show almost all of the ways to do with rtctree what can be done with RTSystemEditor.

## Changelog 

### 3.0
- Changed exceptions to warnings.
- Improved handling of zombies.
- Zombie detection manager.
- Added an API to obtain composite component information.
- Added an API to obtain connections by ID from ports.
- Added an API to pass an ORB.
- Added a path formatter.
- Made exceptions display in a more readable way.
- Performance improvement
- Added a function to limit the paths to be parsed.
- Added zombie nodes.
- Added an API to terminate components.
- Removed the create_rtctree() function. Use RTCTree().
- Added the remove_node() API.
- Changed node.full_path to a list and added node.full_path_str.

### 2.0

- Made it parse more information about execution contexts.
- Made it possible to provide an ORB object from outside.
- Made the reparse_connections() function public.
- Added a new API to obtain the ORB used by a node.
- Added a new API to unbind names from contexts.
- Made it possible to access more CORBA objects.
- Improved zombie recognition efficiency.
- Fixed how unknown CORBA objects are handled.
- Fixed how ports with unknown owners are handled.
- Added a lock to make rtctree objects thread-safe.
- Added an API to reload tree objects.
- Fixed the <u>init</u> function for proper inheritance handling.
- Added a new API to obtain the state of a component in a specific EC.
- Added a new API to update the state of a component in a specific EC.

