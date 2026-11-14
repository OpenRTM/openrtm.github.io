---
layout: page
title: ビュー（リポジトリビュー編）
---

<!-- Title: ビュー（リポジトリビュー編） -->
#contents

ここでは、リポジトリビューについて解説します。
<br>

RTC-RepositoryView は、RTコンポーネント仕様記述ファイルを読み込み、ツリービューで表示する機能をもっています。
<br>

<div align="center"><a href="figREP2_1RepositoryView.png"><img src="figREP2_1RepositoryView.png" width="45%;"></a></div>
<div align="center"><strong>RTC-RepositoryView</strong></div>
<br>


### ファイルのロード
ここでは、RTC-RepositoryView に RTコンポーネント仕様記述ファイルを指定して表示する方法を説明します。<br>
RTC-RepositoryView 内で右クリックし、表示されるコンテキストメニューから [Load File] を選択すると、ファイル選択ダイアログが表示されます。ここで RTC-RepositoryView に読み込む RTコンポーネント仕様記述ファイルを選択します。<br>
このダイアログは xml ファイルのみ表示するようフィルタがかかります。
<br>

<div align="center"><a href="figREP2_2LoadFile.png"><img src="figREP2_2LoadFile.png" width="70%;"></a></div>
<div align="center"><strong>ファイルのロード</strong></div>
<br>

ローカルに存在する RTコンポーネント仕様記述ファイルを読み込んだ場合、最上位階層は読み込んだ RTコンポーネント仕様記述ファイルの絶対パスを表示します。そして、２階層目は RTコンポーネント仕様記述ファイル内で定義されている category 属性の値を表示します。また３階層目は RTコンポーネント仕様記述ファイル内の name 属性に記述されている値と RTコンポーネント仕様記述ファイル名を表示します。


### ディレクトリーのロード
ここでは、RTコンポーネント仕様記述ファイルが存在するディレクトリーを指定して、ディレクトリー内の全ファイルの読み込み、表示を行う方法を説明します。<br>
RTC-RepositoryView 上で右クリックし、表示されるコンテキストメニューから [Load Dir] を選択すると、ディレクトリー選択ダイアログが表示されます。RTC-RepositoryView に読み込むディレクトリーを選択します。ディレクトリー以下に存在する RTコンポーネント仕様記述ファイルを読み込みます。
<br>

<div align="center"><a href="figREP2_3LoadDir.png"><img src="figREP2_3LoadDir.png" width="70%;"></a></div>
<div align="center"><strong>ディレクトリーのロード</strong></div>
<br>

表示方法はファイルのロードと同様です。<br>
すでに展開したディレクトリーに新しい RTコンポーネント仕様記述ファイルを追加し、再度読み込みを行うと追加された RTコンポーネント仕様記述ファイルのみ読み込まれます。
<br>


### 削除
RTC-RepositoryView のコンポーネントは、RTC-RepositoryView 上で右クリックし、コンテキストメニューから [Delete] を選択して削除することが可能です。<br>
[Delete] はパス、category、コンポーネントのいずれかを選択している場合のみ選択できます。
<br>

<div align="center"><a href="figREP2_4Delete.png"><img src="figREP2_4Delete.png" width="70%;"></a></div>
<div align="center"><strong>コンポーネントの削除</strong></div>
<br>

最上位階層であるパスを削除すると、下位の category、コンポーネントも同時に削除されます。また３階層目のコンポーネントを削除し、他のコンポーネントが存在しない場合は再帰的に最上位階層まで削除されます。
<br>

