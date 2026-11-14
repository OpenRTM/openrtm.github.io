---
layout: page
title: openrtm-aist(c++版、python版、java版)に関するトラブルシューティング
---
<br>
<a>No English version available.
</a>

<!-- Title: OpenRTM-aist(C++版、Python版、Java版)に関するトラブルシューティング -->
#contents(4)
OpenRTM-aist (C++版、Python版、Java版)に関するトラブルシューティングをまとめました。

<!-- #clear -->

## OpenRTM-aist (共通)
### OS 共通
#### コンポーネントは起動しているはずなのにゾンビオブジェクトとして表示される。
コンポーネントは起動しており、ネームサーバーにも登録されているのに、RTSystemEditor のネームサービスビュー上ではゾンビオブジェクトとして表示されており、システムエディタにドラッグアンドドロップしても何も表示されない。
##### [原因]コンポーネントを起動したホストに到達できない
RTSystemEditor が動作しているPCからコンポーネントを起動したホストに何らかの理由で到達できていない可能性があります。~
まず、RTSystemEditor が動作しているPCからコンポーネントを起動したホストに対して ping が通るか確認してください。~
例えば、以下の3台のホストA、B、Cがあるとします。
  - hostA: コンポーネントが動いているホスト
  - hostB: ネームサーバーが動いているホスト
  - hostC: RTSystemEditor が動いているホスト

これらのホストのネットワークが以下のような構成になっており、~
**[hostA]-(ネットワークI)-[hostB]-(ネットワークI)-[hostC]**~
かつhostBが**ネットワークI**と**ネットワークII**間を適切にルーティングするように設定されていなければ、hostC から hostAへは到達できません。~
こういった場合は、hostB を適切に設定してhostC から hostAへ到達できるようにする必要があります。
##### [原因]コンポーネントを起動したホストでファイアウォールが有効になっている 
コンポーネントが動作しているホストでファイアウォールが動作している場合、RTSystemEditor とコンポーネントが通信できずにこうした現象が発生する場合があります。~
ファイアウォールの設定を見直すかOFFにするなどして、外部からコンポーネントに通信できるようにしてください。
<br>
### Windows

&aname(tokkenn);
#### インストーラー実行中に「…特権が不足しています。」などと表示されて、インストールが続行できない
: |Administrator特権を持つユーザーとしてログオンし、インストール作業を行ってください。
<br>
#### コンポーネントがネームサービスに登録されない。
ネームサーバー、コンポーネントを起動後、RTSystemEditor などでネームサーバーに接続し、コンポーネントが登録されていない場合があります。~
このような場合は、~
まずは、ログレベルを最高にするため rtc.conf に~
```
 logger.log_level:PARANOID
```
を設定し、コンポーネントを起動してみてください。~
コンポーネントのログに~
```
 naming_svc NameServer connection succeeded: corba/ホスト名:ポート番号
```
というメッセージが無ければ、ネームサーバーへの登録に失敗しています。~
このような場合、以下の原因が考えられます。
##### rtc.conf の corba.nameservers が正しく設定されていない
コンポーネントが読み込む rtc.conf が正しく設定されているかどうか確認してください。利用しようとするネームサーバーを openrtm.aist.go.jp というホスト名と仮定すると、以下の行が rtc.conf に含まれていなければなりません。
```
 corba.nameservers: openrtm.aist.go.jp
```

また、ネームサーバーをポート番号を指定して起動した場合には、ポート番号も指定する必要があります。ネームサーバー起動時に指定したポート番号が1234番の場合、以下のように設定する必要があります。~
```
 corba.nameservers: openrtm.aist.go.jp:1234
```

