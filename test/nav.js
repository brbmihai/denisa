(function () {
  var menuBtn = document.getElementById('nav-menu-btn');
  var sheet = document.getElementById('nav-sheet');
  if (!menuBtn || !sheet) return;

  var panel = sheet.querySelector('.nav-sheet-panel');
  var closeBtns = sheet.querySelectorAll('[data-nav-close]');
  var links = sheet.querySelectorAll('.nav-sheet-link');
  var lastFocus = null;

  function setOpen(open) {
    sheet.hidden = !open;
    sheet.dataset.open = open ? 'true' : 'false';
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.classList.toggle('nav-sheet-open', open);
    if (open) {
      lastFocus = document.activeElement;
      var first = sheet.querySelector('.nav-sheet-link');
      if (first) first.focus();
    } else if (lastFocus) {
      lastFocus.focus();
      lastFocus = null;
    }
  }

  menuBtn.addEventListener('click', function () {
    setOpen(sheet.hidden);
  });

  closeBtns.forEach(function (el) {
    el.addEventListener('click', function () {
      setOpen(false);
    });
  });

  links.forEach(function (link) {
    link.addEventListener('click', function () {
      setOpen(false);
    });
  });

  document.addEventListener('keydown', function (e) {
    if (sheet.hidden) return;
    if (e.key === 'Escape') {
      e.preventDefault();
      setOpen(false);
    }
  });
})();
