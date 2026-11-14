---
layout: page
title: 動作確認(linux編)
---

<!-- Title: 動作確認(Linux編) -->
インストールが正常に終了したら、付属のサンプルで動作テストをします。サンプルは、通常は以下の場所にあります。
- /usr/share/openrtm-1.2/components/python/<サンプルコンポーネントセット名>

ソースからビルドした場合は、ソースディレクトリ下の
- OpenRTM_aist/examples/<span style="color:blue;"><サンプルコンポーネントセット名></span>;


サンプルコンポーネントセットSimpleIOを使って、OpenRTM-aistが正しくビルド・インストールされているかを確認します。

#contents(5)


## サンプルコンポーネントセットSimpleIO

RTコンポーネントConsoleIn、ConsoleOutからなるサンプルセットです。ConsoleInはコンソールから入力された数値をOutPortから出力するコンポーネント、ConsoleOutはInPortに入力された数値をコンソールに表示するコンポーネントです。これらは、SimpleなI/O(入出力)を例示するためのサンプルです。ConsoleInのOutPortからConsoleOutのInPortへ接続を構成し、これらの2つのコンポーネントをアクティブ化(Activate)することで動作します。

以降、サンプルは/usr/share/openrtm-1.2/components/python/SimpleIO下にあることを前程に説明します。また、Python本体の実行ファイルに対してはサーチパスが設定されているものとします。なお、ソースコードからビルドした場合はサンプル実行ファイルルは<span style="color:blue;"><source_dir></span>;/OpenRTM_aist/examples/SimpleIO/にあるので、起動パスを置き換えて下記の説明を利用してください。


## サンプルを使用した動作確認
### RTSystemEditorを使った動作確認
以下の説明ではRTSystemEditor(OpenRTP)を使った動作確認を説明します。RaspbianのケースのようにOpenRTPを使用しない環境での動作確認についてはrtshellのインスト―ルの[動作確認(Linux編)]({{ site.baseurl }}/ja/doc/installation/install_rtshell/check_linux)を参照ください。

#### ネームサーバーの起動
以下の手順に従ってRTSystemEditor、ネームサーバーを起動してください。

- [OpenRTP起動手順]({{ site.baseurl }}/ja/doc/installation/install_1_2/start_openrtp_linux_1_2)

#### ConsoleInの起動
- ターミナルを起動してConsoleInを起動します。
```
 $ python /usr/share/openrtm-1.2/components/python/SimpleIO/ConsoleIn.py
```
自分でビルド・インストールした場合は、
```
 $ python <source_dir>/OpenRTM_aist/examples/SimpleIO/ConsoleIn.py
```
などとしてConsoleInを起動します。

#### ConsoleOutの起動
- 別のターミナルを起動してConsoleOutを起動します。
```
 $ /usr/share/openrtm-1.2/components/python/SimpleIO/ConsoleOut
```
自分でビルド・インストールした場合は、同様に
```
 $ python <source_dir>/OpenRTM_aist/examples/SimpleIO/ConsoleOut.py
```
などとしてConsoleOutを起動します。

#### System Diagramへの配置
- RTSystem Editorのツリー表示の[>]をクリックすると、先ほど起動した2つのコンポーネントが登録されていることがわかります。
<div align="center"><a href="rtm10.png"><img src="rtm10.png" width="60%;"></a></div>
<div align="center"><strong>ConsoleInコンポーネントとConsoleOutコンポーネント</strong></div>
- システムを編集するSystem Diagramを開きます。上部のエディタを[Open New System Editor]ボタン<a href="rtse_open_editor_icon_ja.png"><img src="rtse_open_editor_icon_ja.png" width="3%;"></a>をクリックすると、中央のペインにSystem Diagramが開きます。
- 左側のネームサービスビューに<a href="rtse_rtc_icon_n.png"><img src="rtse_rtc_icon_n.png" width="3%;"></a>のアイコンで表示されているコンポーネント(2つ)を中央のSystem Diagramにドラッグアンドドロップします。
<div align="center"><a href="rtm11.png"><img src="rtm11.png" width="60%;"></a></div>
<div align="center"><strong>コンポーネントをSystem Diagramに配置</strong></div>

#### 接続とアクティブ化
- ConsoleIn0コンポーネントの右側にはデータが出力されるOutPort<a href="rtse_outport_icon_n.png"><img src="rtse_outport_icon_n.png" width="3%;"></a>、ConsoleOut0コンポーネントの左側にはデータが入力されるInPort<a href="rtse_inport_icon_n.png"><img src="rtse_inport_icon_n.png" width="3%;"></a>がそれぞれついています。
<div align="center"><a href="rtm13.png"><img src="rtm13.png" width="60%;"></a></div>
<div align="center"><strong>データポートの接続</strong></div>
- これらInPort/OutPort(まとめてデータポートと呼びます)を接続します。
OutPortからInPort(またはInPortからOutPort)へドラッグランドドロップすると、図のようなダイアログが現れますので、デフォルト設定のまま[OK]ボタンをクリックします。
<div align="center"><a href="rtm12.png"><img src="rtm12.png" width="60%;"></a></div>
<div align="center"><strong>データポート接続ダイアログ</strong></div>
- 2つのコンポーネントの間に接続線が現れます。次に、エディタ上部メニューの[All Activate]ボタン<a href="rtm14.png"><img src="rtm14.png" width="3%;"></a>をクリックし、これらのコンポーネントをアクティブ化します。
- アクティブ化されると、コンポーネントが緑色に変化します。
<div align="center"><a href="rtm15.png"><img src="rtm15.png" width="60%"></a></div>
<div align="center"><strong>アクティブ化されたコンポーネント</strong></div>
- コンポーネントがアクティブ化されるとConsoleInコンポーネント側では
```
 Please input number: 
```
というプロンプト表示に変わりますので、適当な数値(short intの範囲内:32767以下)を入力しEnterキーを押します。すると、ConsoleOut側でも入力した数値が表示され、ConsoleInコンポーネントからConsoleOutコンポーネントへデータが転送されたことがわかります。

以上で、RTSystemEditorを用いたコンポーネントの基本動作の確認は終了です。


