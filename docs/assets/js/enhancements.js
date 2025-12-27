/**
 * Site Enhancements for Agentic AI Course
 * Features: Code copy, keyboard shortcuts, TOC, reading time, progress tracking
 */

(function() {
  'use strict';

  // ========================================
  // Code Copy Buttons (#220)
  // ========================================
  function addCodeCopyButtons() {
    document.querySelectorAll('pre code').forEach(function(codeBlock) {
      const pre = codeBlock.parentNode;
      if (pre.querySelector('.copy-btn')) return;

      const btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.textContent = 'Copy';
      btn.setAttribute('aria-label', 'Copy code to clipboard');

      btn.addEventListener('click', function() {
        navigator.clipboard.writeText(codeBlock.textContent).then(function() {
          btn.textContent = 'Copied!';
          btn.classList.add('copied');
          setTimeout(function() {
            btn.textContent = 'Copy';
            btn.classList.remove('copied');
          }, 2000);
        });
      });

      pre.style.position = 'relative';
      pre.appendChild(btn);
    });
  }

  // ========================================
  // Keyboard Shortcuts (#223)
  // ========================================
  function initKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
      // Cmd/Ctrl + K: Focus search
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.querySelector('.search-input, #search-input, input[type="search"]');
        if (searchInput) searchInput.focus();
      }

      // Arrow keys for week navigation (when not in input)
      if (document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        if (e.key === 'ArrowLeft') {
          const prevLink = document.querySelector('a[href*="week-"]:has(+ .current), .week-nav a:first-child');
          const prev = document.querySelector('.btn-outline[href*="Previous"], a[href*="minus: 1"]');
          if (prev) prev.click();
        }
        if (e.key === 'ArrowRight') {
          const next = document.querySelector('.btn-outline[href*="Next"], a[href*="plus: 1"]');
          if (next) next.click();
        }
      }

      // ? for help overlay
      if (e.key === '?' && !e.metaKey && !e.ctrlKey) {
        if (document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
          toggleShortcutsHelp();
        }
      }

      // Escape to close overlays
      if (e.key === 'Escape') {
        const overlay = document.querySelector('.shortcuts-overlay');
        if (overlay) overlay.remove();
      }
    });
  }

  function toggleShortcutsHelp() {
    let overlay = document.querySelector('.shortcuts-overlay');
    if (overlay) {
      overlay.remove();
      return;
    }

    overlay = document.createElement('div');
    overlay.className = 'shortcuts-overlay';
    overlay.innerHTML = `
      <div class="shortcuts-modal">
        <h3>Keyboard Shortcuts</h3>
        <table>
          <tr><td><kbd>Ctrl/Cmd</kbd> + <kbd>K</kbd></td><td>Focus search</td></tr>
          <tr><td><kbd>Left Arrow</kbd></td><td>Previous week</td></tr>
          <tr><td><kbd>Right Arrow</kbd></td><td>Next week</td></tr>
          <tr><td><kbd>?</kbd></td><td>Show this help</td></tr>
          <tr><td><kbd>Esc</kbd></td><td>Close overlay</td></tr>
        </table>
        <button onclick="this.parentNode.parentNode.remove()">Close</button>
      </div>
    `;
    document.body.appendChild(overlay);
  }

  // ========================================
  // Auto Table of Contents (#224)
  // ========================================
  function generateTOC() {
    const content = document.querySelector('.main-content, main, article');
    if (!content) return;

    const headings = content.querySelectorAll('h2, h3');
    if (headings.length < 3) return;

    const existingTOC = document.querySelector('.auto-toc');
    if (existingTOC) return;

    const toc = document.createElement('nav');
    toc.className = 'auto-toc';
    toc.setAttribute('aria-label', 'Table of contents');

    const title = document.createElement('h4');
    title.textContent = 'On this page';
    toc.appendChild(title);

    const list = document.createElement('ul');
    headings.forEach(function(heading, index) {
      if (!heading.id) {
        heading.id = 'heading-' + index;
      }

      const li = document.createElement('li');
      li.className = heading.tagName.toLowerCase();

      const link = document.createElement('a');
      link.href = '#' + heading.id;
      link.textContent = heading.textContent;
      li.appendChild(link);
      list.appendChild(li);
    });

    toc.appendChild(list);

    // Insert after first h1 or at top of content
    const h1 = content.querySelector('h1');
    if (h1 && h1.nextSibling) {
      h1.parentNode.insertBefore(toc, h1.nextSibling);
    }
  }

  // ========================================
  // Estimated Reading Time (#221)
  // ========================================
  function addReadingTime() {
    const content = document.querySelector('.main-content, main, article');
    if (!content) return;

    const text = content.textContent || '';
    const wordCount = text.trim().split(/\s+/).length;
    const readingTime = Math.ceil(wordCount / 200);

    const h1 = content.querySelector('h1');
    if (!h1 || h1.querySelector('.reading-time')) return;

    const badge = document.createElement('span');
    badge.className = 'reading-time';
    badge.textContent = readingTime + ' min read';
    badge.style.cssText = 'font-size: 0.8rem; color: #666; margin-left: 1rem; font-weight: normal;';
    h1.appendChild(badge);
  }

  // ========================================
  // Course Progress Tracking (#218)
  // ========================================
  function initProgressTracking() {
    // Track page visits
    const path = window.location.pathname;
    const visited = JSON.parse(localStorage.getItem('visited-pages') || '[]');

    if (!visited.includes(path)) {
      visited.push(path);
      localStorage.setItem('visited-pages', JSON.stringify(visited));
    }

    // Mark visited links
    document.querySelectorAll('a[href*="/weeks/week-"]').forEach(function(link) {
      const href = new URL(link.href, window.location.origin).pathname;
      if (visited.includes(href)) {
        link.classList.add('visited-page');
      }
    });
  }

  // ========================================
  // Last Updated Timestamps (#226)
  // ========================================
  function showLastUpdated() {
    const footer = document.querySelector('footer, .site-footer');
    if (!footer || footer.querySelector('.last-updated')) return;

    const lastMod = document.lastModified;
    if (lastMod) {
      const date = new Date(lastMod);
      const formatted = date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      });

      const span = document.createElement('span');
      span.className = 'last-updated';
      span.textContent = 'Last updated: ' + formatted;
      span.style.cssText = 'display: block; font-size: 0.8rem; color: #666; margin-top: 0.5rem;';
      footer.appendChild(span);
    }
  }

  // ========================================
  // Mobile Navigation Enhancement (#225)
  // ========================================
  function enhanceMobileNav() {
    // Add swipe gestures for week navigation
    let touchStartX = 0;
    let touchEndX = 0;

    document.addEventListener('touchstart', function(e) {
      touchStartX = e.changedTouches[0].screenX;
    }, false);

    document.addEventListener('touchend', function(e) {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, false);

    function handleSwipe() {
      const diff = touchStartX - touchEndX;
      if (Math.abs(diff) < 50) return;

      if (diff > 0) {
        // Swipe left - next
        const next = document.querySelector('a[href*="plus: 1"], .btn-outline[href*="Next"]');
        if (next) next.click();
      } else {
        // Swipe right - previous
        const prev = document.querySelector('a[href*="minus: 1"], .btn-outline[href*="Previous"]');
        if (prev) prev.click();
      }
    }
  }

  // ========================================
  // CSS Styles
  // ========================================
  function addStyles() {
    const style = document.createElement('style');
    style.textContent = `
      /* Code Copy Button */
      .copy-btn {
        position: absolute;
        top: 0.5rem;
        right: 0.5rem;
        padding: 0.25rem 0.5rem;
        font-size: 0.75rem;
        background: #e9ecef;
        border: 1px solid #ddd;
        border-radius: 4px;
        cursor: pointer;
        opacity: 0;
        transition: opacity 0.2s;
      }
      pre:hover .copy-btn { opacity: 1; }
      .copy-btn.copied { background: #2CA02C; color: white; border-color: #2CA02C; }

      /* Shortcuts Overlay */
      .shortcuts-overlay {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0,0,0,0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
      }
      .shortcuts-modal {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        max-width: 400px;
      }
      .shortcuts-modal table { width: 100%; margin: 1rem 0; }
      .shortcuts-modal td { padding: 0.5rem; }
      .shortcuts-modal kbd {
        background: #e9ecef;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        font-family: monospace;
      }
      .shortcuts-modal button {
        padding: 0.5rem 1rem;
        background: #0066CC;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }

      /* Auto TOC */
      .auto-toc {
        background: var(--bg-secondary, #f8f9fa);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #3333B2;
      }
      .auto-toc h4 { margin: 0 0 0.5rem 0; font-size: 0.9rem; }
      .auto-toc ul { margin: 0; padding-left: 1rem; list-style: none; }
      .auto-toc li { margin: 0.25rem 0; }
      .auto-toc li.h3 { margin-left: 1rem; }
      .auto-toc a { color: #666; text-decoration: none; font-size: 0.85rem; }
      .auto-toc a:hover { color: #0066CC; }

      /* Visited pages */
      .visited-page::after {
        content: ' ✓';
        color: #2CA02C;
        font-size: 0.8em;
      }

      /* Dark mode adjustments */
      [data-theme="dark"] .shortcuts-modal { background: #1e1e1e; color: #fff; }
      [data-theme="dark"] .shortcuts-modal kbd { background: #333; }
      [data-theme="dark"] .copy-btn { background: #333; border-color: #444; color: #fff; }
    `;
    document.head.appendChild(style);
  }

  // ========================================
  // Initialize All
  // ========================================
  function init() {
    addStyles();
    addCodeCopyButtons();
    initKeyboardShortcuts();
    generateTOC();
    addReadingTime();
    initProgressTracking();
    showLastUpdated();
    enhanceMobileNav();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
