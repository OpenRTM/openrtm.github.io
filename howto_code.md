---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

#assets/rtm_images/rtm_logo.png

layout: page
---



# もくじ

<div class="blog-post-toc m-1">
          {% include toc.html html=content %}
        </div>


[目次の入れ方参考](https://mssp160.netlify.app/2020-11/d5/)

# 引用

> ホゲホゲホゲ

# インラインコード
```python
def hello():
    print("Hello, world!")
```

```bash
$ bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_raspbian.sh)
echo "hogehoge"
```

```c++
# include <iostream>

int main() {
    using namespace std;

    cout << "Hello, World!" << endl;
    return 0;
}
```

```c
#include <stdio.h>

main()
{
  printf("Hello World\n");
}
```

```ruby
puts 'The best way to log and share programmers knowledge.'
```

`puts 'Qiita'` と書くことでインライン表示することも可能です。


|<img src="{{ site.baseurl }}/harumi2/image.png" width="30%">|<img src="{{ site.baseurl }}/harumi2/image.png" width="30%">|<img src="{{ site.baseurl }}/harumi2/image.png" width="30%">|
|:---|:---:|---:|
|hogehoge|ff|1|


# slideshareを表示する

{% include slideshare.html
   src="https://www.slideshare.net/slideshow/embed_code/key/rQEMftWXojYwnh"
%}

{% raw %}
```liquid
{% include slideshare.html
   src="https://www.slideshare.net/slideshow/embed_code/key/XXXX"
%}
```
{% endraw %}

# youtubeを表示する


<iframe width="560" height="315" src="https://www.youtube.com/embed/uPMIyC22--M" frameborder="0" allowfullscreen></iframe>

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/uPMIyC22--M" frameborder="0" allowfullscreen></iframe>
```

- [harumi2]({{ site.baseurl }}/harumi2)
- [harumi2]({{ site.baseurl }}/harumi2/harumi2)

- [test1]({{ site.baseurl }}/test1)
- [/test1/test]({{ site.baseurl }}/test1/test)

- [/harumi]({{ site.baseurl }}/harumi)
- [/harumi/harumi]({{ site.baseurl }}/harumi/harumi)

- [/harumi3]({{ site.baseurl }}/harumi3)
- [/harumi3_1]({{ site.baseurl }}/harumi3/harumi3_1)
- [/harumi3/harumi3]({{ site.baseurl }}/harumi3/harumi3)


<table class="table-alt">
<tr><th>コース名称</th><th width="200">YouTube</th><th width="200">レジュメ等</th></tr>

<tr>
　　<td><b><a href="/tutorials/01_01_intro">ROS体験コース</a></b><br/>インストー
ル不要で，USB一本とパソコンがあれば実行が可能なROS体験ツールを使った体験コースで
す。(<a href="/tutorials/01_01_intro">詳細ページへ</a>)</td>
    <td><div class="center"><a href="https://www.youtube.com/watch?v=mx1BE5LaDWk"><img src="/figs/youtube_button.png" height="64"></a></div></td>
    <td><div class="center"><a href="/tutorials/01_01_intro/01_01_intro.pdf"><img src="/figs/pdf_icon.png" height="64"></a></div></td>
</tr>





![hoge]({{ site.baseurl }}/harumi2/image.png)
<div align="center"><a href="{{ site.baseurl }}/harumi2"><img src="{{ site.baseurl }}/harumi2/image.png" width="30%"></a></div>
<br/>


# News...

inaba-test1
<hr>
{% for post in site.posts limit: 3 %}
  <article>
    <li>
      <a href="{{ post.url }}">
        <img src="{{post.image}}" alt="hogee" height="50" />
        <br>{{ post.title }} ({{post.date | date: "%B %-d, %Y"}})
      </a>
      <a>
        <br>{{ post.excerpt }}
      </a>
    </li>
  </article>
<hr>
{% endfor %}


# News...

inaba-test show list for post  auther=sharathdt

{% assign sorted-posts = site.posts | where: "author","sharathdt" %}
{% for post in sorted-posts limit: 5 %}
  <li>
    <a href="{{ post.url }}">
        {{post.title}}
    </a>
  </li>
{% endfor %}
