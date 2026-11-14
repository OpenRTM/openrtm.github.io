---
layout: page
title: openrtpの起動手順(1.2系、windows)
---

<!-- Title: OpenRTPの起動手順(1.2系、Windows) -->
#contents

## OpenRTPの起動
RTCの操作、RTシステムの構築を行うためのツールRTSystemEditorを起動します。
RTSystemEditorはOpenRTPというツールの中に含まれているため、まずはOpenRTPを起動する必要があります。
デスクトップのショートカットをダブルクリックするか、Windows 10の場合は左下の[ここに入力して検索]に**OpenRTP**と入力して検索結果に表示される[OpenRTP]をクリックして起動してください。

<div align="center"><a href="rtm1.png"><img src="rtm1.png" width="30%;"></a></div>
<div align="center"><strong>デスクトップのショートカット</strong></div>


<div align="center"><a href="rtm2.png"><img src="rtm2.png" width="50%;"></a></div>
<div align="center"><strong>ここに入力して検索</strong></div>

### ワークスペースの選択とEclipseへようこそ
OpenRTPの最初の起動時にはワークスペースとして使用するディレクトリの場所を聞いてきます。それを設定して、今後同じ設定で使い、再度聞かれる必要がない場合は、[この設定をデフォルトとして使用し、今後この質問を表示しない(U)]のチェックボックスをクリックし、チェックの後、[起動]ボタンをクリックしてください。また最初の起動時に[eclipseへようこそ]の画面が開く場合があります。その場合は、左上部の[ようこそ]タブにある[X]ボタンをクリックして閉じてください。

### RTSystemEditor(RTSE)の起動

OpenRTPの[パースペクティブを開く]ボタンをクリックしてください。

<div align="center"><a href="rtm3.png"><img src="rtm3.png" width="60%;"></a></div>
<div align="center"><strong>パースペクティブを開くをクリック</strong></div>

パースペクティブを開くウィンドウから[RTSystemEditor]を選択して[開く]ボタンをクリックしてください。

<div align="center"><a href="rtm4.png"><img src="rtm4.png" width="50%;"></a></div>
<div align="center"><strong>RTSystemEditorの起動</strong></div>

## ネームサーバーの起動
まず、コンポーネントの参照を登録するためのネームサーバーを起動します。

<div align="center"><a href="rtm5.png"><img src="rtm5.png" width="60%;"></a></div>
<div align="center"><strong>ネームサーバーの起動</strong></div>

## Windows Defenderからの警告

ネームサーバーを起動しようとすると、Windows Defenderのファイアウォールにより[Windows セキュリティの重要な警告]ダイアログが表示されることがあります。[パス(H):]のところにOpenRTMのインストールパスのeclipse.exeのパス、例えば**C:Program files\openrtm-aist\1.2.x\utils\openrtp\eclipse.exe**が表示されていることを確認して[プライベート ネットワーク(ホームネットワークや社内ネットワークなど)(R)]にチェックを入れ[パブリックネットワーク(空港、喫茶店など)(非推奨)(U)]のチェックをはずして[アクセスを許可する(A)]をクリックしてください。この画面はWindows 10(build 1909以外だと別のダイアログが表示されることがありますし、設定によっては表示されないこともあります。表示された場合は同様の設定をしてダイアログを閉じてください。また、omniorbに対しても同様のダイアログが表示されることがありますので[アクセスを許可する(A)]をクリックしてアクセスを許可してください。

ネームサーバーの起動に成功するとネームサービスビューに[localhost]と表示されます。

<div align="center"><a href="rtm6.png"><img src="rtm6.png" width="50%;"></a></div>
<div align="center"><strong>ネームサーバーの起動を確認</strong></div>

### ネームサーバーが起動しない場合

#### omniORBがインストールされていない。

openrtm.orgが提供するMSIインストーラーにはomniORBが含まれていますが、手動でインストールした場合には、omniORBが入っていない場合も考えられますので、omniORBがインストールされているか確認してください。


#### 環境変数OMNI_ROOTが設定されていない

「Start Naming Service」は%RTM_ROOT%\bin\rtm-naming.batにあるバッチファイルからネームサーバー(omniNames.exe)を起動します。
この際、omniNames.exeを参照するために環境変数OMNI_NAMESを利用しています。
通常インストーラーでOpenRTM-aistをインストールした場合には、OMNI_ROOT環境変数が自動で設定されますが、何らかの理由で環境変数が無効になっていたり、手動でインストールした場合などは、環境変数が設定されていないことがあります。

システム環境変数OMNI_ROOTが設定されていることを確認してください。
システム環境変数は以下の手順で参照編集することができます。
- 画面左下部の[(虫メガネアイコン）ここに入力して検索]に「システム環境変数」と入力し、表示される[システム環境変数の編集]をクリックする。
- [環境変数(N)...]ボタンをクリックする。

### その他

ユーザー名が2バイト文字の場合、ログを出力するフォルダーを適切に設定できずにomniNames.exeの起動に失敗する場合があります。
その場合、環境変数TEMPを2バイト文字を含まない場所に設定することで改善する場合があります。
適当なテンポラリディレクトリ(以下のケースではC:\temp)を作り、そこを環境変数TEMPが指すように設定してネームサーバーを起動します。

```
 set TEMP=C:\temp
 cmd /c rtm-naming.bat
```



また、まれなケースですが、ホスト名やアドレスの設定の問題で、起動がうまくいかないケースがあります。
その場合、利用しているPCのIPアドレスをomniNames.exeに教えてあげるとうまくいくケースがります。
環境変数OMNIORB_USEHOSTNAMEを以下のように設定します(以下は自ホストのIPアドレスが192.168.0.11の場合の例)。

```
 set cosnames="omninames"
 set orb="omniORB"
 set port=%1
 set OMNIORB_USEHOSTNAME=192.168.0.11
 set PATH=%PATH%;%OMNI_ROOT%\bin\x86_win32
```

