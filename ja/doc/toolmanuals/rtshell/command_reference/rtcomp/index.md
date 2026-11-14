---
layout: page
title: rtcomp
---
<!-- Title: rtcomp -->

## 書式
```
rtcomp [OPTION...] MANAGER
```
## 概要
実行している複数のコンポーネントを、同じマネージャ上に一つのコンポジット・コンポーネントとして構成し、選択されたポートを外部にエクスポートします。Execution contextも選択することが可能です。ポートがエクスポートされているコンポーネントは自動的に構成に含まれます。

## オプション
```
 -c COMPONENT_NAME、--comp=COMPONENT_NAME
 　　　　　　コンポジットコンポーネントに含むコンポーネントを指定します。このオプションは複数個の指定が可能です。
 -n NAME、--name=NAME
 　　　　　　コンポジットコンポーネントのインスタンス名(生成されるコンポネントの名前)を指定する。[デフォルト:CompositeRTC]
 -o OPTIONS、--options=OPTIONS
 　　　　　　コンポーネントを作る時の追加オプション。「&」で始めてください。
 -p PORTS、--port=PORTS
 　　　　　　エクスポート(外部公開)するポートを指定する。ポートがエクスポートされているコンポーネントは自動的にコンポジットコンポーネントに含まれます(-cと同じ)。
 -t TYPE、--type=TYPE
 　　　　　　Execution contextのタイプを指定します。[デフォルト:PeriodicECSharedComposite]
 --version　　プログラムのバージョン番号を表示して終了する
 -h、--help　　ヘルプを表示して終了する
 -v、--verbose より詳細な情報を出力する
```

## パス
rtshellはパスでRTCツリーのオブジェクトを示します。ネームサーバーとネームコンテクストはディレクトリ名として指定され、マネージャとRTコンポーネントはファイル名として指定されます。コマンドに渡したパスはrtshellの現在の作業ディレクトリを元に指定されます。(相対パスの場合)。rtshellの現在の作業ディレクトリはRTCSH_CWDという環境変数に保存されて、rtcwdというコマンドで変更できます。(現時点でrtcwdコマンドはLinux環境では動作していません)

利用できるパスはコマンド実行時に参照しているネームサーバーによって変わります。ネームサーバーが実行されているホスト名はRTCTREE_NAMESERVERSという環境変数で指定できます。また、直接ルート直下のパスとして/<ホスト名>/....のような形でネームサーバーが実行されているホストを指定できます。

例えば、/localhost/comp0.rtcはlocalhostにあるネームサーバーに登録されたcomp0.rtcというRTコンポーネントを示します。/localhost/manager/comp0.rtcはlocalhostにあるネームサーバーの下のmanagerというディレクトリに登録されたcomp0.rtcというRTコンポーネントを示します。./comp0.rtcは現在の作業ディレクトリにあるcomp0.rtcというRTコンポーネントを示します。

RTコンポーネントのポートを示す場合、パスの後にコロン（「:」）で区切って指定します。例えば、/localhost/comp0.rtc:dataはcomp0.rtcというRTコンポーネントのdataというポートを意味します。

新しいポートを作れるコマンドもあり、この場合、オプションでそれらをパスに追加できます。使えるオプションは作られるポートの名前とフォーマッタです。指定方法は以下の通りです:

```
 <path>:<port>.<new_port_name>#<formatter>
```

### 例:
```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff#a_printer
```

新たに作られるポートの名前はstuffで、データはa_printerという関数(フォーマッター)でターミナルに表示するように指定しています。(a_printerの関数はPythonが利用可能な場所に存在する必要があります。普通はユーザーがモジュールで提供します)。作られたポートはcomp0.rtcのinputというポートに接続されます。

`<new_port_name>`という部分は必須ではありません。指定しない場合は"."も指定しないでください。例:

```
 /localhost/blurg.host_cxt/comp0.rtc:input#a_printer
```

`<formatter>`という部分は必須ではありません。書いていない場合は"."も指定しないでください。例:

```
 /localhost/blurg.host_cxt/comp0.rtc:input.stuff
```

## 環境変数
- **RTCTREE_ORB_ARGS**
  - ORBを作る時に渡す変数です。セミコロンで区切ります。必須ではありません。
- **RTCTREE_NAMESERVERS**
  - RTCツリーを作る時に参照するネームサーバーのアドレスです。アドレスをセミコロンで区切ります。リストされたアドレスはRTCツリーに追加されrtshellで参照できるようになります。ルート下のディレクトリ名としてパスで指定することもできるので必須ではありません。
- **RTSH_CWD**
  - rtshellの現在のワーキングディレクトリ。rtshellが自動的に設定します。設定しないでください。

一般的な利用ではユーザーが設定する変数はRTCTREE_NAMESERVERSのみです。よく使うネームサーバーを設定しておくと便利です。例えば、Bashシェルの場合、以下のコマンドはlocalhostとポート192.168.0.1:65346およびホストexample.comにあるネームサーバーをrtshellが参照できるようにします。

```
 $ export RTCTREE_NAMESERVERS=localhost;192.168.0.1:65346;example.com
```

## 返り値
成功の場合はゼロを返します。失敗の場合はゼロではない値を返します。

デバッグ情報とエラーはstderrに出力されます。

## 例
- Controller0.rtcのinポートとMotor0.rtcのoutポートをエクスポートしてMotor0.rtcとController0.rtcによってコンポジットコンポーネントを作ります。コンポジットコンポーネントのインスタンス名はMotorUnitです。
```
 $ rtcomp /localhost/manager.mgr -c /localhost/Motor0.rtc -p /localhost/Controller0.rtc:in -p /localhost/Motor0.rtc:out -n MotorUnit
```