ポート番号が指定されない場合、デフォルトポート番号2809が使用されます。これは omniORB のネームサーバー(omniNames)のデフォルトポート番号です。もし、omniORB 以外のネームサーバーを使用する場合は注意してください。
##### コンポーネント起動したホストからネームサーバーを起動したホストへネットワーク接続ができない
コンポーネントを起動したホストからネームサーバーを起動したホストへネットワーク接続ができるか確認してください。~
まずは、ping が通るかどうか確認します。もし通らなければネットワークの設定を見直してください。~
ping が通っても、ファイアウォールなどで接続が禁止されている可能性があります。まず、ネームサーバーを起動したホスト側のファイアウォールの設定を見直してください。一番簡単な方法は、ファイアウォールをOFFにすることです。方法は各OSやファイアウォールの設定方法を参照してください。
##### ネットワークインターフェースが2つ以上ある
ホストにネットワークインターフェースが2つ以上ある場合、CORBA にどちらのインターフェースを使用するか教えてやる必要があります。~
これは、ネームサーバー側、コンポーネント側両者ともに考慮しなければなりません。~
仮にそれぞれのホストが2つずつインターフェースを持っているとして、各インターフェースのアドレスが以下のように設定されているとします(maskは255.255.255.0と仮定)。~
**ネームサーバーhost: eth0:192.168.0.1, eth1:192.168.100.1**~
**コンポーネントhost: eth0:192.168.0.2, eth1:192.168.11.96**~
この場合、ネームサーバーhostとコンポーネントhostは 192.168.0 のネットワークで接続されているはずです。~
従って、~
**ネームサーバーには eth0:192.168.0.1**~
**コンポーネントには eth0:192.168.0.2**~
のインターフェースを使うように教えてあげる必要があります。~
ネームサーバー側では、ネームサーバーを起動する際に OMNIORB_USEHOSTNAME という環境変数を設定する必要があります。~
```
 (csh系)
 > setenv OMNIORB_USEHOSTNAME 192.168.0.1
```
```
 (bash系)
 > export OMNIORB_USEHOSTNAME=192.168.0.1
 > rtm-naming もしくは omniNames でネームサーバーを起動
```

直接、rtm-naming (UNIX系) もしくは rtm-naming.bat (Windows) に書き込んでも良いでしょう。~
一方、コンポーネント側は rtc.confにcorba.endpoint の設定を記述することで、使用するインターフェースを指定することができます。~

```
 corba.endpoint: インターフェースIPアドレス:ポート番号
 corba:endpoint: 192.168.0.2:       (ポート番号を指定しない場合)
 corba:endpoint: 192.168.0.2:1234   (ポート番号を指定する場合)
```

ポート番号は特に指定しなくても構いませんが、IPアドレスの後の**:(コロン)**を忘れずに付けてください。
<br>

## OpenRTM-aist (C++版)
### Windows

&aname(cmakecompilererrro)
#### CMake 実行時にコンパイラが見つからない

CMake 実行時に以下のエラーが発生する。

```
 No CMAKE_CXX_COMPILER could be found. 
```

まずは、<プロジェクトディレクトリ>/<buildディレクトリ>/CMakeFiles/CMakeError.log

を確認してください。

##### (原因1) 間違ったコンパイラを指定した

CMake を実行 (Configure) する際に、コンパイラをしてします。インストールされている Visual Studio とは異なるコンパイラを指定した場合には、コンパイラが見つからず、**No CMAKE_CXX_COMPILER could be found.** のようなエラーが発生します。

CMakeError.log を見ると、以下のように、コンパイラチェック開始直後にエラーが発生します。

```
 Microsoft (R) Build Engine バージョン 4.6.1586.0
 [Microsoft .NET Framework、バージョン 4.0.30319.42000]
 Copyright (C) Microsoft Corporation. All rights reserved.
 
 2017/04/08 10:47:04 にビルドを開始しました。
 ノード 1 上のプロジェクト "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj" (既定のターゲット)。
 C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj(18,3): error MSB4019: インポートされたプロジェクト 
 "C:\Microsoft.Cpp.Default.props" が見つかりませんでした。<Import> 宣言のパスが正しいかどうか、およびファイルがディスクに存在しているかどうかを確認してください。
 プロジェクト "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj" (既定のターゲット) のビルドが終了しました -- 失敗。
 
 ビルドに失敗しました。
 
 "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj" (既定のターゲット) (1) ->
  C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj(18,3): error MSB4019: インポートされたプロジェクト 
 "C:\Microsoft.Cpp.Default.props" が見つかりませんでした。<Import> 宣言のパスが正しいかどうか、およびファイルがディスクに存在しているかどうかを確認してください。
  
     0 個の警告
     1 エラー
 
 経過時間 00:00:00.50
```

