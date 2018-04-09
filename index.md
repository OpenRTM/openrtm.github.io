---
layout: default
---

# OpenRTM-aist web on the github

OpenRTM-aist臨時Webページ

## Download

### Linux pakages


| Dist/version  | URL                                      |
|:--------------|:-----------------------------------------| 
| Ubuntu 14.04  | https://github.com/n-ando/trusty_pakcage |
| Ubuntu 16.04  | https://github.com/n-ando/xenial_pakcage |

```shell
$ git clone https://github.com/n-ando/xenial_package.git

ubuntu 16.04 (64bit) の場合
$ cd xenial_package/xenial/main/binary-amd64/

C++版のインストール
$ sudo dpkg -i openrtm-aist-1.1.2-0_amd64.deb
$ sudo dpkg -i openrtm-aist-example_1.1.2-0_amd64.deb
$ sudo dpkg -i openrtm-aist-dev_1.1.2-0_amd64.deb

Python版のインストール
$ sudo dpkg -i openrtm-aist-python_1.1.2-1_amd64.deb
$ sudo dpkg -i openrtm-aist-python-example_1.1.2-1_amd64.deb

RTSystemEditor/RTCBuilderのインストール
$ sudo dpkg -i openrtp_1.2.0-0_amd64.deb
```

### Windows installer

| 32bit/64bit   | URL                                      |
|:--------------|:-----------------------------------------| 
| 32bit msi     | https://github.com/n-ando/win32_pakcage  |
| 64bit msi     | https://github.com/n-ando/win64_pakcage  |

msiファイルはそのままではダウンロードできません。以下の手順でmsiをダウンロードしてください。

#### Git for Windowsのダウンロード

- Git for windows
  - https://git-scm.com/download/win

#### gitによるダウンロード

```shell
> git clone https://github.com/n-ando/win64_pakage.git
> cd win64_package
win64_package の中に、OpenRTM-aist-1.1.2-RELEASE_x86_64.msi がダウンロードされています。
```

## NEWS

### ROBOMECH2018 RTM講習会

#### 日時・場所
- 主催: 国立研究開発法人 産業技術総合研究所
- 協賛: ROBOMECH2018, (公社)計測自動制御学会システムインテグレーション部門
- 日時: 2018年6月3日(日), 10:00〜17:00 
- 場所: 北九州国際コンベンションゾーン
- 聴講料: 無料
  - 講習会のみの参加の場合ROBOMEC2018への参加登録は不要ですが、可能な限り参加登録をお願いします。
- 定員: 第1部50名, 実習（第2, 3部）30名程度を予定しております。定員になり次第申し込みは終了させていただきます。第1部のみご参加の方は申し込み不要です。

#### プログラム

| 10:00 -10:50	| 第1部(その1)：インターネットを利用したロボットサービスとRSiの取り組み2018 <br>　担当：成田雅彦 氏（産業技術大学院大学）|
| 11:00 -11:50	| 第1部(その2)：OpenRTM-aistおよびRTコンポーネントプログラミングの概要 <br> 担当：安藤慶昭 氏 (産総研) |
| 11:50 -12:00	| 質疑応答・意見交換 |
| 12:00 -13:00	| 昼食 |
| 13:00 -14:30	| 第2部: RTコンポーネントの作成入門 <br>　　　　　　担当：宮本信彦 氏 (産総研) 他 <br>　　　　　　概要：RTシステムを設計するツールRTSystemEditorおよびRTコンポーネント<br>　　　　　　　　　を作成するツールRTCBuilderの使用方法について解説するとともに、<br>　　　　　　　　　RTCBuilderを使用したRTコンポーネントの作成方法を実習形式で<br>　　　　　　　　　体験していただきます。|
| 14:45 -17:00	| 第3部：プログラミング実習 <br>　　　　　　担当：宮本信彦 氏 (産総研) 他 <br>　　　　　　概要：OpenRTM-aistを利用してロボットを制御するプログラムを実際に作成します。|

- 問い合わせ： n-ando@aist.go.jp


