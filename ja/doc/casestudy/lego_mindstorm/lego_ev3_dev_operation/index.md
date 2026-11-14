---
layout: page
title: ev3デバイスの操作方法について
---

<!-- Title: EV3デバイスの操作方法について -->
#contents

## モーター
### 速度制御
速度を制御するためには以下のデバイスファイルに"on"と書き込む必要があります。

```
 echo on > /sys/class/tacho-motor/motor0/speed_regulation
```

起動時には off になっているので速度制御はできません。
off の場合は duty_cycle_sp でデューティー比を設定できます。

そして以下のファイルに目標速度を書き込みます。

```
 echo 50 > /sys/class/tacho-motor/motor0/speed_sp
```

ここで指定する値は1秒間に何カウント動かすかという値なので、以下のデバイスファイルから取得する値を角速度に掛けて変換してください。
※モーターM、モーターLの場合は count_per_rot で取得できる値が360なので変換しなくても影響はありません。

```
 cat /sys/class/tacho-motor/motor0/count_per_rot
```

後は以下のコマンドを入力すると回転を開始します。

```
 echo run-forever > /sys/class/tacho-motor/motor0/command
```

現在の角速度を取得するためには以下のデバイスファイルを使用します。

```
 cat /sys/class/tacho-motor/motor0/speed
```

以上の手順を ev3dev-lang-cpp を利用して記述すると以下のようになります。

```
 ev3dev::large_motor lm = ev3dev::large_motor();
 lm.set_speed_regulation_enabled("on");
 lm.set_speed_sp(50*lm.count_per_rot());
 lm.run_forever();
 std::cout << lm.speed()/lm.count_per_rot() << std::endl;
```

ev3dev-lang-python を利用して記述すると以下のようになります。

```
 lm = ev3.LargeMotor()
 lm.set_attr_string("speed_regulation", "on")
 lm.speed_sp = 50*lm.count_per_rot
 lm.run_forever()
 print lm.speed/lm.count_per_rot
```


### 一定時間動作させる

モーターを一定時間動作させるには、まず以下のデバイスファイルで時間を設定してください。

```
 echo 2000 > /sys/class/tacho-motor/motor0/time_sp
```

そして以下のコマンドで動作を開始します。
```
 echo run-timed > /sys/class/tacho-motor/motor0/command
```


### 位置制御
位置制御を行うためにはまず duty_cycle_sp (speed_regulation が on の場合は speed_sp) を設定しておく必要があります。

```
 echo 50 > /sys/class/tacho-motor/motor0/speed_sp
```


次に以下のデバイスファイルで位置を設定します。

```
 echo 100 > /sys/class/tacho-motor/motor1/position_sp
```

この位置もカウント数で指定するため、count_per_rot で変換してください。

以下のコマンドで動作を開始します。

```
 echo run-to-abs-pos > /sys/class/tacho-motor/motor1/command
```

現在の位置からの相対的な角度を指定したい場合は以下のコマンドを利用します。

```
 echo run-to-rel-pos > /sys/class/tacho-motor/motor1/command
```

現在の位置は以下のデバイスファイルから取得できます。

```
 cat /sys/class/tacho-motor/motor1/position
```

以上の手順を ev3dev-lang-cpp を利用して記述すると以下のようになります。

```
 ev3dev::large_motor lm = ev3dev::large_motor();
 lm.set_speed_regulation_enabled("on");
 lm.set_speed_sp(50*lm.count_per_rot());
 lm.set_position_sp(100*lm.count_per_rot());
 lm.run_to_abs_pos(100*lm.count_per_rot());
 #lm.run_to_rel_pos(100*lm.count_per_rot());
```

ev3dev-lang-python を利用して記述すると以下のようになります。

```
 lm = ev3.LargeMotor()
 lm.set_attr_string(None, "speed_regulation", "on")
 lm.speed_sp = 50*lm.count_per_rot
 lm.run_to_abs_pos()
 #lm.run_to_rel_pos()
```


## センサーの C++、Python による操作

### カラーセンサーで反射光の強さ取得
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

### タッチセンサーのオンオフ取得
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

### ジャイロセンサーで角度取得
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

## LCD の操作
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


