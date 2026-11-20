(function () {
  var b = document.querySelector('.burger'), n = document.getElementById('nav');
  if (b && n) {
    b.addEventListener('click', function () {
      var open = n.classList.toggle('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    n.addEventListener('click', function (e) {
      if (e.target.closest('a')) { n.classList.remove('open'); b.setAttribute('aria-expanded', 'false'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && n.classList.contains('open')) { n.classList.remove('open'); b.setAttribute('aria-expanded', 'false'); b.focus(); }
    });
  }
  var y = document.getElementById('yr');
  if (y) y.textContent = new Date().getFullYear();
})();
