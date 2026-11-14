---
layout: page
title: operating ev3 devices
---

<!-- Title: Operating EV3 Devices -->
#contents

## Motors

### Speed Control

To control motor speed, you must write `"on"` to the following device file.

```

echo on > /sys/class/tacho-motor/motor0/speed_regulation

```

Speed control is disabled by default at startup because it is set to `off`.

When it is `off`, you can set the duty cycle using `duty_cycle_sp`.

Then write the target speed to the following file.

```

echo 50 > /sys/class/tacho-motor/motor0/speed_sp

```

The value specified here represents the number of counts per second. Therefore, convert angular velocity using the value obtained from the following device file.

*For Motor M and Motor L, the value returned by `count_per_rot` is 360, so conversion is not necessary.*

```

cat /sys/class/tacho-motor/motor0/count_per_rot

```

After that, enter the following command to start rotation.

```

echo run-forever > /sys/class/tacho-motor/motor0/command

```

To obtain the current angular velocity, use the following device file.

```

cat /sys/class/tacho-motor/motor0/speed

```

The above procedure using **ev3dev-lang-cpp** is as follows.

```

ev3dev::large_motor lm = ev3dev::large_motor();
lm.set_speed_regulation_enabled("on");
lm.set_speed_sp(50*lm.count_per_rot());
lm.run_forever();
std::cout << lm.speed()/lm.count_per_rot() << std::endl;

```

Using **ev3dev-lang-python**, it can be written as follows.

```

lm = ev3.LargeMotor()
lm.set_attr_string("speed_regulation", "on")
lm.speed_sp = 50*lm.count_per_rot
lm.run_forever()
print lm.speed/lm.count_per_rot

```

### Running for a Fixed Time

To run a motor for a specified amount of time, first set the duration using the following device file.

```

echo 2000 > /sys/class/tacho-motor/motor0/time_sp

```

Then start operation with the following command.

```

echo run-timed > /sys/class/tacho-motor/motor0/command

```

### Position Control

To perform position control, you must first set `duty_cycle_sp` (or `speed_sp` if `speed_regulation` is enabled).

```

echo 50 > /sys/class/tacho-motor/motor0/speed_sp

```

Next, set the target position using the following device file.

```

echo 100 > /sys/class/tacho-motor/motor1/position_sp

```

Since this position is also specified as a count value, convert it using `count_per_rot`.

Start operation with the following command.

```

echo run-to-abs-pos > /sys/class/tacho-motor/motor1/command

```

To specify an angle relative to the current position, use the following command.

```

echo run-to-rel-pos > /sys/class/tacho-motor/motor1/command

```

The current position can be obtained from the following device file.

```

cat /sys/class/tacho-motor/motor1/position

```

The above procedure using **ev3dev-lang-cpp** is as follows.

```

ev3dev::large_motor lm = ev3dev::large_motor();
lm.set_speed_regulation_enabled("on");
lm.set_speed_sp(50*lm.count_per_rot());
lm.set_position_sp(100*lm.count_per_rot());
lm.run_to_abs_pos(100*lm.count_per_rot());
#lm.run_to_rel_pos(100*lm.count_per_rot());

```

Using **ev3dev-lang-python**, it can be written as follows.

```

lm = ev3.LargeMotor()
lm.set_attr_string(None, "speed_regulation", "on")
lm.speed_sp = 50*lm.count_per_rot
lm.run_to_abs_pos()
#lm.run_to_rel_pos()

```

## Operating Sensors with C++ and Python

### Obtaining Reflected Light Intensity from the Color Sensor

- C++

```

ev3dev::color_sensor cs = ev3dev::color_sensor();
std::cout << cs.reflected_light_intensity() << std::endl;

```

- Python

```

cs = ev3.ColorSensor()
print cs.reflected_light_intensity()

```

### Obtaining the ON/OFF State of the Touch Sensor

- C++

```

ev3dev::touch_sensor ts = ev3dev::touch_sensor();
std::cout << ts.is_pressed() << std::endl;

```

- Python

```

cs = ev3.ColorSensor()
print cs.reflected_light_intensity()

```

### Obtaining the Angle from the Gyro Sensor

- C++

```

ev3dev::gyro_sensor gs = ev3dev::gyro_sensor();
std::cout << gs.angle() << std::endl;

```

- Python

```

gs = ev3.GyroSensor()
print gs.angle()

```

## Operating the LCD

- C++

```

ev3dev::lcd lcd = ev3dev::lcd();
unsigned char *fb = lcd.frame_buffer();
for(int i=0;i < 3072;i++)
{
if(i%24 < 12)fb[i] = 0x00;
else fb[i] = 0xff;
}

```

- Python

```

lcd = ev3.Screen()
lcd.mmap.seek(os.SEEK_SET)
lcd.mmap.write(chr(0xff)*3072)
for i in range(lcd.fix_info.smem_len):
if i%24 < 12:
lcd.mmap.seek(os.SEEK_SET)
lcd.mmap.seek(i)
lcd.mmap.write_byte(chr(0xff))

```
