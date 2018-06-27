
## 10分で始めよう



<a name="startup_openrtm"></a>
最新バージョン OpenRTM-aist-1.1.2-RELEASE では C++版、Python版、Java版を一度にインストールできるようになりました。 また、これまで別途インストールしていた rtshell も同時にインストール可能になりました。

### Python 2.7 インストール

Python 2.7 をインストールしていない場合は、OpenRTM-aist はインストールできません。先に Python2.7 をインストールしてください。

インストールの際は、「Add python.exe to Path」の設定を変更し、「Will be installed on local hard drive」を選択してください。
こうすると、python.exe と Scripts に PATH を通してくれます。　（例：Path=C:\Python27\;C:\Python27\Scripts;...）

<img src="./images/10min_setup/python27_install.jpg" width="300">


### OpenRTM-aist インストール


ここでは32bit用インストーラー OpenRTM-aist-1.1.2-RELEASE_x86.msi を使った手順を紹介します。 インストーラーのダウンロードは、OpenRTM-aist-1.1.2-RELEASE<リンク> をご覧ください。

1. インストーラーを起動し、[次へ] をクリックします。

<img src="./images/10min_setup/install1.png width="300">


2. 使用承諾契約書のページです。ソフトウェアライセンス条項に同意して、[次へ] をクリックします。

<img src="./images/10min_setup/install2.png width="300">


3. インストールの種類を選択します。どちらかを選択して、[次へ] をクリックします。 

<img src="./images/10min_setup/install3.png width="300">


4. セットアップの種類を選択します。[標準] を選択した場合、OpenRTM-aist の C++版、Java版、Python版、OpenRTP、RTSystemEditorRCP、RTShell、OpenRTM-aist-C++版の Visual Studio 2008 から 2015 までのランタイムライブラリ、OpenRTM-aist-1.0.0 から 1.1.1 までのランタイムライブラリがインストールされます。特に変更理由がないようであれば、[標準] をクリックします。

<img src="./images/10min_setup/install4.png width="300">


5. [インストール] をクリックするとインストールが開始します。 

<img src="./images/10min_setup/install5.png width="300">



<img src="./images/10min_setup/install6.png width="300">


6. インストールが終了しました。[完了] をクリックしてインストーラーを終了します。

<img src="./images/10min_setup/install7.png width="300">

<b>インストール終了画面</b>

※使用している Visual Studio のバージョンが2013(vc12)以外の場合は、環境変数の RTM_VC_VERSION を変更してください。


### サンプルコンポーネントを実行する

必須ではありませんが、ここからはスタートメニューに登録されたアプリケーションを多数起動します。毎回スタートメニューから順番にたどるのは大変ですので、

<img src="./images/10min_setup/install8.png width="300">

<b>ファイルの場所を開く</b>

スタート画面の左下隅の矢印からアプリビューを表示して、OpenRTM-aist-1.1.2 の OpenRTP で右クリックし、[ファイルの場所を開く] を選択してください。

そして1つ上のフォルダーに移動してください。

<img src="./images/10min_setup/install31.png width="300">

<b>スタートメニューフォルダー</b>

このように、スタートメニューのフォルダーが開かれ、様々なアプリケーションにアクセスしやすくなります。 では、インストールされたサンプルコンポーネントを実行してみます。

#### ConsoleInComp、ConsoleOutCompを使用する

ConsoleInComp、ConsoleOutComp は DataInPort、DataOutPort の使用方法を示したサンプルです。ConsoleIn 側で入力した数字が，ConsoleOut 側に表示されます。

##### rtm-naming起動

[OpenRTM-aist 1.1.2] > [Tools] の Start Naming Service をクリックして起動します。

<img src="./images/10min_setup/install30.png width="300">

<b>Start Naming Service</b>

##### サンプルコンポーネント起動

[OpenRTM-aist 1.1.2] > [C++] > [Components] > [Examples] の ConsoleInComp.exe と ConsoleOutComp.exe をクリックするとコンソール画面が起動します。 

<img src="./images/10min_setup/install29.png width="300">

<b>ConsoleInComp.exeとConsoleOutComp.exe</b>

##### OpenRTP起動

ここから OpenRTP を操作します。[OpenRTM-aist 1.1.2] > [Tools] の OpenRTP をクリックして起動します。 ワークスペースは適当な場所を指定してください。

<img src="./images/10min_setup/install40.png width="300">

<b>ワークスペースの選択</b>


「ようこそ」画面は今のところ必要ないので左上の [ようこそ] タブの [×] ボタンをクリックして画面を閉じてください。

<img src="./images/10min_setup/install41.png width="300">

<b>初期起動時の画面</b>

右上の「パースペクティブを開く」をクリックし、「RT System Editor」を選択することで、RTSystemEditor が起動します。

<img src="./images/10min_setup/install42.png width="300">

<img src="./images/10min_setup/install43.png width="300">

<b>パースペクティブの切り替え</b>

※NameServerView にネームサーバーが表示されない時は、手動で localhost を追加します。画像の [ネームサーバの追加] をクリックしダイアログを表示します。localhost と入力し、[OK] をクリックして追加します。

<img src="./images/10min_setup/install44.png width="300">

<b>ネームサーバの追加</b>

NameServiceView にコンポーネントが表示されます。最初は折りたたまれて非表示です。[>] をクリックし展開すると、ConsoleInComp、ConsoleOutCompコンポーネントを確認できます。

<img src="./images/10min_setup/install45.png width="300">

<b>コンポーネント起動確認</b>

[OpenNewSystemEditor] をクリックして、SystemDiagram を表示します。

