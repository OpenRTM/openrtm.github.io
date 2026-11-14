---
layout: page
title: "設定ファイルとコマンドラインオプション (基礎編)"
---
<!-- Title: 設定ファイルとコマンドラインオプション (基礎編) -->
#contents

## 設定ファイル  ( rtc.conf ) 
コンポーネントマネージャは起動時に設定ファイル rtc.conf を読み込みます。
コンフィギュレーションファイルは通常 rtc.conf という名前で作成しますが、任意の名前で作成したコンフィギュレーションファイルを渡すこともできます。

### rtc.conf の配置場所

rtc.conf は通常RTC実行ファイル（スタンドアロンコンポーネント： xxxComp や xxxComp.exe など実行形式になっているRTC)  と同じディレクトリーに配置して、その設定を自動的に読み込ませます。
もしくは、<strong>-f</strong> オプションを利用して任意の名前の設定ファイルを読み込ませることもできます。
rtc.conf が実行ファイルと同じディレクトリーにないか、<strong>-f</strong> オプションで指定されていない場合は、代わりにシステムに配置された rtc.conf を読み込みます。

rtc.conf の読み込み優先度は以下のように設定されています。

#### Linux/Unixの場合
1. コマンドラインオプション "-f"
1. 環境変数 "RTC_MANAGER_CONFIG"
1. デフォルト設定ファイル "./rtc.conf"
1. デフォルト設定ファイル "/etc/rtc.conf"
1. デフォルト設定ファイル "/etc/rtc/rtc.conf"
1. デフォルト設定ファイル "/usr/local/etc/rtc.conf"
1. デフォルト設定ファイル "/usr/local/etc/rtc/rtc.conf"
1. 埋め込みコンフィギュレーション値

#### Windowsの場合
1. コマンドラインオプション "-f"
1. 環境変数 "RTC_MANAGER_CONFIG"
1. デフォルト設定ファイル "./rtc.conf"
1. デフォルト設定ファイル "%RTM_ROOT%/%RTM_VC_VERSION%/rtc.conf"

Windowsでは、環境変数 ”RTM_ROOT"' および ’’RTM_VC_VERSION'' で指定されるディレクトリー下に置かれた rtc.conf (通常は C:\Program Files\OpenRTM-aist\(バージョン番号)\(VCのバージョン)) が読み込まれます。

### 主な設定項目
以下に、良く利用される rtc.conf の設定オプションを示します。
以下のオプション以外にも、rtc.conf には様々なオプションを指定することができます。詳細は [rtc.conf設定項目一覧]({{ site.baseurl }}/ja/doc/developersguide/basic_rtc_programming/rtc_conf_reference) を参照してください。

#### ネームサービスに関する設定 
ネーミングサービスの設定に関する項目は以下の通りです。

:<strong>corba.nameservers</strong>|
host_name:port_numberで指定、デフォルトポートは2809 (omniORB のデフォルト)。~
複数サーバーを指定可能で、サーバー名の区切り文字はコンマ "," 。

:<strong>naming.formats</strong>|
%h.host_cxt/%n.rtc →host.host_cxt/MyComp.rtc~
複数指定可能。~
0.2.0互換にしたければ、~
%h.host_cxt/%M.mgr_cxt/%c.cat_cxt/%m.mod_cxt/%n.rtc

:<strong>naming.update.enable</strong>|
“YES” or “NO”~
ネーミングサービスへの登録の自動アップデート設定。~
コンポーネント起動後にネームサービスが起動したときに、再度名前を登録します。

:<strong>naming.update.interval</strong>|
アップデートの周期[s]。デフォルトは10秒。

:<strong>timer.enable</strong>|
“YES” or “NO”~
マネージャタイマー有効・無効。naming.updateを使用するには有効でなければならない。

:<strong>timer.tick</strong>|
タイマーの分解能[s]。デフォルトは100ms。

#### ログ出力に関する設定

:<strong>logger.enable</strong>|
“YES” or “NO”~
ログ出力を有効・無効に設定。

:<strong>logger.file_name</strong>|
ログファイル名。~
%h：ホスト名､%M:マネージャ名,%p：プロセスID 使用可

:<strong>logger.date_format</strong>|
日付フォーマット。strftime(3)の表記法に準拠。~
デフォルト：%b %d %H:%M:%S → Apr 24 01:02:04|

:<strong>logger.log_level</strong>|
ログレベル： SILENT, ERROR, WARN, INFO, DEBUG, TRACE, VERBOSE, PARANOID.~
<!-- ログレベル： SILENT, ERROR, WARN, NORMAL, INFO, DEBUG, TRACE, VERBOSE, PARANOID.~ -->
何も出力しない(SILENT)～全て出力する(PARANOID).~
※以前は RTC 内で使えましたが、現在は使えません。


#### 実行コンテキストに関する設定 

:<strong>exec_cxt.periodic.type</strong>|
使用する実行コンテキストを指定。~
現在のところ、
PeriodicExecutionContext, ExtTrigExecutionContext
が使用可能です。~
デフォルトはPeriodicExecutionContext.

