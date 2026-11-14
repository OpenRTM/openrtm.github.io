---
layout: page
title: rtshellコマンド・リファレンス
---

<!-- Title: rtshellコマンド・リファレンス -->
## 概要
コマンドの多くは、ネームサーバーで動作しているコンポーネントとマネージャーをファイルシステムのように扱えるようにしてあります。ディレクトリに入ったり、コンポーネントをcatのようにで読んだり、アクティブさせたり、ポートを接続できます。ほかのコマンドはRTシステムを管理するためのRTSProfileファイルに関連して使用されます。

## コマンド
<table class="table-alt">
  <tr>
    <td>コマンド名</td>
    <td>概要</td>
  </tr>
  <tr>
    <td><a href="./rtact">rtact</a></td>
    <td>RTコンポーネントをアクティブにします。</td>
  </tr>
  <tr>
    <td><a href="./rtcat">rtcat</a></td>
    <td>RTコンポーネントのメタデータを表示します。</td>
  </tr>
  <tr>
    <td><a href="./rtcheck">rtcheck</a></td>
    <td>起動中のRTシステムを読み込んだRTSProfileデータと比べます。</td>
  </tr>
  <tr>
    <td><a href="./rtcomp">rtcomp</a></td>
    <td>コンポジットコンポーネントを作ります。</td>
  </tr>
  <tr>
    <td><a href="./rtcon">rtcon</a></td>
    <td>ポートを接続します。</td>
  </tr>
  <tr>
    <td><a href="./rtconf">rtconf</a></td>
    <td>コンポーネントのコンフィグレーションを照会/設定します。</td>
  </tr>
  <tr>
    <td><a href="./rtcryo">rtcryo</a></td>
    <td>起動中のRTシステムのRTSProfileデータをファイルかstdoutに出力します。</td>
  </tr>
  <tr>
    <td><a href="./rtcwd">rtcwd</a></td>
    <td>現在の作業ディレクトリを変更します。</td>
  </tr>
  <tr>
    <td><a href="./rtdeact">rtdeact</a></td>
    <td>コンポーネントを非アクティブにします。</td>
  </tr>
  <tr>
    <td><a href="./rtdel">rtdel</a></td>
    <td>ネームサーバーからオブジェクトを消去します。</td>
  </tr>
  <tr>
    <td><a href="./rtdis">rtdis</a></td>
    <td>ポートの接続を切ります。</td>
  </tr>
  <tr>
    <td><a href="./rtdoc">rtdoc</a></td>
    <td>RTコンポーネントのドキュメンテーションを表示します。</td>
  </tr>
  <tr>
    <td><a href="./rtexit">rtexit</a></td>
    <td>RTコンポーネントを停止します。</td>
  </tr>
  <tr>
    <td><a href="./rtfind">rtfind</a></td>
    <td>起動中のRTコンポーネントやマネージャなどを探します。</td>
  </tr>
  <tr>
    <td><a href="./rtinject">rtinject</a></td>
    <td>ポートにデータを送ります。</td>
  </tr>
  <tr>
    <td><a href="./rtlog">rtlog</a></td>
    <td>ポートが送るデータをログに保存して再生します。</td>
  </tr>
  <tr>
    <td><a href="./rtls">rtls</a></td>
    <td>現在の作業ディレクトリ上のオブジェクトをリストします。</td>
  </tr>
  <tr>
    <td><a href="./rtmgr">rtmgr</a></td>
    <td>マネジャーでRTコンポーネントを管理します。</td>
  </tr>
  <tr>
    <td><a href="./rtprint">rtprint</a></td>
    <td>ポートが送るデータをターミナルに表示します。</td>
  </tr>
  <tr>
    <td><a href="./rtpwd">rtpwd</a></td>
    <td>現在の作業ディレクトリを表示します。</td>
  </tr>
  <tr>
    <td><a href="./rtreset">rtreset</a></td>
    <td>RTコンポーネントをリセットします。</td>
  </tr>
  <tr>
    <td><a href="./rtresurrect">rtresurrect</a></td>
    <td>RTSProfileデータを用いてRTシステムの接続を復元します。</td>
  </tr>
  <tr>
    <td><a href="./rtstart">rtstart</a></td>
    <td>RTSProfilleデータを用いてRTシステムを起動します。</td>
  </tr>
  <tr>
    <td><a href="./rtstodot">rtstodot</a></td>
    <td>起動中のRTシステムをグラフで表示します。</td>
  </tr>
  <tr>
    <td><a href="./rtstop">rtstop</a></td>
    <td>RTSProfielデータを用いてRTシステムを停止します。</td>
  </tr>
  <tr>
    <td><a href="./rtteardown">rtteardown</a></td>
    <td>RTSProfileデータを用いてRTシステムを削除する。</td>
  </tr>
</table>


## RTCツリー

すべてのコマンドはRTCツリー上で起動します。RTCツリーとは、ネームサーバー上のコンテキスト、コンポーネント、マネージャなどをファイルシステムに見立てて扱うことができる仕組みです。通常のファイルシステムと同じように扱うことができます。

ネームサーバーはルートディレクトリ"/"直下のサブディレクトリとして扱われます。その下にはファイルやサブディレクトリが存在します。サブディレクトリはネームサーバー上のネーミングコンテクストに対応します。ファイルはコンポーネントとマネージャーに対応します。

