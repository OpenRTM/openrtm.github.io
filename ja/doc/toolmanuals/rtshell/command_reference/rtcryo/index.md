---
layout: page
title: rtcryo
---

<!-- Title: rtcryo -->

## 書式
```
rtcryo [OPTION...] [NAME_SERVER]
```

## 概要
実行中のRTシステムのRTSProfileを保存します。コンポーネント間の接続とコンポーネントの現在のコンフィグレーションパラメータを保存します。接続されていないコンポーネントは保存しません。

ファイル名を指定しない場合、RTSProfileをstdoutに出力します。デフォルトはXMLで保存します。

## オプション
```
 -a ABSTRACT、--abstract=ABSTRACT
 　　　　　　RTシステムの概要を設定します。
 -n SYSNAME、--system-name=SYSNAME
 　　　　　　RTシステムの名前を設定します。
 -o OUTPUT_FILE、--output=OUTPUT_FILE
 　　　　　　出力ファイル名。指定しない場合はstdoutに出力します。
 -v VERSION、--system-version=VERSION
 　　　　　　RTシステムのバージョン設定します。
 -e VENDOR、--vendor=VENDOR
 　　　　　　RTシステムのベンダー名を設定します。
 -x、--xml　　　XML形式で出力します。
 -y、--yaml　 　YAML形式で出力します。
 --version　　　プログラムのバージョン番号を表示します。
 -h、--help 　　ヘルプを表示します。
 -v、--verbose より詳細な情報を出力します。
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
- すべて管理できるネームサーバー上のすべての接続されているコンポーネントの一つのRTシステムとしてRTSProfileをstdoutに出します。
```
 $ rtcryo
```

- 全ての管理できるネームサーバー上のすべての接続されているコンポーネントを一つのRTシステムとしてRTSProfileをsys.rtsysというファイルに保存します。
```
 $ rtcryo -o sys.rtsys
```


- localhostというホストのネームサーバーのすべての接続されているコンポーネントを一つのRTシステムとしてRTSProfileをstdoutに出します。
```
 $ rtcryo localhost
```

- RTシステムの名前をmysystem、バージョンを1.0としてRTSProfile出力します。
```
 $ rtcryo -n 'mysystem' -v 1.0
```


