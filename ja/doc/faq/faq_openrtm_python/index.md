---
layout: page
title: openrtm-aist (python版) に関する faq
---

<!-- Title: OpenRTM-aist (Python版) に関する FAQ -->
#contents(3)

## Windows

### ネームサーバーのコンソール画面が開かない
- 原因1：omniORBpy がインストールされていない
openrtm.org が提供する msi インストーラーには omniORBpy が含まれていますが、手動でインストールした場合には、omniORBpy が入っていない場合も考えられますので、omniORBpy がインストールされているか確認してください。

<br>

- 原因2：py ファイルの関連付けが違っている
ネームサーバーを起動するファイルは、C:\Program Files (x86)\OpenRTM-aist\1.1\bin\rtm-naming.py です。（32bit 版 msi でインストールした場合）<br>
このディレクトリーでコンソール画面を開き、python rtm-naming.py を実行するとネームサーバーは起動するが、rtm-naming.py をダブルクリックして起動できない場合はインストールしている python を確認してください。<br>
Python の 32bit版、64bit版の両方をインストールしている場合、先にインストールしたものが py ファイルに関連付けられるようなので、OpenRTM-aist-Python のインストーラーと同じアーキテクチャの Python を先にインストールすると解決するかもしれません。

<br>

- 原因3：ホスト名やアドレス設定の問題で起動できない
利用している PC の IPアドレスを omniNames.exe  に設定する必要があります。
環境変数 OMNIORB_USEHOSTNAME を以下のように設定します (以下は自ホストの IPアドレスが192.168.0.11の場合の例)。

```
 変数名(N): OMNIORB_USEHOSTNAME
 変数値(V): 192.168.0.11
```

<br>
<br>

### サンプルコンポーネントが起動しない
rtc.conf の設定に問題があります。rtc.conf の設定を以下のように設定し直して確認してください。
```
 corba.nameservers: localhost
```
例えば、corba.endpoint/corba.endpoints などの設定が現在実行中の PC のホストアドレスとミスマッチを起こしている場合などは、CORBA が異常終了します。
<br>
<br>

&aname(pythonusage);
### rtm-naming.py を実行したら、omniNames で "usage:" と表示される  
**現象：rtm-naming.pyを"C**: \Documents and Settings\Hoge\My Documents"等、空白が入っているディレクトリーから実行した場合、omniNamesは "usage:" を表示して終了してしまいます。

:対応方法：上記現象が発生した場合、下記のどちらかの方法で対処してください。

**対処法その1：**C:\の直下(または、パス名に空白が入っていない場所)に"RTMNaming"等適当なフォルダーを作成し rtm-naming.py を実行してください。

**対処法その2：**C:\Python<version>\Lib\site-packages\OpenRTM\rtm-namingのrtm-naming.pyの48行目を下記のように編集してください。~

```
 rtm-naming.py 48行目
  cmd = "omniNames -start "+str(port)+" -logdir \""+str(currdir)+"\" &"
```
<br>
<br>

&aname(pythonexe);
### python.exeが起動しない  
環境変数 Path に Python インストールフォルダーを追加しておいてください (C:\Python26など)。
<br>
<br>
&aname(python);
### Cygwin をインストールしている環境では python.exe が複数存在する場合がある 
Cygwin をインストールしている環境では、Cygwin上にも python.exe が存在する場合があります。その場合は、通例 Cygwin上の python.exe へのサーチパスが優先されるよう設定されるため、環境変数 Path を適切に設定しているのにもかかわらず、今回導入したはずの Python とは違うバージョンの（すなわちCygwin上の）python.exe が起動してしまう場合があります。この場合、Python のバージョンの違いによる不具合が発生してしまいます。この問題は非常に原因が特定しづらいのが特徴です。このように Cygwin などをインストールしている環境で OpenRTM-aist Python版を使う場合は、該当バージョンの Pythonインストールフォルダーから python.exe が起動していることを確認してください。

**確認方法の例：**「python -V」でバージョンを調べる、(Cygwinのある環境では）which python でどの python.exe が実行されているかを確認する...など

**この障害が発見された場合の対処：**Pythonインストールフォルダー(C:\Python26など)を**システム環境変数 Path**（*ユーザー環境変数 Path ではなく）の**先頭に追加**することで解決できます。
<br>
<br>

&aname(MSVCerror);
### 「MSVCP71.dll が見つからなかったため、…」というエラーで終了する 
WINDOWS\system32フォルダー内に msvcp71.dll がないために発生するエラーです。msvcp71.dll を[こちら ](http://www.vector.co.jp/soft/win95/util/se435079.html)から入手してください。
<br>
<br>

&aname(rtc.conf);
### 「Can't open file: ./rtc.conf」などと表示される
:現象：RTコンポーネントの起動フォルダー（あるいはサーチパス上）に rtc.conf が見つからないため、起動できない状態です。
この場合、次のように表示されます。
```
 Can't open file: ./rtc.conf
 Can't open file: /etc/rtc.conf
 Can't open file: /etc/rtc/rtc.conf
 Can't open file: /usr/local/etc/rtc.conf
 Can't open file: /usr/local/etc/rtc/rtc.conf
```
これは rtc.conf を捜すサーチパスがデフォルトの状態であり、上記の順番で探したが見つからないためこのような表示になります。

:対応方法：
これを避けるためには、たとえば~
```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```
という内容のファイル rtc.conf を作成し、上記サーチパス上（通例はカレント＝コンポーネントと同じフォルダー）に配置します。
<br>
<br>

### コンポーネントがネームサービスに登録されない
:原因：rtc.conf の改行コードが CRLF になっている可能性がある。
以下のコマンドにて rtc.conf の確認を行い、CRLF という文字列が表示された場合、新たに rtc.conf の作成を行ってください。
```
 $ file rtc.conf
```
<br>

