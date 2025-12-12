(function() {
  'use strict';

  // Back to top button
  const backToTopBtn = document.getElementById('back-to-top');
  
  if (backToTopBtn) {
    // Show/hide button based on scroll position
    function toggleBackToTop() {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add('visible');
        backToTopBtn.setAttribute('aria-hidden', 'false');
      } else {
        backToTopBtn.classList.remove('visible');
        backToTopBtn.setAttribute('aria-hidden', 'true');
      }
    }

    window.addEventListener('scroll', toggleBackToTop);
    toggleBackToTop(); // Check initial state

    // Smooth scroll to top
    backToTopBtn.addEventListener('click', function() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
      backToTopBtn.blur(); // Remove focus after click
    });
  }

  // Keyboard navigation (j/k for next/previous)
  // Works on archive pages and individual log pages
  if (window.location.pathname.includes('/archive/') || window.location.pathname.includes('/logs/')) {
    let logLinks = [];
    
    // Get all log entry links from archive
    const archiveLinks = document.querySelectorAll('.archive-link');
    const navLinks = document.querySelectorAll('.log-backlinks a[rel="prev"], .log-backlinks a[rel="next"]');
    
    if (archiveLinks.length > 0) {
      // On archive page, collect all log links
      logLinks = Array.from(archiveLinks).map(function(link) {
        return link.href;
      });
    } else if (navLinks.length > 0) {
      // On a log page, use prev/next links
      navLinks.forEach(function(link) {
        if (link.rel === 'prev' || link.rel === 'next') {
          logLinks.push(link.href);
        }
      });
    }

    // Get current page URL
    const currentUrl = window.location.href;

    if (logLinks.length > 0) {
      document.addEventListener('keydown', function(e) {
        // Only handle j/k if not typing in an input/textarea
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable) {
          return;
        }

        if (e.key === 'j' || e.key === 'J') {
          e.preventDefault();
          // Find next log entry
          const currentIndex = logLinks.indexOf(currentUrl);
          if (currentIndex >= 0 && currentIndex < logLinks.length - 1) {
            window.location.href = logLinks[currentIndex + 1];
          } else if (logLinks.length > 0 && currentIndex === -1) {
            // If not found, go to first
            window.location.href = logLinks[0];
          }
        } else if (e.key === 'k' || e.key === 'K') {
          e.preventDefault();
          // Find previous log entry
          const currentIndex = logLinks.indexOf(currentUrl);
          if (currentIndex > 0) {
            window.location.href = logLinks[currentIndex - 1];
          } else if (logLinks.length > 0 && currentIndex === -1) {
            // If not found, go to last
            window.location.href = logLinks[logLinks.length - 1];
          }
        }
      });

      // Show keyboard hint on first visit (only on archive or log pages)
      if (!localStorage.getItem('keyboard-nav-hint-shown')) {
        const hint = document.createElement('div');
        hint.className = 'keyboard-hint';
        if (window.location.pathname.includes('/archive/')) {
          hint.innerHTML = '💡 Tip: Press <kbd>J</kbd> for next, <kbd>K</kbd> for previous entry';
        } else {
          hint.innerHTML = '💡 Tip: Press <kbd>J</kbd> for next, <kbd>K</kbd> for previous entry';
        }
        hint.setAttribute('role', 'status');
        hint.setAttribute('aria-live', 'polite');
        document.body.appendChild(hint);
        
        setTimeout(function() {
          hint.classList.add('fade-out');
          setTimeout(function() {
            hint.remove();
          }, 500);
        }, 5000);
        
        localStorage.setItem('keyboard-nav-hint-shown', 'true');
      }
    }
  }
})();
