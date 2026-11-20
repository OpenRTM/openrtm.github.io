/* CSP-safe initialization for the legacy /search_1 page. */
(function () {
  'use strict';
  function init() {
    var input = document.getElementById('search-input');
    var results = document.getElementById('results-container');
    if (!input || !results || typeof window.SimpleJekyllSearch !== 'function') return;
    window.SimpleJekyllSearch({
      searchInput: input,
      resultsContainer: results,
      json: '/search.json',
      searchResultTemplate: '<li><a href="{url}">{title}</a></li>',
      noResultsText: '見つかりませんでした'
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
