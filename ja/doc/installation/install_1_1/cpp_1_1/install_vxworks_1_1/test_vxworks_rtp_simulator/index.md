---
layout: page
title: openrtm-aist動作確認(vxworks、rtp、シミュレータ利用の場合)
---

<!-- Title: OpenRTM-aist動作確認(VxWorks、RTP、シミュレータ利用の場合) -->
#contents

このページでは、Workbenchのシミュレータを用いてVxWorks用にビルドしたRTCのリアルタイムプロセス(RTP)の動作確認を行う手順を説明します。


## シミュレータの設定

以下の手順でシミュレータの設定を行ってください。

- [VxWorksシミュレータの設定]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/install_vxworks_1_1/test_vxworks_km_simulator/setup_vxwork_simulator)

## シミュレータの接続

WorkbenchのRemote Systemでシミュレータを選択後にconnect 'xxxxx'ボタンを押すとシミュレータと接続します。


<br>

<div align="center"><a href="sim5.png"><img src="sim5.png" width="60%;"></a></div>

<br>




## RTC実行
### ネームサーバー起動
VxWorksシミュレータ上にネームサーバーを起動します。
ネームサーバーはリアルタイムプロセス(RTP)として起動するため、Remote Systemsからシミュレータを右クリックして**Run**→**VxWorks Real Time Process**をクリックしてください。

<br>

<div align="center"><a href="rtp.png"><img src="rtp.png" width="60%;"></a></div>

<br>


Run ConfigurationsウインドウのLaunch Contextタブから各種設定を行ってください。

- 実行するシステムをシミュレータに設定
- omniNames.outのパス設定
- コマンドライン引数の設定

omniNames.outはomniORBのビルドディレクトリに生成されています。
共有ライブラリのパスに**libc.so.1**が無い場合はエラーとなるため、WorkbenchからomniNames.outのディレクトリにコピーしてください。

```
 cp $WIND_BASE/target/lib/usr/root/SIMPENTIUMgnu/bin/libc.so.1 /home/openrtm/omniORB-4.2.2/bin/simpentium_vxWorks_RTP_6.9/
```

RTPについてビルドできない場合は、VxWorksでネームサーバーは起動せずにUbuntu上のネームサーバーにRTCを登録するようにしてください。

- 例：/home/openrtm/omniORB-4.2.2/bin/simpentium_vxWorks_RTP_6.9/omniNames.out

Argumentsにはネームサーバーのポート番号を指定します。

- 例：-start 2809

設定が完了後にRunボタンをクリックするとネームサーバーが起動します。


<br>

<div align="center"><a href="nameserver.png"><img src="nameserver.png" width="60%;"></a></div>

<br>





### RTCの起動
ネームサーバーの起動と同じ手順でrtcd.vxeを実行します。
rtcd.vxeはOpenRTM-aistのビルドディレクトリのutils/rtcd以下に生成されています。


- 例(ConsoleIn)：/home/openrtm/OpenRTM-aist/build_vxworks/examples/SimpleIO/ConsoleIn.vxe
- 例(ConsoleOut)：/home/openrtm/OpenRTM-aist/build_vxworks/examples/SimpleIO/ConsoleOut.vxe

Argumentsには何も入力しなくても大丈夫ですが、Ubuntu側のネームサーバーを起動する場合は、Argumentsに**-o corba.nameservers:192.168.200.254**を追加してください。
Ubuntuのtap0インターフェースのIPアドレスは適宜確認してください。




Ubuntuで起動したRTシステムエディタでRTCが起動したかを確認してください。
VxWorksのネームサーバーにはネームサービス接続ボタンをクリック後、表示されたウインドウでIPアドレスを指定してOKをクリックすると接続します。


<br>

<div align="center"><a href="ns1.png"><img src="ns1.png" width="60%;"></a></div>

<br>


<br>

<div align="center"><a href="ns2.png"><img src="ns2.png" width="60%;"></a></div>

<br>


起動したRTCが登録されているかを確認してください。


<br>

<div align="center"><a href="ns3.png"><img src="ns3.png" width="60%;"></a></div>

<br>

RTCの接続、アクティブ化等の手順はUbuntuで動作確認する場合と同じです。


- [動作確認 (Linux編)]({{ site.baseurl }}/ja/doc/installation/install_1_1/cpp_1_1/test_linux_1_1)


### コマンドラインによる操作について

シミュレータ接続後にTarget Consoleウインドウからコマンド入力ができます。


<br>

<div align="center"><a href="sim6.png"><img src="sim6.png" width="60%;"></a></div>

<br>

以下のコマンドでRTCの動作確認ができます。
Workbench、omniORB、openRTM-aistのパスは適宜変更してください。

```
 cd "/home/openrtm/openrtm-build/omniORB/omniORB_69_rtp_sim/omniORB-4.2.2/bin/simpentium_vxWorks_RTP_6.9"
 cp "/home/openrtm/WindRiver/vxworks-6.9/target/lib/usr/root/SIMPENTIUMgnu/bin/libc.so.1","./"
 rtpSp "./omniNames.out -start 2809"
 
 cd "/home/openrtm/openrtm-build/OpenRTM/OpenRTM_69_rtp_sim/OpenRTM-aist/build_vxworks/examples/SimpleIO"
 cp "/home/openrtm/WindRiver/vxworks-6.9/target/lib/usr/root/SIMPENTIUMgnu/bin/libc.so.1","./"
 rtpSp "./ConsoleOutComp.vxe"
```

