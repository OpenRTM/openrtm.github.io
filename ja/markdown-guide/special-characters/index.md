---
layout: page
title: 特殊文字
date: 2026-10-08
---

#contents

## 目次


見出しのレベル3まで設定した項目で目次を作成し、ページ先頭に表示します。

```
 #contents
```


デフォルトではレベル3までの項目が目次に表示されます。それ以下のレベルを表示したいときは表示したいレベルまでの
```
 #contents(4)
```
#contents(4)


## タブコード

※  未対応

```
 タブコード&t;を間&t;に&t;入れ&t;&t;る。
  - タブコード&Tab;を間&Tab;に&Tab;入れ&Tab;&Tab;る。
```
  - タブコード&Tab;を間&Tab;に&Tab;入れ&Tab;&Tab;る。


## ページ名置換文字
```
  - ページ名: &lbrace;&lbrace; page.title &rbrace;&rbrace;
  - ベースURL: &lbrace;&lbrace; site.baseurl &rbrace;&rbrace;
  - ページURL: &lbrace;&lbrace; page.url &rbrace;&rbrace;
```

  - ページ名: {{ page.title }} 
  - ベースURL: {{ site.baseurl }} 
  - ページURL: {{ page.url }} 

  - 記事の作成日(フロントマターの date): {{page.date}}
  - フロントマターに明記していない場合、Jekyllが自動的にファイルの最終書き込み日時（mtime）を割り当てる: {{page.last_modified_at}} ※  未対応

## 日時置換文字

※  未対応

<table class="table-alt">
  <tr>
    <th>&date;</th>
    <th>&amp;date;</th>
    <th>更新時の日付</th>
  </tr>
  <tr>
    <td>&time;</td>
    <td>&amp;time;</td>
    <td>更新時の時刻</td>
  </tr>
  <tr>
    <td>&now;</td>
    <td>&amp;now;</td>
    <td>更新時の日時</td>
  </tr>
</table>



