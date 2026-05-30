(function () {
  "use strict";

  var burger = document.querySelector(".nav-burger");
  var scrim = document.querySelector(".nav-scrim");
  var drawerClose = document.querySelector(".nav-drawer-close");
  var nav = document.getElementById("primary-navigation");

  if (!burger || !nav) return;

  function isDesktop() {
    return window.matchMedia("(min-width: 900px)").matches;
  }

  function setOpen(open) {
    document.body.classList.toggle("nav-open", open);
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open && !isDesktop() ? "hidden" : "";
    if (scrim) {
      scrim.setAttribute("aria-hidden", open ? "false" : "true");
    }
  }

  burger.addEventListener("click", function () {
    setOpen(!document.body.classList.contains("nav-open"));
  });

  if (scrim) {
    scrim.addEventListener("click", function () {
      setOpen(false);
    });
  }

  if (drawerClose) {
    drawerClose.addEventListener("click", function () {
      setOpen(false);
    });
  }

  nav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      setOpen(false);
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setOpen(false);
  });

  window.addEventListener("resize", function () {
    if (isDesktop()) setOpen(false);
  });
})();
