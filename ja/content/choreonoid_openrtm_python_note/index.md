---
layout: page
title: "choreonoid用openrtm連携プラグイン python版(備考)"
---
#contents

### Choreonoid OpenRTM連携プラグインについて
Choreonoid標準で付属しているOpenRTM連携プラグインには以下の機能がありません。

- コンフィギュレーションパラメータ設定機能
- コネクタ接続時のデータ型判別機能

これらの機能は近いうちに追加される予定らしいですが、現状ではコンフィギュレーションパラメータの設定はRTShell等で外部から実行してください。

コネクタ接続時にデータ型が違っても接続するため注意が必要です。


### 既知のバグ

RTCEditorでPythonモジュールが読み込めない環境が存在するらしいです。
原因は調査中です。


### 未実装の機能

ComponentListアイテムで起動したRTCをシミュレータがtickで実行する機能は現在のところ未実装です。



### 使用したライブラリ

使用したライブラリは以下の通りです。

- Choreonoid
- boost-1.6.1
- Eigen
- omniORB-4.2.2
- OpenRTM-aist-1.2.0
- pybind11
- Python-2.7.13
- Qt 5.8
- yaml-0.1.7


また、サンプルコンポーネントに以下のライブラリを使用しています。

- ODE-0.13
- PySDL2
- SDL2

### Choreonoidに関するメモ
- アイテムの順番が環境によって違う事がある
- プラグインの日本語化には**po**フォルダの中に言語ファイル**ja.po**を用意する。
```
 Pluginルートディレクトリ
```
<table class="table-alt">
  <tr>
    <th>-po</th>
  </tr>
  <tr>
    <td>-ja.po</td>
  </tr>
</table>

ja.poの中身には以下のように翻訳前と翻訳後の文字を羅列する。

```
 msgid "RTC directory"
 msgstr "RTCディレクトリ"
```

これで自動的にPOファイルをMOファイルにコンパイルするはずですが、Choreonoidはプラグイン名に対応するファイルをロードするため、プラグイン名は正しく設定する必要がある。


