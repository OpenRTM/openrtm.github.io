---
layout: page
title: "ros2通信機能の利用"
---

<!-- ROS2通信機能の利用 -->
#contents

## C++版
### Windows

#### Chocolateyのインストール
以下のページの指示に従いインストールします。

- [Chocolatey](https://chocolatey.org/install#installing-chocolatey)

#### Python3のインストール
以下のコマンドでインストールします。

 > choco install -y python

#### OpenSSLのインストール
以下から**Win64OpenSSL-1_0_2r.exe**を入手して、それを実行してインストールします。

- [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)

以下の環境変数を設定します。

<table class="table-alt">
  <tr>
    <td>OPENSSL_CONF</td>
    <td>C:\OpenSSL-Win64\bin\openssl.cfg</td>
  </tr>
</table>

<br>

環境変数PATHに**C:\OpenSSL-Win64\bin**を追加します。

#### asio、eigen、tinyxml、tinyxml-usestl、log4cxxのインストール
以下のページからNuGetパッケージ(**.nupkg**)ファイルをダウンロードしてください。

- https://github.com/ros2/choco-packages/releases

以下のコマンドでインストールします。依存するNugetパッケージが増える場合もあるようなので、適宜変更してください。

 > choco install -y -s <**'ダウンロードしたパス**'> asio eigen tinyxml-usestl tinyxml2 log4cxx


#### Python用パッケージのインストール
以下のコマンドでインストールします。

 > python -m pip install -U catkin_pkg empy pyparsing pyyaml setuptools

#### ROS2のインストール
以下のページから**ros2-****-********-windows-release-amd64.zip**をダウンロードします。

- https://github.com/ros2/ros2/releases

**C:\dev\ros2**等に展開して完了です。

#### OpenRTM-aistのビルド

CMake実行前にROS2の環境を設定するスクリプトを実行します。

 > call C:\dev\ros2\local_setup.bat

CMake実行時に**FASTRTPS_ENABLE**、**ROS2_ENABLE**のオプションをONにします。

 > cmake  -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc14 -G "Visual Studio 16 2019" -A x64 -DFASTRTPS_ENABLE=ON -DROS2_ENABLE=ON ..

その他の手順は通常と同じです。

- [OpenRTM-aistのビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

適当な場所にインストールしてください。

インストールするディレクトリは**CMAKE_INSTALL_PREFIX**のオプションで設定します。

 > cmake .. -DCMAKE_INSTALL_PREFIX=C:/workspace/OpenRTM-aist/build_omni/install
 > cmake --build . --config Release --target install

#### 動作確認

**<**'インストールしたパス**'>\2.0.0\Components\C++\Examples\vc14**のサンプルコンポーネントを実行します。

以下の内容のrtc.confを作成してください。


```
 manager.modules.load_path: {インストールしたパス}\\2.0.0\\ext\\transport
 manager.modules.preload: FastRTPSTransport.dll, ROS2Transport.dll
 manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps&marshaling_type=ros2:std_msgs/Float32&fast-rtps.topic=chatter, ConsoleIn0.out?interface_type=fast-rtps&marshaling_type=ros2:std_msgs/Float32&fast-rtps.topic=chatter
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: manager.module.load_path | シリアライザ用モジュール(FastRTPSTransport.dllとROS2Transport.dll)が置かれている場所
: manager.modules.preload | シリアライザ用モジュールを読み込む順番で指定
: manager.components.preconnect | コネクタ生成時の設定を記述します。interface_type(インターフェース型)に**fast-rtps**を、marshaling_type(マーシャリング型)に対応シリアライザ名を、fast-rtps.topic(トピック)に適当な任意の名前を記述します。

ROS/ROS2用のシリアライザと対応するROS/ROS2メッセージ型の関係を以下のリンクで示します。


- [シリアライザ名とROS/ROS2メッセージ型]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

コネクタの生成は**manager.components.preconnect**オプションにより設定します。
この例では**ConsoleOut0**コンポーネントの**in**のポート、**ConsoleIn0**コンポーネントの**out**のポートにそれぞれコネクタを生成しています。

実行前に環境変数PATHに以下を追加する必要があります。

- <**'インストールしたパス**'>\2.0.0\bin\vc14
- <**'インストールしたパス**'>\2.0.0\omniORB\4.2.3_vc14\bin\x86_win32
- C:\dev\ros2\bin
- C:\ProgramData\chocolatey\lib\tinyxml2\lib
- C:\ProgramData\chocolatey\lib\log4cxx\lib



**ConsoleInComp.exe**、**ConsoleOutComp.exe**を実行すると通信ができるようになります。



### Ubuntu
#### ROS2のインストール
以下のコマンドでインストールします。

```
 $ curl http://repo.ros2.org/repos.key | sudo apt-key add -
 $ sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
 $ export ROS_DISTRO=crystal
 $ sudo apt update
 $ sudo apt install ros-${ROS_DISTRO}-ros-core
```

ROS2用にbashの設定を以下のように行います。(次回以降のbash起動時の設定と、現在実行中のbashの設定を行います。)

```
 echo "source /opt/ros/crystal/setup.bash" >> ~/.bashrc
 source ~/.bashrc
```



#### OpenRTM-aistのビルド

CMake実行時に**FASTRTPS_ENABLE**、**ROS2_ENABLE**のオプションをONにします。

```
 $ cmake -DCORBA=omniORB -DCMAKE_BUILD_TYPE=Release -DFASTRTPS_ENABLE=ON -DROS2_ENABLE=ON ..
```

その他の手順は通常と同じです。

- [OpenRTM-aistのビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

ビルド後にインストールしてください。

```
 $ cmake --build . --target install
```

#### 動作確認
以下のrtc.confを作成します。

```
 manager.modules.load_path: /usr/local/lib/openrtm-2.0/transport/
 manager.modules.preload: FastRTPSTransport.so, ROS2Transport.so
 manager.components.preconnect: ConsoleOut0.in?interface_type=fast-rtps&marshaling_type=ros2:std_msgs/Float32&fast-rtps.topic=chatter, ConsoleIn0.out?interface_type=fast-rtps&marshaling_type=ros2:std_msgs/Float32&fast-rtps.topic=chatter
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: manager.module.load_path | シリアライザ用モジュール(FastRTPSTransport.soとROS2Transport.so)が置かれている場所
: manager.modules.preload | シリアライザ用モジュールを読み込む順番で指定
: manager.components.preconnect | コネクタ生成時の設定を記述します。interface_type(インターフェース型)に**fast-rtps**を、marshaling_type(マーシャリング型)に対応シリアライザ名を、fast-rtps.topic(トピック)に適当な任意の名前を記述します。

OpenRTM-aistのシリアライザが対応しているメッセージ型を以下に示します。

- [シリアライザ名とROS/ROS2メッセージ型]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

RTCを起動して動作確認します。

それぞれ別のターミナルから起動してください。

```
 /usr/local/share/openrtm-2.0/components/c++/examples/ConsoleInComp
```

```
 /usr/local/share/openrtm-2.0/components/c++/examples/ConsoleOutComp
```

## Python版
### Windows
C++版と同じ手順でROS2をインストールしてください。

#### OpenRTM-aistのインストール
OpenRTM-aist 1.2等をインストーラーでインストールしておいてください。
OpenRTM-aist Python版のソースコードを入手してください。

- [Python版のソースコード](https://github.com/OpenRTM/OpenRTM-aist-Python)

以下のコマンドでOpenRTM-aist Python版をインストールしてください。

```
 python setup.py build
 python setup.py install
```

#### 動作確認
動作前に以下のコマンドを実行してください。

```
  call C:\dev\ros2\setup.bat
```

以下のようなrtc.confを作成し、**ROS2Transport.py**をロード後、インターフェース型に**opensplice**を指定して起動します。

```
 manager.modules.load_path: C:\\Python37\\Lib\\site-packages\\OpenRTM_aist\\ext\\transport\\ROS2Transport
 manager.modules.preload: ROS2Transport.py
 manager.components.preconnect: ConsoleOut0.in?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32&ros2.topic=chatter, ConsoleIn0.out?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32&ros2.topic=chatter
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: manager.module.load_path | シリアライザ用モジュール(ROS2Transport.py)が置かれている場所
: manager.modules.preload | シリアライザ用モジュールを読み込む順番で指定
: manager.components.preconnect | コネクタ生成時の設定を記述します。interface_type(インターフェース型)に**ros2**を、marshaling_type(マーシャリング型)に対応シリアライザ名を、ros2.topic(トピック)に適当な任意の名前を記述します。



### Ubuntu
#### ROS2のインストール
以下のコマンドでインストールします。

```
 $ curl http://repo.ros2.org/repos.key | sudo apt-key add -
 $ sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
 $ export ROS_DISTRO=crystal
 $ sudo apt update
 $ sudo apt install ros-${ROS_DISTRO}-desktop
```

ROS2の環境設定のbashを実行するようにします。

```
 $ echo "source /opt/ros/crystal/setup.bash" >> ~/.bashrc
 $ source ~/.bashrc
```


```
 $  sudo apt-get install python-omniorb-omg omniidl-python doxygen
```

#### OpenRTM-aistのインストール
OpenRTM-aist Python版のソースコードを入手してください。

- [Python版のソースコード](https://github.com/OpenRTM/OpenRTM-aist-Python)

以下のコマンドでOpenRTM-aist Python版をビルド/インストールしてください。

```
 $ python setup.py build
 $ python setup.py install
```

#### 動作確認
ros2のsetup.bashを実行するとPYTHONPATHが上書きされるようなので以下のコマンドを実行する。

```
 $ export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/site-packages
 $ export PATH=$PATH:/usr/local/lib/python3.6/site-packages/
```

omniORBpyがインストールされているディレクトリにあわせて変更してください。

以下のようなrtc.confを作成し、**ROS2Transport.py**をロードし、インターフェース型に**ros2**、シリアライザに**ros2:std_msgs/Float32**を指定して起動するように指定します。

```
 manager.modules.load_path: /usr/local/lib/python3.6/site-packages/OpenRTM_aist/ext/transport/ROS2Transport/
 manager.modules.preload: ROS2Transport.py
 manager.components.preconnect: ConsoleOut0.in?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32&ros2.topic=chatter, ConsoleIn0.out?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32&ros2.topic=chatter
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

OpenRTM-aistのシリアライザが対応しているメッセージ型を以下に示します。

- [シリアライザ名とROS/ROS2メッセージ型]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)


以下のコマンドでRTCを起動して動作確認してください。

```
 $ python /usr/local/share/openrtm-2.0/components/python/SimpleIO/ConsoleIn.py
```

```
 $ python /usr/local/share/openrtm-2.0/components/python/SimpleIO/ConsoleOut.py
```

## 起動時のオプション
### C++
[Fast DDS通信機能のオプション]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/dds_comm_use/fast-rtps#起動時のオプション)を設定してください。

### Python
以下のオプションが設定できます。

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>設定例</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>ros2.args</td>
    <td></td>
    <td>**rclpy.init**の引数**args**</td>
  </tr>
  <tr>
    <td>ros2.node.name</td>
    <td>node_name</td>
    <td>ノード名</td>
  </tr>
</table>

## 接続時のオプション
### C++
[Fast DDS通信機能のオプション]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/dds_comm_use/fast-rtps#接続時のオプション)を設定してください。


### Python

接続時に設定可能な項目は以下の通りです。

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>デフォルト値</th>
    <th>オプション</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>marshaling_type</td>
    <td></td>
    <td></td>
    <td>シリアライザの種類。**ros:std_msgs/Float32**などが設定できる。</td>
  </tr>
  <tr>
    <td>ros2.topic</td>
    <td>chatter</td>
    <td></td>
    <td>DDSトピック名</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, SYSTEM_DEFAULT_QOS</td>
    <td>送信側の堅牢性(VOLATILE_DURABILITY_QOS：変わりやすい、TRANSIENT_LOCAL_DURABILITY_QOS：一時的なローカル設定）</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.deadline.period.sec</td>
    <td>0</td>
    <td></td>
    <td>受信側の最小周期</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.deadline.period.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUT0TOMATIC_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS, SYSTEM_DEFAULT_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.liveliness.lease_duration.sec</td>
    <td>0</td>
    <td></td>
    <td>受信側のハートビートの周期</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.liveliness.lease_duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.reliability.kind</td>
    <td>RELIABLE_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS, SYSTEM_DEFAULT_RELIABILITY_QOS</td>
    <td>受信側の信頼性(RELIABLE_RELIABILITY_QOS：高信頼、BEST_EFFORT_RELIABILITY_QOS：最高速度)</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.history.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS, SYSTEM_DEFAULT_HISTORY_QOS</td>
    <td>受信データの保持方法（KEEP_ALL_HISTORY_QOS：すべてのデータを保持、KEEP_LAST_HISTORY_QOSで指定したデータ数だけ保持）</td>
    <td>KEEP_LAST</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td>受信側の保持するデータ数</td>
  </tr>
  <tr>
    <td>ros2.reader_qos.lifespan.duration.sec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.lifespan.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.reader_qos.avoid_ros_namespace_conventions</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.durability.kind</td>
    <td>TRANSIENT_DURABILITY_QOS</td>
    <td>VOLATILE_DURABILITY_QOS, TRANSIENT_LOCAL_DURABILITY_QOS, SYSTEM_DEFAULT_QOS</td>
    <td>送信側の堅牢性(VOLATILE_DURABILITY_QOS：変わりやすい、TRANSIENT_LOCAL_DURABILITY_QOS：一時的なローカル設定）</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.deadline.period.sec</td>
    <td>0</td>
    <td></td>
    <td>送信側の最小周期</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.deadline.period.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.liveliness.kind</td>
    <td>AUTOMATIC_LIVELINESS_QOS</td>
    <td>AUTOMATIC_LIVELINESS_QOS, MANUAL_BY_TOPIC_LIVELINESS_QOS, SYSTEM_DEFAULT_LIVELINESS_QOS</td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.liveliness.lease_duration.sec</td>
    <td>0</td>
    <td></td>
    <td>送信側のハートビートの周期</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.liveliness.lease_duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.reliability.kind</td>
    <td>RELIABLE_RELIABILITY_QOS</td>
    <td>BEST_EFFORT_RELIABILITY_QOS, RELIABLE_RELIABILITY_QOS, SYSTEM_DEFAULT_RELIABILITY_QOS</td>
    <td>送信側の信頼性(RELIABLE_RELIABILITY_QOS：高信頼、BEST_EFFORT_RELIABILITY_QOS：最高速度)</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.history.kind</td>
    <td>KEEP_LAST_HISTORY_QOS</td>
    <td>KEEP_LAST_HISTORY_QOS, KEEP_ALL_HISTORY_QOS, SYSTEM_DEFAULT_HISTORY_QOS</td>
    <td>送信データの保持方法（KEEP_ALL_HISTORY_QOS：すべてのデータを保持、KEEP_LAST_HISTORY_QOSで指定したデータ数だけ保持）</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.history.depth</td>
    <td>1</td>
    <td></td>
    <td>送信側の保持するデータ数</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.lifespan.duration.sec</td>
    <td>0</td>
    <td></td>
    <td>送信側の未送信データの保持時間</td>
  </tr>
  <tr>
    <td>ros2.writer_qos.lifespan.duration.nanosec</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros2.writer_qos.avoid_ros_namespace_conventions</td>
    <td>YES</td>
    <td>YES, NO</td>
    <td></td>
  </tr>
</table>

以下に設定例を記載します。

```
 manager.components.preconnect: ConsoleOut0.in?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32, ConsoleIn0.out?interface_type=ros2&marshaling_type=ros2:std_msgs/Float32
```

## 簡単な動作確認
OpenRTM-aistをビルド、インストールすると、ROS2Transportの簡単な動作確認用の設定ファイルがインストールされます。

```
 D:\ros2-windows\setup.bat
 %RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
 %RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\transport\rtc.ros2.conf
```


```
 source /opt/ros/dashing/setup.sh
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/transport/rtc.ros2.conf
```


