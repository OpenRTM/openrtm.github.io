---
layout: page
title: "rtc.conf設定項目一覧"
---

#contents(3)

## 一般的な設定

### config.version
コンフィギュレーションファイルのバージョン。

このパラメータは内部的にセットされるコンフィギュレーションのバージョン。
通常、OpenRTM-aistと同じバージョンである。rtc.confでセットする必要はなく、読み取り専用のパラメータ。
このバージョンを読み取ることで、rtc.confとOpenRTM-aistのバージョンを知ることができる。

- 設定: 読み出し専用. 設定による影響なし.
- デフォルト: 現在の OpenRTM-aist のバージョンと同じ.
- 例:
```
 config.version: 2.0
```

### openrtm.name

このパラメーターは、内部で設定されているバージョンを含むOpenRTM-aistの名前である。
読み取り専用のパラメータでありrtc.confで設定する必要はない。
このパラメーターを読み取ることにより、OpenRTM-aistの名前とバージョンがわかる。

- 設定: 読み取り専用. 設定による影響なし.
- デフォルト: 現在のバージョン付きの OpenRTM-aist の名称
- 例:
openrtm.name: OpenRTM-aist-2.0.0

### openrtm.version
OpenRTM-aist のバージョン。
- 例:
```
 openrtm.version: 1.0.0
```

## ネームサービスに関する設定

### naming.enable

このオプションはネーミングサービスに関する機能の有効・無効を切り替える。
YESを指定した場合、ネームサービスへRTCの参照を登録する。NOの場合、ネー
ムサービスへのRTCの参照の登録は行われない。

- 指定: **YES** or **NO**
- デフォルト値: YES
- 例:
```
 manager.is_master: NO
```

### naming.type

このオプションはネームサービスのタイプを指定する。現在のところはcorbaの
みをサポートしている。
- 指定: ネームサービスのタイプ
- デフォルト値: corba
- 例:
```
 naming.type: corba
```

### naming.formats

