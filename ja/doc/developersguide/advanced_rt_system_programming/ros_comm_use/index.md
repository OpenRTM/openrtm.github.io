---
layout: page
title: "ros通信機能の利用"
---
<!-- Title: ROS通信機能の利用 -->
#contents

## C++版
### Windows
#### ROSのインストール
以下のサイトの手順に従ってRos4WinをUSBメモリにインストールしてください。

- [Ros4Win](http://hara-jp.com/_default/ja/Topics/ROS_Windows_Install.html)

※リポジトリのURLが変わった関係でrptが正常に動作しない場合があります。修正済みでない場合はまず**'src\rpt\ros4win.py**'のファイルを修正してください。

```
 #PKG_REPO_BASE="http://hara.jpn.com/cgi/" #修正前
 PKG_REPO_BASE="http://hara-jp.com/cgi/"  #修正後
```

以下のコマンドでRos4Winをインストールしてください。

```
 git clone https://github.com/haraisao/rpt
 cd rqt
 python src\rpt\rpt.py update
 python src\rpt\rpt.py install ros_base
 python src\rpt\rpt.py install ros_setup
```


#### OpenRTM-aistのビルド

最初に以下のコマンドで**CMAKE_PREFIX_PATH**、**ROS_HOME_DRIVE**の環境変数を設定します。
ここではドライブ"D:"にインストールしたUSBドライブが刺さっている前提でコマンドを示していますが、違うドライブに刺さっている場合は"D:"の部分をそのドライブ名に変更してください。

```
 set ROS_HOME_DRIVE=D:
 set CMAKE_PREFIX_PATH=%CMAKE_PREFIX_PATH%;%ROS_HOME_DRIVE%/opt/ros/melodic/share
```

以降の作業の前に以下のコマンドでROSの環境を設定します。

```
 D:\opt\ros\melodic\ros_setup.bat
```

CMake実行時に**ROS_ENABLE**のオプションをONにします。

```
 cmake -DORB_ROOT=C:/workspace/omniORB-4.2.3-win64-vc14 -DCORBA=omniORB -G "Visual Studio 16 2019" -A x64 -DROS_ENABLE=ON ..
```

その他の手順は通常と同じです。

- [OpenRTM-aistのビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

ビルド後にインストールしてください。

```
 cmake --build . --config Release --target install
```

#### 動作確認
以下のrtc.confを作成します。

```
 manager.modules.load_path: C:\\workspace\\openrtm\\build_omni\\devel\\bin\\Release
 manager.modules.preload: ROSTransport.dll
 manager.components.preconnect: ConsoleOut0.in?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleOut0, ConsoleIn0.out?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleIn0
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: **manager.modules.load_path**| シリアライザーモジュール(ROSTransport.dll)を置く場所を指定します。
: **manager.modules.preload**| ROS通信のためのシリアライザーモジュールのの指定をします。Windowsの場合には**ROSTransport.dll**を指定します。
: **manager.components.preconnect**| コネクタ生成に関する設定をしています。interface_type(インターフェース型)に**ros**、marshaling_type(マーシャリング型)に対応シリアライザの名前、ros.topic(トピック名)に適当な任意の名前を設定します。

OpenRTM-aistのシリアライザーモジュール(ROSTransport.dll)が対応しているメッセージ型は以下のようになります。

- [シリアライザ名とROS/ROS2メッセージ型]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

RTCを起動して動作確認します。
以下のコマンドでClinkを起動してください。

```
 D:\opt\start_ros.bat
```

以降の作業はClink上で実行します。

以下のファイルを実行します。この時上記の変更をしたrtc.confは、VC14等のOpenRTM-aistをインストール時に指定したVisual Studioのバージョンに関連したのフォルダー(デフォルトではExamplesの下のVC14)に実行するexeファイルがありますので、そこと同じディレクトリに置くようにしてください。

```
 ${OpenRTM_INSTALL_DIR}\2.0\Components\C++\Examples\ConsoleInComp.exe
 ${OpenRTM_INSTALL_DIR}\2.0\Components\C++\Examples\ConsoleOutComp.exe
```

### Ubuntu
#### ROSのインストール

以下のコマンドでインストールしてください。

```
 $ export ROS_DISTRO=melodic
 $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
 $ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
 $ sudo apt-get -y update
 $ sudo apt-get -y install ros-${ROS_DISTRO}-ros-base
 $ sudo rosdep init
 $ rosdep update
```

ROS用にbashの設定を以下のように行います。(次回以降のbash起動時の設定と、現在実行中のbashの設定を行います。)

```
 $ echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
 $ source ~/.bashrc
```

#### OpenRTM-aistのビルド

CMake実行時に**ROS_ENABLE**のオプションをONにします。

```
 $ cmake -DCORBA=omniORB -DCMAKE_BUILD_TYPE=Release -DROS_ENABLE=ON ..
```

その他の手順は通常と同じです。

- [OpenRTM-aistのビルド手順]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

ビルド後にインストールしてください。

```
 $ cmake --build . --target install
```

#### 動作確認
以下のrtc.confを作成します。このファイルは下記のRTCコンポーネントを起動する時に使うカレントワーキングディレクトリにおいてください。

```
 manager.modules.load_path: /usr/local/lib/openrtm-2.0/transport/
 manager.modules.preload: ROSTransport.so
 manager.components.preconnect: ConsoleOut0.in?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleOut0, ConsoleIn0.out?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleIn0
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: **manager.modules.load_path**| シリアライザーモジュール(ROSTransport.so)を置く場所を指定します。
: **manager.modules.preload**| ROS通信のためのシリアライザーモジュールのの指定をします。Ubuntuの場合には**ROSTransport.so**を指定します。
: **manager.components.preconnect**| コネクタ生成に関する設定をしています。interface_type(インターフェース型)に**ros**、marshaling_type(マーシャリング型)に対応シリアライザの名前、ros.topic(トピック名)に適当な任意の名前を設定します。

OpenRTM-aistのシリアライザーモジュール(ROSTransport.so)が対応しているメッセージ型は以下のようになります。

- [シリアライザ名とROS/ROS2メッセージ型]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

ConsoleInComp、ConsoleOutCompを起動して動作確認します。

それぞれ別のターミナルから起動してください。

```
 $ /usr/local/share/openrtm-2.0/components/c++/examples/ConsoleInComp
```

```
 $ /usr/local/share/openrtm-2.0/components/c++/examples/ConsoleOutComp
```




## Python版
### Windows
#### ROSのインストール
以下のページに従ってROSをUSBメモリにインストールしてください。

- [ROS_Windows_Install](http://www.hara-jp.com/_default/ja/Topics/ROS_Windows_Install.html)

#### OpenRTM-aistのインストール
OpenRTM-aist 1.2等をインストーラーでインストールしておいてください。
OpenRTM-aist Python版のソースコードを入手してください。

- [OpenRTM-aist Python版のソースコード](https://github.com/OpenRTM/OpenRTM-aist-Python)

以下のコマンドでOpenRTM-aist Python版をインストールしてください。

```
 python setup.py build
 python setup.py install
```


#### 動作確認
**start_ros.bat**を2回実行して、ROSの環境設定をしたウインドウを2つ開いてください。

```
 D:\opt\start_ros.bat
```

片方のウインドウで**roscore**を起動します。

```
 roscore
```

もう片方のウインドウでOpenRTM-aistをインストールしたディレクトリをPYTHONPATHに設定します。

```
 set PYTHONPATH=%PYTHONPATH%;C:\Python37\Lib\site-packages;C:\Python37\Lib\site-packages\OpenRTM_aist;C:\Python37\Lib\site-packages\OpenRTM_aist\utils;C:\Python37\Lib\site-packages\OpenRTM_aist\RTM_IDL
```

以下のrtc.confを作成します。(rtc.confはRTCのexeファイルが実行される時のディレクトリに作成してください。サンプルバッチファイルを使う場合は、バッチファイルから起動されるexeファイルが置かれているディレクトリになります。)


```
 manager.modules.load_path: C:\\Python37\\Lib\\site-packages\\OpenRTM_aist\\ext\\transport\\ROSTransport
 manager.modules.preload: ROSTransport.py
 manager.components.preconnect: ConsoleOut0.in?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleOut0, ConsoleIn0.out?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleIn0
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: **manager.modules.load_path**| シリアライザーモジュール(ROSTransport.py)を置く場所を指定します。
: **manager.modules.preload**| ROS通信のためのシリアライザーモジュールのの指定をします。Pythonの場合には**ROSTransport.py**を指定します。
: **manager.components.preconnect**| コネクタ生成に関する設定をしています。interface_type(インターフェース型)に**ros**、marshaling_type(マーシャリング型)に対応シリアライザの名前、ros.topic(トピック名)に適当な任意の名前を設定します。


OpenRTM-aistのシリアライザーモジュール(ROSTransport.py)が対応しているメッセージ型は以下のようになります。

- [シリアライザ名とROS/ROS2メッセージ型]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

上記のrtc.confを用いてRTCを起動して動作確認してください。

### Ubuntu
#### ROSのインストール
C++版と同じ手順でROSをインストールしてください。

#### OpenRTM-aistのインストール
以下のパッケージをインストールしてください。

```
 $ sudo apt-get install python-omniorb-omg omniidl-python doxygen
```

以下のコマンドでOpenRTM-aist Python版をインストールします。

```
 $ git clone https://github.com/OpenRTM/OpenRTM-aist-Python
 $ cd OpenRTM-aist-Python
 $ python setup.py build
 $ sudo python setup.py install
```

#### 動作確認
以下のrtc.confを作成します。(rtc.confはRTCを実行する時のカレントワーキングディレクトリに作成してください。)

```
 manager.modules.load_path: /usr/local/lib/python2.7/dist-packages/OpenRTM_aist/ext/transport/ROSTransport/
 manager.modules.preload: ROSTransport.py
 manager.components.preconnect: ConsoleOut0.in?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleOut0, ConsoleIn0.out?interface_type=ros&marshaling_type=ros:std_msgs/Float32&ros.topic=chatter&ros.node.name=ConsoleIn0
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```

: **manager.modules.load_path**| シリアライザーモジュール(ROSTransport.py)を置く場所を指定します。
: **manager.modules.preload**| ROS通信のためのシリアライザーモジュールのの指定をします。Pythonの場合には**ROSTransport.py**を指定します。
: **manager.components.preconnect**| コネクタ生成に関する設定をしています。interface_type(インターフェース型)に**ros**、marshaling_type(マーシャリング型)に対応シリアライザの名前、ros.topic(トピック名)に適当な任意の名前を設定します。

OpenRTM-aistのシリアライザーモジュール(ROSTransport.py)が対応しているメッセージ型は以下のようになります。

- [シリアライザ名とROS/ROS2メッセージ型]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/ros_comm_use/ros_ros2_default_support_message_types)

以下のコマンドでRTCを起動して動作確認してください。

```
 $ python /usr/local/share/openrtm-2.0/components/python/SimpleIO/ConsoleIn.py
```

```
 $ python /usr/local/share/openrtm-2.0/components/python/SimpleIO/ConsoleOut.py
```



### 接続時のオプション
#### C++
データポート接続時のコネクタプロファイルに設定できるオプションは以下の通りです。

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
    <td>ros.topic</td>
    <td>chatter</td>
    <td></td>
    <td>トピック名</td>
  </tr>
  <tr>
    <td>ros.roscore.host</td>
    <td>localhost</td>
    <td></td>
    <td>ROS Masterのホスト名</td>
  </tr>
  <tr>
    <td>ros.roscore.port</td>
    <td>11311</td>
    <td></td>
    <td>ROS Masterのポート番号</td>
  </tr>
  <tr>
    <td>ros.node.name</td>
    <td></td>
    <td></td>
    <td>ROSノードの名前</td>
  </tr>
  <tr>
    <td>ros.node.anonymous</td>
    <td>NO</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.so_keepalive</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_nodelay</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td>YES：ROSノード名をUUIDで設定、NO：ROSノードをrtcompに設定</td>
  </tr>
  <tr>
    <td>ros.tcp_keepcnt</td>
    <td>9</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_keepidle</td>
    <td>60</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_keepintvl</td>
    <td>10</td>
    <td></td>
    <td></td>
  </tr>
</table>


#### Python
データポート接続時のコネクタプロファイルに設定できるオプションは以下の通りです。

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
    <td>ros.topic</td>
    <td>chatter</td>
    <td></td>
    <td>トピック名</td>
  </tr>
  <tr>
    <td>ros.roscore.host</td>
    <td>localhost</td>
    <td></td>
    <td>ROS Masterのホスト名</td>
  </tr>
  <tr>
    <td>ros.roscore.port</td>
    <td>11311</td>
    <td></td>
    <td>ROS Masterのポート番号</td>
  </tr>
  <tr>
    <td>ros.node.name</td>
    <td></td>
    <td></td>
    <td>ROSノードの名前</td>
  </tr>
  <tr>
    <td>ros.node.anonymous</td>
    <td>NO</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.so_reuseaddr</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.so_keepalive</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_nodelay</td>
    <td>YES</td>
    <td>YES,NO</td>
    <td>YES：ROSノード名をUUIDで設定、NO：ROSノードをrtcompに設定</td>
  </tr>
  <tr>
    <td>ros.tcp_keepcnt</td>
    <td>9</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_keepidle</td>
    <td>60</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.tcp_keepintvl</td>
    <td>10</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ros.sock.timeout</td>
    <td>60</td>
    <td></td>
    <td></td>
  </tr>
</table>


## 簡単な動作確認
OpenRTM-aistをビルド、インストールすると、ROSTransportの簡単な動作確認用の設定ファイルがインストールされます。

```
 D:\opt\ros\melodic\ros_setup.bat
 roscore
```

```
 D:\opt\ros\melodic\ros_setup.bat
 %RTM_ROOT%\ext\environment-setup.omniorb.vc16.bat
 %RTM_ROOT%\Components\C++\Examples\vc16\ConsoleOutComp.exe -f %RTM_ROOT%\ext\transport\rtc.ros.conf
```

```
 source /opt/ros/melodic/setup.bash
 roscore
```

```
 source /opt/ros/melodic/setup.bash
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/transport/rtc.ros.conf
```


