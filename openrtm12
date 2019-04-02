## OpenRTM-aist 1.2新機能詳細

### マネージャ起動時にポートを接続する機能

rtc.confに以下のように記述することで、起動時にデータポート、サービスポートを接続できる。

```
manager.components.preconnect: {RTC1}.{port1}?port={RTC2}.{port2}&{option1}={value}, ....
```

例：

```
manager.components.preconnect: ConsoleIn.out?port=ConsoleOut.in&dataflow_type=push&interface_type=corba_cdr, SeqIn.octet?port=SeqOut.octet&dataflow_type=push&interface_type=direct
```


### マネージャ起動時にコンポーネントをアクティベーションする機能

rtc.confに以下のように記述することで、起動時にRTCをアクティベートできる。

```
manager.components.preactivation: {RTC1}, {RTC2}
```

例：

```
manager.components.preactivation: ConsoleIn0, ConsoleOut0
```

### CORBA_RTCUtil：コンポーネント操作関数群の導入

RTC、実行コンテキスト、ポート、コンフィギュレーションパラメータ操作のための関数群を導入。
使用できる関数は以下を参照。

- [CORBA_RTCUtil.h](https://github.com/OpenRTM/OpenRTM-aist/blob/master/src/lib/rtm/CORBA_RTCUtil.h)


### トピックベースのポート接続機能
rtc.confで以下のようにトピック名を設定することで、同一トピック名のポートを自動検索して接続する機能。

```
port.corbaport.{serviceport_name}.rendezvous_point: {topic_name}
port.inport.{inport_name}.subscribe_topic: {topic_name}
port.outport.{outport_name}.publish_topic: {topic_name}
```


例：
```
port.inport.in.subscribe_topic: test_topic
port.outport.out.publish_topic: test_topic
```

### 共有メモリ通信データポート(shared_memory型インターフェース)
データポートでデータを共有メモリにより転送する機能。
コネクタのインターフェース型に`shared_memory`を設定することで使用できる。

```
manager.components.preconnect: ConsoleIn.out?port=ConsoleOut.in&interface_type=shared_memory
```

RTSystemEditorを使用する場合は以下の項目で設定する。

![image](https://user-images.githubusercontent.com/6216077/55385787-e3e66e00-5568-11e9-86a0-a569117d6f57.png)


### 同一プロセス内通信のデータ転送を変数で渡すダイレクト接続データポート(direct型インターフェース)
同一プロセス内のデータポート通信で変数によりデータを渡す機能。
コネクタのインターフェース型に`direct`を設定することで使用できる。

```
manager.components.preconnect: ConsoleIn.out?port=ConsoleOut.in&interface_type=direct
```

RTSystemEditorを使用する場合は以下の項目で設定する。

![image](https://user-images.githubusercontent.com/6216077/55385933-3cb60680-5569-11e9-90ca-95602603c6f1.png)

### OpenSSLによるセキュアな通信機能
OpenSSLによりCORBAの通信を暗号化する機能(SSLIOP)の利用。
rtc.confに以下のように記述することで利用可能。

ただし、証明書や秘密鍵についてはOpenSSLにより生成しておく必要がある。

```
corba.ssl.certificate_authority_file: root.crt
corba.ssl.key_file: server.pem
corba.ssl.key_file_password: password
manager.modules.load_path: C:\\Program Files\\OpenRTM-aist\\1.2.0\\bin\\vc141
manager.preload.modules: SSLTransport.dll
```

デフォルトの状態ではIIOPとSSLIOPの2つのポートが利用可能になっているため, RTSystemEditor等から操作可能である。
IIOPを無効にしてSSLIOPのみで通信を行う場合は、以下の環境変数を設定する。

```
set ORBclientTransportRule=* ssl
```

この場合はRTSystemEditorからの操作はできなくなるため、別途ツールを作成する必要がある。


### 名前付けポリシー機能の拡張(同一ネームサーバー、同一ノードで独自のインスタンス名を設定する)
1.1.2以前ではネームサーバーに登録しようとしているRTCと同じインスタンス名のRTCが存在する場合に登録を上書きしていましたが、適切な番号順に設定できるようになりました。

ネームサーバーで独自のインスタンス名を付けるためにはrtc.confで以下の設定を行います。

```
manager.components.naming_policy: ns_unique
```

同一ノード内で独自のインスタンスを設定する機能は、同一のマスターマネージャに登録されているスレーブマネージャ内で起動したRTCと被らない名前付けを行う機能です。
このため必ずマスターマネージャの起動が必要です。

rtc.confで以下のように記述することで機能を使用できます。

```
naming.type: manager
manager.components.naming_policy: node_unique
```


### rtcloc形式のコンポーネント指定方法(マスターマネージャに登録されたスレーブマネージャからコンポーネントを名前で検索)
別プロセスで起動したRTCのリファレンスを`rtcloc`形式という文字列で取得する。
この機能はマスターマネージャを利用するため、マスターマネージャの起動が必要である。

この機能の利用のためにはrtc.confで`naming.type`のオプションを設定する必要がある。

```
naming.type: manager
```

`rtcloc`形式は以下のように記述する。

```
rtcloc://{マスターマネージャのアドレス}/{RTCのカテゴリ名(省略可)}/{RTCのインスタンス名}
```

この機能を利用することで、以下のように遠隔のRTCをアクティブ化したり、

```
manager.components.preactivate: rtcloc://localhost:2810/example/TestComp20, TestComp10
```

ポートを接続するということができる。

```
manager.components.preconnect: rtcloc://localhost:2810/example/TestComp20.in?port=TestComp10.out
```


### rtcname形式のコンポーネント指定方法(ネームサーバーに登録されたコンポーネントを名前で検索)
別プロセスで起動したRTCのリファレンスを`rtcname`形式という文字列で取得する。
この機能にはネームサーバーを利用する。

`rtcname`形式は以下のように記述する。

```
rtcname://{ネームサーバーのアドレス}/{ネームサーバーでのRTCのパス}
```


この機能を利用することで、以下のように遠隔のRTCをアクティブ化したり、

```
manager.components.preactivate:rtcname://localhost:2809/test.host_cxt/TestComp20, TestComp10
```

ポートを接続するということができる。

```
manager.components.preconnect:rtcname://localhost:2809/test.host_cxt/TestComp20.in?port=TestComp10.out()
```


### デフォルトでデータポートの二重接続を許可しない機能
デフォルトでデータポートを二重に接続できなくなりました。
二重の接続を許可するためには、rtc.confに以下の記述がポートごとに必要です。

```
port.inport.<InPortName>.allow_dup_connection: YES
port.outport.<OutPortName>.allow_dup_connection: YES
```



### omniidl shortcutの利用
同一プロセス内の操作呼び出しの処理時間短縮のため、同一プロセス内で関数を直接呼び出すShortCut機能を利用するようにしました。

### LogstreamBase：ロガー機能の拡張
1.1.2以前ではロガーはファイル出力、標準出力のみしか使用できませんでしたが、様々なロガーを拡張可能になりました。
[Fluent Bit](https://github.com/OpenRTM/OpenRTM-aist/tree/svn/RELENG_1_2/src/ext/logger/fluentbit_stream)によるロガーがサンプルとして実装されています(ただし、C++版はLinuxのみの対応)。


注：LogstreamBaseは2.0で大幅に仕様が変わる予定です。1.2で作成した独自のロガーは使用できなくなります。


### コンポーネントオブザーバのデータ入出力検知機能
コンポーネントオブザーバーというRTC側からRTSystemEditor等に状態等を通知する機能を導入しました。

### モジュール探索パスのサブディレクトリのモジュールを探索する機能
rtc.confで以下のようにモジュール探索パスを設定した場合に、1.1.2以前では設定したパス直下からしかモジュールを探索しませんでしたが、サブディレクトリも探索するようになりました・

```
manager.modules.load_path: ./
```

### ログファイルのエスケープシーケンスをデフォルトで無効にする機能
1.1.2ではログファイルに文字に色を付けるためのエスケープシーケンスが強制的に付加されたためテキストエディタで開くと非常に見づらい問題がありましたが、1.2ではデフォルトでエスケープシーケンスを付加する機能は無効にして設定で有効ににできるようになりました。
有効にするためには、rtc.confに以下のように記述します。


```
logger.escape_sequence_enable: YES
```


### RT System Editorにネームサーバー起動ボタン、終了ボタンを導入
RT System Editor上でネームサーバーの起動、終了ができるようになりました。

以下のボタンで起動します。起動済みの場合は再起動します。

![image](https://user-images.githubusercontent.com/6216077/55392970-46466b00-5577-11e9-85fd-97d370246863.png)

以下のボタンでネームサーバーを終了します。

![image](https://user-images.githubusercontent.com/6216077/55393017-60804900-5577-11e9-9466-dcb0afbe258f.png)


### RT System Editorでコンポーネントにアタッチした実行コンテキストを表示する機能
以下のようにRTCにアタッチした実行コンテキストをシステムダイアグラムで表示できるようになりました。

![image](https://user-images.githubusercontent.com/6216077/55393136-9f160380-5577-11e9-865f-685f28bf8b08.png)

表示するためには以下のボタンを押します。

![image](https://user-images.githubusercontent.com/6216077/55393195-c240b300-5577-11e9-9ed6-6d2b71ca20a5.png)

### RT System EditorにコンポーネントオブザーバーによるRTC監視機能を導入
RTSystemEditorがRTC側からのコンポーネントオブザーバーによる通知によりRTCの生存、終了、状態遷移などを把握するようになりました。

### RT System Editorでデータ入出力中のデータポートを点滅する機能

### RT System Editorにマスターマネージャ起動ボタンを導入
RTSystemEditor上からマスターマネージャを起動できます。

以下のボタンで起動できます。

![image](https://user-images.githubusercontent.com/6216077/55393921-1b5d1680-5579-11e9-80a9-0ee9e40c9d0c.png)

マスターマネージャのモジュールロードパスはOpenCVのサンプルコンポーネントのパスに設定されています。

ネームサーバーから起動したマスターマネージャを選択後、Loadable Modulesボタンを押してください。

![image](https://user-images.githubusercontent.com/6216077/55394029-595a3a80-5579-11e9-94d3-05620e483b9b.png)

これでロード可能なモジュール一覧が表示されますので、適当なモジュールを選択してcreateボタンを押してください。

![image](https://user-images.githubusercontent.com/6216077/55394140-8eff2380-5579-11e9-8637-49989ae43395.png)

以下のウィンドウでOKを押すとRTCが起動します。

![image](https://user-images.githubusercontent.com/6216077/55394199-b5bd5a00-5579-11e9-99d2-a20f06962c7c.png)

### RT System EditorにAll Exitボタンを導入
以下のボタンを押すことでシステムダイアグラム上のRTCを全て終了できるようになりました。

![image](https://user-images.githubusercontent.com/6216077/55394269-e00f1780-5579-11e9-9c38-6de430249e87.png)

### RTC BuilderでChoreonoid用のコードを生成する機能
以下のチェックをオンにすることでChoreonoid用のコードを生成可能になりました。

![image](https://user-images.githubusercontent.com/6216077/55394313-03d25d80-557a-11e9-9163-21ec3f814f35.png)

### RTC Builderで独自データ型のIDLファイルの設定方法の変更
独自データ型のIDLの指定方法が以下のようなテキストボックスに指定する方式に変更になりました。

![image](https://user-images.githubusercontent.com/6216077/55394400-32e8cf00-557a-11e9-9fea-03d62703c8d3.png)

一度使用したIDLファイルはワークスペースに保存されるため、2回目以降はデータ型の一覧に表示されます。
