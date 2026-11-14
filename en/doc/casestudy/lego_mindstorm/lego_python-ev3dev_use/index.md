---
layout: page
title: using python-ev3dev
---

<!-- Title: Using python-ev3dev -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * Using python-ev3dev -->
#contents

## Accessing EV3 Devices with ev3dev-lang

ev3dev-lang is a library for accessing EV3 motors and sensors. It can be used from the following four programming languages:

- C++
- Python
- JavaScript
- Lua

This section introduces examples of accessing EV3 devices using Python and C++.

## Installing python-ev3dev

Install the Python version (Python bindings) of ev3dev-lang directly on the EV3 (not in the cross-development environment).

By entering the following commands, python-ev3dev will be installed on the system and become available from Python.

```
 # cd ~
 # mkdir work
 # cd work
 # apt-get install libboost-python1.55.0 python-setuptools python-pil
 # wget https://github.com/rhempel/ev3dev-lang-python/archive/0.6.0.zip
 # unzip 0.6.0.zip
 # cd ev3dev-lang-python-0.6.0/
 # python setup.py install
```

<!-- # easy_install -U python-ev3dev -->

## Accessing Devices from python-ev3dev

Let's try rotating a motor using python-ev3dev.

First, move to an appropriate directory (running in the directory used to install python-ev3dev will cause an error), and start Python in interactive mode.

```
 # cd
 # python
 Python 2.7.9 (default, Mar  1 2015, 13:52:09)
 [GCC 4.9.2] on linux2
 Type "help", "copyright", "credits" or "license" for more information.
 >>> import ev3dev.ev3 as ev3     (Import the ev3dev module)
 >>> m = ev3.LargeMotor()         (Instantiate a motor object)
 >>> m.connected                  (Check whether the motor is connected)
 True
 >>> m.run_forever(duty_cycle_sp=50)  (Rotate the motor continuously at 50% duty cycle)
 >>> m.stop()                         (Stop the motor)
```

There are three motor stop modes: `'brake'`, `'coast'`, and `'hold'`.

The default mode is `'coast'`, so when `m.stop()` is executed, the motor may continue moving slightly due to inertia.

To make the motor stop immediately, change the mode to `'hold'`.

<!-- >>> m.set(stop_command='hold') -->

```
 >>> m.set_attr_string(None, "stop_command", ev3.Motor.STOP_COMMAND_HOLD)
 >>> m.get_attr_string(None, "stop_command")[1]
 >>> m.run_forever(duty_cycle_sp=50)
 >>> m.stop()
```

As shown above, motors can be controlled relatively easily from Python.

Next, let's use a sensor.

Connect an ultrasonic sensor to Port 2.

While still in Python interactive mode, enter the following commands.

The `for` loop continuously displays the sensor value (in centimeters) for 100 seconds.

Press `Ctrl+C` to exit the loop at any time.

<!-- >>> s = ev3dev.ultrasonic_sensor(ev3dev.INPUT_2) -->

```
 >>> s = ev3.UltrasonicSensor()
 >>> s.distance_centimeters()
 118
 >>> import time
 >>> for i in range(0,100):
 ...     print s.distance_centimeters()
 ...     time.sleep(1)
 ..
 118
 114
 ：(omitted)
 2382
 2366
 326
 76
 ^CTraceback (most recent call last):
   File "<stdin>", line 3, in <module>
 KeyboardInterrupt
 >>>
```

## Learning About python-ev3dev

Tutorials and reference manuals for the various classes and functions available in python-ev3dev can be found on the following page:

- [Python language bindings for ev3dev](http://ddemidov.github.io/ev3dev-lang-python/)

In Python, you can call the **dir()** function on a module or object to view a list of available variables and functions (although `dir()` alone does not distinguish between variables and functions).

```
 >>> dir(ev3)
 ['Button', 'ButtonBase', 'ButtonEVIO', 'ColorSensor', 'DcMotor', 'Device', 'FbMem',
 'FirgelliL12100Motor', 'FirgelliL1250Motor', 'GyroSensor', 'I2cSensor', 'INPUT_1', 'INPUT_2',
 'INPUT_3', 'INPUT_4', 'INPUT_AUTO', 'Image', 'ImageDraw', 'InfraredSensor', 'LargeMotor',
 'Led', 'Leds', 'LegoPort', 'LightSensor', 'MediumMotor', 'Motor', 'NxtMotor', 'OUTPUT_A',
 'OUTPUT_AUTO', 'OUTPUT_B', 'OUTPUT_C', 'OUTPUT_D', 'Popen', 'PowerSupply', 'RemoteControl',
 'Screen', 'Sensor', 'ServoMotor', 'Sound', 'SoundSensor', 'TouchSensor', 'UltrasonicSensor',
 '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 'abspath',
 'array', 'ctypes', 'fcntl', 'fnmatch', 'list_device_names', 'list_devices', 'list_motors',
 'mmap', 'numbers', 'os', 'pack', 're', 'stat', 'unpack']
 >>>
```

For example, the `ev3dev.ev3` module contains something called `Sound`.

There also appears to be a function named `Sound()`, so let's create an instance of it.

As shown below, it does not require any arguments.

<!-- >>> s = ev3dev.sound() -->

```
 >>> s = ev3.Sound()
 >>> dir(s)
 ['__doc__', '__module__', 'beep', 'play', 'speak', 'tone']
```

Running **dir(s)** on the generated object **s** reveals the functions that can likely be called on that object.

Let's try calling `speak()`.

```
 >>> s.speak("Hello RT-Middleware World")
```

The EV3 should speak the phrase.

In practice, some functions cannot be used without knowing what arguments they require and what data types must be passed. However, this method provides a quick way to understand the general usage of a module or object.

For detailed information about function arguments and usage, please refer to the reference manual.

