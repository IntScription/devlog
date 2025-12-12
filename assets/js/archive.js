(function() {
  'use strict';

  // Expand/Collapse All functionality
  const expandAllBtn = document.getElementById('expand-all');
  const collapseAllBtn = document.getElementById('collapse-all');
  const archiveSearch = document.getElementById('archive-search');
  const archiveYears = document.querySelectorAll('.archive-year');
  const archiveEntries = document.querySelectorAll('.archive-entry');

  if (expandAllBtn) {
    expandAllBtn.addEventListener('click', function() {
      archiveYears.forEach(function(details) {
        details.open = true;
        const summary = details.querySelector('summary');
        if (summary) summary.setAttribute('aria-expanded', 'true');
      });
    });
  }

  if (collapseAllBtn) {
    collapseAllBtn.addEventListener('click', function() {
      archiveYears.forEach(function(details) {
        details.open = false;
        const summary = details.querySelector('summary');
        if (summary) summary.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Update aria-expanded when details toggle
  archiveYears.forEach(function(details) {
    details.addEventListener('toggle', function() {
      const summary = this.querySelector('summary');
      if (summary) {
        summary.setAttribute('aria-expanded', this.open.toString());
      }
    });
  });

  // Search/Filter functionality
  if (archiveSearch) {
    archiveSearch.addEventListener('input', function(e) {
      const query = e.target.value.toLowerCase().trim();
      
      if (query === '') {
        // Show all entries
        archiveEntries.forEach(function(entry) {
          entry.style.display = '';
        });
        archiveYears.forEach(function(year) {
          year.style.display = '';
        });
        document.querySelectorAll('.archive-month').forEach(function(month) {
          month.style.display = '';
        });
        return;
      }

      let hasMatches = false;
      let visibleYears = new Set();
      let visibleMonths = new Set();

      archiveEntries.forEach(function(entry) {
        const date = entry.getAttribute('data-date') || '';
        const title = entry.getAttribute('data-title') || '';
        const link = entry.querySelector('.archive-link');
        const excerpt = link ? link.getAttribute('data-excerpt') || '' : '';
        
        const searchable = (date + ' ' + title + ' ' + excerpt).toLowerCase();
        
        if (searchable.includes(query)) {
          entry.style.display = '';
          hasMatches = true;
          // Track which year/month this entry belongs to
          const year = date.substring(0, 4);
          const month = date.substring(0, 7);
          visibleYears.add(year);
          visibleMonths.add(month);
        } else {
          entry.style.display = 'none';
        }
      });

      // Show/hide months based on visible entries
      document.querySelectorAll('.archive-month').forEach(function(month) {
        const monthKey = month.getAttribute('data-month');
        if (visibleMonths.has(monthKey)) {
          month.style.display = '';
        } else {
          month.style.display = 'none';
        }
      });

      // Show/hide years and expand if they have matches
      archiveYears.forEach(function(year) {
        const yearKey = year.getAttribute('data-year');
        if (visibleYears.has(yearKey)) {
          year.style.display = '';
          year.open = true; // Auto-expand years with matches
          const summary = year.querySelector('summary');
          if (summary) summary.setAttribute('aria-expanded', 'true');
        } else {
          year.style.display = 'none';
        }
      });
    });
  }

  // Hover preview tooltip
  const archiveLinks = document.querySelectorAll('.archive-link');
  let tooltip = null;

  archiveLinks.forEach(function(link) {
    link.addEventListener('mouseenter', function(e) {
      const excerpt = this.getAttribute('data-excerpt');
      if (!excerpt || excerpt.trim() === '') return;

      // Remove existing tooltip
      if (tooltip) {
        tooltip.remove();
      }

      tooltip = document.createElement('div');
      tooltip.className = 'archive-tooltip';
      tooltip.textContent = excerpt;
      document.body.appendChild(tooltip);

      const rect = this.getBoundingClientRect();
      tooltip.style.left = rect.left + 'px';
      tooltip.style.top = (rect.bottom + 8) + 'px';
      
      // Adjust if tooltip goes off screen
      setTimeout(function() {
        if (tooltip) {
          const tooltipRect = tooltip.getBoundingClientRect();
          if (tooltipRect.right > window.innerWidth) {
            tooltip.style.left = (window.innerWidth - tooltipRect.width - 16) + 'px';
          }
          if (tooltipRect.bottom > window.innerHeight) {
            tooltip.style.top = (rect.top - tooltipRect.height - 8) + 'px';
          }
        }
      }, 0);
    });

    link.addEventListener('mouseleave', function() {
      if (tooltip) {
        tooltip.remove();
        tooltip = null;
      }
    });
  });
})();
