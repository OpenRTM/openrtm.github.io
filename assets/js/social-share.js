/* CSP-safe social sharing popup handler. */
document.addEventListener('click', function (event) {
  var link = event.target.closest('a[data-share-popup="true"]');
  if (!link) return;
  var popup = window.open(link.href, 'window', 'left=20,top=20,width=500,height=500,toolbar=1,resizable=0');
  if (popup) event.preventDefault();
});