- 対応方法
  - 正しいコンパイラを指定します。

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


##### (原因2) Visual C++がインストールされていない
Visual Studio インストール時に、C++コンパイラを含む Visual C++ がインストールされていない場合があります。

- 対応方法
  - Visual C++ をインストールします
再度インストーラーを（手元にすでになければダウンロードしてから）起動し、「変更」からインストールを行います。
インストールをカスタマイズするを選択して、インストール対象に Visual C++ が含まれていることを確認してからインストールを行います。

この原因の場合も、CMakeError.log の出力内容は（原因1）と同じです。


##### (原因3) rc.exe が実行できない

まれに、インストールされているコンパイラを CMake 実行時に正しく指定しているのにもかかわらず、**No CMAKE_CXX_COMPILER could be found.** のようなエラーが発生することがあります。
原因の一つとして、複数のバージョンの Visual Studio をインストール・アンインストール等を行った際に、まれにツールチェーンの設定に不整合が生じ、以下のようなエラー **rc.exeが実行できない** が発生することがあります。

```
   C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\CL.exe /c /nologo /W0 /WX- /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc140.pdb" /Gd /TC /errorReport:queue CMakeCCompilerId.c
   CMakeCCompilerId.c
 Link:
   C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib" /MACHINE:X64 Debug\CMakeCCompilerId.obj
 LINK : fatal error LNK1158: 'rc.exe' を実行できません。 [C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj]
 プロジェクト "C:\workspace\Flip\build\CMakeFiles\3.7.2\CompilerIdC\CompilerIdC.vcxproj" (既定のターゲット) のビルドが終了しました -- 失敗。
 
 ビルドに失敗しました。
```


- 対応方法
  - rc.exe と rcdll.dll をコピーする

これに対する対処方法としては、rc.exe と rcdll.dll を対象コンパイラのツールディレクトリにコピーする方法があります。

1. rc.exe, rcdll.dll を探す
  - エクスプローラーを開き **C:\Program Files** (又は **C:\Program Files (x86)**) を開き rc.exe を検索する。rcdll.dll は同じディレクトリにあるはずなので探すのは rc.exe のみでよい。
  - 通常は **C:\Program Files (x86)\Windows Kits** の下にいくつかの rc.exe が見つかるが x86 というディレクトリ下にあるものが対象。
  - 検索結果にて対象の rc.exe を右クリックし**「ファイルの場所を開く(I)」**を選択
1. コンパイラのツールディレクトリを開く
  - 別のエクスプローラを開き、ツールの binディレクトリを開く
  - 上のログの例では、**C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe** から、ツールのディレクトリが **C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin** (binディレクトリが対象、x86?amd64は無視してよい)  であることがわかる。
1. rc.exe, rcdll.dll をコピーする
  - 1.で開いたエクスプローラから rc.exe、rcdll.dll を2.で開いたツールディレクトリにコピーする


