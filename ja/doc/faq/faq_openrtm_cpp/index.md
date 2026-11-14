---
layout: page
title: openrtm-aist (c++版) に関する faq
---

<!-- Title: OpenRTM-aist (C++版) に関する FAQ -->
#contents(3)

## Windows

### CMakeに失敗する

- 原因1:アーキテクチャを合わせていない可能性があります。

アーキテクチャを合わせていない可能性があります。
OpenRTM は 32bit をインストールしているのに、CMake でコンパイラを 64bit に指定しているなど、アーキテクチャを合わせていない可能性があります。
アーキテクチャを合わせてから実行する必要があります。

<br>

- 原因2：CMake のバージョンが古い可能性があります。
OpenRTM で対応している CMake および VisualStudio のバージョンをインストールして実行してください。
<br>
<br>

### ネームサーバーのコンソール画面が開かない
- 原因1：omniORB がインストールされていない

openrtm.org が提供する msi インストーラーには omniORB が含まれていますが、手動でインストールした場合には、omniORB が入っていない場合も考えられますので、omniORB がインストールされているか確認してください。

<br>

- 原因2：環境変数 OMNI_ROOT が設定されていない
「Start Naming Service」は %RTM_ROOT%\bin\rtm-naming.bat にあるバッチファイルからネームサーバー (omniNames.exe) を起動します。 この際、omniNames.exe を参照するために環境変数 OMNI_NAMES を利用しています。 
通常インストーラーで OpenRTM-aist をインストールした場合には、OMNI_ROOT 環境変数が自動で設定されますが、何らかの理由で環境変数が無効になったり、手動でインストールした場合は、環境変数が設定されていないことがあります。

環境変数 OMNI_ROOT が設定されていることを確認してください<br>
環境変数は、
- [コントロールパネル] > [システム] > [詳細設定]タブ > [環境変数]
- [マイコンピューター] を右クリック、[プロパティ] > [詳細設定] タブ > [環境変数] などから参照・編集することができます。

原因3：ユーザー名が2バイト文字の場合、ログを出力するフォルダーを適切に設定できずに omniNames.exe の起動に失敗している
環境変数 TEMP を2バイト文字を含まない場所に設定することで改善する場合があります。
適当なテンポラリフォルダー (以下のケースでは C:\temp) を作成し、そこを環境変数 TEMP が指すように、rtm-naming.bat の先頭部分で以下のように設定します。

```
 set cosnames="omninames"
 set orb="omniORB"
 set port=%1
 rem set OMNIORB_USEHOSTNAME=localhost
 set PATH=%PATH%;%OMNI_ROOT%\bin\x86_win32
 set TEMP=C:\temp
```

また、稀なケースですが、ホスト名やアドレスの設定の問題で、起動できないことがあります。
その場合、利用している PC の IPアドレス を omniNames.exe に設定する必要があります。
環境変数 OMNIORB_USEHOSTNAME を以下のように設定します (以下は自ホストの IPアドレスが 192.168.0.11 の場合の例)。

```
 set cosnames="omninames"
 set orb="omniORB"
 set port=%1
 set OMNIORB_USEHOSTNAME=192.168.0.11
 set PATH=%PATH%;%OMNI_ROOT%\bin\x86_win32
```
<br>
<br>

### サンプルコンポーネントが起動しない
rtc.conf の設定に問題があります。rtc.conf の設定を以下のように設定し直して確認してください。
```
 corba.nameservers: localhost
```
例えば、corba.endpoint/corba.endpoints などの設定が現在実行中の PC のホストアドレスとミスマッチを起こしている場合は、CORBA が異常終了します。
<br>
<br>

### サンプルコンポーネントを起動させると、ランタイムエラーで終了する
ライブラリー等が適切にインストールされていない、設定されていない等の原因でラインタイムエラーが表示される場合があります。
PCを再起動する または OpenRTM-aist をすべてアンインストールし、再インストールすることで改善される場合があります。
<br>
<br>

