---
layout: page
title: "ssm通信機能の利用"
---

<!-- Title: SSM通信機能の利用 -->

#contents

このページでは[SSM(Streaming-data-Sharing-Manager](https://github.com/sitRyo/Distributed-Streaming-data-Sharing-Manager)との通信プラグインの導入手順を説明します。

以降の作業はUbuntu 18.04環境を想定しています。

## SSMのインストール

以下のコマンドでSSMをインストールします。

```
 git clone https://github.com/sitRyo/Distributed-Streaming-data-Sharing-Manager -b 32-64bit
 cd Distributed-Streaming-data-Sharing-Manager/
 ./configure --prefix=${OPENRTM_INSTALL_DIR}
 sudo autoreconf -i -f
 make
 make install
```

## OpenRTM-aistのビルド、インストール

CMake実行時に**SSM_ENABLE**のオプションをONにします。SSMのインストール先を指定する場合は**SSM_ROOT**を設定します。

```
 cmake -DSSM_ENABLE=ON -DSSM_ROOT=${OPENRTM_INSTALL_DIR} ..
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
 manager.modules.load_path: /usr/local/lib/openrtm-2.0/transport/
 manager.modules.preload: SSMTransport.so
 manager.components.preconnect: ConsoleOut0.in?interface_type=ssm&ssm.stream_name=test_stream&dataflow_type=pull, ConsoleIn0.out?interface_type=ssm&ssm.stream_name=test_stream
 manager.components.preactivation: ConsoleOut0, ConsoleIn0
```


RTCを起動する前に**ssm-coordinator**を起動します。

```
 ssm-coordinator
```

ConsoleInComp、ConsoleOutCompをそれぞれ別のターミナルで起動するとデータの転送が確認できます。

### 接続時のオプション

データポート接続時のコネクタプロファイルに設定できるオプションは以下の通りです。

<table class="table-alt">
  <tr>
    <th>オプション名</th>
    <th>デフォルト値</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>ssm.stream_name</td>
    <td>sensor_test</td>
    <td></td>
  </tr>
  <tr>
    <td>ssm.stream_size</td>
    <td>0</td>
    <td></td>
  </tr>
  <tr>
    <td>ssm.life_ssm_time</td>
    <td>5.0</td>
    <td></td>
  </tr>
  <tr>
    <td>ssm.cycle_ssm_time</td>
    <td>0.05</td>
    <td></td>
  </tr>
  <tr>
    <td>ssm.stream_id</td>
    <td>0</td>
    <td></td>
  </tr>
</table>

## 簡単な動作確認
OpenRTM-aistをビルド、インストールすると、ROSTransportの簡単な動作確認用の設定ファイルがインストールされます。

```
 ${SSM_INSTALL_DIR}/bin/ssm-coordinator
```

```
 source ${OPENRTM_INSTALL_DIR}/etc/environment-setup.sh
 ${OPENRTM_INSTALL_DIR}/share/openrtm-2.0/components/c++/examples/ConsoleOutComp -f ${OPENRTM_INSTALL_DIR}/etc/transport/rtc.ssm.conf
```


