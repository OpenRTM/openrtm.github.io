/* Google Custom Search integration. Kept external for a strict script-src CSP. */
(function () {
  'use strict';
  var config = document.getElementById('openrtm-google-search-config');
  if (!config) return;

  var cx = config.getAttribute('data-search-engine-id');
  var instant = config.getAttribute('data-instant-search') === 'true';

  if (cx) {
    var gcse = document.createElement('script');
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + encodeURIComponent(cx);
    document.head.appendChild(gcse);
  }

  function executeSearch() {
    var input = document.getElementById('lwt-form-search-input');
    var search = window.google && window.google.search && window.google.search.cse;
    var element = search && search.element && search.element.getElement('searchresults-only0');
    if (!input || !element) return;
    if (input.value === '') element.clearAllResults();
    else element.execute(input.value);
  }

  document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('openrtm-google-search-form');
    if (!form) return;
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      executeSearch();
    });
    if (instant) {
      var input = document.getElementById('lwt-form-search-input');
      if (input) input.addEventListener('keyup', executeSearch);
    }
  });
}());