## 文字参照文字
<table class="table-alt">
  <tr>
    <th>文字</th>
    <th>表記</th>
    <th>意味</th>
  </tr>
  <tr>
    <td>&lt;</td>
    <td>&amp;lt;</td>
    <td>小なり</td>
  </tr>
  <tr>
    <td>&gt;</td>
    <td>&amp;gt;</td>
    <td>大なり</td>
  </tr>
  <tr>
    <td>&amp;</td>
    <td>&amp;amp;</td>
    <td>アンパサンド</td>
  </tr>
  <tr>
    <td>&quot;</td>
    <td>&amp;quot;</td>
    <td>ダブルクォート</td>
  </tr>
  <tr>
    <td>&apos;</td>
    <td>&amp;apos;</td>
    <td>アポストリフィ</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td>&amp;nbsp;</td>
    <td>ノーブレークスペース</td>
  </tr>
  <tr>
    <td>&iexcl;</td>
    <td>&amp;iexcl;</td>
    <td>逆立ち感嘆符</td>
  </tr>
  <tr>
    <td>&cent;</td>
    <td>&amp;cent;</td>
    <td>セント記号</td>
  </tr>
  <tr>
    <td>&pound;</td>
    <td>&amp;pound;</td>
    <td>英貨ポンド記号</td>
  </tr>
  <tr>
    <td>&curren;</td>
    <td>&amp;curren;</td>
    <td>一般通貨記号</td>
  </tr>
  <tr>
    <td>&yen;</td>
    <td>&amp;yen;</td>
    <td>円記号</td>
  </tr>
  <tr>
    <td>&sect;</td>
    <td>&amp;sect;</td>
    <td>節記号</td>
  </tr>
  <tr>
    <td>&uml;</td>
    <td>&amp;uml;</td>
    <td>ウムラウト</td>
  </tr>
  <tr>
    <td>&copy;</td>
    <td>&amp;copy;</td>
    <td>著作権記号</td>
  </tr>
  <tr>
    <td>&ordf;</td>
    <td>&amp;ordf;</td>
    <td>順序の指示（女性形）</td>
  </tr>
  <tr>
    <td>&laquo;</td>
    <td>&amp;laquo;</td>
    <td>左角引用符</td>
  </tr>
  <tr>
    <td>&not;</td>
    <td>&amp;not;</td>
    <td>否定記号</td>
  </tr>
  <tr>
    <td>&reg;</td>
    <td>&amp;reg;</td>
    <td>登録商標</td>
  </tr>
  <tr>
    <td>&macr;</td>
    <td>&amp;macr;</td>
    <td>マクロン</td>
  </tr>
  <tr>
    <td>&deg;</td>
    <td>&amp;deg;</td>
    <td>度記号</td>
  </tr>
  <tr>
    <td>&plusmn;</td>
    <td>&amp;plusmn;</td>
    <td>加減符</td>
  </tr>
  <tr>
    <td>&acute;</td>
    <td>&amp;acute;</td>
    <td>鋭アクセント</td>
  </tr>
  <tr>
    <td>&micro;</td>
    <td>&amp;micro;</td>
    <td>ミクロン記号</td>
  </tr>
  <tr>
    <td>&para;</td>
    <td>&amp;para;</td>
    <td>段落記号</td>
  </tr>
  <tr>
    <td>&middot;</td>
    <td>&amp;middot;</td>
    <td>中黒</td>
  </tr>
  <tr>
    <td>&cedil;</td>
    <td>&amp;cedil;</td>
    <td>セディーユ</td>
  </tr>
  <tr>
    <td>&ordm;</td>
    <td>&amp;ordm;</td>
    <td>順序の指示（男性形）</td>
  </tr>
  <tr>
    <td>&raquo;</td>
    <td>&amp;raquo;</td>
    <td>右角引用符</td>
  </tr>
  <tr>
    <td>&iquest;</td>
    <td>&amp;iquest;</td>
    <td>逆立ち疑問符</td>
  </tr>
  <tr>
    <td>&Agrave;</td>
    <td>&amp;Agrave;</td>
    <td>大文字 A（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Aacute;</td>
    <td>&amp;Aacute;</td>
    <td>大文字 A（鋭アクセント付）</td>
  </tr>
  <tr>
    <td>&Acirc;</td>
    <td>&amp;Acirc;</td>
    <td>大文字 A（曲折アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Atilde;</td>
    <td>&amp;Atilde;</td>
    <td>大文字 A（ティルデ付）</td>
  </tr>
  <tr>
    <td>&Auml;</td>
    <td>&amp;Auml;</td>
    <td>大文字 A（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&Aring;</td>
    <td>&amp;Aring;</td>
    <td>大文字 A（輪付）</td>
  </tr>
  <tr>
    <td>&AElig;</td>
    <td>&amp;AElig;</td>
    <td>大文字 AE 二重母音（合字）</td>
  </tr>
  <tr>
    <td>&Ccedil;</td>
    <td>&amp;Ccedil;</td>
    <td>大文字 C（セディーユ付）</td>
  </tr>
  <tr>
    <td>&Egrave;</td>
    <td>&amp;Egrave;</td>
    <td>大文字 E（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Eacute;</td>
    <td>&amp;Eacute;</td>
    <td>大文字 E（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Ecirc;</td>
    <td>&amp;Ecirc;</td>
    <td>大文字 E（曲折アクセント付）</td>
  </tr>
  <tr>
    <td>&Euml;</td>
    <td>&amp;Euml;</td>
    <td>大文字 E（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&Igrave;</td>
    <td>&amp;Igrave;</td>
    <td>大文字 I（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Iacute;</td>
    <td>&amp;Iacute;</td>
    <td>大文字 I（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Icirc;</td>
    <td>&amp;Icirc;</td>
    <td>大文字 I（曲折アクセント付）</td>
  </tr>
  <tr>
    <td>&Iuml;</td>
    <td>&amp;Iuml;</td>
    <td>大文字 I（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&Ntilde;</td>
    <td>&amp;Ntilde;</td>
    <td>大文字 N（ティルデ付）</td>
  </tr>
  <tr>
    <td>&Ograve;</td>
    <td>&amp;Ograve;</td>
    <td>大文字 O（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Oacute;</td>
    <td>&amp;Oacute;</td>
    <td>大文字 O（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Ocirc;</td>
    <td>&amp;Ocirc;</td>
    <td>大文字 O（曲折アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Otilde;</td>
    <td>&amp;Otilde;</td>
    <td>大文字 O （ティルデ付）</td>
  </tr>
  <tr>
    <td>&Ouml;</td>
    <td>&amp;Ouml;</td>
    <td>大文字 O（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&Oslash;</td>
    <td>&amp;Oslash;</td>
    <td>大文字 O（スラッシュ付）</td>
  </tr>
  <tr>
    <td>&Ugrave;</td>
    <td>&amp;Ugrave;</td>
    <td>大文字 U（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Uacute;</td>
    <td>&amp;Uacute;</td>
    <td>大文字 U（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Ucirc;</td>
    <td>&amp;Ucirc;</td>
    <td>大文字 U（曲折アクセント記号付）</td>
  </tr>
  <tr>
    <td>&Uuml;</td>
    <td>&amp;Uuml;</td>
    <td>大文字 U（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&szlig;</td>
    <td>&amp;szlig;</td>
    <td>ドイツ語の小文字鋭 s（sz 合字）</td>
  </tr>
  <tr>
    <td>&agrave;</td>
    <td>&amp;agrave;</td>
    <td>小文字 a（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&aacute;</td>
    <td>&amp;aacute;</td>
    <td>小文字 a（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&acirc;</td>
    <td>&amp;acirc;</td>
    <td>小文字 a（曲折アクセント記号付）</td>
  </tr>
  <tr>
    <td>&atilde;</td>
    <td>&amp;atilde;</td>
    <td>小文字 a（ティルデ付）</td>
  </tr>
  <tr>
    <td>&auml;</td>
    <td>&amp;auml;</td>
    <td>小文字 a（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&aring;</td>
    <td>&amp;aring;</td>
    <td>小文字 a（輪付）</td>
  </tr>
  <tr>
    <td>&aelig;</td>
    <td>&amp;aelig;</td>
    <td>小文字 ae 二重母音（合字）</td>
  </tr>
  <tr>
    <td>&ccedil;</td>
    <td>&amp;ccedil;</td>
    <td>小文字 c（セディーユ付）</td>
  </tr>
  <tr>
    <td>&egrave;</td>
    <td>&amp;egrave;</td>
    <td>小文字の e（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&eacute;</td>
    <td>&amp;eacute;</td>
    <td>小文字の e（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&ecirc;</td>
    <td>&amp;ecirc;</td>
    <td>小文字の e（曲折アクセント記号付）</td>
  </tr>
  <tr>
    <td>&euml;</td>
    <td>&amp;euml;</td>
    <td>小文字の e（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&igrave;</td>
    <td>&amp;igrave;</td>
    <td>小文字の i（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&iacute;</td>
    <td>&amp;iacute;</td>
    <td>小文字の i（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&icirc;</td>
    <td>&amp;icirc;</td>
    <td>小文字の i（曲折アクセント記号付）</td>
  </tr>
  <tr>
    <td>&iuml;</td>
    <td>&amp;iuml;</td>
    <td>小文字の i（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&ntilde;</td>
    <td>&amp;ntilde;</td>
    <td>小文字 n（ティルデ付）</td>
  </tr>
  <tr>
    <td>&ograve;</td>
    <td>&amp;ograve;</td>
    <td>小文字 o（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&oacute;</td>
    <td>&amp;oacute;</td>
    <td>小文字 o（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&ocirc;</td>
    <td>&amp;ocirc;</td>
    <td>小文字 o（曲折アクセント記号付）</td>
  </tr>
  <tr>
    <td>&otilde;</td>
    <td>&amp;otilde;</td>
    <td>小文字 o（ティルデ付）</td>
  </tr>
  <tr>
    <td>&ouml;</td>
    <td>&amp;ouml;</td>
    <td>小文字 o（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&divide;</td>
    <td>&amp;divide;</td>
    <td>除算記号</td>
  </tr>
  <tr>
    <td>&oslash;</td>
    <td>&amp;oslash;</td>
    <td>小文字 o（斜線付）</td>
  </tr>
  <tr>
    <td>&ugrave;</td>
    <td>&amp;ugrave;</td>
    <td>小文字 u（重アクセント記号付）</td>
  </tr>
  <tr>
    <td>&uacute;</td>
    <td>&amp;uacute;</td>
    <td>小文字 u（鋭アクセント記号付）</td>
  </tr>
  <tr>
    <td>&ucirc;</td>
    <td>&amp;ucirc;</td>
    <td>小文字 u（曲折アクセント記号付）</td>
  </tr>
  <tr>
    <td>&uuml;</td>
    <td>&amp;uuml;</td>
    <td>小文字 u（ウムラウト付）</td>
  </tr>
  <tr>
    <td>&yuml;</td>
    <td>&amp;yuml;</td>
    <td>小文字 y（ウムラウト付）</td>
  </tr>
</table>

## 数値参照文字 

例

<table class="table-alt">
  <tr>
    <th>文字</th>
    <th>表記</th>
    <th>意味</th>
  </tr>
  <tr>
    <td>&#9834;</td>
    <td>&amp; #9834;</td>
    <td>音符</td>
  </tr>
  <tr>
    <td>&#x266A;</td>
    <td>&amp; #x266A;</td>
    <td>音符</td>
  </tr>
  <tr>
    <td>&#38290;</td>
    <td>&amp; #38290;</td>
    <td>入力の難しい漢字(10進表記)</td>
  </tr>
  <tr>
    <td>&#x9DD7;</td>
    <td>&amp; #x9DD7;</td>
    <td>森鴎外の鴎の正字体(16進表記)</td>
  </tr>
</table>