RTCをネームサーバに登録する際のフォーマットを指定する。以下の **%**で始
まる指定子を利用することができる。名前階層のデリミタは **/** であり、名
前と種類(kind)のデリミタは **.** である。

<table class="table-alt">
  <tr>
    <td>%n</td>
    <td>RTCのインスタンス名</td>
  </tr>
  <tr>
    <td>%t</td>
    <td>RTCのタイプ名</td>
  </tr>
  <tr>
    <td>%m</td>
    <td>RTCのモジュール名</td>
  </tr>
  <tr>
    <td>%v</td>
    <td>RTCのバージョン</td>
  </tr>
  <tr>
    <td>%V</td>
    <td>RTCのベンダ名</td>
  </tr>
  <tr>
    <td>%c</td>
    <td>RTCのカテゴリ名</td>
  </tr>
  <tr>
    <td>%h</td>
    <td>ホスト名</td>
  </tr>
  <tr>
    <td>%M</td>
    <td>マネージャ名</td>
  </tr>
  <tr>
    <td>%p</td>
    <td>プロセスID</td>
  </tr>
</table>

- 指定: /<name>.<kind>/<name>.<kind>/...
- デフォルト値: %h.host_cxt/%n.mgr
- 例:
```
 naming.formats: %h.host/%n.rtc
```

### naming.update.enable

RTCのネームサーバへの登録は通常インスタンス生成時に行われる。したがって、
RTCの生成以降に起動されたネームサーバには、当該RTCの名前と参照は登録さ
れない。このオプションを指定することで、定期的にネームサーバを確認し、
ネームサーバの起動が確認された場合、改めて名前と参照を登録する。

- 指定: **YES** or **NO**
- デフォルト値: YES
- 例:
```
 naming.update.enable: YES
```

### naming.update.interval

naming.update.enable が YES の場合、ネームサーバの確認および再登録を行
う周期を指定する。

- 指定: 登録周期を [s] で指定する。
- デフォルト値: 10.0
- 例:
```
 naming.update.interval: 10.0
```

### naming.update.rebind

このオプションに YES を指定すると、すでに名前と参照が登録されているネー
ムサーバ上で名前が削除されるなどした場合にもの、再度登録を行う。

- 指定: **YES** or **NO**
- デフォルト値: NO
- 例:
```
 naming.update.rebind: NO
```

<!-- Logger configurations -->

## ロガー関係の設定

### logger.enable

ロガーの有効化・無効化の指定。

- 指定: **YES** or **NO**
- デフォルト値: YES
- 例:
```
 logger.enable: YES
```

### logger.file_name

ログファイル名の指定。カンマ区切りで複数のファイルへ出力することもでき
る。プロセスIDを置き換える指定子 %p が利用可能。また、ファイル名
**stdout** とするとログを標準出力する。

- 指定: パスを含むファイル名
- デフォルト値: ./rtc%p.log
- 例:
```
 logger.file_name: /tmp/rtc%p.log
 logger.file_name: /tmp/rtc%p.log, stdout
```

### logger.date_format

ログに記載する日付・時刻のフォーマット指定。以下の strftime(3) に似た
フォーマット指定子を利用可能。時刻を指定しない場合、**No** または
**Disable** を指定する。

<table class="table-alt">
  <tr>
    <td>%a</td>
    <td>abbreviated weekday name</td>
  </tr>
  <tr>
    <td>%A</td>
    <td>full weekday name</td>
  </tr>
  <tr>
    <td>%b</td>
    <td>abbreviated month name</td>
  </tr>
  <tr>
    <td>%B</td>
    <td>full month name</td>
  </tr>
  <tr>
    <td>%c</td>
    <td>the standard date and time string</td>
  </tr>
  <tr>
    <td>%d</td>
    <td>day of the month, as a number (1-31)</td>
  </tr>
  <tr>
    <td>%H</td>
    <td>hour, 24 hour format (0-23)</td>
  </tr>
  <tr>
    <td>%I</td>
    <td>hour, 12 hour format (1-12)</td>
  </tr>
  <tr>
    <td>%j</td>
    <td>day of the year, as a number (1-366)</td>
  </tr>
  <tr>
    <td>%m</td>
    <td>month as a number (1-12). <br> Note: some versions of Microsoft Visual C++ may use values that range from 0-11.</td>
  </tr>
  <tr>
    <td>%M</td>
    <td>minute as a number (0-59)</td>
  </tr>
  <tr>
    <td>%p</td>
    <td>locale's equivalent of AM or PM</td>
  </tr>
  <tr>
    <td>%S</td>
    <td>second as a number (0-59)</td>
  </tr>
  <tr>
    <td>%U</td>
    <td>week of the year, sunday as the first day</td>
  </tr>
  <tr>
    <td>%w</td>
    <td>weekday as a decimal (0-6, sunday=0)</td>
  </tr>
  <tr>
    <td>%W</td>
    <td>week of the year, monday as the first day</td>
  </tr>
  <tr>
    <td>%x</td>
    <td>standard date string</td>
  </tr>
  <tr>
    <td>%X</td>
    <td>standard time string</td>
  </tr>
  <tr>
    <td>%y</td>
    <td>year in decimal, without the century (0-99)</td>
  </tr>
  <tr>
    <td>%Y</td>
    <td>year in decimal, with the century</td>
  </tr>
  <tr>
    <td>%Z</td>
    <td>time zone name</td>
  </tr>
  <tr>
    <td>%%</td>
    <td>a percent sign</td>
  </tr>
</table>

- 指定: /<name>.<kind>/<name>.<kind>/...
- デフォルト値: %b %d %H:%M:%S
- 例:
```
 logger.date_format: No
 logger.date_format: Disable
 logger.date_format: [%Y-%m-%dT%H.%M.%S%Z]     // W3C standard format
 logger.date_format: [%b %d %H:%M:%S]          // Syslog format
 logger.date_format: [%a %b %d %Y %H:%M:%S %Z] // RFC2822 format
 logger.date_format: [%a %b %d %H:%M:%S %Z %Y] // data command format
 logger.date_format: [%Y-%m-%d %H.%M.%S]
```

### logger.log_level

以下のログレベルを指定可能。

- SILENT
- FATAL
- ERROR
- WARN
- INFO
- DEBUG
- TRACE
- VERBOSE
- PARANOID

各ログレベルを指定した際に実際にログに記録されるログメッセージのレベ
ルは以下の通り。

<table class="table-alt">
  <tr>
    <td>SILENT</td>
    <td>completely silent</td>
  </tr>
  <tr>
    <td>FATAL</td>
    <td>includes (FATAL)</td>
  </tr>
  <tr>
    <td>ERROR</td>
    <td>includes (FATAL, ERROR)</td>
  </tr>
  <tr>
    <td>WARN</td>
    <td>includes (FATAL, ERROR, WARN)</td>
  </tr>
  <tr>
    <td>INFO</td>
    <td>includes (FATAL, ERROR, WARN, INFO)</td>
  </tr>
  <tr>
    <td>DEBUG</td>
    <td>includes (FATAL, ERROR, WARN, INFO, DEBUG)</td>
  </tr>
  <tr>
    <td>TRACE</td>
    <td>includes (FATAL, ERROR, WARN, INFO, DEBUG, TRACE)</td>
  </tr>
  <tr>
    <td>VERBOSE</td>
    <td>includes (FATAL, ERROR, WARN, INFO, DEBUG, TRACE, VERBOSE)</td>
  </tr>
  <tr>
    <td>PARANOID</td>
    <td>includes (FATAL, ERROR, WARN, INFO, DEBUG, TRACE, VERBOSE, PARA)</td>
  </tr>
</table>

**TRACE**, **VERBOSE**, **PARANOID** の各ログレベルは通常巨大なログファイルを生成します。**PARANOID**を指定すると、ログフォーマットが崩れる場合があります。

- 指定: (SILENT|FATAL|ERROR|WARN|INFO|DEBUG|TRACE|VERBOSE|PARANOID)
- デフォルト値: INFO
- 例:
```
 logger.log_level: DEBUG
```

### logger.clock_type

logger.clock_type 　オプションはログメッセージのタイムスタンプに使用するクロックのタイプを指定します。
現在以下の３種類のクロップタイプが使用可能です

- system: system clock [default]
- logical: logical clock
- adjusted: adjusted clock

論理時間クロック (logical time clock) を利用するには、プログラム中のどこかに以下のように指定してください。
```
 coil::ClockManager::instance().getClock("logical").settime()
```

- 設定: system, logical, adjusted
- デフォルト: system
- 例:
```
 logger.clock_type: system
```

### logger.escape_sequence_enable

このオプションはログ出力に色を付けるかどうかを指定する。logger.file_name: stdout と指定した場合、端末がエスケープシーケンスをサポートしていれば、ログ出力がカラーで表示される。ファイルへの出力に色を付けることはおすすめしない。

- 設定: YES or NO
- デフォルト: NO
- 例:
```
 logger.escape_sequence_enable: NO
```


## CORBAに関する設定

### corba.args

CORBAに与える引数を指定する。CORBA は実装毎に異なるコマンドラインオプショ
ンを持つ。通常コマンドライン引数は、CORBA の API である ORB_init() 関数
に与えられるが、このオプションは指定された文字列をこの ORB_init() 関数
に渡す。

- 指定: 文字列
- デフォルト: 空文字列
- 例:
```
 corba.args: -ORBInitialHost myhost -ORBInitialPort 8888
```

#### 指定例1

画像データなどをデータポートで送る際、1回に送信するデータサイズ約2MBを超える場合には注意が必要。
omniORBでは、giop(General Inter-ORB Protocol)で扱えるサイズはデフォルトで"2097152B(2MB)"であり
このサイズを超えるデータを送ろうとすると、giopの制限のため正しいデータを送ることができない。
corba.args オプションを利用して、最大サイズを変更することが可能である。この指定は、OutPort、InPort両方にて指定する必要がある。

```
 corba.args: -ORBgiopMaxMsgSize 3145728 # この行を追加
                                        # Maxサイズを3Mに指定
```

なお、corba.args に指定する以外に、環境変数を以下のように指定することでこの制限を緩和することができる。

```
  export ORBgiopMaxMsgSize=3145728
```

- （参考）(omniORB configuration and API) http://omniorb.sourceforge.net/omni41/omniORB/omniORB004.html


### corba.endpoint [非推奨]

このプションは corba.endpoints に置き換えられた。非推奨。


### corba.endpoints

CORBAにおいては、リモートのオブジェクトのIORと呼ばれる参照によりアクセ
スするが、IORには当該オブジェクトが動作するノードのアドレスとポート番号
が通常1セットのみ記述されている。OpenRTMが動作しているノードに2つ以上の
ネットワークインターフェースが存在する場合、IORに含まれるノードのアドレ
スとして意図しないアドレスが割り振られる場合がある。

これを解消するために、本オプションでCORBAで利用するネットワークのアドレ
スを指定することができる。**ホストアドレス:ポート番号** として指定するが、ポート番号は省略できる。

ORBの実装によっては、IORに複数のアドレスを含めることができる。ただし、
Java標準のCORBAであるJavaIDLにおいては、複数のアドレスを指定したIOR経由
で当該オブジェクトにアクセスする場合、動作が遅くなるなど問題も報告され
ているので注意が必要である。

**アドレス:ポート** の対を **,(カンマ)**で区切り複数指定することができ
る。特別な文字列として **all** を指定することで、ノードのすべてのアドレ
スをIORに含めることもできる。

- 指定: <host_addr>:<port>, <host_addr>:<port>, ... または all
- デフォルト: 空文字
- 例:
```
 corba.endpoints: 192.168.1.10:1111, 192.168.10.11:2222
 corba.endpoints: 192.168.1.10, 192.168.10.11
 corba.endpoints: all
```

corba.endpoints:

### corba.endpoints_ipv4: [readonly]

このパラメータは読み取り専用で、現在のプロセスが使用しているIPv4のエンドポイントがセットされます。
このパラメータを読むことで、現在使用しているエンドポイントを知ることができます。

- 設定: 読み取り専用
- デフォルト: なし
- 例:
```
 corba.endpoints_ipv6: [readonly]
```

### corba.endpoints_ipv6: [readonly]

このパラメータは読み取り専用で、現在のプロセスが使用しているIPv6のエンドポイントがセットされます。
このパラメータを読むことで、現在使用しているエンドポイントを知ることができます。

- 設定: 読み取り専用
- デフォルト: なし
- 例:
```
 corba.endpoints_ipv6: [readonly]
```

### corba.endpoint_property

このプションは、利用可能なエンドポイントのうち何番目のアドレスをIPv4, IpV6のいずれかのアドレスとして利用するかどうかについて指定する。

- 設定: {ipv4|ipv6}(<number of endpoint address>, ...), 
- デフォルト: なし
- 例:
```
 corba.endpoint_property: ipv4
 corba.endpoint_property: ipv4, ipv6(0)
 corba.endpoint_property: ipv6
 corba.endpoint_property: ipv4(0,1), ipv6(2,3)
```

### corba.nameservers

このプションはRTC等を登録するネームサーバを指定する。カンマ区切りで複数のネームサーバを指定することができる。指定したアドレスおよびポート番号にネームサーバがない場合でも特にエラーにはならず、存在するネームサーバにのみRTCの名前を登録する。
ポート番号が省略された場合はデフォルトのポート番号 2809 が使われます。

- 指定: <host_addr>:<port>, <host_addr>:<port>, ...
- デフォルト: localhost
- 例:
```
 corba.nameservers: openrtm.aist.go.jp:9876
 corba.nameservers: rtm0.aist.go.jp, rtm1.aist.go.jp, rtm2.aist.go.jp
 corba.nameservers: localhost
```

### corba.nameservice.replace_endpoint

ノードに複数のNICが存在する場合、ネームサーバ上に登録されるRTCのIORに含
まれるアドレスが、適切でない場合が存在する。例えば、あるノードが
192.168.0.10と192.168.1.10という2つのアドレスを持ち、192.168.0.1 および
192.168.1.1 に存在する2つのネームサーバ上に登録される場合、仮に
192.168.0.10 が当該ノードでデフォルトで利用されるネットワークインター
フェースだとすると、上記2つのネームサーバネームサーバに登録されるIORには、
192.168.0.10 のみが含まれる。このとき、192.168.1.0 のネットワークではネームサーバ上のIORは到達不可能なアドレスが記載された無意味なものとなる。

このオプションを指定すると、上記のケースのような場合、192.168.1.1 のネー
ムサーバに登録されるIORのアドレスを 192.168.1.10 に置き換える。

ただし、このオプション指定することによって、192.168.1.0 ネットワーク上
の他のノードからは、当該RTCのプロファイル等を利用することはできるが、ポー
トの接続等は行うことはできない。

- 指定: **YES** or **NO**
- デフォルト: NO
- 例:
```
 corba.nameservice.replace_endpoint: NO
```


### corba.alternate_iiop_addresses

このオプションは、代替IIOPアドレスをIORプロファイルに追加します。
IORにはサーバント(CORBAオブジェクトのサーバ)の追加のエンドポイント
を含めることができます。これは、"corba.endpoints"オプションとほぼ
同等ですが、実際にエンドポイントを作成しない点が異なります。
("corba.endpoints" オプションでは実際のエンドポイントを作ろうとし、
できなければエラーが返されます。) このオプションは単に代替のIIOPエ
ンドポイントアドレス情報をIORに追加します。

このオプションは、RTCをNATやルータの内部に配置する場合に使用します。
一般的には、プライベートネットワーク内のRTCはグローバルネットワー
ク上のRTCを接続することはできません。しかしながら、NATやルータのポー
トフォワーディングが適切に設定されていればグローバル側のRTCはプライ
ベートネットワークのRTCに接続することが可能です。

設定は以下のように行います。

1. NATやルータのポートフォワーディングを適切に設定します。
  - ここでは、グローバル側のポート2810をプライベート側のあるアドレ
スの2810へ転送するように設定します。
1. プライベート側のRTCのrtc.confを以下のように設定します。
```
  corba.nameservers: my.global.nameserver.com <- グローバル側のネームサーバを設定
  corba.endpoints: :2810 <- コンポーネントのポート番号
  corba.alternate_iiop_addresses: w.x.y.z:2810 <- ルータのグローバル側のIPアドレスとポート番号
```
1. グローバル側のRTCとプライベート側のRTCを起動

なお、RTSystemEditorでは、プライベート側のRTCへのアクセスが極端に
遅くなる場合があります。これはJavaのIOR追加プロファイル機能の実装
が十分でないため、プライベート側に到達するのに時間がかかるためと考
えられます。rtshellなどを利用すると、接続にかかる時間を減らすこと
ができます。また、RTSystemEditorやrtshellでの接続に時間がかかった
場合でも、一旦接続したポート間の通信速度は通常とほとんど変わりませ
ん。

- 指定: address:port
- デフォルト: 未指定
- 例:
```
 corba.alternate_iiop_addresses: addr:port
```

## manager に関する設定

### manger.name

managerの名前。マネージャがネームサーバで登録される際には、ここで設定した名前で登録される。
この "manager.name" は、ストリング化されたCORBAオブジェクト名でマスター/スレーブマネージャーをグループ化するために使用されます。 "manager.name" が "manager" に設定され、マネージャーがマスターである場合、オブジェクト参照は次のように配置されます。

```
 corbaloc::<hostname>:2810/manager 
```

また、他のスレーブマネージャは以下のストリング化されたIORを持ちます。
```
 corbaloc::<hostname>:<port_number>/manager
```

- 指定: ネームサーバ等に登録可能な任意の名前
- デフォルト値: manager
- 例:
```
 manager.name: manager
```

### manager.instance_name

マネージャのインスタンス名。

この "manager.instance_name" は、ネームサービス登録時のマネージャーの名前に使用されます。 通常、マスターマネージャーの参照は、"manager|mgr" という名前でネームサーバーに登録されます。 このオプションが "foobar" に設定されている場合、登録されたマースターマネージャー名は "foobar|mgr" になります。
- 設定: manager の任意の名称文字列
- デフォルト: manager
- 例:
```
 manager.instance_name: manager
```

### manager_naming_formats

マネージャをネームサーバに登録する際のフォーマットを指定する。以下の
**%**で始まる指定子を利用することができる。

<table class="table-alt">
  <tr>
    <th>指定子</th>
    <th>意味</th>
  </tr>
  <tr>
    <td>%n</td>
    <td>マネージャ名</td>
  </tr>
  <tr>
    <td>%h</td>
    <td>ホスト名</td>
  </tr>
  <tr>
    <td>%M</td>
    <td>マネージャ名</td>
  </tr>
  <tr>
    <td>%p</td>
    <td>マネージャのプロセスID</td>
  </tr>
</table>

- 指定: /<name>.<kind>/<name>.<kind>/...
- デフォルト値: %h.host_cxt/%n.mgr
- 例:
```
 manager.name: %h.host_cxt/%n.mgr
```

### manager.is_master

当該プロセスをマスターマネージャにするかどうか？コマンドラインオプショ
ン **-d** を指定すると、この値が NO に設定されていてもマスターマネージャ
になる。

- 指定: **YES** or **NO**
- デフォルト値: NO
- 例:
```
 manager.is_master: NO
```

### manager.corba_servant

マネージャのCORBAサーバントを起動するかどうかの設定。YES を設定すると、
マネージャのCORBAサーバントが起動するため、リモートからマネージャの操作
が可能になる。NO の場合には、CORBAサーバントが起動しないため、マネージャ
のCORBA経由での操作はできなくなる。

- 指定: **YES** or **NO**
- デフォルト値: YES
- 例:
```
 manager.corba_servant: YES
```

### corba.master_manager

マスターマネージャのアドレスとポート番号。マスターマネージャは、
corbaloc 形式のURL指定でアクセス可能であるが、その際に使用するポート番
号を指定する。また、スレーブマネージャは、ここで指定されたマスターマネー
ジャを自身のマスターマネージャとして解釈、起動時にマスターマネージャに
アクセスしネゴシエーションを行う。

- 指定: <host_name>:<port>
- デフォルト: localhost:2810
- 例:
```
 corba.master_manager: localhost:2810
```

### manager.update_master_manager.enable

スレーブマネージャへのマスターマネージャの登録の自動更新

このオプションは、スレーブマネージャで有効です。 スレーブマネージャーは、自分自身をマスターマネージャーに登録する必要があります。 このオプションを "YES"に設定すると、スレーブマネージャーは定期的にマスターマネージャーに登録します。 「NO」を設定すると、スレーブマネージャは、起動時に一度だけマスタマネージャに登録されます。

- 設定: YES/NO (Read/Write)
- デフォルト: YES
- 例:
```
 manager.update_master_manager.enable:YES
```

### manager.update_master_manager.interval

スレーブマネージャのマスターマネージャへの登録更新周期

このオプションは、corba.update_master_manager.enableに関連します。
「corba.update_master_manager.enable」オプションがYESに設定されている場合、更新間隔はこのオプションによって設定されます。 デフォルトの間隔は10秒です。
- 設定: seconds (Read/Write)
- デフォルト: 10.0
- 例:
manager.update_master_manager.interval: 10.0

### manager.components.naming_policy

このオプションは、RTCの命名（番号付け）ポリシーを指定します。 RTCインスタンスが作成されると、コンポーネントタイプ名（type_name）に次のように増分番号が付けられた名前が割り当てられます。

```
 <type_name> <number>
 example: ConsoleOut0、ConsoleOut1、ConsoleOut2、...
```

デフォルトでは、同じプロセスの同じタイプのコンポーネントには0から順番に番号が付けられるため、異なるプロセスまたは異なるノード（コンピューター）で作成されたRTCは同じ名前を持つ場合があります。これらのRTCがネームサーバー（ns）に登録されると、同じパスと同じ名前のRTCが互いのオブジェクト参照を上書きし、目的のRTCにアクセスできなくなります。したがって、2つのポリシーが提供されます。各ノードに一意の番号を割り当てる「node_unique」とネームサーバーに一意の番号を割り当てる「ns_unique」です。

デフォルトでは、次の3つのオプションを指定できます。

- process_unique：プロセス内で一意の名前（番号）を指定します
- node_unique：ノード内で一意の名前（番号）を指定します
- ns_unique：ネームサーバーで一意の名前（番号）を指定します

ポリシーはユーザーが拡張できます。

- 設定：読み取り/書き込み、{process_unique、node_unique、ns_unique}
- デフォルト：process_unique
- 例：
```
 manager.components.naming_policy: process_unique
```

### manager.components.precreate

事前のコンポーネント作成

このオプションは、マネージャーのイベントループを開始する前に事前に作成するコンポーネントの名前（モジュール名）を指定します。 コンポーネントのファクトリーは、「manager.module.preload」オプションで登録するか、マネージャーに静的にリンクする必要があります。

- 設定: Read/Write, <component class name>, ...
- デフォルト: None
- Example:
```
 manager.components.precreate: ConsoleIn, ConsoleOut, SeqIn, SeqOut
```

### manager.components.preconnect
&aname(preconnect);

事前の接続生成。このオプションは、マネージャーイベントループを開始する前に作成するコネクタを指定します。
ターゲットコンポーネントとポートは、"manager.components.precreate" オプションを使用して事前に作成されている必要があります。
ポートは、"<comp0>.<Port0>?port=<comp1>.<port1>＆<option_key>=<option_value>＆..." の形式で指定されます。
dataflow_type または interface_type が指定されていない場合、"dataflow_type = push", "interface_type = corba_cdr" が自動的に指定されます。

- 設定: <comp0>.<Port0>?port=<comp1>.<port1>&<option_key>=<option_value>&...
- デフォルト: none
- Example:
```
 manager.components.preconnect: ConsoleIn0.out?port=ConsoleOut0.in& \ 
                                                    dataflow_type=push&interface_type=corba_cdr, \ 
                                                    SeqIn0.octet?port=SeqOut0.octet& \ 
                                                    dataflow_type=push&interface_type=direct
```

### manager.components.preactivation
&aname(preactivation);

以前のコンポーネントのアクティブ化。このオプションは、マネージャーのイベントループを開始する前に、事前にアクティブにするコンポーネントの名前（モジュール名）を指定します。 ターゲットコンポーネントは、あらかじめ manager.components.precreate オプションで作成しておく必要があります。

- 設定: Read/Write, <component class name>, ...
- デフォルト: None
- Example:
```
 manager.components.preactivation: ConsoleIn0, ConsoleOut0
```

### manager.cpu_affinity

このオプションは、マネージャのプロセスを特定のCPUにバインドする。
オプション引数は、カンマで区切られた1つ以上のCPU IDでなければならない。
CPU IDは0から始まり、最大値はCPUコア数-1となる。
もし不正なCPU IDが指定された場合、このプロセスはすべてのCPUを利用するよう設定される。

- 指定: バインドするCPU IDをカンマ区切りで指定
- デフォルト: なし
- 例:
```
 manager.cpu_affinity: 0,1
```


## マネージャのライフサイクルオプション

### manager.shutdown_on_nortcs:

プロセス上にRTCが一つもなくなった場合、すなわち同一プロセス上のRTCの最
後の1つが終了した場合に、マネージャをシャットダウンし当該プロセスを終了
させるかどうかを指定する。YES の場合には、RTCが一つもなくなった時点でプ
ロセスが終了する。NOの場合は、RTCが一つもない状態でもマネージャ、プロセ
スともに動き続ける。

- 指定: **YES** or **NO**
- デフォルト: YES
- 例:
```
 manager.shutdown_on_nortcs: YES
```

### manager.shutdown_auto

プロセス内のRTCの有無を一定時間ごとに調べ、RTCがない場合には、マネージャ
およびプロセスをシャットダウンするかどうかを設定する。YESの場合、RTCが
一つもなければ、マネージャおよびプロセスは自動的にシャットダウンされる。
NOの場合、RTCが一つもなくともマネージャおよびプロセスが動作し続ける。

manager.shutdown_on_nortcs との違いは、シャットダウンのトリガが、
manager.shutdown_on_nortcs ではRTCの削除であるのに対して、
manager.shutdown_auto は時間となっている点である。
- 指定: **YES** or **NO**
- デフォルト: YES
- 例:
```
 manager.shutdown_auto: YES
```

### manager.auto_shutdown_duration

プロセス内のRTCの有無調べる周期。単位は秒。上記の manager.shutdown_auto が
YESに設定されている場合、このオプションで設定された周期でRTCの有無を確認
しにいく。

- 指定: 数値 (単位[s])
- デフォルト: 10.0
- 例:
```
 manager.auto_shutdown_duration: 10.0
```

### manager.termination_waittime

マネージャ終了ウェイト時間指定。 このオプションは、マネージャーへの終了要求から実際の終了スレッドが実行を開始するまでの時間を指定します。 単位は秒です。 通常、このオプションを指定または変更する必要はありません。 ただし、CORBAの終了処理が正常に終了する前に別の終了処理を実行して例外が発生した場合は、この時間を調整することで問題が解決する場合があります。

- 設定: Read/Write, duration [s]
- デフォルト: 0.5
- 例:
manager.termination_waittime: 0.5

## モジュール管理に関するオプション

### manager.modules.load_path

マネージャはこのオプションで指定されたサーチパスリストからモジュールを
探索する。パスはカンマ区切りで列挙する。パスのデリミタは、UNIXでもWindowsでも / である。

- 指定: /dir_name0/dir_name1/..., /dir_name0/dir_name1/...
- デフォルト値: ./
- 例:
```
 manager.modules.load_path: C:/Program Files/OpenRTM-aist
 manager.modules.load_path: /usr/lib, /usr/local/lib,       \
                            /usr/local/lib/OpenRTM-aist/libs
```

### manager.modules.preload:

マネージャは起動時に予めローダブルモジュールをロードすることができる。
このオプションで指定されたローダブルモジュール
を、**manager.modules.load_path** で指定されたサーチパスから探し出す。
もし、**manager.modules.abs_path_allowed** で YES が指定されていれば、
ローダブルモジュールを絶対パスで指定することもできる。

- 指定: <module_name>.dll, <module_name>.dll, ...
- デフォルト値: 空
- 例:
```
 manager.modules.preload: ConsoleIn.dll, ConsoleOut.dll
 manager.modules.preload: ConsoleIn.so, ConsoleOut.so
 manager.modules.abs_path_allowed: YES
 manager.modules.preload: /usr/lib/OpenRTM-aist/ConsoleIn.so
```

### manager.modules.abs_path_allowed

モジュールの絶対パス指定許可フラグ。もしこのオプションがYESの場合、モジュールの接待パス指定が許可される。

- 指定: **YES** or **NO**
- デフォルト値: YES
- 例:
```
 manager.modules.abs_path_allowed: YES
```

### manager.modules.search_auto

モジュールの自動検索機能を有効にする。
このオプションは、RTCロード可能モジュールを自動的に検索するかどうかを指定します。 このオプションが "YES" に設定されている場合、RTCインスタンス化がマネージャーに要求されると、ターゲットRTCロード可能モジュール（DLLなど）が自動的に検索され、モジュール検索パスからロードされて、コンポーネントがインスタンス化されます。 NOの場合、ターゲットRTCのロード可能モジュールを事前にロードする必要があります。

- 設定: Read/Write, YES / NO
- デフォルト: YES
- 例:
```
 manager.modules.search_auto: YES
```

### manager.preload.modules: none
CORBA初期化前にロードするモジュールリスト

このオプションは、CORBAの初期化前にロードするモジュールを指定します。 一部の機能を実装するロード可能なモジュールは、CORBAの初期化前にロードする必要があり、そのようなモジュールはこのオプションで指定されます。 モジュールの指定方法はmanager.modules.preloadと同じです。

- 設定: <module_name>(.<extention>) (init_func_name), ...
- デフォルト: none
- Example: 
```
   manager.preload.modules: SSLTransport.dll
   manager.preload.modules: SSLTransport.py
   manager.preload.modules: SSLTransport
   manager.preload.modules: \
   C:\\Python27\\Lib\\site-packages\\OpenRTM_aist\\ext\\SSLTransport
```

<!-- # -->
<!-- # The following options are not implemented yet.  -->
<!-- # -->
<!-- # manager.modules.config_ext: -->
<!-- # manager.modules.config_path: -->
<!-- # manager.modules.detect_loadable: -->
<!-- # manager.modules.init_func_suffix: -->
<!-- # manager.modules.init_func_prefix: -->
<!-- # manager.modules.download_allowed: -->
<!-- # manager.modules.download_dir: -->
<!-- # manager.modules.download_cleanup: -->
<!-- # -->

## マネージャの言語サポートオプション

### manager.supported_languages

マスターマネージャは、リモートアプリケーションなどからの要求に応じて、
スレーブマネージャおよびRTCを起動する。スレーブマネージャは、C++言語版
だけでなく、Java版、Python版などの可能性もある。


- 指定: C++, Java, Python 等の言語をカンマ区切りで指定
- デフォルト: C++, Java, Python3
- 例:
```
 manager.supported_languages: C++, Python3, Java
```

### manager.modules.`<lang>`.suffixes

言語ごとのRTCモジュールの拡張子。
このオプションは、ロード可能なモジュールRTCの拡張を指定します。

```
  manager.modules.<lang>.suffixes
```

`<lang>`の部分はmanager.supported_languagesで指定する必要があります。 "."（ドット）は不要です。 C ++、Python / Python3、Java言語にはそれぞれ適切なデフォルトの拡張子が指定されているため、通常は設定は必要ありません。

- 指定: 共有オブジェクトの拡張子名
- デフォルト:
  - Windows: dll
  - Linux等: so
  - Mac OS X: dylib
- 例
```
 manager.modules.C++.suffixes: dll
 manager.modules.C++.suffixes: so
 manager.modules.C++.suffixes: dylib
```

### manager.modules.`<lang>`.manager_cmd

言語ごとのマネージャプログラム名。
このオプションは、各言語の実行可能マネージャーの名前を指定します。 マスターマネージャーがRTCのインスタンス化を要求されると、スレーブマネージャーが実行され、RTCがスレーブマネージャープロセスでインスタンス化されます。 C++版のRTCはC++版のマネージャ（rtcd）を使用し、Python版RTCはPython版マネージャ（rtcd_python）を使用します。 コマンド検索パスのデフォルトの実行可能ファイルは、C ++、Python / Python3、およびJava言語に対してそれぞれ指定されます。通常、設定は必要ありません。

- 指定: マネージャのコマンド名
- デフォルト:
  - C++: rtcd
  - Python: rtcd_python
  - Java: rtc_java
- 例
```
 manager.modules.C++.manager_cmd: rtcd
 manager.modules.Python.manager_cmd: rtcd_python
 manager.modules.Java.manager_cmd: rtcd_java
```

### manager.modules.`<lang>`.profile_cmd

言語ごとのプロファイル取得コマンド名。
このオプションは、RTCプロファイルを取得するコマンドであるプロファイル実行可能ファイルの名前を言語ごとに指定します。 既存のロード可能なモジュールからRTCを検索する場合、マスターマネージャーはプロファイルコマンドを実行して、ロード可能なモジュールから各コンポーネントのプロファイルを取得します。 C++版RTCはC++版プロファイルコマンド（rtcprof）を使用し、PythonバージョンRTCはPythonバージョンマネージャ（rtcprof_python）を使用します。 コマンド検索パスは、指定された実行可能ファイルに設定する必要があります。 C++、Python / Python3、およびJava言語にはそれぞれ適切なデフォルトの実行可能ファイルが指定されているため、通常は設定は必要ありません。

- 指定: プロファイル取得コマンド名
- デフォルト:
  - C++: rtcprof
  - Python: rtcprof_python
  - Python3: rtcprof_python3
  - Java: rtc_java
- 例
```
 manager.modules.C++.profile_cmd: rtcprof
 manager.modules.Python.profile_cmd: rtcprof_python
 manager.modules.Java.profile_cmd: rtcprof_java
```

### manager.modules.`<lang>`.load_paths

言語ごとのRTCモジュールロードパス。
このオプションは、各言語のロード可能なモジュールRTCのロードパスを指定します。 マスターマネージャーがどこかからRTCを検索する場合、指定されたロードパスが使用されます。

- 指定: RTCモジュールロードパス。
- デフォルト:
  - C++: ./
  - Python: ./
  - Java: ./
- 例
```
 manager.modules.C++.load_paths: ./, /usr/share/openrtm-1.2/components/cxx
 manager.modules.Python.load_paths: ./, /usr/share/openrtm-1.2/components/python
 manager.modules.Python3.load_paths: ./, /usr/share/openrtm-1.2/components/python3
 manager.modules.Java.load_paths: ./, /usr/share/openrtm-1.2/components/java
```

<!-- Timer configuration -->

## タイマに関する設定

### timer.enable

タイマ機能を有効/無効にする。タイマを無効にするとタイマを利用している機
能、例えばネームサーバの定期的確認と再登録等が無効になる。

- 指定: **YES** or **NO**
- デフォルト値: YES
- 例:
```
 timer.enable: YES
```

### timer.tick

タイマの精度を指定する。

- 指定: タイマの精度を [s] で指定する。
- デフォルト値: 0.1 [s], (= 100ms)
- 例:
```
 timer.tick: 1.0
```

## 実行コンテキストオプション

### exec_cxt.periodic.type

デフォルトの実行コンテキストのタイプ。
デフォルトでは以下の実行コンテキストが指定可能。

- PeridicExecutionContext: デフォルトのEC。最も一般的なECで指定しなければこのECが利用される。
- ExtTrigExecutionContext:   外部トリガにより駆動されるEC。デフォルトで組み込み済み。
- OpenHRPExecutionContext:  外部トリガにより並列的に駆動されるEC。デフォルトで組み込み済み。OpenHRP3と一緒に利用される。
- SimulatorExecutionContext: 外部トリガにより並列的に駆動されるEC。デフォルトで組み込み済み。Choreonoidと一緒に利用される。
- RTPreemptEC: （ソフト）リアルタイム実行コンテキスト。LinuxのRT-preemptiveカーネルと一緒に利用される。

- 指定: デフォルトの実行コンテキスト名
- デフォルト値: PeriodicExecutionContext
- 例:
```
 exec_cxt.periodic.type: PeriodicExecutionContext
 exec_cxt.periodic.type: ArtExecutionContext
```

### exec_cxt.periodic.rate

デフォルトの実行コンテキストの周期。このオプションはシステム全体のECの周期を指定する。RTCが明示的にECの周期を指定しない場合、この周期が利用される。

- 指定: デフォルトの実行コンテキスト周期を [Hz] で指定する
- デフォルト値: 1000
- 例:
```
 exec_cxt.periodic.rate: 100
```

### exec_cxt.sync_transition
### exec_cxt.sync_activation
### exec_cxt.sync_deactivation
### exec_cxt.sync_reset

RTCはアクティブ化、非アクティブ化、およびリセットにより、状態が遷移します。 一部の実行コンテキストは、メインロジックを異なるスレッドで実行します。 これらのフラグがYESに設定されている場合、アクティブ化、非アクティブ化、およびリセットは同期して実行されます。 つまり、これらのフラグがYESの場合、状態遷移の完了後にはアクティブ化/非アクティブ化/リセット操作の呼び出しから戻っていることが保証されます。

"sync_transition" は、同期遷移フラグを他のすべての同期遷移フラグ (sync_activation / deactivation / resetting) に一括設定します。

- 設定: YES or NO
- デフォルト：YES（デフォルト設定推奨）
- 例:
```
 exec_cxt.sync_transition: YES
 exec_cxt.sync_activation: YES
 exec_cxt.sync_deactivation: YES
 exec_cxt.sync_reset: YES
```

### exec_cxt.transition_timeout
### exec_cxt.activation_timeout
### exec_cxt.deactivation_timeout
### exec_cxt.reset_timeout

動機遷移時のタイムアウト指定。
動機遷移フラグがYESに設定されているとき、以下のタイムアウトの設定が有効になります。"timeout_transition" オプションが設定された場合、他の activation/deactivation/reset のタイムアウト値が一括で設定されます。

- 設定: Read/Write, seconds [s]
- デフォルト：0.5 [s]
- 例:
```
 exec_cxt.transition_timeout: 0.5
 exec_cxt.activation_timeout: 0.5
 exec_cxt.deactivation_timeout: 0.5
 exec_cxt.reset_timeout: 0.5
```

## SDO サービスオプション

### sdo.service.provider.available_services

このパラメータは現在利用可能なSDOサービス（プロバイダ）のリストが入る。

- 設定: 読み取り専用, `<sdo service0>`, `<sdo service1>`, ... 
- デフォルト: None
- 例:
```
 sdo.service.provider.available_services: <利用可能なSDOサービス（プロバイダ）のリスト>
```

### sdo.service.provider.enabled_services

このオプションは有効にSDOサービス（プロバイダ）を指定する。
特定のサービスをサービス型名で指定するか、全てを有効にする場合は "ALL" を指定する。

- 設定: 読み書き, `<sdo service0>`, `<sdo service1>`, ... または ALL
- デフォルト: ALL
- 例:
```
 sdo.service.provider.enabled_services: <有効にするSDOサービスのリスト>
```

### sdo.service.provider.providing_services

このオプションは現在インスタンス化され提供されているSDOサービス（プロバイダ）が入る。

- 設定: 読み取り専用, `<sdo service0>`, `<sdo service1>`, ... 
- デフォルト: None
- 例:
```
 sdo.service.provider.enabled_services: <現在インスタンス化されているDOサービスのリスト>
```

### sdo.service.consumer.available_services

このパラメータは現在利用可能なSDOサービス（コンシューマ）のリストが入る。

- 設定: 読み取り専用, `<sdo service0>`, `<sdo service1>`, ... 
- デフォルト: None
- 例:
```
 sdo.service.consumer.available_services: <利用可能なSDOサービス（コンシューマ）のリスト>
```


### sdo.service.consumer.enabled_services

このオプションは使用するSDOサービス（コンシューマ）を指定する。
特定のサービスをサービス型名で指定するか、全てを有効にする場合は "ALL" を指定する。

- 設定: 読み書き, `<sdo service0>`, `<sdo service1>`, ... または ALL
- デフォルト: ALL
- 例:
```
 sdo.service.consumer.enabled_services: <有効にするSDOサービスのリスト>
```


## ローカルサービスオプション

### manager.local_service.modules

ローカルサービスモジュールをロードする。
同一プロセス内のRTCに対してユーザ定義のサービを提供するためにローカルサービスメカニズムが提供されています。
コンポーネントは、ローカルサービスをマネージャから取得したり、使用したりすることができます。
例えば、この仕組を利用すると、複数のRTC間で共通のリソースにアクセスしたりできます。

ローカルサービスモジュールは、しばしばコンポーネントのロードやインスタンス化よりも前に初期化されなければいけません。
そのため、ローカルサービスモジュールはこのオプションで指定して事前にロードと初期化を行う必要があります。

- 設定: Read/Write, モジュールロードパス
- デフォルト：None
- 例:
manager.local_service.modules: IEEE1394CameraService.so

### manager.local_service.enabled_services

有効にするローカルサービスを指定する。デフォルトではすべてのローカルサービスがアクティブ化および利用可能に設定されます。このオプションは有効にする特定のローカルサービスを指定します。

- 設定: Read/Write, 有効にするローカルサービス名
- デフォルト：None
- 例:
manager.local_service.enabled_services: IEEE1394CameraService


## ポートの設定


ポートの設定は以下の**port.inport.dataport**、**port.{ポート型}.{ポート名}**、**{カテゴリ名}.{インスタンス名}.port.inport.{ポート名}.{設定項目}**の文字列の後に項目名を指定することで設定できます。
接続時のコネクタプロファイルで同じ設定をしている場合は、コネクタプロファイルの設定で上書きするのでrtc.confの設定は無効になります。

```
 port.{ポート型}.dataport.{設定項目}: {設定値}
 port.{ポート型}.{ポート名}.{設定項目}: {設定値}
 {カテゴリ名}.{インスタンス名}.port.inport.{ポート名}.{設定項目}: {設定値}
```

### allow_dup_connection
2つのポートの間で複数のコネクタを生成しないようにします。
NO(不許可)にした場合、ポートAとポートBで接続した場合、もう一度connect関数を実行してポートAとポートBを接続しようとしてもPRECONDITION_NOT_METの値を返して接続失敗になります。

- 設定: 多重のコネクタを許可か不許可かの設定
- デフォルト：NO
- 例:
```
 port.inport.in.allow_dup_connection: NO
```

### fan_in
InPortのコネクタの最大数を指定する。例えば100に設定すると、InPort Aと接続したポートの数が100以上になると、connect関数実行時にPRECONDITION_NOT_METを返して接続失敗になります。

- 設定: InPortのコネクタの最大数を設定
- デフォルト：100
- 例:
```
 port.inport.in.fan_in: 100
```


### fan_out
OutPortのコネクタの最大数を指定する。例えば100に設定すると、OutPort Aと接続したポートの数が100以上になると、connect関数実行時にPRECONDITION_NOT_METを返して接続失敗になります。

- 設定: OutPortのコネクタの最大数を設定
- デフォルト：100
- 例:
```
 port.outport.out.fan_out: 100
```


### buffer.length
InPort、OutPortのリングバッファのバッファサイズを指定します。OutPortの場合はサブスクリプション型がNew、Periodic型の時に有効です。InPortは常に有効です。

- 設定: バッファサイズを設定
- デフォルト：8
- 例:
```
 port.inport.in.buffer.length: 8
```


### buffer.write.full_policy
InPort、OutPortのリングバッファの上書き時のポリシーを指定します。OutPortの場合はサブスクリプション型がNew、Periodic型の時に有効です。InPortは常に有効です。

- 設定: 上書き時のポリシー
- デフォルト：overwrite
- 例:
```
 port.inport.in.buffer.write.full_policy: block
 port.inport.in.buffer.write.full_policy: do_nothing
```

### buffer.read.empty_policy
InPort、OutPortのリングバッファの読み込み時のポリシーを指定します。OutPortの場合はサブスクリプション型がNew、Periodic型の時に有効です。InPortは常に有効です。

- 設定: 読み込み時のポリシー
- デフォルト：readback
- 例:
```
 port.inport.in.buffer.read.empty_policy: block
 port.inport.in.buffer.read.empty_policy: do_nothing
```



