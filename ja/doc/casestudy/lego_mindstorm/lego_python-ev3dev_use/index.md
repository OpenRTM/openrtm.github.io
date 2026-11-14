---
layout: page
title: python-ev3dev の利用
---

<!-- Title: python-ev3dev の利用 -->
<!-- -*- pukiwiki-edit -*- -->
<!-- * python-ev3dev の利用 -->
#contents

## ev3dev-lang を利用した EV3 デバイスへのアクセス

ev3dev-lang は EV3 のモーターやセンサーにアクセスするためのライブラリです。以下の4つの言語で利用することができます。

- C++
- Python
- JavaScript
- Lua

ここでは、Python と C++ でのアクセス例を示します。

## python-ev3dev のインストール

ev3dev-lang の Python版 (Pythonバインディング) を (クロス開発環境ではなく) EV3 にインストールします。
以下のコマンドを入力すると、python-ev3dev がシステムにインストールされ、Python から利用できるようになります。

```
 # cd ~
 # mkdir work
 # d work
 # apt-get install libboost-python1.55.0 python-setuptools python-pil
 # wget https://github.com/rhempel/ev3dev-lang-python/archive/0.6.0.zip
 # unzip 0.6.0.zip
 # cd ev3dev-lang-python-0.6.0/
 # python setup.py install
```
<!-- # easy_install -U python-ev3dev -->


## python-ev3dev からのデバイスアクセス

python-ev3dev を使ってモーターを回してみます。まず、適当なディレクトリーに移動し（先ほどの python-ev3dev をインストールする時のディレクトリーで実行するとエラーになります) python をインタラクティブモードで起動します。

```
 # cd 
 # python
 Python 2.7.9 (default, Mar  1 2015, 13:52:09)
 [GCC 4.9.2] on linux2
 Type "help", "copyright", "credits" or "license" for more information.
 >>> import ev3dev.ev3 as ev3     (ev3dev モジュールをインポートする)
 >>> m = ev3.LargeMotor() (モーターオブジェクトをインスタンス化)
 >>> m.connected (接続しているかを確認)
 True
 >>> m.run_forever(duty_cycle_sp=50) (デューティー比50%でモータを連続回転)
 >>> m.stop() (モーターを停止)
```

モーターの停止モードには、'break'、'coast'、'hold' の3種類があります。デフォルトは 'coast' に設定してあり、m.stop() 実行時も、惰性で若干動いたと思います。これを、'hold' にして、stop 実行時にピタッと止めます。

<!-- >>> m.set(stop_command='hold') -->
```
 >>> m.set_attr_string(None, "stop_command", ev3.Motor.STOP_COMMAND_HOLD)
 >>> m.get_attr_string(None, "stop_command")[1]
 >>> m.run_forever(duty_cycle_sp=50)
 >>> m.stop()
```

以上のように、Python からモータを比較的容易に制御出来ます。

次にセンサーを利用してみます。ポート2に超音波センサーをつなぎます。引き続き Python のインタラクティブモードから以下のように入力します。
for 文で100秒間センサの値(mm)を表示し続けます。途中でやめたいときは Ctrl+C を押してループを抜けます。

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
 ：中略
 2382
 2366
 326
 76
 ^CTraceback (most recent call last):
   File "<stdin>", line 3, in <module>
 KeyboardInterrupt
 >>>
```

## python-ev3dev を知る

python-ev3dev の様々なクラス・関数のチュートリアル、リファレンスマニュアルは以下のページにあります。

- [Python language bindings for ev3dev](http://ddemidov.github.io/ev3dev-lang-python/)

また、Python では、モジュールやオブジェクトに対して **dir()** 関数を呼ぶと、利用可能な変数や関数のリストを見ることができます（変数か関数かの区別は dir() だけではわかりません）。

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

たとえば、ev3dev.ev3 モジュールには Sound という変数か関数があります。
run_forever() という関数があり、Sound() 関数を呼んでインスタンスを生成してみます。以下の例でわかるように、引数は不要だったようです。

<!-- >>> s = ev3dev.sound() -->
```
 >>> s = ev3.Sound()
 >>> dir(s)
 ['__doc__', '__module__', 'beep', 'play', 'speak', 'tone']
```


生成したオブジェクト **s** に対して **dir(s)** を実行してみます。すると、このオブジェクトで呼び出し可能そうな関数群が分かります。
試しに、speak を呼び出してみます。

```
 >>> s.speak("Hello RT-Middleware World")
```

EV3 から声が出るはずです。
実際には、関数の引数に何が必要なのか、どのようなデータ型を渡す必要があるのか、など詳細を知らないと呼び出せない関数もありますが、この方法でおおよその使い方を把握することができます。詳しい関数の呼び出し方を知りたい場合には、リファレンスマニュアルを参照してください。


