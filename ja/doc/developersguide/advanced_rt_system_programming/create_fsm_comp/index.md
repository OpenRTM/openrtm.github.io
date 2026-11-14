---
layout: page
title: "fsmコンポーネント作成手順"

---
<!-- Title: FSMコンポーネント作成手順 -->
## RTCBuilderでのコード生成

まずは通常のRTC作成手順と同じくプロジェクトの作成、モジュール名の設定、言語の設定(C++)を行います。

次にFSMタブからFSMのチェックボックスをオンにします。
さらに新規作成ボタンを押してGUIエディタを起動します。

<div align="center"><a href="fsm1.png"><img src="fsm1.png" width="30%;"></a></div>


起動したエディタで右クリックして**Add node**を選択する。

<div align="center"><a href="fsm2.png"><img src="fsm2.png" width="30%;"></a></div>

作成したノードを右クリックして**Edit node**を選択します。

<div align="center"><a href="fsm3.png"><img src="fsm3.png" width="30%;"></a></div>

**State Name**を適当な名前に変更します。

<div align="center"><a href="fsm4.png"><img src="fsm4.png" width="30%;"></a></div>

同様の手順でノードを複数作成します。
以下の図ではToggle Initial、Toggle finalを設定しているノードがありますが、この設定により生成するコードは変化しないようです。

<div align="center"><a href="fsm8.png"><img src="fsm8.png" width="30%;"></a></div>

一部のノードは**On Entry**、**On Exit**をオンにしてください。

<div align="center"><a href="fsm7.png"><img src="fsm7.png" width="30%;"></a></div>

またノードからノードへドラッグアンドドロップすることで状態遷移を定義します。

<div align="center"><a href="fsm8-2.png"><img src="fsm8-2.png" width="30%;"></a></div>

エディタを閉じます。

<div align="center"><a href="fsm10.png"><img src="fsm10.png" width="30%;"></a></div>

その後、コード生成を行います。

<div align="center"><a href="fsm11.png"><img src="fsm11.png" width="30%;"></a></div>


## RTCのビルド
ビルドにはOpenRTM-aist 2.0が必要です。
以下の手順でOpenRTM-aistでビルドしてください。

- [https://openrtm.org/openrtm/ja/content/cmake_build_rtm]({{ site.baseurl }}/ja/doc/developersguide/advanced_rt_system_programming/openrtm_cpp_cmake_build)

その後、INSTALLのプロジェクトをビルドして適当な場所にインストールしてください。
インストールする場所を変更するためにはCMAKE_INSTALL_PREFIXのオプションを変更します。

RTCのコードを生成したフォルダで以下のコマンドを実行します。

```
 mkdir build
 cd build
 set OPENRTM_DIR={OpenRTM-aistをインストールしたディレクトリ}\2.0.0\cmake\
 cmake -G "Visual Studio 15 2017" -A x64 ..
 cmake --build . --config Release
```

## コードの編集
執筆中

## 動作確認手順


