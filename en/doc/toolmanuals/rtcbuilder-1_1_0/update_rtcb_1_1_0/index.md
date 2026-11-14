---
layout: page
title: 更新方法 
---
-------jp page!!-------

<!-- Title: 更新方法 -->
#contents
ここでは、OpenRTP（RTCBuilder、RTSystemEditorの総称）をアップデートする手順を説明します。OpenRTP は Eclipse のプラグインとして提供しているので、Eclipse 上で操作します。

### OpenRTP の更新
Eclipse のメニューで、[ヘルプ] > [新規ソフトウエアのインストール] を選択します。

<div align="center"><a href="openrtp_01.jpg"><img src="openrtp_01.jpg" width="40%;"></a></div>

「インストール」ダイアログの [追加] ボタンをクリックし、リポジトリを追加します。名前とロケーションは以下のように指定します。
- **名前** : OpenRTP
- **ロケーション** : http://openrtm.org/pub/openrtp/stable/updates/

<div align="center"><a href="openrtp_02.jpg"><img src="openrtp_02.jpg" width="40%;"></a></div>

OpenRTP 1.1.0 をチェックし [次へ] または [完了] ボタンをクリックします。
<br>
インストール途中で証明書の信頼についての問い合わせ画面が開きますので、レ点を入れて [OK] ボタンをクリックしてください。

<div align="center"><a href="openrtp_03.jpg"><img src="openrtp_03.jpg" width="50%;"></a></div>

インストール後は指示に従い再始動すると更新が反映されます。

### 既存のコンポーネントへの反映方法

すでに、生成したコンポーネントのプロジェクに関しては、次の手順等で対処してください。

- eclipse にもう一度読み込んでコードを再生成します（eclipse 上でいったんプロジェクトを削除し、改めてインポートする）
- eclipse のパッケージ・エクスプローラ画面で、プロジェクト内の RTC.xml をダブルクリックし、[コード生成] ボタンをクリックします
- この時 diff 画面が表示されるので、idl/CMakeLists.txt のみを更新します

Linux や Mac なら単純に sed で置換します。

```
 $ sed -ie 's/\"\${ALL_IDL_SRCS}\"/ALL_IDL_SRCS/' idl/CMakeLists.txt
```

-------jp page!!-------
