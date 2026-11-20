/* CSP-safe initialization for Jekyll Ideal Image Slider includes. */
(function () {
  'use strict';
  if (!window.IdealImageSlider || !window.IdealImageSlider.Slider) return;

  var keys = [
    'height', 'initialHeight', 'maxHeight', 'interval',
    'transitionDuration', 'effect', 'disableNav', 'keyboardNav',
    'previousNavSelector', 'nextNavSelector'
  ];

  function normalize(value) {
    // Existing sliders.yml stores some JavaScript string literals as "'fade'".
    if (typeof value === 'string' && value.length >= 2 &&
        ((value[0] === "'" && value[value.length - 1] === "'") ||
         (value[0] === '"' && value[value.length - 1] === '"'))) {
      return value.slice(1, -1);
    }
    return value;
  }

  document.querySelectorAll('[data-ideal-image-slider]').forEach(function (element) {
    if (element.dataset.iisInitialized === 'true') return;
    var settings = {};
    try {
      settings = JSON.parse(element.getAttribute('data-iis-settings') || '{}') || {};
    } catch (error) {
      console.error('Invalid Ideal Image Slider settings:', error);
      return;
    }
    var options = { selector: '#' + element.id };
    keys.forEach(function (key) {
      if (Object.prototype.hasOwnProperty.call(settings, key) &&
          settings[key] !== null && settings[key] !== '') {
        options[key] = normalize(settings[key]);
      }
    });
    var slider = new window.IdealImageSlider.Slider(options);
    if (element.getAttribute('data-iis-bullets') === 'true') slider.addBulletNav();
    if (element.getAttribute('data-iis-captions') === 'true') slider.addCaptions();
    slider.start();
    element.dataset.iisInitialized = 'true';
  });
}());
