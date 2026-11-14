---
layout: page
title: rtsystemeditor、rtcbuilder、rtshell 等ツールに関する faq
---

<!-- Title: RTSystemEditor、RTCBuilder、rtshell 等ツールに関する FAQ -->
#contents(4)

## RTSystemEditor

### Windows10 などで、高解像度モードのときにアイコン等が小さくなる

Windows10 などで HiDPIモードに対応していないアプリケーションは、高解像度時にウィンドウやアイコンが小さく表示される場合があります。
Eclipse も HiDPIモードでは中途半端にしか対応しておらず、下図のように全体的に小さく表示されます。


<div align="center"><a href="OpenRTP_normal.png"><img src="OpenRTP_normal.png" width="60%;"></a></div>
<div align="center"><strong>通常表示</strong></div>

<div align="center"><a href="OpenRTP_small.png"><img src="OpenRTP_small.png" width="50%;"></a></div>
<div align="center"><strong>HiDPI非対応の場合の表示</strong></div>

以下の手順でレジストリの変更とマニフェストファイルの配置によって、この問題を解決することができます。

レジストリに以下のキーを追加します

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion‌​\SideBySide\PreferEx‌​ternalManifest = (DWORD) 1

  - レジストリにこの値を追加するための reg ファイルを以下からダウンロードしダブルクリックする<br>
