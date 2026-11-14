---
layout: page
title: "search"
permalink: /search_1
---
hoge

<input type="text" id="search-input" placeholder="検索..." />
<ul id="results-container"></ul>

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('results-container'),
  json: '{{ "/search.json" | relative_url }}',
  searchResultTemplate: '<li><a href="{url}">{title}</a></li>',
  noResultsText: '見つかりませんでした'
});
</script>
