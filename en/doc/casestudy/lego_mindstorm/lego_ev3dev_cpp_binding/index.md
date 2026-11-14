---
layout: page
title: using ev3 device c++ bindings
---

<!-- Title: Using EV3 Device C++ Bindings -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * Using cpp-ev3dev -->
#contents

## Using ev3dev-lang

ev3dev-lang includes binding libraries for EV3 devices in C++, Python, Lua, and other languages.

The following sections explain how to install and use the ev3dev bindings available for C++.

## Obtaining ev3dev-lang

The following operations are performed in the cross-development environment. It is assumed that the cross-development environment has already been set up as described above.

First, clone ev3dev-lang from GitHub. Choose an appropriate location within the cross-development environment (in this example, under `/home/openrtm/work`).

```

$ cd ev3-ev3dev-work/home/
$ mkdir -p openrtm/work
$ cd openrtm/work
$ git clone https://github.com/ddemidov/ev3dev-lang-cpp
Cloning into 'ev3dev-lang-cpp'...
remote: Counting objects: 1733, done.
remote: Total 1733 (delta 0), reused 0 (delta 0), pack-reused 1733
Receiving objects: 100% (1733/1733), 510.41 KiB | 310.00 KiB/s, done.
Resolving deltas: 100% (1150/1150), done.
Checking connectivity... done.
$ ls
ev3dev-lang-cpp
$ cd  ev3dev-lang-cpp
$ git checkout c0829011bf668bb77e55049a7f2f396b0b452f41

```

## Building ev3dev-lang

Next, compile the library. First, enter the work directory and start brickstrap in cross-development mode.

```

$ cd ~/work
$ brickstrap -b ev3-ev3dev-jessie -d ev3-ev3dev-work shell

```

Move to the directory cloned from GitHub and run `make`.

```

# cd /home/openrtm/work/ev3dev-lang-cpp/

# mkdir build

# cd build

# cmake .. -DEV3DEV_PLATFORM=EV3

# make

```

When compilation completes, a static library (`libev3dev.a`) is generated under the `build` directory, and several sample applications are generated under the `demos` directory.

## Sample Programs

The sample programs are described below.

The sample programs that can be used with the standard EV3 set are `button-test`, `ev3dev-lang-demo`, and `ev3dev-lang-test`. The `drive-test` and `remote_control-test` programs require an IR sensor and an IR beacon.

<table class="table-alt">
  <tr>
    <td>button-test</td>
    <td>A sample program that displays the ON/OFF status of the buttons (directional pad, center button, and cancel button) on the EV3 Intelligent Brick.</td>
  </tr>
  <tr>
    <td>drive-test</td>
    <td>Mode 1: Uses an IR sensor as a distance sensor and repeatedly drives forward when no obstacle is detected and turns when an obstacle is present. Mode 2: Infrared remote-control mode using an IR beacon. (The standard EV3 set does not include an IR sensor or IR beacon.)</td>
  </tr>
  <tr>
    <td>ev3dev-lang-demo</td>
    <td>A menu-driven demonstration program that provides access to various functions of sensors, motors, LEDs, buttons, sound, battery status, LCD, and other devices.</td>
  </tr>
  <tr>
    <td>ev3dev-lang-test</td>
    <td>A test program for libev3dev. It accesses sensors, motors, LEDs, and other devices to verify the functionality of libev3dev.</td>
  </tr>
  <tr>
    <td>remote_control-test</td>
    <td>A demonstration program for remote control using an IR sensor and an IR beacon.</td>
  </tr>
</table>

## Copying Sample Programs to the EV3

To run the sample programs on an actual EV3, copy them to the EV3.

Make sure that ev3dev is running on the EV3 and that it is connected to the network.

From the cross-development environment, copy the files as follows:

```

# cd demos ← Move to ev3dev-lang-cpp/demos

# scp * ev3dev.local:/tmp/ ← Copy files to /tmp/ on ev3dev.local (EV3)

```

## Running the Sample Programs

Log in to `ev3dev.local` from a terminal and execute the sample program.

```

# ssh ev3dev.local

login: root
password: r00tme

# cd /tmp

# ./ev3dev-lang-demo

*** main menu ***

(s)ensors
(m)otors
(l)eds
(b)uttons
s(o)und
b(a)ttery
l(c)d
(q)uit

Choice:

```

## Building Your Own Programs

When building your own programs, you must include `ev3dev.h` and link against `libev3dev.a`.

The following is an example `CMakeLists.txt`.

```

cmake_minimum_required(VERSION 2.8)

set(ev3dev_dir /home/ev3dev-lang-cpp)
set(ev3dev_lib ${ev3dev_dir}/build/libev3dev.a)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11")

project( testEV3 )
add_executable(testEV3 main.cpp)
include_directories(${ev3dev_dir})
target_link_libraries(testEV3 ${ev3dev_lib} pthread)

```