&aname(cmakecompilererrro);
### CMake 実行時にコンパイラが見つからない

CMake 実行時に以下のエラーが発生する。

```
 No CMAKE_CXX_COMPILER could be found. 
```

まずは、&lt;プロジェクトディレクトリー&gt;/&lt;buildディレクトリー&gt;/CMakeFiles/CMakeError.log を確認してください。

:原因1：間違ったコンパイラを指定した

CMake を実行 (Configure) する際に、コンパイラをしてします。インストールされている Visual Studio とは異なるコンパイラを指定した場合には、コンパイラが見つからず、**No CMAKE_CXX_COMPILER could be found.** のようなエラーが発生します。

CMakeError.log を見ると、以下のように、コンパイラチェック開始直後にエラーが発生します。

```
 Microsoft (R) Build Engine バージョン 4.6.1586.0
 [Microsoft .NET Framework、バージョン 4.0.30319.42000]
 Copyright (C) Microsoft Corporation. All rights reserved.
 
 2017/04/08 10:47:04 にビルドを開始しました。
 ノード 1 上のプロジェクト
 "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj"
 (既定のターゲット)。
 C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj(18,3): 
 error MSB4019: 
 インポートされたプロジェクト 
 "C:\Microsoft.Cpp.Default.props" が見つかりませんでした。<Import> 
 宣言のパスが正しいかどうか、およびファイルがディスクに存在しているかどうかを
 確認してください。
 プロジェクト
 "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj"
 (既定のターゲット) のビルドが終了しました -- 失敗。
 
 ビルドに失敗しました。
 
 "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj"
 (既定のターゲット) (1) ->
  C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj(18,3):
 error MSB4019: インポートされたプロジェクト 
 "C:\Microsoft.Cpp.Default.props" が見つかりませんでした。
 <Import> 宣言のパスが正しいかどうか、およびファイルがディスクに存在しているかどうかを
 確認してください。
  
     0 個の警告
     1 エラー
 
 経過時間 00:00:00.50
```

- 対応方法：正しいコンパイラを指定します。

1. インストールされている OpenRTM を確認
  - → 32bitか、64bitか？ 
1. インストールされている Visual Studio を確認
  - → Visual Studio 2008 (VC9), 2010 (VC10), 2012 (VC11), 2013 (VC12), 2015 (VC14), 2017 (VC15)
1. CMake のキャッシュを削除
  - コンパイラの指定を変更する際には必ずキャッシュを削除する必要があります。
1. CMake Configure で正しいコンパイラを指定
  - 32bit/64bit はインストールされている OpenRTM に合わせる
    - 32bit は無印 (例: Visual Studio 10 2010)
    - 64bit はWin64 (例： Visual Studio 10 2010 Win64)

<br>

- 原因2：Visual C++ がインストールされていない
Visual Studio インストール時に、C++コンパイラを含む Visual C++ がインストールされていない場合があります。

- 対応方法：Visual C++ をインストールします
再度インストーラーを（手元になければダウンロードしてから）起動し、[変更] からインストールを行います。
インストールをカスタマイズするを選択して、インストール対象に Visual C++ が含まれていることを確認してからインストールを行います。

この原因の場合も、CMakeError.log の出力内容は（原因1）と同じです。


- 原因3：rc.exe が実行できない
まれに、インストールされているコンパイラを CMake 実行時に正しく指定しているのにもかかわらず、**No CMAKE_CXX_COMPILER could be found.** のようなエラーが発生することがあります。
原因の一つとして、複数のバージョンの Visual Studio をインストール・アンインストール等を行った際に、まれにツールチェーンの設定に不整合が生じ、以下のようなエラー **rc.exeが実行できない** が発生することがあります。

