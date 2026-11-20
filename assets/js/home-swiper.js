/* Shared home-page Swiper initialization, externalized for CSP. */
document.addEventListener('DOMContentLoaded', function () {
  if (typeof window.Swiper !== 'function') return;
  var slider = document.querySelector('.top-swiper');
  if (!slider) return;
  new window.Swiper(slider, {
    loop: true,
    autoplay: { delay: 4000, disableOnInteraction: false },
    navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
    pagination: { el: '.swiper-pagination', clickable: true }
  });
});
