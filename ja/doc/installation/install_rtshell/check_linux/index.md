---
layout: page
title: 動作確認(linux編)
---

<!-- /node/6996 -->
<!-- Title: 動作確認(Linux編) -->
インストールが正常に終了したら、付属のサンプルで動作テストをします。サンプルは、通常は以下の場所にあります。
- /usr/share/openrtm-1.2/components/python/<サンプルコンポーネントセット名>

サンプルコンポーネントセットSimpleIOを使って、OpenRTM-aistが正しくビルド・インストールされているかを確認します。

#contents(3)


## サンプルコンポーネントセットSimpleIO

RTコンポーネントConsoleIn、ConsoleOutからなるサンプルセットです。ConsoleInはコンソールから入力された数値をOutPortから出力するコンポーネント、ConsoleOutはInPortに入力された数値をコンソールに表示するコンポーネントです。これらは、単純なI/O(入出力)を例示するためのサンプルです。ConsoleInのOutPortからConsoleOutのInPortへ接続を構成し、これらの2つのコンポーネントをアクティブ化(Activate)することで動作します。

以降、サンプルは/usr/share/openrtm-1.2/components/python/SimpleIO下にあり、Python本体の実行ファイルにはサーチパスが設定されているものとして説明を記述します。


## サンプルを使用した動作確認

### ネームサーバーの起動
- ネームサーバーを起動します。以下のコマンドで起動ができます。
```
 $ rtm-naming
```
- OpenRTM-aist(C++)をインストールしていない環境では、下記スクリプトで起動できるように用意しています。
```
 $ python /usr/lib/python2.7/dist-packages/OpenRTM_aist/utils/rtm-naming/rtm-naming.py
       or
 $ python3 /usr/lib/python3/dist-packages/OpenRTM_aist/utils/rtm-naming/rtm-naming.py
```
ここで{Python2.7|python3}は、Python版のOpenRTM-aistをインストールした時のLinux環境でインストールしてあったPythonのバージョンによって変わり、Python 2.7がインストールされていた場合は"Python2.7"です。(Ubuntu18.04のデフォルトはPython2.7です。)

以下のような画面が表示されます。

<div align="center"><a href="startnameservice002.png"><img src="startnameservice002.png" width="60%;"></a></div>
<div align="center"><strong>ネームサーバー画面</strong></div>

### サンプルコンポーネントの起動
- ターミナルを開きます。
- ターミナルでカレントディレクトリを/usr/share/openrtm-1.2/components/python/SimpleIOにします。
```
 $ cd /usr/share/openrtm-1.2/components/python/SimpleIO
```

- ConsoleInコンポーネントを以下のコマンド起動します。
```
 $ python ConsoleIn.py
```

- 別ターミナルを開きます。
- カレントディレクトリを上記と同じところに設定します。
- ConsoleOutコンポーネントを以下のコマンドで起動します。
```
 $ python ConsoleOut.py
```

#### ネームサービス上の名前の確認
- 別ターミナルを開きます
以下のようにして名前を確認してください。
```
 $ rtls -R localhost
 .:
 ConsoleIn0.rtc  ConsoleOut0.rtc
```
#### サンプルコンポーネントの接続
- ConsoleIn0コンポネントとConsoleOut0を以下のコマンド接続します。
上記で開いたターミナルで
```
 rtcon /localhost/ConsoleIn0.rtc:out /localhost/ConsoleOut0.rtc:in
```
と入力します。

### サンプルコンポーネントのアクティブ化
- 上記のターミナルで
```
 rtact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc
```
と入力します。すると、Consolein.pyとConsoleOut.pyを起動したターミナルの以下の画面がとなり、ConsoleIn.pyを起動したターミナルではPlease input number:というプロンプト表示に変わります。

<div align="center"><a href="simpleio_ubuntu.png"><img src="simpleio_ubuntu.png" width="60%;"></a></div>
<div align="center"><strong>アクティブ化後のConsoleInコンポーネントとConsoleOutコンポーネントのターミナル画面</strong></div>

- 適当な数値(short intの範囲内:32767以下)をConsoleInを起動したターミナルで入力しEnterキーを押します。
- ConsoleOut.pyターミナル画面に入力した数値と同じものが表示されます。これでConsoleInコンポーネントからConsoleOutコンポーネントへデータが転送されたことがわかります。

### サンプルコンポーネントの非アクティブ化と終了
- 以下のコマンドで非アクティブ化します。 
```
 rtdeact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc
```
- ConsoleIn.pyのターミナルは入力待ちになっているので、適当な数値: 32767以下を入力してEnterキーを押します。
- 以下のコマンドを入力し、ConsoleIn.pyとConsoleOut.pyの実行が終了するのを、それぞれのターミナルで確認してください。
```
 rtexit /localhost/ConsoleIn0.rtc
 rtexit /localhost/ConsoleOut0.rtc
```

以上で、コマンドラインを用いたコンポーネントの基本動作の確認は終了です。