```
 C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\CL.exe
 /c /nologo /W0 /WX- /Od /D _MBCS /Gm- /EHsc /RTC1
 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc140.pdb"
 /Gd /TC /errorReport:queue CMakeCCompilerId.c
   CMakeCCompilerId.c
 Link:
 C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe
 /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO
 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib
 shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST
 /MANIFESTUAC:"level='asInvoker' uiAccess='false'"
 /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE /TLBID:1
 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib"
 /MACHINE:X64 Debug\CMakeCCompilerId.obj
 LINK : fatal error LNK1158: 'rc.exe' を実行できません。
 [C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj]
 プロジェクト "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj"
 (既定のターゲット) のビルドが終了しました -- 失敗。
 
 ビルドに失敗しました。
```


- 対応方法：rc.exe と rcdll.dll をコピーする
これに対する対処方法としては、rc.exe と rcdll.dll を対象コンパイラのツールディレクトリーにコピーする方法があります。

1. rc.exe, rcdll.dll を探す
  - エクスプローラーを開き **C:\Program Files** (または **C:\Program Files (x86)**) を開き rc.exe を検索する。rcdll.dll は同じディレクトリーにあるはずなので探すのは rc.exe のみでよい。
  - 通常は **C:\Program Files (x86)\Windows Kits** の下にいくつかの rc.exe が見つかるが x86 というディレクトリー下にあるものが対象。
  - 検索結果にて対象の rc.exe を右クリックし**「ファイルの場所を開く」**を選択
1. コンパイラのツールディレクトリーを開く
  - 別のエクスプローラーを開き、ツールの bin ディレクトリーを開く
  - 上のログの例では、**C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe** から、ツールのディレクトリーが **C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin** (binディレクトリーが対象、x86?amd64は無視してよい)  であることがわかる。
1. rc.exe, rcdll.dll をコピーする
  - 1.で開いたエクスプローラーから rc.exe、rcdll.dll を2.で開いたツールディレクトリーにコピーする
<br>
<br>

<br>

### OpenRTP 実行時に xxx.dll が存在しないというエラーが表示される
- 原因1：
  - Windows10 のみの現象の可能性があります。
  - RTM_VC_VERSION が正しく環境変数に設定されていない可能性があります。

- 対処方法：
OpenRTM インストール後に PCを再起動して、環境変数に RTM_VC_VERSION が正しく設定されているかを確認してください。
<br>
<br>

&aname(errorapplication);
### 「このアプリケーションの構成が正しくないため、アプリケーションを開始できませんでした。…」 が表示される
サンプルの RTコンポーネントなどを起動しようとして、xxxComp.exe を実行すると、上記のようなエラーが出る場合があります。
このエラーは起動環境上に VC++ライブラリーのランタイムコンポーネントがないために起こります。
VC++関連の開発環境（Microsoft Visual Studio,Visual C++ Expressなど）をインストールしていない環境では OpenRTM-aist (C++版) を動作させることはできませんので、必ず VC++関連の開発環境をインストールしてください。~
<br>
<br>

&aname(errorinit);
### アプリケーションエラー「アプリケーションを正しく初期化できませんでした。…」が表示される
ネームサーバー起動しようとして、rtm-naming.bat を実行すると、上記のようなエラーが出る場合があります。
このエラーは、起動環境上に VC++ライブラリーのランタイムコンポーネントがないために起こります。
VC++関連の開発環境（Microsoft Visual Studio 、Visual C++  Expressなど）をインストールしていない環境では OpenRTM-aist (C++版) を動作させることはできませんので、必ず VC++関連の開発環境をインストールしてください。
<br>
<br>

#### VC++関係のライブラリーがインストールされていない
Visual Studio 等のアプリケーションのインストールを行ってください。
<br>
<br>

### rtm-naming.bat を実行するとアプリケーションエラーが発生する
VC++関係のライブラリーがインストールされていない可能性が考えるので、インストールを行ってください。
<br>
<br>

### rtm-naming が実行できない
rtm-naming.bat を実行しても黒い窓（コマンドプロンプト画面）が一瞬開いて閉じてしまう。

