---
layout: page
title: "News"
permalink: /en/news/
---

<ul class="news-archive">
  {% for post in site.posts %}
    <li class="news-archive__item">
      <span class="news-archive__date">
        {{ post.date | date: "%Y.%m.%d" }}
      </span>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
