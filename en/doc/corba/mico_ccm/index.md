---
layout: page
title: mico_ccm
---

<!-- Title: MICO_CCM -->
#contents

<!-- * [[MICO CCM]] -->

## ccmd (mico-ccmd) 
The CCM daemon included with MICO.
ccmd performs component installation and management of deployed components on a single host. Therefore, if you want to run components on multiple hosts, it must be executed on each host.
mico-ccmd implements the ComponentInstallation, AssemblyFactory, and ServerActivator interfaces (and services).

- ComponentInstallation
  - On the host where mico-ccmd is running, component implementations can be installed through the ComponentInstallation interface. Normally, components are installed using mico-ccmload.

- AssemblyFactory
  - Through AssemblyFactory, component assemblies can be started on demand.

- ServerActivator
  - Through the ServerActivator interface, component servers can be started on demand.

The deployment tool first communicates with mico-ccm, uploads the component implementation file, and starts the componentserver on that host.
(Does it create a process for each component?)
mico-ccmd is normally a daemon that runs persistently in the background and does nothing visibly.
If it receives a termination signal (SIGINT, Ctrl-C), it terminates all assemblies and component servers.
Finally, it deletes all installed component implementations and exits.


### Options
<table class="table-alt">
  <tr>
    <td>--root <pkgdir></td>
    <td>Path to the directory where installed component implementations are stored. If not specified, they are stored in the current directory.</td>
  </tr>
  <tr>
    <td>--ior <filename></td>
    <td>Specify the file name with this option if you want to save the IOR of mico-ccmd to a file. Use a hyphen to output to standard output.</td>
  </tr>
  <tr>
    <td>-v</td>
    <td>Verbose option. Outputs status messages such as component server start and stop to standard output.</td>
  </tr>
</table>

The standard options of the MICO ORB can also be used.
- With ORBIIOPAddr, it is possible to assign the ORB to a specific IP address (for example, -ORBIIOPAddr hoge.aist.go.jp::1234).
If the port is known, it is also possible to specify mico-ccmd with an object URL.
Since the object key of mico-ccmd is "MicoCCMD",
```
 corbaloc::<host>:<port>/MicoCCMD
```
you can specify the ccmd object with a URL like this.

## ccmload (mico-ccmload)

ccmload is a simple deployment tool that can deploy a single component.
ccmload communicates with the MicoCCM daemon, starts a new component server, and loads a new component.
Then it loads the home <home name> from the shared library <library file> into the container.
Optionally, the home can also be registered with the name server.
<home name> must be the fully qualified name of the component home to be deployed.
<library name> must be the name of the shared library file containing the implementation of <home name>.
ccmload does not upload the shared library of the implementation; the file name must be accessible by the MicoCCM daemon.

<br>
<table class="table-alt">
  <tr>
    <td>--ccmd <IOR></td>
    <td>Gives the object reference of the MicoCCM Daemon.</td>
  </tr>
  <tr>
    <td>--host <host>[:port]</td>
    <td>This option can be used to give the address and port of the MicoCCM daemon. If the port number is not specified, the default port is 1234.</td>
  </tr>
  <tr>
    <td>--ns <name></td>
    <td>Registers the deployed home with the name server under the specified name.</td>
  </tr>
  <tr>
    <td>--ior <filename></td>
    <td>Writes the object reference of the deployed home to the specified file. Use a hyphen to write to standard output.</td>
  </tr>
  <tr>
    <td>-v</td>
    <td>Verbose message output</td>
  </tr>
</table>