- 原因1：omniORB がインストールされていない
  - 対処方法：ダウンロードページから omniORB をダウンロードしインストールしてください。<br>
rtm-naming.bat 内では通常 omniORB のネームサーバー**omniNames.exe**を実行します。~
omniORB がインストールされていないと**omniNames.exe**もインストールされないので、ネームサーバーを実行できません。~
<br>
- 原因2：log ディレクトリーのパス中に2バイト文字が含まれている
  - 対処方法：r tm-naming.bat 内では通常 omniORB のネームサーバー**omniNames.exe**を以下のように実行します。~
```
 omniNames.exe -start 2809 -logdir %TEMP%
```

通常環境変数 %TEMP% はユーザーのテンポラリディレクトリー
```
 C:\Documents and Settings\ユーザー名\Local Settings\Temp
```

を指します。ここで、**ユーザー名**が日本語の場合、omniNames がログファイルを正しく作成できないため、実行できずに終了します。~
対応策としては、以下の3つが考えられます。
- 日本語のユーザー名を使用しない
  - 日本語を使用しないユーザーを新たに作り、その環境で実行する。
- rtm-naming.bat を書き換える
  - **C**: \Program Files\OpenRTM-aist\[バージョン番号]\bin**の下にある rtm-naming.bat の中の以下の部分 ~

```
 %cosnames% -start %port% -logdir %TEMP%\ 
```
を~
```
 %cosnames% -start %port% -logdir [パスに日本語を含まないログディレクトリー]
```
のように書き換えます。~
**パスに日本語を含まないログディレクトリー**は自分に書き込みの権限があるディレクトリーで、安全な場所にしてください。たとえば、C:\tmp など。

- Java版の orbd を使用する
  - OpenRTM-aist の Java版と JDK をインストールすると、スタートメニューの Java版 の examples の中に **start-orbd.vbs** が現れます。これは、JDK に付属する CORBA ネームサーバーを起動するスクリプトです。~
このネームサーバーには、omniNames のような日本語のパスの問題は存在しないので、これを使用することでユーザー名が日本語でも、ネームサーバーを起動できます。
<br>

## UNIX
### configure を実行したがエラーが出て終了する
configure のエラーの大半は、必要なパッケージが見つからないときに出ます。エラーが出た場合には、必要なパッケージがインストールされているか、autoconf が見つけられるディレクトリーにヘッダ、ライブラリーがインストールされているかを確認してください。
<br>
<br>

### make を実行してもビルドが完了しない。または make の実行エラーが表示される 
パッケージのインストールまたは OpenRTM-aist (C++版)のビルドが不完全な可能性があります。もう一度パッケージの自動インストーラーを起動して、パッケージのインストールからやり直してください。
パッケージのインストール中の処理画面に何らかのエラーメッセージが表示された場合、該当するパッケージだけを手動でインストールするなどしてから configure を実行してください。
configure を実行してエラーメッセージが表示されないことを確認してから、再度 make を実行してビルドを完了させてください。
<br>
<br>

### サンプルプログラムの SimpleIO を実行する run.sh が実行できない
run.sh に実行ビットが立っていない可能性があります。下記のように実行ビットを立てて実行するか、直接シェルに渡して実行してください。~
```
 > ls -al run.sh
 -rw-r--r--  1 n-ando  n-ando  1146  4 27 15:12 run.sh
 > chmod 755 run.sh
 > ./run.sh
```
 もしくは
```
 > sh run.sh
```
<br>
<br>

### サンプルプログラムの SimpleIO を起動したが、正常に動作しない
SimpleIO の実行スクリプト run.sh では、ターミナルウィンドウを kterm，xterm，gnome-terminal のいずれかに仮定しております。
このため、これ以外のターミナルウィンドウを使用している場合は、run.sh を適宜書き換えてから実行してください。~
<br>

