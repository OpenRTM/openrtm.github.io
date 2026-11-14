---
layout: page
title: using ev3 devices
---

<!-- -*- pukiwiki-edit -*- -->
<!-- * Using EV3 Devices -->
#contents

## LEGO Mindstorms Sensors and Motors

The LEGO Mindstorms EV3 comes standard with the following motors and sensors:

- Gyro Sensor ×1
- Color Sensor ×1
- Touch Sensor ×2
- Ultrasonic Distance Sensor ×1
- Motor (L) ×2
- Motor (M) ×1

The sensors provide various types of data. The touch sensor can provide ON/OFF values, the ultrasonic and gyro sensors can output continuous values, and the color sensor can recognize several colors.

There are two types of motors (L and M). Both support PWM (torque) control, speed control, and position control. The control gains and related parameters can also be adjusted.

The specifications of the EV3 sensors and motors are shown below.

<table class="table-alt">
  <tr>
    <td><strong>Gyro Sensor</strong>
    </td>
    <td>Angle Mode: Accuracy +/- 3°<br> Angular Velocity Mode: Up to 440 deg/sec <br> Sampling Rate: 1,000 Hz</td>
  </tr>
  <tr>
    <td><strong>Color Sensor</strong></td>
    <td>Measurements: Reflected red light, ambient light intensity, color <br> Number of detectable colors: 8 (None, Black, Blue, Green, Yellow, Red, White, Brown)<br> Sampling Rate: 1,000 Hz <br> Detection Distance: Approximately 1 mm to 18 mm (measured by Afrel)</td>
  </tr>
  <tr>
    <td><strong>Touch Sensor</strong></td>
    <td>On (1), Off (0) <br> Switch Travel Distance: Approximately 4 mm</td>
  </tr>
  <tr>
    <td><strong>Ultrasonic Sensor</strong></td>
    <td>Distance Measurement Range: 3 cm to 250 cm <br> Measurement Accuracy: +/- 1 cm <br> Front Indicator Light: On = ultrasonic transmission, Flashing = ultrasonic observation</td>
  </tr>
  </tr>
  <tr>
  </tr>
  <tr>
  </tr>
  <tr>
    <td><strong>EV3 Large Motor (L)</strong></td>
    <td>Feedback Resolution: 1° <br> Rotation Speed: 160–170 RPM <br> Rated Torque: 0.21 N·m (30 oz·in) <br> Stall Torque: 0.42 N·m (60 oz·in) <br> Weight: 76 g</td>
  </tr>
  <tr>
    <td><strong>EV3 Medium Motor (M)</strong></td>
    <td>Feedback Resolution: 1° <br> Rotation Speed: 240–250 RPM <br> Rated Torque: 0.08 N·m (11 oz·in) <br> Stall Torque: 0.12 N·m (17 oz·in) <br> Weight: 36 g</td>
  </tr>
</table>

## Accessing Devices via sysfs

To access these devices from ev3dev, a mechanism called **sysfs** is used.

sysfs is a virtual file system located under `/sys`. By reading from and writing to files within this file system, it is possible to control motors and access sensor data.

Detailed information on accessing devices through sysfs can be found in the following ev3dev documentation.

- Accessing Various Devices: [http://www.ev3dev.org/docs/drivers/](http://www.ev3dev.org/docs/drivers/)
  - Motor Reference: [http://www.ev3dev.org/docs/drivers/tacho-motor-class/](http://www.ev3dev.org/docs/drivers/tacho-motor-class/)
    - Motor Control Tutorial: [http://www.ev3dev.org/docs/tutorials/tacho-motors/](http://www.ev3dev.org/docs/tutorials/tacho-motors/)
  - Sensor Reference: [http://www.ev3dev.org/docs/drivers/lego-sensor-class/](http://www.ev3dev.org/docs/drivers/lego-sensor-class/)

Specifically, devices can be accessed as shown below.

### Motor Control Example

To make a motor rotate continuously, connect a motor (either L or M) to Port A and enter the following commands from the command line.

```bash
 # echo 50 > /sys/class/tacho-motor/motor0/duty_cycle_sp
 # echo run-forever > /sys/class/tacho-motor/motor0/command
````

To display the current speed, enter the following command. Press Ctrl+C to stop displaying it.

```bash
 # while true; do echo -en "\033[0G$(cat /sys/class/tacho-motor/motor0/speed)   "; done
```

To stop the motor, enter the following command.

```bash
 # echo stop > /sys/class/tacho-motor/motor0/command
```

### Sensor Example

Sensors can be accessed in the same way.

Connect the color sensor to Port 1. Place a red object approximately 1 cm in front of the sensor.

Enter the following commands to display **5**.

```bash
 # echo "COL-COLOR" > /sys/class/lego-sensor/sensor1/mode
 # cat /sys/class/lego-sensor/sensor1/value1
 5
```

The color sensor supports several operating modes. In the example above, color detection mode is used.

In this mode, the following eight colors can be recognized (where 0 indicates that no color is detected).

<table class="table-alt">
  <tr>
    <td>Color</td>
    <td>None</td>
    <td>Black</td>
    <td>Blue</td>
    <td>Green</td>
    <td>Yellow</td>
    <td>Red</td>
    <td>White</td>
    <td>Brown</td>
  </tr>
  <tr>
    <td>Number</td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
  </tr>
</table>

Although devices can be accessed from the command line as shown above, performing these operations directly from a program requires a considerable amount of cumbersome processing.

To simplify device access from programs, dedicated access libraries are available and should be used.

