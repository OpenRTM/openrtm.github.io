---
layout: page
title: コンパイル方法 (ubuntu、cmake、code::blocks利用)
---

<!-- Title: コンパイル方法 (Ubuntu、CMake、Code::Blocks利用) -->
このページでは Ubuntu での Code::Blocks を利用したビルドの方法を説明します。

#contents

## 環境準備
Code::Blocks は以下のコマンドでインストールできます。

```
 sudo apt-get install codeblocks
```

そのほか Doxygen、CMake がインストール済みでない場合は以下のコマンドでインストールを行います。

```
 sudo apt-get install doxygen cmake
```

## ビルド手順

### CMake

RTC ビルダで生成したコードのフォルダーに移動して、以下のコマンドを入力すると build フォルダーに各種ファイルが生成されます。

```
 mkdir build
 cd build
 cmake . -G "CodeBlocks - Unix Makefiles"
```


### Code::Blocks の実行

buildフォルダーの～.cbpを開きます。

<div align="center"><a href="codeblocks2.png"><img src="codeblocks2.png" width="50%;"></a></div>
<br>

[ビルド] ボタンをクリック(もしくは Ctrl+F9)することでビルドが実行されます。

<div align="center"><a href="codeblocks1.png"><img src="codeblocks1.png" width="50%;"></a></div>
<br>

これでbuild/srcフォルダーに実行ファイル、共有ライブラリが生成されます。
