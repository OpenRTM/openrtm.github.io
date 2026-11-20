/* Redirect the landing page to the visitor's preferred language. */
(function () {
  'use strict';
  var language = navigator.language || 'en';
  var target = language.toLowerCase().startsWith('ja') ? '/ja/' : '/en/';
  window.location.replace(target);
}());
