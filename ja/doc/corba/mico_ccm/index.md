---
layout: page
title: mico_ccm
---

<!-- Title: MICO_CCM -->
#contents

<!-- * [[MICO CCM]] -->

## ccmd (mico-ccmd) 
MICO に付属する CCM デーモン。
ccmd は単一ホスト上でのコンポーネントのインストール、デプロイされたコンポーネントの管理を行う。したがって、複数ホストにコンポーネントを実行したい場合は各ホスト上で実行しなければならない。
mico-ccmd はComponentInstallation, AssemblyFactory および ServerActivator インターフェース(およびサービス)が実装されている。

- ComponentInstallation
  - mico-ccmdが実行されているホスト上では、ComponentInstallation インターフェースを通してコンポーネント実装をインストールすることができる。通常は mico-ccmload によりコンポーネントをインストールする。

- AssemblyFactory
  - AssemblyFactory を通してコンポーネントのアセンブリをオンデマンドで起動することができる。

- ServerActivator
  - ServerActivator インターフェースを通してコンポーネントサーバーをオンデマンドで起動することができる。

デプロイメントツールはまず始めに、mico-ccm と通信しコンポーネント実装ファイルをアップロードし、そのホストで componentserver を起動する。
(コンポーネント毎にプロセス作るのか？)
mico-ccmd は通常永続的バックグラウンドで動作するデーモンで、表立っては何もしない。
もし終了シグナル (SIGINT、Ctrl-C) を受け取ると、すべてのアセンブリおよびコンポーネントサーバーを終了させる。
最後に、インストールされたすべてのコンポーネント実装を削除し終了する。


### オプション
<table class="table-alt">
  <tr>
    <td>--root <pkgdir></td>
    <td>インストールされるコンポーネント実装が保存されるディレクトリーへのパス。指定されなければカレントディレクトリーに保存される。</td>
  </tr>
  <tr>
    <td>--ior <filename></td>
    <td>mico-ccmd の IORをファイルに保存したい場合はこのオプションでファイル名を指定する。ハイフンで標準出力する。</td>
  </tr>
  <tr>
    <td>-v</td>
    <td>冗長オプション。コンポーネントサーバーのスタート、ストップ等のステータスメッセージを標準出力する。</td>
  </tr>
</table>

MICO ORB の標準オプションも使用可能。
- ORBIIOPAddr により、特定の IPアドレスに ORB をアサイン (-ORBIIOPAddr hoge.aist.go.jp::1234 等) することが可能である。
ポートが既知であれば、mico-ccmd をオブジェクト URL で指定することも可能である。
mico-ccmd のオブジェクトキーは "MicoCCMD" なので、
```
 corbaloc::<host>:<port>/MicoCCMD
```
といった URL で ccmd のオブジェクトを指定することができる。

## ccmload (mico-ccmload)

ccmload は単一のコンポーネントを配置することができる簡単なデプロイメントツールである。
ccmload は MicoCCM デーモンと通信し新たなコンポーネントサーバーを起動し新たなコンポーネントをロードする。
そして、共有ライブラリ &lt;library file&gt; からホーム &lt;home name&gt; をコンテナにロードする。
オプションとして、home をネームサーバーに登録することもできる。
&lt;home name&gt; はデプロイされるコンポーネントホームの完全な名前である必要がある。
&lt;library name&gt; は &lt;home name&gt; の実装を含む共有ライブラリファイル名でなくてはならない。
ccmload は実装の共有ライブラリをアップロードするのではなく、ファイル名は MicoCCMデーモンがアクセスできるものでなくてはならない。

<br>
<table class="table-alt">
  <tr>
    <td>--ccmd <IOR></td>
    <td>MicoCCM Daemon のオブジェクトリファレンスを与える。</td>
  </tr>
  <tr>
    <td>--host <host>[:port]</td>
    <td>このオプションにより MicoCCM デーモンのアドレスとポートを与えることができる。ポート番号が指定されない場合のデフォルトポートは1234である。</td>
  </tr>
  <tr>
    <td>--ns <name></td>
    <td>デプロイされるホームを指定の名前でネームサーバーに登録する。</td>
  </tr>
  <tr>
    <td>--ior <filename></td>
    <td>デプロイされるホームのオブジェクトリファレンスを指定のファイルに書き出す。ハイフンで標準出力に書き出す。</td>
  </tr>
  <tr>
    <td>-v</td>
    <td>冗長メッセージ出力</td>
  </tr>
</table>

