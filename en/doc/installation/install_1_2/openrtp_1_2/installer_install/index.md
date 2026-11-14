---
layout: page
title: インストーラによるインストール
---
<br>
<a>No English version available.
</a>

<!-- Title: インストーラによるインストール -->

#contents
ここでは、RTSystemEditorとRPCBuilder(OpenRTP)をインストーラを用いてインストールする方法を述べます。


# Windowsでのインストール
- [OpenRTM-aist 1.2系のインストール(Windows、msiインストーラー使用)]({{ site.baseurl }}/en/doc/appendix/openrtm-aist_1_2_windows_msi)

を用いてインストールしてください。デフォルトではこのインストーラが対応している全てのソフトウエアがインストールされます。必要に応じてインストール途中で[カスタム]を選択し、OpenRTPと開発に使用する言語に合わせたOpenRTM-aistランタイムや開発環境をインストールしてください。(なお現状ではデフォルト以外のインストールに対する検証は十分なされていないので、一部だけのインストールでは必要なものがインストールされないなどの問題が起こる可能性があります。デフォルトでインストールするか、各自検証しながら必要なものを別途追加インストールしてください。)
# Linuxでのインストール
[一括インストールスクリプト]({{ site.baseurl }}/en/doc/appendix/bulk_installation_script)を使用して、
root権限で
```
 $ sudo sh pkg_install_xxxx.sh -l openrtp --yes
```
ここで
: xxxx|インストール先のOSの種類を指定する文字列で、ubuntu、debian、raspbian、fedoraのどれかが指定できる。
とすることによってインストールができます。(”sudo ”は環境によっては、別途suコマンドを使うことによって指定する必要がない場合があります。)
またOpenRTP自体は開発ツールであり実際の使用においては言語対応の開発環境がインストールされていることが必要です。よって、一括インストールでは-lオプションでc++、python、javaのどれかを指定して開発対象に合わせたOpenRTM-aistをインストールする必要がありますのでご注意ください。

# JDK8のインストール
OpenRTPの使用にはJDK8相当のJDKが必要です。インストーラにはOpenRTPを実行するPlatformとなるEclipseの実行をするためにOpen JDK8をインストールするようになっていますが、ライセンス条件やサポート条件を満たすために別のJDKが必要な場合は下記のリンクを参照して、別途JDK8をインストールしてください。また一部のOSではJDK8でないJDKがデフォルトでインストールされるためそれをデフォルト使用からはずす必要があることがああります。そのケースでも下記のリンクを参照してください。
- [JDK8のインストール]({{ site.baseurl }}/en/doc/installation/common/install_jdk8)

また、OpenRTPのEclipse環境の実行に使われるJDKはOpenRTP GUI (Eclipse GUI)の中で別途設定する必要があります。OpenRTPを起動後、[Window]>[設定]と選択し、開いたダイアログより、[Java]の横の[>]をクリックし[インストール済みのJRE]クリックして設定してください。



