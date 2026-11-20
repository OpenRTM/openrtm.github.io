/* CSP-compatible initialization for the sidebar's Simple Jekyll Search. */
(function () {
  'use strict';

  function init() {
    var input = document.getElementById('sidebar-search-input');
    var results = document.getElementById('sidebar-results');
    if (!input || !results || window.__sidebarSearchInitialized) return;
    if (typeof window.SimpleJekyllSearch !== 'function') return;

    window.__sidebarSearchInitialized = true;
    window.SimpleJekyllSearch({
      searchInput: input,
      resultsContainer: results,
      json: input.getAttribute('data-search-json'),
      searchResultTemplate: '<li class="site-search__results"><a href="{url}">{title}</a></li>',
      noResultsText: '見つかりませんでした',
      limit: 10
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
