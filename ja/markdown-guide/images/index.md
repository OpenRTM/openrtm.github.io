---
layout: page
title: イメージ
---

#contents(4)

## 配置

### 左寄せする

```
 #ref(aist_name_png_47544.png, left)
```

![代替テキスト](./aist_name_png_47544.png)

<div align="left"><img src="aist_name_png_47544.png" width="300;" align="left"></div>

### センタリングする
```
 #ref(aist_name_png_47544.png, center)
```

<div align="center"><img src="aist_name_png_47544.png" width="300;"></div>

### 右寄せする
```
 #ref(aist_name_png_47544.png, right)
```

<div align="right"><img src="aist_name_png_47544.png" width="300;" align="right"></div>

## テキストまわりこませる
### 左寄せする
```
 #ref(aist_name_png_47544.png, around, left)
```

<div align="left"><img src="aist_name_png_47544.png" width="300;" align="left"></div>
ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ


### センタリングする
```
 #ref(aist_name_png_47544.png, around, center)
```

<div align="center"><img src="aist_name_png_47544.png" width="300;"></div>
ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ

### 右寄せする
```
 #ref(aist_name_png_47544.png, around, right)
```

<div align="right"><img src="aist_name_png_47544.png" width="300;" align="right"></a></div>
ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ

### まわりこみを解除する
```
 #clear
```

<div align="left"><img src="aist_name_png_47544.png" width="300;" align="left"></a></div>
あああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ
#clear
いいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいいい




## 拡大、縮小

### 原寸で表示する

※未確認

```
<div align="center"><img src="logo.png" width="100;"></div>
```

<div align="center"><img src="logo.png" width="100;"></div>


### ％で指定する
```
<div align="center"><img src="logo.png" width="20%;"></div>
```
<div align="center"><img src="logo.png" width="20%;"></div>

```
<div align="center"><img src="logo.png" width="150%;"></div>
```
<div align="center"><img src="logo.png" width="150%;"></div>


### ピクセルで指定する
※未確認

```
 #ref(logo.png, 20x20, wrap)
 #ref(logo.png, 100x100, wrap) 
 #ref(logo.png, 100x20, wrap) 
 #ref(logo.png, 20x100, wrap) 
```


<table class="table-alt">
  <tr>
    <th>20x20</th>
    <th>100x100</th>
    <th>100x20</th>
    <th>20x100</th>
  </tr>
  <tr>
    <td></td>
  </tr>
</table>
<div align="center"><a href="logo.png"><img src="logo.png" width="100;"></a></div> | 
<div align="center"><a href="logo.png"><img src="logo.png" width="100;"></a></div> |
<div align="center"><a href="logo.png"><img src="logo.png" width="100;"></a></div> |
<div align="center"><a href="logo.png"><img src="logo.png" width="100;"></a></div> |

<!-- | 20x20 | 100x100 | 100x20 | 20x100 | -->
<!-- | &ref(logo.png, 20x20, wrap); | &ref(logo.png, 100x100, wrap); | &ref(logo.png, 100x20, wrap); | &ref(logo.png, 20x100, wrap); | -->

## 枠、リンク (※ 未確認)
### イメージに枠を付ける


```
 #ref(aist_name_png_47544.png, wrap)
```

<div align="center"><a href="aist_name_png_47544.png"><img src="aist_name_png_47544.png" width="100;"></a></div>

### イメージに枠を付け無い

```
 #ref(aist_name_png_47544.png, nowrap)
```

<div align="center"><a href="aist_name_png_47544.png"><img src="aist_name_png_47544.png" width="100;"></a></div>

### イメージにリンクを付ける

```
 #ref(aist_name_png_47544.png)
```

<div align="center"><a href="aist_name_png_47544.png"><img src="aist_name_png_47544.png" width="100;"></a></div>

### イメージにリンクを付けない
```
 #ref(aist_name_png_47544.png, nolink)
```

<div align="center"><a href="aist_name_png_47544.png"><img src="aist_name_png_47544.png" width="100;"></a></div>



## イメージ展開の抑制

```
  &ref(aist_name_png_47544.png ,noimg);
```
  - <div align="center"><a href="aist_name_png_47544.png"><img src="aist_name_png_47544.png" width="100;"></a></div>;

## ファイルへのリンク
```
  &ref(http://www.openrtm.org/index.html);
```
  - <div align="center"><a href="http://www.openrtm.org/index.html"><img src="http://www.openrtm.org/index.html" width="100;"></a></div>;


## マージン
```
 #ref(aist_name_png_47544.png,margin=<上下マージン> <左右マージン>)
 または
 #ref(aist_name_png_47544.png,margin=<上下左右マージン>)
```


### マージンなし

```
 #ref(aist_name_png_47544.png,around,left)
```

<div align="left"><a href="aist_name_png_47544.png"><img src="aist_name_png_47544.png" width="100;" align="left"></a></div>
ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ


### 上下、左右別々のマージン

```
 #ref(aist_name_png_47544.png,around,margin=10 50,left)
```

<div align="left"><a href="aist_name_png_47544.png"><img src="aist_name_png_47544.png" width="100; margin:10 50px;" align="left"></a></div>
ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ


### 上下左右同じマージン

```
 #ref(aist_name_png_47544.png,around,margin=50,left)
```

<div align="left"><a href="aist_name_png_47544.png"><img src="aist_name_png_47544.png" width="100; margin:50px;" align="left"></a></div>
ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ

