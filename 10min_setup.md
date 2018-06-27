
## 10分で始めよう



<a name="startup_openrtm"></a>
最新バージョン OpenRTM-aist-1.1.2-RELEASE では C++版、Python版、Java版を一度にインストールできるようになりました。 また、これまで別途インストールしていた rtshell も同時にインストール可能になりました。

### Python 2.7 インストール

Python 2.7 をインストールしていない場合は、OpenRTM-aist はインストールできません。先に Python2.7 をインストールしてください。

インストールの際は、「Add python.exe to Path」の設定を変更し、「Will be installed on local hard drive」を選択してください。
こうすると、python.exe と Scripts に PATH を通してくれます。　（例：Path=C:\Python27\;C:\Python27\Scripts;...）

![Python 2.7 PATHを通す](./images/10min_setup/python27_install.jpg)


### OpenRTM-aist インストール


ここでは32bit用インストーラー OpenRTM-aist-1.1.2-RELEASE_x86.msi を使った手順を紹介します。 インストーラーのダウンロードは、OpenRTM-aist-1.1.2-RELEASE<リンク> をご覧ください。

1. インストーラーを起動し、[次へ] をクリックします。

![](./images/10min_setup/install1.png)

2. 使用承諾契約書のページです。ソフトウェアライセンス条項に同意して、[次へ] をクリックします。

![](./images/10min_setup/install2.png)

3. インストールの種類を選択します。どちらかを選択して、[次へ] をクリックします。 

![](./images/10min_setup/install3.png)

4. セットアップの種類を選択します。[標準] を選択した場合、OpenRTM-aist の C++版、Java版、Python版、OpenRTP、RTSystemEditorRCP、RTShell、OpenRTM-aist-C++版の Visual Studio 2008 から 2015 までのランタイムライブラリ、OpenRTM-aist-1.0.0 から 1.1.1 までのランタイムライブラリがインストールされます。特に変更理由がないようであれば、[標準] をクリックします。

![](./images/10min_setup/install4.png)

5. [インストール] をクリックするとインストールが開始します。 

![](./images/10min_setup/install5.png)

![](./images/10min_setup/install6.png)

6. インストールが終了しました。[完了] をクリックしてインストーラーを終了します。

![インストール終了画面](./images/10min_setup/install7.png)

※使用している Visual Studio のバージョンが2013(vc12)以外の場合は、環境変数の RTM_VC_VERSION を変更してください。


### サンプルコンポーネントを実行する

必須ではありませんが、ここからはスタートメニューに登録されたアプリケーションを多数起動します。毎回スタートメニューから順番にたどるのは大変ですので、


![ファイルの場所を開く](./images/10min_setup/install8.png)

スタート画面の左下隅の矢印からアプリビューを表示して、OpenRTM-aist-1.1.2 の OpenRTP で右クリックし、[ファイルの場所を開く] を選択してください。

そして1つ上のフォルダーに移動してください。

![スタートメニューフォルダー](./images/10min_setup/install31.png)

このように、スタートメニューのフォルダーが開かれ、様々なアプリケーションにアクセスしやすくなります。 では、インストールされたサンプルコンポーネントを実行してみます。

#### ConsoleInComp、ConsoleOutCompを使用する

ConsoleInComp、ConsoleOutComp は DataInPort、DataOutPort の使用方法を示したサンプルです。ConsoleIn 側で入力した数字が，ConsoleOut 側に表示されます。

##### rtm-naming起動

[OpenRTM-aist 1.1.2] > [Tools] の Start Naming Service をクリックして起動します。

![Start Naming Service](./images/10min_setup/install30.png)

##### サンプルコンポーネント起動

[OpenRTM-aist 1.1.2] > [C++] > [Components] > [Examples] の ConsoleInComp.exe と ConsoleOutComp.exe をクリックするとコンソール画面が起動します。 

![ConsoleInComp.exeとConsoleOutComp.exe](./images/10min_setup/install29.png)

##### OpenRTP起動

ここから OpenRTP を操作します。[OpenRTM-aist 1.1.2] > [Tools] の OpenRTP をクリックして起動します。 ワークスペースは適当な場所を指定してください。

![ワークスペースの選択](./images/10min_setup/install40.png)

「ようこそ」画面は今のところ必要ないので左上の [ようこそ] タブの [×] ボタンをクリックして画面を閉じてください。

![初期起動時の画面](./images/10min_setup/install41.png)

右上の「パースペクティブを開く」をクリックし、「RT System Editor」を選択することで、RTSystemEditor が起動します。

