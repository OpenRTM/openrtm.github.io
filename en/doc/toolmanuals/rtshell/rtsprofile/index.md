---
layout: page
title: rtsprofile module
---

init
<!-- Title: rtsprofileモジュール -->
#contents

rtsprofile is a library for using the RTSProfile specification in Python.

## Overview

rtsprofile is an interface library for the RT System Profile (RTSProfile) specification.
This specification describes a complete RT system, and makes it possible to restore and manage the system. Both XML and YAML can be used.

This software is developed by the National Institute of Advanced Industrial Science and Technology with support from NEDO (New Energy and Industrial Technology Development Organization) under the Next-Generation Robot Intelligence Technology Development Project.

## Requirements

- Python 2.6 or later is required because features that do not exist in Python 2.5 or earlier are used.
- If you are using Ubuntu 9.04, you need to manually install Python 2.6. Ubuntu 9.04 or later is recommended.

## Installation

Several installation methods are available.

- Download from the repository (see [Repository](#repo) below) or from the source archive, extract it in an appropriate directory, and install it:

  1. Extract the source.
```
 $ cd /home/blurgle/src/
 $ tar -xvzf rtsprofile-2.0.0-tar.gz
```
  1. Run setup.py.
```
 $ python setup.py install
```
  1. Set environment variables as needed. These are set by default, but if they are not set, you need to set them yourself.
On Windows, make sure that the Python site-packages directory is set in the **PYTHONPATH** environment variable, and that the Python script directory is set in the **PATH** environment variable.
Normally, these are **C:\\Python26\\Lib\\site-packages\\** and **C:\\Python26\\Scripts\\** (if Python is installed in **C:\\Python26\\**).

- On Windows, using the installer is recommended. Using setup.py makes the result easier to configure. However, depending on the environment, additional environment variable settings may be required.

## Usage

The library provides the **RtsProfle** class. After creating an instance of this class, passing an RTSProfile file creates a complete RT System Profile.
Alternatively, you can manually create an RT System Profile for an existing RT system, pass a file name, and save the RTSProfile to that file.

Class information is accessed using Python properties. They are not methods.

For details of the API, refer to the documentation generated with Doxygen.

## Running Tests

The source includes sample files and test scripts. They can be executed with commands such as the following.

```
 $ python test/test.py ./test/rtsystem.xml
 $ python test/test.py ./test/rtsystem.yaml
```

Depending on the value of PYTHONPATH, the tests may use the installed rtsprofile.

## API naming conventions

rtsprofile follows the standard Python style. Refer to [PEP8](http://www.python.org/dev/peps/pep-0008/).

The most important point is that private internal API functions begin with an underscore ("_"). Functions that begin with an underscore should not be accessed from outside the class.
If they are used, undefined behavior may occur. Use only functions that do not begin with an underscore and that have docstrings.

## More Detailed Documentation and Samples

For more detailed documentation, refer to the documentation written with Doxygen.

For samples, refer to the [rtshell source](https://github.com/OpenRTM/rtshell).

&aname(repo);
<a name="repo">
## Repository 

The latest source is available in the [Git repository on github](http://github.com/gbiggs/rtsprofile). You can download it by clicking "Download source".
You can also use "git clone". If you want to send patches, this method is recommended.

```
 $ git clone git://github.com/gbiggs/rtsprofile.git
```

## Changelog
### 2.0

- Fixed the parsing of Message Sending information.
- Changed the data type of PrecedingCondition timeout to integer.
- Added support for YAML format.
- Added tests.
- Changed the default of Preceding Conditions to "SYNC".
- Bug fixes

