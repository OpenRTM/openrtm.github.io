---
layout: page
title: "openrtm-aistを10分で始めよう！"
---

<!-- Title: OpenRTM-aistを10分で始めよう！ -->
#contents

最新バージョンOpenRTM-aist-2.0.2-RELEASEではC++版、Python版、Java版、OpenRTP、rtshell がインストールされます。

# 事前準備
## Pythonのインストール
Pythonをインストールしていない場合は、OpenRTM-aistをインストールできません。
OpenRTM-aistをインストールする前に、Pythonをインストールしてください。バージョンは、"3.12"、"3.11"、"3.10"、"3.9"、"3.8"に対応しています。

Pythonのダウンロードは [OpenRTM-aist 2.0系のWindowsへのインストール]({{ site.baseurl }}/ja/doc/installation/install_2_0/install_windows_2_0/install_2_0) をご覧ください。

Pythonのインストール先は、インストール時の選択 [Customize installation]に対応しています。

サーチパスは、以下の方法で自動で設定されるようにしてください。こうすると、python.exeが置いてあるディレクトリとScriptsディレクトリがPathに追加されます。<br> (例: Path=C:\Python38;C:\ Python38\Scripts;...）

**[インストール手順]**

- Pythonインストーラーを起動します。ここではバージョン3.8を例に説明します。
- 最初の画面の下部にある[add python *** to PATH]にチェックを入れて、[Customize installation]を選択してください。


<div align="center"><img src="python38-install001_.png" width="50%;"></div>

- 次の[Optional Features]画面で変更はありません。[Next]を選択して進んでください。

<div align="center"><a href="python38-install002.png"><img src="python38-install002.png" width="50%;"></a></div>

- [Advanced Options]画面では、[Install for all users]にチェックを入れて、[Customize install location]でインストール先を設定してください。(例: Path=C:\Python38;C:\ Python38\Scripts;...）

<div align="center"><a href="python38-install003.png"><img src="python38-install003.png" width="50%;"></a></div>

- [Install] を選択してインストールを完了します。

## OpenRTM-aistのダウンロード

インストーラーのダウンロードは [ダウンロード]({{ site.baseurl }}/ja/download) をご覧ください。

Microsoft Edge をお使いで、下記メッセージが出てダウンロードできない場合の手順を紹介します。

<div align="center"><a href="msi-download-01.png"><img src="msi-download-01.png" width="50%;"></a></div>

- マウスオーバーで表示される「・・・」をクリックします

<div align="center"><a href="msi-download-02.png"><img src="msi-download-02.png" width="40%;"></a></div>

- 「保存」をクリックします

<div align="center"><a href="msi-download-03.png"><img src="msi-download-03.png" width="40%;"></a></div>

- 「詳細表示」をクリックします

<div align="center"><a href="msi-download-04.png"><img src="msi-download-04.png" width="40%;"></a></div>

- 「保存する」をクリックします

<div align="center"><a href="msi-download-05.png"><img src="msi-download-05.png" width="40%;"></a></div>

- これでダウンロードが完了しますので、「ファイルを開く」をクリックするとインストーラが起動します

<div align="center"><a href="msi-download-06.png"><img src="msi-download-06.png" width="40%;"></a></div>

## OpenRTM-aistのインストール

**[インストール手順]**
1. インストーラーを起動します。[WindowsによってPCが保護されました]の画面が表示されたら[詳細情報]をクリックして[実行]ボタンを表示させて、[実行]をクリックします。(この画面はWindowsのあるバージョン以降でMicrosoft Corp.に登録されていないアプリケーションのインストール時に表示される画面で、本ソフトウエアは登録をしていないため、この画面が表示されます。)
1. [次へ]をクリックします。ここではバージョン2.0.0の画像で説明していますが、2.0.2でも手順は同様です。
<div align="center"><a href="RTM2.0.0-msi-1.png"><img src="RTM2.0.0-msi-1.png" width="50%;"></a></div>
<br>
1. 使用承諾契約書のページです。ソフトウェアライセンス条項に同意して[次へ]をクリックします。
<div align="center"><a href="RTM2.0.0-msi-2.png"><img src="RTM2.0.0-msi-2.png" width="50%;"></a></div>
<br>
1. インストールの種類を選択します。デフォルトのまま[次へ]をクリックします。
<div align="center"><a href="RTM2.0.0-msi-3.png"><img src="RTM2.0.0-msi-3.png" width="50%;"></a></div>
<br>
1. Visual Studioのバージョンを選択します。
  - C++版で使用するVisual Studioのバージョンをシステム環境変数に設定します。
  - インストールされている Visual Studioのバージョンを選択して[次へ]をクリックします。
    - Visual Studioのダウンロードは [OpenRTM-aist 2.0系のWindowsへのインストール]({{ site.baseurl }}/ja/doc/installation/install_2_0/install_windows_2_0/install_2_0) をご覧ください。
    - Visual Studioのバージョンは、インストール終了後にツールのVCVerChangerで変更できます。[(VCVerChangerの使い方)]({{ site.baseurl }}/ja/content/vc_version_changer)
    - Python版、Java版では無関係ですのでデフォルトのまま[次へ]をクリックしてください。
<div align="center"><a href="RTM2.0.0-msi-4.png"><img src="RTM2.0.0-msi-4.png" width="50%;"></a></div>
<br>
1. セットアップの種類を選択します。
[標準]を選択した場合、OpenRTM-aistのC++版、Java版、Python版、OpenRTP、RTSystemEditorRCP、RTShell、OpenRTM-aist-C++版のVisual Studio 2015から2022までのランタイムライブラリ、OpenRTM-aist-1.0.0から2.0.0までのランタイムライブラリがインストールされます。特に変更理由がないようであれば[標準]をクリックします。
<br>
<div align="center"><a href="RTM2.0.0-msi-5.png"><img src="RTM2.0.0-msi-5.png" width="50%;"></a></div>
<br>
1. [インストール]をクリックするとインストールが開始されます。
<div align="center"><a href="RTM2.0.0-msi-6.png"><img src="RTM2.0.0-msi-6.png" width="50%;"></a></div>
<br>
<div align="center"><a href="RTM2.0.0-msi-7.png"><img src="RTM2.0.0-msi-7.png" width="50%;"></a></div>
<br>
1. インストールが終了しました。[完了]をクリックしてインストーラーを終了します。
<div align="center"><a href="RTM2.0.0-msi-8.png"><img src="RTM2.0.0-msi-8.png" width="50%;"></a></div>
<br>
<!-- ※使用しているVisual Studio のバージョンが2019(vc14)以外の場合は、以下のページを参考に環境変数のRTM_VC_VERSIONを変更してください。&br; -->
<!-- [[RTM_VC_VERSIONの変更:/ja/content/vc_version_changer]] -->

## VCVerChangerの実行

インストーラはOpenRTM-aistが使用するシステム環境変数をレジストリに登録しています。この環境変数の中に、他の環境変数である%RTM_VC_VERSION%を含むものがあります。
このようなネストされた環境変数が再帰的に展開されない場合があります。

解決のため、VCVerChanger を実行して下さい。「確認」ボタンを押すと、環境変数を展開してレジストリに書き戻します。
[(VCVerChangerの使い方)]({{ site.baseurl }}/ja/content/vc_version_changer)

## サンプルコンポーネントを実行する
### 事前準備
- 必須ではありませんが、ここからはスタートメニューに登録されたアプリケーションを多数起動します。毎回スタートメニューから順番にたどるのは大変ですので、
スタートボタンからスタートメニューを表示させ[OpenRTM-aist 2.0.2 x86_64]>[C++_Examples]を右クリックして[ファイルの場所を開く]を選択してください。
<br>
<div align="center"><a href="start-menu.png"><img src="start-menu.png" width="50%;"></a></div>
<div align="center"><strong>ファイルの場所を開く</strong></div>
<br>
<div align="center"><a href="start-menu-folder.png"><img src="start-menu-folder.png" width="50%;"></a></div><br>
<div align="center"><strong>スタートメニューフォルダー</strong></div>
<br>
  - このように、スタートメニューのフォルダーが開かれ、メニューに登録されているアプリケーションにアクセスしやすくなります。

## Naming Serviceの起動
- Start Naming Serviceをダブルクリックします。以下のようなコンソール画面が表示されます。
<div align="center"><a href="StartNameService122-001.png"><img src="StartNameService122-001.png" width="50%;"></a></div>
<div align="center"><strong>Start Naming Service</strong></div>
<br>
## サンプルコンポーネント
### ConsoleInComp、ConsoleOutCompを使用する
ConsoleInComp、ConsoleOutCompはDataInPort、DataOutPortの使用方法を示したサンプルです。ConsoleIn側で入力した数字が，ConsoleOut側に表示されます。ここではこの二つのコンポーネントを使用し、動作確認を行います。
### サンプルコンポーネントの起動
- [OpenRTM-aist 2.0.2 x86_64]>[C++_Example]フォルダー内のConsoleIn.batとConsoleOut.batをダブルクリックします。もし[Windows セキュリティのの重要な警告]画面が表示されたら[プライベートネットワーク(ホームネットワーク社内ネットワークなど)(R)]にチェックマークをつけて[アクセスを許可する(A)]をクリックしてください。以下のようなコンソール画面が表示されます。
<!-- CENTER:&ref(ConsoleIn001.png,center,90%);&ref(ConsoleOut001.png,center,90%); -->
<div align="center"><div align="center"><a href="ConsoleInOut122-001.png"><img src="ConsoleInOut122-001.png" width="90%;"></a></div>;</div>
<div align="center"><strong>ConsoleIn.batとConsoleOut.bat</strong></div>
<br>

&aname(openrtp_start);
## OpenRTP起動
- デスクトップのショートカットをクリックして起動します。スタートメニューでは、[OpenRTM-aist 2.0.2 x86_64]>[OpenRTP]と選択してください。先ほど開いたフォルダー画面からOpenRTPをダブルクリックすることによっても起動できます。
  - ワークスペースは適当な場所を指定してください。
<div align="center"><a href="OpenRTP122-001.png"><img src="OpenRTP122-001.png" width="50%;"></a></div>
<div align="center"><strong>ワークスペースの選択</strong></div>
<br>
- 「ようこそ」画面は必要ないので左上の[ようこそ]タブの[×]ボタンをクリックして画面を閉じてください。
<div align="center"><a href="OpenRTP122-002.png"><img src="OpenRTP122-002.png" width="50%;"></a></div>
<div align="center"><strong>初期起動時の画面</strong></div>
<br>

## RTSystemEditorの使用
- 画面右上の[パースペクティブを開く]をクリックします。表示されるダイアログで[RT System Editor]を選択して[開く]をクリックするとRTSystemEditorが起動します。
<div align="center"><div align="center"><a href="OpenRTP122-003.png"><img src="OpenRTP122-003.png" width="30%;"></a></div>;  <div align="center"><a href="OpenRTP122-004.png"><img src="OpenRTP122-004.png" width="30%;"></a></div>;</div>
<div align="center"><strong>パースペクティブの切り替え</strong></div>
<br>
- [NameServiceView]にコンポーネントが表示されます。最初は折りたたまれているため表示されていませんが、[>]をクリックし展開すると、ホスト名のホストコンテキストとConsoleIn、ConsoleOutコンポーネントが確認できます。設定により、ホストコンテキスト(図中 “TPAD-RTM-NO13|host_cxt” のような “ホスト名|host_cxt” の階層) が表示されず、直接コンポーネントが表示される場合もあります。
<div align="center"><a href="OpenRTP122-005.png"><img src="OpenRTP122-005.png" width="30%;"></a></div>
<div align="center"><strong>コンポーネント起動確認</strong></div>
<br>
  - NameServerViewにネームサーバーが表示されない時は、手動でlocalhostを追加します。画像の[ネームサーバを追加]をクリックしてダイアログを表示します。「localhost」と入力し[OK]をクリックして追加します。それでも起動されなかった場合は、一度すべてのコンソール画面を閉じてNaming Serviceの起動からの手順をやり直してみてください。
<div align="center"><div align="center"><a href="OpenRTP122-006.png"><img src="OpenRTP122-006.png" width="30%;"></a></div>;  <div align="center"><a href="OpenRTP122-007.png"><img src="OpenRTP122-007.png" width="30%;"></a></div>;</div>
<div align="center"><strong>ネームサーバの追加</strong></div>
<br>
- ツールバーから [Open New System Editor]をクリックして、[System Diagram]を表示します。
<div align="center"><a href="OpenRTP122-008.png"><img src="OpenRTP122-008.png" width="30%;"></a></div>
<div align="center"><strong>System Diagramを表示</strong></div>
<br>
- [NameServiceView]にあるConsoleIn、ConsoleOutのコンポーネントを[System Diagram]上にドラッグ＆ドロップすると、以下の画像のように表示されます。
<div align="center"><a href="OpenRTP122-009.png"><img src="OpenRTP122-009.png" width="30%;"></a></div>
<div align="center"><strong>コンポーネントをドラッグ＆ドロップ</strong></div>
<br>
- データポート間でドラッグ＆ドロップしてコンポーネントを接続します。その後、接続に必要な情報の入力を促すダイアログが表示されるので[OK]をクリックします。
<div align="center"><div align="center"><a href="OpenRTP122-010.png"><img src="OpenRTP122-010.png" width="30%;"></a></div>;  <div align="center"><a href="OpenRTP122-011.png"><img src="OpenRTP122-011.png" width="30%;"></a></div>;</div>
<div align="center"><strong>コンポーネント接続</strong></div>
<br>
  - 以下の画像のように接続されます。
<div align="center"><a href="OpenRTP122-012.png"><img src="OpenRTP122-012.png" width="30%;"></a></div>
<div align="center"><strong>接続完了</strong></div>
<br>
- コンポーネントの状態をActiveにします。[All Activate]クリックしてください。コンポーネントの色が青から明るい緑に変わったら成功です。コンポーネントは個別に選択して右クリックをすることに個別にActiveにすることも可能です。([All Activate]が表示されていない場合は、Openrtpを再起動してみてください。または、コンポーネントを個別にActiveにしても良いです。）
<div align="center"><a href="OpenRTP122-013.png"><img src="OpenRTP122-013.png" width="30%;"></a></div>
<br>
<div align="center"><a href="OpenRTP122-014.png"><img src="OpenRTP122-014.png" width="30%;"></a></div>
<div align="center"><strong>Activate完了</strong></div>
<br>
### コンポーネントのコンソール画面での動作確認
- 次にコンソール画面で動作確認します。RTSystemEditorで接続後、ConsoleIn画面に「Please input number:」と表示されます。
<div align="center"><a href="Console122-001.png"><img src="Console122-001.png" width="30%;"></a></div>
<div align="center"><strong>「Please input number:」と表示</strong></div>
<br>
- ConsoleIn画面で任意の数値を入力し[Enter]を押すと、ConsoleOut画面に数値が表示されます。
<div align="center"><div align="center"><a href="Console122-002.png"><img src="Console122-002.png" width="50%;"></a></div>;</div>
<div align="center"><strong>動作確認</strong></div>
<br>
  - 数値以外の入力や、大きすぎる数値を入力すると動作がおかしくなることがあります。その場合はCntrl-Cキーでバッチファイルの動作を停止させ、再度バッチファイルの起動からやり直してください。
- コンポーネントを終了する場合は、ツールバーから[All Deactivate]をクリックします。その後、コンポーネントを右クリックして[Exit]してください。
  - Deactivateに時間がかかる場合はConsoleInの数値入力で止まっているので、その場合は何か数値を入力してください。
<div align="center"><a href="Console122-004.png"><img src="Console122-004.png" width="50%;"></a></div>
<div align="center"><strong>コンポーネントのDeactivate</strong></div>
<br>
<div align="center"><a href="Console122-005.png"><img src="Console122-005.png" width="50%;"></a></div>
<div align="center"><strong>コンポーネントの終了</strong></div>
<br>
- 以上でConsoleInとConsoleOutを使用した動作確認は終了です。

## rtshellを利用する
OpenRTM-aistではrtshellが標準でインストールされます。
rtshellを利用することでコマンドラインからRTCのActivate、Deactivate、終了等ができるようになります。<br>
[rtshellのインストール・動作確認(Windows編)]({{ site.baseurl }}/ja/doc/installation/install_rtshell/check_windows) をご覧ください。


## 次は...
下記リンク先をご覧ください。
- **もっとサンプルを動かしてみる　&t;：　**[サンプルコンポーネント]({{ site.baseurl }}/ja/doc/installation/sample_components)
- **コンポーネントを作ってみる　　&t;：　**[ケーススタディー]({{ site.baseurl }}/ja/doc/casestudy)
- **OpenRTMの基礎から学ぶ　　　&t;：　**[デベロッパーズガイド]({{ site.baseurl }}/ja/doc/developersguide)
- **コミュニティーに参加する　　　&t;：　**[コミュニティー]({{ site.baseurl }}/ja/community)
- **公開コンポーネントを見てみる　&t;：　**[プロジェクト]({{ site.baseurl }}/ja/node/123)（Projectページ(プロジェクト,node/123)はリンク切れです）


