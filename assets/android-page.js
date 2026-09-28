(function () {
  const root = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  const english = root.lang === 'en';
  if (english) {
    try {
      if (!localStorage.getItem('easyhub-site-language')) localStorage.setItem('easyhub-site-language', 'en');
    } catch (_) { /* storage may be disabled */ }
  }

  function updateToggle() {
    const dark = root.dataset.theme === 'dark';
    const label = english
      ? (dark ? 'Switch to light mode' : 'Switch to dark mode')
      : (dark ? '切换到浅色模式' : '切换到深色模式');
    toggle.setAttribute('aria-label', label);
    toggle.setAttribute('title', label);
    toggle.setAttribute('aria-pressed', String(dark));
  }

  toggle.addEventListener('click', function () {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('easyhub-site-theme', next); } catch (_) { /* storage may be disabled */ }
    updateToggle();
  });

  const darkQuery = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)');
  if (darkQuery) darkQuery.addEventListener('change', function (event) {
    let saved = '';
    try { saved = localStorage.getItem('easyhub-site-theme') || ''; } catch (_) { /* storage may be disabled */ }
    if (saved !== 'light' && saved !== 'dark') {
      root.dataset.theme = event.matches ? 'dark' : 'light';
      updateToggle();
    }
  });
  updateToggle();

  document.querySelectorAll('.language-switch a[data-lang]').forEach(function (link) {
    link.addEventListener('click', function () {
      try { localStorage.setItem('easyhub-site-language', link.dataset.lang); } catch (_) { /* storage may be disabled */ }
    });
  });

  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && root.classList.contains('motion-ready')) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -25px 0px' });
    reveals.forEach(function (element) { observer.observe(element); });
    window.addEventListener('load', function () {
      setTimeout(function () { reveals.forEach(function (element) { element.classList.add('in'); }); }, 2600);
    });
  } else {
    reveals.forEach(function (element) { element.classList.add('in'); });
  }
})();
