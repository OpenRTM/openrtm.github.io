---
layout: page
title: openrtm-aistを10分で始めよう！
---

<!-- Title: OpenRTM-aistを10分で始めよう！ -->
#contents

最新バージョンOpenRTM-aist-2.1.0-RELEASEではC++版、Python版、Java版、OpenRTP、rtshell がインストールされます。

# 事前準備
## Pythonのインストール
Pythonをインストールしていない場合は、OpenRTM-aistをインストールできません。
OpenRTM-aistをインストールする前に、Pythonをインストールしてください。バージョンは、"3.14"、"3.13"、"3.12"、"3.11"、"3.10"に対応しています。

Pythonのダウンロードは [OpenRTM-aist 2.1系のWindowsへのインストール]({{ site.baseurl }}/ja/doc/installation/install_2_1/install_windows_2_1/install_2_1) をご覧ください。

Pythonのインストール先は、インストール時の選択 [Customize installation]に対応しています。

サーチパスは、以下の方法で自動で設定されるようにしてください。こうすると、python.exeが置いてあるディレクトリとScriptsディレクトリがPathに追加されます。<br> (例: Path=C:\Python313;C:\ Python313\Scripts;...）

**[インストール手順]**

- Pythonインストーラーを起動します。ここではバージョン3.13を例に説明します。
- 最初の画面の下部にある[add python *** to PATH]にチェックを入れて、[Customize installation]を選択してください。


<div align="center"><a href="py313_install_1.png"><img src="py313_install_1.png" width="70%;"></a></div>

- 次の[Optional Features]画面で変更はありません。[Next]を選択して進んでください。

<div align="center"><a href="py313_install_2.png"><img src="py313_install_2.png" width="70%;"></a></div>

- [Advanced Options]画面では、[Install for all users]にチェックを入れて、[Customize install location]でインストール先を設定してください。(例: Path=C:\Python313;C:\ Python313\Scripts;...）

<div align="center"><a href="py313_install_3.png"><img src="py313_install_3.png" width="70%;"></a></div>

- [Install] を選択してインストールを完了します。

## OpenRTM-aistのダウンロード

インストーラーのダウンロードは [ダウンロード]({{ site.baseurl }}/ja/download) をご覧ください。

Microsoft Edge をお使いで、下記メッセージが出てダウンロードできない場合の手順を紹介します。

<div align="center"><a href="edge-download-01.png"><img src="edge-download-01.png" width="70%;"></a></div>

- マウスオーバーで表示される「・・・」をクリックします

<div align="center"><a href="edge-download-02.png"><img src="edge-download-02.png" width="70%;"></a></div>

- 「保存」をクリックします

<div align="center"><a href="edge-download-03.png"><img src="edge-download-03.png" width="60%;"></a></div>

- 「削除」横の「レ（チェックマーク）」をクリックして表示される「保持する」をクリックします

<div align="center"><a href="edge-download-04.png"><img src="edge-download-04.png" width="50%;"></a></div>

- これでダウンロードが完了しますので、「ファイルを開く」をクリックするとインストーラが起動します

## OpenRTM-aistのインストール

**[インストール手順]**
1. インストーラーを起動し、 [次へ]をクリックします。
<div align="center"><a href="RTM210_msi_1.png"><img src="RTM210_msi_1.png" width="90%;"></a></div>
<br>
1. 使用承諾契約書のページです。ソフトウェアライセンス条項に同意して[次へ]をクリックします。
<div align="center"><a href="RTM210_msi_2.png"><img src="RTM210_msi_2.png" width="90%;"></a></div>
<br>
1. インストールの種類を選択します。デフォルトのまま[次へ]をクリックします。
<div align="center"><a href="RTM210_msi_3.png"><img src="RTM210_msi_3.png" width="90%;"></a></div>
<br>
1. セットアップの種類を選択します。
[標準]をクリックすることで全機能がインストールされます。
<br>
<div align="center"><a href="RTM210_msi_4.png"><img src="RTM210_msi_4.png" width="90%;"></a></div>
<br>
1. インストールが終了しました。[完了]をクリックしてインストーラーを終了します。
<div align="center"><a href="RTM210_msi_5.png"><img src="RTM210_msi_5.png" width="90%;"></a></div>
<br>
<!-- ※使用しているVisual Studio のバージョンが2019(vc14)以外の場合は、以下のページを参考に環境変数のRTM_VC_VERSIONを変更してください。&br; -->
<!-- [[RTM_VC_VERSIONの変更:/ja/node/6136/]] -->

## システム環境変数確認

ネストされた環境変数が再帰的に展開されないケースが発生することを確認していますが、ツールのVerChangerで解決できます。詳細は下記ページをご覧ください。
    - [システム環境変数確認]({{ site.baseurl }}/ja/doc/installation/install_2_1/install_windows_2_1/install_2_1#toc9)

## サンプルコンポーネントを実行する

OpenRTPのRTSystemEditor機能を使い、２つのRTCの接続動作を確認する手順を説明します。

&aname(openrtp_start);
### OpenRTP起動
- デスクトップのショートカットをクリックして起動します。
<div align="center"><a href="OpenRTP210-001.png"><img src="OpenRTP210-001.png" width="70%;"></a></div>
<div align="center"><strong>OpenRTP起動</strong></div>

  - ワークスペースは適当な場所を指定してください。
<div align="center"><a href="OpenRTP122-001.png"><img src="OpenRTP122-001.png" width="70%;"></a></div>
<div align="center"><strong>ワークスペースの選択</strong></div>
<br>
- 「ようこそ」画面は必要ないので左上の[ようこそ]タブの[×]ボタンをクリックして画面を閉じてください。
<div align="center"><a href="OpenRTP122-002.png"><img src="OpenRTP122-002.png" width="70%;"></a></div>
<div align="center"><strong>初期起動時の画面</strong></div>
<br>

### RTSystemEditorの使用
- 画面右上の[パースペクティブを開く]をクリックします。表示されるダイアログで[RT System Editor]を選択して[開く]をクリックするとRTSystemEditorが起動します。
<div align="center"><div align="center"><a href="OpenRTP122-003.png"><img src="OpenRTP122-003.png" width="70%;"></a></div>;  <div align="center"><a href="OpenRTP122-004.png"><img src="OpenRTP122-004.png" width="70%;"></a></div>;</div>
<div align="center"><strong>パースペクティブの切り替え</strong></div>
<br>

- 初回起動時のみ「ツールバーの起動に失敗しました。」のダイアログが表示されるので、指示通りにOpenRTPを終了させて再度起動してください。
<div align="center"><a href="OpenRTP210-002.png"><img src="OpenRTP210-002.png" width="70%;"></a></div>
<div align="center"><strong>OpenRTPを再起動</strong></div>

- ネームサービス起動ボタンを押してネームサーバのlocalhostを起動してください。
<div align="center"><div align="center"><a href="OpenRTP210-003.png"><img src="OpenRTP210-003.png" width="70%;"></a></div>;  <div align="center"><a href="OpenRTP210-004.png"><img src="OpenRTP210-004.png" width="70%;"></a></div>;</div>
<div align="center"><strong>ネームサービス起動</strong></div>

### C++のConsoleIn、ConsoleOutを起動
- Windowsの検索窓に小文字で構わないので、「c++_e」 まで入力すると C++_Examples の候補が表示されるのでクリックしてください。
<div align="center"><a href="menu-c++RTC_001.png"><img src="menu-c++RTC_001.png" width="70%;"></a></div>
<div align="center"><strong>C++_Examplesを選択</strong></div>

- C++のサンプルRTCの一覧が表示されますので、ConsoleInとConsoleOutをダブルクリックで起動してください。
<div align="center"><a href="menu-c++RTC_002.png"><img src="menu-c++RTC_002.png" width="20%;"></a></div>
<div align="center"><strong>ConsoleInとConsoleOutを起動</strong></div>

<br>


- 起動すると以下のようなコンソール画面が表示されます。
<!-- CENTER:&ref(ConsoleIn001.png,center,90%);&ref(ConsoleOut001.png,center,90%); -->
<div align="center"><div align="center"><a href="ConsoleInOut122-001.png"><img src="ConsoleInOut122-001.png" width="90%;"></a></div>;</div>
<div align="center"><strong>ConsoleIn.batとConsoleOut.bat</strong></div>
<br>


- ツールバーから [Open New System Editor]をクリックして、[System Diagram]を表示します。
<div align="center"><a href="OpenRTP122-008.png"><img src="OpenRTP122-008.png" width="70%;"></a></div>
<div align="center"><strong>System Diagramを表示</strong></div>
<br>
- [NameServiceView]にあるConsoleIn、ConsoleOutのコンポーネントを[System Diagram]上にドラッグ＆ドロップすると、以下の画像のように表示されます。
<div align="center"><a href="OpenRTP122-009.png"><img src="OpenRTP122-009.png" width="70%;"></a></div>
<div align="center"><strong>コンポーネントをドラッグ＆ドロップ</strong></div>
<br>
- データポート間でドラッグ＆ドロップしてコンポーネントを接続します。その後、接続に必要な情報の入力を促すダイアログが表示されるので[OK]をクリックします。
<div align="center"><div align="center"><a href="OpenRTP122-010.png"><img src="OpenRTP122-010.png" width="70%;"></a></div>;  <div align="center"><a href="OpenRTP122-011.png"><img src="OpenRTP122-011.png" width="70%;"></a></div>;</div>
<div align="center"><strong>コンポーネント接続</strong></div>
<br>
  - 以下の画像のように接続されます。
<div align="center"><a href="OpenRTP122-012.png"><img src="OpenRTP122-012.png" width="70%;"></a></div>
<div align="center"><strong>接続完了</strong></div>
<br>
- コンポーネントの状態をActiveにします。[All Activate]クリックしてください。コンポーネントの色が青から明るい緑に変わったら成功です。コンポーネントは個別に選択して右クリックをすることに個別にActiveにすることも可能です。([All Activate]が表示されていない場合は、Openrtpを再起動してみてください。または、コンポーネントを個別にActiveにしても良いです。）
<div align="center"><a href="OpenRTP122-013.png"><img src="OpenRTP122-013.png" width="70%;"></a></div>
<br>
<div align="center"><a href="OpenRTP122-014.png"><img src="OpenRTP122-014.png" width="70%;"></a></div>
<div align="center"><strong>Activate完了</strong></div>
<br>
### コンポーネントのコンソール画面での動作確認
- 次にコンソール画面で動作確認します。RTSystemEditorで接続後、ConsoleIn画面に「Please input number:」と表示されます。
<div align="center"><a href="Console122-001.png"><img src="Console122-001.png" width="70%;"></a></div>
<div align="center"><strong>「Please input number:」と表示</strong></div>
<br>
- ConsoleIn画面で任意の数値を入力し[Enter]を押すと、ConsoleOut画面に数値が表示されます。
<div align="center"><div align="center"><a href="Console122-002.png"><img src="Console122-002.png" width="90%;"></a></div>;</div>
<div align="center"><strong>動作確認</strong></div>
<br>
  - 数値以外の入力や、大きすぎる数値を入力すると動作がおかしくなることがあります。その場合はCntrl-Cキーでバッチファイルの動作を停止させ、再度バッチファイルの起動からやり直してください。
- コンポーネントを終了する場合は、ツールバーから[All Deactivate]をクリックします。その後、コンポーネントを右クリックして[Exit]してください。
  - Deactivateに時間がかかる場合はConsoleInの数値入力で止まっているので、その場合は何か数値を入力してください。
<div align="center"><a href="Console122-004.png"><img src="Console122-004.png" width="70%;"></a></div>
<div align="center"><strong>コンポーネントのDeactivate</strong></div>
<br>
<div align="center"><a href="Console122-005.png"><img src="Console122-005.png" width="70%;"></a></div>
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
- **公開コンポーネントを見てみる　&t;：　**[プロジェクト](/ja/node/123)（Projectページ(プロジェクト,node/123)はリンク切れです）



