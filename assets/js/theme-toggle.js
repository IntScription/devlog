(function() {
  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  if (!toggle) return;
  const iconSpan = toggle.querySelector('.theme-icon');
  const sun = `<svg width='22' height='22' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='5'/><path d='M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42'/></svg>`;
  const moon = `<svg width='22' height='22' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M21 12.79A9 9 0 1111.21 3a7 7 0 109.79 9.79z'/></svg>`;

  function setTheme(mode) {
    if (mode === 'light') {
      root.setAttribute('data-theme', 'light');
      iconSpan.innerHTML = moon;
    } else {
      root.setAttribute('data-theme', 'dark');
      iconSpan.innerHTML = sun;
    }
  }

  // Initial theme
  let theme = localStorage.getItem('theme');
  if (!theme) {
    theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  setTheme(theme);

  toggle.addEventListener('click', function() {
    theme = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    setTheme(theme);
    localStorage.setItem('theme', theme);
  });
})(); 