![](./images/10min_setup/install42.png)
![パースペクティブの切り替え](./images/10min_setup/install43.png)


※NameServerView にネームサーバーが表示されない時は、手動で localhost を追加します。画像の [ネームサーバの追加] をクリックしダイアログを表示します。localhost と入力し、[OK] をクリックして追加します。

![ネームサーバの追加](./images/10min_setup/install44.png)

NameServiceView にコンポーネントが表示されます。最初は折りたたまれて非表示です。[>] をクリックし展開すると、ConsoleInComp、ConsoleOutCompコンポーネントを確認できます。

![コンポーネント起動確認](./images/10min_setup/install45.png)

[OpenNewSystemEditor] をクリックして、SystemDiagram を表示します。

![SystemDiagramを表示](./images/10min_setup/install46.png)

NameServiceView のコンポーネントをシステム・ダイアグラムにドラッグ＆ドロップすると画像のように表示されます。

![コンポーネントをドラッグ＆ドロップ](./images/10min_setup/install47.png)

コンポーネントを接続します。データポート間でドラッグ＆ドロップ後、接続に必要な情報の入力を促すダイアログが表示されるので、[OK] をクリックします。

![コンポーネント接続](./images/10min_setup/install48.png)
![コンポーネント接続](./images/10min_setup/install49.png)

接続が完了しました。

![接続完了](./images/10min_setup/install50.png)

コンポーネントの状態を Activate にします。[All Activate] クリックしてください。コンポーネントの色が青から明るい緑に変わったら成功です。コンポーネントは個別に選択して Activate にすることも可能です。

![Activate完了](./images/10min_setup/install51.png)
![Activate完了](./images/10min_setup/install52.png)

次にコンソール画面で動作確認します。RTSystemEditor で接続後、ConsoleInComp.exe コンソールに、「Please input number:」と表示されます。

![ConsoleInComp.exeとConsoleOutComp.exe](./images/10min_setup/install24.png)

ConsoleInComp.exe コンソール画面を選択し、数値を入力し [Enter] を押すと、ConsoleOutComp.exe コンソールに数値が表示されます。

![動作確認](./images/10min_setup/install25.png)
![動作確認](./images/10min_setup/install26.png)

※数値以外の入力や、大きすぎる数値を入力するとエラー(赤)になります。 ※コンポーネントがエラーを起こしたら、RTSystemEditor でコンポーネントを右クリックして Reset を選択してください。


以上で ConsoleInComp.exe と ConsoleOutComp.exe を使用した動作確認は終了です。コンポーネントを終了する場合は、Deactivate してから Exit して下さい。

![コンポーネント非アクティブ化](./images/10min_setup/install53.png)

![コンポーネント終了](./images/10min_setup/install54.png)

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

![コマンドプロンプトの起動](./images/10min_setup/install32.png)

まず、C:\Python27\Scripts にパスを設定していない場合は以下のコマンドでパスを設定してください。

    set PATH=C:\Python27\Scripts;%PATH%

次に以下のコマンドでデータポートを接続します。

    rtcon /localhost/ConsoleIn0.rtc:out /localhost/ConsoleOut0.rtc:in

すると ConsoleIn.py、ConsoleOut.py コンソールに以下のような文字列が表示されます。

   ------------------------------
   Listener:        ON_CONNECT
   Profile::name:   outin
   Profile::id:     4d622f80-135f-11e6-b923-001c4231a7a3
   ------------------------------

![データポート接続の表示](./images/10min_setup/install36.png)

念のために RTシステムエディタで確認します。
NameServiceView のコンポーネントをシステム・ダイアグラムにドラッグ＆ドロップすると、 データポートが接続されたことが確認できます。


![データポート接続の確認](./images/10min_setup/install55.png)

そして以下のコマンドで RTC をアクティブ化します。

    rtact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc

アクティブ化に成功していると ConsoleIn.py コンソールに、「Please input number:」と表示されます。

RTシステムエディタを見てみると、RTC がアクティブ化されたことが確認できます。

![アクティブ化の確認](./images/10min_setup/install56.png)

そして ConsoleIn.py コンソール画面で数値を入力すると、ConsoleOut.py コンソールに数値が表示されます。

![ConsoleIn.py と ConsoleOut.py](./images/10min_setup/install38.png)

以下のコマンドで RTC を非アクティブ化してください。

   rtdeact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc
※ConsoleIn が非アクティブ化できない場合、数値入力で止まっているので何か数値を入力してください。

最後に以下のコマンドで RTC を終了させてください。

   rtexit /localhost/ConsoleIn0.rtc
   rtexit /localhost/ConsoleOut0.rtc
