## OpenRTM-aist 1.2の既知の不具合について

### Python3使用時に独自データ型やサービスポート等のIDLコンパイルを含むRTCをビルドするとビルドエラーが発生する

ALL_IDL_TGTのターゲットをビルドした際に実行するskel_wrapper.pyというスクリプトの不具合です。
以下の条件で発生します。

- Python3.6、もしくは3.7を使用
- C++でRTCを作成
- 独自データ型やサービスポートを含む
- Visual Studioでリビルドを行う(未確認ですが、Linuxでmake clean後にmakeしても発生する可能性がある)

対処としては`C:\Program Files\OpenRTM-aist\1.2.0\bin\skel_wrapper.py`を以下のファイルに差し替えるか、Python 2.7を使用するしかありません。

- [skel_wrapper.py](https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/utils/rtm-skelwrapper/skel_wrapper.py)


### 別のマシンで起動したRTCをRTSystemEditorで操作するとRTCが異常終了する
コンポーネントオブザーバーの解除時のバグにより、コンポーネントオブザーバーの通信エラー発生時にRTCが異常終了することがあります。
ファイアウォールで通信がブロックされたり、無線LANが切断されて通信できなくなった場合に発生する可能性があります。

### RTSystemEditor上でPythonのRTCでサービスポートを接続したが、接続されていないように表示される
OpenRTM-aist 1.2からコンポーネントオブザーバーの機能によりポートの接続時などにRTCからRTSystemEditorへ通知が送られるようになりましたが、Python版のバグによりサービスポート接続時は通知されません。
通知がされないだけのため接続自体は正常に完了しています。
RTCをシステムダイアグラムから一旦削除して再配置すると反映されますが、rtc.confに以下のように記述してコンポーネントオブザーバーを無効にしても対応できます。

```
sdo.service.consumer.enabled_services: off
```


### Python版でトピックベース接続機能が動作しない
Python版のトピックベース接続機能はバグにより動作しません。

### rtshellのコマンドが実行できない
rtshellのコマンドを実行するexeファイルの作成方法に問題があったため発生した不具合です。
発生した場合には以下のコマンドでrtshell、rtctree、rtsprofileのアンインストール、rtshellの再インストールをお願いします。

```
pip uninstall rtshell rtctree rtsprofile
pip install rtshell-aist
```