ツリーを構築するためのネームサーバーを与える方法は2通りあります。一つはrtshellコマンドに渡したネームサーバーへの相対パスです。これは現在の作業ディレクトリからの相対パスです。また絶対パス指定して場合はルート直下のディレクトリがネームサーバーがあるホスト名(IPアドレスの場合もあり)です。

もう一つはRTCTREE_NAMESERVERS環境変数です。ネームサーバーのホストアドレスをセミコロンで区切り、リストを渡すこともできます。複数のネームサーバーがあるホストを指定した場合はそれぞれのホストがルート直下に見えるようになります。

## シェルコンプリーション
Bashシェルを使う方はrtshell付属のコンプリーションスクリプトによってrtshellのコマンド入力の補完ができるようになり使いやすくできます。スクリプトは/usr/local/lib/pythonX.Y/dist-packages/rtshellにインストールされます。以下のコマンドでロードしてください:
```
 $ source /usr/local/lib/pythonX.Y/dist-packages/rtshell/bash_completion
```

また上記の行を`/.bashrcというファイルに追加すればターミナル起動時に自動的にロードされます。`

### コンプリーション(補完)の例:
```
 $ rtcwd /localhost/[TAB]
 $ rtcwd /localhost/ubuntu.host_cxt/
```

```
 $ rtcwd /localhost/ubuntu.host_cxt/[TAB][TAB]
 /localhost/ubuntu.host_cxt/ConfigSample0.rtc
 /localhost/ubuntu.host_cxt/ConsoleIn0.rtc
 /localhost/ubuntu.host_cxt/ConsoleOut0.rtc
 /localhost/ubuntu.host_cxt/manager.mgr/
```

```
 $ rtcwd localhost/ubuntu.host_cxt/[ENTER]
```

```
 $ rtconf ConfigSample0.rtc set [TAB]
 double_param0  int_param0     str_param0     vector_param0  
 double_param1  int_param1     str_param1
```

```
 $ rtcon ConsoleIn0.rtc:[TAB]
 $ rtcon ConsoleIn0.rtc:out
```


## システムの要件
- rtshellはrtctreeが必要です。インストールされていない場合はコマンドは起動しません。
- RTSProfileデータを使うコマンドはrtsprofileが必要です。インストールされていない場合はこのコマンドは起動しません。
- rtshellはPython 3.7/3.6/2.7が必要です。
- rtinject 、rtlog及びrtprintはOpenRTM-pythonが必要です。

## パス
rtshell はパスでRTCツリーのオブジェクトを示します。ネームサーバーとネームコンテクストはディレクトリ名として指定され、マネージャとRTコンポーネントはファイル名として指定されます。コマンドに渡したパスはrtshellの現在作業ディレクトリを元に指定されます。(相対パスの場合)。rtshellの現在の作業ディレクトリはRTCSH_CWDという環境変数に保存されて、rtcwdというコマンドで変更できます。(現時点でrtcwdコマンドはLinux環境では動作していません)

利用できるパスはコマンド実行時に参照しているネームサーバーによって変わります。ネームサーバーが実行されているホスト名はRTCTREE_NAMESERVERSという環境変数で指定できます。また、直接ルート直下のパスとして/<ホスト名>/.... のような形でネームサーバーが実行されているホストを指定できます。

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

新たに作られるポートの名前はstuffで、データはa_printerという関数(フォーマッター)でターミナルに表示するように指定します。(a_printerの関数はPythonが利用可能な場所に存在する必要があります。普通はユーザーがモジュールで提供します。) 作られたポートはcomp0.rtcのinputというポートに接続されます。

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
  - RTCツリーを作る時に参照するネームサーバーのアドレスです。アドレスをセミコロンで区切ります。リストされたアドレスはRTCツリーに追加されrtshellで参照できるようになります。ルート下のディレクトリ名としてパスで指定できるので必須ではありません。
- **RTSH_CWD**
  - rtshellの現在の作業ディレクトリ。rtshellが自動的に設定します。設定しないでください。

一般的な利用ではユーザーが設定する変数はRTCTREE_NAMESERVERSのみです。よく使うネームサーバーを設定しておくと便利です。例えば、Bashシェルの場合、以下のコマンドはlocalhostとポート192.168.0.1:65346およびホストexample.comにあるネームサーバーをrtshellが参照できるようにします。

```
 $ export RTCTREE_NAMESERVERS=localhost;192.168.0.1:65346;example.com
```


## 返り値
成功の場合はゼロを返します。失敗の場合はゼロではない値を返します。

デバッグ情報とエラーはstderrに出力されます。

<hr>

- [rtact](./rtact)
- [rtcat](./rtcat)
- [rtcheck](./rtcheck)
- [rtcomp](./rtcomp)
- [rtcon](./rtcon)
- [rtconf](./rtconf)
- [rtcryo](./rtcryo)
- [rtcwd](./rtcwd)
- [rtdeact](./rtdeact)
- [rtdel](./rtdel)
- [rtdis](./rtdis)
- [rtdoc](./rtdoc)
- [rtexit](./rtexit)
- [rtfind](./rtfind)
- [rtinject](./rtinject)
- [rtlog](./rtlog)
- [rtls](./rtls)
- [rtmgr](./rtmgr)
- [rtprint](./rtprint)
- [rtpwd](./rtpwd)
- [rtreset](./rtreset)
- [rtresurrect](./rtresurrect)
- [rtstart](./rtstart)
- [rtstodot](./rtstodot)
- [rtstop](./rtstop)
- [rtteardown](./rtteardown)
