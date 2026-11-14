---
layout: page
title: インストールに関する faq
---

<!-- Title:  インストールに関する FAQ -->
#contents
#clear

## Windows

### WindowsでPythonをインストールしてもバージョン番号が表示されない
OpenRTM-aistがサポートしているPythonバージョンをインストールし、その際Pythonのパスを通したのに、コマンドプロンプトで確認するとバージョン番号が表示されないことがあります。

```
 >python --version
 Python
```

**原因：**
- 先にMicrosoft Store 等からダウンロードされたものがインストールされている可能性があります
- where pythonコマンドでインストール先を確認してください
```
 >where python
```

**対処方法：**
- Pythonのアプリ実行エイリアスを確認し、オンになっていたらオフに変更してWindowsを再起動して下さい
- Windowsの設定 → アプリと機能 → アプリ実行エイリアスで、「pytnon.exe」と「python3.exe」をオフにする


再起動後にコマンドプロンプトでPythonのバージョン番号が表示されることを確認して下さい。
Pythonインストール時のパスを通す手順は、下記ページの解説をご覧ください。 <br>
[OpenRTM-aistを10分で始めよう！・Pythonのインストール]({{ site.baseurl }}/ja/doc/installation/lets_start#toc1) 


<br>
<br>

### Windows Defenderからの警告が出る
ネームサーバやサンプルコンポーネントを起動しようとすると、Windows Defenderのファイアウォールにより[Windows セキュリティの重要な警告]ダイアログが表示されることがあります。
<br>
<br>
**対処方法：**
[プライベート ネットワーク(ホームネットワークや社内ネットワークなど)(R)]にチェックを入れ[パブリックネットワーク(空港、喫茶店など)(非推奨)(U)]のチェックをはずしてアクセスを許可する(A)]をクリックしてください。
<br>
<br>

### Windows10 へ OpenRTM-aist 1.1.2版をインストールしたが、PATH に追加されていない
**原因：**
- Windows10 のみでの現象の可能性があります。
- PATH の設定が長いと長さ制限のために切り捨てられる可能性があります。


**対処方法：**
インストール後にPCを再起動してください。
<br>
<br>

### Windows10 で omniORB の PATH設定が展開されていない

Windows10 で setコマンドを確認したところ、omniORBの PATH設定 %OMNI_ROOT% の変数部分が展開されていなかった。
<br>
<br>
**原因：**
- Windows10 のみでの現象の可能性があります。
- PATH が展開されていない可能性があります。


**対処方法：**
インストール後にPCを再起動してください。
<br>
<br>

### Eclipse が起動できない
JRE がインストールされていない可能性がありますので、対応バージョンの JRE をインストールしてください。
<br>
<br>


## UNIX

### パッケージの自動インストールでダウンロードエラーが表示される 
OpenRTM-aist に付属する自動インストーラーは、パッケージの有無とバージョンを確認し、適当なパッケージがインストールされていない場合に各パッケージのダウンロードサイトからダウンロード及び加工するものです。
このため、自動インストーラーでインストールする場合には、コンピューターを必ずインターネットに接続してください。~
ネットワーク接続が正常でもダウンロードエラーが出る場合、回線の混雑等でウンロードに失敗した場合と、ダウンロードサイト側でファイルの場所や名前が変わった可能性が考えられます。
前者の場合は時間帯等をずらして再度自動インストーラーを実行してみてください。また後者の場合には、該当するパッケージを探してから個々にダウンロードして手動インストールするか、自動インストーラーのダウンロード元アドレスを修正してから改めて起動してください。~
<br>
<br>

&aname(openrtminstfault);
### OpenRTM-aist のインストールに失敗する 
古いバージョンの OpenRTM-aist が完全にアンインストールされていない場合、新しいバージョンのインストールができません。古いバージョンを一度アンインストールしてから、再度インストール作業をします。
#### Fedora・Ubuntu・Debian 共通：
pkg_install_XXXX.sh を利用してアンインストールする。~

```
 >su
 #pkg_install_XXXX.sh -u
```

アンインストールの許可を求められるので、**「y」** を入力しながら完了させます。
あるいは次の手順に従います。

#### Fedora：
yumコマンドでアンインストールする。次の手順でアンインストールを行ってください。~

```
 >su

 #yum remove OpenRTM-aist-example
 #yum remove OpenRTM-aist-dev
 #yum remove OpenRTM-aist-doc
 #yum remove OpenRTM-aist
```
#### Ubuntu / Debian：
apt-getコマンドでアンインストールする。次の手順でアンインストールを行ってください。~
```
 >su

 #apt-get remove OpenRTM-aist-example
 #apt-get remove OpenRTM-aist-dev
 #apt-get remove OpenRTM-aist-doc
 #apt-get remove OpenRTM-aist
```
<br>
<br>

&aname(notusecd);
### apt-get などを使用してインストール作業を行うときに CD を要求される 
Ubuntu、Debian などのディストリビューションで、apt-get や pkg_install_ubuntu.sh, pkg_install_debian.sh を使用してインストール作業をしていると、次のように CD を求められることがあります。
メディア変更:~
```
 　　'Ubuntu 7.10 _Gutsy Gibbon_ Japanese Remix - Release i386 (20071018)'
```

とラベルの付いたディスクをドライブ '/cdrom/' に入れて Enter を押してください。~
もちろん、CD を用意すればよいことなのですが、諸事情により用意できない場合の対処方法を記述します。~
この場合はとりあえず、**C-c**(Ctrl+c) を入力してインストール作業を中断し、以下の手順でインストール作業をやり直してください。

:1. **/etc/apt/sources.list** の編集をする

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

または、~
```
 #deb cdrom:[Debian GNU/Linux 4.0 r3 _Etch_ - Official i386 NETINST Binary-1 20080218-14:15]/ etch contrib main
```

:2. インストール作業をやり直す
先ほど中断したインストール作業を始めからやり直してください。
<br>
