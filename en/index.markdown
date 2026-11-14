---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

#assets/rtm_images/rtm_logo.png

layout: home

title: "ホーム"
excerpt: "OpenRTM-aist | The power to connect"

swiper_images:
  - src: /assets/images/swiper/10min-startup_ja.png
    link: /ja/doc/installation/lets_start
  - src: /assets/images/swiper/rtm201_slider_re.png
    link: /ja/download
  - src: /assets/images/swiper/contest2026.png
    link: /ja/content/content/rtmcontest2026/
  - src: /assets/images/swiper/what_is_openrtm_ja2.jpg
    link: /ja/doc/aboutopenrtm/rtmiddleware
---

{% include top-swiper.html %}

<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  new Swiper('.top-swiper', {
    loop: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev'
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    }
  });
});
</script>

# News

<div class="news-grid">
  {% for post in site.posts limit: 6 %}
    <article class="news-item">
      <a href="{{ post.url | relative_url }}">
        {% if post.image %}
          <!-- div class="news-thumb">
          <img src="{{ post.image | relative_url }}" alt="">
          </div-->
            <div class="news-thumb">

            <div
              class="news-thumb-blur"
              style="background-image: url('{{ post.image | relative_url }}');">
            </div>

            <img
              src="{{ post.image | relative_url }}"
              alt="{{ post.title }}">
           </div>
        {% endif %}
      </a>
     <span class="news-date-wrap">
     <span class="news-date-day">{{ post.date | date: "%-d" }}</span>
     <span class="news-date">{{ post.date | date: " %b , %Y" }}</span>
     </span>
     <h4 class="news-title">
     <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
     </h4>
     <p class="top-news__excerpt">
              {{ post.excerpt | strip_html | truncate: 100 }}
     </p>
     <div class="news-more-wrap">
      <a class="news-more" href="{{ post.url | relative_url }}">続きを読む</a>
    </div>
    </article>
  {% endfor %}
</div>
<br>
<div class="news-more-wrap">
  <a class="news-more" href="{{ site.baseurl }}/ja/news/">その他のnews</a>
</div>
<hr>
<!-- /section -->

- [how to code]({{ site.baseurl }}/howto_code)
- [manual_md1]({{ site.baseurl }}/manual_md1)


<section class="partner-links">
  <div class="partner-links-grid">

    <a href="https://sice-si.org/rtsi/" class="partner-link-card" target="_blank" rel="noopener">
      <img src="{{ '/assets/images/partners/SI_LOGO.jpg' | relative_url }}"
           alt="SICE SI" width="80">
    </a>

    <a href="http://www.omg.or.jp/" class="partner-link-card" target="_blank" rel="noopener">
      <img src="{{ '/assets/images/partners/omg_member.png' | relative_url }}"
           alt="一般社団法人日本OMG" width="80">
    </a>

    <a href="https://rtc-fukushima.jp/" class="partner-link-card" target="_blank" rel="noopener">
      <img src="{{ '/assets/images/partners/rtc-Fukushima-logo.png' | relative_url }}"
           alt="RTC Fukushima" width="80">
    </a>

    <a href="https://www.openrtm.org/openrtm/ja/node/4599" class="partner-link-card" target="_blank" rel="noopener">
      <img src="{{ '/assets/images/partners/nedo_logo.png' | relative_url }}"
           alt="NEDO 次世代知能化技術開発" width="80">
    </a>

  </div>
</section>

