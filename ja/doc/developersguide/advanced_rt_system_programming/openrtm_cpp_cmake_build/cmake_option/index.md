---
layout: page
title: "cmakeのオプション一覧"
---
<!-- Title: CMakeのオプション一覧 -->
#contents


## オプション一覧

<table class="table-alt">
  <tr>
    <th>名前</th>
    <th>説明</th>
    <th>デフォルト</th>
  </tr>
  <tr>
    <td>CORBA</td>
    <td>利用するCORBAのライブラリの種類(omniORB、TAO、ORBexpress)</td>
    <td>omniORB</td>
  </tr>
  <tr>
    <td>ORB_ROOT</td>
    <td>CORBAのライブラリをインストールした場所</td>
    <td>設定しない場合、Ubuntu、omniORBの場合はFindPkgConfigで検索。それ以外はエラー</td>
  </tr>
  <tr>
    <td>SSL_ENABLE</td>
    <td>SSLによるセキュアな通信を有効にするためのプラグインを生成するか<br> ON：生成する<br> OFF：生成しない</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>HTTP_ENABLE</td>
    <td>HTTP通信を有効にするためのプラグインを生成するか<br> ON：生成する<br> OFF：生成しない</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>OPENSSL_ROOT</td>
    <td>OpenSSLの各種ファイルを配置したディレクトリ。Windowsの場合は必須</td>
    <td></td>
  </tr>
  <tr>
    <td>OBSERVER_ENABLE</td>
    <td>コンポーネントオブザーバーを有効にするかどうか<br> ON：有効<br> OFF：無効</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>DOCUMENTS_ENABLE</td>
    <td>Doxygenでドキュメントを生成するかどうか<br> ON：生成する<br> OFF：生成しない</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>ROS_ENABLE</td>
    <td>ROS通信用シリアライザ、インターフェースを生成するか<br> ON：生成する<br> OFF：生成しない</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>FASTRTPS_ENABLE</td>
    <td>DDS(Fast-RTPS)通信用インターフェースを生成するか<br> ON：生成する<br> OFF：生成しない</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>ROS2_ENABLE</td>
    <td>ROS2通信用シリアライザを生成するか<br> ON：生成する<br> OFF：生成しない</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>EXAMPLES_ENABLE</td>
    <td>サンプルコンポーネントを生成するかどうか<br> ON：生成する<br> OFF：生成しない</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>UTILS_ENABLE</td>
    <td>サンプルコンポーネントを生成するかどうか<br> ON：生成する<br> OFF：生成しない</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>EXTLIB_ENABLE</td>
    <td>サンプルコンポーネントを生成するかどうか<br> ON：生成する<br> OFF：生成しない</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>FLUENTBIT_ENABLE</td>
    <td>Fluent Bitロガープラグインを生成するかどうか<br> ON：生成する<br> OFF：生成しない</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>FLUENTBIT_ROOT</td>
    <td>Fluent Bitのソースコードのディレクトリ</td>
    <td></td>
  </tr>
  <tr>
    <td>OPENSPLICE_ENABLE</td>
    <td>DDS(OpenSplice)通信用インターフェースを生成するか<br> ON：生成する<br> OFF：生成しない</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>OPENSPLICE_DIR</td>
    <td>OpenSpliceをインストールしたディレクトリ</td>
    <td></td>
  </tr>
  <tr>
    <td>RAPIDXML_DIR</td>
    <td>rapidxmlを展開したディレクトリ</td>
    <td></td>
  </tr>
</table>

### omniORBに関するオプション

<table class="table-alt">
  <tr>
    <th>名前</th>
    <th>説明</th>
    <th>デフォルト</th>
  </tr>
  <tr>
    <td>OMNI_VERSION</td>
    <td>omniORBのメジャーバージョン。omniORBを手動でビルド、任意の場所にインストールした場合は必須</td>
    <td>設定しなかった場合、LinuxでomniORBがpkg-configでインストールした場合は自動的に設定する。それ以外はエラー</td>
  </tr>
  <tr>
    <td>OMNI_MINOR</td>
    <td>omniORBのマイナーバージョン。omniORBを手動でビルド、任意の場所にインストールした場合は必須</td>
    <td>同上</td>
  </tr>
  <tr>
    <td>OMNITHREAD_VERSION</td>
    <td>omniThreadのバージョン。omniORBを手動でビルド、任意の場所にインストールした場合は必須</td>
    <td>同上</td>
  </tr>
</table>

### ビルドを選択可能なモジュールの依存関係


- OBSERVER_ENABLE
- DOCUMENTS_ENABLE
- EXAMPLES_ENABLE
- UTILS_ENABLE
- EXTLIB_ENABLE

依存はlibcoil、libRTCのみ。

- SSL_ENABLE
- ROS_ENABLE
- FASTRTPS_ENABLE


EXTLIB_ENABLEがONになっている必要がある。


- ROS2_ENABLE

FASTRTPS_ENABLEがONになっている必要があるため、FastRTPSTransportのビルドは必須。