<img src="./images/10min_setup/install46.png width="300">

<b>SystemDiagramを表示</b>

NameServiceView のコンポーネントをシステム・ダイアグラムにドラッグ＆ドロップすると画像のように表示されます。

<img src="./images/10min_setup/install47.png width="300">

<b>コンポーネントをドラッグ＆ドロップ</b>

コンポーネントを接続します。データポート間でドラッグ＆ドロップ後、接続に必要な情報の入力を促すダイアログが表示されるので、[OK] をクリックします。


<img src="./images/10min_setup/install48.png width="300">


<img src="./images/10min_setup/install49.png width="300">

<b>コンポーネント接続</b>

接続が完了しました。

<img src="./images/10min_setup/install50.png width="300">

<b>接続完了</b>

コンポーネントの状態を Activate にします。[All Activate] クリックしてください。コンポーネントの色が青から明るい緑に変わったら成功です。コンポーネントは個別に選択して Activate にすることも可能です。


<img src="./images/10min_setup/install51.png width="300">

<img src="./images/10min_setup/install52.png width="300">


<b>Activate完了</b>

次にコンソール画面で動作確認します。RTSystemEditor で接続後、ConsoleInComp.exe コンソールに、「Please input number:」と表示されます。


<img src="./images/10min_setup/install24.png width="300">

<b>ConsoleInComp.exeとConsoleOutComp.exe</b>

ConsoleInComp.exe コンソール画面を選択し、数値を入力し [Enter] を押すと、ConsoleOutComp.exe コンソールに数値が表示されます。

<img src="./images/10min_setup/install25.png width="300">

<img src="./images/10min_setup/install26.png width="300">

<b>動作確認</b>

※数値以外の入力や、大きすぎる数値を入力するとエラー(赤)になります。 ※コンポーネントがエラーを起こしたら、RTSystemEditor でコンポーネントを右クリックして Reset を選択してください。


以上で ConsoleInComp.exe と ConsoleOutComp.exe を使用した動作確認は終了です。コンポーネントを終了する場合は、Deactivate してから Exit して下さい。

<img src="./images/10min_setup/install53.png width="300">

<b>コンポーネント非アクティブ化</b>

<img src="./images/10min_setup/install54.png width="300">

<b>コンポーネント終了</b>

※Deactivate に時間がかかる場合は ConsoleInComp.exe の数値入力で止まっているので、何か数値を入力してください。

### rtshell を利用する

OpenRTM-aist-1.1.2 では rtshell が標準でインストールされます。 rtshell を利用することでコマンドラインから RTC のアクティブ化、非アクティブ化、終了等ができるようになります。

※64bit版をインストールした場合に dll の不足により動作できない場合があります。その場合は Windows Update を実行してください。

#### RTC の操作

サンプルコンポーネントを起動し、rtshell によりコマンドラインからデータポートの接続、RTC のアクティブ化、非アクティブ化、終了を行います。


##### rtm-naming起動

[OpenRTM-aist 1.1.2] > [Tools] の Start Naming Service をクリックして起動します。

##### サンプルコンポーネント起動

まずはサンプルコンポーネントを起動して、起動したコンポーネントを rtshell で操作します。 [OpenRTM-aist 1.1.2] > [Python] > [Components] > [Examples] のConsoleIn.py と ConsoleOut.py をクリックするとコンソール画面が起動します。

ConsoleIn.py、ConsoleOut.py と ConsoleInComp.exe、ConsoleOutComp.exe の基本的な動作は同じです。

##### コマンドプロンプトからの操作

次にコマンドプロンプトを起動してください。


<img src="./images/10min_setup/install32.png width="300">

<b>コマンドプロンプトの起動</b>

まず、C:\Python27\Scripts にパスを設定していない場合は以下のコマンドでパスを設定してください。

    set PATH=C:\Python27\Scripts;%PATH%

次に以下のコマンドでデータポートを接続します。

    rtcon /localhost/ConsoleIn0.rtc:out /localhost/ConsoleOut0.rtc:in

すると ConsoleIn.py、ConsoleOut.py コンソールに以下のような文字列が表示されます。


   Listener:        ON_CONNECT
   Profile::name:   outin
   Profile::id:     4d622f80-135f-11e6-b923-001c4231a7a3


<img src="./images/10min_setup/install36.png width="300">

<b>データポート接続の表示</b>

念のために RTシステムエディタで確認します。
NameServiceView のコンポーネントをシステム・ダイアグラムにドラッグ＆ドロップすると、 データポートが接続されたことが確認できます。


<img src="./images/10min_setup/install55.png width="300">

<b>データポート接続の確認</b>

そして以下のコマンドで RTC をアクティブ化します。

    rtact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc

アクティブ化に成功していると ConsoleIn.py コンソールに、「Please input number:」と表示されます。

RTシステムエディタを見てみると、RTC がアクティブ化されたことが確認できます。

<img src="./images/10min_setup/install56.png width="300">

<b>アクティブ化の確認</b>


そして ConsoleIn.py コンソール画面で数値を入力すると、ConsoleOut.py コンソールに数値が表示されます。


<img src="./images/10min_setup/install38.png width="300">

<b>ConsoleIn.py と ConsoleOut.py</b>

以下のコマンドで RTC を非アクティブ化してください。

   rtdeact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc

※ConsoleIn が非アクティブ化できない場合、数値入力で止まっているので何か数値を入力してください。

最後に以下のコマンドで RTC を終了させてください。

   rtexit /localhost/ConsoleIn0.rtc

   rtexit /localhost/ConsoleOut0.rtc