:<strong>exec_cxt.periodic.rate</strong>|
実行コンテキストの周波数[Hz]を指定。~
有効範囲：(0, 1000000].~
デフォルト：1000.~


#### その他の設定 

:<strong>corba.endpoint</strong>|
IP_Addr:Port で指定。NIC が複数あるとき、ORB をどちらで listen させるかを指定します。~
Port を指定しない場合でも<strong>:</strong>が必要です。~
例:  corba.endpoint: 192.168.0.12~
NIC が2つある場合必ず指定してください。
(指定しなくても偶然正常に動作することもあります。)

:<strong>corba.args</strong>|
CORBA に対する引数。詳細は omniORB のマニュアルを参照してください。

<strong>[カテゴリ名].[コンポーネント名].config_file</strong>|
<strong>[カテゴリ名].[インスタンス名]. config_file</strong>|
コンポーネントの設定ファイル
カテゴリ名：manipulator、コンポーネント名：myarm、インスタンス名 myarm 0、1、2… の場合
```
 manipulator.myarm.config_file: arm.conf
 または
 manipulator.myarm0.config.file: arm0.conf
```
のように指定可能です。

## コマンドラインオプション


スタンドアロンコンポーネントの場合、またはRTC daemon (rtcd) では、コマンドラインにいくつかのオプションを指定することができます。
以下の表に、指定可能なコマンドラインオプションを示します。

hogehogehoge

<table class="table-alt">
  <tr>
    <th>オプション</th>
    <th>意味</th>
  </tr>
  <tr>
    <td>-a</td>
    <td>マネージャサービス OFF</td>
  </tr>
  <tr>
    <td>-f ファイル名</td>
    <td>設定ファイルの指定</td>
  </tr>
  <tr>
    <td>-o オプション</td>
    <td>オプション指定</td>
  </tr>
  <tr>
    <td>-p ポート番号</td>
    <td>ポート番号指定</td>
  </tr>
  <tr>
    <td>-d</td>
    <td>マスターマネージャ指定</td>
  </tr>
</table>


これらのオプションの詳細な意味をいかに示します。

### -a: マネージャサービスOFF

通常、RTCを起動するためには、内部のコンポーネントマネージャがRTCをインスタンス化したり、削除したりします。（ライフサイクルの管理を行う、という）
デフォルトではこのマネージャを、リモートから制御できるようにサーバー（サーバント）が起動されるようになっています。
しかし、起動後に、同じプロセスで同じRTCを起動したり、別のRTCのモジュールをロードしてRTCを起動させたり等する必要がない場合には、サーバントは不要なので <strong>-a</strong> オプションを指定することでサーバントの起動を抑制することもできます。

### -f: 設定ファイル指定

<strong>-f</strong> オプションを利用すると、任意の名前のファイルを rtc.conf の代わりにスタンドアロンコンポーネントやrtcdに与えることができます。

```
 <利用例>
 ConsoleInComp -f consin.conf
```


### -o: オプション指定

<strong>-o</strong> オプションを利用すると、rtc.conf に指定することのできるオプションをコマンドラインから与えることができます。<strong>-o</strong> オプションで与えたオプションは rtc.conf で指定されたものよりも優先されますので、rtc.conf で指定してあるオプションを一時的に上書きして変更したい場合などは、<strong>-o</strong>オプションを利用すると便利です。
ただし、コマンドラインオプションとして渡すので、空白は引数の切れ目として認識されますので、指定する際には空白を入れないか、シングルクォーテーションかダブルクォーテーションで囲むなどする必要があります。

```
 <利用例>
 ConsoleInComp -o corba.nameservers:localhost,openrtm.org
 ConsoleInComp -o "corba.nameservers:localhost, openrtm.org"
 <正しく認識されない例>
 ConsoleInComp -o corba.nameservers:localhost, openrtm.org
 '',(カンマ)''の後に空白があるため、openrtm.org が別の引数として認識される。
```


### -p: ポート番号指定

<strong>-p</strong> を利用すると、起動するRTCが利用するポート番号を指定することができます。
RTC起動時に特定のポート番号で起動したい場合には、このオプションを利用するとよいでしょう。
このオプションは <strong>corba.endpoints:</strong> オプションでホスト名無しで、ポート番号のみを指定するのと同じふるまいをします。

```
 <利用例>
 ConsoleInComp -p 2810
 以下と同じ
 ConsoleInComp -o "corba.endpoints: :2810" 
```

### -d: マスターマネージャ指定

<strong>-d</strong> オプションを利用すると、起動したスタンドアロンコンポーネントや rtcd をデーモンモードかつマスターマネージャとして起動することができます。
マネージャにはマスターとスレーブがあり、マスターは通常固定ポート番号 2810 でリクエストを待ち受け、スレーブに対してRTCの起動などを委譲します。
<strong>-d</strong> オプションを指定して起動すると、ポート番号がデフォルトでは 2810 に固定され、またマネージャのサーバントがマスターモードで起動され、ネームサービスにマネージャの参照が登録されます。