&aname(errorinit);
#### アプリケーションエラー「アプリケーションを正しく初期化できませんでした。…」
: |ネームサーバー起動しようとして、rtm-naming.bat を実行すると、上記のようなエラーが出る場合があります。このエラーは起動環境上に VC++ライブラリのランタイムコンポーネントがないために起こります。VC++関連の開発環境（Microsoft Visual Studio 、Visual C++  Expressなど）をインストールしていない環境では OpenRTM-aist (C++版) を動作させることはできませんので、必ず VC++関連の開発環境をインストールしてください。~
OpenRTM-aist (C++版)には、VC8（VS2005）ベースのものと、VC9（VS2008）ベースのものがあります。OpenRTM-aist-X.X.X-jp_vc8.msi（X.X.Xはバージョンです。)などのVC8ベースのインストーラーを使用した場合は[Microsoft Visual C++ 2005 SP1 再頒布可能パッケージ (x86) ](http://www.microsoft.com/downloads/details.aspx?FamilyID=200b2fd9-ae1a-4a14-984d-389c36f85647&DisplayLang=ja)を、OpenRTM-aist-X.X.X-jp_vc9.msi（X.X.Xはバージョンです。)などのVC9ベースのインストーラーを使用した場合は[Microsoft Visual C++ 2008 再頒布可能パッケージ (x86) ](http://www.microsoft.com/downloads/details.aspx?displaylang=ja&FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf)をインストールしてください。
<br>
&aname(errorapplication);
#### 「このアプリケーションの構成が正しくないため、アプリケーションを開始できませんでした。…」 

サンプルの RTコンポーネントなどを起動しようとして、xxxComp.exe を実行すると、上記のようなエラーが出る場合があります。このエラーは起動環境上に VC++ライブラリのランタイムコンポーネントがないために起こります。VC++関連の開発環境（Microsoft Visual Studio,Visual C++ Expressなど）をインストールしていない環境では OpenRTM-aist (C++版) を動作させることはできませんので、必ず VC++関連の開発環境をインストールしてください。~
OpenRTM-aist (C++版)には、VC8（VS2005）ベースのものと、VC9（VS2008）ベースのものがあります。OpenRTM-aist-X.X.X-jp_vc8.msi（X.X.Xはバージョンです。)などのVC8ベースのインストーラーを使用した場合は[Microsoft Visual C++ 2005 SP1 再頒布可能パッケージ (x86) ](http://www.microsoft.com/downloads/details.aspx?FamilyID=200b2fd9-ae1a-4a14-984d-389c36f85647&DisplayLang=ja)を、OpenRTM-aist-X.X.X-jp_vc9.msi（X.X.Xはバージョンです。)などのVC9ベースのインストーラーを使用した場合は[Microsoft Visual C++ 2008 再頒布可能パッケージ (x86) ](http://www.microsoft.com/downloads/details.aspx?displaylang=ja&FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf)をインストールしてください。
<br>
#### Visual C++ 2005 Express Edition でビルド時に「'windows.h'が見つからない」というエラー
Visual C++ 2005 Express Edition でビルド時に次のようなエラーが出る場合があります。~
```
 >c:\program files\omniorb\include\omnithread\nt.h(35) : fatal error C1083: include ファイルを開けません。'windows.h': No such file or directory
```

これは**１．Microsoft Platform SDK がインストールがされていない、**あるいは**２．インクルードファイルパス・ライブラリパスの設定不備**が原因と考えられます。

##### １．Microsoft Platform SDK がインストールがされていない
- **対応方法**

Microsoft Platform SDK をインストールする。その際は、[こちら]()(No corresponding page available.)を参考にしてください。あるいは、次の**２．**にしたがってください。

##### ２．インクルードファイルパス・ライブラリパスの設定不備
- **対応方法**
インストールをする順序などの関係で、Visual C++ 2005 Express Edition のインストールディレクトリとは違う場所に Microsoft Platform SDK がインストールされてしまうなどの事情で、Visual C++ 2005 Express Edition のコンパイラが Microsoft Platform SDK のインクルードファイルやライブラリをたぐれなくなっている場合があります。この場合は、インクルードファイルサーチパスやライブラリサーチパスに Microsoft Platform SDK のインストールディレクトリを追加することで問題を解決できます。

- **インクルードファイルサーチパスの追加方法**
Visual C++ 2005 Express Edition のメニューバー→「ツール」→「オプション」を選択し、「オプション」ウィンドウを開きます。左のツリービューから「プロジェクトおよびソリューション」→「VC++ディレクトリ」を選択します。~
右上のプルダウンメニュー「ディレクトリを表示するプロジェクト」を「インクルード　ファイル」として、Microsoft Platform SDK のインクルードファイルのディレクトリ（例えば、「C:\Program Files\Microsoft Platform SDK\Include」）をインクルードファイルのサーチパスに追加します。

- **ライブラリファイルサーチパスの追加方法**
同様にして、「オプション」の左のツリービュー「VC++ディレクトリ」を選択した状態で、右上のプルダウンメニュー「ディレクトリを表示するプロジェクト」を「ライブラリ　ファイル」として、Microsoft Platform SDK のライブラリファイルのディレクトリ（例えば、`C: \Program Files\Microsoft Platform SDK\Lib`）をライブラリファイルのサーチパスに追加します。
なお、サーチパスの具体的な追加方法などは Visual C++ 2005 Express Edition のヘルプ等を参照してください。
<br>
#### rtm-naming の実行でエラー発生 

- 症状
rtm-naming.bat を実行するとアプリケーションエラーが発生する。~
VC++関係のライブラリがインストールされていない可能性が考えられます。

##### VC++関係のライブラリがインストールされていない

Visual Studio 2005 等のアプリケーションがインストールされていない場合は、ここ[Visual Studio 2005 Express Edition](http://www.microsoft.com/japan/msdn/vstudio/express/)から"Visual C++ 2005 Express Edition"のインストールを行ってください。
<br>

#### rtm-naming が実行できない
- 症状
rtm-naming.bat を実行しても黒い窓（コマンドプロンプト画面）が一瞬開いて閉じてしまう。

##### [原因]omniORB がインストールされていない

rtm-naming.bat 内では通常 omniORB のネームサーバー**omniNames.exe**を実行します。~
omniORB がインストールされていないと**omniNames.exe**もインストールされないので、ネームサーバーを実行できません。~
ダウンロードページから omniORB をダウンロードしインストールしてください。

##### [原因]log ディレクトリのパス中に2バイト文字が含まれている
rtm-naming.bat 内では通常 omniORB のネームサーバー**omniNames.exe**を以下のように実行します。~

```
 omniNames.exe -start 2809 -logdir %TEMP%
```

通常環境変数 %TEMP% はユーザーのテンポラリディレクトリ~
```
 C:\Documents and Settings\ユーザ名\Local Settings\Temp
```

を指します。ここで、**ユーザー名**が日本語の場合、omniNames がログファイルを正しく作成できないため、実行できずに終了します。~
対応策としては、以下の3つが考えられます。
:日本語のユーザー名を使用しない|日本語を使用しないユーザーを新たに作り、その環境で実行する。
**rtm-naming.bat を書き換える**
`C: \Program Files\OpenRTM-aist\[バージョン番号]\bin`の下にある rtm-naming.bat の中の以下の部分 ~
```
 %cosnames% -start %port% -logdir %TEMP%\ 
```

を~

```
 %cosnames% -start %port% -logdir [パスに日本語を含まないログディレクトリ]
```

のように書き換えます。~
**パスに日本語を含まないログディレクトリ**は自分に書き込みの権限があるディレクトリで、安全な場所にしてください。たとえば、C:\tmp など。

- Java版の orbd を使用する
OpenRTM-aist の Java版と JDK をインストールすると、スタートメニューの Java版 の examples の中に**start-orbd.vbs**が現れます。これは、JDK に付属する CORBA ネームサーバーを起動するスクリプトです。~
このネームサーバーには、omniNames のような日本語のパスの問題は存在しないので、これを使用することでユーザー名が日本語でも、ネームサーバーを起動できます。
<br>
### Unix
#### パッケージの自動インストールでダウンロードエラーが出る。 
OpenRTM-aist に付属する自動インストーラーは、パッケージの有無とバージョンを確認し、適当なパッケージがインストールされていない場合に各パッケージのダウンロードサイトからダウンロード及び加工するものです。このため、自動インストーラーでインストールする場合には、コンピューターを必ずインターネットに接続してください。~
ネットワーク接続が正常でもダウンロードエラーが出る場合、回線の混雑等でウンロードに失敗した場合と、ダウンロードサイト側でファイルの場所や名前が変わった可能性が考えられます。前者の場合は時間帯等をずらして再度自動インストーラーを実行してみてください。また後者の場合には、該当するパッケージを探してから個々にダウンロードして手動インストールするか、自動インストーラーのダウンロード元アドレスを修正してから改めて起動してください。~
なお、ダウンロードサイト側の変更があった場合、変更情報を当方までご連絡いただければ幸いですので、ご協力をお願いします。
<br>
#### configure を実行したがエラーが出て終了する。
configure のエラーの大半は、必要なパッケージが見つからないときに出ます。エラーが出た場合には、必要なパッケージがインストールされているか、autoconf が見つけられるディレクトリにヘッダ，ライブラリがインストールされているかを確認してください。
<br>
#### make を実行してもビルドが完了しない。または make の実行エラーが出る。 
パッケージのインストールまたは OpenRTM-aist (C++版)のビルドが不完全な可能性があります。もう一度パッケージの自動インストーラーを起動して、パッケージのインストールからやり直してください。パッケージのインストール中の処理画面に何らかのエラーメッセージが出てきた場合、該当するパッケージだけを手動でインストールするなどしてから configure を実行してください。configure を実行してエラーメッセージが出ないことを確認してから、再度 make を実行してビルドを完了させてください。
<br>
&aname(openrtminstfault);
#### OpenRTM-aist のインストールに失敗する 
古いバージョンの OpenRTM-aist が完全にアンインストールされていない場合、新しいバージョンのインストールができません。古いバージョンを一度アンインストールしてから、再度インストール作業をします。
##### Vine・Fedora・ubuntu・debian共通：
pkg_install_XXXX.sh を利用してアンインストールする。~
```
 >su
 #pkg_install_XXXX.sh -u
```

アンインストールの許可を求められるので、**y** を入力しながら完了させます。
あるいは次の手順に従います。
##### Vine：
apt-getコマンドでアンインストールする。次の手順でアンインストールを行ってください。~
```
 >su
 #apt-get remove OpenRTM-aist-example
 #apt-get remove OpenRTM-aist-dev
 #apt-get remove OpenRTM-aist-doc
 #apt-get remove OpenRTM-aist
```
##### Fedora：
yumコマンドでアンインストールする。次の手順でアンインストールを行ってください。~
```
 >su
 #yum remove OpenRTM-aist-example
 #yum remove OpenRTM-aist-dev
 #yum remove OpenRTM-aist-doc
 #yum remove OpenRTM-aist
```
##### ubuntu/debian：
apt-getコマンドでアンインストールする。次の手順でアンインストールを行ってください。~
```
 >su
 #apt-get remove OpenRTM-aist-example
 #apt-get remove OpenRTM-aist-dev
 #apt-get remove OpenRTM-aist-doc
 #apt-get remove OpenRTM-aist
```
<br>
&aname(notusecd);
#### apt-get などを使用してインストール作業を行うときに CD を要求される 
Ubuntu、Debian などのディストリビューションで、apt-get や pkg_install_ubuntu.sh, pkg_install_debian.sh を使用してインストール作業をしていると、次のように CD を求められることがあります。
メディア変更:~
```
 　　'Ubuntu 7.10 _Gutsy Gibbon_ Japanese Remix - Release i386 (20071018)'
```

とラベルの付いたディスクをドライブ '/cdrom/' に入れて Enter を押してください。~
もちろん、CD を用意すればよいことなのですが、諸事情により用意できない場合の対処方法を記述します。~
この場合はとりあえず、**C-c**(Ctrl+c) を入力してインストール作業を中断し、以下の手順でインストール作業をやり直してください。
##### 1.**/etc/apt/sources.list** の編集をする
**/etc/apt/sources.list** の冒頭部分に~
```
 deb cdrom:[Ubuntu 7.10 _Gutsy Gibbon_ Japanese Remix - Release i386 (20071018)]/ gutsy main restricted
```

あるいは~
```
 deb cdrom:[Debian GNU/Linux 4.0 r3 _Etch_ - Official i386 NETINST Binary-1 20080218-14:15]/ etch contrib main
```

というような行がありますので、該当する行頭に **#** 文字を挿入し、コメントアウトしてください。~
```
 #deb cdrom:[Ubuntu 7.10 _Gutsy Gibbon_ Japanese Remix - Release i386 (20071018)]/ gutsy main restricted
```

又は、~
```
 #deb cdrom:[Debian GNU/Linux 4.0 r3 _Etch_ - Official i386 NETINST Binary-1 20080218-14:15]/ etch contrib main
```

##### 2.インストール作業をやり直す
先ほど中断したインストール作業を始めからやり直してください。
<br>
#### サンプルプログラムの SimpleIO を実行する run.sh が実行できない
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
#### サンプルプログラム SimpleIO を起動したが、正常に動かない。 
SimpleIO の実行スクリプト run.sh では、ターミナルウィンドウを kterm，xterm，gnome-terminal のいずれかに仮定しております。このため、これ以外のターミナルウィンドウを使用している場合は、run.sh を適宜書き換えてから実行してください。~
<br>


## OpenRTM-aist (Python版)
### Windows
&aname(pythonusage);
#### rtm-naming.py を実行したら、omniNames が"usage:"を表示して終了してしまう  
##### 症状
rtm-naming.pyを"C:\Documents and Settings\Hoge\My Documents"等ディレクトリ名に空白が入っているディレクトリから実行した場合、omniNamesは"usage:"を表示して終了してしまいます。
##### 対処方法
これは、rtm-naming.py のバグによるものです。上記の症状がでた場合、下記のどちらかの方法で対処してください。
- **対処法その1**
`C:\`の直下(または、パス名に空白が入っていない場所)に"RTMNaming"等適当なフォルダーを作成し rtm-naming.py を実行してください。
- **対処法その2**
`C: \Python<version>\Lib\site-packages\OpenRTM\rtm-namingのrtm-naming.py`の48行目を下記のように編集してください。~

```
 rtm-naming.py 48行目
  cmd = "omniNames -start "+str(port)+" -logdir \""+str(currdir)+"\" &"
```
<br>

&aname(pythonexe);
#### python.exeが起動しない  
環境変数 PathにPython インストールフォルダーを追加しておいてください(`C:\Python26`など)。
<br>

&aname(python);
#### Cygwin をインストールしている環境では python.exe が複数存在する場合がある 
Cygwin をインストールしている環境では、Cygwin上にも python.exe が存在する場合があります。その場合は、通例 Cygwin上の python.exe へのサーチパスが優先されるよう設定されるため、環境変数 Path を適切に設定しているのにもかかわらず、今回導入したはずの Python とは違うバージョンの（すなわちCygwin上の）python.exe が起動してしまう場合があります。この場合、Python のバージョンの違いによる不具合が発生してしまいます。この問題は非常に原因が特定しづらいのが特徴です。このように Cygwin などをインストールしている環境で OpenRTM-aist Python版を使う場合は、該当バージョンのpythonインストールフォルダーから python.exe が起動していることを確認してください。

- 確認方法の例
  - python -Vでバージョンを調べる、（Cygwinのある環境では）which python でどの python.exe が実行されているかを確認する...など
- この障害が発見された場合の対処
  - Pythonインストールフォルダー(`C:\Python26`など)を**システム環境変数 Path**（*ユーザー環境変数 Path ではなく）の**先頭に追加**することで解決できます。
<br>

#### Python2.6 + omniORBpy-3.4 で omniORB のインポート時に"ImportError: DLL load failed"エラーが発生する。
mscr71.dll が見つからないために発生するエラーです。msvcr71.dll を[こちら](http://reddog.s35.xrea.com/wiki/MSVCR71.DLL.html)から入手して、パスが通ったところにコピーしてください。)
<br>

&aname(MSVCerror);
#### 「MSVCP71.dll が見つからなかったため、…」というエラーで終了する 
WINDOWS\system32フォルダー内に msvcp71.dll がないために発生するエラーです。msvcp71.dll を[こちら](http://www.vector.co.jp/soft/win95/util/se435079.html)から入手してください。
<br>

&aname(rtc.conf);
#### 「Can't open file: ./rtc.conf」などと表示される。
RTコンポーネントの起動フォルダー（あるいはサーチパス上）に rtc.conf が見つからないため、起動できない状態です。この場合、次のように表示されます。~

```
 Can't open file: ./rtc.conf
 Can't open file: /etc/rtc.conf
 Can't open file: /etc/rtc/rtc.conf
 Can't open file: /usr/local/etc/rtc.conf
 Can't open file: /usr/local/etc/rtc/rtc.conf
```
これは rtc.conf を捜すサーチパスがデフォルトの状態であり、上記の順番で探したが見つからないためこのような表示になります。これを避けるためには、たとえば~
```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```
という内容のファイル rtc.conf を作成し、上記サーチパス上（通例はカレント＝コンポーネントと同じフォルダー）に配置します。
br>

#### コンポーネントがネームサービスに登録されない
rtc.conf の改行コードが CRLF になっている可能性が考えられます。~
以下のコマンドにて rtc.conf の確認を行い、CRLF という文字列が表示された場合、新たに rtc.conf の作成を行ってください。~
```
 $ file rtc.conf
```
<br>
## OpenRTM-aist (Java版)
### OS 共通
#### Java版コンポーネントでデータ転送に時間がかかる
Java版の RTコンポーネントと C++版など他の言語のコンポーネントとの間で、特に大きなデータ（100kB以上でみられることが多い。）を送受信する場合に、極端に速度が低下する場合があります。これは Java の CORBA 側の問題であることが知られており、タイムアウトを適切に設定することにより回避することができます。~
Java版の RTC が読み込む rtc.conf に以下のように記述することで、Java の CORBA のタイムアウトを設定します。~
```
 corba.args: -ORBTCPReadTimeouts 1:60000:300:1
```
Java (JDK1.5以降) ではデフォルトで、**100:3000:300:20** となっていますが、これを **1:60000:300:1** に変更するという意味です。各項目は左から、
- CORBA データを read するときに、0byte であったときに Read Thread が休止させられる時間(ms)
- CORBA データの read 時に Read Thread が待たされる累積最大時間 (ms)
- GIOP のヘッダーを read するときのタイムアウト(ms)
- CORBA データを read するときに、Read Thread が休止させられたときに、次回の休止の時間を増加する割合(%)

という意味になっています。したがって、**1:60000:300:1** は
- read して0byteのとき、Read Thread を 1ms休止する
- Read Thread が待つ最大累積時間は 6000ms
- GIOP のヘッダを read するときのタイムアウト時間は 300ms
- Read Thread の休止時間は1%づつ増加させる

という意味になります。~
大きなデータの場合、1回の read でデータが読み切れないので、通常何回か read を行います。~
次のデータはすぐには来ませんので、read は読み込みバイト数を 0byte として戻りますが、通常1ms以内には次のデータはやってきます。デフォルトの設定だと Read Thread が100ms待たされますが、そんなに長時間待つ必要はなく1ms程度待てば、すぐに次のデータを読み込むことができます。~
デフォルト設定の場合、100ms待って、さらにもう一度読み込み read が0を返すので、さらに100ms+20%の120ms待ちます。データが大きすぎれば、これを12回繰り返すと最大累積時間の3000msに達してしまうので、タイムアウトしてしまいますし、データが小さくても、データの分割数×100msの時間がかかってしまうので、非常に遅くなります。~
Java の CORBA ではデータを100kBで分割するので、これを超えるデータをやり取りする際には、上記の設定を rtc.conf にて行っておいたほうがよいでしょう。
<br>
### Windows

&aname(JDKver);
#### 「java -version」がインストールした JDK のバージョンと異なる。 
すでに JDK よりも新しいバージョンの JRE（Java Runtime Environment）がインストールされている場合は、JDK をインストールしても「java -version」が JRE のままになることがあります。この場合のインストールの確認方法を説明します。
 「プログラムの追加と削除」での確認方法|Windowsのコントロールパネルから「プログラムの追加と削除」を呼び出し、JDK5 がインストールされていることを確認してください。

<div align="center"><a href="add_or_delete_ja.png"><img src="add_or_delete_ja.png" width="80%;"></a></div>
<div align="center"><strong>JDK5を「プログラムの追加と削除」で確認</strong></div>

マイコンピューターからの確認方法|JDK をデフォルトでインストールした場合には、通常~

```
 C:\Program Files\Java\jdk1.6.0_21
```

というようなパスにインストールされるので、マイコンピューターで直接そのフォルダーの存在を確認します。

<div align="center"><a href="confirm_Java_ja.png"><img src="confirm_Java_ja.png" width="80%;"></a></div>
<div align="center"><strong>マイコンピューターからJDK5を確認</strong></div>
<br>

### Unix

&aname(javafedora);
#### FedoraCore で Java をインストールする際の対応 
OS が FedoraCore の場合、yum にて Java をインストールすると GCJ (The GNU Compiler for Java ) がインストールされてしまい、その GCJ を使用するといくつかの不具合が生じる事があります。~
不具合が発生した場合は、まず、Oracle の Java が使用されているかの確認をしてください。
- **参考**[JDKインストールのためのヒント]({{ site.baseurl }}/en/doc/installation/install_1_1/java_1_1/tips_jdk#fedora)
- [**UNIX系環境で簡易に Oracle の Java を Eclipse に適用する方法**]({{ site.baseurl }}/en/doc/faq/faq_rtp_tools#rtclinksunjava)