[ExternalManifestON.reg](http://openrtm.org/openrtm/sites/default/files/248/ExternalManifestON.reg)
1. `<exeファイル名>`.exe.manifest というファイル名のマニフェストファイルを exe と同じフォルダーに置く
 - OpenRTP用マニフェスト: [eclipse.exe_.manifest](./eclipse.exe_.manifest)
<!-- a href="eclipse.exe_.manifest"><img src="eclipse.exe_.manifest" width="100;"></a>;<br-->
※使用時には eclipse.exe.manifest にリネームする

 - RTSystemEditorRCP用マニフェスト: [RTSystemEditorRCP.exe_.manifest](./RTSystemEditorRCP.exe_.manifest)
<!-- div align="center"><a href="RTSystemEditorRCP.exe_.manifest"><img src="RTSystemEditorRCP.exe_.manifest" width="100;"></a></div>;<br>-->
※RTSystemEditorRCP.exe.manifest にリネームする
<br>

### RTSystemEditor の操作パフォーマンスが悪くなる
RTSystemEditor は常にシステムの情報を収集しながら表示を同期しています。 このシステム情報を収集する際に、 動作していないオブジェクトのリファレンスにアクセスするとタイムアウト待ちを起こして極端に遅くなることがあります。~
動作していないオブジェクトが発生した場合には、 ネームサービスから「Delete from NameService」で削除を行い、また動作していないオブジェクトとポート接続しているオブジェクトを、ネームサービスおよびシステムエディタから削除すると動作が軽くなるでしょう。
<br>

<!-- ****RTコンポーネント以外の CORBA オブジェクトがネームサービスに登録されている場合、そのネームサービスを RtcLink のネームサービスビューで指定するとエラーダイアログが表示される。  -->
<!-- #br -->

### システムエディタにて同一ポート間に複数が接続(重複接続)されていると見分けることができない
接続線では、重複接続の区別がつきません。お手数ですが、プロジェクトファイルでご確認をお願いします。
<br>
<br>

### RTSystemEditor で [All Activate] ボタンが押せない
OpenRTP を再起動してください。
<br>
<br>

### RTSystemEditor でコンフィギュレーションが表示されない
OpenRTP を再起動してください。
<br>
<br>

### RT System Editor の操作パフォーマンスが悪くなります
RT System Editor は常にシステムの情報を収集しながら表示に同期しています。このシステム情報を収集する際に、動作していないオブジェクトのリファレンスにアクセスするとタイムアウト待ちを起こして極端に遅くなることがあります。
動作していないオブジェクトが発生した場合は、ネームサービスビューから「 Delete from NameService 」で削除します。また、動作していないオブジェクトとポート接続しているオブジェクトをネームサービスおよびシステムエディタから削除するとパフォーマンスが戻ることがあります。
<br>
<br>

### Eclipse のワークスペースに「 RT System Editor_Files 」プロジェクトが作成されます。これは何ですか？
RT System Editor が実行時に内部で使用している一時的な情報が保存されています。実行時に一時的に使用しているものですので、実行中には削除しないでください。RT System Editor の停止中にはプロジェクトごと削除しても問題ありません。
<br>
<br>

### システムエディタにて同一ポート間に複数が接続(重複接続)されている場合、見分ける方法はありますか？
**A. **接続線では、重複接続の区別がつきません。お手数ですが、プロジェクトファイルでご確認をお願いします。
<br>
<br>

## RTCBuilder
### RTC プロファイルエディタで保存すると「Error writing file.」というエラーが表示される
保存先の指定が不正な場合に表示されます。保存先を任意のプロジェクト内のディレクトリーにして保存してください。
<br>
<br>

### データ型のプルダウンメニューがブランクになっている
OpenRTM-aist インストール後に PCを再起動していないと現象が発生する可能性があります。再起動を行ってください。
<br>
<br>

## rtc-template（cui版）
### サービスポートのオプションについて 
サービスプロバイダポートを使用する場合は、~
```
 "--service=PortName:ServiceName:Type"
```
を、サービスコンシューマポートを使用する場合は、~
```
 "--consumer=PortName:ServiceName:Type"
```
を与えます。~
これらのオプションには以下のような制限があります。
"--module-name="で与えるコンポーネント名とIDLで指定したサービスインターフェース名は異なるものでなければなりません。
"Type"はサービスインターフェース名と同じでなければなりません。
"ServiceName"と"Type"は対になるプロバイダとコンシューマとで同じでなければなりません。（PortNameはコンポーネント内で唯一であれば任意）
<br>
<br>

## Eclipse
&aname(eclipse);
### Eclipse の起動方法
- Windows系システムの場合 
  - Eclipse のインストールフォルダーから eclipse.exe をさがし、そのアイコンをダブルクリックします。

- UNIX系システムの場合
  - 以下は、一例としてログインシェルが bash である場合を想定して説明しています。

- 環境変数 RTM_JAVA_ROOT が /etc/profile に設定されている場合
  - ファイルブラウザで Eclipse のアイコンをダブルクリックして起動できます。また、次に説明するようにコマンドラインからも起動できます。

- 環境変数 RTM_JAVA_ROOT が .bashrc に設定されている場合
  - <span style="color**: red;">**ダブルクリックでの起動は避けてください。**</span>; 必ず、ターミナルを起動してコマンドラインから Eclipse を起動してください。たとえば、Eclipse が /usr/Eclipse に展開されているとした場合は次のようなコマンドで Eclipse を起動できます。~

```
 $ /usr/Eclipse/eclipse
```
- note:
  -  ダブルクリックでの起動を避ける理由|RTCBuilder で生成した RTC のコードを Eclipse で Ant ビルドするときに、環境変数 RTM_JAVA_ROOT が使用されます。ダブルクリックで Eclipse を起動すると、設定ファイル .bashrc が読み込まれず、Ant ビルドに失敗する場合があります。
<br>
<br>

&aname(rtclinksunjava);
### UNIX 系環境で簡易に Oracle の Java(JRE) を Eclipse に適用する方法
UNIX系の環境では、Java をインストールしようとすると GCJ (The GNU Compiler for Java ) がインストールされてしまうということが多いようです（多くのLinuxディストリビューションが該当しています）。Eclipse tools は Oracle の JRE1.6 以上でないと不具合が発生してしまいます。**とりあえず「Eclipse だけで Oracle の Java を使用したい」場合**は次のようにしてください。~
JDK を入手し、それを実行してできた jre ディレクトリーを Eclipse インストールディレクトリーへコピーしてご使用ください。
<!-- ただし、この方法で RtcTemplate を動かす場合、Java についてのみ RTC テンプレートコード生成ができなくなります。 -->
<!-- ''*'' jdk-6u4-linux-i586.binなどでも大丈夫です。 -->
<br>
**EclipseにOracleのJREを適用する方法例（jdk-6u4-linux-i586.binを使用した場合）**
```
 $ sh jdk-6u4-linux-i586.bin
 $ cp -r jdk1.6.0_04/jre eclipse/
```
<br>
<br>

